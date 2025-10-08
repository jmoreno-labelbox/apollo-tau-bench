from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetOrdersByStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], status: str, limit: int = 20, start_date: str = None, end_date: str = None) -> str:
        if not status:
            payload = {"error": "status is required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        filtered_orders = []

        for order in orders:
            if order["status"] != status:
                continue

            # Date filtering is complicated without appropriate datetime objects, deferring for now as in the original

            order_summary = {
                "order_id": order["order_id"],
                "user_id": order["user_id"],
                "status": order["status"],
                "item_count": len(order["items"]),
                "total_amount": sum(item["price"] for item in order["items"]),
                "tracking_ids": [
                    f["tracking_id"][0]
                    for f in order.get("fulfillments", [])
                    if f.get("tracking_id")
                ],
            }
            filtered_orders.append(order_summary)

        filtered_orders.sort(key=lambda x: x["order_id"], reverse=True)
        payload = filtered_orders[:limit]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrdersByStatus",
                "description": "Get all orders with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Order status to filter by",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of orders to return",
                            "default": 20,
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date for filtering (ISO format, not fully implemented)",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date for filtering (ISO format, not fully implemented)",
                        },
                    },
                    "required": ["status"],
                },
            },
        }
