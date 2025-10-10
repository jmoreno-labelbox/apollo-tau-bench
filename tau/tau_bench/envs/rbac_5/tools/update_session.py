# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSession(Tool):
    """
    Update session properties while keeping session_id immutable.

    kwargs:
      session_id: str (required) - Session ID to update
      end_time: str ISO (optional) - Set session end time
      ip_address: str (optional) - Update IP address
      device: str (optional) - Update device type
      is_mfa: bool (optional) - Update MFA status
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        session_id = kwargs.get("session_id", "")
        end_time = kwargs.get("end_time")
        ip_address = kwargs.get("ip_address")
        device = kwargs.get("device")
        is_mfa = kwargs.get("is_mfa")

        if not session_id:
            return json.dumps({"error": "session_id required"})

        # Find the session
        sessions = data.get("sessions", [])
        session_index = None
        for i, session in enumerate(sessions):
            if session.get("session_id") == session_id:
                session_index = i
                break

        if session_index is None:
            return json.dumps({"error": f"session_id {session_id} not found"})

        # Update the session (cannot modify session_id, user_id, or start_time)
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
        return json.dumps({"ok": True, "session": updated_session})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_session",
                "description": "Update session properties while keeping session_id immutable.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {"type": "string", "description": "Session ID to update."},
                        "end_time": {"type": "string", "description": "ISO timestamp for session end time."},
                        "ip_address": {"type": "string", "description": "Updated IP address."},
                        "device": {"type": "string", "description": "Updated device type (DESKTOP, LAPTOP, MOBILE)."},
                        "is_mfa": {"type": "boolean", "description": "Updated MFA status."}
                    },
                    "required": ["session_id"],
                    "additionalProperties": False
                }
            }
        }
