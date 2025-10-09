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

class ListRolePermissionsTool(Tool):
    """list_role_permissions"""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, param1: str = None, param2: str = None) -> str:
        # Support both role_id and param1 (alias)
        role_id = role_id or param1
        role_perms = data.get("role_permissions", [])
        perms = data.get("permissions", [])
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRolePermissions",
                "description": "List permissions for a role.",
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }
