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

class BulkEnrollCourse(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], team_id: str, course_id: str, enroll_date: str
    ) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

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
        payload = {"success": f"Bulk enrolled {len(members)} members in course {course_id}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
            

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "bulkEnrollCourse",
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
