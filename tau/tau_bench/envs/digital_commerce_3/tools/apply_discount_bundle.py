from tau_bench.envs.tool import Tool
import json
from typing import Any

class ApplyDiscountBundle(Tool):
    """Implement a discount on a cart and compute overall savings."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        cart_id: Any,
        offer_code: Any,
        carts: list = None,
        offers: list = None,
        cart_items: list = None,
        pricebook_entries: list = None,
        accounts: list = None
    ) -> str:
        pass
        cart_id = _idstr(cart_id)
        offer_code = f"{offer_code}"
        if not cart_id or not offer_code:
            return _error("cart_id and offer_code are required.")

        carts = carts if carts is not None else data.get("carts", [])
        cart = _find_one(carts, "cart_id", cart_id)
        if not cart:
            return _error(f"Cart '{cart_id}' not found.")

        offers = offers if offers is not None else data.get("offers", [])
        offer = _find_one(offers, "offer_code", offer_code)
        if not offer or not offer.get("is_active"):
            return _error(f"Offer '{offer_code}' not found or inactive.")

        cart_items = cart_items if cart_items is not None else data.get("cart_items", [])
        pricebook_entries = pricebook_entries if pricebook_entries is not None else data.get("pricebook_entries", [])
        accounts = accounts if accounts is not None else data.get("accounts", [])

        cart_line_items = [
            ci for ci in cart_items if f"{ci.get('cart_id')}" == f"{cart_id}"
        ]
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
            discount_amount = round(
                subtotal * (float(offer.get("discount_value", 0.0)) / 100.0), 2
            )
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
        _append_audit(
            data,
            "discount_applied",
            cart_id,
            {"offer_code": offer_code, "discount_amount": discount_amount},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyDiscountBundle",
                "description": "Apply a discount to a cart and calculate total savings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "offer_code": {"type": "string"},
                    },
                    "required": ["cart_id", "offer_code"],
                },
            },
        }
