from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateTeamTrainingLog(Tool):
    """Insert an entry into the team training log."""

    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None, entry: str = None) -> str:
        logs = data.setdefault("team_training_logs", [])
        logs.append(
            {
                "team_id": team_id,
                "entry": entry,
                "date": datetime.utcnow().date().isoformat(),
            }
        )
        payload = {"success": f"Log entry added for {team_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTeamTrainingLog",
                "description": "Add training log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "entry": {"type": "string"},
                    },
                    "required": ["team_id", "entry"],
                },
            },
        }
