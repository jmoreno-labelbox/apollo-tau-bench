from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetMealHistoryByHouseholdAndDate(Tool):
    """Obtains meal records for a specific household on a particular date."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None, plan_date: str = None) -> str:
        if household_id is None or plan_date is None:
            payload = {"error": "household_id and plan_date parameters are required."}
            out = json.dumps(payload)
            return out

        meal_history = data.get("meal_history", [])

        matching_history = [
            entry
            for entry in meal_history
            if entry.get("household_id") == household_id
            and entry.get("plan_date") == plan_date
        ]
        payload = matching_history
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMealHistoryByHouseholdAndDate",
                "description": "Retrieves meal history for a specific household on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID of the household.",
                        },
                        "plan_date": {
                            "type": "string",
                            "description": "The date of the meal plan entry in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["household_id", "plan_date"],
                },
            },
        }
