from tau_bench.envs.tool import Tool
import json
from typing import Any

class AssignCourseToUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, course_id: str) -> str:
        # Create a consistent date based on user_id and course_id
        import hashlib

        hash_input = f"{user_id}_{course_id}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest()[:8], 16)
        days_offset = hash_value % 30  # A span of 0 to 29 days from the reference date

        # Utilize a stable base date for reliable results
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
        payload = {"message": "Course assigned to user.", "entry": progress_entry}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignCourseToUser",
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
