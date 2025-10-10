# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrderPaymentHistory(Tool):
    """Return payment transactions for an order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        orders = list(data.get("orders", {}).values())
        for order in orders:
            if order.get("order_id") == order_id:
                return json.dumps({"order_id": order_id, "payment_history": order.get("payment_history", [])})
        return json.dumps({"error": "Order not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_payment_history",
                "description": "Get the payment_history array for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"}
                    },
                    "required": ["order_id"]
                }
            }
        }
