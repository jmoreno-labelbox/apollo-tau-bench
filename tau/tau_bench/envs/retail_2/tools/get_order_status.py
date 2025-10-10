# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrderStatus(Tool):
    """Return only the status of an order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        orders = list(data.get("orders", {}).values())
        for order in orders:
            if order.get("order_id") == order_id:
                return json.dumps({"order_id": order_id, "status": order.get("status")})
        return json.dumps({"error": "Order not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_status",
                "description": "Return the order status by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"}
                    },
                    "required": ["order_id"]
                }
            }
        }
