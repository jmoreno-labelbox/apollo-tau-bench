# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListPermissionsForRoleTool(Tool):
    """List permissions bound to a role_id (read operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_permissions = data.get("role_permissions", [])
        permissions = list(data.get("permissions", {}).values())
        if not isinstance(role_permissions, list):
            return json.dumps({"error": "role_permissions must be a list"}, indent=2)
        if not isinstance(permissions, list):
            return json.dumps({"error": "permissions must be a list"}, indent=2)

        role_id = kwargs.get("role_id")
        roles = list(data.get("roles", {}).values())
        if not any(r.get("role_id")==role_id for r in roles):
            return json.dumps({"error": f"role_id {role_id} not found"}, indent=2)
        if not isinstance(role_id, str) or not role_id.strip():
            return json.dumps({"error": "role_id must be a non-empty string"}, indent=2)

        perm_ids = [rp.get("permission_id") for rp in role_permissions if rp.get("role_id") == role_id]
        results = [p for p in permissions if p.get("permission_id") in perm_ids]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_permissions_for_role",
                "description": "List permission records attached to the given role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string"}
                    },
                    "required": ["role_id"]
                }
            }
        }
