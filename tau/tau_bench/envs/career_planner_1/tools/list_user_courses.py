from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListUserCourses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        courses = [
            c
            for c in data.get("user_course_progress", {}).values()
            if c.get("user_id") == user_id
        ]
        payload = {"courses": courses}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListUserCourses",
                "description": "List all courses for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
