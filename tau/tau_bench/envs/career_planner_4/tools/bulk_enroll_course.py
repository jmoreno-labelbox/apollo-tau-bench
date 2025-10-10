# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class bulk_enroll_course(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, course_id: str, enroll_date: str
    ) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("members", [])
        for member in members:
            enrollment = {
                "user_id": member,
                "course_id": course_id,
                "status": "Enrolled",
                "start_date": enroll_date,
                "current_progress_percent": 0,
            }
            data.setdefault("user_course_progress", []).append(enrollment)

        return json.dumps(
            {"success": f"Bulk enrolled {len(members)} members in course {course_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "bulk_enroll_course",
                "description": "Bulk enroll team members in a course",
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
