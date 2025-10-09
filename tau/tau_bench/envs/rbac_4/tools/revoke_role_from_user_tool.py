from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RevokeRoleFromUserTool(Tool):
    """Remove a role from a user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None) -> str:
        uid = user_id
        rid = role_id
        user_roles = data.get("user_roles", [])
        to_remove = [
            ur for ur in user_roles if ur["user_id"] == uid and ur["role_id"] == rid
        ]
        if not to_remove:
            payload = {"error": "Role not found for user"}
            out = json.dumps(payload, indent=2)
            return out
        for rem in to_remove:
            user_roles.remove(rem)
        payload = {"success": f"Role {rid} revoked from user {uid}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeRole",
                "description": "Revokes a specific role from a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                    },
                    "required": ["user_id", "role_id"],
                },
            },
        }
