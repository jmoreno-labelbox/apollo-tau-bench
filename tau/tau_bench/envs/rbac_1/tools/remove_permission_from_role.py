# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemovePermissionFromRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], permission_id, role_id) -> str:

        if not role_id or not permission_id:
            return json.dumps({"error": "Both role_id and permission_id must be provided."})

        role_permissions = data.get('role_permissions', [])

        initial_len = len(role_permissions)

        updated_permissions = [
                rp for rp in role_permissions
                if not (rp.get('role_id') == role_id and rp.get('permission_id') == permission_id)
        ]

        if len(updated_permissions) < initial_len:
            data['role_permissions'] = updated_permissions
            return json.dumps({"role_id": role_id, "permission_id": permission_id, "status": "removed"})
        else:
            return json.dumps({"error": "Permission not found on the specified role."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "remove_permission_from_role",
                        "description": "Removes a specific permission from a role.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_id": {
                                                "type": "string",
                                                "description": "The ID of the role to modify."
                                        },
                                        "permission_id": {
                                                "type": "string",
                                                "description": "The ID of the permission to remove."
                                        }
                                },
                                "required": ["role_id", "permission_id"]
                        }
                }
        }
