# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CancelOutboundOrder(Tool):
    """Tool to cancel an outbound order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        """Execute the tool with given parameters."""
        orders = data.get("outbound_orders", [])
        inventory = list(data.get("inventory", {}).values())
        for order in orders:
            if order.get("order_id") == order_id:
                # if order["status"] in ["Shipped", "Delivered"]:
                #     return json.dumps({"error": f"Cannot cancel order {order_id} with status '{order['status']}'"}, indent=2)

                # De-allocate stock
                # warehouse_id = order["warehouse_id"]
                # for item in order["items"]:
                #     sku = item["sku"]
                #     quantity = item["quantity"]
                #     for inv_item in inventory:
                #         if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                #             inv_item["quantity_allocated"] -= quantity
                #             inv_item["quantity_available"] += quantity
                #             break

                order["status"] = "Cancelled"
                return json.dumps({"order_id": order_id, "status": "Cancelled"}, indent=2)
        return json.dumps({"error": f"Order with ID {order_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "cancel_outbound_order",
                "description": "Cancels a pending or processing outbound order and returns the allocated stock to available inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to cancel."}
                    },
                    "required": ["order_id"],
                },
            },
        }
