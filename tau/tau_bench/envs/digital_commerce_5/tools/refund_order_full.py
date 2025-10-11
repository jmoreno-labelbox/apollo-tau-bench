# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RefundOrderFull(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, reason: str) -> str:
        if not order_id or not reason:
            return _err("order_id and reason are required.")
        order_id = _as_id(order_id)
        orders = list(data.get("orders", {}).values())
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
