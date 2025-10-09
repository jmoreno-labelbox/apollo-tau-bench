from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAllOrderItemsByOrderId(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, order_items: list[dict[str, Any]] = None) -> str:
        order_id = _idstr(order_id)
        if not order_id:
            payload = {"error": "Missing required field: order_id"}
            out = json.dumps(payload, indent=2)
            return out
        order_items = order_items or data.get("order_items", {}).values()
        items = [item for item in order_items.values() if item.get("order_id") == order_id]
        payload = items
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllOrderItemsByOrderId",
                "description": "Return all order items for the specified order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Exact order ID whose items should be returned.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }
