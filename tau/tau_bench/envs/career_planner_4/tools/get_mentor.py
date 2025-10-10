# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_mentor(Tool):
    @staticmethod
    def invoke(data, mentor_id: str) -> str:
        for mentor in data.get("user_mentorship", []):
            if mentor.get("mentor_id") == mentor_id:
                return json.dumps(mentor, indent=2)
        return json.dumps({"error": "Mentor not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_mentor",
                "description": "Fetch mentor details using mentor_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"mentor_id": {"type": "string"}},
                    "required": ["mentor_id"],
                },
            },
        }
