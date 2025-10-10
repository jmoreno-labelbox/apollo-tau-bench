# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        session_id = kwargs.get("session_id")
        user_id = kwargs.get("user_id")
        ip_address = kwargs.get("ip_address")
        only_active = kwargs.get("only_active", False)

        sessions = data.get("sessions", [])

        # If session_id is provided, return single session
        if session_id:
            session = _find_by_id(sessions, "session_id", session_id)
            if not session:
                return json.dumps({"error": f"session_id {session_id} not found"})
            return json.dumps({"ok": True, "session": session if session else "No sessions found"})

        # Filter sessions based on provided criteria
        filtered_sessions = []
        for session in sessions:
            # Filter by user_id if provided
            if user_id and session.get("user_id") != user_id:
                continue
            # Filter by ip_address if provided
            if ip_address and session.get("ip_address") != ip_address:
                continue
            # Filter by active status if requested
            if only_active and session.get("end_time") is not None:
                continue
            filtered_sessions.append(session)

        return json.dumps({"ok": True, "sessions": filtered_sessions if filtered_sessions else "No sessions found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_session",
                "description": "Retrieve sessions by session ID, user ID, or IP address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {"type": "string", "description": "Specific session ID to retrieve."},
                        "user_id": {"type": "string", "description": "Filter by user who owns the sessions."},
                        "ip_address": {"type": "string", "description": "Filter by IP address used in sessions."},
                        "only_active": {"type": "boolean", "description": "Only return sessions without end_time.", "default": False}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
