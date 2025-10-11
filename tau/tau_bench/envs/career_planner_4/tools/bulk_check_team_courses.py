# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class bulk_check_team_courses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("team_members", [])
        progress_data = data.get("user_course_progress", [])
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

        return json.dumps(
            {"team_id": team_id, "member_progress": team_progress}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "bulk_check_team_courses",
                "description": "Check course progress for all team members",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
