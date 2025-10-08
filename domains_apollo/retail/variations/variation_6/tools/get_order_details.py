from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetOrderDetails(Tool):
    """Fetch an order using its ID."""

    @staticmethod
    def invoke(data, order_id=None) -> str:
        if not order_id:
            payload = {"error": "order_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        order = _find_order(data, order_id)
        payload = order or {"error": f"order_id {order_id} not found"}
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
                "name": "getOrderDetails",
                "description": "Fetch an order by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
