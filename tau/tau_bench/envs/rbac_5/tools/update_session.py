from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateSession(Tool):
    """
    Modify session properties while maintaining session_id as immutable.

    kwargs:
      session_id: str (mandatory) - Session ID to modify
      end_time: str ISO (optional) - Specify session end time
      ip_address: str (optional) - Update the IP address
      device: str (optional) - Update the type of device
      is_mfa: bool (optional) - Update MFA status
    """

    @staticmethod
    def invoke(data: dict[str, Any], session_id: str = "", end_time: Any = None, ip_address: Any = None, device: Any = None, is_mfa: Any = None) -> str:
        if not session_id:
            payload = {"error": "session_id required"}
            out = json.dumps(payload)
            return out

        # Locate the session
        sessions = data.get("sessions", [])
        session_index = None
        for i, session in enumerate(sessions):
            if session.get("session_id") == session_id:
                session_index = i
                break

        if session_index is None:
            payload = {"error": f"session_id {session_id} not found"}
            out = json.dumps(payload)
            return out

        # Modify the session (session_id, user_id, or start_time cannot be changed)
        updated_session = dict(sessions[session_index])
        if end_time is not None:
            updated_session["end_time"] = end_time
        if ip_address is not None:
            updated_session["ip_address"] = ip_address
        if device is not None:
            updated_session["device"] = device
        if is_mfa is not None:
            updated_session["is_mfa"] = is_mfa

        data["sessions"][session_index] = updated_session
        payload = {"ok": True, "session": updated_session}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSession",
                "description": "Update session properties while keeping session_id immutable.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {
                            "type": "string",
                            "description": "Session ID to update.",
                        },
                        "end_time": {
                            "type": "string",
                            "description": "ISO timestamp for session end time.",
                        },
                        "ip_address": {
                            "type": "string",
                            "description": "Updated IP address.",
                        },
                        "device": {
                            "type": "string",
                            "description": "Updated device type (DESKTOP, LAPTOP, MOBILE).",
                        },
                        "is_mfa": {
                            "type": "boolean",
                            "description": "Updated MFA status.",
                        },
                    },
                    "required": ["session_id"],
                    "additionalProperties": False,
                },
            },
        }
