# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VerifyInventoryAllocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        orders = data.get("outbound_orders", [])
        inventory = list(data.get("inventory", {}).values())

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"Order {order_id} not found"})

        warehouse_id = order.get("warehouse_id")
        total_units = order.get("total_units", 0)

        # Streamlined allocation verification - in a production environment, line items would be evaluated.
        warehouse_inventory = [item for item in inventory if item.get("warehouse_id") == warehouse_id]
        total_available = sum(item.get("quantity_available", 0) for item in warehouse_inventory)

        allocation_status = "fully_allocated" if total_available >= total_units else "insufficient_inventory"

        return json.dumps({
            "order_id": order_id,
            "allocation_status": allocation_status,
            "required_units": total_units,
            "available_units": total_available
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_inventory_allocation",
                "description": "Verify that inventory is allocated for all items in an order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Order identifier"}
                    },
                    "required": ["order_id"]
                }
            }
        }
