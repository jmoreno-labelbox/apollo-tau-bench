from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetOrderDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None) -> str:
        if not order_id:
            payload = {"error": "order_id is required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        order = next((o for o in orders if o["order_id"] == order_id), None)

        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrderDetails",
                "description": "Retrieve complete details for a specific order by order ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order ID to look up",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }
