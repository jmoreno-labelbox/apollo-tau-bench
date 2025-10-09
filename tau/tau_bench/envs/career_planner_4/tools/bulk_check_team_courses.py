from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class BulkCheckTeamCourses(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        team_id: str,
        teams: list = None,
        user_course_progress: list = None
    ) -> str:
        teams = teams if teams is not None else data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

        members = team.get("team_members", [])
        progress_data = user_course_progress if user_course_progress is not None else data.get("user_course_progress", [])
        team_progress = []

        for member_id in members:
            member_courses = [p for p in progress_data if p.get("user_id") == member_id]
            avg_progress = (
                sum(c.get("current_progress_percent", 0) for c in member_courses)
                / len(member_courses)
                if member_courses
                else 0
            )
            team_progress.append(
                {"user_id": member_id, "average_progress": avg_progress}
            )
        payload = {"team_id": team_id, "member_progress": team_progress}
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
                "name": "bulkCheckTeamCourses",
                "description": "Check course progress for all team members",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
