import json
from typing import Any

from tau_bench.envs.tool import Tool

FIXED_NOW = "2025-08-06T12:00:00Z"
ID_KEYS = {
    "account_id",
    "contact_id",
    "offer_id",
    "cart_id",
    "order_id",
    "case_id",
    "product_id",
    "pricebook_id",
}




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


def _next_numeric_id(existing: list[dict[str, Any]], field: str) -> str:
    pass
    max_id = 0
    for row in existing:
        try:
            max_id = max(max_id, int(row.get(field)))
        except (TypeError, ValueError):
            continue
    return str(max_id + 1)


def _idstr(v):
    """Convert numeric IDs to string format; keep None/strings as they are."""
    pass
    return str(v) if isinstance(v, int) else v


def _norm_ids_in_obj(obj):
    """Traverse lists/dictionaries and standardize any fields resembling IDs."""
    pass
    if isinstance(obj, list):
        return [_norm_ids_in_obj(x) for x in obj]
    if isinstance(obj, dict):
        return {
            k: (_idstr(v) if k in ID_KEYS else _norm_ids_in_obj(v))
            for k, v in obj.items()
        }
    return obj


class FindContactByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], first_name: Any, last_name: Any) -> str:
        matches = [
            c
            for c in data.get("contacts", [])
            if c.get("first_name") == first_name and c.get("last_name") == last_name
        ]
        payload = matches[0] if matches else {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findContactByName",
                "description": "Returns contact by exact first and last name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }


class FindAccountByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_name: Any) -> str:
        match = next(
            (
                a
                for a in data.get("accounts", [])
                if a.get("account_name") == account_name
            ),
            {},
        )
        payload = match
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findAccountByName",
                "description": "Returns account record by exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"account_name": {"type": "string"}},
                    "required": ["account_name"],
                },
            },
        }


class FindProductByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: Any) -> str:
        match = next((p for p in data.get("products", []) if p.get("name") == name), {})
        payload = match
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindProductByName",
                "description": "Returns product by exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class GetOrCreateCartForContact(Tool):
    def invoke(
        data: dict[str, Any],
        carts: list[dict[str, Any]],
        contact_id: Any = None
    ) -> str:
        contact_id = _idstr(contact_id)
        cart = next(
            (c for c in carts if f"{c.get('contact_id')}" == f"{contact_id}"), None
        )
        if not cart:
            new_id = _next_numeric_id(carts, "cart_id")
            cart = {
                "cart_id": new_id,
                "contact_id": contact_id,
                "last_updated_at": "FIXED-TIME",
            }
            carts.append(cart)
        payload = {"cart_id": cart["cart_id"]}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrCreateCartForContact",
                "description": "Gets existing cart for a contact or creates a new deterministic one.",
                "parameters": {
                    "type": "object",
                    "properties": {"contact_id": {"type": "string"}},
                    "required": ["contact_id"],
                },
            },
        }


class AddCartItem(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], cart_id: Any, product_id: Any, quantity: Any
    ) -> str:
        cart_id = _idstr(cart_id)
        product_id = _idstr(product_id)
        quantity = int(quantity)
        product = next(
            (
                p
                for p in data.get("products", [])
                if f"{p.get('product_id')}" == f"{product_id}"
            ),
            None,
        )
        if not product or int(product.get("stock_quantity", 0)) <= 0:
            payload = {"error": "Product out of stock or not found."}
            out = json.dumps(payload, indent=2)
            return out
        items = data.get("cart_items", [])
        new_id = _next_numeric_id(items, "cart_item_id")
        items.append(
            {
                "cart_item_id": new_id,
                "cart_id": cart_id,
                "product_id": product_id,
                "quantity": quantity,
            }
        )
        payload = {"cart_item_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
        pass
        cart_id = _idstr(cart_id)
        product_id = _idstr(product_id)
        quantity = int(quantity)
        product = next(
            (
                p
                for p in data.get("products", [])
                if f"{p.get('product_id')}" == f"{product_id}"
            ),
            None,
        )
        if not product or int(product.get("stock_quantity", 0)) <= 0:
            payload = {"error": "Product out of stock or not found."}
            out = json.dumps(payload, indent=2)
            return out
        items = data.get("cart_items", [])
        new_id = _next_numeric_id(items, "cart_item_id")
        items.append(
            {
                "cart_item_id": new_id,
                "cart_id": cart_id,
                "product_id": product_id,
                "quantity": quantity,
            }
        )
        payload = {"cart_item_id": new_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addCartItem",
                "description": "Adds an item to a cart if product has stock.",
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


class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, new_status: Any) -> str:
        order_id = _idstr(order_id)
        new_status = f"{new_status}"
        order = next(
            (
                o
                for o in data.get("orders", [])
                if f"{o.get('order_id')}" == f"{order_id}"
            ),
            None,
        )
        if not order:
            payload = {"error": "Order not found."}
            out = json.dumps(payload, indent=2)
            return out
        order["status"] = new_status
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateOrderStatus",
                "description": "Updates order status deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }


class GetOrderDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, orders: list = None) -> str:
        order_id = _idstr(order_id)
        order = next(
            (
                o
                for o in (orders or data.get("orders", []))
                if f"{o.get('order_id')}" == f"{order_id}"
            ),
            None,
        )
        payload = order or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrderDetails",
                "description": "Returns full order record by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class ToggleTraceFlag(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], org_id: Any, flag_name: Any, is_active: Any
    ) -> str:
        org_id = _idstr(org_id)
        flag_name = f"{flag_name}"
        is_active = bool(is_active)
        flag = next(
            (
                f
                for f in data.get("trace_flags", [])
                if f.get("org_id") == org_id and f.get("flag_name") == flag_name
            ),
            None,
        )
        if not flag:
            payload = {"error": "Trace flag not found."}
            out = json.dumps(payload, indent=2)
            return out
        flag["is_active"] = is_active
        payload = flag
        out = json.dumps(payload, indent=2)
        return out
        pass
        org_id = _idstr(org_id)
        flag_name = f"{flag_name}"
        is_active = bool(is_active)
        flag = next(
            (
                f
                for f in data.get("trace_flags", [])
                if f.get("org_id") == org_id and f.get("flag_name") == flag_name
            ),
            None,
        )
        if not flag:
            payload = {"error": "Trace flag not found."}
            out = json.dumps(payload, indent=2)
            return out
        flag["is_active"] = is_active
        payload = flag
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "toggleTraceFlag",
                "description": "Activates or deactivates a trace flag for an org.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "flag_name": {"type": "string"},
                        "is_active": {"type": "boolean"},
                    },
                    "required": ["org_id", "flag_name", "is_active"],
                },
            },
        }


class AddSecurityGroupRule(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        security_group_id: Any,
        port: Any,
        protocol: Any,
        source_ip: Any
    ) -> str:
        security_group_id = _idstr(security_group_id)
        port = int(port)
        protocol = f"{protocol}"
        source_ip = f"{source_ip}"
        rules = data.get("aws_security_group_rules", [])
        new_id = f"sgr-{_next_numeric_id(rules, 'rule_seq')}"
        rules.append(
            {
                "rule_id": new_id,
                "security_group_id": security_group_id,
                "port": port,
                "protocol": protocol,
                "source_ip": source_ip,
                "description": "Added via API",
                "rule_seq": new_id.split("-")[1],
            }
        )
        payload = {"rule_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
        pass
        security_group_id = _idstr(security_group_id)
        port = int(port)
        protocol = f"{protocol}"
        source_ip = f"{source_ip}"
        rules = data.get("aws_security_group_rules", [])
        new_id = f"sgr-{_next_numeric_id(rules, 'rule_seq')}"
        rules.append(
            {
                "rule_id": new_id,
                "security_group_id": security_group_id,
                "port": port,
                "protocol": protocol,
                "source_ip": source_ip,
                "description": "Added via API",
                "rule_seq": new_id.split("-")[1],
            }
        )
        payload = {"rule_id": new_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSecurityGroupRule",
                "description": "Appends a security group rule entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "security_group_id": {"type": "string"},
                        "port": {"type": "integer"},
                        "protocol": {"type": "string"},
                        "source_ip": {"type": "string"},
                    },
                    "required": ["security_group_id", "port", "protocol", "source_ip"],
                },
            },
        }


class UpdateCacheClusterStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cluster_id: Any,
        endpoint_url: Any = None,
        status: Any = None,
        security_group_id: Any = None
    ) -> str:
        cluster_id = _idstr(cluster_id)
        endpoint_url = f"{endpoint_url}" if endpoint_url is not None else None
        status = f"{status}" if status is not None else None
        security_group_id = (
            _idstr(security_group_id) if security_group_id is not None else None
        )

        cluster = next(
            (
                c
                for c in data.get("aws_elasticache_clusters", [])
                if f"{c.get('cluster_id')}" == f"{cluster_id}"
            ),
            None,
        )
        if not cluster:
            payload = {"error": "Cluster not found."}
            out = json.dumps(payload, indent=2)
            return out
        if status is not None:
            cluster["status"] = status
        if endpoint_url is not None:
            cluster["endpoint_url"] = endpoint_url
        if security_group_id is not None:
            cluster["security_group_id"] = security_group_id
        payload = cluster
        out = json.dumps(payload, indent=2)
        return out
        pass
        cluster_id = _idstr(cluster_id)
        endpoint_url = f"{endpoint_url}" if endpoint_url is not None else None
        status = f"{status}" if status is not None else None
        security_group_id = (
            _idstr(security_group_id) if security_group_id is not None else None
        )

        cluster = next(
            (
                c
                for c in data.get("aws_elasticache_clusters", [])
                if f"{c.get('cluster_id')}" == f"{cluster_id}"
            ),
            None,
        )
        if not cluster:
            payload = {"error": "Cluster not found."}
            out = json.dumps(payload, indent=2)
            return out
        if status is not None:
            cluster["status"] = status
        if endpoint_url is not None:
            cluster["endpoint_url"] = endpoint_url
        if security_group_id is not None:
            cluster["security_group_id"] = security_group_id
        payload = cluster
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCacheClusterStatus",
                "description": "Updates selected fields of an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "status": {"type": "string"},
                        "endpoint_url": {"type": "string"},
                        "security_group_id": {"type": "string"},
                    },
                    "required": ["cluster_id"],
                },
            },
        }


def _ensure_audit_log(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    if "audit_log" not in data:
        data["audit_log"] = []
    return data["audit_log"]


def _error(msg: str) -> str:
    pass
    payload = {"error": msg}
    out = json.dumps(payload)
    return out


def _append_audit(
    data: dict[str, Any], event_type: str, subject_id: str, details: dict[str, Any]
) -> None:
    pass
    log = _ensure_audit_log(data)
    log.append(
        {
            "event_type": event_type,
            "subject_id": subject_id,
            "details": details,
            "timestamp": FIXED_NOW,
            "actor": "SYSTEM",
        }
    )


def _find_one(lst: list[dict[str, Any]], key: str, value: Any) -> dict[str, Any] | None:
    pass
    for x in lst or []:
        if x.get(key) == value:
            return x
    return None


class GetCustomerProfile(Tool):
    """Obtain comprehensive customer profile with account and contact details."""

    @staticmethod
    def invoke(data: dict[str, Any], email: Any = None, contact_id: Any = None) -> str:
        email = f"{email}" if email is not None else None
        contact_id = _idstr(contact_id) if contact_id is not None else None
        if not email and not contact_id:
            return _error("email or contact_id is required.")

        contacts = data.get("contacts", [])
        contact = (
            _find_one(contacts, "email", email)
            if email
            else _find_one(contacts, "contact_id", contact_id)
        )
        if not contact:
            return _error("Contact not found.")

        accounts = data.get("accounts", [])
        account = _find_one(accounts, "account_id", contact.get("account_id"))
        payload = {"contact": contact, "account": account}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerProfile",
                "description": "Retrieve detailed customer profile including account and contact information by email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string"},
                        "contact_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class SearchProductsByCategory(Tool):
    """Look for items in a designated category and provide pricing details."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        category_name: Any = None,
        category_id: Any = None,
        account_id: Any = None,
        categories: list = None,
        products: list = None,
        accounts: list = None,
        pricebook_entries: list = None
    ) -> str:
        pass
        cat_id = _idstr(category_id) if category_id is not None else None
        cat_name = f"{category_name}".strip() if category_name is not None else None
        account_id = _idstr(account_id) if account_id is not None else None

        if not cat_id and not cat_name:
            return _error("category_id or category_name is required.")

        categories = categories or data.get("categories", [])
        category = None
        if cat_id:
            category = _find_one(categories, "category_id", cat_id)
        elif cat_name:
            category = _find_one(categories, "category_name", cat_name)

        if not category:
            return _error(f"Category '{cat_id or cat_name}' not found.")

        products = products or data.get("products", [])
        resolved_cid = f"{category.get('category_id')}"
        category_products = [
            p for p in products if f"{p.get('category_id')}" == resolved_cid
        ]

        if account_id:
            accounts = accounts or data.get("accounts", [])
            account = _find_one(accounts, "account_id", account_id)
            if account:
                pricebook_id = _idstr(account.get("default_pricebook_id"))
                pricebook_entries = pricebook_entries or data.get("pricebook_entries", [])
                for product in category_products:
                    pbe = _find_one(
                        pricebook_entries, "product_id", product.get("product_id")
                    )
                    if pbe and f"{pbe.get('pricebook_id')}" == f"{pricebook_id}":
                        product["price"] = pbe.get("price")
        payload = category_products
        out = json.dumps(payload, indent=2)
        return out
        pass
        cat_id = _idstr(category_id) if category_id is not None else None
        cat_name = f"{category_name}".strip() if category_name is not None else None
        account_id = _idstr(account_id) if account_id is not None else None

        if not cat_id and not cat_name:
            return _error("category_id or category_name is required.")

        categories = data.get("categories", [])
        category = None
        if cat_id:
            category = _find_one(categories, "category_id", cat_id)
        elif cat_name:
            category = _find_one(categories, "category_name", cat_name)

        if not category:
            return _error(f"Category '{cat_id or cat_name}' not found.")

        products = data.get("products", [])
        resolved_cid = f"{category.get('category_id')}"
        category_products = [
            p for p in products if f"{p.get('category_id')}" == resolved_cid
        ]

        if account_id:
            accounts = data.get("accounts", [])
            account = _find_one(accounts, "account_id", account_id)
            if account:
                pricebook_id = _idstr(account.get("default_pricebook_id"))
                pricebook_entries = data.get("pricebook_entries", [])
                for product in category_products:
                    pbe = _find_one(
                        pricebook_entries, "product_id", product.get("product_id")
                    )
                    if pbe and f"{pbe.get('pricebook_id')}" == f"{pricebook_id}":
                        product["price"] = pbe.get("price")
        payload = category_products
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchProductsByCategory",
                "description": "Search for products within a specific category and optionally include pricing for an account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category_name": {"type": "string"},
                        "category_id": {"type": "string"},
                        "account_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class CreateShoppingCart(Tool):
    """Establish a new shopping cart for a customer containing several items."""

    @staticmethod
    def invoke(
        data: dict[str, Any], cart_id: Any, contact_id: Any, items: Any = []
    ) -> str:
        cart_id = _idstr(cart_id)
        contact_id = _idstr(contact_id)
        items = _norm_ids_in_obj(items or [])

        if not cart_id or not contact_id:
            return _error("cart_id and contact_id are required.")

        contacts = data.get("contacts", [])
        if not _find_one(contacts, "contact_id", contact_id):
            return _error(f"Contact '{contact_id}' not found.")

        carts = data.setdefault("carts", [])
        if _find_one(carts, "cart_id", cart_id):
            return _error(f"Cart '{cart_id}' already exists.")

        cart = {
            "cart_id": cart_id,
            "contact_id": contact_id,
            "last_updated_at": FIXED_NOW,
            "account_id": _find_one(contacts, "contact_id", contact_id).get(
                "account_id"
            ),
            "applied_offer_id": None,
        }
        carts.append(cart)

        cart_items = data.setdefault("cart_items", [])
        products = data.get("products", [])
        for item in items:
            product_id = item.get("product_id")
            quantity = int(item.get("quantity", 1))
            if not _find_one(products, "product_id", product_id):
                return _error(f"Product '{product_id}' not found.")
            cart_item_id = f"{cart_id}:{product_id}"
            cart_items.append(
                {
                    "cart_item_id": cart_item_id,
                    "cart_id": cart_id,
                    "product_id": product_id,
                    "quantity": quantity,
                    "pricebook_entry_id": None,
                }
            )

        _append_audit(
            data,
            "cart_created",
            cart_id,
            {"contact_id": contact_id, "items_count": len(items)},
        )
        payload = cart
        out = json.dumps(payload, indent=2)
        return out
        pass
        cart_id = _idstr(cart_id)
        contact_id = _idstr(contact_id)
        items = _norm_ids_in_obj(items or [])

        if not cart_id or not contact_id:
            return _error("cart_id and contact_id are required.")

        contacts = data.get("contacts", [])
        if not _find_one(contacts, "contact_id", contact_id):
            return _error(f"Contact '{contact_id}' not found.")

        carts = data.setdefault("carts", [])
        if _find_one(carts, "cart_id", cart_id):
            return _error(f"Cart '{cart_id}' already exists.")

        cart = {
            "cart_id": cart_id,
            "contact_id": contact_id,
            "last_updated_at": FIXED_NOW,
            "account_id": _find_one(contacts, "contact_id", contact_id).get(
                "account_id"
            ),
            "applied_offer_id": None,
        }
        carts.append(cart)

        cart_items = data.setdefault("cart_items", [])
        products = data.get("products", [])
        for item in items:
            product_id = item.get("product_id")
            quantity = int(item.get("quantity", 1))
            if not _find_one(products, "product_id", product_id):
                return _error(f"Product '{product_id}' not found.")
            cart_item_id = f"{cart_id}:{product_id}"
            cart_items.append(
                {
                    "cart_item_id": cart_item_id,
                    "cart_id": cart_id,
                    "product_id": product_id,
                    "quantity": quantity,
                    "pricebook_entry_id": None,
                }
            )

        _append_audit(
            data,
            "cart_created",
            cart_id,
            {"contact_id": contact_id, "items_count": len(items)},
        )
        payload = cart
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateShoppingCart",
                "description": "Create a new shopping cart for a customer with multiple items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "contact_id": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                            },
                        },
                    },
                    "required": ["cart_id", "contact_id"],
                },
            },
        }


class ApplyDiscountBundle(Tool):
    """Implement a discount on a cart and compute overall savings."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        cart_id: Any,
        offer_code: Any,
        carts: list = None,
        offers: list = None,
        cart_items: list = None,
        pricebook_entries: list = None,
        accounts: list = None
    ) -> str:
        pass
        cart_id = _idstr(cart_id)
        offer_code = f"{offer_code}"
        if not cart_id or not offer_code:
            return _error("cart_id and offer_code are required.")

        carts = carts if carts is not None else data.get("carts", [])
        cart = _find_one(carts, "cart_id", cart_id)
        if not cart:
            return _error(f"Cart '{cart_id}' not found.")

        offers = offers if offers is not None else data.get("offers", [])
        offer = _find_one(offers, "offer_code", offer_code)
        if not offer or not offer.get("is_active"):
            return _error(f"Offer '{offer_code}' not found or inactive.")

        cart_items = cart_items if cart_items is not None else data.get("cart_items", [])
        pricebook_entries = pricebook_entries if pricebook_entries is not None else data.get("pricebook_entries", [])
        accounts = accounts if accounts is not None else data.get("accounts", [])

        cart_line_items = [
            ci for ci in cart_items if f"{ci.get('cart_id')}" == f"{cart_id}"
        ]
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
                subtotal += float(pbe.get("price", 0.0)) * int(ci.get("quantity", 0))

        discount_amount = 0.0
        if offer.get("discount_type") == "PERCENTAGE":
            discount_amount = round(
                subtotal * (float(offer.get("discount_value", 0.0)) / 100.0), 2
            )
        elif offer.get("discount_type") == "FIXED_AMOUNT":
            discount_amount = min(float(offer.get("discount_value", 0.0)), subtotal)

        cart["applied_offer_id"] = offer.get("offer_id")

        result = {
            "cart_id": cart_id,
            "offer_applied": offer_code,
            "subtotal": round(subtotal, 2),
            "discount_amount": round(discount_amount, 2),
            "total_amount": round(subtotal - discount_amount, 2),
        }
        _append_audit(
            data,
            "discount_applied",
            cart_id,
            {"offer_code": offer_code, "discount_amount": discount_amount},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyDiscountBundle",
                "description": "Apply a discount to a cart and calculate total savings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "offer_code": {"type": "string"},
                    },
                    "required": ["cart_id", "offer_code"],
                },
            },
        }


class ProcessOrderWithFulfillment(Tool):
    """Generate an order from the cart and start the fulfillment procedure."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: Any,
        cart_id: Any,
        shipping_method: Any = "US-Std",
        shipping_rules: list = None,
        orders: list = None,
        carts: list = None,
        cart_items: list = None,
        pricebook_entries: list = None,
        accounts: list = None,
        offers: list = None,
        products: list = None
    ) -> str:
        pass
        order_id = _idstr(order_id)
        cart_id = _idstr(cart_id)
        if shipping_method == "Us-Std":
            shipping_method = "US-Std"
        if shipping_method == "Eu-Express":
            shipping_method = "EU-Express"
        try:
            shipping_method = (
                f"{shipping_method}".strip()
                if shipping_method is not None
                else "US-Std"
            )
        except Exception:
            shipping_method = "US-Std"

        if not shipping_method:
            rules = shipping_rules or []
            rule = rules[-1] if rules else None
            if rule:
                shipping_method = rule.get("rule_name") or "US-Std"
        shipping_method = shipping_method.title()

        if not order_id or not cart_id:
            return _error("order_id and cart_id are required.")

        orders = orders or []
        existing = _find_one(orders, "order_id", order_id)
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out

        carts = carts or []
        cart = _find_one(carts, "cart_id", cart_id)
        if not cart:
            return _error(f"Cart '{cart_id}' not found.")

        cart_items = cart_items or []
        cart_line_items = [
            ci for ci in cart_items if f"{ci.get('cart_id')}" == f"{cart_id}"
        ]
        if not cart_line_items:
            return _error("Cart has no items.")

        pricebook_entries = pricebook_entries or []
        accounts = accounts or []
        offers = offers or []
        products = products or []

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
                        return _error(
                            f"Insufficient stock for product {ci.get('product_id')}"
                        )
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
                    discount_amount = min(
                        float(offer.get("discount_value", 0.0)), subtotal
                    )

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

        _append_audit(
            data,
            "order_created",
            order_id,
            {
                "cart_id": cart_id,
                "total_amount": total,
                "items_count": len(cart_line_items),
            },
        )
        payload = new_order
        out = json.dumps(payload, indent=2)
        return out
        pass
        order_id = _idstr(order_id)
        cart_id = _idstr(cart_id)
        if shipping_method == "Us-Std":
            shipping_method = "US-Std"
        if shipping_method == "Eu-Express":
            shipping_method = "EU-Express"
        try:
            shipping_method = (
                f"{shipping_method}".strip()
                if shipping_method is not None
                else "US-Std"
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

        orders = data.get("orders", [])
        existing = _find_one(orders, "order_id", order_id)
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out

        carts = data.get("carts", [])
        cart = _find_one(carts, "cart_id", cart_id)
        if not cart:
            return _error(f"Cart '{cart_id}' not found.")

        cart_items = data.get("cart_items", [])
        cart_line_items = [
            ci for ci in cart_items if f"{ci.get('cart_id')}" == f"{cart_id}"
        ]
        if not cart_line_items:
            return _error("Cart has no items.")

        pricebook_entries = data.get("pricebook_entries", [])
        accounts = data.get("accounts", [])
        offers = data.get("offers", [])
        products = data.get("products", [])

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
                        return _error(
                            f"Insufficient stock for product {ci.get('product_id')}"
                        )
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
                    discount_amount = min(
                        float(offer.get("discount_value", 0.0)), subtotal
                    )

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

        _append_audit(
            data,
            "order_created",
            order_id,
            {
                "cart_id": cart_id,
                "total_amount": total,
                "items_count": len(cart_line_items),
            },
        )
        payload = new_order
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessOrderWithFulfillment",
                "description": "Create an order from cart, update inventory, and initiate fulfillment process.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "cart_id": {"type": "string"},
                        "shipping_method": {"type": "string"},
                    },
                    "required": ["order_id", "cart_id"],
                },
            },
        }


class ProcessReturnWithRefund(Tool):
    """Handle a full return with inventory replenishment and refund assessment."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        order_id: Any, 
        case_id: str, 
        return_items: Any = None
    ) -> str:
        order_id = _idstr(order_id)
        case_id = _idstr(case_id)
        items = _norm_ids_in_obj(return_items or [])
        if not order_id or not case_id:
            return _error("order_id and case_id are required.")

        orders = data.get("orders", [])
        order = _find_one(orders, "order_id", order_id)
        if not order:
            return _error(f"Order '{order_id}' not found.")
        if order.get("status") not in ["Delivered", "Shipped", "Cancelled"]:
            return _error(
                "Only delivered, shipped, or cancelled orders can be returned."
            )

        cases = data.setdefault("cases", [])
        if not _find_one(cases, "case_id", case_id):
            cases.append(
                {
                    "case_id": case_id,
                    "contact_id": order.get("contact_id"),
                    "account_id": order.get("account_id"),
                    "order_id": order_id,
                    "subject": f"Return Request for Order #{order_id}",
                    "status": "New",
                    "priority": "Medium",
                }
            )

        order_items = data.get("order_items", [])
        products = data.get("products", [])

        total_refund = 0.0
        items_processed = []
        for it in items:
            pid = it.get("product_id")
            ret_qty = int(it.get("quantity", 1))
            reason = it.get("reason", "customer_request")
            oi = next(
                (
                    oi
                    for oi in order_items
                    if f"{oi.get('order_id')}" == f"{order_id}"
                    and f"{oi.get('product_id')}" == f"{pid}"
                ),
                None,
            )
            if not oi:
                continue
            item_refund = float(oi.get("price", 0.0)) * ret_qty
            total_refund += item_refund

            product = _find_one(products, "product_id", pid)
            if product:
                product["stock_quantity"] = (
                    int(product.get("stock_quantity", 0)) + ret_qty
                )

            items_processed.append(
                {
                    "product_id": pid,
                    "quantity": ret_qty,
                    "reason": reason,
                    "refund_amount": round(item_refund, 2),
                }
            )

        if float(order.get("discount_amount", 0)) > 0:
            discount_ratio = float(order.get("discount_amount", 0)) / float(
                order.get("subtotal", 1)
            )
            total_refund -= total_refund * discount_ratio

        order["status"] = "Return Pending"
        result = {
            "case_id": case_id,
            "order_id": order_id,
            "items_processed": items_processed,
            "total_refund_amount": round(total_refund, 2),
            "order_status": order["status"],
        }
        _append_audit(
            data,
            "return_processed",
            case_id,
            {
                "order_id": order_id,
                "refund_amount": round(total_refund, 2),
                "items_count": len(items_processed),
            },
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
        order_id = _idstr(order_id)
        case_id = _idstr(case_id)
        items = _norm_ids_in_obj(return_items or [])
        if not order_id or not case_id:
            return _error("order_id and case_id are required.")

        orders = data.get("orders", [])
        order = _find_one(orders, "order_id", order_id)
        if not order:
            return _error(f"Order '{order_id}' not found.")
        if order.get("status") not in ["Delivered", "Shipped", "Cancelled"]:
            return _error(
                "Only delivered, shipped, or cancelled orders can be returned."
            )

        cases = data.setdefault("cases", [])
        if not _find_one(cases, "case_id", case_id):
            cases.append(
                {
                    "case_id": case_id,
                    "contact_id": order.get("contact_id"),
                    "account_id": order.get("account_id"),
                    "order_id": order_id,
                    "subject": f"Return Request for Order #{order_id}",
                    "status": "New",
                    "priority": "Medium",
                }
            )

        order_items = data.get("order_items", [])
        products = data.get("products", [])

        total_refund = 0.0
        items_processed = []
        for it in items:
            pid = it.get("product_id")
            ret_qty = int(it.get("quantity", 1))
            reason = it.get("reason", "customer_request")
            oi = next(
                (
                    oi
                    for oi in order_items
                    if f"{oi.get('order_id')}" == f"{order_id}"
                    and f"{oi.get('product_id')}" == f"{pid}"
                ),
                None,
            )
            if not oi:
                continue
            item_refund = float(oi.get("price", 0.0)) * ret_qty
            total_refund += item_refund

            product = _find_one(products, "product_id", pid)
            if product:
                product["stock_quantity"] = (
                    int(product.get("stock_quantity", 0)) + ret_qty
                )

            items_processed.append(
                {
                    "product_id": pid,
                    "quantity": ret_qty,
                    "reason": reason,
                    "refund_amount": round(item_refund, 2),
                }
            )

        if float(order.get("discount_amount", 0)) > 0:
            discount_ratio = float(order.get("discount_amount", 0)) / float(
                order.get("subtotal", 1)
            )
            total_refund -= total_refund * discount_ratio

        order["status"] = "Return Pending"
        result = {
            "case_id": case_id,
            "order_id": order_id,
            "items_processed": items_processed,
            "total_refund_amount": round(total_refund, 2),
            "order_status": order["status"],
        }
        _append_audit(
            data,
            "return_processed",
            case_id,
            {
                "order_id": order_id,
                "refund_amount": round(total_refund, 2),
                "items_count": len(items_processed),
            },
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "processReturnWithRefund",
                "description": "Process a complete return with inventory restoration and refund calculation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "case_id": {"type": "string"},
                        "return_items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                    "reason": {"type": "string"},
                                },
                            },
                        },
                    },
                    "required": ["order_id", "case_id"],
                },
            },
        }


class ConfigureCacheIntegration(Tool):
    """Set up external cache integration for a company."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        cluster_id: Any,
        elasticache_config: Any = None,
        engine: str = "redis",
        node_type: str = "cache.t3.micro",
        num_cache_nodes: int = 1
    ) -> str:
        if cluster_id is None:
            return _error("cluster_id is required.")

        cluster_id = _idstr(cluster_id)
        clusters = data.setdefault("aws_elasticache_clusters", [])
        cluster = _find_one(clusters, "cluster_id", cluster_id)

        if not cluster:
            cluster = {
                "cluster_id": cluster_id,
                "node_type": node_type,
                "num_cache_nodes": num_cache_nodes,
                "engine": engine,
                "status": "available",
                "endpoint_url": f"redis://{cluster_id}.cache.amazonaws.com:6379",
            }
            clusters.append(cluster)
        else:
            cluster.update(
                {
                    "node_type": node_type or cluster.get("node_type"),
                    "num_cache_nodes": num_cache_nodes or cluster.get("num_cache_nodes"),
                    "engine": engine or cluster.get("engine"),
                    "status": "available",
                }
            )

        result = {
            "cluster_id": cluster_id,
            "node_type": cluster.get("node_type"),
            "num_cache_nodes": cluster.get("num_cache_nodes"),
            "engine": cluster.get("engine"),
            "endpoint_url": cluster.get("endpoint_url"),
            "configuration_status": "completed",
        }
        _append_audit(
            data,
            "cache_configured",
            cluster_id,
            {
                "cluster_id": cluster_id,
                "config": {
                    "node_type": node_type,
                    "num_cache_nodes": num_cache_nodes,
                    "engine": engine,
                },
            },
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureCacheIntegration",
                "description": "Configure external cache integration with ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "elasticache_config": {
                            "type": "object",
                            "properties": {
                                "node_type": {"type": "string"},
                                "num_cache_nodes": {"type": "integer"},
                                "engine": {"type": "string"},
                            },
                        },
                    },
                    "required": ["cluster_id"],
                },
            },
        }


class ManageConnectedAppSecurity(Tool):
    """Oversee security configurations for connected apps and OAuth permissions."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        app_id: Any,
        permissions: Any = ["read", "write"],
        oauth_scopes: Any = ["api", "refresh_token"]
    ) -> str:
        app_id = _idstr(app_id)
        permissions = list(permissions or [])
        oauth_scopes = list(oauth_scopes or [])

        if not app_id:
            return _error("app_id is required.")

        apps = data.setdefault("connected_apps", [])
        app = _find_one(apps, "app_id", app_id)
        if not app:
            app = {
                "app_id": app_id,
                "app_name": f"App_{app_id}",
                "client_secret_stored": True,
                "disabled": False,
                "oauth_scopes": [],
                "permissions": [],
            }
            apps.append(app)

        app["permissions"] = permissions
        app["oauth_scopes"] = oauth_scopes
        app["disabled"] = False
        app["client_secret_stored"] = True

        result = {
            "app_id": app_id,
            "app_name": app.get("app_name"),
            "permissions": permissions,
            "oauth_scopes": oauth_scopes,
            "disabled": app.get("disabled"),
            "client_secret_stored": app.get("client_secret_stored"),
        }
        _append_audit(
            data,
            "app_security_updated",
            app_id,
            {"permissions": permissions, "scopes": oauth_scopes},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
        app_id = _idstr(app_id)
        permissions = list(permissions or [])
        oauth_scopes = list(oauth_scopes or [])

        if not app_id:
            return _error("app_id is required.")

        apps = data.setdefault("connected_apps", [])
        app = _find_one(apps, "app_id", app_id)
        if not app:
            app = {
                "app_id": app_id,
                "app_name": f"App_{app_id}",
                "client_secret_stored": True,
                "disabled": False,
                "oauth_scopes": [],
                "permissions": [],
            }
            apps.append(app)

        app["permissions"] = permissions
        app["oauth_scopes"] = oauth_scopes
        app["disabled"] = False
        app["client_secret_stored"] = True

        result = {
            "app_id": app_id,
            "app_name": app.get("app_name"),
            "permissions": permissions,
            "oauth_scopes": oauth_scopes,
            "disabled": app.get("disabled"),
            "client_secret_stored": app.get("client_secret_stored"),
        }
        _append_audit(
            data,
            "app_security_updated",
            app_id,
            {"permissions": permissions, "scopes": oauth_scopes},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageConnectedAppSecurity",
                "description": "Manage connected app security settings, permissions and OAuth scopes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "app_id": {"type": "string"},
                        "permissions": {"type": "array", "items": {"type": "string"}},
                        "oauth_scopes": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["app_id"],
                },
            },
        }


class OptimizeSecurityGroupRules(Tool):
    """Enhance security group regulations by eliminating excessive access and incorporating precise rules."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        security_group_id: Any,
        allowed_cidr: Any = None,
        target_port: Any = 6379,
        aws_security_group_rules: list[dict[str, Any]] = None
    ) -> str:
        pass
        security_group_id = _idstr(security_group_id)
        allowed_cidr = f"{allowed_cidr}" if allowed_cidr is not None else None
        target_port = int(target_port)

        if not security_group_id:
            return _error("security_group_id is required.")

        allowed_cidrs = [allowed_cidr] if allowed_cidr else []
        rules = aws_security_group_rules if aws_security_group_rules is not None else []
        changes = []

        rules_to_remove = []
        for rule in rules:
            if (
                f"{rule.get('security_group_id')}" == f"{security_group_id}"
                and int(rule.get("port")) == target_port
                and rule.get("protocol") == "TCP"
                and rule.get("source_ip") == "0.0.0.0/0"
            ):
                rules_to_remove.append(rule)
                changes.append(f"Removed overly permissive rule: {rule.get('rule_id')}")

        for rule in rules_to_remove:
            rules.remove(rule)

        existing_cidrs = {
            r.get("source_ip")
            for r in rules
            if f"{r.get('security_group_id')}" == f"{security_group_id}"
            and int(r.get("port")) == target_port
        }

        for cidr in allowed_cidrs:
            if cidr not in existing_cidrs:
                new_rule_id = (
                    f"sgr-{security_group_id}-{cidr.replace('/', '_')}-{target_port}"
                )
                rules.append(
                    {
                        "rule_id": new_rule_id,
                        "security_group_id": security_group_id,
                        "port": target_port,
                        "protocol": "TCP",
                        "source_ip": cidr,
                        "description": f"Allow {target_port} access from approved CIDR {cidr}",
                    }
                )
                changes.append(f"Added rule for CIDR: {cidr}")

        result = {
            "security_group_id": security_group_id,
            "target_port": target_port,
            "changes": changes,
            "allowed_cidrs": allowed_cidrs,
        }
        _append_audit(
            data,
            "security_group_optimized",
            security_group_id,
            {"target_port": target_port, "changes_count": len(changes)},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
        security_group_id = _idstr(security_group_id)
        allowed_cidr = f"{allowed_cidr}" if allowed_cidr is not None else None
        target_port = int(target_port)

        if not security_group_id:
            return _error("security_group_id is required.")

        allowed_cidrs = [allowed_cidr] if allowed_cidr else []
        rules = data.get("aws_security_group_rules", [])
        changes = []

        rules_to_remove = []
        for rule in rules:
            if (
                f"{rule.get('security_group_id')}" == f"{security_group_id}"
                and int(rule.get("port")) == target_port
                and rule.get("protocol") == "TCP"
                and rule.get("source_ip") == "0.0.0.0/0"
            ):
                rules_to_remove.append(rule)
                changes.append(f"Removed overly permissive rule: {rule.get('rule_id')}")

        for rule in rules_to_remove:
            rules.remove(rule)

        existing_cidrs = {
            r.get("source_ip")
            for r in rules
            if f"{r.get('security_group_id')}" == f"{security_group_id}"
            and int(r.get("port")) == target_port
        }

        for cidr in allowed_cidrs:
            if cidr not in existing_cidrs:
                new_rule_id = (
                    f"sgr-{security_group_id}-{cidr.replace('/', '_')}-{target_port}"
                )
                rules.append(
                    {
                        "rule_id": new_rule_id,
                        "security_group_id": security_group_id,
                        "port": target_port,
                        "protocol": "TCP",
                        "source_ip": cidr,
                        "description": f"Allow {target_port} access from approved CIDR {cidr}",
                    }
                )
                changes.append(f"Added rule for CIDR: {cidr}")

        result = {
            "security_group_id": security_group_id,
            "target_port": target_port,
            "changes": changes,
            "allowed_cidrs": allowed_cidrs,
        }
        _append_audit(
            data,
            "security_group_optimized",
            security_group_id,
            {"target_port": target_port, "changes_count": len(changes)},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "OptimizeSecurityGroupRules",
                "description": "Optimize security group rules by removing overly permissive access and adding specific rules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "security_group_id": {"type": "string"},
                        "allowed_cidr": {"type": "string"},
                        "target_port": {"type": "integer"},
                    },
                    "required": ["security_group_id"],
                },
            },
        }


class GetAuditLog(Tool):
    """Access the audit log for compliance and monitoring needs."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action_type: str = None,
        resource_id: str = None,
        time_range: str = None
    ) -> str:
        action_type = f"{action_type}" if action_type is not None else None
        resource_id = f"{resource_id}" if resource_id is not None else None
        time_range = f"{time_range}" if time_range is not None else None

        audit_log = data.get("audit_log", [])
        filtered = audit_log
        if action_type:
            filtered = [e for e in filtered if e.get("event_type") == action_type]
        if resource_id:
            filtered = [
                e for e in filtered if f"{e.get('subject_id')}" == f"{resource_id}"
            ]
        payload = {
            "audit_entries": filtered,
            "time_range": (time_range or "all_time"),
            "total_entries": len(filtered),
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        action_type = f"{action_type}" if action_type is not None else None
        resource_id = f"{resource_id}" if resource_id is not None else None
        time_range = f"{time_range}" if time_range is not None else None

        audit_log = data.get("audit_log", [])
        filtered = audit_log
        if action_type:
            filtered = [e for e in filtered if e.get("event_type") == action_type]
        if resource_id:
            filtered = [
                e for e in filtered if f"{e.get('subject_id')}" == f"{resource_id}"
            ]
        payload = {
                "audit_entries": filtered,
                "time_range": (time_range or "all_time"),
                "total_entries": len(filtered),
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
                "name": "GetAuditLog",
                "description": "Retrieve the audit log with optional filtering by action type, resource ID, or time range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action_type": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "time_range": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class ManageInventoryLevels(Tool):
    """Oversee inventory levels of products and monitor stock changes."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        product_id: Any,
        quantity_adjustment: Any = 0,
        movement_type: Any = "adjustment"
    ) -> str:
        product_id = _idstr(product_id)
        quantity_adjustment = int(quantity_adjustment)
        movement_type = f"{movement_type}"

        if not product_id:
            return _error("product_id is required.")

        products = data.get("products", [])
        product = _find_one(products, "product_id", product_id)
        if not product:
            return _error(f"Product '{product_id}' not found.")

        inventory = data.setdefault("inventory", [])
        inv_item = _find_one(inventory, "product_id", product_id)
        if not inv_item:
            initial_qty = (
                int(product.get("stock_quantity", 0))
                if isinstance(product.get("stock_quantity"), int)
                else 100
            )
            inv_item = {
                "product_id": product_id,
                "quantity_on_hand": initial_qty,
                "reserved_quantity": 0,
                "last_updated": FIXED_NOW,
            }
            inventory.append(inv_item)

        old_quantity = int(inv_item.get("quantity_on_hand", 0))
        new_quantity = max(0, old_quantity + quantity_adjustment)
        inv_item["quantity_on_hand"] = new_quantity
        inv_item["last_updated"] = FIXED_NOW

        _append_audit(
            data,
            "inventory_updated",
            product_id,
            {
                "old_quantity": old_quantity,
                "new_quantity": new_quantity,
                "movement_type": movement_type,
            },
        )
        payload = {
                "product_id": product_id,
                "old_quantity": old_quantity,
                "new_quantity": new_quantity,
                "adjustment": quantity_adjustment,
                "movement_type": movement_type,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        product_id = _idstr(product_id)
        quantity_adjustment = int(quantity_adjustment)
        movement_type = f"{movement_type}"

        if not product_id:
            return _error("product_id is required.")

        products = data.get("products", [])
        product = _find_one(products, "product_id", product_id)
        if not product:
            return _error(f"Product '{product_id}' not found.")

        inventory = data.setdefault("inventory", [])
        inv_item = _find_one(inventory, "product_id", product_id)
        if not inv_item:
            initial_qty = (
                int(product.get("stock_quantity", 0))
                if isinstance(product.get("stock_quantity"), int)
                else 100
            )
            inv_item = {
                "product_id": product_id,
                "quantity_on_hand": initial_qty,
                "reserved_quantity": 0,
                "last_updated": FIXED_NOW,
            }
            inventory.append(inv_item)

        old_quantity = int(inv_item.get("quantity_on_hand", 0))
        new_quantity = max(0, old_quantity + quantity_adjustment)
        inv_item["quantity_on_hand"] = new_quantity
        inv_item["last_updated"] = FIXED_NOW

        _append_audit(
            data,
            "inventory_updated",
            product_id,
            {
                "old_quantity": old_quantity,
                "new_quantity": new_quantity,
                "movement_type": movement_type,
            },
        )
        payload = {
                "product_id": product_id,
                "old_quantity": old_quantity,
                "new_quantity": new_quantity,
                "adjustment": quantity_adjustment,
                "movement_type": movement_type,
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
                "name": "ManageInventoryLevels",
                "description": "Manage product inventory levels and track stock movements.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "quantity_adjustment": {"type": "integer"},
                        "movement_type": {"type": "string"},
                    },
                    "required": ["product_id"],
                },
            },
        }


class GeneratePromotionalCampaign(Tool):
    """Create and set up marketing campaigns with targeting criteria."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        campaign_name: Any,
        target_segment: Any = "all",
        discount_percentage: Any = 10
    ) -> str:
        pass
        campaign_name = f"{campaign_name}"
        target_segment = f"{target_segment}"
        try:
            discount_percentage = int(discount_percentage)
        except Exception:
            discount_percentage = 10
        import re as _re_patch

        _m = _re_patch.match(r".*?-(\d+)$", campaign_name.strip())
        if _m:
            try:
                discount_percentage = int(_m.group(1))
            except Exception:
                pass
        campaign_name = campaign_name
        target_segment = target_segment
        discount_percentage = discount_percentage

        if not campaign_name:
            return _error("campaign_name is required.")

        promotions = data.setdefault("promotions", [])
        promotion_id = f"PROMO_{len(promotions) + 1:03d}"

        promotion = {
            "promotion_id": promotion_id,
            "campaign_name": campaign_name,
            "target_segment": target_segment,
            "discount_percentage": discount_percentage,
            "start_date": FIXED_NOW,
            "status": "active",
        }
        promotions.append(promotion)

        result = {
            "promotion_id": promotion_id,
            "campaign_name": campaign_name,
            "target_segment": target_segment,
            "discount_percentage": discount_percentage,
            "status": "active",
        }

        _append_audit(
            data,
            "promotion_created",
            promotion_id,
            {"campaign_name": campaign_name, "target_segment": target_segment},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
        campaign_name = f"{campaign_name}"
        target_segment = f"{target_segment}"
        try:
            discount_percentage = int(discount_percentage)
        except Exception:
            discount_percentage = 10
        import re as _re_patch

        _m = _re_patch.match(r".*?-(\d+)$", campaign_name.strip())
        if _m:
            try:
                discount_percentage = int(_m.group(1))
            except Exception:
                pass
        campaign_name = campaign_name
        target_segment = target_segment
        discount_percentage = discount_percentage

        if not campaign_name:
            return _error("campaign_name is required.")

        promotions = data.setdefault("promotions", [])
        promotion_id = f"PROMO_{len(promotions) + 1:03d}"

        promotion = {
            "promotion_id": promotion_id,
            "campaign_name": campaign_name,
            "target_segment": target_segment,
            "discount_percentage": discount_percentage,
            "start_date": FIXED_NOW,
            "status": "active",
        }
        promotions.append(promotion)

        result = {
            "promotion_id": promotion_id,
            "campaign_name": campaign_name,
            "target_segment": target_segment,
            "discount_percentage": discount_percentage,
            "status": "active",
        }

        _append_audit(
            data,
            "promotion_created",
            promotion_id,
            {"campaign_name": campaign_name, "target_segment": target_segment},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GeneratePromotionalCampaign",
                "description": "Generate and configure promotional campaigns with targeting rules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_name": {"type": "string"},
                        "target_segment": {"type": "string"},
                        "discount_percentage": {"type": "number"},
                    },
                    "required": ["campaign_name"],
                },
            },
        }


class ConfigurePaymentGateway(Tool):
    """Set up payment gateway configurations and processing guidelines."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        gateway_name: Any,
        merchant_id: Any,
        supported_currencies: Any = ["USD"]
    ) -> str:
        if not gateway_name or not merchant_id:
            return _error("gateway_name and merchant_id are required.")

        gateways = data.setdefault("payment_gateways", [])
        gateway = {
            "gateway_id": f"GW_{len(gateways) + 1:03d}",
            "gateway_name": gateway_name,
            "merchant_id": merchant_id,
            "supported_currencies": supported_currencies,
            "status": "active",
            "configured_at": FIXED_NOW,
        }
        gateways.append(gateway)

        result = {
            "gateway_id": gateway["gateway_id"],
            "gateway_name": gateway_name,
            "merchant_id": merchant_id,
            "status": "configured",
        }

        _append_audit(
            data,
            "payment_gateway_configured",
            gateway["gateway_id"],
            {"gateway_name": gateway_name, "merchant_id": merchant_id},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
        gateway_name = gateway_name
        merchant_id = merchant_id
        supported_currencies = supported_currencies

        if not gateway_name or not merchant_id:
            return _error("gateway_name and merchant_id are required.")

        gateways = data.setdefault("payment_gateways", [])
        gateway = {
            "gateway_id": f"GW_{len(gateways) + 1:03d}",
            "gateway_name": gateway_name,
            "merchant_id": merchant_id,
            "supported_currencies": supported_currencies,
            "status": "active",
            "configured_at": FIXED_NOW,
        }
        gateways.append(gateway)

        result = {
            "gateway_id": gateway["gateway_id"],
            "gateway_name": gateway_name,
            "merchant_id": merchant_id,
            "status": "configured",
        }

        _append_audit(
            data,
            "payment_gateway_configured",
            gateway["gateway_id"],
            {"gateway_name": gateway_name, "merchant_id": merchant_id},
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigurePaymentGateway",
                "description": "Configure payment gateway settings and processing rules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "gateway_name": {"type": "string"},
                        "merchant_id": {"type": "string"},
                        "supported_currencies": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["gateway_name", "merchant_id"],
                },
            },
        }


class ManageCustomerSegments(Tool):
    """Establish and oversee customer segments according to behavior and demographics."""

    @staticmethod
    def invoke(data: dict[str, Any], segment_name: Any, criteria: Any = None) -> str:
        segment_name = f"{segment_name}".strip()
        if criteria is None:
            criteria = {}
        if not isinstance(criteria, dict):
            return _error("criteria must be an object.")
        if not segment_name:
            return _error("segment_name is required.")
        crit = dict(criteria)
        try:
            if "days" in crit and "period_days" not in crit:
                crit["period_days"] = int(crit.pop("days"))
        except Exception:
            crit["period_days"] = crit.pop("days")
        if "min_order" in crit and "min_orders" not in crit:
            crit["min_orders"] = crit.pop("min_order")
        for k in ("min_orders", "period_days", "lifetime_spend_usd"):
            if k in crit:
                try:
                    crit[k] = int(crit[k])
                except Exception:
                    pass
        segments = data.setdefault("customer_segments", [])
        segment_id = f"SEG_{len(segments) + 1:03d}"

        segment = {
            "segment_id": segment_id,
            "segment_name": segment_name,
            "criteria": crit,
            "customer_count": 10,
            "created_at": FIXED_NOW,
            "status": "active",
        }
        segments.append(segment)
        result = {
            "segment_id": segment_id,
            "segment_name": segment_name,
            "criteria": crit,
            "customer_count": 10,
        }

        _append_audit(
            data, "segment_created", segment_id, {"segment_name": segment_name}
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageCustomerSegments",
                "description": "Create and manage customer segments based on behavior and demographics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "segment_name": {"type": "string"},
                        "criteria": {"type": "object"},
                    },
                    "required": ["segment_name"],
                },
            },
        }


class ProcessBulkProductUpdate(Tool):
    """Handle mass updates to the product catalog with validation checks."""

    @staticmethod
    def invoke(
        data: dict[str, Any], update_type: Any, product_ids: Any, update_data: Any = {}
    ) -> str:
        update_type = f"{update_type}"
        product_ids = [_idstr(x) for x in (product_ids or [])]
        update_data = update_data or {}

        if not update_type or not product_ids:
            return _error("update_type and product_ids are required.")

        products = data.get("products", [])
        bulk_updates = data.setdefault("bulk_updates", [])
        updated_count = 0

        for pid in product_ids:
            product = _find_one(products, "product_id", pid)
            if product:
                if update_type == "price" and "list_price" in update_data:
                    product["list_price"] = update_data["list_price"]
                product["last_modified"] = FIXED_NOW
                updated_count += 1

        update_id = f"UPD_{len(bulk_updates) + 1:03d}"
        bulk_updates.append(
            {
                "update_id": update_id,
                "update_type": update_type,
                "product_ids": list(product_ids),
                "update_data": update_data,
                "processed_at": FIXED_NOW,
            }
        )

        _append_audit(
            data,
            "bulk_product_update",
            update_id,
            {"updated_count": updated_count, "update_type": update_type},
        )
        payload = {
                "update_type": update_type,
                "total_products": len(product_ids),
                "updated_count": updated_count,
                "update_id": update_id,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        update_type = f"{update_type}"
        product_ids = [_idstr(x) for x in (product_ids or [])]
        update_data = update_data or {}

        if not update_type or not product_ids:
            return _error("update_type and product_ids are required.")

        products = data.get("products", [])
        bulk_updates = data.setdefault("bulk_updates", [])
        updated_count = 0

        for pid in product_ids:
            product = _find_one(products, "product_id", pid)
            if product:
                if update_type == "price" and "list_price" in update_data:
                    product["list_price"] = update_data["list_price"]
                product["last_modified"] = FIXED_NOW
                updated_count += 1

        update_id = f"UPD_{len(bulk_updates) + 1:03d}"
        bulk_updates.append(
            {
                "update_id": update_id,
                "update_type": update_type,
                "product_ids": list(product_ids),
                "update_data": update_data,
                "processed_at": FIXED_NOW,
            }
        )

        _append_audit(
            data,
            "bulk_product_update",
            update_id,
            {"updated_count": updated_count, "update_type": update_type},
        )
        payload = {
                "update_type": update_type,
                "total_products": len(product_ids),
                "updated_count": updated_count,
                "update_id": update_id,
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
                "name": "ProcessBulkProductUpdate",
                "description": "Process bulk updates to product catalog with validation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "update_type": {"type": "string"},
                        "product_ids": {"type": "array", "items": {"type": "string"}},
                        "update_data": {"type": "object"},
                    },
                    "required": ["update_type", "product_ids"],
                },
            },
        }


class AnalyzeCustomerBehavior(Tool):
    """Examine customer buying patterns and produce insights."""

    @staticmethod
    def invoke(
        data: dict[str, Any], contact_id: Any, analysis_period: Any = "30d"
    ) -> str:
        contact_id = _idstr(contact_id)
        analysis_period = f"{analysis_period}"
        if not contact_id:
            return _error("contact_id is required.")

        contacts = data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        orders = data.get("orders", [])
        customer_orders = [
            o for o in orders if f"{o.get('contact_id')}" == f"{contact_id}"
        ]

        total_orders = len(customer_orders)
        total_value = sum(float(o.get("total_amount", 0.0)) for o in customer_orders)
        avg_order_value = (
            round(total_value / total_orders, 2) if total_orders > 0 else 0.0
        )

        analysis_id = f"ANLY_{contact_id}_{analysis_period}"
        _append_audit(
            data,
            "customer_behavior_analyzed",
            analysis_id,
            {"analysis_period": analysis_period},
        )
        payload = {
                "analysis_id": analysis_id,
                "contact_id": contact_id,
                "analysis_period": analysis_period,
                "total_orders": total_orders,
                "avg_order_value": avg_order_value,
                "preferred_categories": ["Electronics"],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        contact_id = _idstr(contact_id)
        analysis_period = f"{analysis_period}"
        if not contact_id:
            return _error("contact_id is required.")

        contacts = data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        orders = data.get("orders", [])
        customer_orders = [
            o for o in orders if f"{o.get('contact_id')}" == f"{contact_id}"
        ]

        total_orders = len(customer_orders)
        total_value = sum(float(o.get("total_amount", 0.0)) for o in customer_orders)
        avg_order_value = (
            round(total_value / total_orders, 2) if total_orders > 0 else 0.0
        )

        analysis_id = f"ANLY_{contact_id}_{analysis_period}"
        _append_audit(
            data,
            "customer_behavior_analyzed",
            analysis_id,
            {"analysis_period": analysis_period},
        )
        payload = {
                "analysis_id": analysis_id,
                "contact_id": contact_id,
                "analysis_period": analysis_period,
                "total_orders": total_orders,
                "avg_order_value": avg_order_value,
                "preferred_categories": ["Electronics"],
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
                "name": "AnalyzeCustomerBehavior",
                "description": "Analyze customer purchasing behavior and generate insights.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string"},
                        "analysis_period": {"type": "string"},
                    },
                    "required": ["contact_id"],
                },
            },
        }


class ManageSupplierRelationships(Tool):
    """Oversee relationships with suppliers and procurement processes."""

    @staticmethod
    def invoke(
        data: dict[str, Any], supplier_name: Any, action: Any, contact_email: str = None, supplier_data: Any = {}
    ) -> str:
        pass
        supplier_name = supplier_name
        action = action
        supplier_data = supplier_data

        if not supplier_name or not action:
            return _error("supplier_name and action are required.")

        suppliers = data.setdefault("suppliers", [])

        if action == "add":
            supplier = {
                "supplier_id": f"SUP_{len(suppliers) + 1:03d}",
                "supplier_name": supplier_name,
                "contact_email": contact_email,
                "rating": 4.0,
                "status": "active",
                "added_at": FIXED_NOW,
            }
            suppliers.append(supplier)

        result = {
            "supplier_name": supplier_name,
            "action": action,
            "status": "completed",
        }

        _append_audit(data, "supplier_managed", supplier_name, {"action": action})
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
        supplier_name = supplier_name
        action = action
        supplier_data = supplier_data

        if not supplier_name or not action:
            return _error("supplier_name and action are required.")

        suppliers = data.setdefault("suppliers", [])

        if action == "add":
            supplier = {
                "supplier_id": f"SUP_{len(suppliers) + 1:03d}",
                "supplier_name": supplier_name,
                "contact_email": supplier_data.get("contact_email"),
                "rating": 4.0,
                "status": "active",
                "added_at": FIXED_NOW,
            }
            suppliers.append(supplier)

        result = {
            "supplier_name": supplier_name,
            "action": action,
            "status": "completed",
        }

        _append_audit(data, "supplier_managed", supplier_name, {"action": action})
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageSupplierRelationships",
                "description": "Manage supplier relationships and procurement workflows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_name": {"type": "string"},
                        "action": {"type": "string"},
                        "supplier_data": {"type": "object"},
                    },
                    "required": ["supplier_name", "action"],
                },
            },
        }


class ProcessCustomerFeedback(Tool):
    """Handle and classify customer feedback for enhancement of quality."""

    @staticmethod
    def invoke(
        data: dict[str, Any], contact_id: Any, feedback_text: Any, rating: Any = None
    ) -> str:
        contact_id = _idstr(contact_id)
        feedback_text = f"{feedback_text}"
        rating = int(rating) if rating is not None else None

        if not contact_id or not feedback_text:
            return _error("contact_id and feedback_text are required.")

        contacts = data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        feedback_entries = data.setdefault("customer_feedback", [])
        feedback_id = f"FB_{len(feedback_entries) + 1:04d}"

        feedback = {
            "feedback_id": feedback_id,
            "contact_id": contact_id,
            "feedback_text": feedback_text,
            "rating": rating,
            "sentiment": "positive",
            "submitted_at": FIXED_NOW,
            "status": "new",
        }
        feedback_entries.append(feedback)

        _append_audit(
            data, "feedback_processed", feedback_id, {"contact_id": contact_id}
        )
        payload = {
                "feedback_id": feedback_id,
                "contact_id": contact_id,
                "sentiment": "positive",
                "rating": rating,
                "status": "processed",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        contact_id = _idstr(contact_id)
        feedback_text = f"{feedback_text}"
        rating = int(rating) if rating is not None else None

        if not contact_id or not feedback_text:
            return _error("contact_id and feedback_text are required.")

        contacts = data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        feedback_entries = data.setdefault("customer_feedback", [])
        feedback_id = f"FB_{len(feedback_entries) + 1:04d}"

        feedback = {
            "feedback_id": feedback_id,
            "contact_id": contact_id,
            "feedback_text": feedback_text,
            "rating": rating,
            "sentiment": "positive",
            "submitted_at": FIXED_NOW,
            "status": "new",
        }
        feedback_entries.append(feedback)

        _append_audit(
            data, "feedback_processed", feedback_id, {"contact_id": contact_id}
        )
        payload = {
                "feedback_id": feedback_id,
                "contact_id": contact_id,
                "sentiment": "positive",
                "rating": rating,
                "status": "processed",
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
                "name": "ProcessCustomerFeedback",
                "description": "Process and categorize customer feedback for quality improvement.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string"},
                        "feedback_text": {"type": "string"},
                        "rating": {"type": "integer"},
                    },
                    "required": ["contact_id", "feedback_text"],
                },
            },
        }


class ConfigureShippingRules(Tool):
    """Set up shipping regulations and delivery choices."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        rule_name: Any,
        shipping_zone: Any,
        customer_id: Any = None,
        tracking_enabled: bool = False
    ) -> str:
        customer_id = _idstr(customer_id) if customer_id is not None else None
        try:
            tracking_enabled = (
                bool(tracking_enabled)
                if isinstance(tracking_enabled, bool)
                else str(tracking_enabled).strip().lower() == "true"
            )
        except Exception:
            tracking_enabled = False

        shipping_zone = shipping_zone or ("US" if customer_id else None)
        if shipping_zone == "US-Standard":
            shipping_zone = "US-Std"

        if not rule_name or not shipping_zone:
            return _error("rule_name and shipping_zone are required.")

        shipping_rules = data.setdefault("shipping_rules", [])
        rule_id = f"SHIP_{len(shipping_rules) + 1:03d}"

        rule = {
            "rule_id": rule_id,
            "rule_name": rule_name,
            "shipping_zone": shipping_zone,
            "tracking_enabled": bool(tracking_enabled),
            "base_cost": 5.99,
            "created_at": FIXED_NOW,
            "status": "active",
        }
        shipping_rules.append(rule)

        result = {
            "rule_id": rule_id,
            "rule_name": rule_name,
            "shipping_zone": shipping_zone,
            "status": "configured",
        }

        _append_audit(
            data, "shipping_rule_configured", rule_id, {"rule_name": rule_name}
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
        customer_id = _idstr(customer_id) if customer_id is not None else None
        try:
            tracking_enabled = (
                bool(tracking_enabled)
                if isinstance(tracking_enabled, bool)
                else str(tracking_enabled).strip().lower() == "true"
            )
        except Exception:
            tracking_enabled = False

        shipping_zone = shipping_zone or ("US" if customer_id else None)
        if shipping_zone == "US-Standard":
            shipping_zone = "US-Std"

        if not rule_name or not shipping_zone:
            return _error("rule_name and shipping_zone are required.")

        shipping_rules = data.setdefault("shipping_rules", [])
        rule_id = f"SHIP_{len(shipping_rules) + 1:03d}"

        rule = {
            "rule_id": rule_id,
            "rule_name": rule_name,
            "shipping_zone": shipping_zone,
            "tracking_enabled": bool(tracking_enabled),
            "base_cost": 5.99,
            "created_at": FIXED_NOW,
            "status": "active",
        }
        shipping_rules.append(rule)

        result = {
            "rule_id": rule_id,
            "rule_name": rule_name,
            "shipping_zone": shipping_zone,
            "status": "configured",
        }

        _append_audit(
            data, "shipping_rule_configured", rule_id, {"rule_name": rule_name}
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureShippingRules",
                "description": "Configure shipping rules and delivery options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_name": {"type": "string"},
                        "tracking_enabled": {"type": "boolean"},
                        "customer_id": {"type": "string"},
                        "shipping_zone": {"type": "string"},
                    },
                    "required": ["rule_name", "shipping_zone"],
                },
            },
        }


class ManageProductRecommendations(Tool):
    """Create and oversee product suggestions for customers."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        contact_id: Any,
        recommendation_type: Any = "similar_products",
        contacts: list = None,
        products: list = None
    ) -> str:
        pass
        contact_id = _idstr(contact_id)
        recommendation_type = f"{recommendation_type}"
        if not contact_id:
            return _error("contact_id is required.")

        contacts = contacts if contacts is not None else data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        products = products if products is not None else data.get("products", [])
        recommendations = products[:3]

        recommendation_list = [
            {
                "product_id": p.get("product_id"),
                "product_name": p.get("name"),
                "confidence_score": round(0.9 - (i * 0.1), 2),
            }
            for i, p in enumerate(recommendations)
        ]

        _append_audit(
            data,
            "recommendations_generated",
            contact_id,
            {"recommendation_type": recommendation_type},
        )
        payload = {
                "contact_id": contact_id,
                "recommendation_type": recommendation_type,
                "recommendations": recommendation_list,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        contact_id = _idstr(contact_id)
        recommendation_type = f"{recommendation_type}"
        if not contact_id:
            return _error("contact_id is required.")

        contacts = data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        products = data.get("products", [])
        recommendations = products[:3]

        recommendation_list = [
            {
                "product_id": p.get("product_id"),
                "product_name": p.get("name"),
                "confidence_score": round(0.9 - (i * 0.1), 2),
            }
            for i, p in enumerate(recommendations)
        ]

        _append_audit(
            data,
            "recommendations_generated",
            contact_id,
            {"recommendation_type": recommendation_type},
        )
        payload = {
                "contact_id": contact_id,
                "recommendation_type": recommendation_type,
                "recommendations": recommendation_list,
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
                "name": "ManageProductRecommendations",
                "description": "Generate and manage product recommendations for customers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string"},
                        "recommendation_type": {"type": "string"},
                    },
                    "required": ["contact_id"],
                },
            },
        }


class ProcessLoyaltyProgram(Tool):
    """Oversee enrollment in the customer loyalty program and associated rewards."""

    @staticmethod
    def invoke(
        data: dict[str, Any], contact_id: Any, action: Any, points: Any = 0
    ) -> str:
        contact_id = _idstr(contact_id)
        action = f"{action}".strip().lower()
        try:
            points = int(points)
        except Exception:
            points = 0

        if not contact_id or not action:
            return _error("contact_id and action are required.")

        contacts = data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        loyalty_members = data.setdefault("loyalty_program", [])
        member = _find_one(loyalty_members, "contact_id", contact_id)

        # registration route
        if action == "enroll" and not member:
            member = {
                "contact_id": contact_id,
                "member_id": f"LOY_{len(loyalty_members) + 1:04d}",
                "points_balance": 100,
                "tier": "bronze",
                "enrolled_at": FIXED_NOW,
                "status": "active",
            }
            loyalty_members.append(member)

        # standardize frequent synonyms for action
        _LOY_MAP = {"add_points": "add", "adjust_points": "adjust"}
        action = _LOY_MAP.get(action, action)

        if action in ("add", "adjust"):
            if not member:
                member = {
                    "contact_id": contact_id,
                    "member_id": f"LOY_{len(loyalty_members) + 1:04d}",
                    "points_balance": 0,
                    "tier": "bronze",
                    "enrolled_at": FIXED_NOW,
                    "status": "active",
                }
                loyalty_members.append(member)
            member["points_balance"] = int(member.get("points_balance", 0)) + int(points)

        _append_audit(data, "loyalty_program_activity", contact_id, {"action": action})
        payload = {
            "contact_id": contact_id,
            "action": action,
            "points": points,
            "points_balance": member.get("points_balance", 0) if member else 0,
            "tier": member.get("tier", "bronze") if member else "bronze",
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        contact_id = _idstr(contact_id)
        action = f"{action}".strip().lower()
        try:
            points = int(points)
        except Exception:
            points = 0

        if not contact_id or not action:
            return _error("contact_id and action are required.")

        contacts = data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        loyalty_members = data.setdefault("loyalty_program", [])
        member = _find_one(loyalty_members, "contact_id", contact_id)

        #registration route
        if action == "enroll" and not member:
            member = {
                "contact_id": contact_id,
                "member_id": f"LOY_{len(loyalty_members) + 1:04d}",
                "points_balance": 100,
                "tier": "bronze",
                "enrolled_at": FIXED_NOW,
                "status": "active",
            }
            loyalty_members.append(member)

        #standardize frequent synonyms for action
        _LOY_MAP = {"add_points": "add", "adjust_points": "adjust"}
        action = _LOY_MAP.get(action, action)

        if action in ("add", "adjust"):
            if not member:
                member = {
                    "contact_id": contact_id,
                    "member_id": f"LOY_{len(loyalty_members) + 1:04d}",
                    "points_balance": 0,
                    "tier": "bronze",
                    "enrolled_at": FIXED_NOW,
                    "status": "active",
                }
                loyalty_members.append(member)
            member["points_balance"] = int(member.get("points_balance", 0)) + int(
                points
            )

        _append_audit(data, "loyalty_program_activity", contact_id, {"action": action})
        payload = {
                "contact_id": contact_id,
                "action": action,
                "points": points,
                "points_balance": member.get("points_balance", 0) if member else 0,
                "tier": member.get("tier", "bronze") if member else "bronze",
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
                "name": "ProcessLoyaltyProgram",
                "description": "Manage customer loyalty program enrollment and rewards.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string"},
                        "action": {"type": "string"},
                        "points": {"type": "integer"},
                    },
                    "required": ["contact_id", "action"],
                },
            },
        }


class ConfigureContentDeliveryNetwork(Tool):
    """Set up CDN configurations to enhance content delivery efficiency."""

    @staticmethod
    def invoke(
        data: dict[str, Any], cdn_provider: Any, region: Any = "us-east-1"
    ) -> str:
        if not cdn_provider:
            return _error("cdn_provider is required.")

        cdn_configs = data.setdefault("cdn_configurations", [])
        config_id = f"CDN_{len(cdn_configs) + 1:03d}"

        config = {
            "config_id": config_id,
            "cdn_provider": cdn_provider,
            "region": region,
            "configured_at": FIXED_NOW,
            "status": "active",
        }
        cdn_configs.append(config)

        result = {
            "config_id": config_id,
            "cdn_provider": cdn_provider,
            "region": region,
            "status": "configured",
        }

        _append_audit(data, "cdn_configured", config_id, {"cdn_provider": cdn_provider})
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
        cdn_provider = cdn_provider
        region = region

        if not cdn_provider:
            return _error("cdn_provider is required.")

        cdn_configs = data.setdefault("cdn_configurations", [])
        config_id = f"CDN_{len(cdn_configs) + 1:03d}"

        config = {
            "config_id": config_id,
            "cdn_provider": cdn_provider,
            "region": region,
            "configured_at": FIXED_NOW,
            "status": "active",
        }
        cdn_configs.append(config)

        result = {
            "config_id": config_id,
            "cdn_provider": cdn_provider,
            "region": region,
            "status": "configured",
        }

        _append_audit(data, "cdn_configured", config_id, {"cdn_provider": cdn_provider})
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureContentDeliveryNetwork",
                "description": "Configure CDN settings for improved content delivery performance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cdn_provider": {"type": "string"},
                        "region": {"type": "string"},
                    },
                    "required": ["cdn_provider"],
                },
            },
        }


class ManageApiRateLimits(Tool):
    """Establish and oversee API rate limiting rules."""

    @staticmethod
    def invoke(data: dict[str, Any], api_endpoint: Any, rate_limit: Any = 100) -> str:
        if not api_endpoint:
            return _error("api_endpoint is required.")

        rate_limits = data.setdefault("api_rate_limits", [])
        limit_id = f"RATE_{len(rate_limits) + 1:03d}"

        rate_limit_config = {
            "limit_id": limit_id,
            "api_endpoint": api_endpoint,
            "rate_limit": rate_limit,
            "configured_at": FIXED_NOW,
            "status": "active",
        }
        rate_limits.append(rate_limit_config)

        result = {
            "limit_id": limit_id,
            "api_endpoint": api_endpoint,
            "rate_limit": rate_limit,
            "status": "configured",
        }

        _append_audit(
            data, "rate_limit_configured", limit_id, {"api_endpoint": api_endpoint}
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageApiRateLimits",
                "description": "Configure and manage API rate limiting policies.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "api_endpoint": {"type": "string"},
                        "rate_limit": {"type": "integer"},
                    },
                    "required": ["api_endpoint"],
                },
            },
        }


class ProcessDataBackup(Tool):
    """Oversee data backup and restoration activities."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        backup_type: Any = "incremental",
        storage_location: Any = "s3"
    ) -> str:
        backups = data.setdefault("data_backups", [])
        backup_id = f"BKP_{len(backups) + 1:04d}"

        backup = {
            "backup_id": backup_id,
            "backup_type": backup_type,
            "storage_location": storage_location,
            "data_size_mb": 1024,
            "started_at": FIXED_NOW,
            "status": "completed",
        }
        backups.append(backup)

        result = {
            "backup_id": backup_id,
            "backup_type": backup_type,
            "storage_location": storage_location,
            "status": "completed",
        }

        _append_audit(data, "backup_processed", backup_id, {"backup_type": backup_type})
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
        backup_type = backup_type
        storage_location = storage_location

        backups = data.setdefault("data_backups", [])
        backup_id = f"BKP_{len(backups) + 1:04d}"

        backup = {
            "backup_id": backup_id,
            "backup_type": backup_type,
            "storage_location": storage_location,
            "data_size_mb": 1024,
            "started_at": FIXED_NOW,
            "status": "completed",
        }
        backups.append(backup)

        result = {
            "backup_id": backup_id,
            "backup_type": backup_type,
            "storage_location": storage_location,
            "status": "completed",
        }

        _append_audit(data, "backup_processed", backup_id, {"backup_type": backup_type})
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessDataBackup",
                "description": "Manage data backup and recovery operations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "backup_type": {"type": "string"},
                        "storage_location": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class GetDataBackupInfo(Tool):
    """Retrieve backup metadata using backup_id or provide the most recent backup."""

    @staticmethod
    def invoke(data: dict[str, Any], backup_id: Any = None) -> str:
        backups = data.get("data_backups", [])
        if not backups:
            return _error("No backups found.")
        if backup_id:
            match = _find_one(backups, "backup_id", backup_id)
            if not match:
                return _error(f"Backup '{backup_id}' not found.")
            payload = match
            out = json.dumps(payload, indent=2)
            return out
        payload = backups[-1]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDataBackupInfo",
                "description": "Fetch backup metadata by backup_id or the latest backup if none specified.",
                "parameters": {
                    "type": "object",
                    "properties": {"backup_id": {"type": "string"}},
                    "required": [],
                },
            },
        }


class GetNextCartId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], carts: list[dict[str, Any]] = None) -> str:
        if carts is None:
            carts = []
        if not carts:
            next_id = 706
        else:
            max_id = max(int(c.get("cart_id", "0")) for c in carts)
            next_id = max_id + 1
        payload = {"next_cart_id": f"{next_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNextCartId",
                "description": "Return the next available cart_id as a zero-padded string.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class GetNextOrderId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], orders: list = None) -> str:
        if orders is None:
            orders = data.get("orders", [])
        if not orders:
            next_id = 9017
        else:
            max_id = max(int(o.get("order_id", "0")) for o in orders)
            next_id = max_id + 1
        payload = {"next_order_id": f"{next_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNextOrderId",
                "description": "Return the next available order_id as a zero-padded string.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class GetCacheClusterInfo(Tool):
    """Obtain ElastiCache cluster information using cluster_id."""

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any) -> str:
        cluster_id = _idstr(cluster_id)
        if not cluster_id:
            return _error("cluster_id is required.")
        clusters = data.get("aws_elasticache_clusters", [])
        cluster = _find_one(clusters, "cluster_id", cluster_id)
        if not cluster:
            return _error(f"Cluster '{cluster_id}' not found.")
        payload = cluster
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCacheClusterInfo",
                "description": "Fetch ElastiCache cluster details by cluster_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }


class GetApiRateLimitConfig(Tool):
    """Retrieve rate limit settings for a specified API endpoint."""

    @staticmethod
    def invoke(data: dict[str, Any], api_endpoint: Any) -> str:
        if not api_endpoint:
            return _error("api_endpoint is required.")

        rate_limits = data.get("api_rate_limits", [])
        configs = [rl for rl in rate_limits if rl.get("api_endpoint") == api_endpoint]
        if not configs:
            return _error(f"Rate limit for '{api_endpoint}' not found.")
        latest = configs[-1]
        payload = latest
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetApiRateLimitConfig",
                "description": "Fetch rate limit configuration for a given API endpoint.",
                "parameters": {
                    "type": "object",
                    "properties": {"api_endpoint": {"type": "string"}},
                    "required": ["api_endpoint"],
                },
            },
        }


class GetConnectedAppSecurity(Tool):
    """Obtain security settings for connected apps using app_id."""

    @staticmethod
    def invoke(data: dict[str, Any], app_id: Any) -> str:
        app_id = _idstr(app_id)
        if not app_id:
            return _error("app_id is required.")
        apps = data.get("connected_apps", [])
        app = _find_one(apps, "app_id", app_id)
        if not app:
            return _error(f"Connected app '{app_id}' not found.")
        payload = app
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetConnectedAppSecurity",
                "description": "Fetch connected app security configuration by app_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"app_id": {"type": "string"}},
                    "required": ["app_id"],
                },
            },
        }


TOOLS = [
    FindProductByName(),
    GetCustomerProfile(),
    SearchProductsByCategory(),
    CreateShoppingCart(),
    ApplyDiscountBundle(),
    ProcessOrderWithFulfillment(),
    ProcessReturnWithRefund(),
    ConfigureCacheIntegration(),
    UpdateCacheClusterStatus(),
    GetCacheClusterInfo(),
    AddSecurityGroupRule(),
    ManageConnectedAppSecurity(),
    GetConnectedAppSecurity(),
    OptimizeSecurityGroupRules(),
    GetAuditLog(),
    ManageInventoryLevels(),
    GeneratePromotionalCampaign(),
    ConfigurePaymentGateway(),
    ManageCustomerSegments(),
    ProcessBulkProductUpdate(),
    AnalyzeCustomerBehavior(),
    ManageSupplierRelationships(),
    ProcessCustomerFeedback(),
    ConfigureShippingRules(),
    ManageProductRecommendations(),
    ProcessLoyaltyProgram(),
    ConfigureContentDeliveryNetwork(),
    ManageApiRateLimits(),
    GetApiRateLimitConfig(),
    ProcessDataBackup(),
    GetDataBackupInfo(),
    GetNextCartId(),
    GetNextOrderId(),
]
