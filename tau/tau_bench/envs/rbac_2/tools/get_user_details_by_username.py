# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserDetailsByUsername(Tool):
    """Retrieves a user's full details using their username."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        username = kwargs.get("username")
        try:
           users = list(data.get('users', {}).values())
        except (KeyError, json.JSONDecodeError):
            users = []

        for user in users:
            if user.get('username') == username:
                return json.dumps(user)

        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details_by_username",
                "description": "Retrieves full user details based on their username.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The username to search for."
                        }
                    },
                "required": ["username"]
                }
            }
        }
