# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrdersByStatus(Tool):
    """Tool to retrieve outbound orders by status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        list_of_orders = kwargs.get("list_of_ids", None)
        orders = data.get("outbound_orders", [])
        result = [order['order_id'] for order in orders if order["status"].lower() == status.lower()]
        if list_of_orders:
            result = [r for r in result if r in list_of_orders]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_orders_by_status",
                "description": "Retrieve all outbound orders with a given status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Status of the order (e.g., 'Shipped', 'Delivered')"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of orders to choose from."
                        }
                    },
                    "required": ["status"]
                }
            }
        }
