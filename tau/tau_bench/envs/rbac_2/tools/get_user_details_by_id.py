# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserDetailsById(Tool):
    """Retrieves a user's full details using their unique user_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        try:
           users = list(data.get('users', {}).values())
        except (KeyError, json.JSONDecodeError):
            users = []

        for user in users:
            if user.get('user_id') == user_id:
                return json.dumps(user)

        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details_by_id",
                "description": "Retrieves full user details based on their unique user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user (e.g., U-001)."
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }
