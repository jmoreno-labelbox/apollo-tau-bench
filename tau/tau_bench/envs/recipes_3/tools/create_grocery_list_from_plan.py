from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateGroceryListFromPlan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: int, created_by_user_id: int) -> str:
        plans = _get_table(data, "meal_plans")
        mp = next((p for p in plans if p.get("meal_plan_id") == meal_plan_id), None)
        if not mp:
            return _error("meal_plan not found")
        return CreateGroceryList.invoke(
            data,
            household_id=mp.get("household_id"),
            source_meal_plan_id=meal_plan_id,
            created_by_user_id=created_by_user_id,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGroceryListFromPlan",
                "description": "Creates a grocery list from a meal_plan_id (derives household).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "created_by_user_id": {"type": "integer"},
                    },
                    "required": ["meal_plan_id", "created_by_user_id"],
                },
            },
        }
