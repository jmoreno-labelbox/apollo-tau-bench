# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TmuxSessionManagerTool(Tool):
    """Manages tmux session creation for persistent remote processes."""

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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        requested_session = kwargs["session_name"]

        # Set up session tracking
        data.setdefault("tmux_sessions", [])

        # Check if session already exists
        if requested_session in data["tmux_sessions"]:
            return json.dumps({
                "status": "exists",
                "session_name": requested_session
            })

        # Register new session
        data["tmux_sessions"].append(requested_session)

        return json.dumps({
            "status": "created",
            "session_name": requested_session
        })
