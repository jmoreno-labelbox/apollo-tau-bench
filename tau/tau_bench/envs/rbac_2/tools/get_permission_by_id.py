from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPermissionById(Tool):
    """Retrieve complete details of a specific permission by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], permission_id: str = None) -> str:
        try:
            permissions = data.get("permissions", [])
        except (KeyError, json.JSONDecodeError):
            permissions = []

        for perm in permissions:
            if perm.get("permission_id") == permission_id:
                payload = perm
                out = json.dumps(payload)
                return out
        payload = {"error": f"Permission with ID '{permission_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermissionById",
                "description": "Retrieves the full details of a specific permission (action, resource_id) using its unique permission_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "The unique ID of the permission to retrieve (e.g., 'P-021').",
                        }
                    },
                    "required": ["permission_id"],
                },
            },
        }
