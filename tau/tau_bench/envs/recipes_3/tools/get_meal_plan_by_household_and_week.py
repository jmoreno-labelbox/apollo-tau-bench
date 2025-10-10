# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMealPlanByHouseholdAndWeek(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, week_start_date: str) -> str:
        row = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        return json({"meal_plan": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_meal_plan_by_household_and_week",
                "description": "Find a meal_plan by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                    },
                    "required": ["household_id", "week_start_date"],
                },
            },
        }
