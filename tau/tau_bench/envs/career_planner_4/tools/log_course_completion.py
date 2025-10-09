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

class LogCourseCompletion(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, course_id: str, completion_date: str
    ) -> str:
        # Modify current course progress or establish a new record
        courses = data.get("user_course_progress", [])
        course = next(
            (
                c
                for c in courses
                if c.get("user_id") == user_id and c.get("course_id") == course_id
            ),
            None,
        )
        if course:
            course.update(
                {
                    "status": "Completed",
                    "completion_date": completion_date,
                    "current_progress_percent": 100,
                }
            )
        else:
            courses.append(
                {
                    "user_id": user_id,
                    "course_id": course_id,
                    "status": "Completed",
                    "completion_date": completion_date,
                    "current_progress_percent": 100,
                }
            )
        payload = {"success": f"Course {course_id} completion logged for user {user_id}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "logCourseCompletion",
                "description": "Log course completion for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "completion_date": {"type": "string"},
                    },
                    "required": ["user_id", "course_id", "completion_date"],
                },
            },
        }
