# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserRoleDetailsByUserRoleId(Tool):
    """ Retrieves the details of a specific user role assignment by its user_role_id. """

    @staticmethod
    def invoke(data: Dict[str, Any], user_role_id) -> str:
        try:
            user_roles = data.get("user_roles", [])
        except:
            user_roles = []

        for user_role in user_roles:
            if user_role.get("user_role_id") == user_role_id:
                return json.dumps(user_role)

        return json.dumps({"error": f"User role with ID \'{user_role_id}\' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_role_details_by_user_role_id",
                "description": "Retrieves the full details of a specific user role assignment by its user_role_id (e.g., \'UR-029\').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_role_id": {
                            "type": "string",
                            "description": "The unique identifier of the user role assignment to retrieve (e.g., \'UR-029\')."
                        }
                    },
                    "required": ["user_role_id"]
                }
            }
        }
