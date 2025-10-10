# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrderDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        orders = data.get("outbound_orders", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)

        if not order:
            return json.dumps({"error": f"Order {order_id} not found"})

        return json.dumps(order)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Retrieve detailed information about a specific order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Order identifier"}
                    },
                    "required": ["order_id"]
                }
            }
        }
