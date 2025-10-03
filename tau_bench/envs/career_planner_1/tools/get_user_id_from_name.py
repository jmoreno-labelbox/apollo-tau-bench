from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetUserIdFromName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], first_name: str, last_name: str) -> str:
        users = data.get("users", [])
        full_name = f"{first_name} {last_name}"
        for user in users:
            if user.get("name") == full_name:
                payload = {"user_id": user["user_id"]}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetUserIdFromName",
                "description": "Get user ID from first and last name",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }
