# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MinimizeNewIngredients(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], recipe_ids: List[int], max_new_ingredients_per_recipe: int = 5
    ) -> str:
        kept: List[int] = []
        ri = data.get("recipe_ingredients", [])
        for rid in recipe_ids or []:
            rows = [r for r in ri if int(r.get("recipe_id")) == int(rid)]
            non_staples = 0
            for row in rows:
                ing = _ingredient_by_id(data, int(row.get("ingredient_id")))
                if not ing or not bool(ing.get("pantry_staple_flag", False)):
                    non_staples += 1
            if non_staples <= int(max_new_ingredients_per_recipe):
                kept.append(int(rid))
        return json.dumps({"minimized_recipe_ids": kept})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "minimize_new_ingredients",
                "description": "Keep recipes whose non-staple ingredient count is ≤ cap.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "max_new_ingredients_per_recipe": {"type": "integer"},
                    },
                    "required": ["recipe_ids", "max_new_ingredients_per_recipe"],
                },
            },
        }
