# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemovePermission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        permission_id_to_remove = kwargs.get("permission_id")

        if not permission_id_to_remove:
            return json.dumps({"error": "permission_id must be provided."})

        permissions = list(data.get('permissions', {}).values())
        initial_permissions_len = len(permissions)
        updated_permissions = [p for p in permissions if p.get('permission_id') != permission_id_to_remove]

        if len(updated_permissions) == initial_permissions_len:
            return json.dumps({"error": "Permission not found."})

        data['permissions'] = updated_permissions

        role_permissions = data.get('role_permissions', [])
        updated_role_permissions = [rp for rp in role_permissions if rp.get('permission_id') != permission_id_to_remove]
        data['role_permissions'] = updated_role_permissions

        return json.dumps({"permission_id": permission_id_to_remove, "status": "removed"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_permission",
                "description": "Deletes a permission from the system, including its assignments to any roles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "The ID of the permission to be removed."
                        }
                    },
                    "required": ["permission_id"]
                }
            }
        }
