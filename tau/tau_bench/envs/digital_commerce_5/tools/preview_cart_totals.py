from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class PreviewCartTotals(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        carts: list[dict[str, Any]] = None,
        cart_items: list[dict[str, Any]] = None,
        accounts: list[dict[str, Any]] = None,
        pricebook_entries: list[dict[str, Any]] = None,
        offers: list[dict[str, Any]] = None,
        cart_id: Any = None
    ) -> str:
        cart_id = _as_id(cart_id)
        if not cart_id:
            return _err("cart_id is required.")
        carts = carts or []
        cart = next((c for c in carts if c.get("cart_id") == cart_id), None)
        if not cart:
            return _err("Cart not found.")

        items = cart_items or []
        lines = [ci for ci in items.values() if ci.get("cart_id") == cart_id]

        accounts = accounts or []
        account = next(
            (a for a in accounts if a.get("account_id") == cart.get("account_id")), None
        )
        pricebook_id = cart.get("override_pricebook_id") or (
            account.get("default_pricebook_id") if account else "1"
        )

        pbes = pricebook_entries or []
        offers = offers or []

        subtotal = 0.0
        for li in lines:
            entry = next(
                (
                    e
                    for e in pbes
                    if e.get("pricebook_id") == pricebook_id
                    and e.get("product_id") == li.get("product_id")
                ),
                None,
            )
            if not entry:
                return _err("Missing pricebook entry.")
            subtotal += float(entry.get("price", 0.0)) * int(li.get("quantity", 0))

        discount_amount = 0.0
        if cart.get("applied_offer_id"):
            offer = next(
                (
                    o
                    for o in offers
                    if o.get("offer_id") == cart.get("applied_offer_id")
                    and o.get("is_active") is True
                ),
                None,
            )
            if offer:
                if offer.get("discount_type") == "PERCENTAGE":
                    discount_amount = round(
                        subtotal * (float(offer.get("discount_value", 0.0)) / 100.0), 2
                    )
                elif offer.get("discount_type") == "FIXED_AMOUNT":
                    discount_amount = min(
                        float(offer.get("discount_value", 0.0)), subtotal
                    )

        total_amount = round(subtotal - discount_amount, 2)
        payload = {
                "cart_id": cart_id,
                "subtotal": round(subtotal, 2),
                "discount_amount": round(discount_amount, 2),
                "total_amount": total_amount,
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
                "name": "PreviewCartTotals",
                "description": "Compute cart totals from items + offer with current pricebook; no writes.",
                "parameters": {
                    "type": "object",
                    "properties": {"cart_id": {"type": "string"}},
                    "required": ["cart_id"],
                },
            },
        }
