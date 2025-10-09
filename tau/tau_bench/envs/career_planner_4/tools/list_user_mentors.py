from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ListUserMentors(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        mentorships = [
            m
            for m in data.get("user_mentorship_relationships", [])
            if m.get("mentee_id") == user_id
        ]
        payload = {"mentorships": mentorships}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserMentors",
                "description": "List all mentors for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
