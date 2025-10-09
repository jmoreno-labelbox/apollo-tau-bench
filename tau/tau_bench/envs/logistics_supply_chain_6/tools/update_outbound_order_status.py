from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateOutboundOrderStatus(Tool):
    """Utility for modifying the status of an outbound order."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        new_status: str,
        tracking_number: str | None = None,
        carrier_id: str | None = None
    ) -> str:
        """Run the tool with the provided parameters."""
        _new_statusL = new_status or ''.lower()
        pass
        orders = data.get("outbound_orders", {}).values()
        inventory = data.get("inventory", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                order["status"] = new_status
                if tracking_number:
                    order["tracking_number"] = tracking_number
                if carrier_id:
                    order["carrier_id"] = carrier_id

                # If dispatched, reduce on_hand and allocated amounts
                if new_status.lower() == "shipped" and "items" in order:
                    warehouse_id = order["warehouse_id"]
                    for item in order["items"]:
                        sku = item["sku"]
                        quantity = item["quantity"]
                        for inv_item in inventory.values():
                            if (
                                inv_item["warehouse_id"] == warehouse_id
                                and inv_item["sku"] == sku
                            ):
                                inv_item["quantity_on_hand"] -= quantity
                                inv_item["quantity_allocated"] -= quantity
                                break
                payload = {"order_id": order_id, "new_status": new_status}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Order with ID {order_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
        """Run the tool with the provided parameters."""
        _new_statusL = new_status or ''.lower()
        pass
        orders = data.get("outbound_orders", {}).values()
        inventory = data.get("inventory", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                order["status"] = new_status
                if tracking_number:
                    order["tracking_number"] = tracking_number
                if carrier_id:
                    order["carrier_id"] = carrier_id

                #If dispatched, reduce on_hand and allocated amounts
                if new_status.lower() == "shipped" and "items" in order:
                    warehouse_id = order["warehouse_id"]
                    for item in order["items"]:
                        sku = item["sku"]
                        quantity = item["quantity"]
                        for inv_item in inventory.values():
                            if (
                                inv_item["warehouse_id"] == warehouse_id
                                and inv_item["sku"] == sku
                            ):
                                inv_item["quantity_on_hand"] -= quantity
                                inv_item["quantity_allocated"] -= quantity
                                break
                payload = {"order_id": order_id, "new_status": new_status}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Order with ID {order_id} not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateOutboundOrderStatus",
                "description": "Updates the status of an outbound order (e.g., to 'Shipped'). If shipping, adjusts inventory and adds tracking info.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status (e.g., 'Processing', 'Shipped', 'Delivered', 'Cancelled').",
                        },
                        "tracking_number": {
                            "type": "string",
                            "description": "The tracking number, if the order is being shipped.",
                        },
                        "carrier_id": {
                            "type": "string",
                            "description": "The ID of the carrier, if the order is being shipped.",
                        },
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }
