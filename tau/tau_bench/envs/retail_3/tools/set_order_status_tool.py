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

class SetOrderStatusTool(Tool):
    """
    Set or change an order's status in orders.json.

    Behavior:
    - Confirms the order exists.
    - Updates order['status'] to the provided value.
    - Does not alter fulfillments or payment_history.

    Input (kwargs):
        order_id (str, required)
        status (str, required)  # e.g., "pending", "fulfilled", "completed", "cancelled"

    Output:
        JSON string with {"order_id","status"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, status: str = None) -> str:
        if not order_id or not isinstance(status, str) or not status:
            payload = {"error": "order_id and non-empty status are required"}
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

        order["status"] = status
        payload = {"order_id": order_id, "status": status}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetOrderStatus",
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
