from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class GetMealPlanEntriesByRecipeId(Tool):
    """Fetches all meal plan entries that incorporate a particular recipe ID."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: str = None) -> str:
        if recipe_id is None:
            payload = {"error": "recipe_id parameter is required."}
            out = json.dumps(payload)
            return out
        meal_plan_entries = data.get("meal_plan_entries", [])
        matching_entries = [
            entry for entry in meal_plan_entries if entry.get("recipe_id") == recipe_id
        ]
        payload = matching_entries
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMealPlanEntriesByRecipeId",
                "description": "Retrieves all meal plan entries that use a specific recipe ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID of the recipe to find in meal plans.",
                        }
                    },
                    "required": ["recipe_id"],
                },
            },
        }
