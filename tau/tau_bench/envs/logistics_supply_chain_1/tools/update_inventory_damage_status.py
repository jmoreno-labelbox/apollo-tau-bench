from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateInventoryDamageStatus(Tool):
    """Modifies the inventory count to transfer a quantity of units from 'available' to 'damaged'."""

    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, damaged_quantity: int = None) -> str:
        if not all([inventory_id, damaged_quantity]):
            payload = {"error": "inventory_id and damaged_quantity are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        inventory_record = next(
            (
                i
                for i in data.get("inventory", [])
                if i.get("inventory_id") == inventory_id
            ),
            None,
        )

        if not inventory_record:
            payload = {"error": f"Inventory record '{inventory_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if damaged_quantity > 0:
            if damaged_quantity > inventory_record.get("quantity_available", 0):
                payload = {
                        "error": f"Cannot mark {damaged_quantity} as damaged, only {inventory_record.get('quantity_available')} are available."
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            inventory_record["quantity_available"] -= damaged_quantity
            inventory_record["quantity_damaged"] += damaged_quantity
        elif damaged_quantity < 0:
            abs_damaged_quantity = abs(damaged_quantity)

            inventory_record["quantity_available"] += abs_damaged_quantity

            if abs_damaged_quantity > inventory_record.get("quantity_damaged", 0):
                inventory_record["quantity_damaged"] = 0
            else:
                inventory_record["quantity_damaged"] -= abs_damaged_quantity
        else:
            pass
        payload = inventory_record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryDamageStatus",
                "description": "Updates an inventory record to reflect damaged goods by moving a quantity from 'available' to 'damaged'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "The ID of the inventory record to update.",
                        },
                        "damaged_quantity": {
                            "type": "integer",
                            "description": "The number of units to mark as damaged.",
                        },
                    },
                    "required": ["inventory_id", "damaged_quantity"],
                },
            },
        }
