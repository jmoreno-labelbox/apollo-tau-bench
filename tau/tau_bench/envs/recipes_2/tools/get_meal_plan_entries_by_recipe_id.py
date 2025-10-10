# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMealPlanEntriesByRecipeId(Tool):
    """Retrieves all meal plan entries that use a specific recipe ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_id) -> str:
        if recipe_id is None:
            return json.dumps({"error": "recipe_id parameter is required."})
        meal_plan_entries = list(data.get("meal_plan_entries", {}).values())
        matching_entries = [entry for entry in meal_plan_entries if entry.get("recipe_id") == recipe_id]
        return json.dumps(matching_entries)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_meal_plan_entries_by_recipe_id",
                "description": "Retrieves all meal plan entries that use a specific recipe ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer", "description": "The unique ID of the recipe to find in meal plans."}},
                    "required": ["recipe_id"],
                },
            },
        }
