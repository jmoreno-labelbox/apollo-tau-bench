# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventoryDamageStatus(Tool):
    """Updates the inventory count to move a number of units from 'available' to 'damaged'."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get('inventory_id')
        damaged_quantity = kwargs.get('damaged_quantity')

        if not all([inventory_id, damaged_quantity]):
            return json.dumps({"error": "inventory_id and damaged_quantity are required."}, indent=2)

        inventory_record = next((i for i in list(data.get('inventory', {}).values()) if i.get('inventory_id') == inventory_id), None)

        if not inventory_record:
            return json.dumps({"error": f"Inventory record '{inventory_id}' not found."}, indent=2)

        if damaged_quantity > 0:
            if damaged_quantity > inventory_record.get('quantity_available', 0):
                return json.dumps({"error": f"Cannot mark {damaged_quantity} as damaged, only {inventory_record.get('quantity_available')} are available."}, indent=2)
            inventory_record['quantity_available'] -= damaged_quantity
            inventory_record['quantity_damaged'] += damaged_quantity
        elif damaged_quantity < 0:
            abs_damaged_quantity = abs(damaged_quantity)

            inventory_record['quantity_available'] += abs_damaged_quantity

            if abs_damaged_quantity > inventory_record.get('quantity_damaged', 0):
                inventory_record['quantity_damaged'] = 0
            else:
                inventory_record['quantity_damaged'] -= abs_damaged_quantity
        else:
            pass

        return json.dumps(inventory_record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_damage_status",
                "description": "Updates an inventory record to reflect damaged goods by moving a quantity from 'available' to 'damaged'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {"type": "string", "description": "The ID of the inventory record to update."},
                        "damaged_quantity": {"type": "integer", "description": "The number of units to mark as damaged."}
                    },
                    "required": ["inventory_id", "damaged_quantity"]
                }
            }
        }
