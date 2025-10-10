# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class check_user_training_completion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, team_id: str) -> str:
        training_logs = data.get("team_training_log", [])
        user_training = [log for log in training_logs if log.get("user_id") == user_id]
        completed_training = [
            log for log in user_training if log.get("status") == "Completed"
        ]

        completion_rate = (
            len(completed_training) / len(user_training) if user_training else 0
        )

        return json.dumps(
            {
                "user_id": user_id,
                "team_id": team_id,
                "total_training_sessions": len(user_training),
                "completed_sessions": len(completed_training),
                "completion_rate": completion_rate,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_user_training_completion",
                "description": "Check training completion status for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "team_id": {"type": "string"},
                    },
                    "required": ["user_id", "team_id"],
                },
            },
        }
