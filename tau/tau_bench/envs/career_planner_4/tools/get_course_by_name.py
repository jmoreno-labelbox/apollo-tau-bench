# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_course_by_name(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], course_name: str) -> str:
        courses = data.get("course_catalog", [])

        # Attempt an exact match initially.
        course = next(
            (c for c in courses if c.get("name", "").lower() == course_name.lower()),
            None,
        )

        # If an exact match is unavailable, attempt a partial match.
        if not course:
            course = next(
                (
                    c
                    for c in courses
                    if course_name.lower() in c.get("name", "").lower()
                ),
                None,
            )

        if course:
            return json.dumps(
                {
                    "course_found": True,
                    "course_id": course.get("course_id"),
                    "course_name": course.get("name"),
                    "provider": course.get("provider"),
                    "level": course.get("level"),
                },
                indent=2,
            )
        else:
            return json.dumps(
                {
                    "course_found": False,
                    "error": f"Course '{course_name}' not found",
                    "suggestion": "Try using partial course name or check course catalog",
                },
                indent=2,
            )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_course_by_name",
                "description": "Find course ID by course name (exact or partial match)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "course_name": {
                            "type": "string",
                            "description": "Full or partial course name to search for",
                        }
                    },
                    "required": ["course_name"],
                },
            },
        }
