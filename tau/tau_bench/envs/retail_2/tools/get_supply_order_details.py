# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplyOrderDetails(Tool):
    """Retrieve a supply order from supply_orders.json by supply_order_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], supply_order_id: str) -> str:
        supply_orders = data.get("supply_orders", [])
        for so in supply_orders:
            if so.get("supply_order_id") == supply_order_id:
                return json.dumps(so)
        return json.dumps({"error": "Supply order not found", "supply_order_id": supply_order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supply_order_details",
                "description": "Get supply order details by supply_order_id from supply_orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"}
                    },
                    "required": ["supply_order_id"]
                }
            }
        }
