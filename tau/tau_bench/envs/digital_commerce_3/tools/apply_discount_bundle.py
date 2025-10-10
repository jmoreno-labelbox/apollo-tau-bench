# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyDiscountBundle(Tool):
    """Apply a discount to a cart and calculate total savings."""

    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, offer_code: Any) -> str:
        cart_id = _idstr(cart_id)
        offer_code = f"{offer_code}"
        if not cart_id or not offer_code:
            return _error("cart_id and offer_code are required.")

        carts = data.get("carts", [])
        cart = _find_one(carts, "cart_id", cart_id)
        if not cart:
            return _error(f"Cart '{cart_id}' not found.")

        offers = data.get("offers", [])
        offer = _find_one(offers, "offer_code", offer_code)
        if not offer or not offer.get("is_active"):
            return _error(f"Offer '{offer_code}' not found or inactive.")

        cart_items = data.get("cart_items", [])
        pricebook_entries = data.get("pricebook_entries", [])
        accounts = list(data.get("accounts", {}).values())

        cart_line_items = [ci for ci in cart_items if f"{ci.get('cart_id')}" == f"{cart_id}"]
        account = _find_one(accounts, "account_id", cart.get("account_id"))
        pricebook_id = account.get("default_pricebook_id") if account else "1"

        subtotal = 0.0
        for ci in cart_line_items:
            pbe = next(
                (
                    p
                    for p in pricebook_entries
                    if f"{p.get('product_id')}" == f"{ci.get('product_id')}"
                    and f"{p.get('pricebook_id')}" == f"{pricebook_id}"
                ),
                None,
            )
            if pbe:
                subtotal += float(pbe.get("price", 0.0)) * int(ci.get("quantity", 0))

        discount_amount = 0.0
        if offer.get("discount_type") == "PERCENTAGE":
            discount_amount = round(subtotal * (float(offer.get("discount_value", 0.0)) / 100.0), 2)
        elif offer.get("discount_type") == "FIXED_AMOUNT":
            discount_amount = min(float(offer.get("discount_value", 0.0)), subtotal)

        cart["applied_offer_id"] = offer.get("offer_id")

        result = {
            "cart_id": cart_id,
            "offer_applied": offer_code,
            "subtotal": round(subtotal, 2),
            "discount_amount": round(discount_amount, 2),
            "total_amount": round(subtotal - discount_amount, 2),
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_discount_bundle",
                "description": "Apply a discount to a cart and calculate total savings.",
                "parameters": {
                    "type": "object",
                    "properties": {"cart_id": {"type": "string"}, "offer_code": {"type": "string"}},
                    "required": ["cart_id", "offer_code"],
                },
            },
        }
