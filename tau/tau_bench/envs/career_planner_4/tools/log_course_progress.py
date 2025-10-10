# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class log_course_progress(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
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
        return json.dumps(
            {
                "success": f"Course progress logged for {user_id} in {course_id}: {progress}%"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "log_course_progress",
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
