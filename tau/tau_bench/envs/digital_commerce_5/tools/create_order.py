from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], order_id: Any, cart_id: Any, created_at: Any
    ) -> str:
        pass
        order_id = _as_id(order_id)
        cart_id = _as_id(cart_id)
        if not order_id or not cart_id or not created_at:
            return _err("order_id, cart_id, created_at are required.")

        orders = data.setdefault("orders", [])
        existing = next(
            (o for o in orders if _as_id(o.get("order_id")) == order_id), None
        )
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out

        carts = data.get("carts", [])
        cart = next((c for c in carts if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")

        cart_items = data.get("cart_items", [])
        lines = [ci for ci in cart_items if _as_id(ci.get("cart_id")) == cart_id]
        if not lines:
            return _err("Cart has no items.")

        accounts = data.get("accounts", [])
        account = next(
            (
                a
                for a in accounts
                if _as_id(a.get("account_id")) == _as_id(cart.get("account_id"))
            ),
            None,
        )
        pricebook_id = cart.get("override_pricebook_id") or (
            account.get("default_pricebook_id") if account else "1"
        )
        pbes = data.get("pricebook_entries", [])
        offers = data.get("offers", [])
        products = data.get("products", [])

        subtotal = 0.0
        for li in lines:
            pid = _as_id(li.get("product_id"))
            pbe = next(
                (
                    e
                    for e in pbes
                    if _as_id(e.get("pricebook_id")) == _as_id(pricebook_id)
                    and _as_id(e.get("product_id")) == pid
                ),
                None,
            )
            if not pbe:
                return _err("Missing pricebook entry.")
            price = float(pbe.get("price", 0.0))
            qty = int(li.get("quantity", 0))
            subtotal += price * qty

            prod = next(
                (p for p in products if _as_id(p.get("product_id")) == pid), None
            )
            if not prod:
                return _err(f"Product {pid} not found.")
            current = int(prod.get("stock_quantity", 0))
            if current < qty:
                return _err(f"Insufficient stock for product {pid}.")
            prod["stock_quantity"] = current - qty

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
                    discount_amount = min(
                        float(offer.get("discount_value", 0.0)), subtotal
                    )

        total = round(subtotal - discount_amount, 2)

        new_order = {
            "order_id": order_id,
            "contact_id": cart.get("contact_id"),
            "account_id": cart.get("account_id"),
            "applied_offer_id": cart.get("applied_offer_id"),
            "order_date": created_at,
            "status": "Processing",
            "subtotal": round(subtotal, 2),
            "discount_amount": round(discount_amount, 2),
            "total_amount": total,
            "shipping_address_used": None,
        }
        orders.append(new_order)

        order_items = data.setdefault("order_items", [])
        for idx, li in enumerate(lines, start=1):
            pid = _as_id(li.get("product_id"))
            pbe = next(
                (
                    e
                    for e in pbes
                    if _as_id(e.get("pricebook_id")) == _as_id(pricebook_id)
                    and _as_id(e.get("product_id")) == pid
                ),
                None,
            )
            price = float(pbe.get("price", 0.0)) if pbe else 0.0
            order_items.append(
                {
                    "order_item_id": f"{order_id}_item_{idx}",
                    "order_id": order_id,
                    "product_id": pid,
                    "quantity": int(li.get("quantity", 0)),
                    "price": price,
                }
            )
        payload = new_order
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrder",
                "description": "Create an order from a cart at a fixed created_at timestamp and compute totals.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "cart_id": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["order_id", "cart_id", "created_at"],
                },
            },
        }
