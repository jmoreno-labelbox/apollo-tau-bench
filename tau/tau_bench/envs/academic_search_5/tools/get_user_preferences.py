from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserPreferences(Tool):
    """Utility for fetching the preference settings of a particular user."""

    @staticmethod
    def invoke(data: dict[str, Any], *, user_id: Any = None) -> str:
        user_id = user_id
        if not user_id:
            payload = {"error": "user_id is required."}
            out = json.dumps(payload)
            return out

        preferences = data.get("user_preferences", {}).values()
        for pref in preferences.values():
            if pref.get("user_id") == user_id:
                payload = pref
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Preferences not found for the given user ID."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserPreferences",
                "description": "Retrieves the preference settings (like notification channel and UI theme) for a single user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to retrieve preferences for.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
