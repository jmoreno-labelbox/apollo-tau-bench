# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table


class CreateCartWithItems(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        customer_email: str,
        items: List[Dict[str, Any]],
        promo_code: Optional[str] = None,
        shipping_method: Optional[str] = None,
    ) -> str:
        customers = _ensure_table(data, "customers")
        carts = _ensure_table(data, "carts")
        cart_items = _ensure_table(data, "cart_items")
        pbes = _ensure_table(data, "pricebook_entries")
        products = _ensure_table(data, "products")
        offers = _ensure_table(data, "offers")
        methods = _ensure_table(data, "shipping_methods")

        cust = _find_one(customers, email=customer_email)
        if not cust:
            cid = _stable_id("cust", customer_email)
            cust = {"customer_id": cid, "email": customer_email, "created_at": FIXED_NOW}
            customers.append(cust)

        subtotal = 0.0
        lines = []
        for it in items:
            code = it["product_code"]
            qty = int(it["qty"])
            pbe = next((r for r in pbes if r.get("product_code") == code), None)
            if pbe:
                unit = float(pbe.get("unit_price", 0.0))
            else:
                prod = _find_one(products, product_code=code) or {}
                unit = float(prod.get("base_price", 0.0))
            line_total = round(unit * qty, 2)
            subtotal = round(subtotal + line_total, 2)
            lines.append(
                {"product_code": code, "qty": qty, "unit_price": unit, "line_total": line_total}
            )

        discount = 0.0
        if promo_code:
            promo = _find_one(offers, offer_code=promo_code) or _find_one(offers, name=promo_code)
            if promo and bool(promo.get("active", promo.get("is_active", False))):
                dt = (promo.get("discount_type") or "").upper()
                dv = float(promo.get("discount_value", 0.0))
                if dt == "PERCENTAGE":
                    discount = round(subtotal * dv / 100.0, 2)
                elif dt == "FIXED_AMOUNT":
                    discount = round(min(dv, subtotal), 2)

        method = (shipping_method or "STANDARD").upper()
        rate_row = _find_one(methods, code=method) or {"code": "STANDARD", "rate": 5.00}
        shipping = float(rate_row.get("rate", 5.00))

        total = round(subtotal - discount + shipping, 2)
        candidate = _stable_id("cart", cust["customer_id"], FIXED_NOW)
        cart_id = _ensure_unique_id(carts, "cart_id", candidate)

        carts.append(
            {
                "cart_id": cart_id,
                "customer_id": cust["customer_id"],
                "customer_email": customer_email,
                "subtotal": subtotal,
                "discount": discount,
                "shipping": shipping,
                "total": total,
                "created_at": FIXED_NOW,
            }
        )
        for li in lines:
            cart_items.append({"cart_id": cart_id, **li})

        return _json(
            {
                "cart_id": cart_id,
                "subtotal": subtotal,
                "discount": discount,
                "shipping": shipping,
                "total": total,
                "shipping_method": method,
            }
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_cart_with_items",
                "description": "Create a cart; auto-calc prices, promo, and shipping method.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_email": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_code": {"type": "string"},
                                    "qty": {"type": "integer", "minimum": 1},
                                },
                                "required": ["product_code", "qty"],
                            },
                        },
                        "promo_code": {"type": "string"},
                        "shipping_method": {
                            "type": "string",
                            "description": "e.g., STANDARD, EXPRESS, OVERNIGHT",
                        },
                    },
                    "required": ["customer_email", "items"],
                },
            },
        }
