from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCourseByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], course_name: str) -> str:
        _course_nameL = course_name or ''.lower()
        pass
        courses = data.get("course_catalog", [])

        # Attempt an exact match initially
        course = next(
            (c for c in courses if c.get("name", "").lower() == course_name.lower()),
            None,
        )

        # If an exact match is not found, attempt a partial match
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
            payload = {
                "course_found": True,
                "course_id": course.get("course_id"),
                "course_name": course.get("name"),
                "provider": course.get("provider"),
                "level": course.get("level"),
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                "course_found": False,
                "error": f"Course '{course_name}' not found",
                "suggestion": "Try using partial course name or check course catalog",
            }
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
                "name": "getCourseByName",
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
