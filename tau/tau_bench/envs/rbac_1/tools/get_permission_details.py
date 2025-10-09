from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPermissionDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], permission_id: str = None, permission_name: str = None) -> str:
        if not permission_id and not permission_name:
            payload = {"error": "Either permission_id or permission_name must be provided."}
            out = json.dumps(payload)
            return out

        for permission in data.get("permissions", []):
            if permission_id and permission.get("permission_id") == permission_id:
                payload = permission
                out = json.dumps(payload)
                return out
            if permission_name and permission.get("action") == permission_name:
                payload = permission
                out = json.dumps(payload)
                return out
        payload = {"error": "Permission not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermissionDetails",
                "description": "Retrieves the full details of a permission by its ID or name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "The ID of the permission to retrieve.",
                        },
                        "permission_name": {
                            "type": "string",
                            "description": "The name (action) of the permission to retrieve.",
                        },
                    },
                },
            },
        }
