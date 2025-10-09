from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateStockLevel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, quantity_to_add: int = None) -> str:
        inventory = data.get("inventory", [])

        found_item = None
        for item in inventory:
            if item.get("id") == inventory_id:
                found_item = item
                break

        if found_item:
            found_item["quantity"] += quantity_to_add
            if found_item["quantity"] > found_item.get("reorder_level", 0):
                found_item["status"] = "in_stock"
            elif found_item["quantity"] > 0:
                found_item["status"] = "low_stock"
            else:
                found_item["status"] = "out_of_stock"
            payload = {
                "status": "success",
                "inventory_id": inventory_id,
                "new_quantity": found_item["quantity"],
            }
            out = json.dumps(payload)
            return out
        payload = {"status": "error", "reason": "Inventory ID not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateStockLevel",
                "description": "Updates the stock level for an inventory item, e.g., when receiving a shipment or correcting a count.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "The unique ID of the inventory item.",
                        },
                        "quantity_to_add": {
                            "type": "integer",
                            "description": "The number of units to add to the current quantity (can be negative).",
                        },
                    },
                    "required": ["inventory_id", "quantity_to_add"],
                },
            },
        }
