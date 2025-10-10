# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserRolesByUserId(Tool):
    """ Retrieves all role assignments for a specific user ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        try:
            user_roles = data.get('user_roles', [])
        except:
            user_roles = []

        assigned_roles = [
            role for role in user_roles
            if role.get("user_id") == user_id
        ]

        return json.dumps(assigned_roles)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_roles_by_user_id",
                "description": "Lists all roles currently assigned to a specific user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose roles are to be listed."
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }
