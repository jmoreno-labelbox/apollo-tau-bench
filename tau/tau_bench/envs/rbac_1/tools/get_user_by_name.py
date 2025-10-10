# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        first_name = kwargs.get("first_name", "").lower()
        last_name = kwargs.get("last_name", "").lower()
        username_to_find = f"{first_name[0]}{last_name}" if first_name else last_name
        for user in list(data.get('users', {}).values()):
            if user.get('username') == username_to_find:
                return json.dumps(user)
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_user_by_name",
                        "description": "Retrieves user details based on their first and last name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "first_name": {
                                                "type": "string",
                                                "description": "The first name of the user."
                                        },
                                        "last_name": {
                                                "type": "string",
                                                "description": "The last name of the user."
                                        }
                                },
                                "required": ["first_name", "last_name"]
                        }
                }
        }
