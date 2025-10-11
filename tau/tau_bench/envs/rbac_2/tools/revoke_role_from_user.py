# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RevokeRoleFromUser(Tool):
    """ Revokes a specific role from a user by deleting the user-role entry from the database."""

    @staticmethod
    def invoke(data: Dict[str, Any], user_role_id) -> str:
        try:
            user_roles = data.get('user_roles', [])
        except:
            user_roles = []

        index = -1
        for i, assignment in enumerate(user_roles):
            if assignment.get("user_role_id") == user_role_id:
                index = i
                break

        if index != -1:
            revoked_assignment = user_roles.pop(index)
        else:
            return json.dumps({"error": f"User-role with ID '{user_role_id}' not found."})

        data['user_roles'] = user_roles

        return json.dumps({
            "message": "User-role assignment revoked successfully.",
            "revoked_details": revoked_assignment
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_role_from_user",
                "description": "Revokes a specific role from a user by deleting the assignment record. Requires the user_role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_role_id": {
                            "type": "string",
                            "description": "The unique ID of the user-role assignment to be revoked (e.g., 'UR-003')."
                        }
                    },
                    "required": ["user_role_id"]
                }
            }
        }
