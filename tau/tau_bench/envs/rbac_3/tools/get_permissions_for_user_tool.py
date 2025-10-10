# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPermissionsForUserTool(Tool):
    """get_permissions_for_user"""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        roles_active = [
            r.get("role_id")
            for r in data.get("user_roles", [])
            if r.get("user_id") == user_id and not r.get("expires_on")
        ]
        role_perms = data.get("role_permissions", [])
        perms = list(data.get("permissions", {}).values())
        perm_map = {p.get("permission_id"): p for p in perms}
        seen = set()
        result: List[Dict[str, Any]] = []
        for rp in role_perms:
            if rp.get("role_id") in roles_active:
                p = perm_map.get(rp.get("permission_id"))
                if p and p.get("permission_id") not in seen:
                    seen.add(p.get("permission_id"))
                    result.append(
                        {
                            "permission_id": p.get("permission_id"),
                            "action": p.get("action"),
                            "resource_id": p.get("resource_id"),
                        }
                    )
        result = sorted(result, key=lambda p: (p.get("permission_id") or ""))
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_permissions_for_user",
                "description": (
                    "Resolve permissions for a user via user_roles → role_permissions → permissions."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
