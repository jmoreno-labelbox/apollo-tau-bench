from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetRecipeDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: int) -> str:
        recipes = _get_table(data, "recipes")
        row = next((r for r in recipes if r.get("recipe_id") == recipe_id), None)
        payload = {"recipe": row}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRecipeDetails",
                "description": "Returns the recipe row for recipe_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }
