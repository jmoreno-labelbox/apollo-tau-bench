# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateOutboundOrder(Tool):
    """Tool to update outbound order details."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        updates = kwargs.get("updates")
        orders = data.get("outbound_orders", [])

        for order in orders:
            if order["order_id"] == order_id:
                order.update(updates)
                return json.dumps({"success": f"outbound order {order_id} updated"}, indent=2)
        return json.dumps({"error": f"order_id {order_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_outbound_order",
                "description": "Update outbound order by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The outbound order ID to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["order_id", "updates"]
                }
            }
        }
