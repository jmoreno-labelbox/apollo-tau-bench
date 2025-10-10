# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventoryReservedQuantity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get('inventory_id')
        change_amount = kwargs.get('change_amount')
        inventory_items = list(data.get("inventory", {}).values())
        updated_item = None
        for item in inventory_items:
            if item.get("id") == inventory_id:
                item["reserved_quantity"] = item.get("reserved_quantity", 0) + change_amount
                updated_item = item
                break
        return json.dumps({"updated_inventory_item": updated_item})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_reserved_quantity",
                "description": "Updates the reserved quantity for an inventory item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Unique identifier of the inventory item to update.",
                        },
                        "change_amount": {
                            "type": "integer",
                            "description": "The amount to change the reserved quantity by (positive for add, negative for remove).",
                        },
                    },
                    "required": ["inventory_id", "change_amount"],
                },
            },
        }
