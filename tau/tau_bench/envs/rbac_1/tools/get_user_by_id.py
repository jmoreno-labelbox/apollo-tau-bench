# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        for user in list(data.get('users', {}).values()):
            if user.get('user_id') == user_id:
                return json.dumps(user)
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_user_by_id",
                        "description": "Retrieves user details based on user ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {
                                                "type": "string",
                                                "description": "The user ID to search for."
                                        }
                                },
                                "required": ["user_id"]
                        }
                }
        }
