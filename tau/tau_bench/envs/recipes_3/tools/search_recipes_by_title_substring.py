# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchRecipesByTitleSubstring(Tool):
    """Searches for recipes with titles containing the specified text."""
    @staticmethod
    def invoke(data: Dict[str, Any], title_substring: str) -> str:
        if not title_substring:
            return json.dumps({"error": "title_substring parameter is required."})
        recipes = list(data.get("recipes", {}).values())
        matching_recipes = [
            recipe for recipe in recipes 
            if title_substring.lower() in recipe.get("recipe_title", "").lower()
        ]
        return json.dumps(matching_recipes)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_recipes_by_title_substring",
                "description": "Searches for recipes with titles containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title_substring": {"type": "string", "description": "The text to search for in recipe titles."}
                    },
                    "required": ["title_substring"],
                },
            },
        }
