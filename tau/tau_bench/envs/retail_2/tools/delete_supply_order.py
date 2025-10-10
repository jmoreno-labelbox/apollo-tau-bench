# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteSupplyOrder(Tool):
    """Deletes a supply order record from supply_orders.json by its ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], supply_order_id: str) -> str:
        supply_orders = data.get("supply_orders", [])
        order_to_delete = None
        for order in supply_orders:
            if order.get("supply_order_id") == supply_order_id:
                order_to_delete = order
                break

        if order_to_delete:
            supply_orders.remove(order_to_delete)
            return json.dumps({"status": "success", "deleted_supply_order_id": supply_order_id})

        return json.dumps({"error": "Supply order not found", "supply_order_id": supply_order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_supply_order",
                "description": "Permanently deletes a supply order record from supply_orders.json using its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"}
                    },
                    "required": ["supply_order_id"]
                }
            }
        }
