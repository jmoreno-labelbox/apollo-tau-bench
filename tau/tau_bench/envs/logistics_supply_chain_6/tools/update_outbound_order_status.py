# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateOutboundOrderStatus(Tool):
    """Tool to update the status of an outbound order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, new_status: str, tracking_number: Optional[str] = None, carrier_id: Optional[str] = None) -> str:
        """Execute the tool with given parameters."""
        orders = data.get("outbound_orders", [])
        inventory = list(data.get("inventory", {}).values())
        for order in orders:
            if order.get("order_id") == order_id:
                order["status"] = new_status
                if tracking_number:
                    order["tracking_number"] = tracking_number
                if carrier_id:
                    order["carrier_id"] = carrier_id

                # Upon shipment, reduce the on_hand and allocated quantities.
                if new_status.lower() == "shipped" and "items" in order:
                    warehouse_id = order["warehouse_id"]
                    for item in order["items"]:
                        sku = item["sku"]
                        quantity = item["quantity"]
                        for inv_item in inventory:
                            if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                                inv_item["quantity_on_hand"] -= quantity
                                inv_item["quantity_allocated"] -= quantity
                                break

                return json.dumps({"order_id": order_id, "new_status": new_status}, indent=2)
        return json.dumps({"error": f"Order with ID {order_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "update_outbound_order_status",
                "description": "Updates the status of an outbound order (e.g., to 'Shipped'). If shipping, adjusts inventory and adds tracking info.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to update."},
                        "new_status": {"type": "string", "description": "The new status (e.g., 'Processing', 'Shipped', 'Delivered', 'Cancelled')."},
                        "tracking_number": {"type": "string", "description": "The tracking number, if the order is being shipped."},
                        "carrier_id": {"type": "string", "description": "The ID of the carrier, if the order is being shipped."}
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }
