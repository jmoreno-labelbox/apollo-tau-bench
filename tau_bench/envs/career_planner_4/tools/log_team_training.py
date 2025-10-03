from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class LogTeamTraining(Tool):
    @staticmethod
    def invoke(data: dict, team_id: str, training_session: dict) -> str:
        data.setdefault("team_training_log", []).append(training_session)
        payload = {
            "success": f"Training session {training_session['training_session_id']} logged for team {team_id}"
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
                "name": "logTeamTraining",
                "description": "Append a new training session record for a team.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "training_session": {"type": "object"},
                    },
                    "required": ["team_id", "training_session"],
                },
            },
        }
