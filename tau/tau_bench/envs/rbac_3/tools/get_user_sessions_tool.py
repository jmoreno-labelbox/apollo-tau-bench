from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class GetUserSessionsTool(Tool):
    """get_user_sessions: alias for listing active sessions of a user."""

    @staticmethod
    def invoke(data: dict[str, Any], param1: Any = None, param2: Any = None, user_id: str = None) -> str:
        # Support user_id as alias for param1
        param1 = param1 or user_id
        return ListActiveSessionsTool.invoke(data, param1=param1, param2=param2)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserSessions",
                "description": "Return active sessions for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
