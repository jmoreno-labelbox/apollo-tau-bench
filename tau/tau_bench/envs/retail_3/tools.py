import json
import os
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


def _gen_order_id(seed: int | None = None) -> str:
    """
    Create a synthetic order ID that aligns with dataset flavor.

    Note: Collisions are rare but possible; this is acceptable for simulation.
    """
    pass
    base = seed if isinstance(seed, int) else int(datetime.utcnow().timestamp())
    return f"#W{base % 10_000_000:07d}"


def _gen_supply_order_id(seed: int | None = None) -> str:
    """
    Create a synthetic supply order ID (#SOxxxx) for simulation purposes.
    """
    pass
    base = seed if isinstance(seed, int) else int(datetime.utcnow().timestamp())
    return f"#SO{base % 10_000:04d}"


def _now_iso() -> str:
    """Provide the current UTC timestamp in ISO format (with seconds precision)."""
    pass
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


def _recalculate_financials(order: dict[str, Any]):
    """Reassesses financial totals for an order according to its items."""
    pass
    items_total = sum(item.get("price", 0) for item in order.get("items", []))
    #Make sure to address floating point precision problems
    order["items_total"] = round(items_total, 2)

    #Revise the initial payment in the history to show the updated total
    if order.get("payment_history"):
        order["payment_history"][0]["amount"] = order["items_total"]


def _adjust_stock(
    data: dict[str, Any], product_id: str, item_id: str, quantity_change: int
):
    pass
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


class CreateOrderTool(Tool):
    """
    Generate a new retail order by resolving variants from products.json and
    utilizing the customer's default address from users.json (unless specified otherwise).

    Behavior:
    - Confirms that the user exists (users.json).
    - Checks items: each must contain product_id, item_id, and an optional quantity>=1.
    - Resolves each (product_id, item_id) in products.json; expands according to quantity.
    - Adds a new order entry in orders.json:
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
    def invoke(data: dict[str, Any], supplier_id: str = None, items: list = None) -> str:
        if not supplier_id or not isinstance(items, list) or not items:
            payload = {"error": "supplier_id and non-empty items are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        suppliers = data.get("suppliers", [])
        if not any(s.get("supplier_id") == supplier_id for s in suppliers):
            payload = {"error": f"supplier_id '{supplier_id}' not found in suppliers"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        resolved_items: list[dict[str, Any]] = []
        products = data.get("products", [])
        for line in items:
            pid = line.get("product_id")
            iid = line.get("item_id")
            qty = int(line.get("quantity", 1) or 1)
            if not pid or not iid or qty < 1:
                payload = {
                        "error": "Each item must include product_id, item_id, and quantity>=1"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
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
                payload = {
                        "error": f"Variant not found for product_id='{pid}', item_id='{iid}'"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
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
        payload = {
                "message": "supply_order_created",
                "supply_order_id": new_so["supply_order_id"],
                "items_count": len(resolved_items),
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
                "name": "createOrder",
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
    Add a payment or refund entry to an order's payment_history in orders.json.

    Behavior:
    - Confirms the target order exists.
    - Adds an entry with fields:
        {
          "transaction_type": "payment" | "refund",
          "amount": float,
          "payment_method_id": str,
          "timestamp": "UTC ISO"
        }
    - No automatic reconciliation occurs; the caller manages amounts.

    Input (kwargs):
        order_id (str, required)
        transaction_type (str, required: "payment" or "refund")
        amount (float, required, >0)
        payment_method_id (str, required)

    Output:
        JSON string with {"order_id","payment_history_len"} or {"error":...}.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        order_id: str = None, 
        transaction_type: str = None, 
        amount: float = None, 
        payment_method_id: str = None
    ) -> str:
        if (
            not order_id
            or transaction_type not in {"payment", "refund"}
            or not isinstance(amount, (int, float))
            or amount <= 0
            or not payment_method_id
        ):
            payload = {
                    "error": "order_id, transaction_type('payment'|'refund'), positive amount, payment_method_id required"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        entry = {
            "transaction_type": transaction_type,
            "amount": float(amount),
            "payment_method_id": payment_method_id,
            "timestamp": _now_iso(),
        }
        (order.setdefault("payment_history", [])).append(entry)
        payload = {
                "order_id": order_id,
                "payment_history_len": len(order["payment_history"]),
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
                "name": "AppendPayment",
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
    Assign a courier to an order and generate a tracking entry in tracking.json.

    Behavior:
    - Retrieves the order (orders.json) and the user's country (users.json) to select a courier from couriers.json.
    - Chooses the first available tracking_id from the selected courier's tracking_ids.
    - Creates a new entry in tracking.json:
        {
          "tracking_id": [ "<id>" ],
          "order_id": "...",
          "courier_name": "...",
          "status_history": [{ "status": "label_created", "timestamp": "UTC ISO" }]
        }
    - Additionally, adds a fulfillment snippet to the order in orders.json:
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
    def invoke(data: dict[str, Any], order_id: str = None) -> str:
        if not order_id:
            payload = {"error": "order_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        users = data.get("users", [])
        user = next(
            (u for u in users if u.get("user_id") == order.get("user_id")), None
        )
        if not user:
            payload = {"error": f"user '{order.get('user_id')}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        country = ((user.get("address") or {}).get("country")) or "USA"
        couriers = data.get("couriers", [])
        courier = next(
            (c for c in couriers if country in (c.get("coverage_area") or [])),
            couriers[0] if couriers else None,
        )
        if not courier:
            payload = {"error": f"No courier covers '{country}'"}
            out = json.dumps(payload, indent=2)
            return out

        used = {
            tid for t in data.get("tracking", []) for tid in t.get("tracking_id", [])
        }
        tid = next(
            (tid for tid in courier.get("tracking_ids", []) if tid not in used), None
        )
        if not tid:
            payload = {
                    "error": f"No available tracking_id for courier '{courier.get('name')}'"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        data.setdefault("tracking", []).append(
            {
                "tracking_id": [tid],
                "order_id": order_id,
                "courier_name": courier.get("name"),
                "status_history": [
                    {"status": "label_created", "timestamp": _now_iso()}
                ],
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
        payload = {
                "order_id": order_id,
                "tracking_id": tid,
                "courier_name": courier.get("name"),
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
                "name": "assignCourierAndCreateTracking",
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
    Update the tracking status for an order in tracking.json and reflect the change in orders.json.

    Behavior:
    - Confirms that the specified tracking_id exists in tracking.json.
    - Adds a new status entry to status_history.
    - If order_status is provided, also adds a fulfillment update to the order.
      Suggested status progression: label_created -> shipped -> in_transit -> out_for_delivery -> delivered.
    - If status == "delivered", optionally set order.status = "completed".

    Input (kwargs):
        tracking_id (str, required)
        status (str, required)              # e.g., "shipped", "delivered", etc.
        order_status (str, optional)        # e.g., "fulfilled", "completed"

    Output:
        JSON string with {"tracking_id","new_status","history_len"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None, status: str = None, order_status: str = None) -> str:
        if not tracking_id or not status:
            payload = {"error": "tracking_id and status are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        tracking = data.get("tracking", [])
        tr = next(
            (t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None
        )
        if not tr:
            payload = {"error": f"tracking_id '{tracking_id}' not found in tracking.json"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Verify that tracking_history is present prior to adding
        if "tracking_history" not in tr:
            tr["tracking_history"] = {}

        tr["tracking_history"][status] = _now_iso()

        # Replicate into orders.json if relevant
        orders = data.get("orders", [])
        order = next(
            (o for o in orders if o.get("order_id") == tr.get("order_id")), None
        )
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
        payload = {
                "tracking_id": tracking_id,
                "new_status": status,
                "history_len": len(tr["tracking_history"]),
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
                "name": "AdvanceTrackingStatus",
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
    Cancel an order and optionally generate an automatic refund entry.

    Behavior:
    - Confirms the order exists and is not already completed or cancelled.
    - Changes order.status to "cancelled".
    - If refund_amount > 0, adds a refund entry to payment_history.
    - Does NOT modify tracking.json; callers must manage carrier processes independently.

    Input (kwargs):
        order_id (str, required)
        refund_amount (float, optional, default=0)
        payment_method_id (str, optional, required if refund_amount > 0)

    Output:
        JSON string with {"order_id","status","refund_created":bool} or {"error":...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, refund_amount: float = 0, payment_method_id: str = None) -> str:
        if not order_id:
            payload = {"error": "order_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        if refund_amount > 0 and not payment_method_id:
            payload = {"error": "payment_method_id is required when refund_amount > 0"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        if order.get("status") in {"completed", "cancelled"}:
            payload = {"error": f"order already {order.get('status')}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

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
        payload = {
                "order_id": order_id,
                "status": "cancelled",
                "refund_created": refund_created,
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
                "name": "CancelOrderAndRefund",
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
    - Confirms the order exists.
    - For each {product_id, item_id, quantity}, resolves the variant from products.json.
    - Adds one entry per unit to order["items"] (consistent with dataset structure).
    - Does not recalculate totals; this function only modifies the item list.

    Input (kwargs):
        order_id (str, required)
        items (List[dict], required) -> {product_id, item_id, quantity?}

    Output:
        JSON string with {"order_id","added_count","items_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, items: list = None) -> str:
        if not order_id or not isinstance(items, list) or not items:
            payload = {"error": "order_id and non-empty items are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        orders = data.get("orders", [])
        products = data.get("products", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)

        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        added = 0
        for line in items:
            pid = line.get("product_id")
            iid = line.get("item_id")
            qty = int(line.get("quantity", 1) or 1)

            if not pid or not iid or qty < 1:
                payload = {
                        "error": "Each item must include product_id, item_id, and quantity>=1"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            product = next((p for p in products if p.get("product_id") == pid), None)
            variant = (product.get("variants") or {}).get(iid) if product else None

            if not variant:
                payload = {
                        "error": f"Variant not found for product_id='{pid}', item_id='{iid}'"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

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
        payload = {
                "order_id": order_id,
                "added_count": added,
                "items_len": len(order.get("items", [])),
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
                "name": "AddItemsToOrder",
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
    Remove items from an order based on index positions within order['items'].

    Behavior:
    - Confirms the order exists and 'indices' is a list of unique integers.
    - Deletes items at the specified indices (0-based) that are present in the current list.
    - Silently ignores out-of-range indices to ensure robustness.

    Input (kwargs):
        order_id (str, required)
        indices (List[int], required)

    Output:
        JSON string with {"order_id","removed_count","items_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, indices: list = None) -> str:
        if not order_id or not isinstance(indices, list) or not indices:
            payload = {"error": "order_id and non-empty indices are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        try:
            idxs = sorted({int(i) for i in indices if int(i) >= 0}, reverse=True)
        except Exception:
            payload = {"error": "indices must be a list of integers >= 0"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

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
        payload = {
                "order_id": order_id,
                "removed_count": removed_count,
                "items_len": len(items),
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
                "name": "RemoveItemsByIndex",
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
    Set or change an order's status in orders.json.

    Behavior:
    - Confirms the order exists.
    - Updates order['status'] to the provided value.
    - Does not alter fulfillments or payment_history.

    Input (kwargs):
        order_id (str, required)
        status (str, required)  # e.g., "pending", "fulfilled", "completed", "cancelled"

    Output:
        JSON string with {"order_id","status"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, status: str = None) -> str:
        if not order_id or not isinstance(status, str) or not status:
            payload = {"error": "order_id and non-empty status are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        order["status"] = status
        payload = {"order_id": order_id, "status": status}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetOrderStatus",
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
    Associate an existing tracking record with an order by creating a fulfillment entry.

    Behavior:
    - Confirms the order exists.
    - Checks that the tracking_id is present in tracking.json (within any record's 'tracking_id' list).
    - Adds a fulfillment entry to the order containing at least:
        { "status": "linked", "tracking_id": "<id>", "timestamp": "UTC ISO" }
      Optionally includes 'courier' if available in the tracking record.

    Input (kwargs):
        order_id (str, required)
        tracking_id (str, required)

    Output:
        JSON string with {"order_id","tracking_id","fulfillments_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, tracking_id: str = None) -> str:
        if not order_id or not tracking_id:
            payload = {"error": "order_id and tracking_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        tracking = data.get("tracking", [])
        tr = next(
            (t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None
        )
        if not tr:
            payload = {"error": f"tracking_id '{tracking_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        fulfillment = {
            "status": "linked",
            "tracking_id": tracking_id,
            "timestamp": _now_iso(),
        }
        if tr.get("courier_name"):
            fulfillment["courier"] = tr["courier_name"]

        order.setdefault("fulfillments", []).append(fulfillment)
        payload = {
                "order_id": order_id,
                "tracking_id": tracking_id,
                "fulfillments_len": len(order.get("fulfillments", [])),
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
                "name": "LinkExistingTrackingToOrder",
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
    Generate a new supply order in supply_orders.json for restocking needs.

    Behavior:
    - Accepts a supplier_id and a list of items {product_id, item_id, quantity}.
    - Resolves each variant from products.json to retain name/price/options.
    - Creates a new entry in supply_orders.json with:
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
    def invoke(data: dict[str, Any], supplier_id: str = None, items: list = None) -> str:
        if not supplier_id or not isinstance(items, list) or not items:
            payload = {"error": "supplier_id and non-empty items are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        suppliers = data.get("suppliers", [])
        if not any(s.get("supplier_id") == supplier_id for s in suppliers):
            payload = {"error": f"supplier_id '{supplier_id}' not found in suppliers"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        products = data.get("products", [])
        resolved_items: list[dict[str, Any]] = []

        for line in items:
            pid = line.get("product_id")
            iid = line.get("item_id")
            qty = int(line.get("quantity", 1) or 1)
            if not pid or not iid or qty < 1:
                payload = {
                        "error": "Each item must include product_id, item_id, and quantity>=1"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

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
                payload = {
                        "error": f"Variant not found for product_id='{pid}', item_id='{iid}'"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

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
        payload = {
                "message": "supply_order_created",
                "supply_order_id": new_so["supply_order_id"],
                "items_count": len(resolved_items),
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
                "name": "createSupplyOrder",
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
    Set or change the status of a supply order in supply_orders.json.

    Behavior:
    - Confirms that the supply_order_id exists.
    - Updates entry['status'] to the provided value.
    - If status == "received", sets 'received_at' timestamp (UTC ISO) if not already present.

    Input (kwargs):
        supply_order_id (str, required)
        status (str, required)  # e.g., "pending","approved","in_transit","received","cancelled"

    Output:
        JSON string with {"supply_order_id","status"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None, status: str = None) -> str:
        so_id = supply_order_id

        if not so_id or not isinstance(status, str) or not status:
            payload = {"error": "supply_order_id and non-empty status are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        supply_orders = data.get("supply_orders", [])
        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            payload = {"error": f"supply_order_id '{so_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        so["status"] = status
        if status == "received" and not so.get("received_at"):
            so["received_at"] = _now_iso()
        payload = {"supply_order_id": so_id, "status": status}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetSupplyOrderStatus",
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
    Add an event note to a supply order's 'events' list in supply_orders.json.

    Behavior:
    - Confirms that the supply_order_id exists.
    - Adds an event object:
        {
          "type": "<string>",
          "message": "<string>",
          "timestamp": "UTC ISO"
        }
    - Creates the 'events' list if it is not already present.

    Input (kwargs):
        supply_order_id (str, required)
        event_type (str, required)
        message (str, required)

    Output:
        JSON string with {"supply_order_id","events_len"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None, event_type: str = None, message: str = None) -> str:
        so_id = supply_order_id
        event_type = event_type
        message = message

        if not so_id or not event_type or not message:
            payload = {"error": "supply_order_id, event_type, and message are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        supply_orders = data.get("supply_orders", [])
        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            payload = {"error": f"supply_order_id '{so_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        event = {
            "type": str(event_type),
            "message": str(message),
            "timestamp": _now_iso(),
        }
        so.setdefault("events", []).append(event)
        payload = {"supply_order_id": so_id, "events_len": len(so.get("events", []))}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendSupplyOrderEvent",
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
    """Retrieves financial information for an order from the shared in-memory state."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None) -> str:
        # Fetches the 'orders' object from the in-memory state, which could have been altered.
        orders = data.get("orders", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"Order '{order_id}' not found in the current state"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"order_id": order_id, "items_total": order.get("items_total", 0)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderFinancials",
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
    Locate orders filtered by user_id and optional status.

    Behavior:
    - If status is provided, filters orders for an exact match.
    - Returns a concise listing: order_id, status, items_len, timestamp.

    Input (kwargs):
        user_id (str, required)
        status (str, optional)

    Output:
        JSON string with {"user_id","count","orders":[...]} or {"error":...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, status: str = None) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload, indent=2)
            return out

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
        payload = {"user_id": user_id, "count": len(filtered), "orders": filtered}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindOrdersByUserAndStatus",
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
    Assign a specific courier (by name) to an order and generate a tracking entry.

    Behavior:
    - Confirms the order exists (orders.json).
    - Confirms the courier exists (couriers.json).
    - Selects the first available tracking_id from the courier.
    - Creates a new record in tracking.json and adds a fulfillment entry to the order.

    Input (kwargs):
        order_id (str, required)
        courier_name (str, required)

    Output:
        JSON string with {"order_id","tracking_id","courier_name"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, courier_name: str = None) -> str:
        if not order_id or not courier_name:
            payload = {"error": "order_id and courier_name are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        couriers = data.get("couriers", [])
        courier = next((c for c in couriers if c.get("name") == courier_name), None)
        if not courier:
            payload = {"error": f"courier '{courier_name}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        used_ids = {
            tid for t in data.get("tracking", []) for tid in t.get("tracking_id", [])
        }
        candidate_ids = courier.get("tracking_ids", [])
        tid = next((tid for tid in candidate_ids if tid not in used_ids), None)

        if not tid:
            payload = {"error": f"No available tracking_id for courier '{courier_name}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        tracking = data.setdefault("tracking", [])
        tracking.append(
            {
                "tracking_id": [tid],
                "order_id": order_id,
                "courier_name": courier_name,
                "status_history": [
                    {"status": "label_created", "timestamp": _now_iso()}
                ],
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
        payload = {"order_id": order_id, "tracking_id": tid, "courier_name": courier_name}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "attachCourierByName",
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
    Modify the courier_name of an existing tracking record in tracking.json.

    Behavior:
    - Confirms that tracking_id exists in tracking.json (found within each record's tracking_id list).
    - Replaces 'courier_name' with the provided value.
    - Adds a status_history note 'courier_updated'.

    Input (kwargs):
        tracking_id (str, required)
        courier_name (str, required)

    Output:
        JSON string with {"tracking_id","courier_name"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None, courier_name: str = None) -> str:
        if not tracking_id or not courier_name:
            payload = {"error": "tracking_id and courier_name are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        tracking = data.get("tracking", [])
        rec = next(
            (t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None
        )
        if not rec:
            payload = {"error": f"tracking_id '{tracking_id}' not found in tracking records"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        rec["courier_name"] = courier_name
        rec.setdefault("status_history", []).append(
            {"status": "courier_updated", "timestamp": _now_iso()}
        )
        payload = {"tracking_id": tracking_id, "courier_name": courier_name}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTrackingCourier",
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
    Add a custom event to the status_history of a tracking record.

    Behavior:
    - Confirms that tracking_id exists in tracking.json.
    - Adds {"status": <event_status>, "timestamp": UTC ISO, "note": <optional str>}.
    - Does not alter orders.json (pure tracking enhancement).

    Input (kwargs):
        tracking_id (str, required)
        event_status (str, required)   # e.g., "in_transit", "delayed", "checkpoint"
        note (str, optional)

    Output:
        JSON string with {"tracking_id","new_status","history_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None, event_status: str = None, note: str = None) -> str:
        if not tracking_id or not event_status:
            payload = {"error": "tracking_id and event_status are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        tracking = data.get("tracking", [])
        rec = next(
            (t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None
        )
        if not rec:
            payload = {"error": f"tracking_id '{tracking_id}' not found in tracking records"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        event = {"status": str(event_status), "timestamp": _now_iso()}
        if note:
            event["note"] = str(note)

        rec.setdefault("status_history", []).append(event)
        payload = {
                "tracking_id": tracking_id,
                "new_status": event_status,
                "history_len": len(rec.get("status_history", [])),
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
                "name": "AddTrackingCustomEvent",
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
    """Locates tracking information for an order from the shared in-memory state."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None) -> str:
        # Retrieves the tracking information from the in-memory state.
        tracking_data = data.get("tracking", [])

        tr = next((t for t in tracking_data if t.get("order_id") == order_id), None)
        if not tr:
            payload = {
                "error": f"Tracking for order '{order_id}' not found in the current state"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = tr
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindTrackingByOrder",
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
    Locate supply orders filtered by optional supplier_id and/or status.

    Behavior:
    - If supplier_id is provided, only returns matching entries.
    - If status is provided, only returns entries with an exact match.
    - Returns a concise view: supply_order_id, supplier_id, status, items_count, created_at.

    Input (kwargs):
        supplier_id (str, optional)
        status (str, optional)

    Output:
        JSON string with {"count","supply_orders":[...]}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, status: str = None) -> str:
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
        payload = {"count": len(filtered), "supply_orders": filtered}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindSupplyOrders",
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
    Divide an order's items into several shipments, generating tracking and fulfillments.

    Behavior:
    - Confirms the order exists.
    - For each shipment entry, requires 'indices' (0-based positions in order.items)
      and a 'courier_name' to generate a tracking record.
    - Creates one tracking record for each shipment and adds corresponding fulfillment
      entries to the order. Items are not deleted; this function only generates logistics records.

    Input (kwargs):
        order_id (str, required)
        shipments (List[dict], required): each with
            - indices: List[int]  # positions within order['items']
            - courier_name: str

    Output:
        JSON string with {"order_id","created_trackings":[{"courier_name","tracking_id","count"}], "shipments_count"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, shipments: list = None) -> str:
        if not order_id or not isinstance(shipments, list) or not shipments:
            payload = {"error": "order_id and non-empty shipments are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        couriers = data.get("couriers", [])
        tracking_db = data.get("tracking", [])
        items_len = len(order.get("items", []))
        created = []

        used_tracking_ids = {
            tid for t in tracking_db for tid in t.get("tracking_id", [])
        }

        for sh in shipments:
            idxs = sh.get("indices")
            courier_name = sh.get("courier_name")
            if not isinstance(idxs, list) or not idxs or not courier_name:
                payload = {
                        "error": "each shipment requires 'indices' (list) and 'courier_name'"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            #check that indices are within the valid range
            valid = [
                i
                for i in {int(i) for i in idxs if isinstance(i, (int, float))}
                if 0 <= i < items_len
            ]
            if not valid:
                payload = {"error": f"shipment has no valid indices within 0..{items_len-1}"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            #locate courier
            courier = next((c for c in couriers if c.get("name") == courier_name), None)
            if not courier:
                payload = {"error": f"courier '{courier_name}' not found"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

            #select the first available tracking id
            tid = next(
                (
                    tid
                    for tid in courier.get("tracking_ids", [])
                    if tid not in used_tracking_ids
                ),
                None,
            )
            if not tid:
                payload = {"error": f"No available tracking_id for courier '{courier_name}'"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            used_tracking_ids.add(tid)

            #generate tracking record
            tracking_db.append(
                {
                    "tracking_id": [tid],
                    "order_id": order_id,
                    "courier_name": courier_name,
                    "status_history": [
                        {"status": "label_created", "timestamp": _now_iso()}
                    ],
                }
            )

            #add fulfillment to the order
            (order.setdefault("fulfillments", [])).append(
                {
                    "status": "label_created",
                    "tracking_id": tid,
                    "courier": courier_name,
                    "timestamp": _now_iso(),
                    "items_indices": sorted(valid),
                }
            )

            created.append(
                {"courier_name": courier_name, "tracking_id": tid, "count": len(valid)}
            )
        payload = {
                "order_id": order_id,
                "created_trackings": created,
                "shipments_count": len(created),
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
                "name": "splitOrderIntoShipments",
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
    Combine items from a source order into a target order when both are associated with the same user.

    Behavior:
    - Confirms both orders exist and are linked to the same user_id.
    - Adds all items from the source to the target's 'items'.
    - Optionally transfers payment_history as well (flag include_payments).
    - Changes the source order status to "cancelled" after the merge.
    - Does not merge fulfillments; logistics remain tied to the original order_id.

    Input (kwargs):
        target_order_id (str, required)
        source_order_id (str, required)
        include_payments (bool, optional, default=False)

    Output:
        JSON string with {"target_order_id","source_order_id","moved_items","target_items_len","source_status"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], target_order_id: str = None, source_order_id: str = None, include_payments: bool = False) -> str:
        if not target_order_id or not source_order_id or target_order_id == source_order_id:
            payload = {
                    "error": "target_order_id and source_order_id must be provided and different"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        orders = data.get("orders", [])
        target = next((o for o in orders if o.get("order_id") == target_order_id), None)
        source = next((o for o in orders if o.get("order_id") == source_order_id), None)
        if not target or not source:
            payload = {"error": "target or source order not found"}
            out = json.dumps(payload, indent=2)
            return out

        if target.get("user_id") != source.get("user_id"):
            payload = {"error": "orders belong to different users"}
            out = json.dumps(payload, indent=2)
            return out

        moved_items = len(source.get("items", []))
        (target.setdefault("items", [])).extend(source.get("items", []))

        if include_payments and source.get("payment_history"):
            (target.setdefault("payment_history", [])).extend(
                source.get("payment_history", [])
            )

        source["status"] = "cancelled"
        payload = {
                "target_order_id": target_order_id,
                "source_order_id": source_order_id,
                "moved_items": moved_items,
                "target_items_len": len(target.get("items", [])),
                "source_status": source.get("status"),
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
                "name": "MergeOrdersForSameUser",
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
    Reopen an order that was previously cancelled by changing its status back to 'pending'.

    Behavior:
    - Confirms the order exists and is currently 'cancelled'.
    - Updates order['status'] to 'pending'.
    - Does not alter items, payment_history, or fulfillments.

    Input (kwargs):
        order_id (str, required)

    Output:
        JSON string with {"order_id","status"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None) -> str:
        if not order_id:
            payload = {"error": "order_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        if order.get("status") != "cancelled":
            payload = {
                    "error": f"order status must be 'cancelled', found '{order.get('status')}'"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        order["status"] = "pending"
        payload = {"order_id": order_id, "status": "pending"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReopenCancelledOrder",
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
    Substitutes an item in an order, recalculates financials, and refreshes tracking,
    with all modifications taking place in the shared in-memory state.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str, index: int, product_id: str, item_id: str) -> str:
        orders = data.get("orders", [])
        products = data.get("products", [])
        tracking_data = data.get("tracking", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"Order '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

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
            payload = {"error": f"Variant '{item_id}' for product '{product_id}' not found"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        items = order.get("items", [])
        if not 0 <= index < len(items):
            payload = {
                    "error": f"Index {index} is out of bounds for the items in order '{order_id}'"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

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
        payload = {
                "status": "success",
                "message": f"Order {order_id} was successfully modified in memory.",
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
                "name": "ReplaceItemVariantInOrder",
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
    Automatically authorize a pending supply order and log an approval event.

    Behavior:
    - Confirms that the supply order exists and is in 'pending' status.
    - Changes status to 'approved'.
    - Adds an event {type: "approved", message: <optional reason>, timestamp: UTC ISO}.

    Input (kwargs):
        supply_order_id (str, required)
        reason (str, optional)

    Output:
        JSON string with {"supply_order_id","status","events_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None, reason: str = None) -> str:
        so_id = supply_order_id

        if not so_id:
            payload = {"error": "supply_order_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        supply_orders = data.get("supply_orders", [])
        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            payload = {"error": f"supply_order_id '{so_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if so.get("status") != "pending":
            payload = {
                    "error": f"status must be 'pending' to auto-approve (found '{so.get('status')}')"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        so["status"] = "approved"
        event = {
            "type": "approved",
            "message": reason or "auto-approved",
            "timestamp": _now_iso(),
        }
        (so.setdefault("events", [])).append(event)
        payload = {
                "supply_order_id": so_id,
                "status": "approved",
                "events_len": len(so.get("events", [])),
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
                "name": "AutoApproveSupplyOrder",
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
    Create a duplicate of an existing order as a new one for the same user.

    Behavior:
    - Confirms the source order exists.
    - Copies user_id, address, items; resets fulfillments to [] and payment_history to [].
    - Changes status to "pending" and generates a new order_id and timestamp.
    - Adds the new order to orders.json.

    Input (kwargs):
        source_order_id (str, required)

    Output:
        JSON string with {"source_order_id","new_order_id","items_count"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], source_order_id: str = None) -> str:
        src_id = source_order_id
        if not src_id:
            payload = {"error": "source_order_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", [])
        src = next((o for o in orders if o.get("order_id") == src_id), None)
        if not src:
            payload = {"error": f"source_order_id '{src_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

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
        payload = {
                "source_order_id": src_id,
                "new_order_id": new_order["order_id"],
                "items_count": len(new_order.get("items", [])),
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
                "name": "duplicateOrder",
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
    Delete a payment/refund entry from an order's payment_history by index.

    Behavior:
    - Confirms the order exists and the index is within range.
    - Deletes payment_history[index].

    Input (kwargs):
        order_id (str, required)
        index (int, required)   # 0-based

    Output:
        JSON string with {"order_id","removed":true,"payment_history_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, index: int = None) -> str:
        if not order_id or index is None:
            payload = {"error": "order_id and index are required"}
            out = json.dumps(payload, indent=2)
            return out

        try:
            idx = int(index)
        except Exception:
            payload = {"error": "index must be an integer"}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        history = order.get("payment_history", [])
        if not (0 <= idx < len(history)):
            payload = {"error": f"index out of range 0..{max(0, len(history)-1)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        history.pop(idx)
        order["payment_history"] = history
        payload = {
                "order_id": order_id,
                "removed": True,
                "payment_history_len": len(history),
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
                "name": "RemovePaymentByIndex",
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
    Add an alternate tracking_id to an existing tracking record.

    Behavior:
    - Confirms that tracking_id exists in tracking data.
    - Retrieves courier_name from the record.
    - Obtains an unused tracking_id from the same courier.
    - Adds the new tracking_id and records 'alt_tracking_added' in status_history.
    """

    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None) -> str:
        original_tid = tracking_id
        if not original_tid:
            payload = {"error": "tracking_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        tracking = data.get("tracking", [])
        rec = next(
            (t for t in tracking if original_tid in (t.get("tracking_id") or [])), None
        )
        if not rec:
            payload = {
                    "error": f"tracking_id '{original_tid}' not found in tracking records"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        courier_name = rec.get("courier_name")
        if not courier_name:
            payload = {"error": "courier_name is missing on the tracking record"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        couriers = data.get("couriers", [])
        courier = next((c for c in couriers if c.get("name") == courier_name), None)
        if not courier:
            payload = {"error": f"courier '{courier_name}' not found in couriers data"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        used_ids = {tid for t in tracking for tid in t.get("tracking_id", [])}
        candidate_ids = courier.get("tracking_ids", [])
        new_tid = next((tid for tid in candidate_ids if tid not in used_ids), None)

        if not new_tid:
            payload = {"error": f"No available tracking_id for courier '{courier_name}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        rec.setdefault("tracking_id", []).append(new_tid)
        rec.setdefault("status_history", []).append(
            {"status": "alt_tracking_added", "timestamp": _now_iso()}
        )
        payload = {
                "original_tracking_id": original_tid,
                "added_tracking_id": new_tid,
                "all_tracking_ids": rec.get("tracking_id", []),
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
                "name": "appendAlternateTrackingId",
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
    Reassign an existing tracking record to a different courier, creating a new tracking id.

    Behavior:
    - Confirms the tracking record exists.
    - Confirms the new courier exists and provides an unused tracking id.
    - Updates tracking.courier_name, adds the new id to tracking.tracking_id (maintains history),
      and records 'reassigned_to_<courier>'.
    - Adds a fulfillment update to the corresponding order indicating the reassignment and new tracking id.

    Input (kwargs):
        tracking_id (str, required)     # any id currently on the record
        new_courier_name (str, required)

    Output:
        JSON string with {"order_id","old_courier","new_courier","new_tracking_id"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None, new_courier_name: str = None) -> str:
        if not tracking_id or not new_courier_name:
            payload = {"error": "tracking_id and new_courier_name are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        tracking_db = data.get("tracking", [])
        rec = next(
            (t for t in tracking_db if tracking_id in (t.get("tracking_id") or [])), None
        )
        if not rec:
            payload = {"error": f"tracking_id '{tracking_id}' not found in tracking"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        old_courier = rec.get("courier_name")

        couriers = data.get("couriers", [])
        new_courier = next(
            (c for c in couriers if c.get("name") == new_courier_name), None
        )
        if not new_courier:
            payload = {"error": f"courier '{new_courier_name}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        used_tids = {tid for t in tracking_db for tid in (t.get("tracking_id") or [])}
        new_tid = next(
            (t for t in new_courier.get("tracking_ids", []) if t not in used_tids), None
        )
        if not new_tid:
            payload = {"error": f"No available tracking_id for courier '{new_courier_name}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

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
        payload = {
                "order_id": order_id,
                "old_courier": old_courier,
                "new_courier": new_courier_name,
                "new_tracking_id": new_tid,
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
                "name": "reassignTrackingToNewCourier",
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
    Designate a supply order as 'received' and finalize it with a terminal timestamp.

    Behavior:
    - Confirms the supply order exists.
    - Changes status to 'received' and records 'received_at' with UTC ISO (if not already present).
    - Adds an event {type: "received", message: <optional note>, timestamp: UTC ISO} to events.
    - Updates inventory of received items.
    - Changes status to 'closed' and records 'closed_at' with UTC ISO.

    Input (kwargs):
        supply_order_id (str, required)
        note (str, optional)

    Output:
        JSON string with {"supply_order_id","status","received_at","closed_at","events_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None, note: str = None) -> str:
        so_id = supply_order_id

        if not so_id:
            payload = {"error": "supply_order_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        supply_orders = data.get("supply_orders", [])
        products = data.get("products", [])

        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            payload = {"error": f"supply_order_id '{so_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #1. Change status to 'received' and include received_at timestamp
        so["status"] = "received"
        if not so.get("received_at"):
            so["received_at"] = _now_iso()

        #Add 'received' event
        event = {
            "type": "received",
            "message": (note or "supply order received"),
            "timestamp": _now_iso(),
        }
        (so.setdefault("events", [])).append(event)

        #2. Adjust product inventory for every item in the supply order
        for so_item in so.get("items", []):
            product_id = so_item.get("product_id")
            quantity = so_item.get("quantity", 0)

            product = next(
                (p for p in products if p.get("product_id") == product_id), None
            )
            if product:
                product["quantity"] = product.get("quantity", 0) + quantity
                product["reserved_quantity"] = (
                    product.get("reserved_quantity", 0) + quantity
                )

        #3. Change final status to 'closed' and include closed_at timestamp
        so["status"] = "closed"
        so["closed_at"] = _now_iso()
        payload = {
                "supply_order_id": so_id,
                "status": so["status"],
                "received_at": so["received_at"],
                "closed_at": so["closed_at"],
                "events_len": len(so.get("events", [])),
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
                "name": "ReceiveSupplyOrderAndClose",
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
    Modify the price of an existing product variant in products.json.

    Behavior:
    - Confirms that the specified product_id exists in products.json.
    - Confirms that the specified item_id exists within product['variants'].
    - Replaces the 'price' field with the new positive numeric value.
    - Does NOT create new products or variants; strictly updates the price of an existing variant.

    Input (kwargs):
        product_id (str, required)
        item_id (str, required)
        new_price (float, required, > 0)

    Output:
        JSON string with {"product_id","item_id","old_price","new_price"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None, item_id: str = None, new_price: Any = None) -> str:
        # Basic validation
        if not product_id or not item_id or new_price is None:
            payload = {"error": "product_id, item_id and new_price are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        try:
            price_val = float(new_price)
            if price_val <= 0:
                payload = {"error": "new_price must be a positive number"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        except Exception:
            payload = {"error": "new_price must be numeric"}
            out = json.dumps(payload, indent=2)
            return out

        products = data.get("products", [])
        product = next((p for p in products if p.get("product_id") == product_id), None)
        if not product:
            payload = {"error": f"product_id '{product_id}' not found in products"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        variants = product.get("variants") or {}
        variant = variants.get(item_id)
        if not variant:
            payload = {
                    "error": f"item_id '{item_id}' not found under product_id '{product_id}'"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        old_price = variant.get("price")
        variant["price"] = price_val
        product["variants"][item_id] = variant  # redundant, but maintains symmetry
        payload = {
                "product_id": product_id,
                "item_id": item_id,
                "old_price": old_price,
                "new_price": price_val,
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
                "name": "UpdateProductVariantPrice",
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
