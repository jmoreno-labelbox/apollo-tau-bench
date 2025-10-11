# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump








def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _decode_filter_token(token: Optional[str]) -> Tuple[str, int, bool]:
    if not token:
        return ("Dinner", 0, False)
    try:
        _, meal_type, ppart, pfpart = token.split(":")
        min_protein = int(ppart[1:])
        pf = True if pfpart == "PF1" else False
        return (meal_type, min_protein, pf)
    except Exception:
        return ("Dinner", 0, False)

def _all_recipe_ids_filtered(data: Dict[str, Any], meal_type: str = "Dinner", min_protein_g: int = 0, peanut_free: bool = False) -> List[int]:
    out = []
    for r in data.get("recipes", []):
        if r.get("meal_type") != meal_type:
            continue
        if int(r.get("protein_g_per_serving", 0)) < int(min_protein_g):
            continue
        if peanut_free and not r.get("is_peanut_free", False):
            continue
        out.append(int(r.get("recipe_id")))
    return out

class ListRecipesByFilters(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], filter_token, meal_type = "Dinner", min_protein_g = 0, peanut_free = False) -> str:
        token = filter_token
        if token:
            meal_type, min_protein, pf = _decode_filter_token(token)
        else:
            min_protein = int(min_protein_g)
            pf = bool(peanut_free)
        out = _all_recipe_ids_filtered(data, meal_type, min_protein, pf)
        return _json_dump({"candidate_recipe_ids_json": json.dumps(out)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"list_recipes_by_filters","description":"List recipe_ids as JSON from a token or direct parameters.","parameters":{"type":"object","properties":{"filter_token":{"type":"string"},"meal_type":{"type":"string"},"min_protein_g":{"type":"integer"},"peanut_free":{"type":"boolean"}},"required":[]}}}