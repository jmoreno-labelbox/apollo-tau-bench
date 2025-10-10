# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOutboundOrderById(Tool):
    """Tool to retrieve an outbound order by order ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        orders = list(data.get("outbound_orders", {}).values())
        for order in orders:
            if order["order_id"] == order_id:
                return json.dumps(order, indent=2)
        return json.dumps({"error": f"Order with ID {order_id} not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_outbound_order_by_id",
                "description": "Retrieve outbound order using order ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order ID (e.g., 'ORD-0004')"
                        }
                    },
                    "required": ["order_id"]
                }
            }
        }
