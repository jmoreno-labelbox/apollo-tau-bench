# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRecipeIngredients(Tool):
    """Retrieves all ingredients for a specific recipe ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        recipe_id = kwargs.get("recipe_id")
        recipe_ingredients = data.get("recipe_ingredients", [])
        ingredients = [ri for ri in recipe_ingredients if ri.get("recipe_id") == recipe_id]
        return json.dumps(ingredients)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_recipe_ingredients",
                "description": "Retrieves all ingredients for a specific recipe ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer", "description": "The unique ID of the recipe."}},
                    "required": ["recipe_id"],
                },
            },
        }
