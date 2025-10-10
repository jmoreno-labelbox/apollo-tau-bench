import json
import os
from datetime import datetime
from typing import Any, Dict, List, Optional

from domains.dto import Tool

DATA_DIR = os.path.join(os.path.dirname(__file__), "../../data")


def _adjust_stock(data: Dict[str, Any], product_id: str, item_id: str, quantity_change: int):
    products = data.get("products", [])
    for p in products:
        if p.get("product_id") == product_id:
            variant = (p.get("variants") or {}).get(item_id)
            if variant:
                stock_info = variant.get("stock", {})
                current_stock = stock_info.get("quantity", 0)
                stock_info["quantity"] = current_stock + quantity_change
                variant["stock"] = stock_info
                break


def _recalculate_financials(order: Dict[str, Any]):
    """Recalculates financial totals for an order based on its items."""
    items_total = sum(item.get("price", 0) for item in order.get("items", []))
    # Ensure floating point precision issues are handled
    order["items_total"] = round(items_total, 2)

    # Update the first payment in the history to reflect the new total
    if order.get("payment_history"):
        order["payment_history"][0]["amount"] = order["items_total"]


def _now_iso() -> str:
    """Return current UTC timestamp in ISO format (seconds precision)."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


def _gen_supply_order_id(seed: Optional[int] = None) -> str:
    """
    Generate a synthetic supply order identifier (#SOxxxx) for simulations.
    """
    base = seed if isinstance(seed, int) else int(datetime.utcnow().timestamp())
    return f"#SO{base % 10_000:04d}"


def _gen_order_id(seed: Optional[int] = None) -> str:
    """
    Generate a synthetic order identifier matching dataset flavor.

    Note: Collisions are unlikely but not impossible; this is OK for simulation.
    """
    base = seed if isinstance(seed, int) else int(datetime.utcnow().timestamp())
    return f"#W{base % 10_000_000:07d}"


class CreateOrderTool(Tool):
    """
    Create a new retail order by resolving variants from products.json and
    using the customer's default address from users.json (unless overridden).

    Behavior:
    - Validates that user exists (users.json).
    - Validates items: each must include product_id, item_id, optional quantity>=1.
    - Resolves each (product_id, item_id) in products.json; expands by quantity.
    - Appends a new order entry in orders.json:
        {
          "order_id": "#Wxxxxxxx",
          "user_id": "...",
          "address": {...},              # from users.json or override
          "items": [resolved variants],  # one entry per unit
          "fulfillments": [],
          "status": "pending",
          "payment_history": [],
          "timestamp": "UTC ISO"
        }

    Input (kwargs):
        user_id (str, required)
        items (List[dict], required) -> {product_id, item_id, quantity?}
        address_override (dict, optional)

    Output:
        JSON string with {"message","order_id","status","items_count"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        items_spec = kwargs.get("items")

        if not supplier_id or not isinstance(items_spec, list) or not items_spec:
            return json.dumps({"error": "supplier_id and non-empty items are required"}, indent=2)

        suppliers = data.get("suppliers", [])
        if not any(s.get("supplier_id") == supplier_id for s in suppliers):
            return json.dumps(
                {"error": f"supplier_id '{supplier_id}' not found in suppliers"},
                indent=2,
            )

        resolved_items: List[Dict[str, Any]] = []
        products = data.get("products", [])
        for line in items_spec:
            pid = line.get("product_id")
            iid = line.get("item_id")
            qty = int(line.get("quantity", 1) or 1)
            if not pid or not iid or qty < 1:
                return json.dumps(
                    {"error": "Each item must include product_id, item_id, and quantity>=1"},
                    indent=2,
                )
            variant = None
            for p in products:
                if p.get("product_id") == pid:
                    variant_data = (p.get("variants") or {}).get(iid)
                    if variant_data:
                        variant = {
                            "name": p.get("name"),
                            "product_id": pid,
                            "item_id": iid,
                            "price": variant_data.get("price"),
                            "options": variant_data.get("options", {}),
                        }
                        break
            if not variant:
                return json.dumps(
                    {"error": f"Variant not found for product_id='{pid}', item_id='{iid}'"},
                    indent=2,
                )
            enriched = dict(variant)
            enriched["quantity"] = qty
            resolved_items.append(enriched)

        supply_orders = data.setdefault("supply_orders", [])
        new_so = {
            "supply_order_id": _gen_supply_order_id(),
            "supplier_id": supplier_id,
            "status": "pending",
            "items": resolved_items,
            "created_at": _now_iso(),
            "events": [],
        }
        supply_orders.append(new_so)

        return json.dumps(
            {
                "message": "supply_order_created",
                "supply_order_id": new_so["supply_order_id"],
                "items_count": len(resolved_items),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order",
                "description": "Create a new retail order by resolving product variants and writing into orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Existing user_id from users.json.",
                        },
                        "items": {
                            "type": "array",
                            "description": "Lines to add; each line expands by quantity into separate items.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "item_id": {"type": "string"},
                                    "quantity": {
                                        "type": "integer",
                                        "minimum": 1,
                                        "default": 1,
                                    },
                                },
                                "required": ["product_id", "item_id"],
                            },
                        },
                        "address_override": {
                            "type": "object",
                            "description": "Optional address that replaces the user's default.",
                            "properties": {
                                "address1": {"type": "string"},
                                "address2": {"type": "string"},
                                "city": {"type": "string"},
                                "country": {"type": "string"},
                                "state": {"type": "string"},
                                "zip": {"type": "string"},
                            },
                        },
                    },
                    "required": ["user_id", "items"],
                },
            },
        }


class AppendPaymentTool(Tool):
    """
    Append a payment or refund entry to an order's payment_history in orders.json.

    Behavior:
    - Validates the target order exists.
    - Appends an entry with fields:
        {
          "transaction_type": "payment" | "refund",
          "amount": float,
          "payment_method_id": str,
          "timestamp": "UTC ISO"
        }
    - No automatic reconciliation is performed; caller controls amounts.

    Input (kwargs):
        order_id (str, required)
        transaction_type (str, required: "payment" or "refund")
        amount (float, required, >0)
        payment_method_id (str, required)

    Output:
        JSON string with {"order_id","payment_history_len"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        txn_type = kwargs.get("transaction_type")
        amount = kwargs.get("amount")
        pm_id = kwargs.get("payment_method_id")

        if (
            not order_id
            or txn_type not in {"payment", "refund"}
            or not isinstance(amount, (int, float))
            or amount <= 0
            or not pm_id
        ):
            return json.dumps(
                {
                    "error": "order_id, transaction_type('payment'|'refund'), positive amount, payment_method_id required"
                },
                indent=2,
            )

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        entry = {
            "transaction_type": txn_type,
            "amount": float(amount),
            "payment_method_id": pm_id,
            "timestamp": _now_iso(),
        }
        (order.setdefault("payment_history", [])).append(entry)

        return json.dumps(
            {
                "order_id": order_id,
                "payment_history_len": len(order["payment_history"]),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_payment",
                "description": "Append a payment or refund entry to an order's payment_history in orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "transaction_type": {
                            "type": "string",
                            "enum": ["payment", "refund"],
                        },
                        "amount": {"type": "number", "minimum": 0},
                        "payment_method_id": {"type": "string"},
                    },
                    "required": [
                        "order_id",
                        "transaction_type",
                        "amount",
                        "payment_method_id",
                    ],
                },
            },
        }


class AssignCourierAndCreateTrackingTool(Tool):
    """
    Assign a courier to an order and create a tracking entry in tracking.json.

    Behavior:
    - Reads the order (orders.json) and user's country (users.json) to choose a courier from couriers.json.
    - Picks the first unused tracking_id from the chosen courier's tracking_ids.
    - Writes a new entry to tracking.json:
        {
          "tracking_id": [ "<id>" ],
          "order_id": "...",
          "courier_name": "...",
          "status_history": [{ "status": "label_created", "timestamp": "UTC ISO" }]
        }
    - Also appends a fulfillment snippet to the order in orders.json:
        {
          "status": "label_created",
          "tracking_id": "<id>",
          "courier": "<courier_name>",
          "timestamp": "UTC ISO"
        }

    Input (kwargs):
        order_id (str, required)

    Output:
        JSON string with {"order_id","tracking_id","courier_name"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        if not order_id:
            return json.dumps({"error": "order_id is required"}, indent=2)

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == order.get("user_id")), None)
        if not user:
            return json.dumps({"error": f"user '{order.get('user_id')}' not found"}, indent=2)

        country = ((user.get("address") or {}).get("country")) or "USA"
        couriers = data.get("couriers", [])
        courier = next(
            (c for c in couriers if country in (c.get("coverage_area") or [])),
            couriers[0] if couriers else None,
        )
        if not courier:
            return json.dumps({"error": f"No courier covers '{country}'"}, indent=2)

        used = {tid for t in data.get("tracking", []) for tid in t.get("tracking_id", [])}
        tid = next((tid for tid in courier.get("tracking_ids", []) if tid not in used), None)
        if not tid:
            return json.dumps(
                {"error": f"No available tracking_id for courier '{courier.get('name')}'"}, indent=2
            )

        data.setdefault("tracking", []).append(
            {
                "tracking_id": [tid],
                "order_id": order_id,
                "courier_name": courier.get("name"),
                "status_history": [{"status": "label_created", "timestamp": _now_iso()}],
            }
        )

        order.setdefault("fulfillments", []).append(
            {
                "status": "label_created",
                "tracking_id": tid,
                "courier": courier.get("name"),
                "timestamp": _now_iso(),
            }
        )

        return json.dumps(
            {
                "order_id": order_id,
                "tracking_id": tid,
                "courier_name": courier.get("name"),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_courier_and_create_tracking",
                "description": "Assign a courier based on user's country and create a new tracking record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Target order_id in orders.json.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }


class AdvanceTrackingStatusTool(Tool):
    """
    Advance tracking status for an order in tracking.json and mirror the change to orders.json.

    Behavior:
    - Validates that the given tracking_id exists in tracking.json.
    - Appends a new status entry into status_history.
    - If provided with order_status, also appends a fulfillment update on the order.
      Suggested status flow: label_created -> shipped -> in_transit -> out_for_delivery -> delivered.
    - If status == "delivered", optionally mark order.status = "completed".

    Input (kwargs):
        tracking_id (str, required)
        status (str, required)              # e.g., "shipped", "delivered", etc.
        order_status (str, optional)        # e.g., "fulfilled", "completed"

    Output:
        JSON string with {"tracking_id","new_status","history_len"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tracking_id = kwargs.get("tracking_id")
        status = kwargs.get("status")
        order_status = kwargs.get("order_status")

        if not tracking_id or not status:
            return json.dumps({"error": "tracking_id and status are required"}, indent=2)

        tracking = data.get("tracking", [])
        tr = next((t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None)
        if not tr:
            return json.dumps(
                {"error": f"tracking_id '{tracking_id}' not found in tracking.json"},
                indent=2,
            )

        # Ensure tracking_history exists before appending
        if "tracking_history" not in tr:
            tr["tracking_history"] = {}

        tr["tracking_history"][status] = _now_iso()

        # Mirror into orders.json if applicable
        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == tr.get("order_id")), None)
        if order:
            if "fulfillments" not in order:
                order["fulfillments"] = []

            order["fulfillments"].append(
                {
                    "status": status,
                    "tracking_id": tracking_id,
                    "timestamp": _now_iso(),
                }
            )
            if status == "delivered":
                order["status"] = "completed"
            if order_status:
                order["status"] = order_status

        return json.dumps(
            {
                "tracking_id": tracking_id,
                "new_status": status,
                "history_len": len(tr["tracking_history"]),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "advance_tracking_status",
                "description": "Append a new tracking status and optionally update the order status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "status": {"type": "string"},
                        "order_status": {
                            "type": "string",
                            "description": "Optional order status to set.",
                        },
                    },
                    "required": ["tracking_id", "status"],
                },
            },
        }


class CancelOrderAndRefundTool(Tool):
    """
    Cancel an order and optionally create an automatic refund entry.

    Behavior:
    - Validates the order exists and is not already completed/cancelled.
    - Sets order.status = "cancelled".
    - If refund_amount > 0, appends a refund entry to payment_history.
    - Does NOT touch tracking.json; callers should handle carrier processes separately.

    Input (kwargs):
        order_id (str, required)
        refund_amount (float, optional, default=0)
        payment_method_id (str, optional, required if refund_amount > 0)

    Output:
        JSON string with {"order_id","status","refund_created":bool} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        refund_amount = float(kwargs.get("refund_amount", 0) or 0)
        payment_method_id = kwargs.get("payment_method_id")

        if not order_id:
            return json.dumps({"error": "order_id is required"}, indent=2)
        if refund_amount > 0 and not payment_method_id:
            return json.dumps(
                {"error": "payment_method_id is required when refund_amount > 0"},
                indent=2,
            )

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        if order.get("status") in {"completed", "cancelled"}:
            return json.dumps({"error": f"order already {order.get('status')}"}, indent=2)

        items_to_return = order.get("items", [])

        order["status"] = "cancelled"

        for item in items_to_return:
            product_id = item.get("product_id")
            item_id = item.get("item_id")
            if product_id and item_id:
                _adjust_stock(data, product_id, item_id, 1)

        refund_created = False
        if refund_amount > 0:
            (order.setdefault("payment_history", [])).append(
                {
                    "transaction_type": "refund",
                    "amount": refund_amount,
                    "payment_method_id": payment_method_id,
                    "timestamp": _now_iso(),
                }
            )
            refund_created = True

        return json.dumps(
            {
                "order_id": order_id,
                "status": "cancelled",
                "refund_created": refund_created,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_order_and_refund",
                "description": "Cancel an existing order and optionally append a refund entry in orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "refund_amount": {"type": "number", "minimum": 0, "default": 0},
                        "payment_method_id": {
                            "type": "string",
                            "description": "Required when refund_amount > 0",
                        },
                    },
                    "required": ["order_id"],
                },
            },
        }


class AddItemsToOrderTool(Tool):
    """
    Add one or more items to an existing order by resolving variants from products.json.

    Behavior:
    - Validates the order exists.
    - For each {product_id, item_id, quantity}, resolves the variant from products.json.
    - Appends one entry per unit to order["items"] (consistent with dataset structure).
    - Does not recalculate totals; this tool only amends the item list.

    Input (kwargs):
        order_id (str, required)
        items (List[dict], required) -> {product_id, item_id, quantity?}

    Output:
        JSON string with {"order_id","added_count","items_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        items_spec = kwargs.get("items")

        if not order_id or not isinstance(items_spec, list) or not items_spec:
            return json.dumps({"error": "order_id and non-empty items are required"}, indent=2)

        orders = data.get("orders", [])
        products = data.get("products", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)

        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        added = 0
        for line in items_spec:
            pid = line.get("product_id")
            iid = line.get("item_id")
            qty = int(line.get("quantity", 1) or 1)

            if not pid or not iid or qty < 1:
                return json.dumps(
                    {"error": "Each item must include product_id, item_id, and quantity>=1"},
                    indent=2,
                )

            product = next((p for p in products if p.get("product_id") == pid), None)
            variant = (product.get("variants") or {}).get(iid) if product else None

            if not variant:
                return json.dumps(
                    {"error": f"Variant not found for product_id='{pid}', item_id='{iid}'"},
                    indent=2,
                )

            resolved_item = {
                "name": product.get("name"),
                "product_id": pid,
                "item_id": iid,
                "price": variant.get("price"),
                "options": variant.get("options", {}),
            }

            for _ in range(qty):
                (order.setdefault("items", [])).append(resolved_item)
                added += 1

            _adjust_stock(data, pid, iid, -qty)

        return json.dumps(
            {
                "order_id": order_id,
                "added_count": added,
                "items_len": len(order.get("items", [])),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_items_to_order",
                "description": "Add one or more resolved product variants into an existing order (orders.json).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "item_id": {"type": "string"},
                                    "quantity": {
                                        "type": "integer",
                                        "minimum": 1,
                                        "default": 1,
                                    },
                                },
                                "required": ["product_id", "item_id"],
                            },
                        },
                    },
                    "required": ["order_id", "items"],
                },
            },
        }


class RemoveItemsByIndexTool(Tool):
    """
    Remove items from an order by index positions within order['items'].

    Behavior:
    - Validates the order exists and 'indices' is a list of distinct integers.
    - Removes items at the provided indices (0-based) present in the current list.
    - Ignores out-of-range indices silently to be robust.

    Input (kwargs):
        order_id (str, required)
        indices (List[int], required)

    Output:
        JSON string with {"order_id","removed_count","items_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        indices = kwargs.get("indices")

        if not order_id or not isinstance(indices, list) or not indices:
            return json.dumps({"error": "order_id and non-empty indices are required"}, indent=2)

        try:
            idxs = sorted({int(i) for i in indices if int(i) >= 0}, reverse=True)
        except Exception:
            return json.dumps({"error": "indices must be a list of integers >= 0"}, indent=2)

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        items = order.get("items", [])
        removed_count = 0
        for i in idxs:
            if 0 <= i < len(items):
                removed_item = items.pop(i)

                product_id = removed_item.get("product_id")
                item_id = removed_item.get("item_id")

                if product_id and item_id:
                    _adjust_stock(data, product_id, item_id, 1)

                removed_count += 1

        order["items"] = items
        return json.dumps(
            {"order_id": order_id, "removed_count": removed_count, "items_len": len(items)},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_items_by_index",
                "description": "Remove items from an order by zero-based indices within order['items'].",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "indices": {
                            "type": "array",
                            "items": {"type": "integer", "minimum": 0},
                        },
                    },
                    "required": ["order_id", "indices"],
                },
            },
        }


class SetOrderStatusTool(Tool):
    """
    Set or override an order's status in orders.json.

    Behavior:
    - Validates the order exists.
    - Sets order['status'] = provided value.
    - Does not modify fulfillments or payment_history.

    Input (kwargs):
        order_id (str, required)
        status (str, required)  # e.g., "pending", "fulfilled", "completed", "cancelled"

    Output:
        JSON string with {"order_id","status"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        status = kwargs.get("status")

        if not order_id or not isinstance(status, str) or not status:
            return json.dumps({"error": "order_id and non-empty status are required"}, indent=2)

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        order["status"] = status
        return json.dumps({"order_id": order_id, "status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_order_status",
                "description": "Set or override the 'status' field of an existing order (orders.json).",
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


class LinkExistingTrackingToOrderTool(Tool):
    """
    Link an existing tracking record to an order by creating a fulfillment entry.

    Behavior:
    - Validates the order exists.
    - Validates that the tracking_id exists in tracking.json (under any record's 'tracking_id' list).
    - Appends a fulfillment entry on the order containing at least:
        { "status": "linked", "tracking_id": "<id>", "timestamp": "UTC ISO" }
      Optionally includes 'courier' if found on the tracking record.

    Input (kwargs):
        order_id (str, required)
        tracking_id (str, required)

    Output:
        JSON string with {"order_id","tracking_id","fulfillments_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        tracking_id = kwargs.get("tracking_id")

        if not order_id or not tracking_id:
            return json.dumps({"error": "order_id and tracking_id are required"}, indent=2)

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        tracking = data.get("tracking", [])
        tr = next((t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None)
        if not tr:
            return json.dumps({"error": f"tracking_id '{tracking_id}' not found"}, indent=2)

        fulfillment = {
            "status": "linked",
            "tracking_id": tracking_id,
            "timestamp": _now_iso(),
        }
        if tr.get("courier_name"):
            fulfillment["courier"] = tr["courier_name"]

        order.setdefault("fulfillments", []).append(fulfillment)

        return json.dumps(
            {
                "order_id": order_id,
                "tracking_id": tracking_id,
                "fulfillments_len": len(order.get("fulfillments", [])),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_existing_tracking_to_order",
                "description": "Link an existing tracking_id from tracking.json to an order by appending a fulfillment entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "tracking_id": {"type": "string"},
                    },
                    "required": ["order_id", "tracking_id"],
                },
            },
        }


class CreateSupplyOrderTool(Tool):
    """
    Create a new supply order in supply_orders.json for restocking purposes.

    Behavior:
    - Accepts a supplier_id and a list of items {product_id, item_id, quantity}.
    - Resolves each variant from products.json to carry forward name/price/options.
    - Writes a new entry to supply_orders.json with:
        {
          "supply_order_id": "#SOxxxx",
          "supplier_id": "...",
          "status": "pending",
          "items": [ {variant..., "quantity": int} ],
          "created_at": "UTC ISO",
          "events": []
        }

    Input (kwargs):
        supplier_id (str, required)
        items (List[dict], required) -> {product_id, item_id, quantity>=1}

    Output:
        JSON string with {"message","supply_order_id","items_count"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        items_spec = kwargs.get("items")

        if not supplier_id or not isinstance(items_spec, list) or not items_spec:
            return json.dumps({"error": "supplier_id and non-empty items are required"}, indent=2)

        suppliers = data.get("suppliers", [])
        if not any(s.get("supplier_id") == supplier_id for s in suppliers):
            return json.dumps(
                {"error": f"supplier_id '{supplier_id}' not found in suppliers"},
                indent=2,
            )

        products = data.get("products", [])
        resolved_items: List[Dict[str, Any]] = []

        for line in items_spec:
            pid = line.get("product_id")
            iid = line.get("item_id")
            qty = int(line.get("quantity", 1) or 1)
            if not pid or not iid or qty < 1:
                return json.dumps(
                    {"error": "Each item must include product_id, item_id, and quantity>=1"},
                    indent=2,
                )

            variant = None
            for p in products:
                if p.get("product_id") == pid:
                    variant_data = (p.get("variants") or {}).get(iid)
                    if variant_data:
                        variant = {
                            "name": p.get("name"),
                            "product_id": pid,
                            "item_id": iid,
                            "price": variant_data.get("price"),
                            "options": variant_data.get("options", {}),
                        }
                        break

            if not variant:
                return json.dumps(
                    {"error": f"Variant not found for product_id='{pid}', item_id='{iid}'"},
                    indent=2,
                )

            enriched = dict(variant)
            enriched["quantity"] = qty
            resolved_items.append(enriched)

        supply_orders = data.setdefault("supply_orders", [])
        new_so = {
            "supply_order_id": _gen_supply_order_id(),
            "supplier_id": supplier_id,
            "status": "pending",
            "items": resolved_items,
            "created_at": _now_iso(),
            "events": [],
        }
        supply_orders.append(new_so)

        return json.dumps(
            {
                "message": "supply_order_created",
                "supply_order_id": new_so["supply_order_id"],
                "items_count": len(resolved_items),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_supply_order",
                "description": "Create a new supply order with resolved product variants and write to supply_orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "item_id": {"type": "string"},
                                    "quantity": {
                                        "type": "integer",
                                        "minimum": 1,
                                        "default": 1,
                                    },
                                },
                                "required": ["product_id", "item_id"],
                            },
                        },
                    },
                    "required": ["supplier_id", "items"],
                },
            },
        }


class SetSupplyOrderStatusTool(Tool):
    """
    Set or override the status of a supply order in supply_orders.json.

    Behavior:
    - Validates that the supply_order_id exists.
    - Sets entry['status'] = provided value.
    - If status == "received", sets 'received_at' timestamp (UTC ISO) when not present.

    Input (kwargs):
        supply_order_id (str, required)
        status (str, required)  # e.g., "pending","approved","in_transit","received","cancelled"

    Output:
        JSON string with {"supply_order_id","status"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        so_id = kwargs.get("supply_order_id")
        status = kwargs.get("status")

        if not so_id or not isinstance(status, str) or not status:
            return json.dumps(
                {"error": "supply_order_id and non-empty status are required"}, indent=2
            )

        supply_orders = data.get("supply_orders", [])
        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            return json.dumps({"error": f"supply_order_id '{so_id}' not found"}, indent=2)

        so["status"] = status
        if status == "received" and not so.get("received_at"):
            so["received_at"] = _now_iso()

        return json.dumps({"supply_order_id": so_id, "status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_supply_order_status",
                "description": "Set or override the 'status' of an existing supply order (supply_orders.json).",
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


class AppendSupplyOrderEventTool(Tool):
    """
    Append an event note to a supply order's 'events' list in supply_orders.json.

    Behavior:
    - Validates that the supply_order_id exists.
    - Appends an event object:
        {
          "type": "<string>",
          "message": "<string>",
          "timestamp": "UTC ISO"
        }
    - Creates the 'events' list if it does not exist.

    Input (kwargs):
        supply_order_id (str, required)
        event_type (str, required)
        message (str, required)

    Output:
        JSON string with {"supply_order_id","events_len"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        so_id = kwargs.get("supply_order_id")
        event_type = kwargs.get("event_type")
        message = kwargs.get("message")

        if not so_id or not event_type or not message:
            return json.dumps(
                {"error": "supply_order_id, event_type, and message are required"},
                indent=2,
            )

        supply_orders = data.get("supply_orders", [])
        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            return json.dumps({"error": f"supply_order_id '{so_id}' not found"}, indent=2)

        event = {
            "type": str(event_type),
            "message": str(message),
            "timestamp": _now_iso(),
        }
        so.setdefault("events", []).append(event)

        return json.dumps(
            {"supply_order_id": so_id, "events_len": len(so.get("events", []))},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_supply_order_event",
                "description": "Append a typed event with message to a supply order's events array (supply_orders.json).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["supply_order_id", "event_type", "message"],
                },
            },
        }


class GetOrderFinancialsTool(Tool):
    """Gets financial data for an order from the shared in-memory state."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        # Reads the 'orders' object from the in-memory state, which may have been modified.
        orders = data.get("orders", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps(
                {"error": f"Order '{order_id}' not found in the current state"}, indent=2
            )

        # This will now reflect any changes made by previous tools
        return json.dumps(
            {"order_id": order_id, "items_total": order.get("items_total", 0)}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_financials",
                "description": "Retrieves financial totals for a given order from the current state.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class FindOrdersByUserAndStatusTool(Tool):
    """
    Find orders filtered by user_id and optional status.

    Behavior:
    - If status is provided, filters orders with exact match.
    - Returns a compact listing: order_id, status, items_len, timestamp.

    Input (kwargs):
        user_id (str, required)
        status (str, optional)

    Output:
        JSON string with {"user_id","count","orders":[...]} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        status = kwargs.get("status")

        if not user_id:
            return json.dumps({"error": "user_id is required"}, indent=2)

        orders = data.get("orders", [])
        filtered = []
        for o in orders:
            if o.get("user_id") != user_id:
                continue
            if status and o.get("status") != status:
                continue
            filtered.append(
                {
                    "order_id": o.get("order_id"),
                    "status": o.get("status"),
                    "items_len": len(o.get("items", [])),
                    "timestamp": o.get("timestamp"),
                }
            )

        return json.dumps(
            {"user_id": user_id, "count": len(filtered), "orders": filtered}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_orders_by_user_and_status",
                "description": "Return orders for a given user_id, optionally filtered by status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["user_id"],
                },
            },
        }


class AttachCourierByNameTool(Tool):
    """
    Attach a specific courier (by name) to an order and create a tracking entry.

    Behavior:
    - Validates order exists (orders.json).
    - Validates courier exists (couriers.json).
    - Picks first unused tracking_id from the courier.
    - Writes a new record to tracking.json and appends a fulfillment entry to the order.

    Input (kwargs):
        order_id (str, required)
        courier_name (str, required)

    Output:
        JSON string with {"order_id","tracking_id","courier_name"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        courier_name = kwargs.get("courier_name")

        if not order_id or not courier_name:
            return json.dumps({"error": "order_id and courier_name are required"}, indent=2)

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        couriers = data.get("couriers", [])
        courier = next((c for c in couriers if c.get("name") == courier_name), None)
        if not courier:
            return json.dumps({"error": f"courier '{courier_name}' not found"}, indent=2)

        used_ids = {tid for t in data.get("tracking", []) for tid in t.get("tracking_id", [])}
        candidate_ids = courier.get("tracking_ids", [])
        tid = next((tid for tid in candidate_ids if tid not in used_ids), None)

        if not tid:
            return json.dumps(
                {"error": f"No available tracking_id for courier '{courier_name}'"},
                indent=2,
            )

        tracking = data.setdefault("tracking", [])
        tracking.append(
            {
                "tracking_id": [tid],
                "order_id": order_id,
                "courier_name": courier_name,
                "status_history": [{"status": "label_created", "timestamp": _now_iso()}],
            }
        )

        order.setdefault("fulfillments", []).append(
            {
                "status": "label_created",
                "tracking_id": tid,
                "courier": courier_name,
                "timestamp": _now_iso(),
            }
        )

        return json.dumps(
            {"order_id": order_id, "tracking_id": tid, "courier_name": courier_name},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "attach_courier_by_name",
                "description": "Attach a specific courier by name to an order and create a new tracking record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "courier_name": {"type": "string"},
                        "tracking_id": {"type": "string"},
                    },
                    "required": ["order_id", "courier_name", "tracking_id"],
                },
            },
        }


class UpdateTrackingCourierTool(Tool):
    """
    Update the courier_name of an existing tracking record in tracking.json.

    Behavior:
    - Validates tracking_id exists in tracking.json (present inside each record's tracking_id list).
    - Overwrites 'courier_name' with the provided value.
    - Appends a status_history note 'courier_updated'.

    Input (kwargs):
        tracking_id (str, required)
        courier_name (str, required)

    Output:
        JSON string with {"tracking_id","courier_name"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tracking_id = kwargs.get("tracking_id")
        courier_name = kwargs.get("courier_name")

        if not tracking_id or not courier_name:
            return json.dumps({"error": "tracking_id and courier_name are required"}, indent=2)

        tracking = data.get("tracking", [])
        rec = next((t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None)
        if not rec:
            return json.dumps(
                {"error": f"tracking_id '{tracking_id}' not found in tracking records"},
                indent=2,
            )

        rec["courier_name"] = courier_name
        rec.setdefault("status_history", []).append(
            {"status": "courier_updated", "timestamp": _now_iso()}
        )

        return json.dumps(
            {"tracking_id": tracking_id, "courier_name": courier_name},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_tracking_courier",
                "description": "Update the courier_name field for an existing tracking record (tracking.json).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "courier_name": {"type": "string"},
                    },
                    "required": ["tracking_id", "courier_name"],
                },
            },
        }


class AddTrackingCustomEventTool(Tool):
    """
    Append a custom event to the status_history of a tracking record.

    Behavior:
    - Validates tracking_id exists in tracking.json.
    - Appends {"status": <event_status>, "timestamp": UTC ISO, "note": <optional str>}.
    - Does not modify orders.json (pure tracking enrichment).

    Input (kwargs):
        tracking_id (str, required)
        event_status (str, required)   # e.g., "in_transit", "delayed", "checkpoint"
        note (str, optional)

    Output:
        JSON string with {"tracking_id","new_status","history_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tracking_id = kwargs.get("tracking_id")
        event_status = kwargs.get("event_status")
        note = kwargs.get("note")

        if not tracking_id or not event_status:
            return json.dumps({"error": "tracking_id and event_status are required"}, indent=2)

        tracking = data.get("tracking", [])
        rec = next((t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None)
        if not rec:
            return json.dumps(
                {"error": f"tracking_id '{tracking_id}' not found in tracking records"},
                indent=2,
            )

        event = {"status": str(event_status), "timestamp": _now_iso()}
        if note:
            event["note"] = str(note)

        rec.setdefault("status_history", []).append(event)

        return json.dumps(
            {
                "tracking_id": tracking_id,
                "new_status": event_status,
                "history_len": len(rec.get("status_history", [])),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_tracking_custom_event",
                "description": "Append a custom status event (with optional note) to a tracking record's status_history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "event_status": {"type": "string"},
                        "note": {"type": "string"},
                    },
                    "required": ["tracking_id", "event_status"],
                },
            },
        }


class FindTrackingByOrderTool(Tool):
    """Finds tracking data for an order from the shared in-memory state."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        # Reads the tracking data from the in-memory state.
        tracking_data = data.get("tracking", [])

        tr = next((t for t in tracking_data if t.get("order_id") == order_id), None)
        if not tr:
            return json.dumps(
                {"error": f"Tracking for order '{order_id}' not found in the current state"},
                indent=2,
            )

        # The 'item_ids' field will now reflect any changes made previously.
        return json.dumps(tr, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_tracking_by_order",
                "description": "Finds the tracking record for a given order_id from the current state.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class FindSupplyOrdersTool(Tool):
    """
    Find supply orders filtered by optional supplier_id and/or status.

    Behavior:
    - If supplier_id is provided, only returns matching records.
    - If status is provided, only returns records with exact status.
    - Returns a compact view: supply_order_id, supplier_id, status, items_count, created_at.

    Input (kwargs):
        supplier_id (str, optional)
        status (str, optional)

    Output:
        JSON string with {"count","supply_orders":[...]}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        status = kwargs.get("status")

        supply_orders = data.get("supply_orders", [])
        filtered = []
        for so in supply_orders:
            if supplier_id and so.get("supplier_id") != supplier_id:
                continue
            if status and so.get("status") != status:
                continue
            filtered.append(
                {
                    "supply_order_id": so.get("supply_order_id"),
                    "supplier_id": so.get("supplier_id"),
                    "status": so.get("status"),
                    "items_count": len(so.get("items", [])),
                    "created_at": so.get("created_at"),
                }
            )

        return json.dumps({"count": len(filtered), "supply_orders": filtered}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_supply_orders",
                "description": "Find supply orders filtered by optional supplier_id and/or status from supply_orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                },
            },
        }


class SplitOrderIntoShipmentsTool(Tool):
    """
    Split an order's items into multiple shipments, creating tracking and fulfillments.

    Behavior:
    - Validates order exists.
    - For each shipment entry, requires 'indices' (0-based positions in order.items)
      and a 'courier_name' to create a tracking record.
    - Creates one tracking record per shipment and appends corresponding fulfillment
      entries to the order. Items are not removed; this tool only creates logistics records.

    Input (kwargs):
        order_id (str, required)
        shipments (List[dict], required): each with
            - indices: List[int]  # positions within order['items']
            - courier_name: str

    Output:
        JSON string with {"order_id","created_trackings":[{"courier_name","tracking_id","count"}], "shipments_count"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        shipments = kwargs.get("shipments")

        if not order_id or not isinstance(shipments, list) or not shipments:
            return json.dumps({"error": "order_id and non-empty shipments are required"}, indent=2)

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        couriers = data.get("couriers", [])
        tracking_db = data.get("tracking", [])
        items_len = len(order.get("items", []))
        created = []

        used_tracking_ids = {tid for t in tracking_db for tid in t.get("tracking_id", [])}

        for sh in shipments:
            idxs = sh.get("indices")
            courier_name = sh.get("courier_name")
            if not isinstance(idxs, list) or not idxs or not courier_name:
                return json.dumps(
                    {"error": "each shipment requires 'indices' (list) and 'courier_name'"},
                    indent=2,
                )

            # validate indices exist within range
            valid = [
                i
                for i in set(int(i) for i in idxs if isinstance(i, (int, float)))
                if 0 <= i < items_len
            ]
            if not valid:
                return json.dumps(
                    {"error": f"shipment has no valid indices within 0..{items_len-1}"},
                    indent=2,
                )

            # find courier
            courier = next((c for c in couriers if c.get("name") == courier_name), None)
            if not courier:
                return json.dumps({"error": f"courier '{courier_name}' not found"}, indent=2)

            # pick first unused tracking id
            tid = next(
                (tid for tid in courier.get("tracking_ids", []) if tid not in used_tracking_ids),
                None,
            )
            if not tid:
                return json.dumps(
                    {"error": f"No available tracking_id for courier '{courier_name}'"},
                    indent=2,
                )

            used_tracking_ids.add(tid)

            # create tracking entry
            tracking_db.append(
                {
                    "tracking_id": [tid],
                    "order_id": order_id,
                    "courier_name": courier_name,
                    "status_history": [{"status": "label_created", "timestamp": _now_iso()}],
                }
            )

            # append fulfillment to order
            (order.setdefault("fulfillments", [])).append(
                {
                    "status": "label_created",
                    "tracking_id": tid,
                    "courier": courier_name,
                    "timestamp": _now_iso(),
                    "items_indices": sorted(valid),
                }
            )

            created.append({"courier_name": courier_name, "tracking_id": tid, "count": len(valid)})

        return json.dumps(
            {
                "order_id": order_id,
                "created_trackings": created,
                "shipments_count": len(created),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "split_order_into_shipments",
                "description": "Create multiple shipments for an order by indices and courier, generating tracking and fulfillment entries.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "shipments": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "indices": {
                                        "type": "array",
                                        "items": {"type": "integer", "minimum": 0},
                                    },
                                    "courier_name": {"type": "string"},
                                },
                                "required": ["indices", "courier_name"],
                            },
                        },
                    },
                    "required": ["order_id", "shipments"],
                },
            },
        }


class MergeOrdersForSameUserTool(Tool):
    """
    Merge items from a source order into a target order when both belong to the same user.

    Behavior:
    - Validates both orders exist and belong to the same user_id.
    - Appends all items from source into target's 'items'.
    - Optionally moves payment_history too (flag include_payments).
    - Sets source order status to "cancelled" after merge.
    - Does not merge fulfillments; logistics remain bound to the original order_id.

    Input (kwargs):
        target_order_id (str, required)
        source_order_id (str, required)
        include_payments (bool, optional, default=False)

    Output:
        JSON string with {"target_order_id","source_order_id","moved_items","target_items_len","source_status"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target_id = kwargs.get("target_order_id")
        source_id = kwargs.get("source_order_id")
        include_payments = bool(kwargs.get("include_payments", False))

        if not target_id or not source_id or target_id == source_id:
            return json.dumps(
                {"error": "target_order_id and source_order_id must be provided and different"},
                indent=2,
            )

        orders = data.get("orders", [])
        target = next((o for o in orders if o.get("order_id") == target_id), None)
        source = next((o for o in orders if o.get("order_id") == source_id), None)
        if not target or not source:
            return json.dumps({"error": "target or source order not found"}, indent=2)

        if target.get("user_id") != source.get("user_id"):
            return json.dumps({"error": "orders belong to different users"}, indent=2)

        moved_items = len(source.get("items", []))
        (target.setdefault("items", [])).extend(source.get("items", []))

        if include_payments and source.get("payment_history"):
            (target.setdefault("payment_history", [])).extend(source.get("payment_history", []))

        source["status"] = "cancelled"

        return json.dumps(
            {
                "target_order_id": target_id,
                "source_order_id": source_id,
                "moved_items": moved_items,
                "target_items_len": len(target.get("items", [])),
                "source_status": source.get("status"),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "merge_orders_for_same_user",
                "description": "Merge items (and optionally payments) from a source order into a target order for the same user; cancel the source.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_order_id": {"type": "string"},
                        "source_order_id": {"type": "string"},
                        "include_payments": {"type": "boolean", "default": False},
                    },
                    "required": ["target_order_id", "source_order_id"],
                },
            },
        }


class ReopenCancelledOrderTool(Tool):
    """
    Reopen a previously cancelled order by setting status back to 'pending'.

    Behavior:
    - Validates order exists and is currently 'cancelled'.
    - Sets order['status'] = 'pending'.
    - Does not modify items, payment_history, or fulfillments.

    Input (kwargs):
        order_id (str, required)

    Output:
        JSON string with {"order_id","status"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        if not order_id:
            return json.dumps({"error": "order_id is required"}, indent=2)

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        if order.get("status") != "cancelled":
            return json.dumps(
                {"error": f"order status must be 'cancelled', found '{order.get('status')}'"},
                indent=2,
            )

        order["status"] = "pending"

        return json.dumps({"order_id": order_id, "status": "pending"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reopen_cancelled_order",
                "description": "Reopen a cancelled order by setting its status back to 'pending'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                    },
                    "required": ["order_id"],
                },
            },
        }


class ReplaceItemVariantInOrderTool(Tool):
    """
    Replaces an item in an order, recalculates financials, and updates tracking,
    with all changes occurring in the shared in-memory state.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        index = kwargs.get("index")
        product_id = kwargs.get("product_id")
        item_id = kwargs.get("item_id")

        orders = data.get("orders", [])
        products = data.get("products", [])
        tracking_data = data.get("tracking", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"Order '{order_id}' not found"}, indent=2)

        new_variant = None
        for p in products:
            if p.get("product_id") == product_id:
                variant_details = p.get("variants", {}).get(item_id)
                if variant_details:
                    new_variant = {
                        "name": p.get("name"),
                        "product_id": product_id,
                        "item_id": item_id,
                        "price": variant_details.get("price"),
                        "options": variant_details.get("options", {}),
                    }
                    break
        if not new_variant:
            return json.dumps(
                {"error": f"Variant '{item_id}' for product '{product_id}' not found"}, indent=2
            )

        items = order.get("items", [])
        if not 0 <= index < len(items):
            return json.dumps(
                {"error": f"Index {index} is out of bounds for the items in order '{order_id}'"},
                indent=2,
            )

        old_item = items[index]
        old_product_id = old_item.get("product_id")
        old_item_id = old_item.get("item_id")

        items[index] = new_variant

        if old_product_id and old_item_id:
            _adjust_stock(data, old_product_id, old_item_id, 1)

        _adjust_stock(data, product_id, item_id, -1)

        _recalculate_financials(order)

        tr = next((t for t in tracking_data if t.get("order_id") == order_id), None)
        if tr and old_item_id and "item_ids" in tr:
            try:
                id_index = tr["item_ids"].index(old_item_id)
                tr["item_ids"][id_index] = item_id
            except ValueError:
                pass

        return json.dumps(
            {
                "status": "success",
                "message": f"Order {order_id} was successfully modified in memory.",
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "replace_item_variant_in_order",
                "description": "Replaces an item in an order with a new variant and updates financials and tracking in memory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "index": {"type": "integer"},
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                    },
                    "required": ["order_id", "index", "product_id", "item_id"],
                },
            },
        }


class AutoApproveSupplyOrderTool(Tool):
    """
    Automatically approve a pending supply order and register an approval event.

    Behavior:
    - Validates that the supply order exists and is in 'pending' status.
    - Sets status to 'approved'.
    - Appends an event {type: "approved", message: <optional reason>, timestamp: UTC ISO}.

    Input (kwargs):
        supply_order_id (str, required)
        reason (str, optional)

    Output:
        JSON string with {"supply_order_id","status","events_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        so_id = kwargs.get("supply_order_id")
        reason = kwargs.get("reason")

        if not so_id:
            return json.dumps({"error": "supply_order_id is required"}, indent=2)

        supply_orders = data.get("supply_orders", [])
        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            return json.dumps({"error": f"supply_order_id '{so_id}' not found"}, indent=2)

        if so.get("status") != "pending":
            return json.dumps(
                {"error": f"status must be 'pending' to auto-approve (found '{so.get('status')}')"},
                indent=2,
            )

        so["status"] = "approved"
        event = {
            "type": "approved",
            "message": reason or "auto-approved",
            "timestamp": _now_iso(),
        }
        (so.setdefault("events", [])).append(event)

        return json.dumps(
            {
                "supply_order_id": so_id,
                "status": "approved",
                "events_len": len(so.get("events", [])),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "auto_approve_supply_order",
                "description": "Approve a pending supply order and append an 'approved' event to its events array.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": ["supply_order_id"],
                },
            },
        }


class DuplicateOrderTool(Tool):
    """
    Duplicate an existing order into a new one for the same user.

    Behavior:
    - Validates the source order exists.
    - Clones user_id, address, items; resets fulfillments to [] and payment_history to [].
    - Sets status to "pending" and generates a new order_id and timestamp.
    - Appends the new order to orders.json.

    Input (kwargs):
        source_order_id (str, required)

    Output:
        JSON string with {"source_order_id","new_order_id","items_count"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        src_id = kwargs.get("source_order_id")
        if not src_id:
            return json.dumps({"error": "source_order_id is required"}, indent=2)

        orders = data.get("orders", [])
        src = next((o for o in orders if o.get("order_id") == src_id), None)
        if not src:
            return json.dumps({"error": f"source_order_id '{src_id}' not found"}, indent=2)

        new_order = {
            "order_id": _gen_order_id(),
            "user_id": src.get("user_id"),
            "address": src.get("address"),
            "items": list(src.get("items", [])),
            "fulfillments": [],
            "status": "pending",
            "payment_history": [],
            "timestamp": _now_iso(),
        }
        orders.append(new_order)

        return json.dumps(
            {
                "source_order_id": src_id,
                "new_order_id": new_order["order_id"],
                "items_count": len(new_order.get("items", [])),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "duplicate_order",
                "description": "Duplicate an existing order (same user/address/items) with a fresh id, pending status, and no payments/fulfillments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_order_id": {"type": "string"},
                    },
                    "required": ["source_order_id"],
                },
            },
        }


class RemovePaymentByIndexTool(Tool):
    """
    Remove a payment/refund entry from an order's payment_history by index.

    Behavior:
    - Validates the order exists and index is within range.
    - Removes payment_history[index].

    Input (kwargs):
        order_id (str, required)
        index (int, required)   # 0-based

    Output:
        JSON string with {"order_id","removed":true,"payment_history_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        index = kwargs.get("index")

        if not order_id or index is None:
            return json.dumps({"error": "order_id and index are required"}, indent=2)

        try:
            idx = int(index)
        except Exception:
            return json.dumps({"error": "index must be an integer"}, indent=2)

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        history = order.get("payment_history", [])
        if not (0 <= idx < len(history)):
            return json.dumps(
                {"error": f"index out of range 0..{max(0, len(history)-1)}"}, indent=2
            )

        history.pop(idx)
        order["payment_history"] = history

        return json.dumps(
            {
                "order_id": order_id,
                "removed": True,
                "payment_history_len": len(history),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_payment_by_index",
                "description": "Remove a payment/refund entry at a given index from an order's payment_history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "index": {"type": "integer", "minimum": 0},
                    },
                    "required": ["order_id", "index"],
                },
            },
        }


class AppendAlternateTrackingIdTool(Tool):
    """
    Append an alternate tracking_id to an existing tracking record.

    Behavior:
    - Validates tracking_id exists in tracking data.
    - Reads courier_name from record.
    - Pulls an unused tracking_id from the same courier.
    - Appends the new tracking_id and logs 'alt_tracking_added' in status_history.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        original_tid = kwargs.get("tracking_id")
        if not original_tid:
            return json.dumps({"error": "tracking_id is required"}, indent=2)

        tracking = data.get("tracking", [])
        rec = next((t for t in tracking if original_tid in (t.get("tracking_id") or [])), None)
        if not rec:
            return json.dumps(
                {"error": f"tracking_id '{original_tid}' not found in tracking records"},
                indent=2,
            )

        courier_name = rec.get("courier_name")
        if not courier_name:
            return json.dumps({"error": "courier_name is missing on the tracking record"}, indent=2)

        couriers = data.get("couriers", [])
        courier = next((c for c in couriers if c.get("name") == courier_name), None)
        if not courier:
            return json.dumps(
                {"error": f"courier '{courier_name}' not found in couriers data"},
                indent=2,
            )

        used_ids = {tid for t in tracking for tid in t.get("tracking_id", [])}
        candidate_ids = courier.get("tracking_ids", [])
        new_tid = next((tid for tid in candidate_ids if tid not in used_ids), None)

        if not new_tid:
            return json.dumps(
                {"error": f"No available tracking_id for courier '{courier_name}'"},
                indent=2,
            )

        rec.setdefault("tracking_id", []).append(new_tid)
        rec.setdefault("status_history", []).append(
            {"status": "alt_tracking_added", "timestamp": _now_iso()}
        )

        return json.dumps(
            {
                "original_tracking_id": original_tid,
                "added_tracking_id": new_tid,
                "all_tracking_ids": rec.get("tracking_id", []),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_alternate_tracking_id",
                "description": (
                    "Append an alternate tracking_id to an existing tracking record. "
                    "Selects an unused ID from the same courier and appends it to the tracking_id list."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {
                            "type": "string",
                            "description": "An existing tracking_id that identifies the tracking record to modify.",
                        }
                    },
                    "required": ["tracking_id"],
                },
            },
        }


class ReassignTrackingToNewCourierTool(Tool):
    """
    Reassign an existing tracking record to a different courier, generating a fresh tracking id.

    Behavior:
    - Validates the tracking record exists.
    - Validates the new courier exists and provides an unused tracking id.
    - Updates tracking.courier_name, appends the new id to tracking.tracking_id (keeps history),
      and logs 'reassigned_to_<courier>'.
    - Appends a fulfillment update into the corresponding order noting the reassignment and new tracking id.

    Input (kwargs):
        tracking_id (str, required)     # any id currently on the record
        new_courier_name (str, required)

    Output:
        JSON string with {"order_id","old_courier","new_courier","new_tracking_id"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tid = kwargs.get("tracking_id")
        new_courier_name = kwargs.get("new_courier_name")

        if not tid or not new_courier_name:
            return json.dumps({"error": "tracking_id and new_courier_name are required"}, indent=2)

        tracking_db = data.get("tracking", [])
        rec = next((t for t in tracking_db if tid in (t.get("tracking_id") or [])), None)
        if not rec:
            return json.dumps({"error": f"tracking_id '{tid}' not found in tracking"}, indent=2)

        old_courier = rec.get("courier_name")

        couriers = data.get("couriers", [])
        new_courier = next((c for c in couriers if c.get("name") == new_courier_name), None)
        if not new_courier:
            return json.dumps({"error": f"courier '{new_courier_name}' not found"}, indent=2)

        used_tids = {tid for t in tracking_db for tid in (t.get("tracking_id") or [])}
        new_tid = next((t for t in new_courier.get("tracking_ids", []) if t not in used_tids), None)
        if not new_tid:
            return json.dumps(
                {"error": f"No available tracking_id for courier '{new_courier_name}'"},
                indent=2,
            )

        rec["courier_name"] = new_courier_name
        rec.setdefault("tracking_id", []).append(new_tid)
        rec.setdefault("status_history", []).append(
            {"status": f"reassigned_to_{new_courier_name}", "timestamp": _now_iso()}
        )

        order_id = rec.get("order_id")
        if order_id:
            orders = data.get("orders", [])
            order = next((o for o in orders if o.get("order_id") == order_id), None)
            if order:
                order.setdefault("fulfillments", []).append(
                    {
                        "status": "carrier_reassigned",
                        "tracking_id": new_tid,
                        "courier": new_courier_name,
                        "timestamp": _now_iso(),
                    }
                )

        return json.dumps(
            {
                "order_id": order_id,
                "old_courier": old_courier,
                "new_courier": new_courier_name,
                "new_tracking_id": new_tid,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reassign_tracking_to_new_courier",
                "description": "Reassign a tracking record to a different courier and append the new tracking id; mirror change to order fulfillments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "new_courier_name": {"type": "string"},
                    },
                    "required": ["tracking_id", "new_courier_name"],
                },
            },
        }


class ReceiveSupplyOrderAndCloseTool(Tool):
    """
    Mark a supply order as 'received' and close it with a terminal timestamp.

    Behavior:
    - Validates the supply order exists.
    - Sets status to 'received' and stamps 'received_at' with UTC ISO (if not present).
    - Appends an event {type: "received", message: <optional note>, timestamp: UTC ISO} to events.
    - Updates stock of received items.
    - Sets status to 'closed' and stamps 'closed_at' with UTC ISO.

    Input (kwargs):
        supply_order_id (str, required)
        note (str, optional)

    Output:
        JSON string with {"supply_order_id","status","received_at","closed_at","events_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        so_id = kwargs.get("supply_order_id")
        note = kwargs.get("note")

        if not so_id:
            return json.dumps({"error": "supply_order_id is required"}, indent=2)

        supply_orders = data.get("supply_orders", [])
        products = data.get("products", [])

        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            return json.dumps({"error": f"supply_order_id '{so_id}' not found"}, indent=2)

        # 1. Update status to 'received' and add received_at timestamp
        so["status"] = "received"
        if not so.get("received_at"):
            so["received_at"] = _now_iso()

        # Append 'received' event
        event = {
            "type": "received",
            "message": (note or "supply order received"),
            "timestamp": _now_iso(),
        }
        (so.setdefault("events", [])).append(event)

        # 2. Update product stock for each item in the supply order
        for so_item in so.get("items", []):
            product_id = so_item.get("product_id")
            quantity = so_item.get("quantity", 0)

            product = next((p for p in products if p.get("product_id") == product_id), None)
            if product:
                product["quantity"] = product.get("quantity", 0) + quantity
                product["reserved_quantity"] = product.get("reserved_quantity", 0) + quantity

        # 3. Set final status to 'closed' and add closed_at timestamp
        so["status"] = "closed"
        so["closed_at"] = _now_iso()

        return json.dumps(
            {
                "supply_order_id": so_id,
                "status": so["status"],
                "received_at": so["received_at"],
                "closed_at": so["closed_at"],
                "events_len": len(so.get("events", [])),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "receive_supply_order_and_close",
                "description": "Set a supply order to 'received' and 'closed', update product stock, and append events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "note": {"type": "string"},
                    },
                    "required": ["supply_order_id"],
                },
            },
        }


class UpdateProductVariantPriceTool(Tool):
    """
    Update the price of an existing product variant in products.json.

    Behavior:
    - Validates that the provided product_id exists in products.json.
    - Validates that the provided item_id exists within product['variants'].
    - Overwrites the 'price' field with the new positive numeric value.
    - Does NOT create new products or variants; strictly updates an existing variant's price.

    Input (kwargs):
        product_id (str, required)
        item_id (str, required)
        new_price (float, required, > 0)

    Output:
        JSON string with {"product_id","item_id","old_price","new_price"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_id = kwargs.get("product_id")
        item_id = kwargs.get("item_id")
        new_price = kwargs.get("new_price")

        # Validação básica
        if not product_id or not item_id or new_price is None:
            return json.dumps({"error": "product_id, item_id and new_price are required"}, indent=2)
        try:
            price_val = float(new_price)
            if price_val <= 0:
                return json.dumps({"error": "new_price must be a positive number"}, indent=2)
        except Exception:
            return json.dumps({"error": "new_price must be numeric"}, indent=2)

        products = data.get("products", [])
        product = next((p for p in products if p.get("product_id") == product_id), None)
        if not product:
            return json.dumps(
                {"error": f"product_id '{product_id}' not found in products"}, indent=2
            )

        variants = product.get("variants") or {}
        variant = variants.get(item_id)
        if not variant:
            return json.dumps(
                {"error": f"item_id '{item_id}' not found under product_id '{product_id}'"},
                indent=2,
            )

        old_price = variant.get("price")
        variant["price"] = price_val
        product["variants"][item_id] = variant  # redundante, mas mantém simetria

        return json.dumps(
            {
                "product_id": product_id,
                "item_id": item_id,
                "old_price": old_price,
                "new_price": price_val,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_product_variant_price",
                "description": "Update the 'price' field of an existing product variant in products.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "new_price": {"type": "number", "minimum": 0},
                    },
                    "required": ["product_id", "item_id", "new_price"],
                },
            },
        }


TOOLS = [
    CreateOrderTool(),
    AppendPaymentTool(),
    AssignCourierAndCreateTrackingTool(),
    AdvanceTrackingStatusTool(),
    CancelOrderAndRefundTool(),
    AddItemsToOrderTool(),
    RemoveItemsByIndexTool(),
    SetOrderStatusTool(),
    LinkExistingTrackingToOrderTool(),
    CreateSupplyOrderTool(),
    SetSupplyOrderStatusTool(),
    AppendSupplyOrderEventTool(),
    GetOrderFinancialsTool(),
    FindOrdersByUserAndStatusTool(),
    AttachCourierByNameTool(),
    UpdateTrackingCourierTool(),
    AddTrackingCustomEventTool(),
    FindTrackingByOrderTool(),
    FindSupplyOrdersTool(),
    SplitOrderIntoShipmentsTool(),
    MergeOrdersForSameUserTool(),
    ReopenCancelledOrderTool(),
    ReplaceItemVariantInOrderTool(),
    AutoApproveSupplyOrderTool(),
    DuplicateOrderTool(),
    RemovePaymentByIndexTool(),
    AppendAlternateTrackingIdTool(),
    ReassignTrackingToNewCourierTool(),
    ReceiveSupplyOrderAndCloseTool(),
    UpdateProductVariantPriceTool(),
]
