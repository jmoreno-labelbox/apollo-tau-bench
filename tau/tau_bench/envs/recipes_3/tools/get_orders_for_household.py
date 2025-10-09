from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetOrdersForHousehold(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], household_id: int) -> str:
        orders = _get_table(data, "orders")
        rows = [o for o in orders.values() if o.get("household_id") == household_id]
        payload = {"orders": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrdersForHousehold",
                "description": "Returns all orders for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }
