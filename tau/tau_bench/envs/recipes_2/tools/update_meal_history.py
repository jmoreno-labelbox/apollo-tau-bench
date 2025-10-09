from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateMealHistory(Tool):
    """Modifies a record in the meal history, including its preparation status or rating."""

    @staticmethod
    def invoke(data: dict[str, Any], history_id: str = None, was_prepared: bool = None, rating_int: int = None) -> str:
        if history_id is None:
            payload = {"error": "history_id parameter is required."}
            out = json.dumps(payload)
            return out

        history = data.get("meal_history", [])
        for entry in history:
            if entry.get("history_id") == history_id:
                if was_prepared is not None:
                    entry["was_prepared"] = was_prepared
                if rating_int is not None:
                    entry["rating_int"] = rating_int
                payload = entry
                out = json.dumps(payload)
                return out
        payload = {"error": f"Meal history entry with ID '{history_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateMealHistory",
                "description": "Updates an entry in the meal history, such as its preparation status or rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "history_id": {"type": "integer"},
                        "was_prepared": {
                            "type": "boolean",
                            "description": "Set to true if the meal was prepared.",
                        },
                        "rating_int": {
                            "type": "integer",
                            "description": "Rating from 1 to 5, can be null.",
                        },
                    },
                    "required": ["history_id"],
                },
            },
        }
