from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchRecipes(Tool):
    """Looks for recipes according to different parameters."""

    @staticmethod
    def invoke(data: dict[str, Any], cuisine: str = None, meal_type: str = None, is_peanut_free: bool = None) -> str:
        recipes = data.get("recipes", {}).values()
        results = []
        for recipe in recipes.values():
            match = True
            if cuisine and recipe.get("cuisine") != cuisine:
                match = False
            if meal_type and recipe.get("meal_type") != meal_type:
                match = False
            if (
                is_peanut_free is not None
                and recipe.get("is_peanut_free") != is_peanut_free
            ):
                match = False
            if match:
                results.append(recipe)
        payload = results
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchRecipes",
                "description": "Searches for recipes based on various criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cuisine": {
                            "type": "string",
                            "description": "The cuisine of the recipe (e.g., Italian, Mexican).",
                        },
                        "meal_type": {
                            "type": "string",
                            "description": "The type of meal (e.g., Dinner, Lunch).",
                        },
                        "is_peanut_free": {
                            "type": "boolean",
                            "description": "Filter for peanut-free recipes.",
                        },
                    },
                },
            },
        }
