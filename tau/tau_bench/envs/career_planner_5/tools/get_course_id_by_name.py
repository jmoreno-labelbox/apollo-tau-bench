# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_course_id_by_name(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], course_name: str) -> str:
        courses = data.get("course_catalog", [])
        # Find a course where the name contains the provided string (case-insensitive)
        course = next(
            (c for c in courses if course_name.lower() in c.get("name", "").lower()),
            None,
        )
        if course:
            return json.dumps({"course_id": course["course_id"]}, indent=2)
        return json.dumps(
            {"error": f"Course with name containing '{course_name}' not found"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_course_id_by_name",
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
