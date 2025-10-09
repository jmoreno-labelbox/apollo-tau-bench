from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateUserStatus(Tool):
    """Modifying the 'status' field for a particular user in the database."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, new_status: str = None,
    updated_by: Any = None,
    ) -> str:
        user_id_to_update = user_id
        new_status = new_status

        try:
            users = data.get("users", [])
        except:
            users = []

        user_to_update = None
        for user in users:
            if user.get("user_id") == user_id_to_update:
                user["status"] = new_status
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
                "name": "UpdateUserStatus",
                "description": "Updates the status of a user account (e.g., to ACTIVE, DISABLED, SUSPENDED).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose status needs to be updated.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the user. Must be one of: ACTIVE, INACTIVE, SUSPENDED, DISABLED.",
                        },
                    },
                    "required": ["user_id", "new_status"],
                },
            },
        }
