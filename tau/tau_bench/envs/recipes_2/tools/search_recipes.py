# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchRecipes(Tool):
    """Searches for recipes based on various criteria."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        recipes = list(data.get("recipes", {}).values())
        cuisine = kwargs.get("cuisine")
        meal_type = kwargs.get("meal_type")
        is_peanut_free = kwargs.get("is_peanut_free")
        results = []
        for recipe in recipes:
            match = True
            if cuisine and recipe.get("cuisine") != cuisine:
                match = False
            if meal_type and recipe.get("meal_type") != meal_type:
                match = False
            if is_peanut_free is not None and recipe.get("is_peanut_free") != is_peanut_free:
                match = False
            if match:
                results.append(recipe)
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_recipes",
                "description": "Searches for recipes based on various criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cuisine": {"type": "string", "description": "The cuisine of the recipe (e.g., Italian, Mexican)."},
                        "meal_type": {"type": "string", "description": "The type of meal (e.g., Dinner, Lunch)."},
                        "is_peanut_free": {"type": "boolean", "description": "Filter for peanut-free recipes."},
                    },
                },
            },
        }
