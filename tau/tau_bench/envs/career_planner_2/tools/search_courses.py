from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchCourses(Tool):
    """Look for courses based on skill."""

    @staticmethod
    def invoke(data: dict[str, Any], skill: str) -> str:
        skill_query = skill
        # Adjusted to look for 'related_skills' and conduct a case-insensitive check
        courses = [
            c
            for c in data.get("course_catalog", {}).values()
            if skill_query.lower() in [s.lower() for s in c.get("related_skills", [])]
        ]
        payload = courses
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchCourses",
                "description": "Search for courses by skill.",
                "parameters": {
                    "type": "object",
                    "properties": {"skill": {"type": "string"}},
                    "required": ["skill"],
                },
            },
        }
