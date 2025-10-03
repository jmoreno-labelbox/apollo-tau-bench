from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class TmuxSessionManagerTool(Tool):
    """Oversees tmux session creation for ongoing remote processes."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createTmuxSession",
                "description": "Creates a named tmux session to ensure process persistence.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_name": {
                            "type": "string",
                            "description": "The name for the tmux session.",
                        }
                    },
                    "required": ["session_name"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], session_name: str) -> str:
        requested_session = session_name

        # Establish session tracking
        data.setdefault("tmux_sessions", [])

        # Verify if a session is already present
        if requested_session in data["tmux_sessions"]:
            payload = {"status": "exists", "session_name": requested_session}
            out = json.dumps(payload)
            return out

        # Create a new session
        data["tmux_sessions"].append(requested_session)
        payload = {"status": "created", "session_name": requested_session}
        out = json.dumps(payload)
        return out
