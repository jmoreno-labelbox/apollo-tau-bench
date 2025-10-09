from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetOrderDetails(Tool):
    """Retrieve complete order information from orders.json using order_id."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                payload = order
                out = json.dumps(payload)
                return out
        payload = {"error": "Order not found", "order_id": order_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderDetails",
                "description": "Get order details from orders.json by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
