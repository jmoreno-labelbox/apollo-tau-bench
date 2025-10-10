# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryForHouseholdAndIngredientId(Tool):
    """Retrieves inventory items for a specific household and ingredient."""
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, ingredient_id: int) -> str:
        if household_id is None or ingredient_id is None:
            return json.dumps({"error": "household_id and ingredient_id parameters are required."})
        inventory = data.get("inventory_items", [])
        household_ingredient_inventory = [
            item for item in inventory 
            if item.get("household_id") == household_id and item.get("ingredient_id") == ingredient_id
        ]
        return json.dumps(household_ingredient_inventory)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_for_household_and_ingredient_id",
                "description": "Retrieves inventory items for a specific household and ingredient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer", "description": "The unique ID of the household."},
                        "ingredient_id": {"type": "integer", "description": "The unique ID of the ingredient."}
                    },
                    "required": ["household_id", "ingredient_id"],
                },
            },
        }
