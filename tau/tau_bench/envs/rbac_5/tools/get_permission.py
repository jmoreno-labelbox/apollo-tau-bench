# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPermission(Tool):
    """
    Retrieve permissions by ID, action, or resource.

    kwargs:
      permission_id: str (optional) - Specific permission ID to retrieve
      action: str (optional) - Filter by permission action
      resource_id: str (optional) - Filter by resource involved in permissions
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        permission_id = kwargs.get("permission_id")
        action = kwargs.get("action")
        resource_id = kwargs.get("resource_id")
        description = kwargs.get("description")

        permissions = list(data.get("permissions", {}).values())

        # If permission_id is provided, return single permission
        if permission_id:
            permission = _find_by_id(permissions, "permission_id", permission_id)
            if not permission:
                return json.dumps({"error": f"permission_id {permission_id} not found"})
            return json.dumps({"ok": True, "permission": permission})

        # Filter permissions based on provided criteria
        filtered_permissions = []
        for permission in permissions:
            if action and permission.get("action") != action:
                continue
            if resource_id and permission.get("resource_id") != resource_id:
                continue
            if description and permission.get("description") != description:
                continue
            filtered_permissions.append(permission)

        return json.dumps({"ok": True, "permissions": filtered_permissions})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_permission",
                "description": "Retrieve permissions by ID, action, or resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {"type": "string", "description": "Specific permission ID to retrieve."},
                        "action": {"type": "string", "description": "Filter by permission action."},
                        "resource_id": {"type": "string", "description": "Filter by resource involved in permissions."},
                        "description": {"type": "string", "description": "Filter by permission description."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
