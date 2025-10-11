# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRecipeDetails(Tool):
    """Retrieves the full details for a specific recipe ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_id) -> str:
        recipes = data.get("recipes", [])
        for recipe in recipes:
            if recipe.get("recipe_id") == recipe_id:
                return json.dumps(recipe)
        return json.dumps({"error": f"Recipe with ID '{recipe_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_recipe_details",
                "description": "Retrieves the full details for a specific recipe ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer", "description": "The unique ID of the recipe."}},
                    "required": ["recipe_id"],
                },
            },
        }
