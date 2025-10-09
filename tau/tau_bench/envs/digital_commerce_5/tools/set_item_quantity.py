from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SetItemQuantity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cart_item_id: Any, new_quantity: Any) -> str:
        if not cart_item_id or new_quantity is None:
            return _err("cart_item_id and new_quantity are required.")
        cart_item_id = str(cart_item_id)
        items = data.get("cart_items", {}).values()
        line = next(
            (ci for ci in items.values() if ci.get("cart_item_id") == cart_item_id), None
        )
        if not line:
            return _err("Cart item not found.")
        q = int(new_quantity)
        if q <= 0:
            return _err("new_quantity must be positive.")
        line["quantity"] = q
        payload = {"cart_item_id": cart_item_id, "new_quantity": q}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetItemQuantity",
                "description": "Set quantity for an existing cart line.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_item_id": {"type": "string"},
                        "new_quantity": {"type": "integer"},
                    },
                    "required": ["cart_item_id", "new_quantity"],
                },
            },
        }
