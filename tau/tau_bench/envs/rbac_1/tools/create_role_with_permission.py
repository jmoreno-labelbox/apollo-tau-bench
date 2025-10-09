from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class CreateRoleWithPermission(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        permission_name: str,
        resource_id: str,
        permission_description: str = None,
        role_name: str = None,
        role_description: str = None
    ) -> str:
        permissions = data.get("permissions", [])
        roles = data.get("roles", [])
        role_permissions = data.get("role_permissions", [])

        new_perm_id_num = (
            max((int(p["permission_id"][2:]) for p in permissions), default=0) + 1
        )
        new_perm_id = f"P-{new_perm_id_num:03d}"
        new_permission = {
            "permission_id": new_perm_id,
            "action": permission_name,
            "resource_id": resource_id,
            "description": permission_description or f"Permission for the '{role_name}' role.",
        }
        permissions.append(new_permission)
        data["permissions"] = permissions

        new_role_id_num = max((int(r["role_id"][4:]) for r in roles), default=0) + 1
        new_role_id = f"ROL-{new_role_id_num:03d}"
        new_role = {
            "role_id": new_role_id,
            "role_name": role_name,
            "description": role_description or f"Role with permission '{permission_name}'.",
            "is_temporary": False,
        }
        roles.append(new_role)
        data["roles"] = roles

        new_assignment = {"role_id": new_role_id, "permission_id": new_perm_id}
        role_permissions.append(new_assignment)
        data["role_permissions"] = role_permissions
        payload = {"permission_id": new_perm_id, "role_id": new_role_id, "status": "success"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRoleWithPermission",
                "description": "Creates a new permission and a new role, then assigns the permission to the role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "The name for the new role (e.g., 'special-report-viewer').",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource the permission applies to.",
                        },
                        "permission_name": {
                            "type": "string",
                            "description": "The name of the action for the new permission (e.g., 'read-special-report').",
                        },
                        "permission_description": {
                            "type": "string",
                            "description": "An optional description for the new permission.",
                        },
                        "role_description": {
                            "type": "string",
                            "description": "An optional description for the new role.",
                        },
                    },
                    "required": ["permission_name", "role_name", "resource_id"],
                },
            },
        }
