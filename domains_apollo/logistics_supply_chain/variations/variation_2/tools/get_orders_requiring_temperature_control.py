from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetOrdersRequiringTemperatureControl(Tool):
    """Utility for fetching orders that necessitate temperature regulation."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_ids: list[str] = None) -> str:
        orders = data.get("outbound_orders", [])
        result = [
            order["order_id"]
            for order in orders
            if order.get("temperature_control_required")
        ]
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        if len(result) == 0:
            payload = "No temperature control required"
            out = json.dumps(payload, indent=2)
            return out
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrdersRequiringTemperatureControl",
                "description": "Retrieve outbound orders with temperature control requirements.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of orders to choose from.",
                        }
                    },
                },
            },
        }
