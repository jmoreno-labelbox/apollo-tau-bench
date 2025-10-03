from tau_bench.envs.tool import Tool
import json
from typing import Any

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
