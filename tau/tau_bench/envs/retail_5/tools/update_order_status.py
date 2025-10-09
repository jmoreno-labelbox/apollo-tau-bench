from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, new_status: str = None) -> str:
        if not order_id or not new_status:
            payload = {"error": "order_id and new_status are required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        order = next((o for o in orders.values() if o["order_id"] == order_id), None)

        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out

        old_status = order["status"]
        order["status"] = new_status
        payload = {
                "success": True,
                "order_id": order_id,
                "old_status": old_status,
                "new_status": new_status,
                "updated_at": get_current_timestamp(),
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
                "name": "updateOrderStatus",
                "description": "Update the status of an existing order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order ID to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status for the order",
                        },
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }
