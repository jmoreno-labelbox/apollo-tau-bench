# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump


class FlagOverlapLastMonthOnList(Tool):
    """Mark overlap_last_month_flag if ingredient appeared in recipes cooked in last 30 days."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        household_id = kwargs.get("household_id")
        anchor_date = kwargs.get("anchor_date")
        if list_id is None or household_id is None:
            return _json_dump({"error": "list_id and household_id are required"})
        lr = json.loads(ListRecentMealHistory.invoke(data, household_id=household_id, days_back=30, anchor_date=anchor_date))
        recent = [int(x) for x in lr.get("recent_recipe_ids", [])]
        ingr_recent = set(int(r["ingredient_id"]) for r in _collect_recipe_ingredients(data, recent))
        updated = 0
        for item in list(data.get("grocery_list_items", {}).values()):
            if int(item.get("list_id")) != int(list_id):
                continue
            item["overlap_last_month_flag"] = int(item.get("ingredient_id")) in ingr_recent
            updated += 1
        return _json_dump({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"flag_overlap_last_month_on_list",
            "description":"Set overlap flag for list items based on last 30 days of meals.",
            "parameters":{"type":"object","properties":{
                "list_id":{"type":"integer"},
                "household_id":{"type":"integer"},
                "anchor_date":{"type":"string"}
            },"required":["list_id","household_id"]}
        }}
