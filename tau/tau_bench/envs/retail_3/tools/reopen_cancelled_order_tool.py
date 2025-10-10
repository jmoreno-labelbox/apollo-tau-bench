# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReopenCancelledOrderTool(Tool):
    """
    Reopen a previously cancelled order by setting status back to 'pending'.

    Behavior:
    - Validates order exists and is currently 'cancelled'.
    - Sets order['status'] = 'pending'.
    - Does not modify items, payment_history, or fulfillments.

    Input (kwargs):
        order_id (str, required)

    Output:
        JSON string with {"order_id","status"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], order_id) -> str:
        if not order_id:
            return json.dumps({"error": "order_id is required"}, indent=2)

        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        if order.get("status") != "cancelled":
            return json.dumps(
                {"error": f"order status must be 'cancelled', found '{order.get('status')}'"},
                indent=2,
            )

        order["status"] = "pending"

        return json.dumps({"order_id": order_id, "status": "pending"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reopen_cancelled_order",
                "description": "Reopen a cancelled order by setting its status back to 'pending'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                    },
                    "required": ["order_id"],
                },
            },
        }
