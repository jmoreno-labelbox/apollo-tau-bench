# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveItemFromCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, product_id: Any) -> str:
        cart_id = _as_id(cart_id)
        product_id = _as_id(product_id)
        if not cart_id or not product_id:
            return _err("cart_id and product_id are required.")
        items = data.get("cart_items", [])
        before = len(items)
        data["cart_items"] = [
            ci
            for ci in items
            if not (
                _as_id(ci.get("cart_id")) == cart_id and _as_id(ci.get("product_id")) == product_id
            )
        ]
        if len(data["cart_items"]) == before:
            return _err("Cart line not found.")
        return json.dumps({"removed_cart_item_id": f"{cart_id}:{product_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_item_from_cart",
                "description": "Remove a product from a cart.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "product_id": {"type": "string"},
                    },
                    "required": ["cart_id", "product_id"],
                },
            },
        }
