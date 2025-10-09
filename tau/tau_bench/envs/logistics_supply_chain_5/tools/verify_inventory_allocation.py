from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class VerifyInventoryAllocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, outbound_orders: list = None, inventory: list = None) -> str:
        orders = outbound_orders if outbound_orders is not None else data.get("outbound_orders", [])
        inventory = inventory if inventory is not None else data.get("inventory", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"Order {order_id} not found"})

        warehouse_id = order.get("warehouse_id")
        total_units = order.get("total_units", 0)

        # Basic allocation verification - a real system would assess line items
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
                "name": "VerifyInventoryAllocation",
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
