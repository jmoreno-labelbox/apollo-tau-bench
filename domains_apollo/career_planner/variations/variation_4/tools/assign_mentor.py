from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class AssignMentor(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
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
        payload = {"success": f"Mentor {mentor_id} assigned to {mentee}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "assignMentor",
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
