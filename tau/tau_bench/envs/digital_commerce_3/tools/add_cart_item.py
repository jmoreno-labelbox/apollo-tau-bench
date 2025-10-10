# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddCartItem(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, product_id: Any, quantity: Any) -> str:
        cart_id = _idstr(cart_id)
        product_id = _idstr(product_id)
        quantity = int(quantity)
        product = next(
            (p for p in list(data.get("products", {}).values()) if f"{p.get('product_id')}" == f"{product_id}"),
            None,
        )
        if not product or int(product.get("stock_quantity", 0)) <= 0:
            return json.dumps({"error": "Product out of stock or not found."}, indent=2)
        items = data.get("cart_items", [])
        new_id = _next_numeric_id(items, "cart_item_id")
        items.append(
            {
                "cart_item_id": new_id,
                "cart_id": cart_id,
                "product_id": product_id,
                "quantity": quantity,
            }
        )
        return json.dumps({"cart_item_id": new_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_cart_item",
                "description": "Adds an item to a cart if product has stock.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "product_id": {"type": "string"},
                        "quantity": {"type": "integer"},
                    },
                    "required": ["cart_id", "product_id", "quantity"],
                },
            },
        }
