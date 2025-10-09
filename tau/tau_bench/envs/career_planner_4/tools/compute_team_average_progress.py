from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ComputeTeamAverageProgress(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        team_id: str,
        teams: list = None,
        user_course_progress: list = None
    ) -> str:
        teams = teams if teams is not None else data.get("teams", {}).values()
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

        members = team.get("members", [])
        if not members:
            payload = {"average_progress": 0}
            out = json.dumps(payload, indent=2)
            return out

        total_progress = 0
        user_progress = user_course_progress if user_course_progress is not None else data.get("user_course_progress", {}).values()
        for member in members:
            user_courses = [p for p in user_progress.values() if p.get("user_id") == member]
            if user_courses:
                avg_progress = sum(
                    p.get("current_progress_percent", 0) for p in user_courses
                ) / len(user_courses)
                total_progress += avg_progress

        team_average = total_progress / len(members) if members else 0
        payload = {"team_average_progress": team_average, "team_id": team_id}
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
                "name": "computeTeamAverageProgress",
                "description": "Compute average course progress for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
