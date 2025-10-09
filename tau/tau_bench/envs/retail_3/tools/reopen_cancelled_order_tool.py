from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ReopenCancelledOrderTool(Tool):
    """
    Reopen an order that was previously cancelled by changing its status back to 'pending'.

    Behavior:
    - Confirms the order exists and is currently 'cancelled'.
    - Updates order['status'] to 'pending'.
    - Does not alter items, payment_history, or fulfillments.

    Input (kwargs):
        order_id (str, required)

    Output:
        JSON string with {"order_id","status"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None) -> str:
        if not order_id:
            payload = {"error": "order_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        if order.get("status") != "cancelled":
            payload = {
                    "error": f"order status must be 'cancelled', found '{order.get('status')}'"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        order["status"] = "pending"
        payload = {"order_id": order_id, "status": "pending"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReopenCancelledOrder",
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
