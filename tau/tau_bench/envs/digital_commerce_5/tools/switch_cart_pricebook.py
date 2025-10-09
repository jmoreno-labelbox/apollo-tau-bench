from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SwitchCartPricebook(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cart_id: Any, pricebook_id: Any) -> str:
        cart_id = _as_id(cart_id)
        pricebook_id = _as_id(pricebook_id)
        if not cart_id or not pricebook_id:
            return _err("cart_id and pricebook_id are required.")
        carts = data.get("carts", {}).values()
        cart = next((c for c in carts.values() if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")
        cart["override_pricebook_id"] = pricebook_id
        payload = {"cart_id": cart_id, "pricebook_id": pricebook_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SwitchCartPricebook",
                "description": "Override the pricebook used for a cart (deterministic).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "pricebook_id": {"type": "string"},
                    },
                    "required": ["cart_id", "pricebook_id"],
                },
            },
        }
