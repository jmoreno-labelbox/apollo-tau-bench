# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        new_username = kwargs.get("new_username")
        new_email = kwargs.get("new_email")

        for user in list(data.get('users', {}).values()):
            if user.get('user_id') == user_id:
                if new_username:
                    user['username'] = new_username
                if new_email:
                    user['email'] = new_email
                return json.dumps(user)
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_user_details",
                        "description": "Updates a user's username and/or email address.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "new_username": {"type": "string"},
                                        "new_email": {"type": "string"}
                                },
                                "required": ["user_id"]
                        }
                }
        }
