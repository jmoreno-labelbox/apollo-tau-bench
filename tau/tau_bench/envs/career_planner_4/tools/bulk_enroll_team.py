# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class bulk_enroll_team(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, course_id: str, enroll_date: str
    ) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("team_members", [])
        enrolled_members = []

        for member_id in members:
            enrollment = {
                "user_id": member_id,
                "course_id": course_id,
                "status": "Enrolled",
                "start_date": enroll_date,
                "completion_date": None,
                "current_progress_percent": 0,
            }
            data.setdefault("user_course_progress", []).append(enrollment)
            enrolled_members.append(member_id)

        return json.dumps(
            {
                "success": f"Team {team_id} enrolled in course {course_id}",
                "enrolled_members": enrolled_members,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "bulk_enroll_team",
                "description": "Enroll all team members in a course",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "enroll_date": {"type": "string"},
                    },
                    "required": ["team_id", "course_id", "enroll_date"],
                },
            },
        }
