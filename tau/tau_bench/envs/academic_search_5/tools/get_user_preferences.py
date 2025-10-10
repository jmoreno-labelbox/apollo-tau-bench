# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserPreferences(Tool):
    """Tool to retrieve the preference settings for a specific user."""
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        if not user_id:
            return json.dumps({"error": "user_id is required."})

        preferences = data.get('user_preferences', [])
        for pref in preferences:
            if pref.get('user_id') == user_id:
                return json.dumps(pref, indent=2)
        return json.dumps({"error": "Preferences not found for the given user ID."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_preferences",
                "description": "Retrieves the preference settings (like notification channel and UI theme) for a single user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user to retrieve preferences for."}
                    },
                    "required": ["user_id"]
                }
            }
        }
