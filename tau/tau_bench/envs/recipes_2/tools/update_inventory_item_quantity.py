# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventoryItemQuantity(Tool):
    """Updates the quantity of an item in the household inventory."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inv_item_id = kwargs.get("inv_item_id")
        new_quantity = kwargs.get("new_quantity")
        inventory = list(data.get("inventory_items", {}).values())
        for item in inventory:
            if item.get("inv_item_id") == inv_item_id:
                item["quantity"] = new_quantity
                return json.dumps(item)
        return json.dumps({"error": f"Inventory item {inv_item_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_item_quantity",
                "description": "Updates the quantity of an item in the household inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inv_item_id": {"type": "integer"}, "new_quantity": {"type": "number"},
                    },
                    "required": ["inv_item_id", "new_quantity"],
                },
            },
        }
