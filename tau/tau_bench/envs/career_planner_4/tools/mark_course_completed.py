# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class mark_course_completed(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], user_id: str, course_id: str, completion_date: str
    ) -> str:
        progress = data.get("user_course_progress", [])
        user_progress = next(
            (
                p
                for p in progress
                if p.get("user_id") == user_id and p.get("course_id") == course_id
            ),
            None,
        )
        if user_progress:
            user_progress["status"] = "Completed"
            user_progress["completion_date"] = completion_date
            user_progress["current_progress_percent"] = 100
        else:
            new_progress = {
                "user_id": user_id,
                "course_id": course_id,
                "status": "Completed",
                "completion_date": completion_date,
                "current_progress_percent": 100,
            }
            progress.append(new_progress)
        return json.dumps(
            {"success": f"Course {course_id} marked completed for user {user_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "mark_course_completed",
                "description": "Mark a course as completed for a user",
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
