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

class RefundOrderPartial(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, amount: Any, reason: str) -> str:
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
        refunds.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "refund_order_partial",
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