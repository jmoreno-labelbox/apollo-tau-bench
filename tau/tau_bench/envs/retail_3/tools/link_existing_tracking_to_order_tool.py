from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class LinkExistingTrackingToOrderTool(Tool):
    """
    Associate an existing tracking record with an order by creating a fulfillment entry.

    Behavior:
    - Confirms the order exists.
    - Checks that the tracking_id is present in tracking.json (within any record's 'tracking_id' list).
    - Adds a fulfillment entry to the order containing at least:
        { "status": "linked", "tracking_id": "<id>", "timestamp": "UTC ISO" }
      Optionally includes 'courier' if available in the tracking record.

    Input (kwargs):
        order_id (str, required)
        tracking_id (str, required)

    Output:
        JSON string with {"order_id","tracking_id","fulfillments_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, tracking_id: str = None) -> str:
        if not order_id or not tracking_id:
            payload = {"error": "order_id and tracking_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        orders = data.get("orders", {}).values()
        order = next((o for o in orders.values() if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        tracking = data.get("tracking", {}).values()
        tr = next(
            (t for t in tracking.values() if tracking_id in (t.get("tracking_id") or [])), None
        )
        if not tr:
            payload = {"error": f"tracking_id '{tracking_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        fulfillment = {
            "status": "linked",
            "tracking_id": tracking_id,
            "timestamp": _now_iso(),
        }
        if tr.get("courier_name"):
            fulfillment["courier"] = tr["courier_name"]

        order.setdefault("fulfillments", []).append(fulfillment)
        payload = {
                "order_id": order_id,
                "tracking_id": tracking_id,
                "fulfillments_len": len(order.get("fulfillments", [])),
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
                "name": "LinkExistingTrackingToOrder",
                "description": "Link an existing tracking_id from tracking.json to an order by appending a fulfillment entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "tracking_id": {"type": "string"},
                    },
                    "required": ["order_id", "tracking_id"],
                },
            },
        }
