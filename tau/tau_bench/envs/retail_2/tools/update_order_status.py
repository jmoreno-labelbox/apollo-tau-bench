# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateOrderStatus(Tool):
    """Change the status of an order deterministically."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, status: str) -> str:
        orders = list(data.get("orders", {}).values())
        for order in orders:
            if order.get("order_id") == order_id:
                order["status"] = status
                return json.dumps({"status": "success", "order_id": order_id, "new_status": status})
        return json.dumps({"error": "Order not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_order_status",
                "description": "Update order status (e.g., pending, delivered, cancelled) by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "status": {"type": "string"}
                    },
                    "required": ["order_id", "status"]
                }
            }
        }
