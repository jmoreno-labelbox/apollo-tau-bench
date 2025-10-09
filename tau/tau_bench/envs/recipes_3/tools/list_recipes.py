from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListRecipes(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        meal_type: str = None,
        cuisine: str = None,
        peanut_free: bool = None,
        min_protein_g: float = None,
        no_heat_required: bool = None,
        minimal_prep: bool = None
    ) -> str:
        recipes = _get_table(data, "recipes")
        rows = recipes
        if meal_type:
            rows = [r for r in rows if r.get("meal_type") == meal_type]
        if cuisine:
            rows = [r for r in rows if r.get("cuisine") == cuisine]
        if peanut_free is True:
            rows = [r for r in rows if r.get("is_peanut_free") is True]
        if isinstance(min_protein_g, (int, float)):
            rows = [
                r for r in rows if (r.get("protein_g_per_serving") or 0) >= min_protein_g
            ]
        if no_heat_required is True:
            rows = [r for r in rows if (r.get("cook_minutes") or 0) == 0]
        if minimal_prep is True:
            rows = [r for r in rows if (r.get("prep_minutes") or 999) <= 10]
        payload = {"recipes": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRecipes",
                "description": "Lists recipes filtered by fields (meal_type, cuisine, peanut_free, min_protein_g, no_heat_required, minimal_prep).",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }
