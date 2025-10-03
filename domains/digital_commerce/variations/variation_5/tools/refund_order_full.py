from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class RefundOrderFull(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, reason: Any) -> str:
        if not order_id or not reason:
            return _err("order_id and reason are required.")
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
            "reason": reason,
        }
        refunds.append(rec)
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
