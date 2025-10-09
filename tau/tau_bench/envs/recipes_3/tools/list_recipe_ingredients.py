from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListRecipeIngredients(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: int) -> str:
        ri = _get_table(data, "recipe_ingredients")
        rows = [x for x in ri if x.get("recipe_id") == recipe_id]
        payload = {"recipe_ingredients": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRecipeIngredients",
                "description": "Returns recipe_ingredients rows for recipe_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }
