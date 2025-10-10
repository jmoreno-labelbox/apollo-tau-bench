# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_course_progress(Tool):
    @staticmethod
    def invoke(data, user_id: str, course_id: str, progress_percent: int) -> str:
        record = {
            "user_id": user_id,
            "course_id": course_id,
            "progress_percent": progress_percent,
        }
        data.setdefault("course_progress_updates", []).append(record)
        return json.dumps(
            {
                "success": f"Course {course_id} progress for {user_id} updated to {progress_percent}%."
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_course_progress",
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
