from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetUserProfile(Tool):
    """Retrieve an employee's profile using their ID."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        uid = user_id
        for u in data.get("users", []):
            if u.get("user_id") == uid:
                payload = u
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserProfile",
                "description": "Fetch user profile.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
