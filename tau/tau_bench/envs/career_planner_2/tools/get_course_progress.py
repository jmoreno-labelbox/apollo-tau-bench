# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCourseProgress(Tool):
    """Look up enrollment progress for a course."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        cid = kwargs.get("course_id")
        for rec in data.get("user_course_progress", []):
            if rec.get("user_id") == uid and rec.get("course_id") == cid:
                return json.dumps(rec, indent=2)
        return json.dumps({"error": "Progress record not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_course_progress",
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
