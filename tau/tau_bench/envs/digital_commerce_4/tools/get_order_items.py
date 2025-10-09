from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetOrderItems(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        order_items: list = None
    ) -> str:
        order_id = _sid(order_id)
        items = order_items if order_items is not None else data.get("order_items", [])
        result = [i for i in items if i.get("order_id") == order_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderItems",
                "description": "List items for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
