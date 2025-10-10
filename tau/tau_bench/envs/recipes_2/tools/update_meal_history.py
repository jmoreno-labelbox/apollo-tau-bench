# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateMealHistory(Tool):
    """Updates an entry in the meal history, such as its preparation status or rating."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        history_id = kwargs.get("history_id")
        was_prepared = kwargs.get("was_prepared")
        rating_int = kwargs.get("rating_int")

        if history_id is None:
            return json.dumps({"error": "history_id parameter is required."})

        history = data.get("meal_history", [])
        for entry in history:
            if entry.get("history_id") == history_id:
                if was_prepared is not None:
                    entry["was_prepared"] = was_prepared
                if rating_int is not None:
                    entry["rating_int"] = rating_int
                return json.dumps(entry)
        
        return json.dumps({"error": f"Meal history entry with ID '{history_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_meal_history",
                "description": "Updates an entry in the meal history, such as its preparation status or rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "history_id": {"type": "integer"},
                        "was_prepared": {"type": "boolean", "description": "Set to true if the meal was prepared."},
                        "rating_int": {"type": "integer", "description": "Rating from 1 to 5, can be null."},
                    },
                    "required": ["history_id"],
                },
            },
        }
