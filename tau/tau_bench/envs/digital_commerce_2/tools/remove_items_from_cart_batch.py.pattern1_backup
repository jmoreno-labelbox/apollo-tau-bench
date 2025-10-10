# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveItemsFromCartBatch(Tool):
    """Remove multiple products from a cart in one call."""

    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, product_ids: Any) -> str:
        cart_id = cart_id
        product_ids: List[str] = product_ids
        if not cart_id or not product_ids or not isinstance(product_ids, list):
            return json.dumps(
                {"error": "Missing required fields: cart_id and list 'product_ids'."}, indent=2
            )
        cart_items = data.get("cart_items", [])
        before = len(cart_items)
        cart_items[:] = [
            r
            for r in cart_items
            if not (r.get("cart_id") == cart_id and r.get("product_id") in product_ids)
        ]
        removed = before - len(cart_items)
        return json.dumps(
            {"removed_count": removed, "cart_id": cart_id, "removed_product_ids": product_ids},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_items_from_cart_batch",
                "description": "Remove multiple products from a cart in one call.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "product_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["cart_id", "product_ids"],
                },
            },
        }
