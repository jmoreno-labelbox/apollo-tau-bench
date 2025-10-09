from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetOrderDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: int) -> str:
        orders = _get_table(data, "orders")
        items = _get_table(data, "order_items")
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        rows = [it for it in items.values() if it.get("order_id") == order_id]
        payload = {"order": order, "items": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderDetails",
                "description": "Returns an order row and its items.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "integer"}},
                    "required": ["order_id"],
                },
            },
        }
