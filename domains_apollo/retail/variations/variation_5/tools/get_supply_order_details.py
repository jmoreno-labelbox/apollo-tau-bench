from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetSupplyOrderDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None) -> str:
        if not supply_order_id:
            payload = {"error": "supply_order_id is required"}
            out = json.dumps(payload)
            return out

        supply_orders = data["supply_orders"]
        order = next(
            (o for o in supply_orders if o["supply_order_id"] == supply_order_id), None
        )

        if not order:
            payload = {"error": f"Supply order {supply_order_id} not found"}
            out = json.dumps(payload)
            return out
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getSupplyOrderDetails",
                "description": "Get detailed information about a specific supply order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {
                            "type": "string",
                            "description": "Supply order ID to get details for",
                        }
                    },
                    "required": ["supply_order_id"],
                },
            },
        }
