# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






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

class RefundOrderFull(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, reason: str) -> str:
        if not order_id or not reason:
            return _err("order_id and reason are required.")
        order_id = _as_id(order_id)
        orders = list(list(list(data.get("orders", {}).values())) if isinstance(data.get("orders"), dict) else data.get("orders", []))
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