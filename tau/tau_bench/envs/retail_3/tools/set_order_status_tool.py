# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetOrderStatusTool(Tool):
    """
    Set or override an order's status in orders.json.

    Behavior:
    - Validates the order exists.
    - Sets order['status'] = provided value.
    - Does not modify fulfillments or payment_history.

    Input (kwargs):
        order_id (str, required)
        status (str, required)  # e.g., "pending", "fulfilled", "completed", "cancelled"

    Output:
        JSON string with {"order_id","status"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        status = kwargs.get("status")

        if not order_id or not isinstance(status, str) or not status:
            return json.dumps({"error": "order_id and non-empty status are required"}, indent=2)

        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        order["status"] = status
        return json.dumps({"order_id": order_id, "status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_order_status",
                "description": "Set or override the 'status' field of an existing order (orders.json).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["order_id", "status"],
                },
            },
        }
