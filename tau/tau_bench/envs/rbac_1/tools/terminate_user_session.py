from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class TerminateUserSession(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], session_id: str = None) -> str:
        sessions = data.get("user_sessions", {}).values()
        terminated = False
        for session in sessions.values():
            if session.get("session_id") == session_id:
                session["end_time"] = NOW.strftime(DT_STR_FORMAT)
                session["status"] = "TERMINATED"
                terminated = True
                break

        if terminated:
            payload = session
            out = json.dumps(payload)
            return out
        payload = {"error": "Session not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "terminateUserSession",
                "description": "Terminates a user's active session.",
                "parameters": {
                    "type": "object",
                    "properties": {"session_id": {"type": "string"}},
                    "required": ["session_id"],
                },
            },
        }
