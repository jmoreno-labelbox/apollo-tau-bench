# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExcludeRecipeIds(Tool):
    """Remove any recipe_ids that appear in a provided exclusion list."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidates_json = kwargs.get("candidate_recipe_ids_json", "[]")
        exclude_ids = kwargs.get("exclude_recipe_ids", [])
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
