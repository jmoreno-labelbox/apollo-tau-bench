from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchRecipesByTitleSubstring(Tool):
    """Looks for recipes whose titles include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], title_substring: str = None) -> str:
        if not title_substring:
            payload = {"error": "title_substring parameter is required."}
            out = json.dumps(payload)
            return out
        recipes = data.get("recipes", [])
        matching_recipes = [
            recipe
            for recipe in recipes
            if title_substring.lower() in recipe.get("recipe_title", "").lower()
        ]
        payload = matching_recipes
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchRecipesByTitleSubstring",
                "description": "Searches for recipes with titles containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title_substring": {
                            "type": "string",
                            "description": "The text to search for in recipe titles.",
                        }
                    },
                    "required": ["title_substring"],
                },
            },
        }
