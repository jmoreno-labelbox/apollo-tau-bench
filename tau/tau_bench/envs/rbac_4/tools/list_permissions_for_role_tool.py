from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListPermissionsForRoleTool(Tool):
    """Display permissions associated with a role_id (read operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        role_permissions = data.get("role_permissions", [])
        permissions = data.get("permissions", [])
        if not isinstance(role_permissions, list):
            payload = {"error": "role_permissions must be a list"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(permissions, list):
            payload = {"error": "permissions must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        roles = data.get("roles", [])
        if not any(r.get("role_id") == role_id for r in roles):
            payload = {"error": f"role_id {role_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(role_id, str) or not role_id.strip():
            payload = {"error": "role_id must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out

        perm_ids = [
            rp.get("permission_id")
            for rp in role_permissions
            if rp.get("role_id") == role_id
        ]
        results = [p for p in permissions if p.get("permission_id") in perm_ids]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPermissionsForRole",
                "description": "List permission records attached to the given role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }
