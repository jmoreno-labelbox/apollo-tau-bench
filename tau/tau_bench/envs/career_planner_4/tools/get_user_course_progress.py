# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_user_course_progress(Tool):
    @staticmethod
    def invoke(data, user_id: str, course_id: str):
        # Minimal simulation: Return a mock object with "status" or "grade"
        # In real usage, we would look up user_course_progress in data
        return json.dumps(
            {"user_course_progress": {"status": "Not Completed", "grade": 0}}, indent=2
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_user_course_progress",
                "description": "Fetch the user's progress record for a specific course.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                    },
                    "required": ["user_id", "course_id"],
                },
            },
        }
