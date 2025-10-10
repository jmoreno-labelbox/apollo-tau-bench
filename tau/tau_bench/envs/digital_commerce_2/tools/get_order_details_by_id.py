# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrderDetailsById(Tool):
    """Fetch full order details by order_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: Any) -> str:
        order_id = _idstr(order_id)
        if not order_id:
            return json.dumps({"error": "Missing required field: order_id"}, indent=2)
        orders = list(data.get("orders", {}).values())
        for order in orders:
            if order.get("order_id") == order_id:
                return json.dumps(order, indent=2)

        return json.dumps({"error": f"No order found with ID '{order_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_details_by_id",
                "description": "Fetch full order details by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Exact order ID to retrieve."}
                    },
                    "required": ["order_id"],
                },
            },
        }
