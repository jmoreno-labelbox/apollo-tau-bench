from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ListTeamTraining(Tool):
    @staticmethod
    def invoke(
        data,
        team_id: str,
        team_training_log: list = None
    ) -> str:
        sessions = [
            ts
            for ts in (team_training_log or [])
            if ts.get("training_session_id", "").startswith("TS")
        ]
        payload = {"team_training_log": sessions}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listTeamTraining",
                "description": "List all training sessions for a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
