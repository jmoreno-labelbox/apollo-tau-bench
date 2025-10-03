from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        order_id = _sid(order_id)
        orders = data.get("orders", [])
        o = next((x for x in orders if x.get("order_id") == order_id), None)
        payload = o or {"error": f"order {order_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrder",
                "description": "Retrieve order record by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
