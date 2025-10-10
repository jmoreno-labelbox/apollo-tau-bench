# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class schedule_team_training(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, course_id: str, session_date: str
    ) -> str:
        training_session = {
            "team_id": team_id,
            "course_id": course_id,
            "session_date": session_date,
            "status": "Scheduled",
        }
        data.setdefault("team_training_sessions", []).append(training_session)
        return json.dumps(
            {"success": f"Training session scheduled for team {team_id}"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "schedule_team_training",
                "description": "Schedule a training session for a team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "session_date": {"type": "string"},
                    },
                    "required": ["team_id", "course_id", "session_date"],
                },
            },
        }
