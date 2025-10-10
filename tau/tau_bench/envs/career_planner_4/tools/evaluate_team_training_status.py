# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class evaluate_team_training_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        training_logs = data.get("team_training_log", [])
        team_training = [log for log in training_logs if log.get("team_id") == team_id]

        total_sessions = len(team_training)
        completed_sessions = sum(
            1 for log in team_training if log.get("status") == "Completed"
        )
        in_progress_sessions = sum(
            1 for log in team_training if log.get("status") == "In Progress"
        )

        completion_rate = (
            completed_sessions / total_sessions if total_sessions > 0 else 0
        )

        return json.dumps(
            {
                "team_id": team_id,
                "total_training_sessions": total_sessions,
                "completed_sessions": completed_sessions,
                "in_progress_sessions": in_progress_sessions,
                "completion_rate": completion_rate,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "evaluate_team_training_status",
                "description": "Evaluate training status for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
