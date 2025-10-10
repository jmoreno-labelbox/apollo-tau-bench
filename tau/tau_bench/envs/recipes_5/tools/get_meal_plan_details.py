# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMealPlanDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
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
