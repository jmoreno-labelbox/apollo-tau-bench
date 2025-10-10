# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGroceryListItemsByListIdAndIngredientId(Tool):
    """Retrieves grocery list items from a specific list that match a given ingredient ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        ingredient_id = kwargs.get("ingredient_id")

        if list_id is None or ingredient_id is None:
            return json.dumps({"error": "list_id and ingredient_id parameters are required."})

        grocery_list_items = data.get("grocery_list_items", [])
        
        matching_items = [
            item for item in grocery_list_items 
            if item.get("list_id") == list_id and item.get("ingredient_id") == ingredient_id
        ]
        
        return json.dumps(matching_items)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grocery_list_items_by_list_id_and_ingredient_id",
                "description": "Retrieves grocery list items from a specific list that match a given ingredient ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "integer",
                            "description": "The unique ID of the grocery list.",
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient to find on the list.",
                        }
                    },
                    "required": ["list_id", "ingredient_id"],
                },
            },
        }
