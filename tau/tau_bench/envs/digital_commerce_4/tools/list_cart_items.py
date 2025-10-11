# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCartItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any) -> str:
        if not cart_id:
            return json.dumps({"error": "cart_id is required."}, indent=2)
        cart_id = _as_id(cart_id)
        rows = [ci for ci in data.get("cart_items", []) if _as_id(ci.get("cart_id")) == cart_id]
        # return basic, predictable fields
        items = [
            {
                "cart_item_id": r.get("cart_item_id"),
                "product_id": r.get("product_id"),
                "quantity": int(r.get("quantity", 0)),
            }
            for r in rows
        ]
        return json.dumps({"cart_id": cart_id, "items": items}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_cart_items",
                "description": "List items in a cart (cart_item_id, product_id, quantity).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string", "description": "Existing cart_id."}
                    },
                    "required": ["cart_id"],
                },
            },
        }
