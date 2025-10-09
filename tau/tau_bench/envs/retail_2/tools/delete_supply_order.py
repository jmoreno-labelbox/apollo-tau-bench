from tau_bench.envs.tool import Tool
import json
from typing import Any

class DeleteSupplyOrder(Tool):
    """Remove a supply order entry from supply_orders.json using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str) -> str:
        supply_orders = data.get("supply_orders", [])
        order_to_delete = None
        for order in supply_orders:
            if order.get("supply_order_id") == supply_order_id:
                order_to_delete = order
                break

        if order_to_delete:
            supply_orders.remove(order_to_delete)
            payload = {"status": "success", "deleted_supply_order_id": supply_order_id}
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
                "name": "DeleteSupplyOrder",
                "description": "Permanently deletes a supply order record from supply_orders.json using its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"supply_order_id": {"type": "string"}},
                    "required": ["supply_order_id"],
                },
            },
        }
