from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetCourseProgress(Tool):
    """Check the enrollment progress for a particular course."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, course_id: str = None) -> str:
        for rec in data.get("user_course_progress", []):
            if rec.get("user_id") == user_id and rec.get("course_id") == course_id:
                payload = rec
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Progress record not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCourseProgress",
                "description": "Fetch course progress.",
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
