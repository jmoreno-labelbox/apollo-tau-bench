from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUserPreferences(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        preferences = data.get("user_preferences", [])

        for pref in preferences:
            if pref.get("user_id") == user_id:
                payload = pref
                out = json.dumps(payload, indent=2)
                return out
        payload = {
                "error": "User preferences not found",
                "user_id": user_id,
                "available_users_with_prefs": [p.get("user_id") for p in preferences],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUserPreferences",
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
