# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateItemsInCartBatch(Tool):
    """Update quantities for multiple products in a cart in one call."""

    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, items: Any) -> str:
        cart_id = cart_id
        items: List[Dict[str, Any]] = items
        if not cart_id or not items or not isinstance(items, list):
            return json.dumps(
                {
                    "error": "Missing required fields: cart_id and list 'items' with {product_id, new_quantity}"
                },
                indent=2,
            )
        cart_items = data.get("cart_items", [])
        updated = []
        for it in items:
            pid = it.get("product_id")
            new_q = it.get("new_quantity")
            if not pid or new_q is None:
                return json.dumps(
                    {"error": "Each item must include product_id and new_quantity"}, indent=2
                )
            for row in cart_items:
                if row.get("cart_id") == cart_id and row.get("product_id") == pid:
                    row["quantity"] = int(new_q)
                    updated.append(row)
                    break
        if not updated:
            return json.dumps(
                {"error": f"No matching items found to update for cart '{cart_id}'"}, indent=2
            )
        return json.dumps(updated, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_items_in_cart_batch",
                "description": "Update quantities for multiple products in a cart.",
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
                                    "new_quantity": {"type": "integer"},
                                },
                                "required": ["product_id", "new_quantity"],
                            },
                        },
                    },
                    "required": ["cart_id", "items"],
                },
            },
        }
