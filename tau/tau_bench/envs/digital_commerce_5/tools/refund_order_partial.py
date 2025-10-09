from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class RefundOrderPartial(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, amount: Any, reason: Any) -> str:
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
        data["refunds"][rec["refund_id"]] = rec
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RefundOrderPartial",
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
