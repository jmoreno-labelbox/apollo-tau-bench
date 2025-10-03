from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class CreateMealPlan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None, created_by_user_id: int = None, week_start_date: str = None) -> str:
        if created_by_user_id is None:
            created_by_user_id = _first_user_id(data)
        if household_id is None:
            household_id = _default_household_id(data, created_by_user_id)
        week_start_date = week_start_date or _next_week_start_date_for_household(data, household_id)
        if household_id is None or created_by_user_id is None:
            return _json_dump({"error": "unable to infer household or user"})
        meal_plans = data.get("meal_plans", [])
        next_id = _max_id(meal_plans, "meal_plan_id", 6000) + 1
        new_row = {
            "meal_plan_id": next_id,
            "household_id": int(household_id),
            "week_start_date": str(week_start_date),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T00:00:00Z",
        }
        meal_plans.append(new_row)
        return _json_dump({"meal_plan_id": next_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMealPlan",
                "description": "Insert a new meal_plan with defaults for household, creator, and week_start_date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "created_by_user_id": {"type": "integer"},
                    },
                    "required": [],
                },
            },
        }
