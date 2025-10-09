from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetGroceryListItemsByListIdAndIngredientId(Tool):
    """Fetches items from a specific grocery list that correspond to a particular ingredient ID."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: str = None, ingredient_id: str = None) -> str:
        if list_id is None or ingredient_id is None:
            payload = {"error": "list_id and ingredient_id parameters are required."}
            out = json.dumps(payload)
            return out

        grocery_list_items = data.get("grocery_list_items", [])

        matching_items = [
            item
            for item in grocery_list_items
            if item.get("list_id") == list_id
            and item.get("ingredient_id") == ingredient_id
        ]
        payload = matching_items
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGroceryListItemsByListIdAndIngredientId",
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
                        },
                    },
                    "required": ["list_id", "ingredient_id"],
                },
            },
        }
