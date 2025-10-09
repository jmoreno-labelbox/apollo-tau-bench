from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserCourseProgress(Tool):
    """Retrieve the complete course progress for a user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        uid = user_id
        progress = [
            rec
            for rec in data.get("user_course_progress", {}).values()
            if rec.get("user_id") == uid
        ]
        payload = progress
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserCourseProgress",
                "description": "Get all course progress for user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
