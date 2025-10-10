# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserPreferences(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        preferences = data.get("user_preferences", [])

        for pref in preferences:
            if pref.get("user_id") == user_id:
                return json.dumps(pref, indent=2)

        return json.dumps(
            {
                "error": "User preferences not found",
                "user_id": user_id,
                "available_users_with_prefs": [p.get("user_id") for p in preferences],
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_preferences",
                "description": "Retrieves the career and learning preferences for a given user, such as preferred industries, work style, and learning formats.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
