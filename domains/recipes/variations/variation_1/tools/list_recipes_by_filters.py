from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListRecipesByFilters(Tool):
    """Enumerate recipe_ids (in JSON string format) that correspond to a filter_token."""

    @staticmethod
    def invoke(data: dict[str, Any], filter_token: str = None, no_heat: Any = None) -> str:
        if not filter_token:
            return _json_dump({"error": "filter_token is required"})
        try:
            parts = filter_token.split(":")
            meal_type = parts[1]
            min_protein = int(parts[2][1:])
            pf = parts[3] == "PF1"
            ex = parts[4][2:] if len(parts) > 4 else ""
            excluded = {c for c in ex.split(",") if c} if ex else set()
        except Exception:
            return _json_dump({"error": "invalid filter_token"})
        out = []
        for r in data.get("recipes", []):
            if str(r.get("meal_type")) != meal_type:
                continue
            if int(r.get("protein_g_per_serving", 0)) < min_protein:
                continue
            if pf and not bool(r.get("is_peanut_free", False)):
                continue
            if excluded and str(r.get("cuisine")) in excluded:
                continue
            out.append(int(r.get("recipe_id")))
        return _json_dump({"candidate_recipe_ids_json": json.dumps(out)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListRecipesByFilters",
                "description": "List recipe_ids (as JSON string) matching a filter token.",
                "parameters": {
                    "type": "object",
                    "properties": {"filter_token": {"type": "string"}},
                    "required": ["filter_token"],
                },
            },
        }
