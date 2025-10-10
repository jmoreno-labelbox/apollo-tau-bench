# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveItemFromGroceryList(Tool):
    """Removes an item from a grocery list by its item ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_id = kwargs.get("item_id")
        if item_id is None:
            return json.dumps({"error": "item_id parameter is required."})

        items = list(data.get("grocery_list_items", {}).values())
        original_count = len(items)
        # Remove the item that has the corresponding ID.
        data["grocery_list_items"] = [item for item in items if item.get("item_id") != item_id]

        if len(data["grocery_list_items"]) < original_count:
            return json.dumps({"status": "success", "message": f"Item {item_id} removed from grocery list."})
        else:
            return json.dumps({"error": f"Item with ID '{item_id}' not found on any grocery list."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_item_from_grocery_list",
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
