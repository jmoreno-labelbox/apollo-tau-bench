# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TerminateUserSession(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        session_id = kwargs.get("session_id")
        sessions = data.get('user_sessions', [])
        terminated = False
        for session in sessions:
            if session.get('session_id') == session_id:
                session['end_time'] = NOW.strftime(DT_STR_FORMAT)
                session['status'] = 'TERMINATED'
                terminated = True
                break

        if terminated:
            return json.dumps(session)
        return json.dumps({"error": "Session not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "terminate_user_session",
                        "description": "Terminates a user's active session.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "session_id": {"type": "string"}
                                },
                                "required": ["session_id"]
                        }
                }
        }
