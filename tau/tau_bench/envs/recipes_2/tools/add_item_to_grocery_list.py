from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddItemToGroceryList(Tool):
    """Inserts a new item into a grocery list."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, ingredient_id: int = None, quantity: float = None, unit: str = None) -> str:
        items = data.get("grocery_list_items", [])
        # Automatically create the next item_id
        new_id = max([item.get("item_id", 0) for item in items]) + 1 if items else 8101

        ingredients = data.get("ingredients", [])
        ingredient_info = next(
            (ing for ing in ingredients if ing["ingredient_id"] == ingredient_id), None
        )
        if not ingredient_info:
            payload = {"error": f"Ingredient {ingredient_id} not found."}
            out = json.dumps(payload)
            return out

        new_item = {
            "item_id": new_id,
            "list_id": list_id,
            "ingredient_id": ingredient_id,
            "quantity": quantity,
            "unit": unit,
            "grocery_section": ingredient_info.get("grocery_section"),
            "pantry_staple_flag": ingredient_info.get("pantry_staple_flag"),
            "overlap_last_month_flag": False,
        }
        data["grocery_list_items"].append(new_item)
        payload = new_item
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddItemToGroceryList",
                "description": "Adds a new item to a grocery list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "ingredient_id": {"type": "integer"},
                        "quantity": {"type": "number"},
                        "unit": {"type": "string"},
                    },
                    "required": ["list_id", "ingredient_id", "quantity", "unit"],
                },
            },
        }
