from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddItemToCart(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], cart_id: Any, product_id: Any, quantity: Any
    ) -> str:
        cart_id = _as_id(cart_id)
        product_id = _as_id(product_id)
        if not cart_id or not product_id or quantity is None:
            return _err("cart_id, product_id, quantity are required.")
        carts = data.get("carts", [])
        cart = next((c for c in carts if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")
        products = data.get("products", [])
        product = next(
            (p for p in products if _as_id(p.get("product_id")) == product_id), None
        )
        if not product:
            return _err("Product not found.")
        qty = int(quantity)
        if qty <= 0:
            return _err("Quantity must be positive.")
        items = data.setdefault("cart_items", [])
        existing = next(
            (
                ci
                for ci in items
                if _as_id(ci.get("cart_id")) == cart_id
                and _as_id(ci.get("product_id")) == product_id
            ),
            None,
        )
        if existing:
            existing["quantity"] = int(existing.get("quantity", 0)) + qty
            payload = {"cart_item_id": f"{cart_id}:{product_id}", "updated": True}
            out = json.dumps(
                payload, indent=2
            )
            return out
        cart_item = {
            "cart_item_id": f"{cart_id}:{product_id}",
            "cart_id": cart_id,
            "product_id": product_id,
            "quantity": qty,
        }
        items.append(cart_item)
        payload = {"cart_item_id": cart_item["cart_item_id"], "updated": False}
        out = json.dumps(
            payload, indent=2
        )
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddItemToCart",
                "description": "Add a product to a cart using the account's default pricebook.",
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
