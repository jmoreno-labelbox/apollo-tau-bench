# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FlagOverlapLastMonthOnList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        household_id = kwargs.get("household_id")
        anchor_date = kwargs.get("anchor_date")
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        if list_id is None:
            list_id = _latest_list_id(data, household_id)
        if list_id is None or household_id is None:
            return _json_dump({"updated_items": 0})
        recent_ingrs = set([row["ingredient_id"] for row in _collect_recipe_ingredients(data, _recent_recipe_ids(data, household_id, 30, anchor_date))])
        cnt = 0
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            item["overlap_last_month_flag"] = int(item.get("ingredient_id")) in recent_ingrs
            cnt += 1
        return _json_dump({"updated_items": cnt})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"flag_overlap_last_month_on_list","description":"Mark grocery items that overlap with last 30 days; defaults to latest list and household.","parameters":{"type":"object","properties":{"list_id":{"type":"integer"},"household_id":{"type":"integer"},"anchor_date":{"type":"string"}},"required":[]}}}
