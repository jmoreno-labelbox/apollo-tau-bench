# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ClearCart(Tool):
    """Remove all items from a given cart."""

    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any) -> str:
        cart_id = _idstr(cart_id)
        if not cart_id:
            return json.dumps({"error": "Missing required field: cart_id"}, indent=2)
        cart_items = list(data.get("cart_items", {}).values())
        removed_count = 0
        for item in list(cart_items):
            if item.get("cart_id") == cart_id:
                cart_items.remove(item)
                removed_count += 1

        if removed_count == 0:
            return json.dumps({"error": f"No items found for cart_id '{cart_id}'"}, indent=2)

        return json.dumps(
            {"message": f"All items removed from cart '{cart_id}'", "removed_count": removed_count},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "clear_cart",
                "description": "Remove all items from a given cart.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string", "description": "ID of the cart to clear."}
                    },
                    "required": ["cart_id"],
                },
            },
        }
