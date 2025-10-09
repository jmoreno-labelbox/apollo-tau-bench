from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPermissionsByResource(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None) -> str:
        for res in data.get("resources", []):
            if res.get("resource_id") == resource_id:
                resource_id = res.get("resource_id")
                break
        if not resource_id:
            payload = {"error": "Resource not found"}
            out = json.dumps(payload)
            return out

        perms = []
        for perm in data.get("permissions", []):
            if perm.get("resource_id") == resource_id:
                perms.append(perm)
        payload = perms
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermissionsByResource",
                "description": "Retrieves all permissions referencing a given resource.",
                "parameters": {
                    "type": "object",
                    "properties": {"resource_id": {"type": "string"}},
                    "required": ["resource_id"],
                },
            },
        }
