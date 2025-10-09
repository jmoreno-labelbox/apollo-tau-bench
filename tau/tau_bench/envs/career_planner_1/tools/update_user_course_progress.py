from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateUserCourseProgress(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, course_id: str, updates: dict[str, Any]
    ) -> str:
        rec = next(
            (
                r
                for r in data.get("user_course_progress", [])
                if r["user_id"] == user_id and r["course_id"] == course_id
            ),
            None,
        )
        if rec:
            rec.update(updates)
            payload = {"success": "course progress updated"}
            out = json.dumps(payload)
            return out
        payload = {"error": "course enrollment not found"}
        out = json.dumps(payload)
        return out
    

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateUserCourseProgress",
                "description": "Update an existing course-progress record for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["user_id", "course_id", "updates"],
                },
            },
        }
