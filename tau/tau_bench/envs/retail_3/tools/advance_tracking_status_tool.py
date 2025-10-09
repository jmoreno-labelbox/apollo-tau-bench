from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class AdvanceTrackingStatusTool(Tool):
    """
    Update the tracking status for an order in tracking.json and reflect the change in orders.json.

    Behavior:
    - Confirms that the specified tracking_id exists in tracking.json.
    - Adds a new status entry to status_history.
    - If order_status is provided, also adds a fulfillment update to the order.
      Suggested status progression: label_created -> shipped -> in_transit -> out_for_delivery -> delivered.
    - If status == "delivered", optionally set order.status = "completed".

    Input (kwargs):
        tracking_id (str, required)
        status (str, required)              # e.g., "shipped", "delivered", etc.
        order_status (str, optional)        # e.g., "fulfilled", "completed"

    Output:
        JSON string with {"tracking_id","new_status","history_len"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None, status: str = None, order_status: str = None) -> str:
        if not tracking_id or not status:
            payload = {"error": "tracking_id and status are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        tracking = data.get("tracking", [])
        tr = next(
            (t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None
        )
        if not tr:
            payload = {"error": f"tracking_id '{tracking_id}' not found in tracking.json"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Verify that tracking_history is present prior to adding
        if "tracking_history" not in tr:
            tr["tracking_history"] = {}

        tr["tracking_history"][status] = _now_iso()

        # Replicate into orders.json if relevant
        orders = data.get("orders", [])
        order = next(
            (o for o in orders if o.get("order_id") == tr.get("order_id")), None
        )
        if order:
            if "fulfillments" not in order:
                order["fulfillments"] = []

            order["fulfillments"].append(
                {
                    "status": status,
                    "tracking_id": tracking_id,
                    "timestamp": _now_iso(),
                }
            )
            if status == "delivered":
                order["status"] = "completed"
            if order_status:
                order["status"] = order_status
        payload = {
                "tracking_id": tracking_id,
                "new_status": status,
                "history_len": len(tr["tracking_history"]),
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
                "name": "AdvanceTrackingStatus",
                "description": "Append a new tracking status and optionally update the order status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "status": {"type": "string"},
                        "order_status": {
                            "type": "string",
                            "description": "Optional order status to set.",
                        },
                    },
                    "required": ["tracking_id", "status"],
                },
            },
        }
