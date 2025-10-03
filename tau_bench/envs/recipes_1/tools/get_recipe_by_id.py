from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetRecipeById(Tool):
    """Retrieve a recipe row using its id."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: str = None) -> str:
        if recipe_id is None:
            return _json_dump({"error": "recipe_id is required"})
        row = _recipe_by_id(data, int(recipe_id))
        return _json_dump(row or {"error": f"recipe_id {recipe_id} not found"})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRecipeById",
                "description": "Return a recipe by recipe_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }
