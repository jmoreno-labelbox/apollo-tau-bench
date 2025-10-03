from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCourse(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], course_id: str) -> str:
        courses = data.get("course_catalog", [])
        course = next((c for c in courses if c.get("course_id") == course_id), None)
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
