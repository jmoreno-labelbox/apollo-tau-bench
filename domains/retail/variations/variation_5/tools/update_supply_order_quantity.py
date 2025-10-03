from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class UpdateSupplyOrderQuantity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None, new_quantity: int = None) -> str:
        if not supply_order_id or new_quantity is None:
            payload = {"error": "supply_order_id and new_quantity are required"}
            out = json.dumps(
                payload)
            return out

        if new_quantity < 0:
            payload = {"error": "Quantity cannot be negative"}
            out = json.dumps(payload)
            return out

        supply_orders = data["supply_orders"]
        order = next(
            (o for o in supply_orders if o["supply_order_id"] == supply_order_id), None
        )

        if not order:
            payload = {"error": f"Supply order {supply_order_id} not found"}
            out = json.dumps(payload)
            return out

        if order["status"] not in ["pending"]:
            payload = {
                    "error": f'Cannot update quantity for order with status: {order["status"]}'
                }
            out = json.dumps(
                payload)
            return out

        old_quantity = order["quantity"]
        old_total_cost = order["total_cost"]

        order["quantity"] = new_quantity
        order["total_cost"] = new_quantity * order["unit_cost"]
        payload = {
                "success": True,
                "supply_order_id": supply_order_id,
                "old_quantity": old_quantity,
                "new_quantity": new_quantity,
                "old_total_cost": old_total_cost,
                "new_total_cost": order["total_cost"],
                "updated_at": get_current_timestamp(),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSupplyOrderQuantity",
                "description": "Update the quantity of a pending supply order and recalculate total cost.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {
                            "type": "string",
                            "description": "Supply order ID to update",
                        },
                        "new_quantity": {
                            "type": "integer",
                            "description": "New quantity for the order",
                        },
                    },
                    "required": ["supply_order_id", "new_quantity"],
                },
            },
        }
