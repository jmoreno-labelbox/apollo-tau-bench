# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkExistingTrackingToOrderTool(Tool):
    """
    Link an existing tracking record to an order by creating a fulfillment entry.

    Behavior:
    - Validates the order exists.
    - Validates that the tracking_id exists in tracking.json (under any record's 'tracking_id' list).
    - Appends a fulfillment entry on the order containing at least:
        { "status": "linked", "tracking_id": "<id>", "timestamp": "UTC ISO" }
      Optionally includes 'courier' if found on the tracking record.

    Input (kwargs):
        order_id (str, required)
        tracking_id (str, required)

    Output:
        JSON string with {"order_id","tracking_id","fulfillments_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        tracking_id = kwargs.get("tracking_id")

        if not order_id or not tracking_id:
            return json.dumps({"error": "order_id and tracking_id are required"}, indent=2)

        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        tracking = data.get("tracking", [])
        tr = next((t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None)
        if not tr:
            return json.dumps({"error": f"tracking_id '{tracking_id}' not found"}, indent=2)

        fulfillment = {
            "status": "linked",
            "tracking_id": tracking_id,
            "timestamp": _now_iso(),
        }
        if tr.get("courier_name"):
            fulfillment["courier"] = tr["courier_name"]

        order.setdefault("fulfillments", []).append(fulfillment)

        return json.dumps(
            {
                "order_id": order_id,
                "tracking_id": tracking_id,
                "fulfillments_len": len(order.get("fulfillments", [])),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_existing_tracking_to_order",
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
