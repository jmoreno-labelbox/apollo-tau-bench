from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
