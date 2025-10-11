# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserByEmail(Tool):
    """Retrieves a user's details by their email address."""
    @staticmethod
    def invoke(data: Dict[str, Any], email) -> str:
        users = list(data.get("users", {}).values())
        for user in users:
            if user.get("email") == email:
                return json.dumps(user)
        return json.dumps({"error": f"User with email '{email}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_by_email",
                "description": "Retrieves a user's details by their email address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "The email address of the user to find.",
                        }
                    },
                    "required": ["email"],
                },
            },
        }
