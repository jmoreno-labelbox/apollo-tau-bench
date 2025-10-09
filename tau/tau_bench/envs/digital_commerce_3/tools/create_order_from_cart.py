from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateOrderFromCart(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cart_id: Any,
        contact_id: Any,
        account_id: Any,
        offer_id: Any = None
    ) -> str:
        cart_id = _idstr(cart_id)
        contact_id = _idstr(contact_id)
        account_id = _idstr(account_id)
        offer_id = _idstr(offer_id) if offer_id is not None else None

        carts = data.get("carts", [])
        cart = next(
            (
                c
                for c in carts
                if f"{c.get('cart_id')}" == f"{cart_id}"
                and f"{c.get('contact_id')}" == f"{contact_id}"
            ),
            None,
        )
        if not cart:
            payload = {"error": "Cart for contact not found."}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", [])
        order_items = data.get("order_items", [])
        cart_items = [
            ci
            for ci in data.get("cart_items", [])
            if f"{ci.get('cart_id')}" == f"{cart_id}"
        ]

        account = next(
            (
                a
                for a in data.get("accounts", [])
                if f"{a.get('account_id')}" == f"{account_id}"
            ),
            None,
        )
        pricebook_id = account.get("default_pricebook_id") if account else "1"
        prices = [
            e
            for e in data.get("pricebook_entries", [])
            if f"{e.get('pricebook_id')}" == f"{pricebook_id}"
        ]

        subtotal = 0.0
        for item in cart_items:
            entry = next(
                (
                    e
                    for e in prices
                    if f"{e.get('product_id')}" == f"{item.get('product_id')}"
                ),
                None,
            )
            if not entry:
                payload = {"error": "Missing pricebook entry."}
                out = json.dumps(payload, indent=2)
                return out
            subtotal += float(entry.get("price", 0.0)) * int(item.get("quantity", 0))

        discount_amount = 0.0
        if offer_id:
            offer = next(
                (
                    o
                    for o in data.get("offers", [])
                    if f"{o.get('offer_id')}" == f"{offer_id}"
                    and o.get("is_active") is True
                ),
                None,
            )
            if offer:
                if offer.get("discount_type") == "PERCENTAGE":
                    discount_amount = round(
                        subtotal * (float(offer.get("discount_value", 0.0)) / 100.0), 2
                    )
                else:
                    discount_amount = float(offer.get("discount_value", 0.0))

        total_amount = round(subtotal - discount_amount, 2)

        new_order_id = _next_numeric_id(orders, "order_id")
        order = {
            "order_id": new_order_id,
            "contact_id": contact_id,
            "account_id": account_id,
            "applied_offer_id": offer_id,
            "order_date": "FIXED-DATE",
            "status": "Processing",
            "subtotal": round(subtotal, 2),
            "discount_amount": round(discount_amount, 2),
            "total_amount": total_amount,
            "shipping_address_used": (
                account.get("shipping_street") if account else None
            ),
        }
        orders.append(order)

        for item in cart_items:
            entry = next(
                (
                    e
                    for e in prices
                    if f"{e.get('product_id')}" == f"{item.get('product_id')}"
                ),
                None,
            )
            price = float(entry.get("price", 0.0))
            new_oi_id = _next_numeric_id(order_items, "order_item_id")
            order_items.append(
                {
                    "order_item_id": new_oi_id,
                    "order_id": new_order_id,
                    "product_id": item.get("product_id"),
                    "quantity": int(item.get("quantity")),
                    "price": price,
                }
            )
        payload = {"order_id": new_order_id}
        out = json.dumps(payload, indent=2)
        return out
        pass
        cart_id = _idstr(cart_id)
        contact_id = _idstr(contact_id)
        account_id = _idstr(account_id)
        offer_id = _idstr(offer_id) if offer_id is not None else None

        carts = data.get("carts", [])
        cart = next(
            (
                c
                for c in carts
                if f"{c.get('cart_id')}" == f"{cart_id}"
                and f"{c.get('contact_id')}" == f"{contact_id}"
            ),
            None,
        )
        if not cart:
            payload = {"error": "Cart for contact not found."}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", [])
        order_items = data.get("order_items", [])
        cart_items = [
            ci
            for ci in data.get("cart_items", [])
            if f"{ci.get('cart_id')}" == f"{cart_id}"
        ]

        account = next(
            (
                a
                for a in data.get("accounts", [])
                if f"{a.get('account_id')}" == f"{account_id}"
            ),
            None,
        )
        pricebook_id = account.get("default_pricebook_id") if account else "1"
        prices = [
            e
            for e in data.get("pricebook_entries", [])
            if f"{e.get('pricebook_id')}" == f"{pricebook_id}"
        ]

        subtotal = 0.0
        for item in cart_items:
            entry = next(
                (
                    e
                    for e in prices
                    if f"{e.get('product_id')}" == f"{item.get('product_id')}"
                ),
                None,
            )
            if not entry:
                payload = {"error": "Missing pricebook entry."}
                out = json.dumps(payload, indent=2)
                return out
            subtotal += float(entry.get("price", 0.0)) * int(item.get("quantity", 0))

        discount_amount = 0.0
        if offer_id:
            offer = next(
                (
                    o
                    for o in data.get("offers", [])
                    if f"{o.get('offer_id')}" == f"{offer_id}"
                    and o.get("is_active") is True
                ),
                None,
            )
            if offer:
                if offer.get("discount_type") == "PERCENTAGE":
                    discount_amount = round(
                        subtotal * (float(offer.get("discount_value", 0.0)) / 100.0), 2
                    )
                else:
                    discount_amount = float(offer.get("discount_value", 0.0))

        total_amount = round(subtotal - discount_amount, 2)

        new_order_id = _next_numeric_id(orders, "order_id")
        order = {
            "order_id": new_order_id,
            "contact_id": contact_id,
            "account_id": account_id,
            "applied_offer_id": offer_id,
            "order_date": "FIXED-DATE",
            "status": "Processing",
            "subtotal": round(subtotal, 2),
            "discount_amount": round(discount_amount, 2),
            "total_amount": total_amount,
            "shipping_address_used": (
                account.get("shipping_street") if account else None
            ),
        }
        orders.append(order)

        for item in cart_items:
            entry = next(
                (
                    e
                    for e in prices
                    if f"{e.get('product_id')}" == f"{item.get('product_id')}"
                ),
                None,
            )
            price = float(entry.get("price", 0.0))
            new_oi_id = _next_numeric_id(order_items, "order_item_id")
            order_items.append(
                {
                    "order_item_id": new_oi_id,
                    "order_id": new_order_id,
                    "product_id": item.get("product_id"),
                    "quantity": int(item.get("quantity")),
                    "price": price,
                }
            )
        payload = {"order_id": new_order_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createOrderFromCart",
                "description": "Creates a new order from a cart using the account's default pricebook and optional offer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "contact_id": {"type": "string"},
                        "account_id": {"type": "string"},
                        "offer_id": {"type": "string"},
                    },
                    "required": ["cart_id", "contact_id", "account_id"],
                },
            },
        }
