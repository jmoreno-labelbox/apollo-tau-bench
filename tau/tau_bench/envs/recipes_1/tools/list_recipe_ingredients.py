# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRecipeIngredients(Tool):
    """Return joined recipe_ingredients for a recipe_id with ingredient metadata."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        recipe_id = kwargs.get("recipe_id")
        if recipe_id is None:
            return _json_dump({"error": "recipe_id is required"})
        rows = [r for r in list(data.get("recipe_ingredients", {}).values()) if int(r.get("recipe_id")) == int(recipe_id)]
        ingr_ix = _index_by(list(data.get("ingredients", {}).values()), "ingredient_id")
        out = []
        for ri in rows:
            iid = int(ri["ingredient_id"])
            meta = ingr_ix.get(iid, {})
            out.append({**ri, **{
                "ingredient_name": meta.get("ingredient_name"),
                "grocery_section": meta.get("grocery_section"),
                "pantry_staple_flag": meta.get("pantry_staple_flag"),
                "peanut_free_flag": meta.get("peanut_free_flag"),
                "default_unit": meta.get("default_unit"),
            }})
        return _json_dump(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "list_recipe_ingredients",
            "description": "Join recipe_ingredients with ingredient metadata.",
            "parameters": {"type": "object", "properties": {"recipe_id": {"type": "integer"}}, "required": ["recipe_id"]}
        }}
