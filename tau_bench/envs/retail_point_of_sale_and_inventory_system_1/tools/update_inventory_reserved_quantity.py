from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class UpdateInventoryReservedQuantity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, change_amount: int = None) -> str:
        inventory_items = data.get("inventory", [])
        updated_item = None
        for item in inventory_items:
            if item.get("id") == inventory_id:
                item["reserved_quantity"] = (
                    item.get("reserved_quantity", 0) + change_amount
                )
                updated_item = item
                break
        payload = {"updated_inventory_item": updated_item}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryReservedQuantity",
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
