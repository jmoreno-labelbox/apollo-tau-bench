from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateItemsInCartBatch(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cart_id: Any, items: list[dict[str, Any]]) -> str:
        if not cart_id or not items or not isinstance(items, list):
            payload = {
                "error": "Missing required fields: cart_id and list 'items' with {product_id, new_quantity}"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        cart_items = data.get("cart_items", {}).values()
        updated = []
        for it in items:
            pid = it.get("product_id")
            new_q = it.get("new_quantity")
            if not pid or new_q is None:
                payload = {"error": "Each item must include product_id and new_quantity"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            for row in cart_items.values():
                if row.get("cart_id") == cart_id and row.get("product_id") == pid:
                    row["quantity"] = int(new_q)
                    updated.append(row)
                    break
        if not updated:
            payload = {"error": f"No matching items found to update for cart '{cart_id}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = updated
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateItemsInCartBatch",
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
