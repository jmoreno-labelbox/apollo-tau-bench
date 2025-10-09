from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RemoveItemsFromCartBatch(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cart_id: Any, product_ids: list[str]) -> str:
        if not cart_id or not product_ids or not isinstance(product_ids, list):
            payload = {"error": "Missing required fields: cart_id and list 'product_ids'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        cart_items = data.get("cart_items", {}).values()
        before = len(cart_items)
        cart_items[:] = [
            r
            for r in cart_items.values() if not (r.get("cart_id") == cart_id and r.get("product_id") in product_ids)
        ]
        removed = before - len(cart_items)
        payload = {
                "removed_count": removed,
                "cart_id": cart_id,
                "removed_product_ids": product_ids,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveItemsFromCartBatch",
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
