# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import FIXED_NOW, _find_one








def _idstr(v):
    """Coerce numeric IDs to strings; leave None/strings unchanged."""
    return str(v) if isinstance(v, int) else v

def _find_one(lst: List[Dict[str, Any]], key: str, value: Any) -> Dict[str, Any] | None:
    for x in lst or []:
        if x.get(key) == value:
            return x
    return None

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

class ProcessOrderWithFulfillment(Tool):
    """Create an order from cart and initiate fulfillment process."""

    @staticmethod
    def invoke(
        data: Dict[str, Any], order_id: Any, cart_id: Any, shipping_method: Any = "US-Std"
    ) -> str:
        order_id = _idstr(order_id)
        cart_id = _idstr(cart_id)
        if shipping_method == "Us-Std":
            shipping_method = "US-Std"
        if shipping_method == "Eu-Express":
            shipping_method = "EU-Express"
        try:
            shipping_method = (
                f"{shipping_method}".strip() if shipping_method is not None else "US-Std"
            )
        except Exception:
            shipping_method = "US-Std"

        if not shipping_method:
            rules = data.get("shipping_rules", [])
            rule = rules[-1] if rules else None
            if rule:
                shipping_method = rule.get("rule_name") or "US-Std"
        shipping_method = shipping_method.title()

        if not order_id or not cart_id:
            return _error("order_id and cart_id are required.")

        orders = list(data.get("orders", {}).values())
        existing = _find_one(orders, "order_id", order_id)
        if existing:
            return json.dumps(existing, indent=2)

        carts = data.get("carts", [])
        cart = _find_one(carts, "cart_id", cart_id)
        if not cart:
            return _error(f"Cart '{cart_id}' not found.")

        cart_items = data.get("cart_items", [])
        cart_line_items = [ci for ci in cart_items if f"{ci.get('cart_id')}" == f"{cart_id}"]
        if not cart_line_items:
            return _error("Cart has no items.")

        pricebook_entries = data.get("pricebook_entries", [])
        accounts = list(data.get("accounts", {}).values())
        offers = data.get("offers", [])
        products = list(data.get("products", {}).values())

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
                price = float(pbe.get("price", 0.0))
                qty = int(ci.get("quantity", 0))
                subtotal += price * qty
                product = _find_one(products, "product_id", ci.get("product_id"))
                if product:
                    current_stock = int(product.get("stock_quantity", 0))
                    if current_stock < qty:
                        return _error(f"Insufficient stock for product {ci.get('product_id')}")
                    product["stock_quantity"] = current_stock - qty

        discount_amount = 0.0
        applied_offer_id = cart.get("applied_offer_id")
        if applied_offer_id:
            offer = _find_one(offers, "offer_id", applied_offer_id)
            if offer and offer.get("is_active"):
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
            "account_id": cart.get("account_id"),
            "applied_offer_id": applied_offer_id,
            "order_date": FIXED_NOW,
            "status": "Processing",
            "subtotal": round(subtotal, 2),
            "discount_amount": round(discount_amount, 2),
            "total_amount": total,
            "shipping_method": shipping_method,
        }
        orders.append(new_order)

        order_items = data.setdefault("order_items", [])
        for idx, ci in enumerate(cart_line_items, start=1):
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
                order_items.append(
                    {
                        "order_item_id": f"{order_id}_item_{idx}",
                        "order_id": order_id,
                        "product_id": ci.get("product_id"),
                        "quantity": int(ci.get("quantity", 0)),
                        "price": float(pbe.get("price", 0.0)),
                    }
                )

        return json.dumps(new_order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_order_with_fulfillment",
                "description": "Create an order from cart, update inventory, and initiate fulfillment process. Standard shipping method is US-Std.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "cart_id": {"type": "string"},
                        "shipping_method": {"type": "string", "enum": ["US-Std", "EU-Std", "US-Priority", "EU-Priority", "US-Express", "EU-Express"]},
                    },
                    "required": ["order_id", "cart_id"],
                },
            },
        }