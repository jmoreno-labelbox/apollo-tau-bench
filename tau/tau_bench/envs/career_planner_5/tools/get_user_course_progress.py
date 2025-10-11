# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_user_course_progress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, course_id: str) -> str:
        progress = next(
            (
                p
                for p in data.get("user_course_progress", [])
                if p.get("user_id") == user_id and p.get("course_id") == course_id
            ),
            None,
        )
        return (
            json.dumps(progress, indent=2)
            if progress
            else json.dumps({"error": "Course progress not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_user_course_progress",
                "description": "Get course progress for a specific user and course",
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
