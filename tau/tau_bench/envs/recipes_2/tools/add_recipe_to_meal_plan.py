# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddRecipeToMealPlan(Tool):
    """Adds a recipe entry to an existing meal plan."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        plan_date = kwargs.get("plan_date")
        recipe_id = kwargs.get("recipe_id")
        meal_type = kwargs.get("meal_type", "Dinner")
        servings_adult = kwargs.get("servings_adult", 2)
        servings_child = kwargs.get("servings_child", 1)
        notes = kwargs.get("notes", "")

        entries = data.get("meal_plan_entries", [])
        # Automatically create the subsequent entry_id.
        new_id = max([entry.get("entry_id", 0) for entry in entries]) + 1 if entries else 6101

        new_entry = {
            "entry_id": new_id,
            "meal_plan_id": meal_plan_id,
            "plan_date": plan_date,
            "meal_type": meal_type,
            "recipe_id": recipe_id,
            "servings_adult": servings_adult,
            "servings_child": servings_child,
            "notes": notes
        }
        data["meal_plan_entries"].append(new_entry)
        return json.dumps(new_entry)
        
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_recipe_to_meal_plan",
                "description": "Adds a recipe entry to an existing meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "plan_date": {"type": "string", "description": "Date for the meal in YYYY-MM-DD format."},
                        "recipe_id": {"type": "integer"},
                        "notes": {"type": "string", "description": "Optional notes for the meal entry."},
                    },
                    "required": ["meal_plan_id", "plan_date", "recipe_id"],
                },
            },
        }
