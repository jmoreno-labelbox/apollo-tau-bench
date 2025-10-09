from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class EvaluateTeamTrainingStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str) -> str:
        training_logs = data.get("team_training_log", {}).values()
        team_training = [log for log in training_logs.values() if log.get("team_id") == team_id]

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
        payload = {
            "team_id": team_id,
            "total_training_sessions": total_sessions,
            "completed_sessions": completed_sessions,
            "in_progress_sessions": in_progress_sessions,
            "completion_rate": completion_rate,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "evaluateTeamTrainingStatus",
                "description": "Evaluate training status for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
