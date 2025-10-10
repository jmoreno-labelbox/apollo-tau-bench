# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRecipeIngredients(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_id: int) -> str:
        rows = [
            r
            for r in data.get("recipe_ingredients", [])
            if int(r.get("recipe_id")) == int(recipe_id)
        ]
        return json({"recipe_ingredients": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_recipe_ingredients",
                "description": "List recipe_ingredients for a recipe.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }
