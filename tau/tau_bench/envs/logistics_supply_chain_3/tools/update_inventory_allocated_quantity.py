# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventoryAllocatedQuantity(Tool):
    """Updates the allocated and available quantities for a product in a warehouse upon order creation."""

    @staticmethod
    def invoke(data: Dict[str, Any], quantity_to_allocate, sku, warehouse_id) -> str:
        inventory_items = list(data.get("inventory", {}).values())

        if not all([sku, warehouse_id, quantity_to_allocate]):
            return json.dumps(
                {"error": "SKU, warehouse ID, and quantity to allocate are required."}
            )

        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                available = item.get("quantity_available", 0)
                if available < quantity_to_allocate:
                    return json.dumps(
                        {
                            "error": f"Insufficient quantity available. Available: {available}, Required: {quantity_to_allocate}"
                        }
                    )

                original_allocated = item.get("quantity_allocated", 0)
                item["quantity_available"] = available - quantity_to_allocate
                item["quantity_allocated"] = original_allocated + quantity_to_allocate

                return json.dumps(
                    {
                        "status": "success",
                        "inventory_id": item.get("inventory_id"),
                        "new_available_quantity": item["quantity_available"],
                        "new_allocated_quantity": item["quantity_allocated"],
                    }
                )
        return json.dumps({"error": "Inventory record not found to update"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_allocated_quantity",
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
