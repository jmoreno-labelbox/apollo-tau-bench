# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddMealHistory(Tool):
    """Adds a new entry to the meal history."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        recipe_id = kwargs.get("recipe_id")
        plan_date = kwargs.get("plan_date")
        was_prepared = kwargs.get("was_prepared")
        rating_int = kwargs.get("rating_int")

        history = data.get("meal_history", [])
        new_id = max([h.get("history_id", 0) for h in history]) + 1 if history else 6201

        new_entry = {
            "history_id": new_id,
            "household_id": household_id,
            "plan_date": plan_date,
            "recipe_id": recipe_id,
            "was_prepared": was_prepared,
            "rating_int": rating_int
        }
        data["meal_history"].append(new_entry)
        return json.dumps(new_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_meal_history",
                "description": "Adds a new entry to the meal history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "recipe_id": {"type": "integer"},
                        "plan_date": {"type": "string", "description": "Date the meal was planned for in YYYY-MM-DD format."},
                        "was_prepared": {"type": "boolean"},
                        "rating_int": {"type": "integer", "description": "Rating from 1 to 5; can be null."},
                    },
                    "required": ["household_id", "recipe_id", "plan_date", "was_prepared"],
                },
            },
        }
