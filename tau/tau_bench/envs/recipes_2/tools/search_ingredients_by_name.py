from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchIngredientsByName(Tool):
    """Looks for ingredients whose names contain the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        if not name_query:
            payload = {"error": "name_query parameter is required."}
            out = json.dumps(payload)
            return out

        ingredients = data.get("ingredients", {}).values()

        matching_ingredients = [
            ingredient
            for ingredient in ingredients.values() if name_query.lower() in ingredient.get("ingredient_name", "").lower()
        ]
        payload = matching_ingredients
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchIngredientsByName",
                "description": "Searches for ingredients with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in ingredient names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }
