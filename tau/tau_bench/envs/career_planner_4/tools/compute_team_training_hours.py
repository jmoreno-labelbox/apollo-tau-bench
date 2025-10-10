# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class compute_team_training_hours(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str, year: int = 2025) -> str:
        training_logs = data.get("team_training_log", [])
        team_logs = [log for log in training_logs if log.get("team_id") == team_id]
        total_hours = len(team_logs) * 8  # Simulated computation
        return json.dumps({"total_hours": total_hours, "team_id": team_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "compute_team_training_hours",
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
