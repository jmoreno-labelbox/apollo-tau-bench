from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListRecipeIngredients(Tool):
    """Retrieve combined recipe_ingredients for a recipe_id along with ingredient metadata."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_id: int = None) -> str:
        if recipe_id is None:
            return _json_dump({"error": "recipe_id is required"})
        rows = [
            r
            for r in data.get("recipe_ingredients", {}).values()
            if int(r.get("recipe_id")) == int(recipe_id)
        ]
        ingr_ix = _index_by(list(data.get("ingredients", {}).values()), "ingredient_id")
        out = []
        for ri in rows:
            iid = int(ri["ingredient_id"])
            meta = ingr_ix.get(iid, {}).values()
            out.append(
                {
                    **ri,
                    **{
                        "ingredient_name": meta.get("ingredient_name"),
                        "grocery_section": meta.get("grocery_section"),
                        "pantry_staple_flag": meta.get("pantry_staple_flag"),
                        "peanut_free_flag": meta.get("peanut_free_flag"),
                        "default_unit": meta.get("default_unit"),
                    },
                }
            )
        return _json_dump(out)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListRecipeIngredients",
                "description": "Join recipe_ingredients with ingredient metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }
