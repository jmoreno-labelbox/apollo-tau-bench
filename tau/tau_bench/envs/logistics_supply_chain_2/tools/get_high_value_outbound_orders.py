# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHighValueOutboundOrders(Tool):
    """Tool to retrieve outbound orders above a specified value."""

    @staticmethod
    def invoke(data: Dict[str, Any], list_of_ids = None, min_value = 100000) -> str:
        threshold = min_value
        list_of_orders = list_of_ids
        orders = list(data.get("outbound_orders", {}).values())
        result = [order['order_id'] for order in orders if order.get("total_value", 0) >= threshold]
        if list_of_orders:
            result = [r for r in result if r in list_of_orders]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_high_value_outbound_orders",
                "description": "Retrieve outbound orders where total value exceeds the given threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "min_value": {
                            "type": "number",
                            "description": "Minimum total value (default is 100000)"
                        },
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
