from tau_bench.envs.tool import Tool
import json
from typing import Any

class EnforceMinimumOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        orders: list = None,
        accounts: list = None
    ) -> str:
        order_id = _sid(order_id)
        orders = orders if orders is not None else data.get("orders", [])
        accounts = accounts if accounts is not None else data.get("accounts", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        account = next(
            (a for a in accounts if a.get("account_id") == order.get("account_id")),
            None,
        )
        threshold = (
            50.0 if (account and account.get("type") == "B2C Customer") else 1000.0
        )
        eligible = float(order.get("total_amount", 0.0)) >= threshold
        _append_audit(
            data,
            "ELIGIBILITY_CHECK",
            order_id,
            {"eligible": eligible, "threshold": threshold},
        )
        _ws_append(
            data,
            order_id,
            "ELIGIBILITY_CHECK",
            {"eligible": eligible, "threshold": threshold},
        )
        payload = {"order_id": order_id, "eligible": eligible, "threshold": threshold}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnforceMinimumOrder",
                "description": "Check if an order meets minimum order thresholds (Retail vs B2B).",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
