# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateGroceryListFromMealPlan(Tool):
    """Generates a grocery list from a meal plan."""
    @staticmethod
    def invoke(data: Dict[str, Any], household_id, meal_plan_id, user_id) -> str:

        lists = list(data.get("grocery_lists", {}).values())
        # Automatically create the subsequent list_id.
        new_id = max([l.get("list_id", 0) for l in lists]) + 1 if lists else 8001

        new_list = {
            "list_id": new_id,
            "household_id": household_id,
            "source_meal_plan_id": meal_plan_id,
            "created_by_user_id": user_id,
            "created_at": "2025-08-20T12:00:00Z", # Employing a constant timestamp for uniformity.
            "status_enum": "initialized"
        }
        data["grocery_lists"].append(new_list)
        return json.dumps(new_list)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_grocery_list_from_meal_plan",
                "description": "Generates a grocery list from a meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "meal_plan_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                    },
                    "required": ["household_id", "meal_plan_id", "user_id"],
                },
            },
        }
