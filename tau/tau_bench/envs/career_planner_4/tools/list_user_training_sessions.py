# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_user_training_sessions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        training_logs = data.get("team_training_log", [])
        user_sessions = [log for log in training_logs if log.get("user_id") == user_id]
        return json.dumps({"training_sessions": user_sessions}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_training_sessions",
                "description": "List training sessions for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
