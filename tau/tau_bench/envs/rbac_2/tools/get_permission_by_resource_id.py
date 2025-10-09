from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPermissionByResourceId(Tool):
    """Locates all permissions linked to a specific resource ID."""

    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None) -> str:
        pass
        resource_id_to_find = resource_id
        try:
            all_permissions = data.get("permissions", {}).values()
        except (KeyError, json.JSONDecodeError):
            payload = []
            out = json.dumps(payload)
            return out

        matching_permissions = [
            perm
            for perm in all_permissions.values() if perm.get("resource_id") == resource_id_to_find
        ]
        payload = matching_permissions
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPermissionByResourceId",
                "description": "Retrieves a list of all permissions that are directly associated with a specific resource ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The unique ID of the resource to find permissions for (e.g., 'RES-032').",
                        }
                    },
                    "required": ["resource_id"],
                },
            },
        }
