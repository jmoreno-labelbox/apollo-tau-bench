from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ClearCart(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cart_id: Any) -> str:
        pass
        cart_id = _idstr(cart_id)
        if not cart_id:
            payload = {"error": "Missing required field: cart_id"}
            out = json.dumps(payload, indent=2)
            return out
        cart_items = data.get("cart_items", {}).values()
        removed_count = 0
        for item in list(cart_items):  # duplicate to prevent changes while iterating
            if item.get("cart_id") == cart_id:
                cart_items.remove(item)
                removed_count += 1

        if removed_count == 0:
            payload = {"error": f"No items found for cart_id '{cart_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {
            "message": f"All items removed from cart '{cart_id}'",
            "removed_count": removed_count,
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
                "name": "ClearCart",
                "description": "Remove all items from a given cart.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {
                            "type": "string",
                            "description": "ID of the cart to clear.",
                        }
                    },
                    "required": ["cart_id"],
                },
            },
        }
