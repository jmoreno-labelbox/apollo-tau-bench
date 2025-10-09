from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSession(Tool):
    """
    Retrieve sessions by session ID, user ID, or IP address.

    kwargs:
      session_id: str (optional) - Specific session ID to retrieve
      user_id: str (optional) - Filter by user who owns the sessions
      ip_address: str (optional) - Filter by IP address used in sessions
      only_active: bool = False - Only return sessions without end_time
    """

    @staticmethod
    def invoke(data: dict[str, Any], session_id: str = None, user_id: str = None, ip_address: str = None, only_active: bool = False) -> str:
        sessions = data.get("sessions", {}).values()

        # If session_id is supplied, return the specific session
        if session_id:
            session = _find_by_id(sessions, "session_id", session_id)
            if not session:
                payload = {"error": f"session_id {session_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "session": session if session else "No sessions found"}
            out = json.dumps(payload)
            return out

        # Narrow down sessions according to the supplied criteria
        filtered_sessions = []
        for session in sessions.values():
            # Narrow down by user_id if supplied
            if user_id and session.get("user_id") != user_id:
                continue
            # Narrow down by ip_address if supplied
            if ip_address and session.get("ip_address") != ip_address:
                continue
            # Narrow down by active status if requested
            if only_active and session.get("end_time") is not None:
                continue
            filtered_data["sessions"][session_id] = session
        payload = {
            "ok": True,
            "sessions": (
                filtered_sessions if filtered_sessions else "No sessions found"
            ),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSession",
                "description": "Retrieve sessions by session ID, user ID, or IP address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {
                            "type": "string",
                            "description": "Specific session ID to retrieve.",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Filter by user who owns the sessions.",
                        },
                        "ip_address": {
                            "type": "string",
                            "description": "Filter by IP address used in sessions.",
                        },
                        "only_active": {
                            "type": "boolean",
                            "description": "Only return sessions without end_time.",
                            "default": False,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
