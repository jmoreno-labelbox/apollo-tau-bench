from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateOrderStatus(Tool):
    """Alter the status of an order in a predictable manner."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str, status: str) -> str:
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                order["status"] = status
                payload = {"status": "success", "order_id": order_id, "new_status": status}
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
                "name": "UpdateOrderStatus",
                "description": "Update order status (e.g., pending, delivered, cancelled) by order_id.",
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
