# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class log_course_completion(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], user_id: str, course_id: str, completion_date: str
    ) -> str:
        # Modify current course progress or generate a new entry.
        courses = data.get("user_course_progress", [])
        course = next(
            (
                c
                for c in courses
                if c.get("user_id") == user_id and c.get("course_id") == course_id
            ),
            None,
        )
        if course:
            course.update(
                {
                    "status": "Completed",
                    "completion_date": completion_date,
                    "current_progress_percent": 100,
                }
            )
        else:
            courses.append(
                {
                    "user_id": user_id,
                    "course_id": course_id,
                    "status": "Completed",
                    "completion_date": completion_date,
                    "current_progress_percent": 100,
                }
            )
        return json.dumps(
            {"success": f"Course {course_id} completion logged for user {user_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "log_course_completion",
                "description": "Log course completion for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "completion_date": {"type": "string"},
                    },
                    "required": ["user_id", "course_id", "completion_date"],
                },
            },
        }
