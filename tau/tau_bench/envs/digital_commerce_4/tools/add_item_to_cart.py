# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddItemToCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, product_id: Any, quantity: Any) -> str:
        cart_id = _as_id(cart_id)
        product_id = _as_id(product_id)
        if not cart_id or not product_id or quantity is None:
            return _err("cart_id, product_id, quantity are required.")
        qty = int(quantity)
        if qty <= 0:
            return _err("Quantity must be positive.")

        carts = data.get("carts", [])
        if not any(_as_id(c.get("cart_id")) == cart_id for c in carts):
            return _err("Cart not found.")

        products = list(data.get("products", {}).values())
        if not any(_as_id(p.get("product_id")) == product_id for p in products):
            return _err("Product not found.")

        items = data.get("cart_items", [])
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
            data["cart_items"] = items
            return json.dumps({"cart_item_id": existing["cart_item_id"], "updated": True}, indent=2)

        next_id = str(
            max(
                [
                    int(ci["cart_item_id"])
                    for ci in items
                    if str(ci.get("cart_item_id", "")).isdigit()
                ]
                or [0]
            )
            + 1
        )
        line = {
            "cart_item_id": next_id,
            "cart_id": cart_id,
            "product_id": product_id,
            "quantity": qty,
        }
        items.append(line)
        data["cart_items"] = items
        return json.dumps({"cart_item_id": next_id, "updated": False}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_item_to_cart",
                "description": "Add a product to a cart (upsert by product). New lines receive the next numeric cart_item_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string", "description": "Existing cart_id."},
                        "product_id": {"type": "string", "description": "Target product_id."},
                        "quantity": {"type": "integer", "description": "Positive whole number."},
                    },
                    "required": ["cart_id", "product_id", "quantity"],
                },
            },
        }
