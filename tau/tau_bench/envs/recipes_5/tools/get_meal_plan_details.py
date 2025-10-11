# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id
def _latest_meal_plan_for_household(data: Dict[str, Any], household_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if household_id is None:
        return None
    plans = [m for m in data.get("meal_plans", []) if m.get("household_id") == household_id]
    if not plans:
        return None
    return sorted(plans, key=lambda m: int(m.get("meal_plan_id", 0)), reverse=True)[0]

def _household_for_user(data: Dict[str, Any], user_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if user_id is not None:
        h = next((h for h in data.get("households", []) if h.get("primary_user_id") == user_id), None)
        if h:
            return h
    households = data.get("households", [])
    if not households:
        return None
    return sorted(households, key=lambda h: int(h.get("household_id", 10**9)))[0]

def _latest_meal_plan_id(data: Dict[str, Any], household_id: Optional[int]) -> Optional[int]:
    mp = _latest_meal_plan_for_household(data, household_id)
    return int(mp["meal_plan_id"]) if mp else None

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

class GetMealPlanDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], meal_plan_id) -> str:
        if meal_plan_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            meal_plan_id = _latest_meal_plan_id(data, household_id)
        if meal_plan_id is None:
            return _json_dump({"error": "no meal_plan available"})
        row = next((m for m in data.get("meal_plans", []) if m.get("meal_plan_id") == meal_plan_id), None)
        if not row:
            return _json_dump({"error": f"meal_plan_id {meal_plan_id} not found"})
        return _json_dump(row)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_meal_plan_details","description":"Get a meal_plan row; defaults to latest.","parameters":{"type":"object","properties":{"meal_plan_id":{"type":"integer"}},"required":[]}}}