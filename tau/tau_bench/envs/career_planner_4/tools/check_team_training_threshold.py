# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class check_team_training_threshold(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, threshold: int, comparison: str
    ) -> str:
        # Calculation of training hours for the mock team.
        training_data = data.get("team_training_log", [])
        team_sessions = [t for t in training_data if t.get("team_id") == team_id]

        # Sample calculation - actual training hours would be totaled in a real system.
        total_hours = len(team_sessions) * 25  # Consider each session to be 25 hours long.

        if comparison == "below":
            condition_met = total_hours < threshold
            return json.dumps(
                {
                    "condition_met": condition_met,
                    "team_id": team_id,
                    "total_hours": total_hours,
                    "threshold": threshold,
                    "comparison": comparison,
                },
                indent=2,
            )
        else:
            condition_met = total_hours >= threshold
            return json.dumps(
                {
                    "condition_met": condition_met,
                    "team_id": team_id,
                    "total_hours": total_hours,
                    "threshold": threshold,
                    "comparison": comparison,
                },
                indent=2,
            )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_team_training_threshold",
                "description": "Check if team training hours meet threshold",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "threshold": {"type": "integer"},
                        "comparison": {"type": "string", "enum": ["below", "above"]},
                    },
                    "required": ["team_id", "threshold", "comparison"],
                },
            },
        }
