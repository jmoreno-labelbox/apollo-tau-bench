# Sierra Copyright

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _now_iso() -> str:
    """Return current UTC timestamp in ISO format (seconds precision)."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"

class SplitOrderIntoShipmentsTool(Tool):
    """
    Split an order's items into multiple shipments, creating tracking and fulfillments.

    Behavior:
    - Validates order exists.
    - For each shipment entry, requires 'indices' (0-based positions in order.items)
      and a 'courier_name' to create a tracking record.
    - Creates one tracking record per shipment and appends corresponding fulfillment
      entries to the order. Items are not removed; this tool only creates logistics records.

    Input (kwargs):
        order_id (str, required)
        shipments (List[dict], required): each with
            - indices: List[int]  # indexes in order['items']
            - courier_name: str

    Output:
        JSON string with {"order_id","created_trackings":[{"courier_name","tracking_id","count"}], "shipments_count"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], order_id, shipments) -> str:

        if not order_id or not isinstance(shipments, list) or not shipments:
            return json.dumps({"error": "order_id and non-empty shipments are required"}, indent=2)

        orders = list(list(list(data.get("orders", {}).values())) if isinstance(data.get("orders"), dict) else data.get("orders", []))
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        couriers = data.get("couriers", [])
        tracking_db = data.get("tracking", [])
        items_len = len(order.get("items", []))
        created = []

        used_tracking_ids = {tid for t in tracking_db for tid in t.get("tracking_id", [])}

        for sh in shipments:
            idxs = sh.get("indices")
            courier_name = sh.get("courier_name")
            if not isinstance(idxs, list) or not idxs or not courier_name:
                return json.dumps(
                    {"error": "each shipment requires 'indices' (list) and 'courier_name'"},
                    indent=2,
                )

            # check if indices are within the valid range
            valid = [
                i
                for i in set(int(i) for i in idxs if isinstance(i, (int, float)))
                if 0 <= i < items_len
            ]
            if not valid:
                return json.dumps(
                    {"error": f"shipment has no valid indices within 0..{items_len-1}"},
                    indent=2,
                )

            # locate courier
            courier = next((c for c in couriers if c.get("name") == courier_name), None)
            if not courier:
                return json.dumps({"error": f"courier '{courier_name}' not found"}, indent=2)

            # select the initial available tracking ID
            tid = next(
                (tid for tid in courier.get("tracking_ids", []) if tid not in used_tracking_ids),
                None,
            )
            if not tid:
                return json.dumps(
                    {"error": f"No available tracking_id for courier '{courier_name}'"},
                    indent=2,
                )

            used_tracking_ids.add(tid)

            # generate tracking record
            tracking_db.append(
                {
                    "tracking_id": [tid],
                    "order_id": order_id,
                    "courier_name": courier_name,
                    "status_history": [{"status": "label_created", "timestamp": _now_iso()}],
                }
            )

            # add fulfillment to the order
            (order.setdefault("fulfillments", [])).append(
                {
                    "status": "label_created",
                    "tracking_id": tid,
                    "courier": courier_name,
                    "timestamp": _now_iso(),
                    "items_indices": sorted(valid),
                }
            )

            created.append({"courier_name": courier_name, "tracking_id": tid, "count": len(valid)})

        return json.dumps(
            {
                "order_id": order_id,
                "created_trackings": created,
                "shipments_count": len(created),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "split_order_into_shipments",
                "description": "Create multiple shipments for an order by indices and courier, generating tracking and fulfillment entries.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "shipments": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "indices": {
                                        "type": "array",
                                        "items": {"type": "integer", "minimum": 0},
                                    },
                                    "courier_name": {"type": "string"},
                                },
                                "required": ["indices", "courier_name"],
                            },
                        },
                    },
                    "required": ["order_id", "shipments"],
                },
            },
        }