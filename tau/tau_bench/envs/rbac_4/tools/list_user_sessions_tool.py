from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListUserSessionsTool(Tool):
    """Display sessions for a specific user with an optional filter for active sessions only (read operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, active_only: bool = False) -> str:
        sessions = data.get("sessions", [])
        if not isinstance(sessions, list):
            payload = {"error": "sessions must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(user_id, str) or not user_id.strip():
            payload = {"error": "user_id must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out

        if active_only not in (True, False):
            payload = {"error": "active_only must be a boolean if provided"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        results = []
        for s in sessions:
            if s.get("user_id") != user_id:
                continue
            if active_only and s.get("end_time") is not None:
                continue
            results.append(s)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListUserSessions",
                "description": "List sessions for a user; optionally filter to only active sessions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id"},
                        "active_only": {
                            "type": "boolean",
                            "description": "If true, only return sessions without end_time",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }
