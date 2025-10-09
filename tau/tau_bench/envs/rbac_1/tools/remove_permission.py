from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RemovePermission(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], permission_id: str = None) -> str:
        permission_id_to_remove = permission_id

        if not permission_id_to_remove:
            payload = {"error": "permission_id must be provided."}
            out = json.dumps(payload)
            return out

        permissions = data.get("permissions", {}).values()
        initial_permissions_len = len(permissions)
        updated_permissions = [
            p for p in permissions.values() if p.get("permission_id") != permission_id_to_remove
        ]

        if len(updated_permissions) == initial_permissions_len:
            payload = {"error": "Permission not found."}
            out = json.dumps(payload)
            return out

        data["permissions"] = updated_permissions

        role_permissions = data.get("role_permissions", {}).values()
        updated_role_permissions = [
            rp
            for rp in role_permissions.values() if rp.get("permission_id") != permission_id_to_remove
        ]
        data["role_permissions"] = updated_role_permissions
        payload = {"permission_id": permission_id_to_remove, "status": "removed"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removePermission",
                "description": "Deletes a permission from the system, including its assignments to any roles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "The ID of the permission to be removed.",
                        }
                    },
                    "required": ["permission_id"],
                },
            },
        }
