from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateInventoryQuantity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str, new_quantity: int) -> str:
        inventory = data.get("inventory", [])

        for i, inv_record in enumerate(inventory):
            if inv_record.get("id") == inventory_id:
                inventory[i]["quantity"] = new_quantity
                inventory[i]["updated_at"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                data["inventory"] = inventory
                payload = inventory[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Inventory record with ID {inventory_id} not found."}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateInventoryQuantity",
                "description": "Update the quantity of an inventory record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Unique identifier of the inventory record.",
                        },
                        "new_quantity": {
                            "type": "integer",
                            "description": "New quantity for the inventory record.",
                        },
                    },
                    "required": ["inventory_id", "new_quantity"],
                },
            },
        }
