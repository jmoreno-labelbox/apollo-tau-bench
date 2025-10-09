from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateUserDepartment(Tool):
    """Modifies the 'department' field for a specific user in the database."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, new_department: str = None) -> str:
        user_id_to_update = user_id
        new_department = new_department

        try:
            users = data.get("users", [])
        except (KeyError, json.JSONDecodeError):
            users = []

        user_to_update = None
        for user in users:
            if user.get("user_id") == user_id_to_update:
                user["department"] = new_department
                user_to_update = user
                break

        if not user_to_update:
            payload = {"error": f"User with ID '{user_id_to_update}' not found."}
            out = json.dumps(payload)
            return out

        data["users"] = users
        payload = user_to_update
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserDepartment",
                "description": "Updates the department for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose department needs to be updated.",
                        },
                        "new_department": {
                            "type": "string",
                            "description": "The new department to assign to the user.",
                        },
                    },
                    "required": ["user_id", "new_department"],
                },
            },
        }
