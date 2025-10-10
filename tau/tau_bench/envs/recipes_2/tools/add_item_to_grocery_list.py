# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddItemToGroceryList(Tool):
    """Adds a new item to a grocery list."""
    @staticmethod
    def invoke(data: Dict[str, Any], ingredient_id, list_id, quantity, unit) -> str:
        
        items = list(data.get("grocery_list_items", {}).values())
        # Auto-generate the subsequent item_id.
        new_id = max([item.get("item_id", 0) for item in items]) + 1 if items else 8101
        
        ingredients = list(data.get("ingredients", {}).values())
        ingredient_info = next((ing for ing in ingredients if ing["ingredient_id"] == ingredient_id), None)
        if not ingredient_info:
            return json.dumps({"error": f"Ingredient {ingredient_id} not found."})

        new_item = {
            "item_id": new_id,
            "list_id": list_id,
            "ingredient_id": ingredient_id,
            "quantity": quantity,
            "unit": unit,
            "grocery_section": ingredient_info.get("grocery_section"),
            "pantry_staple_flag": ingredient_info.get("pantry_staple_flag"),
            "overlap_last_month_flag": False
        }
        data["grocery_list_items"].append(new_item)
        return json.dumps(new_item)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_item_to_grocery_list",
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
