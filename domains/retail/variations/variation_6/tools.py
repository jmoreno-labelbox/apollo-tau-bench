import json
from typing import Any

from domains.dto import Tool


def _find_product_by_item(data, item_id):
    pass
    for p in data.get("products", []):
        variants = p.get("variants", {})
        if item_id in variants:
            return p, variants[item_id]
    return None, None


def _find_courier(data, courier_id):
    pass
    return next(
        (c for c in data.get("couriers", []) if c.get("courier_id") == courier_id), None
    )


def _ensure_list(dct, key):
    pass
    if key not in dct or not isinstance(dct[key], list):
        dct[key] = []
    return dct[key]


def _find_order(data, order_id):
    pass
    return next(
        (o for o in data.get("orders", []) if o.get("order_id") == order_id), None
    )


def _find_tracking(data, tracking_id):
    pass
    return next(
        (
            t
            for t in data.get("tracking", [])
            if tracking_id in t.get("tracking_id", [])
        ),
        None,
    )


def _find_user(data, user_id):
    pass
    return next((u for u in data.get("users", []) if u.get("user_id") == user_id), None)


class GetUserById(Tool):
    """Retrieve a user using user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        user = _find_user(data, user_id)
        payload = user or {"error": f"user_id {user_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getUserById",
                "description": "Return the user object by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class FindUsersByCity(Tool):
    """Enumerate users in a specified city (exact match)."""

    @staticmethod
    def invoke(data, city: str = None) -> str:
        if not city:
            payload = {"error": "city is required"}
            out = json.dumps(payload, indent=2)
            return out
        users = data.get("users", [])
        out = [u for u in users if u.get("address", {}).get("city") == city]
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "findUsersByCity",
                "description": "Find all users whose address.city equals the given city.",
                "parameters": {
                    "type": "object",
                    "properties": {"city": {"type": "string"}},
                    "required": ["city"],
                },
            },
        }


class UpdateUserAddress(Tool):
    """Modify a user's address to the supplied fields."""

    @staticmethod
    def invoke(data, user_id=None, address=None) -> str:
        if not user_id or not isinstance(address, dict):
            payload = {"error": "user_id and address (object) are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        user = _find_user(data, user_id)
        if not user:
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        user["address"] = address
        payload = {"success": True, "user_id": user_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateUserAddress",
                "description": "Replace a user's address with the provided object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "address": {"type": "object"},
                    },
                    "required": ["user_id", "address"],
                },
            },
        }


class AddPaymentMethod(Tool):
    """Link a payment method record to a user. A stable id must be included in the payload."""

    @staticmethod
    def invoke(data, user_id: str = None, payment_method: dict = None) -> str:
        if not user_id or not isinstance(payment_method, dict) or "id" not in payment_method:
            payload = {"error": "user_id and payment_method object with 'id' are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        user = _find_user(data, user_id)
        if not user:
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        pm = user.setdefault("payment_methods", {})
        pm[payment_method["id"]] = payment_method
        payload = {"success": True, "user_id": user_id, "payment_method_id": payment_method["id"]}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "addPaymentMethod",
                "description": "Add/update a payment method on a user. The payload must include a 'id'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "payment_method": {"type": "object"},
                    },
                    "required": ["user_id", "payment_method"],
                },
            },
        }


class GetProductById(Tool):
    """Fetch a product using product_id."""

    @staticmethod
    def invoke(data, product_id: str = None) -> str:
        if not product_id:
            payload = {"error": "product_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        prod = next(
            (p for p in data.get("products", []) if p.get("product_id") == product_id),
            None,
        )
        payload = prod or {"error": f"product_id {product_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getProductById",
                "description": "Get a product by product_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"product_id": {"type": "string"}},
                    "required": ["product_id"],
                },
            },
        }


class GetItemVariant(Tool):
    """Retrieve product and variant using item_id."""

    @staticmethod
    def invoke(data, item_id: str = None) -> str:
        if not item_id:
            payload = {"error": "item_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        prod, variant = _find_product_by_item(data, item_id)
        if not prod:
            payload = {"error": f"item_id {item_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"product_id": prod["product_id"], "variant": variant}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getItemVariant",
                "description": "Return the variant record and product_id for a given item_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"item_id": {"type": "string"}},
                    "required": ["item_id"],
                },
            },
        }


class SetVariantAvailability(Tool):
    """Adjust a variant's 'available' status."""

    @staticmethod
    def invoke(data, item_id=None, available=None) -> str:
        if item_id is None or available is None:
            payload = {"error": "item_id and available are required"}
            out = json.dumps(payload, indent=2)
            return out
        prod, variant = _find_product_by_item(data, item_id)
        if not prod:
            payload = {"error": f"item_id {item_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        prod["variants"][item_id]["available"] = bool(available)
        payload = {"success": True, "item_id": item_id, "available": bool(available)}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "setVariantAvailability",
                "description": "Set the boolean 'available' flag for a variant.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "available": {"type": "boolean"},
                    },
                    "required": ["item_id", "available"],
                },
            },
        }


class SetVariantPrice(Tool):
    """Assign a specific numeric value as the price for a variant."""

    @staticmethod
    def invoke(data, item_id=None, price=None) -> str:
        if item_id is None or price is None:
            payload = {"error": "item_id and price are required"}
            out = json.dumps(payload, indent=2)
            return out
        prod, variant = _find_product_by_item(data, item_id)
        if not prod:
            payload = {"error": f"item_id {item_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        prod["variants"][item_id]["price"] = float(price)
        payload = {"success": True, "item_id": item_id, "price": float(price)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "setVariantPrice",
                "description": "Set a specific variant price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "price": {"type": "number"},
                    },
                    "required": ["item_id", "price"],
                },
            },
        }


class SearchProductsByName(Tool):
    """Search for a substring in names without case sensitivity (read-only)."""

    @staticmethod
    def invoke(data, query: str = "") -> str:
        q = query.lower()
        out = [p for p in data.get("products", []) if q in p.get("name", "").lower()]
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "searchProductsByName",
                "description": "Search products by name (case-insensitive contains).",
                "parameters": {
                    "type": "object",
                    "properties": {"query": {"type": "string"}},
                },
            },
        }


class GetOrderDetails(Tool):
    """Fetch an order using its ID."""

    @staticmethod
    def invoke(data, order_id=None) -> str:
        if not order_id:
            payload = {"error": "order_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        order = _find_order(data, order_id)
        payload = order or {"error": f"order_id {order_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getOrderDetails",
                "description": "Fetch an order by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class UpdateOrderStatus(Tool):
    """Update the order status to the given value."""

    @staticmethod
    def invoke(data, order_id=None, status=None) -> str:
        if not order_id or status is None:
            payload = {"error": "order_id and status are required"}
            out = json.dumps(payload, indent=2)
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        o["status"] = status
        payload = {"success": True, "order_id": order_id, "status": status}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateOrderStatus",
                "description": "Update the status field on an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["order_id", "status"],
                },
            },
        }


class AddOrderPayment(Tool):
    """Add a payment record."""

    @staticmethod
    def invoke(data, order_id=None, amount=None, payment_method_id=None, transaction_id=None) -> str:
        if not order_id or amount is None or not payment_method_id or not transaction_id:
            payload = {
                "error": "order_id, amount, payment_method_id, transaction_id are required"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        hist = _ensure_list(o, "payment_history")
        # idempotent: substitute existing with the same txn_id
        existing = next((h for h in hist if h.get("transaction_id") == transaction_id), None)
        record = {
            "transaction_type": "payment",
            "amount": float(amount),
            "payment_method_id": payment_method_id,
            "transaction_id": transaction_id,
        }
        if existing:
            existing.update(record)
        else:
            hist.append(record)
        payload = {"success": True, "order_id": order_id, "transaction_id": transaction_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "addOrderPayment",
                "description": "Add or upsert a payment record for an order (by transaction_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "amount": {"type": "number"},
                        "payment_method_id": {"type": "string"},
                        "transaction_id": {"type": "string"},
                    },
                    "required": [
                        "order_id",
                        "amount",
                        "payment_method_id",
                        "transaction_id",
                    ],
                },
            },
        }


class RefundOrderPayment(Tool):
    """Add a refund record using the specified refund_id."""

    @staticmethod
    def invoke(data, order_id: str = None, amount: float = None, reason_code: str = None, refund_id: str = None) -> str:
        if not order_id or amount is None or not reason_code or not refund_id:
            payload = {"error": "order_id, amount, reason_code, refund_id are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        hist = _ensure_list(o, "payment_history")
        existing = next((h for h in hist if h.get("refund_id") == refund_id), None)
        record = {
            "transaction_type": "refund",
            "amount": float(amount),
            "reason_code": reason_code,
            "refund_id": refund_id,
        }
        if existing:
            existing.update(record)
        else:
            hist.append(record)
        payload = {"success": True, "order_id": order_id, "refund_id": refund_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "refundOrderPayment",
                "description": "Add or upsert a refund record for an order (by refund_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "amount": {"type": "number"},
                        "reason_code": {"type": "string"},
                        "refund_id": {"type": "string"},
                    },
                    "required": ["order_id", "amount", "reason_code", "refund_id"],
                },
            },
        }


class CancelOrderItems(Tool):
    """Designate certain items in an order as cancelled with a reason_code (adds 'cancelled': True)."""

    @staticmethod
    def invoke(data, order_id: str = None, item_ids: list = None, reason_code: str = None) -> str:
        if item_ids is None:
            item_ids = []
        if not order_id or not item_ids or not reason_code:
            payload = {"error": "order_id, item_ids, reason_code are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        updated = []
        for item in o.get("items", []):
            if item.get("item_id") in item_ids:
                item["cancelled"] = True
                item["cancellation_reason"] = reason_code
                updated.append(item["item_id"])
        payload = {
                "success": True,
                "order_id": order_id,
                "cancelled_item_ids": updated,
                "reason_code": reason_code,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "cancelOrderItems",
                "description": "Mark given item_ids in an order as cancelled with a reason_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "reason_code": {"type": "string"},
                    },
                    "required": ["order_id", "item_ids", "reason_code"],
                },
            },
        }


class UpdateItemOption(Tool):
    """Modify a specific option key for a particular item in an order."""

    @staticmethod
    def invoke(data, order_id=None, item_id=None, option_key=None, option_value=None) -> str:
        if not order_id or not item_id or option_key is None or option_value is None:
            payload = {"error": "order_id, item_id, option_key, option_value are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        it = next((i for i in o.get("items", []) if i.get("item_id") == item_id), None)
        if not it:
            payload = {"error": f"item_id {item_id} not in order {order_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        opts = it.setdefault("options", {})
        opts[option_key] = option_value
        payload = {
                "success": True,
                "order_id": order_id,
                "item_id": item_id,
                "option_key": option_key,
                "option_value": option_value,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateItemOption",
                "description": "Update a single option on an order item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "option_key": {"type": "string"},
                        "option_value": {},
                    },
                    "required": ["order_id", "item_id", "option_key", "option_value"],
                },
            },
        }


class AddOrderTag(Tool):
    """Include a tag string to an order (idempotent)."""

    @staticmethod
    def invoke(data, order_id=None, tag=None) -> str:
        if not order_id or tag is None:
            payload = {"error": "order_id and tag are required"}
            out = json.dumps(payload, indent=2)
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        tags = o.setdefault("order_tags", [])
        if tag not in tags:
            tags.append(tag)
        payload = {"success": True, "order_id": order_id, "tag": tag}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "addOrderTag",
                "description": "Append a tag to order.order_tags if not present.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "tag": {"type": "string"},
                    },
                    "required": ["order_id", "tag"],
                },
            },
        }


class ComputeOrderTotal(Tool):
    """Calculate the total of item prices for an order (excludes refunds/payments)."""

    @staticmethod
    def invoke(data, order_id: str = None) -> str:
        if not order_id:
            payload = {"error": "order_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        total = sum(i.get("price", 0) for i in o.get("items", []))
        payload = {"order_id": order_id, "computed_total": round(float(total), 2)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "computeOrderTotal",
                "description": "Return computed sum of item prices for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class GetTrackingInfo(Tool):
    """Fetch tracking record using tracking_id."""

    @staticmethod
    def invoke(data, tracking_id=None) -> str:
        if not tracking_id:
            payload = {"error": "tracking_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        t = _find_tracking(data, tracking_id)
        payload = t or {"error": f"tracking_id {tracking_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getTrackingInfo",
                "description": "Get tracking record by tracking_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"tracking_id": {"type": "string"}},
                    "required": ["tracking_id"],
                },
            },
        }


class AppendTrackingEvent(Tool):
    """Insert or replace an event timestamp in tracking_history for a tracking id (key -> timestamp)."""

    @staticmethod
    def invoke(data, tracking_id=None, event=None, timestamp=None) -> str:
        if not tracking_id or not event or not timestamp:
            payload = {"error": "tracking_id, event, timestamp are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        t = _find_tracking(data, tracking_id)
        if not t:
            payload = {"error": f"tracking_id {tracking_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        history = t.setdefault("tracking_history", {})
        history[event] = timestamp
        payload = {
                "success": True,
                "tracking_id": tracking_id,
                "event": event,
                "timestamp": timestamp,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "appendTrackingEvent",
                "description": "Set an event timestamp in tracking.tracking_history for a given tracking_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "event": {"type": "string"},
                        "timestamp": {"type": "string"},
                    },
                    "required": ["tracking_id", "event", "timestamp"],
                },
            },
        }


class LinkTrackingToOrder(Tool):
    """Create a fulfillment record that associates tracking_id and item_ids with an order (idempotent by exact tuple)."""

    @staticmethod
    def invoke(data, order_id: str = None, tracking_id: str = None, item_ids: list = None) -> str:
        if item_ids is None:
            item_ids = []
        if not order_id or not tracking_id or not item_ids:
            payload = {"error": "order_id, tracking_id, item_ids are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        fl = _ensure_list(o, "fulfillments")
        payload = {"tracking_id": [tracking_id], "item_ids": item_ids}
        if payload not in fl:
            fl.append(payload)
        payload = {
                "success": True,
                "order_id": order_id,
                "tracking_id": tracking_id,
                "item_ids": item_ids,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "linkTrackingToOrder",
                "description": "Append a fulfillment mapping (tracking_id, item_ids) to an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "tracking_id": {"type": "string"},
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["order_id", "tracking_id", "item_ids"],
                },
            },
        }


class SplitOrderFulfillment(Tool):
    """Establish a new tracking record and fulfillment for a selection of items, based on the given tracking_id and courier_id."""

    @staticmethod
    def invoke(
        data, 
        order_id: str, 
        item_ids: list = [], 
        tracking_id: str = None, 
        courier_id: str = None, 
        delivery_options: str = "Standard", 
        address: str = None
    ) -> str:
        if not order_id or not item_ids or not tracking_id or not courier_id:
            payload = {"error": "order_id, item_ids, tracking_id, courier_id are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        order = _find_order(data, order_id)
        if not order:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        # Establish or replace tracking record
        tr_list = data.setdefault("tracking", [])
        tr = _find_tracking(data, tracking_id)
        if not tr:
            tr = {
                "tracking_id": [tracking_id],
                "item_ids": item_ids,
                "address": address or order.get("address"),
                "delivery_carrier": courier_id,
                "delivery_options": delivery_options,
                "order_id": order_id,
                "tracking_history": {},
            }
            tr_list.append(tr)
        else:
            tr["item_ids"] = item_ids
            tr["delivery_carrier"] = courier_id
            tr["delivery_options"] = delivery_options
            tr["order_id"] = order_id
            tr["address"] = address or order.get("address")
        # Connect to order fulfillments
        fl = _ensure_list(order, "fulfillments")
        payload = {"tracking_id": [tracking_id], "item_ids": item_ids}
        if payload not in fl:
            fl.append(payload)
        payload = {
            "success": True,
            "order_id": order_id,
            "tracking_id": tracking_id,
            "courier_id": courier_id,
            "item_ids": item_ids,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "splitOrderFulfillment",
                "description": "Create a tracking record and link a subset of items to it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "tracking_id": {"type": "string"},
                        "courier_id": {"type": "string"},
                        "delivery_options": {"type": "string"},
                        "address": {"type": "object"},
                    },
                    "required": ["order_id", "item_ids", "tracking_id", "courier_id"],
                },
            },
        }


class GetSupplierDetails(Tool):
    """Retrieve supplier record using supplier_id."""

    @staticmethod
    def invoke(data, supplier_id: str = None) -> str:
        if not supplier_id:
            payload = {"error": "supplier_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        sup = next(
            (
                s
                for s in data.get("suppliers", [])
                if s.get("supplier_id") == supplier_id
            ),
            None,
        )
        payload = sup or {"error": f"supplier_id {supplier_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getSupplierDetails",
                "description": "Fetch supplier by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"supplier_id": {"type": "string"}},
                    "required": ["supplier_id"],
                },
            },
        }


class PlaceSupplyOrder(Tool):
    """Establish or modify a supply order using the given supply_order_id."""

    @staticmethod
    def invoke(
        data,
        supply_order_id: str = None,
        supplier_id: str = None,
        product_id: str = None,
        item_id: str = None,
        quantity: int = None,
        unit_cost: float = None,
        status: str = "pending"
    ) -> str:
        if (
            not all([supply_order_id, supplier_id, product_id, item_id])
            or quantity is None
            or unit_cost is None
        ):
            payload = {
                "error": "supply_order_id, supplier_id, product_id, item_id, quantity, unit_cost are required"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        so_list = data.setdefault("supply_orders", [])
        existing = next(
            (s for s in so_list if s.get("supply_order_id") == supply_order_id), None
        )
        record = {
            "supply_order_id": supply_order_id,
            "supplier_id": supplier_id,
            "product_id": product_id,
            "item_id": item_id,
            "quantity": int(quantity),
            "status": status,
            "order_date": "2025-01-01T00:00:00",
            "unit_cost": float(unit_cost),
            "total_cost": round(float(unit_cost) * int(quantity), 2),
        }
        if existing:
            existing.update(record)
        else:
            so_list.append(record)
        payload = {"success": True, "supply_order_id": supply_order_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "placeSupplyOrder",
                "description": "Create or overwrite a supply order by supply_order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "supplier_id": {"type": "string"},
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "quantity": {"type": "integer"},
                        "unit_cost": {"type": "number"},
                        "status": {"type": "string"},
                    },
                    "required": [
                        "supply_order_id",
                        "supplier_id",
                        "product_id",
                        "item_id",
                        "quantity",
                        "unit_cost",
                    ],
                },
            },
        }


class UpdateSupplyOrderStatus(Tool):
    """Update the status of a supply order."""

    @staticmethod
    def invoke(data, supply_order_id=None, status=None) -> str:
        if not supply_order_id or not status:
            payload = {"error": "supply_order_id and status are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        so = next(
            (
                s
                for s in data.get("supply_orders", [])
                if s.get("supply_order_id") == supply_order_id
            ),
            None,
        )
        if not so:
            payload = {"error": f"supply_order_id {supply_order_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        so["status"] = status
        payload = {"success": True, "supply_order_id": supply_order_id, "status": status}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateSupplyOrderStatus",
                "description": "Update a supply order's status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["supply_order_id", "status"],
                },
            },
        }


class GetCourierDetails(Tool):
    """Retrieve courier record."""

    @staticmethod
    def invoke(data, courier_id: str = None) -> str:
        if not courier_id:
            payload = {"error": "courier_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        c = _find_courier(data, courier_id)
        payload = c or {"error": f"courier_id {courier_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getCourierDetails",
                "description": "Fetch courier record by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"courier_id": {"type": "string"}},
                    "required": ["courier_id"],
                },
            },
        }


class ReassignCourierForTracking(Tool):
    """Modify the delivery_carrier for a current tracking record."""

    @staticmethod
    def invoke(data, tracking_id: str = None, courier_id: str = None) -> str:
        if not tracking_id or not courier_id:
            payload = {"error": "tracking_id and courier_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        tr = _find_tracking(data, tracking_id)
        if not tr:
            payload = {"error": f"tracking_id {tracking_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        tr["delivery_carrier"] = courier_id
        payload = {"success": True, "tracking_id": tracking_id, "courier_id": courier_id}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "reassignCourierForTracking",
                "description": "Update delivery_carrier for a tracking record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "courier_id": {"type": "string"},
                    },
                    "required": ["tracking_id", "courier_id"],
                },
            },
        }


class AllocateTrackingId(Tool):
    """Generate a new tracking_id string using courier_id and a seed provided by the caller."""

    @staticmethod
    def invoke(data, courier_id: str = None, seed: int = None) -> str:
        if not courier_id or seed is None:
            payload = {"error": "courier_id and seed are required"}
            out = json.dumps(payload, indent=2)
            return out
        new_id = f"TRK-{courier_id.strip('#')}-{str(seed)}"
        payload = {"tracking_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "allocateTrackingId",
                "description": "Return a tracking id for a courier based on a numeric/string seed.",
                "parameters": {
                    "type": "object",
                    "properties": {"courier_id": {"type": "string"}, "seed": {}},
                    "required": ["courier_id", "seed"],
                },
            },
        }


class ScheduleDelivery(Tool):
    """Establish a 'scheduled' timestamp in tracking_history."""

    @staticmethod
    def invoke(data, tracking_id: str = None, scheduled: str = None) -> str:
        if not tracking_id or not scheduled:
            payload = {"error": "tracking_id and scheduled (ISO string) are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        tr = _find_tracking(data, tracking_id)
        if not tr:
            payload = {"error": f"tracking_id {tracking_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        hist = tr.setdefault("tracking_history", {})
        hist["scheduled"] = scheduled
        payload = {"success": True, "tracking_id": tracking_id, "scheduled": scheduled}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "scheduleDelivery",
                "description": "Set scheduled timestamp for a tracking record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "scheduled": {"type": "string"},
                    },
                    "required": ["tracking_id", "scheduled"],
                },
            },
        }


class FraudMarkOrder(Tool):
    """Link a fraud_check dictionary to an order."""

    @staticmethod
    def invoke(data, order_id: str = None, risk_level: str = None, reason_code: str = None) -> str:
        if not order_id or not risk_level or not reason_code:
            payload = {"error": "order_id, risk_level, reason_code are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        o["fraud_check"] = {"risk_level": risk_level, "reason_code": reason_code}
        payload = {"success": True, "order_id": order_id, "risk_level": risk_level}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "fraudMarkOrder",
                "description": "Mark an order with fraud_check metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "risk_level": {"type": "string"},
                        "reason_code": {"type": "string"},
                    },
                    "required": ["order_id", "risk_level", "reason_code"],
                },
            },
        }


class ComputeUserFillRate(Tool):
    """Calculate a basic fill rate for a user's orders: delivered_items divided by total_items across all orders."""

    @staticmethod
    def invoke(data, user_id: str = None) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        user_orders = [o for o in data.get("orders", []) if o.get("user_id") == user_id]
        total = sum(len(o.get("items", [])) for o in user_orders)
        delivered = 0
        for o in user_orders:
            #tally items in fulfillments that tracking indicates as delivered
            for f in o.get("fulfillments", []):
                for tid in f.get("tracking_id", []):
                    tr = _find_tracking(data, tid)
                    if tr and tr.get("tracking_history", {}).get("delivered"):
                        delivered += len(f.get("item_ids", []))
        rate = (delivered / total) if total else 0.0
        payload = {"user_id": user_id, "fill_rate": round(rate, 4)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "computeUserFillRate",
                "description": "Compute delivered item share across a user's orders.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class UpsertTrackingAddress(Tool):
    """Modify the address in a tracking record."""

    @staticmethod
    def invoke(data, tracking_id=None, address=None) -> str:
        if not tracking_id or not isinstance(address, dict):
            payload = {"error": "tracking_id and address (object) are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        tr = _find_tracking(data, tracking_id)
        if not tr:
            payload = {"error": f"tracking_id {tracking_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        tr["address"] = address
        payload = {"success": True, "tracking_id": tracking_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "upsertTrackingAddress",
                "description": "Replace address on a tracking record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "address": {"type": "object"},
                    },
                    "required": ["tracking_id", "address"],
                },
            },
        }


#Export instances of tools
TOOLS = [
    GetUserById(),
    FindUsersByCity(),
    UpdateUserAddress(),
    AddPaymentMethod(),
    GetProductById(),
    GetItemVariant(),
    SetVariantAvailability(),
    SetVariantPrice(),
    SearchProductsByName(),
    GetOrderDetails(),
    UpdateOrderStatus(),
    AddOrderPayment(),
    RefundOrderPayment(),
    CancelOrderItems(),
    UpdateItemOption(),
    AddOrderTag(),
    ComputeOrderTotal(),
    GetTrackingInfo(),
    AppendTrackingEvent(),
    LinkTrackingToOrder(),
    SplitOrderFulfillment(),
    GetSupplierDetails(),
    PlaceSupplyOrder(),
    UpdateSupplyOrderStatus(),
    GetCourierDetails(),
    ReassignCourierForTracking(),
    AllocateTrackingId(),
    ScheduleDelivery(),
    FraudMarkOrder(),
    ComputeUserFillRate(),
    UpsertTrackingAddress(),
]
