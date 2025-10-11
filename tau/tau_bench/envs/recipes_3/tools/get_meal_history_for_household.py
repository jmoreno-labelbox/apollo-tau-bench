# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMealHistoryForHousehold(Tool):
    """Retrieves the meal history for a given household ID for a specified number of past days."""
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, days_ago: int = 14) -> str:
        from datetime import datetime, timedelta
        meal_history = data.get("meal_history", [])
        current_date = datetime.strptime("2025-08-20", "%Y-%m-%d")
        start_date = current_date - timedelta(days=days_ago)
        history = [
            h for h in meal_history 
            if h.get("household_id") == household_id and 
               datetime.strptime(h.get("plan_date"), "%Y-%m-%d") >= start_date
        ]
        return json.dumps(history)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_meal_history_for_household",
                "description": "Retrieves the meal history for a given household ID for a specified number of past days.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer", "description": "The unique ID of the household."},
                        "days_ago": {"type": "integer", "description": "Number of past days to retrieve history for. Defaults to 14."},
                    },
                    "required": ["household_id"],
                },
            },
        }
