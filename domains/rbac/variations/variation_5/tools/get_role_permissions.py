from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

class GetRolePermissions(Tool):
    """
    Retrieve mappings of roles to permissions filtered by role_id and/or permission_id.

    kwargs:
      role_id: str (optional) - Filter mappings for a specific role
      permission_id: str (optional) - Filter mappings for a specific permission
      include_role: bool = False - Include role details in each mapping
      include_permission: bool = False - Include permission details in each mapping
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, permission_id: str = None, include_role: bool = False, include_permission: bool = False) -> str:
        if not role_id and not permission_id:
            payload = {"error": "Must provide role_id and/or permission_id"}
            out = json.dumps(payload)
            return out

        mappings = data.get("role_permissions", [])

        # Narrow down
        out = []
        for rp in mappings:
            if role_id and rp.get("role_id") != role_id:
                continue
            if permission_id and rp.get("permission_id") != permission_id:
                continue
            out.append(dict(rp))

        # Optional extensions
        if include_role or include_permission:
            role_map = {r.get("role_id"): r for r in data.get("roles", [])}
            perm_map = {p.get("permission_id"): p for p in data.get("permissions", [])}
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
        payload = {"ok": True, "role_permissions": out}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRolePermissions",
                "description": "Retrieve role-permission mappings filtered by role_id and/or permission_id with optional detail expansion.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "Filter by role_id (e.g., ROL-032).",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "Filter by permission_id (e.g., P-081).",
                        },
                        "include_role": {
                            "type": "boolean",
                            "description": "Include role details in each mapping.",
                            "default": False,
                        },
                        "include_permission": {
                            "type": "boolean",
                            "description": "Include permission details in each mapping.",
                            "default": False,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
