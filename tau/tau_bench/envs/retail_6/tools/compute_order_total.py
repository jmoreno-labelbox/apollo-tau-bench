from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputeOrderTotal(Tool):
    """Calculate the total of item prices for an order (excludes refunds/payments)."""

    @staticmethod
    def invoke(data, order_id: str = None) -> str:
        if not order_id:
            payload = {"error": "order_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        total = sum(i.get("price", 0) for i in o.get("items", []))
        payload = {"order_id": order_id, "computed_total": round(float(total), 2)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "computeOrderTotal",
                "description": "Return computed sum of item prices for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
