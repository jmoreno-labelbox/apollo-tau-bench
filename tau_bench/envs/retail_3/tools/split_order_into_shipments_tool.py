from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class SplitOrderIntoShipmentsTool(Tool):
    """
    Divide an order's items into several shipments, generating tracking and fulfillments.

    Behavior:
    - Confirms the order exists.
    - For each shipment entry, requires 'indices' (0-based positions in order.items)
      and a 'courier_name' to generate a tracking record.
    - Creates one tracking record for each shipment and adds corresponding fulfillment
      entries to the order. Items are not deleted; this function only generates logistics records.

    Input (kwargs):
        order_id (str, required)
        shipments (List[dict], required): each with
            - indices: List[int]  # positions within order['items']
            - courier_name: str

    Output:
        JSON string with {"order_id","created_trackings":[{"courier_name","tracking_id","count"}], "shipments_count"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, shipments: list = None) -> str:
        if not order_id or not isinstance(shipments, list) or not shipments:
            payload = {"error": "order_id and non-empty shipments are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        couriers = data.get("couriers", [])
        tracking_db = data.get("tracking", [])
        items_len = len(order.get("items", []))
        created = []

        used_tracking_ids = {
            tid for t in tracking_db for tid in t.get("tracking_id", [])
        }

        for sh in shipments:
            idxs = sh.get("indices")
            courier_name = sh.get("courier_name")
            if not isinstance(idxs, list) or not idxs or not courier_name:
                payload = {
                        "error": "each shipment requires 'indices' (list) and 'courier_name'"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            #check that indices are within the valid range
            valid = [
                i
                for i in {int(i) for i in idxs if isinstance(i, (int, float))}
                if 0 <= i < items_len
            ]
            if not valid:
                payload = {"error": f"shipment has no valid indices within 0..{items_len-1}"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            #locate courier
            courier = next((c for c in couriers if c.get("name") == courier_name), None)
            if not courier:
                payload = {"error": f"courier '{courier_name}' not found"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

            #select the first available tracking id
            tid = next(
                (
                    tid
                    for tid in courier.get("tracking_ids", [])
                    if tid not in used_tracking_ids
                ),
                None,
            )
            if not tid:
                payload = {"error": f"No available tracking_id for courier '{courier_name}'"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            used_tracking_ids.add(tid)

            #generate tracking record
            tracking_db.append(
                {
                    "tracking_id": [tid],
                    "order_id": order_id,
                    "courier_name": courier_name,
                    "status_history": [
                        {"status": "label_created", "timestamp": _now_iso()}
                    ],
                }
            )

            #add fulfillment to the order
            (order.setdefault("fulfillments", [])).append(
                {
                    "status": "label_created",
                    "tracking_id": tid,
                    "courier": courier_name,
                    "timestamp": _now_iso(),
                    "items_indices": sorted(valid),
                }
            )

            created.append(
                {"courier_name": courier_name, "tracking_id": tid, "count": len(valid)}
            )
        payload = {
                "order_id": order_id,
                "created_trackings": created,
                "shipments_count": len(created),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "splitOrderIntoShipments",
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
