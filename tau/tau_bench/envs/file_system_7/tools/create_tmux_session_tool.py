from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class CreateTmuxSessionTool(Tool):
    """Emulates the creation of a new tmux session on a remote server."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTmuxSession",
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
        if "tmux_sessions" not in data:
            data["tmux_sessions"] = []
        if session_name in data["tmux_sessions"]:
            payload = {"status": "exists", "session_name": session_name}
            out = json.dumps(payload)
            return out
        data["tmux_sessions"].append(session_name)
        payload = {"status": "created", "session_name": session_name}
        out = json.dumps(payload)
        return out
