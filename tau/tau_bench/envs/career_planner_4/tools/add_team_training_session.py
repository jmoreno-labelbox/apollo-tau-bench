# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_team_training_session(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str, training: dict) -> str:
        training["team_id"] = team_id
        data.setdefault("team_training_sessions", []).append(training)
        return json.dumps(
            {"success": f"Training session added for team {team_id}"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_team_training_session",
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
