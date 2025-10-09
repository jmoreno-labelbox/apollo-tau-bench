from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetTeamTrainingLog(Tool):
    """Retrieve entries from the team training log."""

    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None) -> str:
        logs = [
            log
            for log in data.get("team_training_logs", [])
            if log.get("team_id") == team_id
        ]
        payload = logs
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamTrainingLog",
                "description": "Get team training log.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
