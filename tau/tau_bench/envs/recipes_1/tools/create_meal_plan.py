from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateMealPlan(Tool):
    """Add a new meal_plan row and return the meal_plan_id."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        household_id: int = None, 
        week_start_date: str = None, 
        created_by_user_id: int = None
    ) -> str:
        if household_id is None or created_by_user_id is None or not week_start_date:
            return _json_dump(
                {
                    "error": "household_id, week_start_date, created_by_user_id are required"
                }
            )
        tbl = data.setdefault("meal_plans", [])
        next_id = _max_id(tbl, "meal_plan_id", 6000) + 1
        row = {
            "meal_plan_id": next_id,
            "household_id": int(household_id),
            "week_start_date": str(week_start_date),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T00:00:00Z",
        }
        data["meal_plans"][row["meal_plan_id"]] = row
        return _json_dump({"meal_plan_id": next_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMealPlan",
                "description": "Create a new meal plan (header).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "created_by_user_id": {"type": "integer"},
                    },
                    "required": [
                        "household_id",
                        "week_start_date",
                        "created_by_user_id",
                    ],
                },
            },
        }
