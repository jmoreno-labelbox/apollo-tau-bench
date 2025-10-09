from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AssignRoleToUser(Tool):
    """Assigning a role directly to a user."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        role_id: str = None,
        assigned_by: str = None,
        expires_on: str = None
,
    assigned_on: Any = None,
    ) -> str:
        try:
            user_roles = data.get("user_roles", [])
        except (KeyError, json.JSONDecodeError):
            user_roles = []
        existing_ids = [
            int(ur["user_role_id"].replace("UR-", ""))
            for ur in user_roles
            if ur.get("user_role_id", "").startswith("UR-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        user_role_id = f"UR-{next_id_num:03d}"

        new_assignment = {
            "user_role_id": user_role_id,
            "user_id": user_id,
            "role_id": role_id,
            "assigned_by": assigned_by,
            "expires_on": expires_on,
        }

        user_roles.append(new_assignment)
        data["user_roles.json"] = json.dumps(user_roles, indent=4)
        payload = new_assignment
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignRoleToUser",
                "description": "Directly assigns a specific role to a user. This is a privileged action for processes like onboarding.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user to whom the role will be assigned.",
                        },
                        "role_id": {
                            "type": "string",
                            "description": "The unique ID of the role to be assigned.",
                        },
                        "assigned_by": {
                            "type": "string",
                            "description": "The user ID of the administrator or manager performing the assignment.",
                        },
                        "expires_on": {
                            "type": "string",
                            "description": "Optional: The timestamp when the role assignment expires. Use null for permanent roles.",
                        },
                    },
                    "required": ["user_id", "role_id", "assigned_by"],
                },
            },
        }
