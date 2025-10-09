from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RemoveRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        role_id_to_remove = role_id

        if not role_id_to_remove:
            payload = {"error": "role_id must be provided."}
            out = json.dumps(payload)
            return out

        roles = data.get("roles", {}).values()
        initial_roles_len = len(roles)
        updated_roles = [
            role for role in roles.values() if role.get("role_id") != role_id_to_remove
        ]

        if len(updated_roles) == initial_roles_len:
            payload = {"error": "Role not found."}
            out = json.dumps(payload)
            return out

        data["roles"] = updated_roles

        role_permissions = data.get("role_permissions", {}).values()
        updated_role_permissions = [
            rp for rp in role_permissions.values() if rp.get("role_id") != role_id_to_remove
        ]
        data["role_permissions"] = updated_role_permissions

        user_roles = data.get("user_roles", {}).values()
        updated_user_roles = [
            ur for ur in user_roles.values() if ur.get("role_id") != role_id_to_remove
        ]
        data["user_roles"] = updated_user_roles
        payload = {"role_id": role_id_to_remove, "status": "removed"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeRole",
                "description": "Deletes a role from the system, including all associated user and permission assignments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The ID of the role to be removed.",
                        }
                    },
                    "required": ["role_id"],
                },
            },
        }
