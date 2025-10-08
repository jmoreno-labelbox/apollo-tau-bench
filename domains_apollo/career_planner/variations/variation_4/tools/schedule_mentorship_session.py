from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ScheduleMentorshipSession(Tool):
    @staticmethod
    def invoke(data: dict, relationship: dict) -> str:
        data.setdefault("user_mentorship_relationships", []).append(relationship)
        payload = {
            "success": f"Mentorship session {relationship['relationship_id']} scheduled"
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "scheduleMentorshipSession",
                "description": "Schedule a new mentorship session by adding a new relationship record.",
                "parameters": {
                    "type": "object",
                    "properties": {"relationship": {"type": "object"}},
                    "required": ["relationship"],
                },
            },
        }
