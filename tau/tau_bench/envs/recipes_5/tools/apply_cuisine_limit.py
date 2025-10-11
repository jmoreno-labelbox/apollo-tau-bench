# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump








def _recipe_by_id(data: Dict[str, Any], recipe_id: int) -> Optional[Dict[str, Any]]:
    return next((r for r in data.get("recipes", []) if r.get("recipe_id") == recipe_id), None)

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _ids_from_kwargs_or_defaults(data: Dict[str, Any], kwargs: Dict[str, Any]) -> List[int]:
    ids = _parse_json_list_ids(kwargs.get("recipe_ids_json") or kwargs.get("candidate_recipe_ids_json"))
    if ids:
        return ids
    ft = kwargs.get("filter_token")
    if ft:
        meal, mp, pf = _decode_filter_token(ft)
        return _all_recipe_ids_filtered(data, meal, mp, pf)
    meal = kwargs.get("meal_type", "Dinner")
    mp = int(kwargs.get("min_protein_g", 0))
    pf = bool(kwargs.get("peanut_free", False))
    return _all_recipe_ids_filtered(data, meal, mp, pf)

class ApplyCuisineLimit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], max_per_cuisine = 2) -> str:
        ids = _ids_from_kwargs_or_defaults(data, kwargs)
        max_per_cuisine = int(max_per_cuisine)
        cuisine_counts: Dict[str, int] = {}
        selected: List[int] = []
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            cz = r.get("cuisine", "Unknown")
            cnt = cuisine_counts.get(cz, 0)
            if cnt < max_per_cuisine:
                selected.append(rid)
                cuisine_counts[cz] = cnt + 1
        return _json_dump({"cuisine_limited_recipe_ids_json": json.dumps(selected)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"apply_cuisine_limit","description":"Limit a list of recipes to at most N per cuisine; defaults to 2 and Dinner pool if none provided.","parameters":{"type":"object","properties":{"recipe_ids_json":{"type":"string"},"filter_token":{"type":"string"},"meal_type":{"type":"string"},"min_protein_g":{"type":"integer"},"peanut_free":{"type":"boolean"},"max_per_cuisine":{"type":"integer"}},"required":[]}}}