# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignCourseToUser(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs["user_id"]
        course_id = kwargs["course_id"]

        # Generate deterministic date based on user_id and course_id
        import hashlib

        hash_input = f"{user_id}_{course_id}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest()[:8], 16)
        days_offset = hash_value % 30  # 0-29 days from base date

        # Use a fixed base date for deterministic results
        base_date = "2025-07-01"
        from datetime import datetime, timedelta

        base_dt = datetime.strptime(base_date, "%Y-%m-%d")
        assigned_date = (base_dt + timedelta(days=days_offset)).strftime("%Y-%m-%d")

        progress_entry = {
            "user_id": user_id,
            "course_id": course_id,
            "status": "assigned",
            "assigned_date": assigned_date,
        }

        data.setdefault("user_course_progress", []).append(progress_entry)
        return json.dumps(
            {"message": "Course assigned to user.", "entry": progress_entry}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_course_to_user",
                "description": "Assigns a course to a user and logs it in course progress with deterministic date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user receiving the course assignment.",
                        },
                        "course_id": {
                            "type": "string",
                            "description": "The ID of the course to assign.",
                        },
                    },
                    "required": ["user_id", "course_id"],
                },
            },
        }
