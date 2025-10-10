# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOutboundOrderStatus(Tool):
    """Tool to get the status of an outbound order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        """Execute the tool with given parameters."""
        orders = data.get("outbound_orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                return json.dumps(order, indent=2)
        return json.dumps({"error": f"Order with ID {order_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_outbound_order_status",
                "description": "Retrieves the current status and details of a specific outbound customer order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to look up."}
                    },
                    "required": ["order_id"],
                },
            },
        }
