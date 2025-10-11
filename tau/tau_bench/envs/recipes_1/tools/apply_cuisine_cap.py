# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump








def _recipe_by_id(data: Dict[str, Any], recipe_id: int) -> Optional[Dict[str, Any]]:
    return next((r for r in data.get("recipes", []) if int(r.get("recipe_id")) == recipe_id), None)

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

class ApplyCuisineCap(Tool):
    """Limit a list of recipe_ids to at most N per cuisine."""
    @staticmethod
    def invoke(data: Dict[str, Any], max_per_cuisine = 2, recipe_ids_json = "[]") -> str:
        max_per_cuisine = int(max_per_cuisine)
        ids = _parse_json_list_ids(recipe_ids_json)
        counts: Dict[str, int] = {}
        selected: List[int] = []
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            cz = str(r.get("cuisine"))
            c = counts.get(cz, 0)
            if c < max_per_cuisine:
                selected.append(rid)
                counts[cz] = c + 1
        return _json_dump({"cuisine_limited_recipe_ids_json": json.dumps(selected)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"apply_cuisine_cap",
            "description":"Apply a per-cuisine maximum to a recipe set.",
            "parameters":{"type":"object","properties":{
                "recipe_ids_json":{"type":"string"},
                "max_per_cuisine":{"type":"integer"}
            },"required":["recipe_ids_json","max_per_cuisine"]}
        }}