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

class CheckCourseCompletionStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, course_id: str) -> str:
        progress = data.get("user_course_progress", [])
        user_progress = next(
            (
                p
                for p in progress
                if p.get("user_id") == user_id and p.get("course_id") == course_id
            ),
            None,
        )
        completed = (
            user_progress.get("status") == "Completed" if user_progress else False
        )
        payload = {"completed": completed, "user_id": user_id, "course_id": course_id}
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
                "name": "checkCourseCompletionStatus",
                "description": "Check if a user has completed a course",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                    },
                    "required": ["user_id", "course_id"],
                },
            },
        }
