from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateMealPlan(Tool):
    """Establishes a new meal plan for a family."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None, week_start_date: str = None, created_by_user_id: int = None) -> str:
        meal_plans = data.get("meal_plans", {}).values()
        # Automatically create the subsequent meal_plan_id
        new_id = (
            max([plan.get("meal_plan_id", 0) for plan in meal_plans.values()]) + 1
            if meal_plans
            else 6001
        )

        new_plan = {
            "meal_plan_id": new_id,
            "household_id": household_id,
            "week_start_date": week_start_date,
            "created_by_user_id": created_by_user_id,
            "created_at": "2025-08-20T11:00:00Z",  # Employing a constant timestamp for uniformity
        }
        data["meal_plans"][meal_plan_id] = new_plan
        payload = new_plan
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMealPlan",
                "description": "Creates a new meal plan for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {
                            "type": "string",
                            "description": "Start date of the week in YYYY-MM-DD format.",
                        },
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
