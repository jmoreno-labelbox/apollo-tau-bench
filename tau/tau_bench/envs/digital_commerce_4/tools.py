import json
import re
from typing import Any, Dict, List

from domains.dto import Tool

FIXED_NOW = "2025-08-06T12:00:00Z"


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
    def invoke(data: Dict[str, Any], category_id: Any) -> str:
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


class GetPricebookByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: Any) -> str:
        pricebooks = data.get("pricebooks", [])
        match = next((pb for pb in pricebooks if pb.get("pricebook_name") == name), None)
        return json.dumps(match or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pricebook_by_name",
                "description": "Resolve a pricebook by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class GetOfferByCode(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], code: Any) -> str:
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
    def invoke(data: Dict[str, Any], contact_id: Any) -> str:
        contact_id = _as_id(contact_id)
        if not contact_id:
            return _err("contact_id required.")

        contacts = data.get("contacts", [])
        contact = next((c for c in contacts if _as_id(c.get("contact_id")) == contact_id), None)
        if not contact:
            return _err("Contact not found.")

        carts = data.get("carts", [])
        numeric_ids = [int(c["cart_id"]) for c in carts if str(c.get("cart_id", "")).isdigit()]
        next_id = str(max(numeric_ids or [0]) + 1)

        cart = {
            "cart_id": next_id,
            "contact_id": contact_id,
            "account_id": contact.get("account_id"),
            "applied_offer_id": None,
            "override_pricebook_id": None,
            "last_updated_at": FIXED_NOW,
        }
        carts.append(cart)
        data["carts"] = carts
        return json.dumps(cart, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_cart",
                "description": "Create a cart for a contact; system auto-assigns the next numeric cart_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {
                            "type": "string",
                            "description": "Existing contact_id.",
                        },
                    },
                    "required": ["contact_id"],
                },
            },
        }


class AddItemToCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, product_id: Any, quantity: Any) -> str:
        cart_id = _as_id(cart_id)
        product_id = _as_id(product_id)
        if not cart_id or not product_id or quantity is None:
            return _err("cart_id, product_id, quantity are required.")
        qty = int(quantity)
        if qty <= 0:
            return _err("Quantity must be positive.")

        carts = data.get("carts", [])
        if not any(_as_id(c.get("cart_id")) == cart_id for c in carts):
            return _err("Cart not found.")

        products = data.get("products", [])
        if not any(_as_id(p.get("product_id")) == product_id for p in products):
            return _err("Product not found.")

        items = data.get("cart_items", [])
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
            data["cart_items"] = items
            return json.dumps({"cart_item_id": existing["cart_item_id"], "updated": True}, indent=2)

        next_id = str(
            max(
                [
                    int(ci["cart_item_id"])
                    for ci in items
                    if str(ci.get("cart_item_id", "")).isdigit()
                ]
                or [0]
            )
            + 1
        )
        line = {
            "cart_item_id": next_id,
            "cart_id": cart_id,
            "product_id": product_id,
            "quantity": qty,
        }
        items.append(line)
        data["cart_items"] = items
        return json.dumps({"cart_item_id": next_id, "updated": False}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_item_to_cart",
                "description": "Add a product to a cart (upsert by product). New lines receive the next numeric cart_item_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string", "description": "Existing cart_id."},
                        "product_id": {"type": "string", "description": "Target product_id."},
                        "quantity": {"type": "integer", "description": "Positive whole number."},
                    },
                    "required": ["cart_id", "product_id", "quantity"],
                },
            },
        }


class SetItemQuantity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_item_id: Any, quantity: Any) -> str:
        if not cart_item_id or quantity is None:
            return _err("cart_item_id and quantity are required.")
        cart_item_id = str(cart_item_id)
        items = data.get("cart_items", [])
        line = next((ci for ci in items if ci.get("cart_item_id") == cart_item_id), None)
        if not line:
            return _err("Cart item not found.")
        q = int(quantity)
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
                        "quantity": {"type": "integer"},
                    },
                    "required": ["cart_item_id", "quantity"],
                },
            },
        }


class RemoveItemFromCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, product_id: Any) -> str:
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
    def invoke(data: Dict[str, Any], cart_id: Any, code: Any) -> str:
        cart_id = _as_id(cart_id)
        if not cart_id or not code:
            return _err("cart_id and code are required.")

        carts = data.get("carts", [])
        cart = next((c for c in carts if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")

        offers = data.get("offers", [])
        offer = next(
            (o for o in offers if o.get("offer_code") == code and o.get("is_active") is True), None
        )
        if not offer:
            return _err("Offer not found or inactive.")

        cart["applied_offer_id"] = offer.get("offer_id")
        data["carts"] = carts
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
                "description": "Apply an active offer code to a cart (sets cart.applied_offer_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string", "description": "Existing cart_id."},
                        "code": {"type": "string", "description": "Valid offer_code."},
                    },
                    "required": ["cart_id", "code"],
                },
            },
        }


# --- add this class (e.g., below FindAccountByName) -------------------------


class GetAccountById(Tool):
    """Read an account by its account_id."""

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_account_by_id",
                "description": "Return a single account record for the given account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "The account_id to fetch."}
                    },
                    "required": ["account_id"],
                    "additionalProperties": False,
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: Any) -> str:
        accounts = data.get("accounts") or []
        target_id = str(account_id)
        result = {}
        for acc in accounts:
            if str(acc.get("account_id")) == target_id:
                result = acc
                break
        return json.dumps(result, indent=2)


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
        accounts = data.get("accounts", [])
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

        # auto-assign order_id if omitted
        orders = data.get("orders", [])
        if not order_id:
            numeric_ids = [
                int(o["order_id"]) for o in orders if str(o.get("order_id", "")).isdigit()
            ]
            order_id = str(max(numeric_ids or [0]) + 1)
        order_id = _as_id(order_id)

        # pricing context
        contacts = data.get("contacts", [])
        contact = next(
            (c for c in contacts if _as_id(c.get("contact_id")) == _as_id(cart.get("contact_id"))),
            None,
        )
        accounts = data.get("accounts", [])
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


class ListOrderItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: Any) -> str:
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
        if not isinstance(address, str):
            return _err("address must be a string.")

        order["shipping_address_used"] = address
        data["orders"] = orders
        return json.dumps({"order_id": order_id, "shipping_address_used": address}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_order_shipping_address",
                "description": "Attach a string shipping address to an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Target order_id."},
                        "address": {
                            "type": "string",
                            "description": "Full shipping address string.",
                        },
                    },
                    "required": ["order_id", "address"],
                },
            },
        }


class CancelOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: Any) -> str:
        order_id = _as_id(order_id)
        if not order_id:
            return _err("order_id required.")
        orders = data.get("orders", [])
        order = next((o for o in orders if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")
        order["status"] = "Cancelled"
        order["cancelled_at"] = FIXED_NOW
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
                    },
                    "required": ["order_id"],
                },
            },
        }


class CreateCase(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        order_id: Any,
        contact_id: Any,
        subject: Any,
    ) -> str:
        case_id = None
        if not order_id or not contact_id or not subject:
            return _err("order_id, contact_id, subject are required.")
        order_id = _as_id(order_id)
        contact_id = _as_id(contact_id)
        subject = subject.capitalize()

        cases = data.setdefault("cases", [])

        cid = _as_id(case_id)
        if not cid:
            nums = []
            for c in cases:
                existing = _as_id(c.get("case_id"))
                if existing is not None and str(existing).isdigit():
                    nums.append(int(existing))
            next_id = (max(nums) + 1) if nums else 5001
            cid = str(next_id)

        exist = next((c for c in cases if _as_id(c.get("case_id")) == cid), None)
        if exist:
            return json.dumps(exist, indent=2)

        case = {
            "case_id": cid,
            "order_id": order_id,
            "contact_id": contact_id,
            "subject": subject,
            "status": "New",
            "created_at": FIXED_NOW,
        }
        cases.append(case)
        return json.dumps(case, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_case",
                "description": "Create a support case linked to an order and contact. ",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "contact_id": {"type": "string"},
                        "subject": {"type": "string"},
                    },
                    "required": ["order_id", "contact_id", "subject"],
                },
            },
        }


class UpdateCaseStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], case_id: Any, status: Any) -> str:
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
    def invoke(data: Dict[str, Any], order_id: Any) -> str:
        if not order_id:
            return _err("order_id required.")
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
        }
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
                    },
                    "required": ["order_id"],
                },
            },
        }


class RefundOrderPartial(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: Any, amount: Any) -> str:
        if not order_id or amount is None:
            return _err("order_id and amount are required.")
        order_id = _as_id(order_id)

        orders = data.get("orders", [])
        order = next((o for o in orders if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")

        amt = round(float(amount), 2)
        current = float(order.get("total_amount", 0.0))
        if amt < 0:
            return _err("amount must be non-negative.")
        if amt > current:
            return _err("amount exceeds order total_amount.")

        order["total_amount"] = round(current - amt, 2)
        data["orders"] = orders
        return json.dumps(
            {
                "order_id": order_id,
                "refunded_amount": amt,
                "new_total_amount": order["total_amount"],
                "kind": "partial",
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "refund_order_partial",
                "description": "Reduce order total_amount by refund amount (clamped ≥ 0).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Target order_id."},
                        "amount": {
                            "type": "number",
                            "description": "Refund amount to subtract (≤ current total_amount).",
                        },
                    },
                    "required": ["order_id", "amount"],
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
        cluster_name: Any,
        endpoint_url: Any,
        status: Any,
        instance_type: Any,
        security_group_id: Any,
    ) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        existing = next((c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None)
        if existing:
            return json.dumps(existing, indent=2)

        rec = {
            "cluster_id": cluster_id,
            "cluster_name": str(cluster_name),
            "endpoint_url": str(endpoint_url),
            "status": str(status),
            "instance_type": str(instance_type),
            "security_group_id": _as_id(security_group_id),
        }
        clusters.append(rec)
        data["aws_elasticache_clusters"] = clusters
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "provision_elasticache_cluster",
                "description": "Create an ElastiCache cluster record with required fields only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string", "description": "New cluster_id string."},
                        "cluster_name": {"type": "string", "description": "Human-readable name."},
                        "endpoint_url": {
                            "type": "string",
                            "description": "Hostname:port or 'NULL' if failed.",
                        },
                        "status": {
                            "type": "string",
                            "description": "e.g., 'available', 'provisioning', 'failed'.",
                        },
                        "instance_type": {
                            "type": "string",
                            "description": "e.g., 'cache.t3.medium'.",
                        },
                        "security_group_id": {
                            "type": "string",
                            "description": "Security group that protects the cluster.",
                        },
                    },
                    "required": [
                        "cluster_id",
                        "cluster_name",
                        "endpoint_url",
                        "status",
                        "instance_type",
                        "security_group_id",
                    ],
                },
            },
        }


class UpdateElastiCacheInstanceType(Tool):
    """Update only the instance_type on an existing ElastiCache cluster record."""

    @staticmethod
    def invoke(data: Dict[str, Any], cluster_id: Any, instance_type: Any) -> str:
        if not cluster_id or not instance_type:
            return json.dumps({"error": "cluster_id and instance_type are required."}, indent=2)

        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        rec = next((c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None)
        if not rec:
            return json.dumps({"error": "Cluster not found."}, indent=2)

        rec["instance_type"] = str(instance_type)
        data["aws_elasticache_clusters"] = clusters
        return json.dumps(
            {"cluster_id": cluster_id, "instance_type": rec["instance_type"]}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_elasticache_instance_type",
                "description": "Update the instance_type on an ElastiCache cluster record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {
                            "type": "string",
                            "description": "Target cluster_id from aws_elasticache_clusters.",
                        },
                        "instance_type": {
                            "type": "string",
                            "description": "New instance class, e.g., 'cache.t3.medium'.",
                        },
                    },
                    "required": ["cluster_id", "instance_type"],
                },
            },
        }


class DeleteElastiCacheCluster(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cluster_id: Any) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        m = next((c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None)
        if not m:
            return _err("Cluster not found.")
        m["status"] = "Deleted"
        deleted_at = FIXED_NOW
        m["deleted_at"] = str(deleted_at)
        m["last_modified_at"] = str(deleted_at)
        return json.dumps({"cluster_id": cluster_id, "status": "Deleted"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_elasticache_cluster",
                "description": "Mark an ElastiCache cluster as Deleted.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                    },
                    "required": ["cluster_id"],
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


def _next_sgr_id(data: Dict[str, Any]) -> str:
    n = len(data.get("aws_security_group_rules", [])) + 1
    return "sgr-" + f"{n:016x}"


class AddSecurityGroupRule(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        security_group_id: Any,
        protocol: Any,
        port: Any,
        source_ip: Any,
    ) -> str:
        rid = _next_sgr_id(data)
        rules = data.get("aws_security_group_rules", [])
        rec = {
            "rule_id": rid,
            "security_group_id": _as_id(security_group_id),
            "protocol": str(protocol).upper(),
            "port": int(port),
            "source_ip": str(source_ip),
        }
        rules.append(rec)
        data["aws_security_group_rules"] = rules
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_security_group_rule",
                "description": "Add a rule to a security group (rule_id format: sgr- + 16 lowercase hex).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "security_group_id": {
                            "type": "string",
                            "description": "Target security group (sg-...).",
                        },
                        "protocol": {"type": "string", "description": "Protocol, e.g., 'TCP'."},
                        "port": {"type": "integer", "description": "Port number, e.g., 6379."},
                        "source_ip": {
                            "type": "string",
                            "description": "CIDR, e.g., '10.0.0.0/16'.",
                        },
                    },
                    "required": [
                        "security_group_id",
                        "protocol",
                        "port",
                        "source_ip",
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


class UpdateSubnetGroupDescription(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], subnet_group_id: Any, name: Any, description: Any) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = data.get("aws_subnet_groups", [])
        g = next((x for x in groups if _as_id(x.get("subnet_group_id")) == subnet_group_id), None)
        if not g:
            return _err("Subnet group not found.")
        g["name"] = str(name)
        g["description"] = str(description)
        return json.dumps(
            {
                "subnet_group_id": subnet_group_id,
                "name": g["name"],
                "description": g["description"],
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_subnet_group_description",
                "description": "Rename a subnet group and update its description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subnet_group_id": {"type": "string"},
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": ["subnet_group_id", "name", "description"],
                },
            },
        }


class UpdateElastiCacheClusterConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cluster_id: Any, node_type: Any, num_nodes: Any) -> str:
        changed_at = FIXED_NOW
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
                    },
                    "required": ["cluster_id", "node_type", "num_nodes"],
                },
            },
        }


class GetContactByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name: Any, last_name: Any) -> str:
        if not first_name or not last_name:
            return json.dumps({"error": "first_name and last_name are required."}, indent=2)
        fn = str(first_name).strip().lower()
        ln = str(last_name).strip().lower()
        contacts = data.get("contacts", [])
        matches = [
            c
            for c in contacts
            if str(c.get("first_name", "")).strip().lower() == fn
            and str(c.get("last_name", "")).strip().lower() == ln
        ]
        if not matches:
            return json.dumps({}, indent=2)

        # deterministic: lowest numeric contact_id wins if multiple
        def _key(c):
            s = str(c.get("contact_id", ""))
            try:
                return int(s)
            except Exception:
                return float("inf")

        return json.dumps(sorted(matches, key=_key)[0], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_contact_by_name",
                "description": "Return a contact by exact first and last name (includes contact_id and account_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "Exact first name from contacts.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Exact last name from contacts.",
                        },
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }


class ListOrdersForContact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: str) -> str:
        if not contact_id:
            return json.dumps({"error": "contact_id is required."}, indent=2)
        contact_id = _as_id(contact_id)
        rows = [o for o in data.get("orders", []) if _as_id(o.get("contact_id")) == contact_id]
        rows = sorted(rows, key=lambda o: str(o.get("order_date", "")), reverse=True)  # ISO desc
        return json.dumps({"orders": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_orders_for_contact",
                "description": "List orders for a contact_id, newest first.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string", "description": "Target contact_id."},
                    },
                    "required": ["contact_id"],
                },
            },
        }


class ListActiveOffers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        offers = [o for o in data.get("offers", []) if o.get("is_active") is True]
        return json.dumps({"offers": offers}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_active_offers",
                "description": "List all active offers (offer_code, discount_type/value).",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class GetDefaultPricebookForAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: Any) -> str:
        if not account_id:
            return json.dumps({"error": "account_id is required."}, indent=2)
        account_id = _as_id(account_id)
        acc = next(
            (a for a in data.get("accounts", []) if _as_id(a.get("account_id")) == account_id), None
        )
        if not acc:
            return json.dumps({}, indent=2)
        pbid = _as_id(acc.get("default_pricebook_id"))
        pb = next(
            (p for p in data.get("pricebooks", []) if _as_id(p.get("pricebook_id")) == pbid), None
        )
        return json.dumps({"account_id": account_id, "pricebook": (pb or {})}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_default_pricebook_for_account",
                "description": "Return the default pricebook record for an account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Target account_id."}
                    },
                    "required": ["account_id"],
                },
            },
        }


class ValidateReturnEligibility(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: Any) -> str:
        if not order_id:
            return json.dumps({"error": "order_id is required."}, indent=2)
        order_id = _as_id(order_id)
        order = next(
            (o for o in data.get("orders", []) if _as_id(o.get("order_id")) == order_id), None
        )
        if not order:
            return json.dumps({}, indent=2)
        status = str(order.get("status", ""))
        eligible_statuses = {"Delivered", "Completed"}  # align with SOP
        eligible = status in eligible_statuses
        out = {"order_id": order_id, "status": status, "eligible": eligible}
        if not eligible:
            out["reason"] = "Order status is not eligible for return."
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_return_eligibility",
                "description": "Check if an order is eligible for return based on status (Delivered/Completed).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Order to check."}
                    },
                    "required": ["order_id"],
                },
            },
        }


class ListCartsForContact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: Any) -> str:
        if not contact_id:
            return json.dumps({"error": "contact_id is required."}, indent=2)
        contact_id = _as_id(contact_id)
        carts = [c for c in data.get("carts", []) if _as_id(c.get("contact_id")) == contact_id]

        def _idnum(s):
            try:
                return int(str(s))
            except Exception:
                return 10**9

        carts.sort(
            key=lambda c: (str(c.get("last_updated_at", "")), -_idnum(c.get("cart_id"))),
            reverse=True,
        )
        return json.dumps({"contact_id": contact_id, "carts": carts}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_carts_for_contact",
                "description": "List carts for a contact, newest first.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string", "description": "Target contact_id."}
                    },
                    "required": ["contact_id"],
                },
            },
        }


class ListCartItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any) -> str:
        if not cart_id:
            return json.dumps({"error": "cart_id is required."}, indent=2)
        cart_id = _as_id(cart_id)
        rows = [ci for ci in data.get("cart_items", []) if _as_id(ci.get("cart_id")) == cart_id]
        # return minimal, deterministic fields
        items = [
            {
                "cart_item_id": r.get("cart_item_id"),
                "product_id": r.get("product_id"),
                "quantity": int(r.get("quantity", 0)),
            }
            for r in rows
        ]
        return json.dumps({"cart_id": cart_id, "items": items}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_cart_items",
                "description": "List items in a cart (cart_item_id, product_id, quantity).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string", "description": "Existing cart_id."}
                    },
                    "required": ["cart_id"],
                },
            },
        }


class ReturnOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: Any, lines: Any) -> str:
        order_id = _as_id(order_id)
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
                    },
                    "required": ["order_id", "lines"],
                },
            },
        }


TOOLS = [
    GetContactByEmail(),
    GetProductByName(),
    GetContactByName(),
    ListProductsInCategory(),
    GetPricebookByName(),
    GetOfferByCode(),
    CreateCart(),
    AddItemToCart(),
    SetItemQuantity(),
    RemoveItemFromCart(),
    ApplyOfferToCart(),
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
    UpdateElastiCacheInstanceType(),
    DeleteElastiCacheCluster(),
    ListSubnetGroups(),
    CreateSubnetGroup(),
    ListSecurityGroupRules(),
    AddSecurityGroupRule(),
    GetSubnetGroup(),
    UpdateSubnetGroupDescription(),
    UpdateElastiCacheClusterConfig(),
    ValidateReturnEligibility(),
    ListOrdersForContact(),
    ListActiveOffers(),
    GetDefaultPricebookForAccount(),
    ListCartsForContact(),
    ListCartItems(),
    GetAccountById(),
]
