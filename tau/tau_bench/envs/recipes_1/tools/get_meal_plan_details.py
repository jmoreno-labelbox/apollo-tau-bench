# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMealPlanDetails(Tool):
    """Return a meal_plan row by id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        if meal_plan_id is None:
            return _json_dump({"error": "meal_plan_id is required"})
        row = _require(data, "meal_plans", "meal_plan_id", int(meal_plan_id))
        return _json_dump(row or {"error": f"meal_plan_id {meal_plan_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_meal_plan_details",
            "description":"Get a meal_plan header by id.",
            "parameters":{"type":"object","properties":{"meal_plan_id":{"type":"integer"}},"required":["meal_plan_id"]}
        }}
