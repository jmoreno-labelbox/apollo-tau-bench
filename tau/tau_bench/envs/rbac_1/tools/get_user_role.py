from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_name: str = None) -> str:
        role_id = None
        for role in data.get("roles", []):
            if role.get("role_name") == role_name:
                role_id = role.get("role_id")
                break
        if not role_id:
            payload = {"error": "Role not found"}
            out = json.dumps(payload)
            return out

        for ur in data.get("user_roles", []):
            if ur.get("user_id") == user_id and ur.get("role_id") == role_id:
                payload = ur
                out = json.dumps(payload)
                return out
        payload = {"error": "User role assignment not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRoles",
                "description": "Retrieves a specific role assignment for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_name": {"type": "string"},
                    },
                    "required": ["user_id", "role_name"],
                },
            },
        }
