from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class GetMealPlanDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: str = None) -> str:
        if meal_plan_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            meal_plan_id = _latest_meal_plan_id(data, household_id)
        if meal_plan_id is None:
            return _json_dump({"error": "no meal_plan available"})
        row = next(
            (
                m
                for m in data.get("meal_plans", [])
                if m.get("meal_plan_id") == meal_plan_id
            ),
            None,
        )
        if not row:
            return _json_dump({"error": f"meal_plan_id {meal_plan_id} not found"})
        return _json_dump(row)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMealPlanDetails",
                "description": "Get a meal_plan row; defaults to latest.",
                "parameters": {
                    "type": "object",
                    "properties": {"meal_plan_id": {"type": "integer"}},
                    "required": [],
                },
            },
        }
