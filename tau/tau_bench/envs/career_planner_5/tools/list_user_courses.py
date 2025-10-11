# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_user_courses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        courses = [
            c
            for c in data.get("user_course_progress", [])
            if c.get("user_id") == user_id
        ]
        return json.dumps({"courses": courses}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_courses",
                "description": "List all courses for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
