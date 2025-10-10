# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListUserMentorships(Tool):
    @staticmethod
    def invoke(data, user_id: str) -> str:
        rels = [
            rel
            for rel in data.get("user_mentorship_relationships", [])
            if rel.get("mentee_id") == user_id
        ]
        return json.dumps({"mentorships": rels}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_mentorships",
                "description": "List all mentorship relationships for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
