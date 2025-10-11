# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateMealPlan(Tool):
    """Creates a new meal plan for a household."""
    @staticmethod
    def invoke(data: Dict[str, Any], created_by_user_id, household_id, week_start_date) -> str:

        meal_plans = data.get("meal_plans", [])
        # Automatically create the subsequent meal_plan_id.
        new_id = max([plan.get("meal_plan_id", 0) for plan in meal_plans]) + 1 if meal_plans else 6001

        new_plan = {
            "meal_plan_id": new_id,
            "household_id": household_id,
            "week_start_date": week_start_date,
            "created_by_user_id": created_by_user_id,
            "created_at": "2025-08-20T11:00:00Z" # Employing a static timestamp for uniformity
        }
        data["meal_plans"].append(new_plan)
        return json.dumps(new_plan)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_meal_plan",
                "description": "Creates a new meal plan for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string", "description": "Start date of the week in YYYY-MM-DD format."},
                        "created_by_user_id": {"type": "integer"},
                    },
                    "required": ["household_id", "week_start_date", "created_by_user_id"],
                },
            },
        }
