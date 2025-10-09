from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CancelOutboundOrder(Tool):
    """Utility for voiding an outbound order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str, outbound_orders: list = None, inventory: list = None) -> str:
        """Run the tool using the specified parameters."""
        orders = outbound_orders if outbound_orders is not None else data.get("outbound_orders", {}).values()
        inventory = inventory if inventory is not None else data.get("inventory", {}).values()
        for order in orders:
            if order.get("order_id") == order_id:
                # if order["status"] is in ["Shipped", "Delivered"]:
                # return json.dumps({"error": f"Order {order_id} cannot be canceled due to status '{order['status']}'"}, indent=2)

                # Release allocated stock
                # warehouse_id is set to order["warehouse_id"]
                # for item in order["items"]:
                # sku is assigned from item["sku"]
                # quantity is taken from item["quantity"]
                # for inv_item in inventory:
                # if inv_item["warehouse_id"] matches warehouse_id and inv_item["sku"] matches sku:
                # inv_item["quantity_allocated"] is decreased by quantity
                # inv_item["quantity_available"] is increased by quantity
                # exit the loop

                order["status"] = "Cancelled"
                payload = {"order_id": order_id, "status": "Cancelled"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Order with ID {order_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "CancelOutboundOrder",
                "description": "Cancels a pending or processing outbound order and returns the allocated stock to available inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to cancel.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }
