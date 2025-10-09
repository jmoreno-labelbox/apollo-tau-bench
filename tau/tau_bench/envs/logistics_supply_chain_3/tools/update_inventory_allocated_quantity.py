from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateInventoryAllocatedQuantity(Tool):
    """Modifies the allocated and available quantities for a product in a warehouse when an order is created."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, warehouse_id: str = None, quantity_to_allocate: int = None) -> str:
        inventory_items = data.get("inventory", {}).values()

        if not all([sku, warehouse_id, quantity_to_allocate]):
            payload = {"error": "SKU, warehouse ID, and quantity to allocate are required."}
            out = json.dumps(payload)
            return out

        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                available = item.get("quantity_available", 0)
                if available < quantity_to_allocate:
                    payload = {
                        "error": f"Insufficient quantity available. Available: {available}, Required: {quantity_to_allocate}"
                    }
                    out = json.dumps(payload)
                    return out

                original_allocated = item.get("quantity_allocated", 0)
                item["quantity_available"] = available - quantity_to_allocate
                item["quantity_allocated"] = original_allocated + quantity_to_allocate
                payload = {
                    "status": "success",
                    "inventory_id": item.get("inventory_id"),
                    "new_available_quantity": item["quantity_available"],
                    "new_allocated_quantity": item["quantity_allocated"],
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Inventory record not found to update"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryAllocatedQuantity",
                "description": "Allocates stock for an outbound order, decreasing available quantity and increasing allocated quantity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to allocate.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse from which to allocate.",
                        },
                        "quantity_to_allocate": {
                            "type": "integer",
                            "description": "The quantity of the product to allocate.",
                        },
                    },
                    "required": ["sku", "warehouse_id", "quantity_to_allocate"],
                },
            },
        }
