from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddRecipeToMealPlan(Tool):
    """Incorporates a recipe entry into a current meal plan."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        meal_plan_id: int,
        plan_date: str,
        recipe_id: int,
        meal_type: str = "Dinner",
        servings_adult: int = 2,
        servings_child: int = 1,
        notes: str = ""
    ) -> str:
        entries = data.get("meal_plan_entries", [])
        # Automatically create the next entry_id
        new_id = (
            max([entry.get("entry_id", 0) for entry in entries]) + 1
            if entries
            else 6101
        )

        new_entry = {
            "entry_id": new_id,
            "meal_plan_id": meal_plan_id,
            "plan_date": plan_date,
            "meal_type": meal_type,
            "recipe_id": recipe_id,
            "servings_adult": servings_adult,
            "servings_child": servings_child,
            "notes": notes,
        }
        data["meal_plan_entries"].append(new_entry)
        payload = new_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddRecipeToMealPlan",
                "description": "Adds a recipe entry to an existing meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "plan_date": {
                            "type": "string",
                            "description": "Date for the meal in YYYY-MM-DD format.",
                        },
                        "recipe_id": {"type": "integer"},
                        "notes": {
                            "type": "string",
                            "description": "Optional notes for the meal entry.",
                        },
                    },
                    "required": ["meal_plan_id", "plan_date", "recipe_id"],
                },
            },
        }
