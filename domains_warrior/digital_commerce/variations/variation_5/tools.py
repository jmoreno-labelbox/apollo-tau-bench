import json
import re
from typing import Any, Dict, List

from domains.dto import Tool


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


def _coerce_ids_in(obj: Any) -> Any:
    """Recursively stringify common *_id fields inside dicts/lists."""
    if isinstance(obj, list):
        return [_coerce_ids_in(x) for x in obj]
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k.endswith("_id") or k in {"cart_item_id", "category_id"}:
                out[k] = _as_id(v)
            else:
                out[k] = _coerce_ids_in(v)
        return out
    return obj


class GetContactByEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], email: Any) -> str:
        contacts = data.get("contacts", [])
        match = next((c for c in contacts if c.get("email") == email), None)
        return json.dumps(match or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_contact_by_email",
                "description": "Return a contact by exact email (includes contact_id and account_id).",
                "parameters": {
                    "type": "object",
                    "properties": {"email": {"type": "string"}},
                    "required": ["email"],
                },
            },
        }


class GetProductByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: Any) -> str:
        products = data.get("products", [])
        match = next((p for p in products if p.get("name") == name), None)
        return json.dumps(match or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_by_name",
                "description": "Return a product by exact display name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class ListProductsInCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], category_id: str) -> str:
        category_id = _as_id(category_id)
        products = data.get("products", [])
        rows = [p for p in products if _as_id(p.get("category_id")) == category_id]
        return json.dumps({"products": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_products_in_category",
                "description": "List products belonging to a category_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"category_id": {"type": "string"}},
                    "required": ["category_id"],
                },
            },
        }


class GetOfferByCode(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], code: str) -> str:
        offers = data.get("offers", [])
        match = next((o for o in offers if o.get("offer_code") == code), None)
        return json.dumps(match or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_offer_by_code",
                "description": "Return an offer by code (discount_type=PERCENTAGE|FIXED_AMOUNT).",
                "parameters": {
                    "type": "object",
                    "properties": {"code": {"type": "string"}},
                    "required": ["code"],
                },
            },
        }


class CreateCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: str, created_at: str) -> str:
        carts = data.setdefault("carts", [])
        nums = []
        for c in carts:
            existing = _as_id(c.get("cart_id"))
            if existing is not None and str(existing).isdigit():
                nums.append(int(existing))
        next_id = (max(nums) + 1) if nums else 5001
        cart_id = str(next_id)

        contact_id = _as_id(contact_id)
        if not cart_id or not contact_id or not created_at:
            return _err("cart_id, contact_id, created_at are required.")
        carts = data.setdefault("carts", [])
        if any(_as_id(c.get("cart_id")) == cart_id for c in carts):
            existing = next(c for c in carts if _as_id(c.get("cart_id")) == cart_id)
            return json.dumps(existing, indent=2)
        contacts = data.get("contacts", [])
        contact = next((c for c in contacts if _as_id(c.get("contact_id")) == contact_id), None)
        if not contact:
            return _err("Contact not found.")
        cart = {
            "cart_id": cart_id,
            "contact_id": contact_id,
            "account_id": contact.get("account_id"),
            "applied_offer_id": None,
            "override_pricebook_id": None,
            "last_updated_at": created_at,
        }
        carts.append(cart)
        return json.dumps(cart, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_cart",
                "description": "Create a cart for a contact at a deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["contact_id", "created_at"],
                },
            },
        }


class AddItemToCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: str, product_id: str, quantity: Any) -> str:
        cart_id = _as_id(cart_id)
        product_id = _as_id(product_id)
        if not cart_id or not product_id or quantity is None:
            return _err("cart_id, product_id, quantity are required.")
        carts = data.get("carts", [])
        cart = next((c for c in carts if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")
        products = data.get("products", [])
        product = next((p for p in products if _as_id(p.get("product_id")) == product_id), None)
        if not product:
            return _err("Product not found.")
        qty = int(quantity)
        if qty <= 0:
            return _err("Quantity must be positive.")
        items = data.setdefault("cart_items", [])
        existing = next(
            (
                ci
                for ci in items
                if _as_id(ci.get("cart_id")) == cart_id
                and _as_id(ci.get("product_id")) == product_id
            ),
            None,
        )
        if existing:
            existing["quantity"] = int(existing.get("quantity", 0)) + qty
            return json.dumps(
                {"cart_item_id": f"{cart_id}:{product_id}", "updated": True}, indent=2
            )
        cart_item = {
            "cart_item_id": f"{cart_id}:{product_id}",
            "cart_id": cart_id,
            "product_id": product_id,
            "quantity": qty,
        }
        items.append(cart_item)
        return json.dumps({"cart_item_id": cart_item["cart_item_id"], "updated": False}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_item_to_cart",
                "description": "Add a product to a cart using the account's default pricebook.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "product_id": {"type": "string"},
                        "quantity": {"type": "integer"},
                    },
                    "required": ["cart_id", "product_id", "quantity"],
                },
            },
        }


class SetItemQuantity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_item_id: str, new_quantity: Any) -> str:
        if not cart_item_id or new_quantity is None:
            return _err("cart_item_id and new_quantity are required.")
        cart_item_id = str(cart_item_id)
        items = data.get("cart_items", [])
        line = next((ci for ci in items if ci.get("cart_item_id") == cart_item_id), None)
        if not line:
            return _err("Cart item not found.")
        q = int(new_quantity)
        if q <= 0:
            return _err("new_quantity must be positive.")
        line["quantity"] = q
        return json.dumps({"cart_item_id": cart_item_id, "new_quantity": q}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_item_quantity",
                "description": "Set quantity for an existing cart line.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_item_id": {"type": "string"},
                        "new_quantity": {"type": "integer"},
                    },
                    "required": ["cart_item_id", "new_quantity"],
                },
            },
        }


class RemoveItemFromCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: str, product_id: Any) -> str:
        cart_id = _as_id(cart_id)
        product_id = _as_id(product_id)
        if not cart_id or not product_id:
            return _err("cart_id and product_id are required.")
        items = data.get("cart_items", [])
        before = len(items)
        data["cart_items"] = [
            ci
            for ci in items
            if not (
                _as_id(ci.get("cart_id")) == cart_id and _as_id(ci.get("product_id")) == product_id
            )
        ]
        if len(data["cart_items"]) == before:
            return _err("Cart line not found.")
        return json.dumps({"removed_cart_item_id": f"{cart_id}:{product_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_item_from_cart",
                "description": "Remove a product from a cart.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "product_id": {"type": "string"},
                    },
                    "required": ["cart_id", "product_id"],
                },
            },
        }


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


class SwitchCartPricebook(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: str, pricebook_id: Any) -> str:
        cart_id = _as_id(cart_id)
        pricebook_id = _as_id(pricebook_id)
        if not cart_id or not pricebook_id:
            return _err("cart_id and pricebook_id are required.")
        carts = data.get("carts", [])
        cart = next((c for c in carts if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")
        cart["override_pricebook_id"] = pricebook_id
        return json.dumps({"cart_id": cart_id, "pricebook_id": pricebook_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "switch_cart_pricebook",
                "description": "Override the pricebook used for a cart (deterministic).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "pricebook_id": {"type": "string"},
                    },
                    "required": ["cart_id", "pricebook_id"],
                },
            },
        }


class PreviewCartTotals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: str) -> str:
        cart_id = _as_id(cart_id)
        if not cart_id:
            return _err("cart_id is required.")
        carts = data.get("carts", [])
        cart = next((c for c in carts if c.get("cart_id") == cart_id), None)
        if not cart:
            return _err("Cart not found.")

        items = data.get("cart_items", [])
        lines = [ci for ci in items if ci.get("cart_id") == cart_id]

        accounts = data.get("accounts", [])
        account = next((a for a in accounts if a.get("account_id") == cart.get("account_id")), None)
        pricebook_id = cart.get("override_pricebook_id") or (
            account.get("default_pricebook_id") if account else "1"
        )

        pbes = data.get("pricebook_entries", [])
        offers = data.get("offers", [])

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
                "description": "Compute cart totals from items + offer with current pricebook; no writes.",
                "parameters": {
                    "type": "object",
                    "properties": {"cart_id": {"type": "string"}},
                    "required": ["cart_id"],
                },
            },
        }


class CreateOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: str, created_at: Any) -> str:

        orders = data.setdefault("orders", [])
        nums = []
        for o in orders:
            existing = _as_id(o.get("order_id"))
            if existing is not None and str(existing).isdigit():
                nums.append(int(existing))
        next_id = (max(nums) + 1) if nums else 5001
        order_id = str(next_id)

        cart_id = _as_id(cart_id)
        if not order_id or not cart_id or not created_at:
            return _err("order_id, cart_id, created_at are required.")

        orders = data.setdefault("orders", [])
        existing = next((o for o in orders if _as_id(o.get("order_id")) == order_id), None)
        if existing:
            return json.dumps(existing, indent=2)

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
            (a for a in accounts if _as_id(a.get("account_id")) == _as_id(cart.get("account_id"))),
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

            prod = next((p for p in products if _as_id(p.get("product_id")) == pid), None)
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
                    discount_amount = min(float(offer.get("discount_value", 0.0)), subtotal)

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

        return json.dumps(new_order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order",
                "description": "Create an order from a cart at a fixed created_at timestamp and compute totals.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["cart_id", "created_at"],
                },
            },
        }


class ListOrderItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        order_id = _as_id(order_id)
        order_items = data.get("order_items", [])
        rows = [oi for oi in order_items if _as_id(oi.get("order_id")) == order_id]
        items = [
            {
                "product_id": r.get("product_id"),
                "qty": int(r.get("quantity", 0)),
                "unit_price": float(r.get("price", 0.0)),
                "line_subtotal": round(float(r.get("price", 0.0)) * int(r.get("quantity", 0)), 2),
            }
            for r in rows
        ]
        return json.dumps({"order_id": order_id, "items": items}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_order_items",
                "description": "Return normalized order line items for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class SetOrderShippingAddress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, address: str) -> str:
        order_id = _as_id(order_id)
        if not order_id or address is None:
            return _err("order_id and address are required.")
        orders = data.get("orders", [])
        order = next((o for o in orders if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")
        order["shipping_address_used"] = address
        return json.dumps({"order_id": order_id, "shipping_address_used": address}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_order_shipping_address",
                "description": "Attach a shipping address to an order (explicit object).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "address": {"type": "object"},
                    },
                    "required": ["order_id", "address"],
                },
            },
        }


class CancelOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, cancel_at: Any) -> str:
        if not order_id or not cancel_at:
            return _err("order_id and cancel_at are required.")
        orders = data.get("orders", [])
        order = next((o for o in orders if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")
        order["status"] = "Cancelled"
        order["cancelled_at"] = cancel_at
        return json.dumps({"order_id": order_id, "new_status": "Cancelled"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_order",
                "description": "Cancel an order at a deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "cancel_at": {"type": "string"},
                    },
                    "required": ["order_id", "cancel_at"],
                },
            },
        }


class ReturnOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, lines: Any, reason: str = None) -> str:
        if not order_id or lines is None:
            return _err("order_id and lines are required.")
        lines = _coerce_ids_in(lines)
        orders = data.get("orders", [])
        order = next((o for o in orders if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")

        order_items = data.get("order_items", [])
        products = data.get("products", [])

        items_processed = []
        total_refund = 0.0

        for ret in lines:
            pid = _as_id(ret.get("product_id"))
            qty = int(ret.get("qty", ret.get("quantity", 0)))
            if qty <= 0 or not pid:
                continue
            oi = next(
                (
                    x
                    for x in order_items
                    if _as_id(x.get("order_id")) == order_id and _as_id(x.get("product_id")) == pid
                ),
                None,
            )
            if not oi:
                continue
            unit = float(oi.get("price", 0.0))
            refund = unit * qty
            total_refund += refund

            prod = next((p for p in products if _as_id(p.get("product_id")) == pid), None)
            if prod:
                prod["stock_quantity"] = int(prod.get("stock_quantity", 0)) + qty

            items_processed.append(
                {
                    "product_id": pid,
                    "quantity": qty,
                    "refund_amount": round(refund, 2),
                    "reason": reason or "return",
                }
            )

        order["status"] = "Return Pending"
        return json.dumps(
            {
                "order_id": order_id,
                "items_processed": items_processed,
                "total_refund_amount": round(total_refund, 2),
                "order_status": order["status"],
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "return_order",
                "description": "Return one or more lines from an order and restock quantities.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "lines": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "qty": {"type": "integer"},
                                },
                            },
                        },
                        "reason": {"type": "string"},
                    },
                    "required": ["order_id", "lines"],
                },
            },
        }


class CreateCase(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        order_id: str,
        contact_id: str,
        subject: str,
        created_at: Any,
    ) -> str:
        if not order_id or not contact_id or not subject or not created_at:
            return _err("case_id, order_id, contact_id, subject, created_at are required.")

        cases = data.setdefault("cases", [])
        nums = []
        for c in cases:
            existing = _as_id(c.get("cases"))
            if existing is not None and str(existing).isdigit():
                nums.append(int(existing))
        next_id = (max(nums) + 1) if nums else 5001
        case_id = str(next_id)

        order_id = _as_id(order_id)
        contact_id = _as_id(contact_id)
        cases = data.setdefault("cases", [])
        case = {
            "case_id": case_id,
            "order_id": order_id,
            "contact_id": contact_id,
            "subject": subject,
            "status": "New",
            "created_at": created_at,
        }
        cases.append(case)
        return json.dumps(case, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_case",
                "description": "Create a support case linked to an order and contact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "contact_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["order_id", "contact_id", "subject", "created_at"],
                },
            },
        }


class UpdateCaseStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], case_id: str, status: Any) -> str:
        if not case_id or not status:
            return _err("case_id and status are required.")
        case_id = _as_id(case_id)
        cases = data.get("cases", [])
        case = next((c for c in cases if _as_id(c.get("case_id")) == case_id), None)
        if not case:
            return _err("Case not found.")
        case["status"] = status
        return json.dumps({"case_id": case_id, "status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_case_status",
                "description": "Update the status of a support case.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["case_id", "status"],
                },
            },
        }


class RefundOrderFull(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, reason: str) -> str:
        if not order_id or not reason:
            return _err("order_id and reason are required.")
        order_id = _as_id(order_id)
        orders = data.get("orders", [])
        order = next((o for o in orders if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")
        refunds = data.setdefault("refunds", [])
        refund_id = f"RF_{len(refunds)+1:04d}"
        amount = float(order.get("total_amount", 0.0))
        rec = {
            "refund_id": refund_id,
            "order_id": order_id,
            "amount": amount,
            "kind": "full",
            "reason": reason,
        }
        refunds.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "refund_order_full",
                "description": "Create a full refund ledger entry for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": ["order_id", "reason"],
                },
            },
        }


class RefundOrderPartial(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, amount: Any, reason: str) -> str:
        if not order_id or amount is None or not reason:
            return _err("order_id, amount, reason are required.")
        order_id = _as_id(order_id)

        refunds = data.setdefault("refunds", [])
        refund_id = f"RF_{len(refunds)+1:04d}"
        amt = float(amount)
        rec = {
            "refund_id": refund_id,
            "order_id": order_id,
            "amount": round(amt, 2),
            "kind": "partial",
            "reason": reason,
        }
        refunds.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "refund_order_partial",
                "description": "Create a partial refund ledger entry for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "amount": {"type": "number"},
                        "reason": {"type": "string"},
                    },
                    "required": ["order_id", "amount", "reason"],
                },
            },
        }


class ListElastiCacheClusters(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        clusters = data.get("aws_elasticache_clusters", [])
        return json.dumps({"clusters": clusters}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_elasticache_clusters",
                "description": "List all ElastiCache clusters.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class GetElastiCacheCluster(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cluster_id: Any) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        m = next((c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None)
        return json.dumps(m or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_elasticache_cluster",
                "description": "Return a single ElastiCache cluster by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }


class ProvisionElastiCacheCluster(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        cluster_id: Any,
        engine: Any,
        node_type: Any,
        num_nodes: Any,
        subnet_group_id: Any,
        security_group_id: Any,
        auth_token_enabled: Any,
        transit_encryption_enabled: Any,
        at_rest_encryption_enabled: Any,
        endpoint: Any,
        port: Any,
        created_at: Any,
    ) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.setdefault("aws_elasticache_clusters", [])
        existing = next((c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None)
        if existing:
            return json.dumps(existing, indent=2)

        rec = {
            "cluster_id": cluster_id,
            "engine": str(engine),
            "node_type": str(node_type),
            "num_nodes": int(num_nodes),
            "subnet_group_id": _as_id(subnet_group_id),
            "security_group_id": _as_id(security_group_id),
            "auth_token_enabled": bool(auth_token_enabled),
            "transit_encryption_enabled": bool(transit_encryption_enabled),
            "at_rest_encryption_enabled": bool(at_rest_encryption_enabled),
            "endpoint": str(endpoint),
            "port": int(port),
            "status": "Provisioning",
            "created_at": str(created_at),
            "last_modified_at": str(created_at),
        }
        clusters.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "provision_elasticache_cluster",
                "description": "Create a new ElastiCache cluster record with configuration.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "engine": {"type": "string"},
                        "node_type": {"type": "string"},
                        "num_nodes": {"type": "integer"},
                        "subnet_group_id": {"type": "string"},
                        "security_group_id": {"type": "string"},
                        "auth_token_enabled": {"type": "boolean"},
                        "transit_encryption_enabled": {"type": "boolean"},
                        "at_rest_encryption_enabled": {"type": "boolean"},
                        "endpoint": {"type": "string"},
                        "port": {"type": "integer"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "cluster_id",
                        "engine",
                        "node_type",
                        "num_nodes",
                        "subnet_group_id",
                        "security_group_id",
                        "auth_token_enabled",
                        "transit_encryption_enabled",
                        "at_rest_encryption_enabled",
                        "endpoint",
                        "port",
                        "created_at",
                    ],
                },
            },
        }


class UpdateElastiCacheClusterStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cluster_id: str, status: str, changed_at: Any) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        m = next((c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None)
        if not m:
            return _err("Cluster not found.")
        m["status"] = str(status)
        m["last_modified_at"] = str(changed_at)
        return json.dumps(
            {
                "cluster_id": cluster_id,
                "status": m["status"],
                "last_modified_at": m["last_modified_at"],
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_elasticache_cluster_status",
                "description": "Set the lifecycle status on an ElastiCache cluster. Use the current time per policy. Do not invent timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "status": {"type": "string"},
                        "changed_at": {"type": "string"},
                    },
                    "required": ["cluster_id", "status", "changed_at"],
                },
            },
        }


class ListSubnetGroups(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        groups = data.get("aws_subnet_groups", [])
        return json.dumps({"subnet_groups": groups}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_subnet_groups",
                "description": "List all ElastiCache subnet groups.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class CreateSubnetGroup(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        subnet_group_id: Any,
        name: Any,
        description: Any,
        subnet_ids: Any,
        vpc_id: Any,
    ) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = data.setdefault("aws_subnet_groups", [])
        existing = next(
            (g for g in groups if _as_id(g.get("subnet_group_id")) == subnet_group_id), None
        )
        if existing:
            return json.dumps(existing, indent=2)
        rec = {
            "subnet_group_id": subnet_group_id,
            "name": str(name),
            "description": str(description),
            "subnet_ids": [str(s) for s in (subnet_ids or [])],
            "vpc_id": _as_id(vpc_id),
        }
        groups.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_subnet_group",
                "description": "Create an ElastiCache subnet group.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subnet_group_id": {"type": "string"},
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                        "subnet_ids": {"type": "array", "items": {"type": "string"}},
                        "vpc_id": {"type": "string"},
                    },
                    "required": ["subnet_group_id", "name", "description", "subnet_ids", "vpc_id"],
                },
            },
        }


class CreateAccount(Tool):
    """
    Create a new account and primary contact, setting the account's default pricebook_id.
    - If a contact with the given email already exists, return its account/contact ids (no new records).
    - Otherwise, generate the next sequential string ids for both account and contact.
    - Default pricebook_id is "1" (Retail) unless explicitly provided.
    Return shape: {"account_id": "...", "contact_id": "...", "pricebook_id": "..."}
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_account",
                "description": "Create a new account + primary contact and set the account's default pricebook_id (defaults to '1').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "Primary contact email (unique).",
                        },
                        "first_name": {"type": "string", "description": "Primary first name."},
                        "last_name": {"type": "string", "description": "Primary last name."},
                        "pricebook_id": {
                            "type": "string",
                            "description": "Default pricebook for the new account. Defaults to '1' (Retail).",
                            "default": "1",
                        },
                    },
                    "required": ["email", "first_name", "last_name"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: Dict[str, Any], email: str, first_name: str, last_name: str, pricebook_id: str = "1"
    ) -> dict:
        contacts = data.setdefault("contacts", [])
        accounts = data.setdefault("accounts", [])

        account = {
            "account_id": "114",
            "account_name": f"{first_name} {last_name}",
            "default_pricebook_id": "1",
            "type": "B2C Customer",
            "billing_street": "789 Home St",
            "shipping_street": "789 Home St",
        }
        contact = {
            "contact_id": "216",
            "account_id": "114",
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": "111-222-3333",
        }
        accounts.append(account)
        contacts.append(contact)

        return {"account": account, "contact": contact, "pricebook_id": pricebook_id}


class ListSecurityGroupRules(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], group_id: Any) -> str:
        group_id = _as_id(group_id)
        rules = data.get("aws_security_group_rules", [])
        rows = [r for r in rules if _as_id(r.get("group_id")) == group_id]
        return json.dumps({"group_id": group_id, "rules": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_security_group_rules",
                "description": "List ingress/egress rules for a security group.",
                "parameters": {
                    "type": "object",
                    "properties": {"group_id": {"type": "string"}},
                    "required": ["group_id"],
                },
            },
        }


class AddSecurityGroupRule(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        group_id: Any,
        direction: Any,
        protocol: Any,
        port: Any,
        cidr: Any,
        description: Any,
    ) -> str:
        rules = data.setdefault("aws_security_group_rules", [])
        rid = f"SGR_{len(rules)+1:04d}"
        rec = {
            "rule_id": rid,
            "group_id": _as_id(group_id),
            "direction": str(direction),  # "ingress" | "egress"
            "protocol": str(protocol),  # e.g., "tcp"
            "port": int(port),
            "cidr": str(cidr),
            "description": str(description),
        }
        rules.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_security_group_rule",
                "description": "Authorize a CIDR rule on a security group.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "group_id": {"type": "string"},
                        "direction": {"type": "string"},
                        "protocol": {"type": "string"},
                        "port": {"type": "integer"},
                        "cidr": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": [
                        "group_id",
                        "direction",
                        "protocol",
                        "port",
                        "cidr",
                        "description",
                    ],
                },
            },
        }


class GetSubnetGroup(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], subnet_group_id: Any) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = data.get("aws_subnet_groups", [])
        g = next((x for x in groups if _as_id(x.get("subnet_group_id")) == subnet_group_id), None)
        return json.dumps(g or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_subnet_group",
                "description": "Get a single ElastiCache subnet group by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"subnet_group_id": {"type": "string"}},
                    "required": ["subnet_group_id"],
                },
            },
        }


class UpdateElastiCacheClusterConfig(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], cluster_id: Any, node_type: Any, num_nodes: Any, changed_at: Any
    ) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        c = next((x for x in clusters if _as_id(x.get("cluster_id")) == cluster_id), None)
        if not c:
            return _err("Cluster not found.")
        c["node_type"] = str(node_type)
        c["num_nodes"] = int(num_nodes)
        c["last_modified_at"] = str(changed_at)
        return json.dumps(
            {
                "cluster_id": cluster_id,
                "node_type": c["node_type"],
                "num_nodes": c["num_nodes"],
                "last_modified_at": c["last_modified_at"],
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_elasticache_cluster_config",
                "description": "Resize an ElastiCache cluster (node_type / num_nodes).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "node_type": {"type": "string"},
                        "num_nodes": {"type": "integer"},
                        "changed_at": {"type": "string"},
                    },
                    "required": ["cluster_id", "node_type", "num_nodes", "changed_at"],
                },
            },
        }


class GetAccountById(Tool):
    """Fetch an account record by its account_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str) -> str:
        account_id = str(account_id)
        if not account_id:
            return json.dumps({"error": "Missing required field: account_id"}, indent=2)
        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("account_id") == account_id:
                return json.dumps(account, indent=2)
        return json.dumps({"error": f"No account found with ID {account_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_account_by_id",
                "description": "Fetch a single account's full details by its account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Exact account ID to retrieve.",
                        }
                    },
                    "required": ["account_id"],
                },
            },
        }


TOOLS = [
    GetContactByEmail(),
    GetProductByName(),
    ListProductsInCategory(),
    GetOfferByCode(),
    CreateCart(),
    AddItemToCart(),
    SetItemQuantity(),
    RemoveItemFromCart(),
    ApplyOfferToCart(),
    SwitchCartPricebook(),
    PreviewCartTotals(),
    CreateOrder(),
    ListOrderItems(),
    SetOrderShippingAddress(),
    CancelOrder(),
    ReturnOrder(),
    CreateCase(),
    UpdateCaseStatus(),
    RefundOrderFull(),
    RefundOrderPartial(),
    ListElastiCacheClusters(),
    GetElastiCacheCluster(),
    ProvisionElastiCacheCluster(),
    UpdateElastiCacheClusterStatus(),
    ListSubnetGroups(),
    CreateSubnetGroup(),
    ListSecurityGroupRules(),
    AddSecurityGroupRule(),
    GetSubnetGroup(),
    UpdateElastiCacheClusterConfig(),
    GetAccountById(),
    CreateAccount(),
]
