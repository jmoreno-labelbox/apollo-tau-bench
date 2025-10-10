# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class log_team_training(Tool):
    @staticmethod
    def invoke(data, team_id: str, training_session: dict) -> str:
        data.setdefault("team_training_log", []).append(training_session)
        return json.dumps(
            {
                "success": f"Training session {training_session['training_session_id']} logged for team {team_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "log_team_training",
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
