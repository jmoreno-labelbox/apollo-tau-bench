# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSupplyOrderStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supply_order_id: str, new_status: str, delivery_date: str = None) -> str:
        """
        Update supply order status for inventory management and procurement tracking

        Writes to: supply_orders.json (updates existing supply order status)
        """
        # Rule: Supply orders with status 'cancelled' require alternative sourcing and cannot be fulfilled
        valid_statuses = ["pending", "fulfilled", "cancelled"]
        if new_status not in valid_statuses:
            return json.dumps({
                "error": f"Invalid status '{new_status}'. Valid statuses: {', '.join(valid_statuses)}",
                "status": "failed"
            })

        # Find the supply order to update
        supply_orders = data.get("supply_orders", [])
        supply_order_to_update = None
        order_index = None

        for i, order in enumerate(supply_orders):
            if order.get("supply_order_id") == supply_order_id:
                supply_order_to_update = order
                order_index = i
                break

        if not supply_order_to_update:
            return json.dumps({"error": f"Supply order {supply_order_id} not found", "status": "failed"})

        # Rule: Supply orders must reference valid supplier_id and existing product_id
        supplier_id = supply_order_to_update.get("supplier_id")
        product_id = supply_order_to_update.get("product_id")

        if not supplier_id or not product_id:
            return json.dumps({
                "error": f"Supply order {supply_order_id} has invalid supplier or product reference",
                "status": "failed"
            })

        # WRITE OPERATION: Update supply order status in supply_orders.json
        old_status = supply_order_to_update.get("status")
        supply_order_to_update["status"] = new_status
        supply_order_to_update["last_updated"] = datetime.now().isoformat()

        # Add delivery information if provided and status is fulfilled
        if delivery_date and new_status == "fulfilled":
            supply_order_to_update["delivery_date"] = delivery_date
            supply_order_to_update["fulfilled_date"] = datetime.now().isoformat()

        # Track cancellation reason for alternative sourcing
        if new_status == "cancelled" and old_status != "cancelled":
            supply_order_to_update["cancelled_date"] = datetime.now().isoformat()
            supply_order_to_update["requires_alternative_sourcing"] = True

        # Update the supply order in the data structure
        data["supply_orders"][order_index] = supply_order_to_update

        # Calculate impact metrics
        quantity = supply_order_to_update.get("quantity", 0)
        total_cost = supply_order_to_update.get("total_cost", 0)

        result = {
            "status": "success",
            "supply_order_id": supply_order_id,
            "supplier_id": supplier_id,
            "product_id": product_id,
            "item_id": supply_order_to_update.get("item_id"),
            "status_change": {
                "previous_status": old_status,
                "new_status": new_status
            },
            "order_details": {
                "quantity": quantity,
                "total_cost": total_cost
            },
            "fulfillment_info": {
                "delivery_date": delivery_date,
                "fulfilled_date": supply_order_to_update.get("fulfilled_date")
            } if new_status == "fulfilled" else None,
            "requires_alternative_sourcing": supply_order_to_update.get("requires_alternative_sourcing", False),
            "last_updated": supply_order_to_update["last_updated"]
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_supply_order_status",
                "description": "Update supply order status for inventory management and procurement tracking",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string", "description": "Supply order identifier (e.g., '#SO9359')"},
                        "new_status": {"type": "string", "description": "New status (pending, fulfilled, cancelled)"},
                        "delivery_date": {"type": "string", "description": "Expected/actual delivery date (optional, ISO format)"}
                    },
                    "required": ["supply_order_id", "new_status"]
                }
            }
        }
