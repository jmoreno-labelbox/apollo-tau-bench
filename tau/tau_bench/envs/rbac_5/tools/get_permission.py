# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_by_id(items: List[Dict[str, Any]], key: str, value: str) -> Optional[Dict[str, Any]]:
    for it in items or []:
        if it.get(key) == value:
            return it
    return None

class GetPermission(Tool):
    """
    Retrieve permissions by ID, action, or resource.

    kwargs:
      permission_id: str (optional) - Specific permission ID to retrieve
      action: str (optional) - Filter by permission action
      resource_id: str (optional) - Filter by resource involved in permissions
    """
    @staticmethod
    def invoke(data: Dict[str, Any], action, description, permission_id, resource_id) -> str:

        permissions = list(data.get("permissions", {}).values())

        # Return a single permission if permission_id is given.
        if permission_id:
            permission = _find_by_id(permissions, "permission_id", permission_id)
            if not permission:
                return json.dumps({"error": f"permission_id {permission_id} not found"})
            return json.dumps({"ok": True, "permission": permission})

        # Restrict permissions according to specified parameters.
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