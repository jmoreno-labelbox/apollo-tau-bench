# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateMealPlan(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, week_start_date: str, created_by_user_id: int
    ) -> str:
        tbl = _tbl(data, "meal_plans")
        next_id = _max_id(tbl, "meal_plan_id", 6000) + 1
        row = {
            "meal_plan_id": next_id,
            "household_id": int(household_id),
            "week_start_date": str(week_start_date),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T00:00:00",
        }
        tbl.append(row)
        return _json({"meal_plan_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_meal_plan",
                "description": "Create a new meal plan (header).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "created_by_user_id": {"type": "integer"},
                    },
                    "required": ["household_id", "week_start_date", "created_by_user_id"],
                },
            },
        }
