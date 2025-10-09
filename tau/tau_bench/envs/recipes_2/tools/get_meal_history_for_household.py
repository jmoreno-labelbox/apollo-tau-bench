from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetMealHistoryForHousehold(Tool):
    """Obtains the meal records for a specific household ID over a defined number of previous days."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str, days_ago: int = 14) -> str:
        meal_history = data.get("meal_history", [])
        current_date = datetime.strptime("2025-08-20", "%Y-%m-%d")
        start_date = current_date - timedelta(days=days_ago)
        history = [
            h
            for h in meal_history
            if h.get("household_id") == household_id
            and datetime.strptime(h.get("plan_date"), "%Y-%m-%d") >= start_date
        ]
        payload = history
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMealHistoryForHousehold",
                "description": "Retrieves the meal history for a given household ID for a specified number of past days.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID of the household.",
                        },
                        "days_ago": {
                            "type": "integer",
                            "description": "Number of past days to retrieve history for. Defaults to 14.",
                        },
                    },
                    "required": ["household_id"],
                },
            },
        }
