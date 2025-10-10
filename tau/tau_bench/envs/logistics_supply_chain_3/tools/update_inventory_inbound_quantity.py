# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventoryInboundQuantity(Tool):
    """Updates the inbound quantity for a specific product in a warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_items = list(data.get("inventory", {}).values())
        sku = kwargs.get("sku")
        warehouse_id = kwargs.get("warehouse_id")
        quantity_to_add = kwargs.get("quantity_to_add")
        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                original_inbound = item.get("quantity_inbound", 0)
                item["quantity_inbound"] = original_inbound + quantity_to_add
                return json.dumps(
                    {
                        "status": "success",
                        "inventory_id": item.get("inventory_id"),
                        "new_inbound_quantity": item["quantity_inbound"],
                    }
                )
        return json.dumps({"error": "Inventory record not found to update"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_inbound_quantity",
                "description": "Updates the inbound quantity for a specific product in a warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse.",
                        },
                        "quantity_to_add": {
                            "type": "integer",
                            "description": "The quantity to add to the inbound total.",
                        },
                    },
                    "required": ["sku", "warehouse_id", "quantity_to_add"],
                },
            },
        }
