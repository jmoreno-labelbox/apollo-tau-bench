# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _err(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

def _as_id(x: Any) -> str:
    if x is None:
        return x
    if isinstance(x, str):
        return x
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)

class AddItemToCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: str, product_id: str, quantity: Any) -> str:
        cart_id = _as_id(cart_id)
        product_id = _as_id(product_id)
        if not cart_id or not product_id or quantity is None:
            return _err("cart_id, product_id, quantity are required.")
        carts = data.get("carts", [])
        cart = next((c for c in carts if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")
        products = list(list(list(data.get("products", {}).values())) if isinstance(data.get("products"), dict) else data.get("products", []))
        product = next((p for p in products if _as_id(p.get("product_id")) == product_id), None)
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
            return json.dumps(
                {"cart_item_id": f"{cart_id}:{product_id}", "updated": True}, indent=2
            )
        cart_item = {
            "cart_item_id": f"{cart_id}:{product_id}",
            "cart_id": cart_id,
            "product_id": product_id,
            "quantity": qty,
        }
        items.append(cart_item)
        return json.dumps({"cart_item_id": cart_item["cart_item_id"], "updated": False}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_item_to_cart",
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