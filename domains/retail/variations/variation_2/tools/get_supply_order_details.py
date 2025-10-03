from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetSupplyOrderDetails(Tool):
    """Fetch a supply order from supply_orders.json using supply_order_id."""

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str) -> str:
        supply_orders = data.get("supply_orders", [])
        for so in supply_orders:
            if so.get("supply_order_id") == supply_order_id:
                payload = so
                out = json.dumps(payload)
                return out
        payload = {"error": "Supply order not found", "supply_order_id": supply_order_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplyOrderDetails",
                "description": "Get supply order details by supply_order_id from supply_orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"supply_order_id": {"type": "string"}},
                    "required": ["supply_order_id"],
                },
            },
        }
