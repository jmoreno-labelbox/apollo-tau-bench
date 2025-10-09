from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddCartItem(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], cart_id: Any, product_id: Any, quantity: Any
    ) -> str:
        cart_id = _idstr(cart_id)
        product_id = _idstr(product_id)
        quantity = int(quantity)
        product = next(
            (
                p
                for p in data.get("products", {}).values()
                if f"{p.get('product_id')}" == f"{product_id}"
            ),
            None,
        )
        if not product or int(product.get("stock_quantity", 0)) <= 0:
            payload = {"error": "Product out of stock or not found."}
            out = json.dumps(payload, indent=2)
            return out
        items = data.get("cart_items", {}).values()
        new_id = _next_numeric_id(items, "cart_item_id")
        items.append(
            {
                "cart_item_id": new_id,
                "cart_id": cart_id,
                "product_id": product_id,
                "quantity": quantity,
            }
        )
        payload = {"cart_item_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
        pass
        cart_id = _idstr(cart_id)
        product_id = _idstr(product_id)
        quantity = int(quantity)
        product = next(
            (
                p
                for p in data.get("products", {}).values()
                if f"{p.get('product_id')}" == f"{product_id}"
            ),
            None,
        )
        if not product or int(product.get("stock_quantity", 0)) <= 0:
            payload = {"error": "Product out of stock or not found."}
            out = json.dumps(payload, indent=2)
            return out
        items = data.get("cart_items", {}).values()
        new_id = _next_numeric_id(items, "cart_item_id")
        items.append(
            {
                "cart_item_id": new_id,
                "cart_id": cart_id,
                "product_id": product_id,
                "quantity": quantity,
            }
        )
        payload = {"cart_item_id": new_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addCartItem",
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
