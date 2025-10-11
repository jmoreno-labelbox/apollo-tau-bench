# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _idstr(v):
    return str(v) if isinstance(v, int) else v

class GetAllItemsInCart(Tool):
    """Fetch all items in a cart by cart_id in simplified format."""

    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any) -> str:
        cart_id = _idstr(cart_id)
        if not cart_id:
            return json.dumps({"error": "Missing required field: cart_id"}, indent=2)
        cart_items = list(data.get("cart_items", {}).values())
        items_list = []
        for item in cart_items:
            if item.get("cart_id") == cart_id:
                items_list.append(
                    {"product_id": item.get("product_id"), "quantity": item.get("quantity")}
                )

        if not items_list:
            return json.dumps({"error": f"No items found for cart_id '{cart_id}'"}, indent=2)

        return json.dumps(items_list, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_items_in_cart",
                "description": "Fetch all items in a cart by cart_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {
                            "type": "string",
                            "description": "Exact cart ID to retrieve items for.",
                        }
                    },
                    "required": ["cart_id"],
                },
            },
        }