# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump






def _recipe_by_id(data: Dict[str, Any], recipe_id: int) -> Optional[Dict[str, Any]]:
    return next((r for r in data.get("recipes", []) if int(r.get("recipe_id")) == recipe_id), None)

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

class GetRecipeById(Tool):
    """Return a recipe row by id."""
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_id) -> str:
        if recipe_id is None:
            return _json_dump({"error": "recipe_id is required"})
        row = _recipe_by_id(data, int(recipe_id))
        return _json_dump(row or {"error": f"recipe_id {recipe_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "get_recipe_by_id",
            "description": "Return a recipe by recipe_id.",
            "parameters": {"type": "object", "properties": {"recipe_id": {"type": "integer"}}, "required": ["recipe_id"]}
        }}