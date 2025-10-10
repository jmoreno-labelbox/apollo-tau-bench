# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class schedule_mentorship_session(Tool):
    @staticmethod
    def invoke(data, relationship: dict) -> str:
        data.setdefault("user_mentorship_relationships", []).append(relationship)
        return json.dumps(
            {
                "success": f"Mentorship session {relationship['relationship_id']} scheduled"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "schedule_mentorship_session",
                "description": "Schedule a new mentorship session by adding a new relationship record.",
                "parameters": {
                    "type": "object",
                    "properties": {"relationship": {"type": "object"}},
                    "required": ["relationship"],
                },
            },
        }
