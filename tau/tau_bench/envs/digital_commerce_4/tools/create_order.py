# Sierra copyright notice.

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

class CreateOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, order_id: Any = None) -> str:
        cart_id = _as_id(cart_id)
        if not cart_id:
            return _err("cart_id required.")

        carts = data.get("carts", [])
        cart = next((c for c in carts if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")

        cart_items = data.get("cart_items", [])
        lines = [ci for ci in cart_items if _as_id(ci.get("cart_id")) == cart_id]
        if not lines:
            return _err("Cart has no items.")

        # automatically generate order_id if not provided
        orders = list(data.get("orders", {}).values())
        if not order_id:
            numeric_ids = [
                int(o["order_id"]) for o in orders if str(o.get("order_id", "")).isdigit()
            ]
            order_id = str(max(numeric_ids or [0]) + 1)
        order_id = _as_id(order_id)

        # pricing information
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
        pricebook_id = cart.get("override_pricebook_id") or (
            account.get("default_pricebook_id") if account else "1"
        )

        pbes = data.get("pricebook_entries", [])
        offers = data.get("offers", [])
        products = list(data.get("products", {}).values())

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

            prod = next((p for p in products if _as_id(p.get("product_id")) == pid), None)
            if not prod:
                return _err(f"Product {pid} not found.")
            current = int(prod.get("stock_quantity", 0))
            if current < qty:
                return _err(f"Insufficient stock for product {pid}.")
            prod["stock_quantity"] = current - qty
        data["products"] = products

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

        total = round(subtotal - discount_amount, 2)

        new_order = {
            "order_id": order_id,
            "contact_id": cart.get("contact_id"),
            "account_id": account.get("account_id") if account else None,
            "applied_offer_id": cart.get("applied_offer_id"),
            "order_date": FIXED_NOW,
            "status": "Processing",
            "subtotal": round(subtotal, 2),
            "discount_amount": round(discount_amount, 2),
            "total_amount": total,
            "shipping_address_used": None,
        }
        orders.append(new_order)
        data["orders"] = orders

        order_items = data.get("order_items", [])
        next_oid = (
            max(
                [
                    int(oi["order_item_id"])
                    for oi in order_items
                    if str(oi.get("order_item_id", "")).isdigit()
                ]
                or [0]
            )
            + 1
        )
        for idx, li in enumerate(lines):
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
                    "order_item_id": str(next_oid + idx),
                    "order_id": order_id,
                    "product_id": pid,
                    "quantity": int(li.get("quantity", 0)),
                    "price": price,
                }
            )
        data["order_items"] = order_items
        data["carts"] = carts

        return json.dumps(new_order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order",
                "description": "Create an order from a cart; auto-assigns order_id if omitted; writes order and order_items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {
                            "type": "string",
                            "description": "Existing cart_id that has at least one cart item.",
                        },
                        "order_id": {
                            "type": "string",
                            "description": "(Optional) Explicit order_id; if omitted, system assigns next numeric string.",
                        },
                    },
                    "required": ["cart_id"],
                },
            },
        }