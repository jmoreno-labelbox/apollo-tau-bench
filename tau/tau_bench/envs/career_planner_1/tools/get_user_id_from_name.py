# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserIdFromName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str, last_name: str) -> str:
        users = list(data.get("users", {}).values())
        full_name = f"{first_name} {last_name}"
        for user in users:
            if user.get("name") == full_name:
                return json.dumps({"user_id": user["user_id"]}, indent=2)
        return json.dumps({"error": "User not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_user_id_from_name",
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
