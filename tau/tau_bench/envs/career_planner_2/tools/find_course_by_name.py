# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCourseByName(Tool):
    """Find a course's ID by its name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        for c in data.get("course_catalog", []):
            if c.get("name").lower() == name.lower():
                return json.dumps({"course_id": c.get("course_id")})
        return json.dumps({"error": "Course not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_course_by_name",
                "description": "Find a course's ID by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
