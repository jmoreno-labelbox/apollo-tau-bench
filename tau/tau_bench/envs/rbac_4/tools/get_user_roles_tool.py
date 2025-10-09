from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserRolesTool(Tool):
    """Get all roles allocated to a particular user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        uid = user_id
        roles_map = [
            ur["role_id"] for ur in data.get("user_roles", []) if ur["user_id"] == uid
        ]
        roles = [r for r in data.get("roles", []) if r["role_id"] in roles_map]
        payload = roles
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRoles",
                "description": "Retrieve all role objects assigned to a given user_id",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
