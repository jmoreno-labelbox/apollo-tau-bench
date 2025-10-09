from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AssignPermissionToRole(Tool):
    """
    Allocate a permission to a role by establishing a role-permission mapping.

    kwargs:
      role_id: str (mandatory)
      permission_id: str (mandatory)
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = "", permission_id: str = "") -> str:
        role_id = role_id.strip()
        permission_id = permission_id.strip()

        if not role_id or not permission_id:
            payload = {"error": "role_id and permission_id are required"}
            out = json.dumps(payload)
            return out

        # Confirm presence
        if not _find_by_id(data.get("roles", {}).values(), "role_id", role_id):
            payload = {"error": f"role_id {role_id} not found"}
            out = json.dumps(payload)
            return out
        if not _find_by_id(data.get("permissions", {}).values(), "permission_id", permission_id):
            payload = {"error": f"permission_id {permission_id} not found"}
            out = json.dumps(payload)
            return out

        # Verify if the mapping is present
        mappings = data.get("role_permissions", {}).values()
        for rp in mappings.values():
            if (
                rp.get("role_id") == role_id
                and rp.get("permission_id") == permission_id
            ):
                payload = {"ok": True, "role_permission": rp, "no_op": True}
                out = json.dumps(payload)
                return out

        new_mapping = {"role_id": role_id, "permission_id": permission_id}
        data.setdefault("role_permissions", []).append(new_mapping)
        payload = {"ok": True, "role_permission": new_mapping, "action": "created"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignPermissionToRole",
                "description": "Assign a permission to a role by creating a role-permission mapping.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "Target role_id (e.g., ROL-030).",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "Target permission_id (e.g., P-113).",
                        },
                    },
                    "required": ["role_id", "permission_id"],
                    "additionalProperties": False,
                },
            },
        }
