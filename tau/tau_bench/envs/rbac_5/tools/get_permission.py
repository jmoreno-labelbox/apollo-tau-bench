from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPermission(Tool):
    """
    Retrieve permissions based on ID, action, or resource.

    kwargs:
      permission_id: str (optional) - Specific permission ID to retrieve
      action: str (optional) - Filter by the action of the permission
      resource_id: str (optional) - Filter by the resource associated with permissions
    """

    @staticmethod
    def invoke(data: dict[str, Any], permission_id: str = None, action: str = None, resource_id: str = None, description: str = None) -> str:
        permissions = data.get("permissions", {}).values()

        # If permission_id is supplied, return the specific permission
        if permission_id:
            permission = _find_by_id(permissions, "permission_id", permission_id)
            if not permission:
                payload = {"error": f"permission_id {permission_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "permission": permission}
            out = json.dumps(payload)
            return out

        # Narrow down permissions according to the supplied criteria
        filtered_permissions = []
        for permission in permissions.values():
            if action and permission.get("action") != action:
                continue
            if resource_id and permission.get("resource_id") != resource_id:
                continue
            if description and permission.get("description") != description:
                continue
            filtered_data["permissions"][permission_id] = permission
        payload = {"ok": True, "permissions": filtered_permissions}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermission",
                "description": "Retrieve permissions by ID, action, or resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "Specific permission ID to retrieve.",
                        },
                        "action": {
                            "type": "string",
                            "description": "Filter by permission action.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Filter by resource involved in permissions.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Filter by permission description.",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
