# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddItemsToCartBatch(Tool):
    """Add multiple products to a cart in one call."""

    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, items: Any) -> str:
        cart_id = cart_id
        items: List[Dict[str, Any]] = items
        if not cart_id or not items or not isinstance(items, list):
            return json.dumps(
                {
                    "error": "Missing required fields: cart_id and list 'items' with {product_id, quantity}"
                },
                indent=2,
            )
        cart_items = list(data.get("cart_items", {}).values())
        created = []
        next_num = len(cart_items) + 1
        for it in items:
            pid = it.get("product_id")
            qty = it.get("quantity")
            if not pid or qty is None:
                return json.dumps(
                    {"error": "Each item must include product_id and quantity"}, indent=2
                )
            rec = {
                "cart_item_id": f"item_{next_num}",
                "cart_id": cart_id,
                "product_id": pid,
                "quantity": int(qty),
            }
            cart_items.append(rec)
            created.append(rec)
            next_num += 1
        return json.dumps(created, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_items_to_cart_batch",
                "description": "Add multiple products to a cart in one call.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["product_id", "quantity"],
                            },
                        },
                    },
                    "required": ["cart_id", "items"],
                },
            },
        }
