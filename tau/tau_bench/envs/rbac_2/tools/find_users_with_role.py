# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindUsersWithRole(Tool):
    """ Find all users who are currently assigned a specific role. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        try:
            all_user_roles = data.get('user_roles', [])
        except:
            all_user_roles = []

        users_with_role = [
            assignment["user_id"] for assignment in all_user_roles
            if assignment.get("role_id") == role_id
        ]
        unique_user_ids = list(set(users_with_role))
        
        return json.dumps(unique_user_ids)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_users_with_role",
                "description": "Finds and returns a list of all user IDs that are currently assigned a specific role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The unique ID of the role to search for (e.g., 'ROL-013')."
                        }
                    },
                    "required": ["role_id"]
                }
            }
        }
