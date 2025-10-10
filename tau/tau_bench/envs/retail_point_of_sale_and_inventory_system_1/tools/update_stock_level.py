# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateStockLevel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], inventory_id, quantity_to_add) -> str:
        inventory = list(data.get("inventory", {}).values())  # Ajustado para lista

        found_item = None
        for item in inventory:
            if item.get("id") == inventory_id:
                found_item = item
                break

        if found_item:
            found_item['quantity'] += quantity_to_add
            if found_item['quantity'] > found_item.get('reorder_level', 0):
                found_item['status'] = 'in_stock'
            elif found_item['quantity'] > 0:
                found_item['status'] = 'low_stock'
            else:
                found_item['status'] = 'out_of_stock'

            return json.dumps({
                "status": "success",
                "inventory_id": inventory_id,
                "new_quantity": found_item['quantity']
            })

        return json.dumps({"status": "error", "reason": "Inventory ID not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_stock_level",
                "description": "Updates the stock level for an inventory item, e.g., when receiving a shipment or correcting a count.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {"type": "string", "description": "The unique ID of the inventory item."},
                        "quantity_to_add": {"type": "integer", "description": "The number of units to add to the current quantity (can be negative)."},
                    },
                    "required": ["inventory_id", "quantity_to_add"],
                },
            },
        }
