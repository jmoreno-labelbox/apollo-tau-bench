from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserRoleDetailsByUserRoleId(Tool):
    """Fetches the details of a specific user role assignment using its user_role_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_role_id: str = None) -> str:
        try:
            user_roles = data.get("user_roles", [])
        except:
            user_roles = []

        for user_role in user_roles:
            if user_role.get("user_role_id") == user_role_id:
                payload = user_role
                out = json.dumps(payload)
                return out
        payload = {"error": f"User role with ID '{user_role_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRoleDetailsByUserRoleId",
                "description": "Retrieves the full details of a specific user role assignment by its user_role_id (e.g., 'UR-029').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_role_id": {
                            "type": "string",
                            "description": "The unique identifier of the user role assignment to retrieve (e.g., 'UR-029').",
                        }
                    },
                    "required": ["user_role_id"],
                },
            },
        }
