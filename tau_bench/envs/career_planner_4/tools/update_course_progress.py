from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateCourseProgress(Tool):
    @staticmethod
    def invoke(data, user_id: str, course_id: str, progress_percent: int) -> str:
        record = {
            "user_id": user_id,
            "course_id": course_id,
            "progress_percent": progress_percent,
        }
        data.setdefault("course_progress_updates", []).append(record)
        payload = {
            "success": f"Course {course_id} progress for {user_id} updated to {progress_percent}%."
        }
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
                "name": "updateCourseProgress",
                "description": "Update the progress percentage for a user in a specific course.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "progress_percent": {"type": "integer"},
                    },
                    "required": ["user_id", "course_id", "progress_percent"],
                },
            },
        }
