# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRolePermissions(Tool):
    """
    Retrieve role-permission mappings filtered by role_id and/or permission_id.

    kwargs:
      role_id: str (optional) - Filter mappings for a specific role
      permission_id: str (optional) - Filter mappings for a specific permission
      include_role: bool = False - Include role details in each mapping
      include_permission: bool = False - Include permission details in each mapping
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        permission_id = kwargs.get("permission_id")
        include_role = kwargs.get("include_role", False)
        include_permission = kwargs.get("include_permission", False)

        if not role_id and not permission_id:
            return json.dumps({"error": "Must provide role_id and/or permission_id"})

        mappings = data.get("role_permissions", [])

        # Refine
        out = []
        for rp in mappings:
            if role_id and rp.get("role_id") != role_id:
                continue
            if permission_id and rp.get("permission_id") != permission_id:
                continue
            out.append(dict(rp))

        # Optional extensions
        if include_role or include_permission:
            role_map = {r.get("role_id"): r for r in list(data.get("roles", {}).values())}
            perm_map = {p.get("permission_id"): p for p in list(data.get("permissions", {}).values())}
            for item in out:
                if include_role:
                    rid = item.get("role_id")
                    role = role_map.get(rid)
                    if role:
                        item["role"] = role
                if include_permission:
                    pid = item.get("permission_id")
                    perm = perm_map.get(pid)
                    if perm:
                        item["permission"] = perm

        return json.dumps({"ok": True, "role_permissions": out})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_permissions",
                "description": "Retrieve role-permission mappings filtered by role_id and/or permission_id with optional detail expansion.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string", "description": "Filter by role_id (e.g., ROL-032)."},
                        "permission_id": {"type": "string", "description": "Filter by permission_id (e.g., P-081)."},
                        "include_role": {"type": "boolean", "description": "Include role details in each mapping.", "default": False},
                        "include_permission": {"type": "boolean", "description": "Include permission details in each mapping.", "default": False}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
