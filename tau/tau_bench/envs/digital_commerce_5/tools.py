import json
import re
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def _coerce_ids_in(obj: Any) -> Any:
    """Convert common *_id fields within dictionaries/lists to strings recursively."""
    pass
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


def _err(msg: str) -> str:
    pass
    payload = {"error": msg}
    out = json.dumps(payload, indent=2)
    return out


def _as_id(x: Any) -> str:
    pass
    if x is None:
        return x
    if isinstance(x, str):
        return x
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)


class GetContactByEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], email: Any) -> str:
        contacts = data.get("contacts", {}).values()
        match = next((c for c in contacts.values() if c.get("email") == email), None)
        payload = match or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetContactByEmail",
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
    def invoke(data: dict[str, Any], name: Any) -> str:
        products = data.get("products", {}).values()
        match = next((p for p in products.values() if p.get("name") == name), None)
        payload = match or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductByName",
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
    def invoke(data: dict[str, Any], category_id: Any, products: list = None) -> str:
        if products is None:
            products = data.get("products", {}).values()
        category_id = _as_id(category_id)
        rows = [p for p in products.values() if _as_id(p.get("category_id")) == category_id]
        payload = {"products": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListProductsInCategory",
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
    def invoke(data: dict[str, Any], name: Any) -> str:
        pricebooks = data.get("pricebooks", {}).values()
        match = next(
            (pb for pb in pricebooks.values() if pb.get("pricebook_name") == name), None
        )
        payload = match or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPricebookByName",
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
    def invoke(data: dict[str, Any], code: Any) -> str:
        offers = data.get("offers", {}).values()
        match = next((o for o in offers.values() if o.get("offer_code") == code), None)
        payload = match or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOfferByCode",
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
    def invoke(
        data: dict[str, Any], cart_id: Any, contact_id: Any, created_at: Any
    ) -> str:
        cart_id = _as_id(cart_id)
        contact_id = _as_id(contact_id)
        if not cart_id or not contact_id or not created_at:
            return _err("cart_id, contact_id, created_at are required.")
        carts = data.setdefault("carts", [])
        if any(_as_id(c.get("cart_id")) == cart_id for c in carts.values()):
            existing = next(c for c in carts.values() if _as_id(c.get("cart_id")) == cart_id)
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        contacts = data.get("contacts", {}).values()
        contact = next(
            (c for c in contacts.values() if _as_id(c.get("contact_id")) == contact_id), None
        )
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
        data["carts"][cart_id] = cart
        payload = cart
        out = json.dumps(payload, indent=2)
        return out
            

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCart",
                "description": "Create a cart for a contact at a deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "contact_id": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["cart_id", "contact_id", "created_at"],
                },
            },
        }


class AddItemToCart(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], cart_id: Any, product_id: Any, quantity: Any
    ) -> str:
        cart_id = _as_id(cart_id)
        product_id = _as_id(product_id)
        if not cart_id or not product_id or quantity is None:
            return _err("cart_id, product_id, quantity are required.")
        carts = data.get("carts", {}).values()
        cart = next((c for c in carts.values() if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")
        products = data.get("products", {}).values()
        product = next(
            (p for p in products.values() if _as_id(p.get("product_id")) == product_id), None
        )
        if not product:
            return _err("Product not found.")
        qty = int(quantity)
        if qty <= 0:
            return _err("Quantity must be positive.")
        items = data.setdefault("cart_items", [])
        existing = next(
            (
                ci
                for ci in items.values() if _as_id(ci.get("cart_id")) == cart_id
                and _as_id(ci.get("product_id")) == product_id
            ),
            None,
        )
        if existing:
            existing["quantity"] = int(existing.get("quantity", 0)) + qty
            payload = {"cart_item_id": f"{cart_id}:{product_id}", "updated": True}
            out = json.dumps(
                payload, indent=2
            )
            return out
        cart_item = {
            "cart_item_id": f"{cart_id}:{product_id}",
            "cart_id": cart_id,
            "product_id": product_id,
            "quantity": qty,
        }
        data["cart_items"][cart_item_id] = cart_item
        payload = {"cart_item_id": cart_item["cart_item_id"], "updated": False}
        out = json.dumps(
            payload, indent=2
        )
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddItemToCart",
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
    def invoke(data: dict[str, Any], cart_item_id: Any, new_quantity: Any) -> str:
        if not cart_item_id or new_quantity is None:
            return _err("cart_item_id and new_quantity are required.")
        cart_item_id = str(cart_item_id)
        items = data.get("cart_items", {}).values()
        line = next(
            (ci for ci in items.values() if ci.get("cart_item_id") == cart_item_id), None
        )
        if not line:
            return _err("Cart item not found.")
        q = int(new_quantity)
        if q <= 0:
            return _err("new_quantity must be positive.")
        line["quantity"] = q
        payload = {"cart_item_id": cart_item_id, "new_quantity": q}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetItemQuantity",
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
    def invoke(data: dict[str, Any], cart_id: Any, product_id: Any) -> str:
        cart_id = _as_id(cart_id)
        product_id = _as_id(product_id)
        if not cart_id or not product_id:
            return _err("cart_id and product_id are required.")
        items = data.get("cart_items", {}).values()
        before = len(items)
        data["cart_items"] = [
            ci
            for ci in items.values() if not (
                _as_id(ci.get("cart_id")) == cart_id
                and _as_id(ci.get("product_id")) == product_id
            )
        ]
        if len(data["cart_items"]) == before:
            return _err("Cart line not found.")
        payload = {"removed_cart_item_id": f"{cart_id}:{product_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveItemFromCart",
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
    def invoke(data: dict[str, Any], carts: list = None, offers: list = None, cart_id: Any = None, code: Any = None) -> str:
        if carts is None:
            carts = data.get("carts", {}).values()
        if offers is None:
            offers = data.get("offers", {}).values()

        cart_id = _as_id(cart_id)
        if not cart_id or not code:
            return _err("cart_id and code are required.")

        cart = next((c for c in carts.values() if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")

        offer = next(
            (
                o
                for o in offers.values() if o.get("offer_code") == code and o.get("is_active") is True
            ),
            None,
        )
        if not offer:
            return _err("Offer not found or inactive.")

        cart["applied_offer_id"] = offer.get("offer_id")
        payload = {
            "cart_id": cart_id,
            "applied_offer_id": cart["applied_offer_id"],
            "code": code,
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
                "name": "ApplyOfferToCart",
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
    def invoke(data: dict[str, Any], cart_id: Any, pricebook_id: Any) -> str:
        cart_id = _as_id(cart_id)
        pricebook_id = _as_id(pricebook_id)
        if not cart_id or not pricebook_id:
            return _err("cart_id and pricebook_id are required.")
        carts = data.get("carts", {}).values()
        cart = next((c for c in carts.values() if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")
        cart["override_pricebook_id"] = pricebook_id
        payload = {"cart_id": cart_id, "pricebook_id": pricebook_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SwitchCartPricebook",
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
        cart = next((c for c in carts.values() if c.get("cart_id") == cart_id), None)
        if not cart:
            return _err("Cart not found.")

        items = cart_items or []
        lines = [ci for ci in items.values() if ci.get("cart_id") == cart_id]

        accounts = accounts or []
        account = next(
            (a for a in accounts.values() if a.get("account_id") == cart.get("account_id")), None
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
                    for e in pbes.values() if e.get("pricebook_id") == pricebook_id
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
                    for o in offers.values() if o.get("offer_id") == cart.get("applied_offer_id")
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
            (o for o in orders.values() if _as_id(o.get("order_id")) == order_id), None
        )
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out

        carts = data.get("carts", {}).values()
        cart = next((c for c in carts.values() if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")

        cart_items = data.get("cart_items", {}).values()
        lines = [ci for ci in cart_items.values() if _as_id(ci.get("cart_id")) == cart_id]
        if not lines:
            return _err("Cart has no items.")

        accounts = data.get("accounts", {}).values()
        account = next(
            (
                a
                for a in accounts.values() if _as_id(a.get("account_id")) == _as_id(cart.get("account_id"))
            ),
            None,
        )
        pricebook_id = cart.get("override_pricebook_id") or (
            account.get("default_pricebook_id") if account else "1"
        )
        pbes = data.get("pricebook_entries", {}).values()
        offers = data.get("offers", {}).values()
        products = data.get("products", {}).values()

        subtotal = 0.0
        for li in lines:
            pid = _as_id(li.get("product_id"))
            pbe = next(
                (
                    e
                    for e in pbes.values() if _as_id(e.get("pricebook_id")) == _as_id(pricebook_id)
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
                (p for p in products.values() if _as_id(p.get("product_id")) == pid), None
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
                    for o in offers.values() if _as_id(o.get("offer_id")) == _as_id(cart.get("applied_offer_id"))
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
        data["orders"][order_id] = new_order

        order_items = data.setdefault("order_items", [])
        for idx, li in enumerate(lines, start=1):
            pid = _as_id(li.get("product_id"))
            pbe = next(
                (
                    e
                    for e in pbes.values() if _as_id(e.get("pricebook_id")) == _as_id(pricebook_id)
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


class GetOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any) -> str:
        order_id = _as_id(order_id)
        orders = data.get("orders", {}).values()
        match = next((o for o in orders.values() if _as_id(o.get("order_id")) == order_id), None)
        payload = match or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrder",
                "description": "Return an order by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class ListOrderItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, order_items: list[dict[str, Any]] = None) -> str:
        order_id = _as_id(order_id)
        order_items = order_items if order_items is not None else data.get("order_items", {}).values()
        rows = [oi for oi in order_items.values() if _as_id(oi.get("order_id")) == order_id]
        items = [
            {
                "product_id": r.get("product_id"),
                "qty": int(r.get("quantity", 0)),
                "unit_price": float(r.get("price", 0.0)),
                "line_subtotal": round(
                    float(r.get("price", 0.0)) * int(r.get("quantity", 0)), 2
                ),
            }
            for r in rows
        ]
        payload = {"order_id": order_id, "items": items}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListOrderItems",
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
    def invoke(data: dict[str, Any], order_id: Any, address: Any) -> str:
        order_id = _as_id(order_id)
        if not order_id or address is None:
            return _err("order_id and address are required.")
        orders = data.get("orders", {}).values()
        order = next((o for o in orders.values() if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")
        order["shipping_address_used"] = address
        payload = {"order_id": order_id, "shipping_address_used": address}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetOrderShippingAddress",
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
    def invoke(data: dict[str, Any], order_id: Any, cancel_at: Any) -> str:
        order_id = _as_id(order_id)
        if not order_id or not cancel_at:
            return _err("order_id and cancel_at are required.")
        orders = data.get("orders", {}).values()
        order = next((o for o in orders.values() if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")
        order["status"] = "Cancelled"
        order["cancelled_at"] = cancel_at
        payload = {"order_id": order_id, "new_status": "Cancelled"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CancelOrder",
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
    def invoke(
        data: dict[str, Any], order_id: Any, lines: Any, reason: Any = None
    ) -> str:
        order_id = _as_id(order_id)
        if not order_id or lines is None:
            return _err("order_id and lines are required.")
        lines = _coerce_ids_in(lines)
        orders = data.get("orders", {}).values()
        order = next((o for o in orders.values() if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")

        order_items = data.get("order_items", {}).values()
        products = data.get("products", {}).values()

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
                    for x in order_items.values() if _as_id(x.get("order_id")) == order_id
                    and _as_id(x.get("product_id")) == pid
                ),
                None,
            )
            if not oi:
                continue
            unit = float(oi.get("price", 0.0))
            refund = unit * qty
            total_refund += refund

            prod = next(
                (p for p in products.values() if _as_id(p.get("product_id")) == pid), None
            )
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
        payload = {
                "order_id": order_id,
                "items_processed": items_processed,
                "total_refund_amount": round(total_refund, 2),
                "order_status": order["status"],
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
                "name": "ReturnOrder",
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
        data: dict[str, Any],
        case_id: Any,
        order_id: Any,
        contact_id: Any,
        subject: Any,
        created_at: Any,
    ) -> str:
        if (
            not case_id
            or not order_id
            or not contact_id
            or not subject
            or not created_at
        ):
            return _err(
                "case_id, order_id, contact_id, subject, created_at are required."
            )
        case_id = _as_id(case_id)
        order_id = _as_id(order_id)
        contact_id = _as_id(contact_id)
        cases = data.setdefault("cases", [])
        exist = next((c for c in cases.values() if _as_id(c.get("case_id")) == case_id), None)
        if exist:
            payload = exist
            out = json.dumps(payload, indent=2)
            return out
        case = {
            "case_id": case_id,
            "order_id": order_id,
            "contact_id": contact_id,
            "subject": subject,
            "status": "New",
            "created_at": created_at,
        }
        data["cases"][case_id] = case
        payload = case
        out = json.dumps(payload, indent=2)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCase",
                "description": "Create a support case linked to an order and contact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_id": {"type": "string"},
                        "order_id": {"type": "string"},
                        "contact_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "case_id",
                        "order_id",
                        "contact_id",
                        "subject",
                        "created_at",
                    ],
                },
            },
        }


class UpdateCaseStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], case_id: Any, status: Any) -> str:
        if not case_id or not status:
            return _err("case_id and status are required.")
        case_id = _as_id(case_id)
        cases = data.get("cases", {}).values()
        case = next((c for c in cases.values() if _as_id(c.get("case_id")) == case_id), None)
        if not case:
            return _err("Case not found.")
        case["status"] = status
        payload = {"case_id": case_id, "status": status}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCaseStatus",
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
    def invoke(data: dict[str, Any], order_id: Any, reason: Any) -> str:
        if not order_id or not reason:
            return _err("order_id and reason are required.")
        order_id = _as_id(order_id)
        orders = data.get("orders", {}).values()
        order = next((o for o in orders.values() if _as_id(o.get("order_id")) == order_id), None)
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
        data["refunds"][rec["refund_id"]] = rec
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RefundOrderFull",
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
    def invoke(data: dict[str, Any], order_id: Any, amount: Any, reason: Any) -> str:
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
        data["refunds"][rec["refund_id"]] = rec
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RefundOrderPartial",
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


#--- AWS: ElastiCache / Subnet Groups / Security Group Regulations -----------------
from typing import Any

#(reuse _err, _as_id from your document)


class ListElastiCacheClusters(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], aws_elasticache_clusters: list = None) -> str:
        clusters = aws_elasticache_clusters if aws_elasticache_clusters is not None else []
        payload = {"clusters": clusters}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListElasticacheClusters",
                "description": "List all ElastiCache clusters.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class GetElastiCacheCluster(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, aws_elasticache_clusters: list = None) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = aws_elasticache_clusters or []
        m = next(
            (c for c in clusters.values() if _as_id(c.get("cluster_id")) == cluster_id), None
        )
        payload = m or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetElasticacheCluster",
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
        data: dict[str, Any],
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
        existing = next(
            (c for c in clusters.values() if _as_id(c.get("cluster_id")) == cluster_id), None
        )
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out

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
        data["aws_elasticache_clusters"][rec["aws_elasticache_cluster_id"]] = rec
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProvisionElasticacheCluster",
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
    def invoke(
        data: dict[str, Any], cluster_id: Any, status: Any, changed_at: Any
    ) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", {}).values()
        m = next(
            (c for c in clusters.values() if _as_id(c.get("cluster_id")) == cluster_id), None
        )
        if not m:
            return _err("Cluster not found.")
        m["status"] = str(status)
        m["last_modified_at"] = str(changed_at)
        payload = {
            "cluster_id": cluster_id,
            "status": m["status"],
            "last_modified_at": m["last_modified_at"],
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
                "name": "UpdateElasticacheClusterStatus",
                "description": "Set the lifecycle status on an ElastiCache cluster.",
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


class DeleteElastiCacheCluster(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, deleted_at: Any) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", {}).values()
        m = next(
            (c for c in clusters.values() if _as_id(c.get("cluster_id")) == cluster_id), None
        )
        if not m:
            return _err("Cluster not found.")
        m["status"] = "Deleted"
        m["deleted_at"] = str(deleted_at)
        m["last_modified_at"] = str(deleted_at)
        payload = {"cluster_id": cluster_id, "status": "Deleted"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteElasticacheCluster",
                "description": "Mark an ElastiCache cluster as Deleted.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "deleted_at": {"type": "string"},
                    },
                    "required": ["cluster_id", "deleted_at"],
                },
            },
        }


class ListSubnetGroups(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], aws_subnet_groups: list = None) -> str:
        groups = aws_subnet_groups if aws_subnet_groups is not None else []
        payload = {"subnet_groups": groups}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSubnetGroups",
                "description": "List all ElastiCache subnet groups.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class CreateSubnetGroup(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        subnet_group_id: Any,
        name: Any,
        description: Any,
        subnet_ids: Any,
        vpc_id: Any,
    ) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = data.setdefault("aws_subnet_groups", [])
        existing = next(
            (g for g in groups.values() if _as_id(g.get("subnet_group_id")) == subnet_group_id),
            None,
        )
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        rec = {
            "subnet_group_id": subnet_group_id,
            "name": str(name),
            "description": str(description),
            "subnet_ids": [str(s) for s in (subnet_ids or [])],
            "vpc_id": _as_id(vpc_id),
        }
        data["aws_subnet_groups"][rec["aws_subnet_group_id"]] = rec
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSubnetGroup",
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
                    "required": [
                        "subnet_group_id",
                        "name",
                        "description",
                        "subnet_ids",
                        "vpc_id",
                    ],
                },
            },
        }


class DeleteSubnetGroup(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subnet_group_id: Any, aws_subnet_groups: list = None) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = aws_subnet_groups if aws_subnet_groups is not None else data.get("aws_subnet_groups", {}).values()
        before = len(groups)
        data["aws_subnet_groups"] = [
            g for g in groups.values() if _as_id(g.get("subnet_group_id")) != subnet_group_id
        ]
        if len(data["aws_subnet_groups"]) == before:
            return _err("Subnet group not found.")
        payload = {"deleted_subnet_group_id": subnet_group_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteSubnetGroup",
                "description": "Delete an ElastiCache subnet group.",
                "parameters": {
                    "type": "object",
                    "properties": {"subnet_group_id": {"type": "string"}},
                    "required": ["subnet_group_id"],
                },
            },
        }


class ListSecurityGroupRules(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], group_id: Any, aws_security_group_rules: list = None) -> str:
        group_id = _as_id(group_id)
        rules = aws_security_group_rules if aws_security_group_rules is not None else []
        rows = [r for r in rules.values() if _as_id(r.get("group_id")) == group_id]
        payload = {"group_id": group_id, "rules": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSecurityGroupRules",
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
        data: dict[str, Any],
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
            "direction": str(direction),  #"ingress" or "egress"
            "protocol": str(protocol),  #for example, "tcp"
            "port": int(port),
            "cidr": str(cidr),
            "description": str(description),
        }
        data["aws_security_group_rules"][rec["aws_security_group_rule_id"]] = rec
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSecurityGroupRule",
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


class RemoveSecurityGroupRule(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], aws_security_group_rules: list = None, rule_id: Any = None) -> str:
        rule_id = _as_id(rule_id)
        rules = aws_security_group_rules or []
        before = len(rules)
        data["aws_security_group_rules"] = [
            r for r in rules.values() if _as_id(r.get("rule_id")) != rule_id
        ]
        if len(data["aws_security_group_rules"]) == before:
            return _err("Rule not found.")
        payload = {"deleted_rule_id": rule_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeSecurityGroupRule",
                "description": "Revoke a security group rule by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"rule_id": {"type": "string"}},
                    "required": ["rule_id"],
                },
            },
        }


class GetSubnetGroup(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subnet_group_id: Any, aws_subnet_groups: list = None) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = aws_subnet_groups or []
        g = next(
            (x for x in groups.values() if _as_id(x.get("subnet_group_id")) == subnet_group_id),
            None,
        )
        payload = g or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSubnetGroup",
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
    def invoke(
        data: dict[str, Any], subnet_group_id: Any, name: Any, description: Any
    ) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = data.get("aws_subnet_groups", {}).values()
        g = next(
            (x for x in groups.values() if _as_id(x.get("subnet_group_id")) == subnet_group_id),
            None,
        )
        if not g:
            return _err("Subnet group not found.")
        g["name"] = str(name)
        g["description"] = str(description)
        payload = {
            "subnet_group_id": subnet_group_id,
            "name": g["name"],
            "description": g["description"],
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
                "name": "UpdateSubnetGroupDescription",
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
    def invoke(
        data: dict[str, Any],
        cluster_id: Any,
        node_type: Any,
        num_nodes: Any,
        changed_at: Any,
    ) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", {}).values()
        c = next(
            (x for x in clusters.values() if _as_id(x.get("cluster_id")) == cluster_id), None
        )
        if not c:
            return _err("Cluster not found.")
        c["node_type"] = str(node_type)
        c["num_nodes"] = int(num_nodes)
        c["last_modified_at"] = str(changed_at)
        payload = {
            "cluster_id": cluster_id,
            "node_type": c["node_type"],
            "num_nodes": c["num_nodes"],
            "last_modified_at": c["last_modified_at"],
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
                "name": "UpdateElasticacheClusterConfig",
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


class UpdateSecurityGroupRule(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], rule_id: Any, cidr: Any, description: Any) -> str:
        # Updates only the rules established through our add_security_group_rule (rule_id = 'SGR_####')
        rule_id = _as_id(rule_id)
        rules = data.get("aws_security_group_rules", {}).values()
        r = next((x for x in rules.values() if _as_id(x.get("rule_id")) == rule_id), None)
        if not r:
            return _err("Rule not found.")
        r["cidr"] = str(cidr)
        r["description"] = str(description)
        payload = {"rule_id": rule_id, "cidr": r["cidr"], "description": r["description"]}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSecurityGroupRule",
                "description": "Update an existing security group rule's CIDR and description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_id": {"type": "string"},
                        "cidr": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": ["rule_id", "cidr", "description"],
                },
            },
        }


def _next_sequential_id(existing_ids, prefix):
    pass
    mx = 0
    pat = re.compile(r"^" + re.escape(prefix) + r"(\d+)$")
    for s in existing_ids:
        if not s:
            continue
        m = pat.match(str(s))
        if m:
            try:
                mx = max(mx, int(m.group(1)))
            except ValueError:
                pass
    return f"{prefix}{mx+1:03d}"


class ReserveCartId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], carts: list[dict[str, Any]] = None, _id_reservations: dict[str, Any] = None) -> str:
        used = [c.get("cart_id") for c in (carts or [])]
        reserved = (_id_reservations or {}).get("cart_ids", [])
        next_id = _next_sequential_id(list(used) + list(reserved), "C")
        resv = data.setdefault("_id_reservations", [])
        resv["cart_ids"] = list(set(reserved + [next_id]))
        payload = {"cart_id": next_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReserveCartId",
                "description": "Generate and reserve the next cart_id (C###) by scanning existing carts and prior reservations.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class ReserveOrderId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], orders: list[dict[str, Any]] = None, _id_reservations: dict[str, Any] = None) -> str:
        used = [o.get("order_id") for o in (orders or [])]
        reserved = (_id_reservations or {}).get("order_ids", [])
        next_id = _next_sequential_id(list(used) + list(reserved), "O")
        resv = data.setdefault("_id_reservations", [])
        resv["order_ids"] = list(set(reserved + [next_id]))
        payload = {"order_id": next_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReserveOrderId",
                "description": "Generate and reserve the next order_id (O###) by scanning existing orders and prior reservations.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


TOOLS = [
    GetContactByEmail(),
    GetProductByName(),
    ListProductsInCategory(),
    GetPricebookByName(),
    GetOfferByCode(),
    CreateCart(),
    AddItemToCart(),
    SetItemQuantity(),
    RemoveItemFromCart(),
    ApplyOfferToCart(),
    SwitchCartPricebook(),
    PreviewCartTotals(),
    CreateOrder(),
    GetOrder(),
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
    DeleteElastiCacheCluster(),
    ListSubnetGroups(),
    CreateSubnetGroup(),
    DeleteSubnetGroup(),
    ListSecurityGroupRules(),
    AddSecurityGroupRule(),
    GetSubnetGroup(),
    UpdateSubnetGroupDescription(),
    UpdateElastiCacheClusterConfig(),
    UpdateSecurityGroupRule(),
    RemoveSecurityGroupRule(),
    ReserveCartId(),
    ReserveOrderId(),
]
