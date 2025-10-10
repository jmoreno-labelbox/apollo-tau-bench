# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _first_user_id


class ExcludeRecentRecipes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        cand = _ids_from_kwargs_or_defaults(data, kwargs)
        recent = kwargs.get("recent_recipe_ids")
        if recent is None:
            days_back = int(kwargs.get("days_back", 14))
            anchor_date = kwargs.get("anchor_date")
            recent = _recent_recipe_ids(data, household_id, days_back, anchor_date)
        filtered = [rid for rid in cand if rid not in set(int(x) for x in recent)]
        return _json_dump({"filtered_recipe_ids_json": json.dumps(filtered)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"exclude_recent_recipes","description":"Remove recipes that appeared in recent history; defaults to last 14 days for default household.","parameters":{"type":"object","properties":{"candidate_recipe_ids_json":{"type":"string"},"filter_token":{"type":"string"},"meal_type":{"type":"string"},"min_protein_g":{"type":"integer"},"peanut_free":{"type":"boolean"},"recent_recipe_ids":{"type":"array","items":{"type":"integer"}},"household_id":{"type":"integer"},"days_back":{"type":"integer"},"anchor_date":{"type":"string"}},"required":[]}}}
