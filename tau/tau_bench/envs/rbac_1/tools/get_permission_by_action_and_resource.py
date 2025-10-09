from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPermissionByActionAndResource(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], action: str = None, resource_name: str = None) -> str:
        resource_id = None
        for res in data.get("resources", {}).values():
            if res.get("name") == resource_name:
                resource_id = res.get("resource_id")
                break
        if not resource_id:
            payload = {"error": "Resource not found"}
            out = json.dumps(payload)
            return out

        for perm in data.get("permissions", {}).values():
            if perm.get("action") == action and perm.get("resource_id") == resource_id:
                payload = perm
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
                "name": "getPermissionByActionAndResource",
                "description": "Retrieves a permission based on its action and resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string"},
                        "resource_name": {"type": "string"},
                    },
                    "required": ["action", "resource_name"],
                },
            },
        }
