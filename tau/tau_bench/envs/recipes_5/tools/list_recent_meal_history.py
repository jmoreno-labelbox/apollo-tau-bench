# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id
def _household_for_user(data: Dict[str, Any], user_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if user_id is not None:
        h = next((h for h in data.get("households", []) if h.get("primary_user_id") == user_id), None)
        if h:
            return h
    households = data.get("households", [])
    if not households:
        return None
    return sorted(households, key=lambda h: int(h.get("household_id", 10**9)))[0]

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

class ListRecentMealHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], anchor_date, household_id, days_back = 14) -> str:
        days_back = int(days_back)
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        out = _recent_recipe_ids(data, household_id, days_back, anchor_date)
        return _json_dump({"household_id": household_id, "days_back": days_back, "recent_recipe_ids": out})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"list_recent_meal_history","description":"Return recent recipe_ids; defaults to last 14 days for default household.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"},"days_back":{"type":"integer"},"anchor_date":{"type":"string"}},"required":[]}}}