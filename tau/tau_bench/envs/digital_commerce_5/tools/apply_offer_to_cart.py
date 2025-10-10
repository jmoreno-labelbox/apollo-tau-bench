# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyOfferToCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: str, code: Any) -> str:
        cart_id = _as_id(cart_id)
        if not cart_id or not code:
            return _err("cart_id and code are required.")
        carts = data.get("carts", [])
        offers = data.get("offers", [])
        cart = next((c for c in carts if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")
        offer = next(
            (o for o in offers if o.get("offer_code") == code and o.get("is_active") is True), None
        )
        if not offer:
            return _err("Offer not found or inactive.")
        cart["applied_offer_id"] = offer.get("offer_id")
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
                "description": "Apply an offer code to a cart (sets applied_offer_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "code": {"type": "string"},
                    },
                    "required": ["cart_id", "code"],
                },
            },
        }
