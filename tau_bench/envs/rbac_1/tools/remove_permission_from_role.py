from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class RemovePermissionFromRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, permission_id: str = None) -> str:
        if not role_id or not permission_id:
            payload = {"error": "Both role_id and permission_id must be provided."}
            out = json.dumps(payload)
            return out

        role_permissions = data.get("role_permissions", [])

        initial_len = len(role_permissions)

        updated_permissions = [
            rp
            for rp in role_permissions
            if not (
                rp.get("role_id") == role_id
                and rp.get("permission_id") == permission_id
            )
        ]

        if len(updated_permissions) < initial_len:
            data["role_permissions"] = updated_permissions
            payload = {
                "role_id": role_id,
                "permission_id": permission_id,
                "status": "removed",
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": "Permission not found on the specified role."}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemovePermissionFromRole",
                "description": "Removes a specific permission from a role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The ID of the role to modify.",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "The ID of the permission to remove.",
                        },
                    },
                    "required": ["role_id", "permission_id"],
                },
            },
        }
