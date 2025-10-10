# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateTmuxSessionTool(Tool):
    """Simulates creating a new tmux session on a remote server."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_tmux_session",
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
    def invoke(data: Dict[str, Any], session_name) -> str:
        if "tmux_sessions" not in data:
            data["tmux_sessions"] = []
        if session_name in data["tmux_sessions"]:
            return json.dumps({"status": "exists", "session_name": session_name})
        data["tmux_sessions"].append(session_name)
        return json.dumps({"status": "created", "session_name": session_name})
