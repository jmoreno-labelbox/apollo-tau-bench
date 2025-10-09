from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetOrderDetailsById(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any) -> str:
        order_id = _idstr(order_id)
        if not order_id:
            payload = {"error": "Missing required field: order_id"}
            out = json.dumps(payload, indent=2)
            return out
        orders = data.get("orders", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                payload = order
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No order found with ID '{order_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderDetailsById",
                "description": "Fetch full order details by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Exact order ID to retrieve.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }
