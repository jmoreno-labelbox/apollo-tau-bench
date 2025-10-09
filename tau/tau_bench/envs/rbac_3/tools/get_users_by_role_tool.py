from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUsersByRoleTool(Tool):
    """get_users_by_role: enumerate user_ids with an assigned role (active only)."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        result = [
            ur.get("user_id")
            for ur in data.get("user_roles", [])
            if ur.get("role_id") == role_id and not ur.get("expires_on")
        ]
        payload = {"role_id": role_id, "user_ids": sorted(result)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUsersByRole",
                "description": (
                    "List users with an active assignment of the given role."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }
