from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class AddTeamTrainingSession(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str, training: dict) -> str:
        training["team_id"] = team_id
        data.setdefault("team_training_sessions", []).append(training)
        payload = {"success": f"Training session added for team {team_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addTeamTrainingSession",
                "description": "Add a training session for a team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "training": {"type": "object"},
                    },
                    "required": ["team_id", "training"],
                },
            },
        }
