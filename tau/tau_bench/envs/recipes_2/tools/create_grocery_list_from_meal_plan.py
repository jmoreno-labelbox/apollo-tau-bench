from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateGroceryListFromMealPlan(Tool):
    """Creates a shopping list based on a meal plan."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None, meal_plan_id: int = None, user_id: int = None) -> str:
        lists = data.get("grocery_lists", {}).values()
        # Automatically create the next list_id
        new_id = max([l.get("list_id", 0) for l in lists.values()]) + 1 if lists else 8001

        new_list = {
            "list_id": new_id,
            "household_id": household_id,
            "source_meal_plan_id": meal_plan_id,
            "created_by_user_id": user_id,
            "created_at": "2025-08-20T12:00:00Z",  # Utilizing a stable timestamp for consistency
            "status_enum": "initialized",
        }
        data["grocery_lists"].append(new_list)
        payload = new_list
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGroceryListFromMealPlan",
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
