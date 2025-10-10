# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class check_course_completion_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, course_id: str) -> str:
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
        return json.dumps(
            {"completed": completed, "user_id": user_id, "course_id": course_id},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_course_completion_status",
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
