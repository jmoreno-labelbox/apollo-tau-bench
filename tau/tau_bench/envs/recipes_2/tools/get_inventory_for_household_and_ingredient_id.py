# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryForHouseholdAndIngredientId(Tool):
    """Retrieves all inventory items for a given household ID and a specific ingredient ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        ingredient_id = kwargs.get("ingredient_id")

        if household_id is None or ingredient_id is None:
            return json.dumps({"error": "household_id and ingredient_id parameters are required."})

        inventory = list(data.get("inventory_items", {}).values())
        
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
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID of the household.",
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient to find in the inventory.",
                        }
                    },
                    "required": ["household_id", "ingredient_id"],
                },
            },
        }
