from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUserDetailsTool(Tool):
    """Retrieve full user information."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        uid = user_id
        for u in data.get("users", []):
            if u["user_id"] == uid:
                payload = u
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"user_id {uid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserDetails",
                "description": "Get full details of a user by their user_id",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
