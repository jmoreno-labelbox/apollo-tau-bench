from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class FindCourseByName(Tool):
    """Identify a course's ID based on its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        for c in data.get("course_catalog", []):
            if c.get("name").lower() == name.lower():
                payload = {"course_id": c.get("course_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "Course not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCourseByName",
                "description": "Find a course's ID by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
