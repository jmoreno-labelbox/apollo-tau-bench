# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _err(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

class SetItemQuantity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_item_id: str, new_quantity: Any) -> str:
        if not cart_item_id or new_quantity is None:
            return _err("cart_item_id and new_quantity are required.")
        cart_item_id = str(cart_item_id)
        items = data.get("cart_items", [])
        line = next((ci for ci in items if ci.get("cart_item_id") == cart_item_id), None)
        if not line:
            return _err("Cart item not found.")
        q = int(new_quantity)
        if q <= 0:
            return _err("new_quantity must be positive.")
        line["quantity"] = q
        return json.dumps({"cart_item_id": cart_item_id, "new_quantity": q}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_item_quantity",
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