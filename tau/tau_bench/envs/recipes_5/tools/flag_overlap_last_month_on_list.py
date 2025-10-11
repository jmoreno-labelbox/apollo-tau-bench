# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id














def _recent_recipe_ids(data: Dict[str, Any], household_id: Optional[int], days_back: int = 14, anchor_date: Optional[str] = None) -> List[int]:
    if household_id is None:
        return []
    if anchor_date:
        y, m, d = [int(x) for x in str(anchor_date).split("-")]
        end = date(y, m, d)
    else:
        hh_rows = [h for h in data.get("meal_history", []) if h.get("household_id") == household_id]
        if hh_rows:
            md = max([h["plan_date"] for h in hh_rows])
            y, m, d = [int(x) for x in md.split("-")]
            end = date(y, m, d)
        else:
            end = date(2025, 1, 1)
    start = end - timedelta(days=int(days_back))
    return [
        int(r.get("recipe_id"))
        for r in data.get("meal_history", [])
        if r.get("household_id") == household_id and str(r.get("plan_date")) >= start.isoformat()
    ]

def _latest_list_id(data: Dict[str, Any], household_id: Optional[int]) -> Optional[int]:
    gl = _latest_list_for_household(data, household_id)
    return int(gl["list_id"]) if gl else None

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

def _collect_recipe_ingredients(data: Dict[str, Any], recipe_ids: List[int]) -> List[Dict[str, Any]]:
    ri = data.get("recipe_ingredients", [])
    return [row for row in ri if row.get("recipe_id") in recipe_ids]

class FlagOverlapLastMonthOnList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], anchor_date, household_id, list_id) -> str:
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