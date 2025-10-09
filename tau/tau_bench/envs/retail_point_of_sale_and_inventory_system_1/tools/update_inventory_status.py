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

class UpdateInventoryStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, status: str = None) -> str:
        inventory_items = data.get("inventory", [])
        updated_item = None
        for item in inventory_items:
            if item.get("id") == inventory_id:
                item["status"] = status
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
                "name": "UpdateInventoryStatus",
                "description": "Updates the status of an inventory item (e.g., 'in_stock', 'low_stock', 'out_of_stock', 'critical').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Unique identifier of the inventory item to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status of the inventory item.",
                        },
                    },
                    "required": ["inventory_id", "status"],
                },
            },
        }
