from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserRoles(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_name: str = None) -> str:
        assigned_role_ids = [
            ur["role_id"]
            for ur in data.get("user_roles", [])
            if ur.get("user_id") == user_id
        ]
        role_names = [
            role["role_name"]
            for role in data.get("roles", [])
            if role["role_id"] in assigned_role_ids
        ]
        payload = {"user_id": user_id, "roles": role_names}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRoles",
                "description": "Retrieves all roles assigned to a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
