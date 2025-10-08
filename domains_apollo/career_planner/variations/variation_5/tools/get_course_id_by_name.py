from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCourseIdByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], course_name: str) -> str:
        _course_nameL = course_name or ''.lower()
        pass
        courses = data.get("course_catalog", [])
        # Locate a course whose name includes the specified string (case-insensitive)
        course = next(
            (c for c in courses if course_name.lower() in c.get("name", "").lower()),
            None,
        )
        if course:
            payload = {"course_id": course["course_id"]}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Course with name containing '{course_name}' not found"}
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
                "name": "getCourseIdByName",
                "description": "Find a course ID by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "course_name": {
                            "type": "string",
                            "description": "The name or partial name of the course to find.",
                        }
                    },
                    "required": ["course_name"],
                },
            },
        }
