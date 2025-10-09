from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserRolesTool(Tool):
    """Get all roles assigned to a specific user (echo user_id for chaining)."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        roles: list[str] = []
        assignments = data.get("user_roles", {}).values()
        for assignment in assignments.values():
            if assignment.get("user_id") == user_id and not assignment.get(
                "expires_on"
            ):
                roles.append(assignment.get("role_id"))
        payload = {"user_id": user_id, "roles": roles}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRoles",
                "description": "Get all active role IDs assigned to a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Unique user identifier (e.g., U-007)",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
