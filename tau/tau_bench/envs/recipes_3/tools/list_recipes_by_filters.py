# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRecipesByFilters(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], filter_token: str) -> str:
        try:
            parts = filter_token.split(":")
            meal_type = parts[1]
            min_protein = int(parts[2][1:])
            pf = parts[3] == "PF1"
            ex = parts[4][2:] if len(parts) > 4 else ""
            excluded = set([c for c in ex.split(",") if c])
        except Exception:
            return json({"error": "invalid filter_token"})
        ids: List[int] = []
        for r in list(data.get("recipes", {}).values()):
            if str(r.get("meal_type")) != meal_type:
                continue
            if int(r.get("protein_g_per_serving", 0)) < min_protein:
                continue
            if pf and not bool(r.get("is_peanut_free", False)):
                continue
            if excluded and str(r.get("cuisine")) in excluded:
                continue
            ids.append(int(r.get("recipe_id")))
        return json({"candidate_recipe_ids": ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_recipes_by_filters",
                "description": "List recipe_ids matching a filter token.",
                "parameters": {
                    "type": "object",
                    "properties": {"filter_token": {"type": "string"}},
                    "required": ["filter_token"],
                },
            },
        }
