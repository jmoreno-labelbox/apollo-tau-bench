# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class assign_mentor(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str = "",
        mentor_id: str = "",
        mentee_id: str = "",
        focus_areas: list = [],
        start_date: str = "",
    ) -> str:
        mentee = user_id or mentee_id
        relationship = {
            "relationship_id": f"MR{int(datetime.now().timestamp() * 1000) % 10000}",
            "mentor_id": mentor_id,
            "mentee_id": mentee,
            "focus_areas": focus_areas or [],
            "start_date": start_date,
            "status": "Active",
        }
        data.setdefault("user_mentorship_relationships", []).append(relationship)
        return json.dumps(
            {"success": f"Mentor {mentor_id} assigned to {mentee}"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "assign_mentor",
                "description": "Assign a mentor to a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "mentor_id": {"type": "string"},
                        "mentee_id": {"type": "string"},
                        "focus_areas": {"type": "array", "items": {"type": "string"}},
                        "start_date": {"type": "string"},
                    },
                    "required": ["mentor_id"],
                },
            },
        }
