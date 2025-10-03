from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class LogCourseProgress(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        course_id: str,
        progress: int,
        update_date: str,
    ) -> str:
        record = {
            "user_id": user_id,
            "course_id": course_id,
            "progress": progress,
            "update_date": update_date,
        }
        data.setdefault("course_progress_log", []).append(record)
        payload = {
            "success": f"Course progress logged for {user_id} in {course_id}: {progress}%"
        }
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
                "name": "logCourseProgress",
                "description": "Log course progress for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "progress": {"type": "integer"},
                        "update_date": {"type": "string"},
                    },
                    "required": ["user_id", "course_id", "progress", "update_date"],
                },
            },
        }
