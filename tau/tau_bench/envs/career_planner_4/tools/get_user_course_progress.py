from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetUserCourseProgress(Tool):
    @staticmethod
    def invoke(
        data,
        user_id: str,
        prefix: str,
        course_id: str):
        payload = {"user_course_progress": {"status": "Not Completed", "grade": 0}}
        out = json.dumps(
            payload,
        indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getUserCourseProgress",
                "description": "Fetch the user's progress record for a specific course.",
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
