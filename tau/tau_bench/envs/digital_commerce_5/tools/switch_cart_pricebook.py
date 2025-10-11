# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _err(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

def _as_id(x: Any) -> str:
    if x is None:
        return x
    if isinstance(x, str):
        return x
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)

class SwitchCartPricebook(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: str, pricebook_id: Any) -> str:
        cart_id = _as_id(cart_id)
        pricebook_id = _as_id(pricebook_id)
        if not cart_id or not pricebook_id:
            return _err("cart_id and pricebook_id are required.")
        carts = data.get("carts", [])
        cart = next((c for c in carts if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")
        cart["override_pricebook_id"] = pricebook_id
        return json.dumps({"cart_id": cart_id, "pricebook_id": pricebook_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "switch_cart_pricebook",
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