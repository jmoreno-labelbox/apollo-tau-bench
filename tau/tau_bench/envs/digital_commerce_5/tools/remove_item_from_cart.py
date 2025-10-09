from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RemoveItemFromCart(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cart_id: Any, product_id: Any) -> str:
        cart_id = _as_id(cart_id)
        product_id = _as_id(product_id)
        if not cart_id or not product_id:
            return _err("cart_id and product_id are required.")
        items = data.get("cart_items", {}).values()
        before = len(items)
        data["cart_items"] = [
            ci
            for ci in items.values() if not (
                _as_id(ci.get("cart_id")) == cart_id
                and _as_id(ci.get("product_id")) == product_id
            )
        ]
        if len(data["cart_items"]) == before:
            return _err("Cart line not found.")
        payload = {"removed_cart_item_id": f"{cart_id}:{product_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveItemFromCart",
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
