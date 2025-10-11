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

class ApplyOfferToCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, code: Any) -> str:
        cart_id = _as_id(cart_id)
        if not cart_id or not code:
            return _err("cart_id and code are required.")

        carts = data.get("carts", [])
        cart = next((c for c in carts if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")

        offers = data.get("offers", [])
        offer = next(
            (o for o in offers if o.get("offer_code") == code and o.get("is_active") is True), None
        )
        if not offer:
            return _err("Offer not found or inactive.")

        cart["applied_offer_id"] = offer.get("offer_id")
        data["carts"] = carts
        return json.dumps(
            {"cart_id": cart_id, "applied_offer_id": cart["applied_offer_id"], "code": code},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_offer_to_cart",
                "description": "Apply an active offer code to a cart (sets cart.applied_offer_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string", "description": "Existing cart_id."},
                        "code": {"type": "string", "description": "Valid offer_code."},
                    },
                    "required": ["cart_id", "code"],
                },
            },
        }