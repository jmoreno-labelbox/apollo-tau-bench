from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindRolesByResourceId(Tool):
    """Locates all roles that provide permissions for a specific resource ID."""

    @staticmethod
    def invoke(data: dict[str, Any], role_permissions: list = None, permissions: list = None, resource_id: str = None) -> str:
        try:
            role_permissions = role_permissions if role_permissions is not None else data.get("role_permissions", [])
            permissions = permissions if permissions is not None else data.get("permissions", [])
        except:
            payload = {"error": "Data files not found."}
            out = json.dumps(payload)
            return out

        perm_ids_for_resource = {
            p["permission_id"]
            for p in permissions
            if p.get("resource_id") == resource_id
        }

        if not perm_ids_for_resource:
            payload = []
            out = json.dumps(payload)
            return out

        role_ids_for_resource = {
            rp["role_id"]
            for rp in role_permissions
            if rp.get("permission_id") in perm_ids_for_resource
        }
        payload = list(role_ids_for_resource)
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindRolesByResourceId",
                "description": "Returns a list of role IDs that are associated with a given resource ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource to find associated roles for.",
                        }
                    },
                    "required": ["resource_id"],
                },
            },
        }
