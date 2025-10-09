from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindResourcesByRoleId(Tool):
    """Identifies all resource IDs that a specific role provides permissions for."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        try:
            role_permissions = data.get("role_permissions", {}).values()
            permissions = data.get("permissions", {}).values()
        except:
            payload = {"error": "Data files not found."}
            out = json.dumps(payload)
            return out

        perm_ids_for_role = {
            rp["permission_id"]
            for rp in role_permissions.values() if rp.get("role_id") == role_id
        }

        if not perm_ids_for_role:
            payload = []
            out = json.dumps(payload)
            return out

        resource_ids = {
            p["resource_id"]
            for p in permissions.values() if p.get("permission_id") in perm_ids_for_role
        }
        payload = list(resource_ids)
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindResourcesByRoleId",
                "description": "Returns a list of all unique resource IDs that a specific role has permissions for.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The ID of the role to find associated resources for.",
                        }
                    },
                    "required": ["role_id"],
                },
            },
        }
