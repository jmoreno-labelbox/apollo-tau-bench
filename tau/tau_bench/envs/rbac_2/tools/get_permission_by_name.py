from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPermissionByName(Tool):
    """
    Locate a specific permission by its action name, with the option to filter by a resource ID.
    If resource_id is not provided, it will return the first permission that matches the name.
    """

    @staticmethod
    def invoke(data: dict[str, Any], permission_name: str = None, resource_id: str = None) -> str:
        try:
            permissions = data.get("permissions", {}).values()
        except (KeyError, json.JSONDecodeError):
            permissions = []

        for perm in permissions.values():
            if perm.get("action") == permission_name:
                if resource_id and perm.get("resource_id") != resource_id:
                    continue
                payload = perm
                out = json.dumps(payload)
                return out

        error_message = f"Permission '{permission_name}' not found."
        if resource_id:
            error_message += f" on resource '{resource_id}'"
        payload = {"error": error_message}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermissionByName",
                "description": "Retrieves the details of a specific permission by its action name (e.g., 'admin-db-cluster'). Can be optionally filtered by the resource it applies to.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_name": {
                            "type": "string",
                            "description": "The name of the action the permission allows (e.g., 'read-repo', 'admin-db-cluster').",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Optional. The ID of the resource to filter by (e.g., 'RES-025').",
                        },
                    },
                    "required": ["permission_name"],
                },
            },
        }
