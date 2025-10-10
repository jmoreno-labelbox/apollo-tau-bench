# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _max_id, _json_dump


class CreateMealPlan(Tool):
    """Insert a new meal_plan row and return meal_plan_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        week_start_date = kwargs.get("week_start_date")
        created_by_user_id = kwargs.get("created_by_user_id")
        if household_id is None or created_by_user_id is None or not week_start_date:
            return _json_dump({"error": "household_id, week_start_date, created_by_user_id are required"})
        tbl = data.setdefault("meal_plans", [])
        next_id = _max_id(tbl, "meal_plan_id", 6000) + 1
        row = {
            "meal_plan_id": next_id,
            "household_id": int(household_id),
            "week_start_date": str(week_start_date),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T00:00:00Z"
        }
        tbl.append(row)
        return _json_dump({"meal_plan_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_meal_plan",
            "description":"Create a new meal plan (header).",
            "parameters":{"type":"object","properties":{
                "household_id":{"type":"integer"},
                "week_start_date":{"type":"string"},
                "created_by_user_id":{"type":"integer"}
            },"required":["household_id","week_start_date","created_by_user_id"]}
        }}
