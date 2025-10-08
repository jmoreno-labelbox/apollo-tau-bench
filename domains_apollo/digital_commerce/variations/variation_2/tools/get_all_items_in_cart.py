from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class GetAllItemsInCart(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cart_id: Any, cart_items: list[dict[str, Any]] = None) -> str:
        cart_id = _idstr(cart_id)
        if not cart_id:
            payload = {"error": "Missing required field: cart_id"}
            out = json.dumps(payload, indent=2)
            return out
        cart_items = cart_items or []
        items_list = []
        for item in cart_items:
            if item.get("cart_id") == cart_id:
                items_list.append(
                    {
                        "product_id": item.get("product_id"),
                        "quantity": item.get("quantity"),
                    }
                )

        if not items_list:
            payload = {"error": f"No items found for cart_id '{cart_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = items_list
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllItemsInCart",
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
