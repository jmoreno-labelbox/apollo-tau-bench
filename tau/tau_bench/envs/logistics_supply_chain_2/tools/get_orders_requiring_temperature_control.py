# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrdersRequiringTemperatureControl(Tool):
    """Tool to retrieve orders that require temperature control."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        orders = data.get("outbound_orders", [])
        list_of_orders = kwargs.get("list_of_ids", None)
        result = [order['order_id'] for order in orders if order.get("temperature_control_required")]
        if list_of_orders:
            result = [r for r in result if r in list_of_orders]
        if len(result) == 0:
            return json.dumps("No temperature control required", indent=2)
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_orders_requiring_temperature_control",
                "description": "Retrieve outbound orders with temperature control requirements.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of orders to choose from."
                        }
                    }
                }
            }
        }
