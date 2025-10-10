# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignPermissionToRole(Tool):
    """
    Assign a permission to a role by creating a role-permission mapping.

    kwargs:
      role_id: str (required)
      permission_id: str (required)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = (kwargs.get("role_id", "") or "").strip()
        permission_id = (kwargs.get("permission_id", "") or "").strip()

        if not role_id or not permission_id:
            return json.dumps({"error": "role_id and permission_id are required"})

        # Check for presence
        if not _find_by_id(list(data.get("roles", {}).values()), "role_id", role_id):
            return json.dumps({"error": f"role_id {role_id} not found"})
        if not _find_by_id(list(data.get("permissions", {}).values()), "permission_id", permission_id):
            return json.dumps({"error": f"permission_id {permission_id} not found"})

        # Verify the presence of a mapping.
        mappings = data.get("role_permissions", [])
        for rp in mappings:
            if rp.get("role_id") == role_id and rp.get("permission_id") == permission_id:
                return json.dumps({"ok": True, "role_permission": rp, "no_op": True})

        new_mapping = {"role_id": role_id, "permission_id": permission_id}
        data.setdefault("role_permissions", []).append(new_mapping)
        return json.dumps({"ok": True, "role_permission": new_mapping, "action": "created"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_permission_to_role",
                "description": "Assign a permission to a role by creating a role-permission mapping.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string", "description": "Target role_id (e.g., ROL-030)."},
                        "permission_id": {"type": "string", "description": "Target permission_id (e.g., P-113)."}
                    },
                    "required": ["role_id", "permission_id"],
                    "additionalProperties": False
                }
            }
        }
