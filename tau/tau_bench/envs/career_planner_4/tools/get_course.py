from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetCourse(Tool):
    def invoke(
        data: dict[str, Any],
        course_id: str,
        course_catalog: list[dict[str, Any]] = None
    ) -> str:
        course = next((c for c in course_catalog if c.get("course_id") == course_id), None)
        return (
            json.dumps(course, indent=2)
            if course
            else json.dumps({"error": "Course not found"}, indent=2)
        )
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getCourse",
                "description": "Get course details by course ID",
                "parameters": {
                    "type": "object",
                    "properties": {"course_id": {"type": "string"}},
                    "required": ["course_id"],
                },
            },
        }
