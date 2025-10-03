from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ListUserMentorships(Tool):
    @staticmethod
    def invoke(data, user_id: str, user_mentorship_relationships: list = None) -> str:
        if user_mentorship_relationships is None:
            user_mentorship_relationships = data.get("user_mentorship_relationships", [])
        rels = [
            rel
            for rel in user_mentorship_relationships
            if rel.get("mentee_id") == user_id
        ]
        payload = {"mentorships": rels}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListUserMentorships",
                "description": "List all mentorship relationships for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
