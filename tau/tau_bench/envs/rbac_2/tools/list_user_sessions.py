from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListUserSessions(Tool):
    """Identify all recent login sessions associated with a specific user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        user_id_to_find = user_id
        try:
            all_sessions = data.get("sessions", [])
        except:
            all_sessions = []

        user_sessions = [
            session
            for session in all_sessions
            if session.get("user_id") == user_id_to_find
        ]
        payload = user_sessions
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListUserSessions",
                "description": "Retrieves a list of all recent login sessions for a specific user by their user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose sessions are to be retrieved.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
