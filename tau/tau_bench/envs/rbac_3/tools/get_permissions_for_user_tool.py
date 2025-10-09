from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPermissionsForUserTool(Tool):
    """GetPermissionsForUser"""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        roles_active = [
            r.get("role_id")
            for r in data.get("user_roles", [])
            if r.get("user_id") == user_id and not r.get("expires_on")
        ]
        role_perms = data.get("role_permissions", [])
        perms = data.get("permissions", [])
        perm_map = {p.get("permission_id"): p for p in perms}
        seen = set()
        result: list[dict[str, Any]] = []
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
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermissionsForUser",
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
