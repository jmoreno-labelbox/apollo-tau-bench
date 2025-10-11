# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchIngredientsByName(Tool):
    """Searches for ingredients with names containing the specified text."""
    @staticmethod
    def invoke(data: Dict[str, Any], name_query: str) -> str:
        if not name_query:
            return json.dumps({"error": "name_query parameter is required."})
        ingredients = list(list(list(data.get("ingredients", {}).values())) if isinstance(data.get("ingredients"), dict) else data.get("ingredients", []))
        matching_ingredients = [
            ingredient for ingredient in ingredients 
            if name_query.lower() in ingredient.get("ingredient_name", "").lower()
        ]
        return json.dumps(matching_ingredients)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_ingredients_by_name",
                "description": "Searches for ingredients with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {"type": "string", "description": "The text to search for in ingredient names."}
                    },
                    "required": ["name_query"],
                },
            },
        }
