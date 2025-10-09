from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CheckUserSessionsById(Tool):
    """Identifies all recent login sessions for a specific user to assist in security investigations."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        user_id_to_find = user_id
        try:
            all_sessions = data.get("sessions", [])
        except (KeyError, json.JSONDecodeError):
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
                "name": "CheckUserSessionsById",
                "description": "Retrieves a list of all recent login sessions for a specific user ID as part of a security investigation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose sessions are to be checked.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
