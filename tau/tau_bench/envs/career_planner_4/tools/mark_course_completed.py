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

class MarkCourseCompleted(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, course_id: str, completion_date: str
    ) -> str:
        progress = data.get("user_course_progress", {}).values()
        user_progress = next(
            (
                p
                for p in progress.values() if p.get("user_id") == user_id and p.get("course_id") == course_id
            ),
            None,
        )
        if user_progress:
            user_progress["status"] = "Completed"
            user_progress["completion_date"] = completion_date
            user_progress["current_progress_percent"] = 100
        else:
            new_progress = {
                "user_id": user_id,
                "course_id": course_id,
                "status": "Completed",
                "completion_date": completion_date,
                "current_progress_percent": 100,
            }
            data["user_course_progress"][new_progress["user_course_progres_id"]] = new_progress
        payload = {"success": f"Course {course_id} marked completed for user {user_id}"}
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
                "name": "markCourseCompleted",
                "description": "Mark a course as completed for a user",
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
