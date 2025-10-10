# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventoryQuantity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], inventory_id: str, new_quantity: int) -> str:
        inventory = list(data.get("inventory", {}).values())

        for i, inv_record in enumerate(inventory):
            if inv_record.get("id") == inventory_id:
                inventory[i]["quantity"] = new_quantity
                inventory[i]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data["inventory"] = inventory
                return json.dumps(inventory[i], indent=2)

        return json.dumps({"error": f"Inventory record with ID {inventory_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_quantity",
                "description": "Update the quantity of an inventory record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {"type": "string", "description": "Unique identifier of the inventory record."},
                        "new_quantity": {"type": "integer", "description": "New quantity for the inventory record."}
                    },
                    "required": ["inventory_id", "new_quantity"]
                }
            }
        }
