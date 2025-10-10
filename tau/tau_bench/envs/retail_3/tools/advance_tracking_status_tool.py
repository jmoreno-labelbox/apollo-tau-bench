# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AdvanceTrackingStatusTool(Tool):
    """
    Advance tracking status for an order in tracking.json and mirror the change to orders.json.

    Behavior:
    - Validates that the given tracking_id exists in tracking.json.
    - Appends a new status entry into status_history.
    - If provided with order_status, also appends a fulfillment update on the order.
      Suggested status flow: label_created -> shipped -> in_transit -> out_for_delivery -> delivered.
    - If status == "delivered", optionally mark order.status = "completed".

    Input (kwargs):
        tracking_id (str, required)
        status (str, required)              # e.g., "shipped", "delivered", etc.
        order_status (str, optional)        # e.g., "fulfilled", "completed"

    Output:
        JSON string with {"tracking_id","new_status","history_len"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tracking_id = kwargs.get("tracking_id")
        status = kwargs.get("status")
        order_status = kwargs.get("order_status")

        if not tracking_id or not status:
            return json.dumps({"error": "tracking_id and status are required"}, indent=2)

        tracking = data.get("tracking", [])
        tr = next((t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None)
        if not tr:
            return json.dumps(
                {"error": f"tracking_id '{tracking_id}' not found in tracking.json"},
                indent=2,
            )

        # Ensure tracking_history exists before appending
        if "tracking_history" not in tr:
            tr["tracking_history"] = {}

        tr["tracking_history"][status] = _now_iso()

        # Mirror into orders.json if applicable
        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if o.get("order_id") == tr.get("order_id")), None)
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

        return json.dumps(
            {
                "tracking_id": tracking_id,
                "new_status": status,
                "history_len": len(tr["tracking_history"]),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "advance_tracking_status",
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
