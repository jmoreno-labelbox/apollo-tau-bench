from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ComputeTeamTrainingHours(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        team_id: str,
        year: int = 2025
    ) -> str:
        training_logs = data.get("team_training_log", [])
        team_logs = [log for log in training_logs if log.get("team_id") == team_id]
        total_hours = len(team_logs) * 8  # Simulated calculation
        payload = {"total_hours": total_hours, "team_id": team_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "computeTeamTrainingHours",
                "description": "Compute total training hours for a team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "year": {"type": "integer"},
                    },
                    "required": ["team_id"],
                },
            },
        }
