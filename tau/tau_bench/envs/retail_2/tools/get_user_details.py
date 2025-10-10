# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserDetails(Tool):
    """Retrieve full user details from users.json by user_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        users = list(data.get("users", {}).values())
        for user in users:
            if user.get("user_id") == user_id:
                return json.dumps(user)
        return json.dumps({"error": "User not found", "user_id": user_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get user details from users.json by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"}
                    },
                    "required": ["user_id"]
                }
            }
        }
