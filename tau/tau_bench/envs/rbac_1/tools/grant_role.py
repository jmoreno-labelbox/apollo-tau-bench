from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GrantRole(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        user_id: str = None, 
        role_id: str = None, 
        assigned_by: str = None, 
        expires_on: str = None
    ) -> str:
        user_roles = data.get("user_roles", {}).values()

        new_id_num = (
            max([int(ur["user_role_id"][3:]) for ur in user_roles], default=0) + 1
        )
        new_user_role_id = f"UR-{new_id_num:03d}"
        new_assignment = {
            "user_role_id": new_user_role_id,
            "user_id": user_id,
            "role_id": role_id,
            "assigned_by": assigned_by,
            "expires_on": expires_on,
        }
        data["user_roles"][user_role_id] = new_assignment
        data["user_roles"] = user_roles
        payload = new_assignment
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GrantRole",
                "description": "Assigns a role to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "assigned_by": {"type": "string"},
                        "expires_on": {"type": "string", "format": "date-time"},
                    },
                    "required": ["user_id", "role_id", "assigned_by"],
                },
            },
        }
