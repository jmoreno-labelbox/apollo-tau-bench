# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMealHistoryByHouseholdAndDate(Tool):
    """Retrieves meal history for a specific household on a given date."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        plan_date = kwargs.get("plan_date")

        if household_id is None or plan_date is None:
            return json.dumps({"error": "household_id and plan_date parameters are required."})

        meal_history = data.get("meal_history", [])
        
        matching_history = [
            entry for entry in meal_history 
            if entry.get("household_id") == household_id and entry.get("plan_date") == plan_date
        ]
        
        return json.dumps(matching_history)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_meal_history_by_household_and_date",
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
                        }
                    },
                    "required": ["household_id", "plan_date"],
                },
            },
        }
