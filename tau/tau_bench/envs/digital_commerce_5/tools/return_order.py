# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _err(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

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

class ReturnOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, lines: Any, reason: str = None) -> str:
        if not order_id or lines is None:
            return _err("order_id and lines are required.")
        lines = _coerce_ids_in(lines)
        orders = list(list(list(data.get("orders", {}).values())) if isinstance(data.get("orders"), dict) else data.get("orders", []))
        order = next((o for o in orders if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")

        order_items = data.get("order_items", [])
        products = list(list(list(data.get("products", {}).values())) if isinstance(data.get("products"), dict) else data.get("products", []))

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