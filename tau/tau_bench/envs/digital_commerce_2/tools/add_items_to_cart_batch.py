from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddItemsToCartBatch(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cart_id: Any, items: list[dict[str, Any]]) -> str:
        if not cart_id or not items or not isinstance(items, list):
            payload = {
                "error": "Missing required fields: cart_id and list 'items' with {product_id, quantity}"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        cart_items = data.get("cart_items", {}).values()
        created = []
        next_num = len(cart_items) + 1
        for it in items:
            pid = it.get("product_id")
            qty = it.get("quantity")
            if not pid or qty is None:
                payload = {"error": "Each item must include product_id and quantity"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            rec = {
                "cart_item_id": f"item_{next_num}",
                "cart_id": cart_id,
                "product_id": pid,
                "quantity": int(qty),
            }
            data["cart_items"][rec["cart_item_id"]] = rec
            created.append(rec)
            next_num += 1
        payload = created
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddItemsToCartBatch",
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
