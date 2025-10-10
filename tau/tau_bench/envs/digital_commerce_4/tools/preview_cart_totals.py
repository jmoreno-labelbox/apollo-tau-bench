# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PreviewCartTotals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any) -> str:
        cart_id = _as_id(cart_id)
        if not cart_id:
            return _err("cart_id is required.")

        carts = data.get("carts", [])
        cart = next((c for c in carts if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")

        items = data.get("cart_items", [])
        lines = [ci for ci in items if _as_id(ci.get("cart_id")) == cart_id]

        contacts = data.get("contacts", [])
        contact = next(
            (c for c in contacts if _as_id(c.get("contact_id")) == _as_id(cart.get("contact_id"))),
            None,
        )
        accounts = list(data.get("accounts", {}).values())
        account = next(
            (
                a
                for a in accounts
                if _as_id(a.get("account_id"))
                == _as_id(contact.get("account_id") if contact else None)
            ),
            None,
        )

        pricebook_id = account.get("default_pricebook_id")

        pbes = data.get("pricebook_entries", [])
        offers = data.get("offers", [])

        subtotal = 0.0
        for li in lines:
            entry = next(
                (
                    e
                    for e in pbes
                    if _as_id(e.get("pricebook_id")) == _as_id(pricebook_id)
                    and _as_id(e.get("product_id")) == _as_id(li.get("product_id"))
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
                    if _as_id(o.get("offer_id")) == _as_id(cart.get("applied_offer_id"))
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
                    discount_amount = min(float(offer.get("discount_value", 0.0)), subtotal)

        total_amount = round(subtotal - discount_amount, 2)
        return json.dumps(
            {
                "cart_id": cart_id,
                "subtotal": round(subtotal, 2),
                "discount_amount": round(discount_amount, 2),
                "total_amount": total_amount,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "preview_cart_totals",
                "description": "Compute cart totals from items + applied offer using the active pricebook.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string", "description": "Existing cart_id."}
                    },
                    "required": ["cart_id"],
                },
            },
        }
