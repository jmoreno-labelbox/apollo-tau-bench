# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_team_training(Tool):
    @staticmethod
    def invoke(data, team_id: str) -> str:
        sessions = [
            ts
            for ts in data.get("team_training_log", [])
            if ts.get("training_session_id", "").startswith("TS")
        ]
        # (In a real scenario, you would filter by team_id)
        return json.dumps({"team_training_log": sessions}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_team_training",
                "description": "List all training sessions for a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
