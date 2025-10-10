# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyCuisineLimit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ids = _ids_from_kwargs_or_defaults(data, kwargs)
        max_per_cuisine = int(kwargs.get("max_per_cuisine", 2))
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
