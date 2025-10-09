from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserRolesByUserId(Tool):
    """Fetches all role assignments associated with a specific user ID."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        try:
            user_roles = data.get("user_roles", [])
        except:
            user_roles = []

        assigned_roles = [role for role in user_roles if role.get("user_id") == user_id]
        payload = assigned_roles
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRolesByUserId",
                "description": "Lists all roles currently assigned to a specific user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose roles are to be listed.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
