# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRolePermissionsTool(Tool):
    """list_role_permissions"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs["role_id"]
        role_perms = data.get("role_permissions", [])
        perms = list(data.get("permissions", {}).values())
        perm_map = {p.get("permission_id"): p for p in perms}
        out = []
        for rp in role_perms:
            if rp.get("role_id") == role_id:
                p = perm_map.get(rp.get("permission_id"))
                if p:
                    out.append(
                        {
                            "permission_id": p.get("permission_id"),
                            "action": p.get("action"),
                            "resource_id": p.get("resource_id"),
                        }
                    )
        out = sorted(out, key=lambda p: (p.get("permission_id") or ""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_role_permissions",
                "description": "List permissions for a role.",
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }
