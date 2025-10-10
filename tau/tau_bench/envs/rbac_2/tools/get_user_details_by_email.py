# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserDetailsByEmail(Tool):
    """Retrieves a user's full details using their email address."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email = kwargs.get("email")
        try:
            users = list(data.get('users', {}).values())
        except (KeyError, json.JSONDecodeError):
            users = []

        for user in users:
            if user.get('email') == email:
                return json.dumps(user)

        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details_by_email",
                "description": "Retrieves full user details based on their email address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "The email address to search for."
                        }
                    },
                "required": ["email"]
                }
            }
        }
