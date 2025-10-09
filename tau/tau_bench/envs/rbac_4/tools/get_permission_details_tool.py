from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPermissionDetailsTool(Tool):
    """Retrieve comprehensive information about a permission using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], permission_id: str = None) -> str:
        for p in data.get("permissions", {}).values():
            if p["permission_id"] == permission_id:
                payload = p
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Permission {permission_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermissionDetails",
                "description": "Get full permission record from permission_id",
                "parameters": {
                    "type": "object",
                    "properties": {"permission_id": {"type": "string"}},
                    "required": ["permission_id"],
                },
            },
        }
