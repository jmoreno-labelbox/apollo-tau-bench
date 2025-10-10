# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_user_mentors(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        mentorships = [
            m
            for m in data.get("user_mentorship_relationships", [])
            if m.get("mentee_id") == user_id
        ]
        return json.dumps({"mentorships": mentorships}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_mentors",
                "description": "List all mentors for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
