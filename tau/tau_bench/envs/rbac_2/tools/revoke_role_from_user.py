from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class RevokeRoleFromUser(Tool):
    """Removes a specific role from a user by eliminating the user-role record from the database."""

    @staticmethod
    def invoke(data: dict[str, Any], user_role_id: str = None) -> str:
        try:
            user_roles = data.get("user_roles", [])
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
            payload = {"error": f"User-role with ID '{user_role_id}' not found."}
            out = json.dumps(payload)
            return out

        data["user_roles"] = user_roles
        payload = {
            "message": "User-role assignment revoked successfully.",
            "revoked_details": revoked_assignment,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeRoleFromUser",
                "description": "Revokes a specific role from a user by deleting the assignment record. Requires the user_role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_role_id": {
                            "type": "string",
                            "description": "The unique ID of the user-role assignment to be revoked (e.g., 'UR-003').",
                        }
                    },
                    "required": ["user_role_id"],
                },
            },
        }
