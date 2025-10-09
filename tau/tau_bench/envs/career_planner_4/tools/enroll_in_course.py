from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class EnrollInCourse(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, course_id: str, enroll_date: str
    ) -> str:
        enrollment = {
            "user_id": user_id,
            "course_id": course_id,
            "status": "Enrolled",
            "start_date": enroll_date,
            "completion_date": None,
            "current_progress_percent": 0,
        }
        data.setdefault("user_course_progress", []).append(enrollment)
        payload = {"success": f"User {user_id} enrolled in course {course_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "enrollInCourse",
                "description": "Enroll a user in a course",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "enroll_date": {"type": "string"},
                    },
                    "required": ["user_id", "course_id", "enroll_date"],
                },
            },
        }
