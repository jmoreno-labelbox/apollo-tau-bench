# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump






def _parse_json_list_ids(json_str: str) -> List[int]:
    try:
        arr = json.loads(json_str)
        if isinstance(arr, list):
            return [int(x) for x in arr]
    except Exception:
        pass
    return []

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

class ExcludeRecipeIds(Tool):
    """Remove any recipe_ids that appear in a provided exclusion list."""
    @staticmethod
    def invoke(data: Dict[str, Any], candidate_recipe_ids_json = "[]", exclude_recipe_ids = []) -> str:
        candidates_json = candidate_recipe_ids_json
        exclude_ids = exclude_recipe_ids
        cand = _parse_json_list_ids(candidates_json)
        exset = set(int(x) for x in (exclude_ids or []))
        out = [rid for rid in cand if rid not in exset]
        return _json_dump({"filtered_recipe_ids_json": json.dumps(out)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"exclude_recipe_ids",
            "description":"Return candidates minus provided recipe_ids.",
            "parameters":{"type":"object","properties":{
                "candidate_recipe_ids_json":{"type":"string"},
                "exclude_recipe_ids":{"type":"array","items":{"type":"integer"}}
            },"required":["candidate_recipe_ids_json","exclude_recipe_ids"]}
        }}