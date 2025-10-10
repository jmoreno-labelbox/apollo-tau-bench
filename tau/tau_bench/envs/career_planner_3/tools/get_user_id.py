# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        users = list(data.get("users", {}).values())
        user_name = kwargs.get("user_name")

        for user in users:
            if user.get("name") == user_name:
                return json.dumps({"user_id": user.get("user_id")})

        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_user_id",
                "description": "Search for user by name",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_name": {
                            "type": "string",
                            "description": "The full name of the user.",
                        }
                    },
                    "required": ["user_name"],
                },
            },
        }
