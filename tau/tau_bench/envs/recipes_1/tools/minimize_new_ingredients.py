# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MinimizeNewIngredients(Tool):
    """Keep only recipes whose non-staple ingredient count ≤ cap."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        recipe_ids_json = kwargs.get("recipe_ids_json", "[]")
        max_new = int(kwargs.get("max_new_ingredients_per_recipe", 3))
        ids = _parse_json_list_ids(recipe_ids_json)
        kept: List[int] = []
        for rid in ids:
            rows = [r for r in data.get("recipe_ingredients", []) if int(r.get("recipe_id")) == rid]
            non_staples = 0
            for ri in rows:
                ing = _ingredient_by_id(data, int(ri["ingredient_id"]))
                if not ing or not bool(ing.get("pantry_staple_flag", False)):
                    non_staples += 1
            if non_staples <= max_new:
                kept.append(rid)
        return _json_dump({"minimized_recipe_ids_json": json.dumps(kept)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"minimize_new_ingredients",
            "description":"Filter recipes by maximum non-staple ingredient count.",
            "parameters":{"type":"object","properties":{
                "recipe_ids_json":{"type":"string"},
                "max_new_ingredients_per_recipe":{"type":"integer"}
            },"required":["recipe_ids_json","max_new_ingredients_per_recipe"]}
        }}
