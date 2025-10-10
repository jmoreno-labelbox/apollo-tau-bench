# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserSessionsTool(Tool):
    """get_user_sessions: alias to list active sessions for a user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return ListActiveSessionsTool.invoke(data, **kwargs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_sessions",
                "description": "Return active sessions for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
