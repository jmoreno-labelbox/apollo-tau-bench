# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateGroceryListForPlanByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        created_by_user_id: int,
        week_start_date: str,
        status_enum: str = "initialized",
    ) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return json({"error": "meal_plan not found for keys"})
        tbl = _tbl(data, "grocery_lists")
        next_id = _max_id(tbl, "list_id", 8000) + 1
        row = {
            "list_id": next_id,
            "household_id": int(household_id),
            "source_meal_plan_id": int(plan.get("meal_plan_id")),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T12:00:00",
            "status_enum": str(status_enum),
        }
        tbl.append(row)
        return json({"list_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_grocery_list_for_plan_by_keys",
                "description": "Create a grocery list for a plan by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "created_by_user_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "status_enum": {"type": "string"},
                    },
                    "required": ["household_id", "created_by_user_id", "week_start_date"],
                },
            },
        }
