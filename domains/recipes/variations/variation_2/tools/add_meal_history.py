from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class AddMealHistory(Tool):
    """Inserts a new record into the meal history."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int = None, recipe_id: int = None, plan_date: str = None, was_prepared: bool = None, rating_int: int = None) -> str:
        history = data.get("meal_history", [])
        new_id = max([h.get("history_id", 0) for h in history]) + 1 if history else 6201

        new_entry = {
            "history_id": new_id,
            "household_id": household_id,
            "plan_date": plan_date,
            "recipe_id": recipe_id,
            "was_prepared": was_prepared,
            "rating_int": rating_int,
        }
        data["meal_history"].append(new_entry)
        payload = new_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddMealHistory",
                "description": "Adds a new entry to the meal history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "recipe_id": {"type": "integer"},
                        "plan_date": {
                            "type": "string",
                            "description": "Date the meal was planned for in YYYY-MM-DD format.",
                        },
                        "was_prepared": {"type": "boolean"},
                        "rating_int": {
                            "type": "integer",
                            "description": "Rating from 1 to 5; can be null.",
                        },
                    },
                    "required": [
                        "household_id",
                        "recipe_id",
                        "plan_date",
                        "was_prepared",
                    ],
                },
            },
        }
