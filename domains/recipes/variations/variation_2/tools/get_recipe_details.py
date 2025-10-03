from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class GetRecipeDetails(Tool):
    """Fetches complete information for a particular recipe ID."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: str = None) -> str:
        recipes = data.get("recipes", [])
        for recipe in recipes:
            if recipe.get("recipe_id") == recipe_id:
                payload = recipe
                out = json.dumps(payload)
                return out
        payload = {"error": f"Recipe with ID '{recipe_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRecipeDetails",
                "description": "Retrieves the full details for a specific recipe ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_id": {
                            "type": "integer",
                            "description": "The unique ID of the recipe.",
                        }
                    },
                    "required": ["recipe_id"],
                },
            },
        }
