from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetOrderStatus(Tool):
    """Provide solely the status of an order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        orders = data.get("orders", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                payload = {"order_id": order_id, "status": order.get("status")}
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
                "name": "GetOrderStatus",
                "description": "Return the order status by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
