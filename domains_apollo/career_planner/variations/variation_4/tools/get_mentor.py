from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetMentor(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mentor_id: str) -> str:
        user_mentorship = data.get("user_mentorship", [])
        for mentor in user_mentorship:
            if mentor.get("mentor_id") == mentor_id:
                payload = mentor
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Mentor not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getMentor",
                "description": "Fetch mentor details using mentor_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"mentor_id": {"type": "string"}},
                    "required": ["mentor_id"],
                },
            },
        }
