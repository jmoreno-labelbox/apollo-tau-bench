from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class FindUsersWithRole(Tool):
    """Identify all users currently assigned to a specific role."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        try:
            all_user_roles = data.get("user_roles", [])
        except:
            all_user_roles = []

        users_with_role = [
            assignment["user_id"]
            for assignment in all_user_roles
            if assignment.get("role_id") == role_id
        ]
        unique_user_ids = list(set(users_with_role))
        payload = unique_user_ids
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindUsersWithRole",
                "description": "Finds and returns a list of all user IDs that are currently assigned a specific role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The unique ID of the role to search for (e.g., 'ROL-013').",
                        }
                    },
                    "required": ["role_id"],
                },
            },
        }
