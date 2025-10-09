from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class MinimizeNewIngredients(Tool):
    """Retain only recipes with a non-staple ingredient count ≤ cap."""
    @staticmethod
    def invoke(data: dict[str, Any], recipe_ids_json: str = "[]", max_new_ingredients_per_recipe: int = 3) -> str:
        ids = _parse_json_list_ids(recipe_ids_json)
        kept: list[int] = []
        for rid in ids:
            rows = [
                r
                for r in data.get("recipe_ingredients", {}).values()
                if int(r.get("recipe_id")) == rid
            ]
            non_staples = 0
            for ri in rows:
                ing = _ingredient_by_id(data, int(ri["ingredient_id"]))
                if not ing or not bool(ing.get("pantry_staple_flag", False)):
                    non_staples += 1
            if non_staples <= max_new_ingredients_per_recipe:
                kept.append(rid)
        return _json_dump({"minimized_recipe_ids_json": json.dumps(kept)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MinimizeNewIngredients",
                "description": "Filter recipes by maximum non-staple ingredient count.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids_json": {"type": "string"},
                        "max_new_ingredients_per_recipe": {"type": "integer"},
                    },
                    "required": ["recipe_ids_json", "max_new_ingredients_per_recipe"],
                },
            },
        }
