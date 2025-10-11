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
    def invoke(data: Dict[str, Any], order_id: Any, amount: Any) -> str:
        if not order_id or amount is None:
            return _err("order_id and amount are required.")
        order_id = _as_id(order_id)

        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")

        amt = round(float(amount), 2)
        current = float(order.get("total_amount", 0.0))
        if amt < 0:
            return _err("amount must be non-negative.")
        if amt > current:
            return _err("amount exceeds order total_amount.")

        order["total_amount"] = round(current - amt, 2)
        data["orders"] = orders
        return json.dumps(
            {
                "order_id": order_id,
                "refunded_amount": amt,
                "new_total_amount": order["total_amount"],
                "kind": "partial",
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "refund_order_partial",
                "description": "Reduce order total_amount by refund amount (clamped ≥ 0).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Target order_id."},
                        "amount": {
                            "type": "number",
                            "description": "Refund amount to subtract (≤ current total_amount).",
                        },
                    },
                    "required": ["order_id", "amount"],
                },
            },
        }