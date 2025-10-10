# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchCourses(Tool):
    """Search for courses by skill."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        skill_query = kwargs.get("skill")
        # Corrected to search 'related_skills' and perform a case-insensitive comparison
        courses = [
            c
            for c in data.get("course_catalog", [])
            if skill_query.lower() in [s.lower() for s in c.get("related_skills", [])]
        ]
        return json.dumps(courses, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_courses",
                "description": "Search for courses by skill.",
                "parameters": {
                    "type": "object",
                    "properties": {"skill": {"type": "string"}},
                    "required": ["skill"],
                },
            },
        }
