from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RemoveItemFromGroceryList(Tool):
    """Deletes an item from a grocery list using its item ID."""

    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None) -> str:
        if item_id is None:
            payload = {"error": "item_id parameter is required."}
            out = json.dumps(payload)
            return out

        items = data.get("grocery_list_items", [])
        original_count = len(items)
        # Exclude the item that has the corresponding ID
        data["grocery_list_items"] = [
            item for item in items if item.get("item_id") != item_id
        ]

        if len(data["grocery_list_items"]) < original_count:
            payload = {
                "status": "success",
                "message": f"Item {item_id} removed from grocery list.",
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"Item with ID '{item_id}' not found on any grocery list."}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveItemFromGroceryList",
                "description": "Removes an item from a grocery list by its item ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "integer",
                            "description": "The unique ID of the grocery list item to remove.",
                        }
                    },
                    "required": ["item_id"],
                },
            },
        }
