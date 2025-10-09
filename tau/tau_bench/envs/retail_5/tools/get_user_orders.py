from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetUserOrders(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, status: str = None, limit: int = 10) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        user_orders = []

        for order in orders:
            if order["user_id"] == user_id:
                if status and order["status"] != status:
                    continue
                user_orders.append(
                    {
                        "order_id": order["order_id"],
                        "status": order["status"],
                        "items": order["items"],
                        "total_amount": sum(item["price"] for item in order["items"]),
                    }
                )

        user_orders.sort(key=lambda x: x["order_id"], reverse=True)
        payload = user_orders[:limit]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUserOrders",
                "description": "Get all orders for a specific user with optional status filtering.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User ID to get orders for",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by order status",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of orders to return",
                            "default": 10,
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }
