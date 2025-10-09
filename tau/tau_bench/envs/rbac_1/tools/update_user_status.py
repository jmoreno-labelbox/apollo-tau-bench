from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateUserStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, status: str = None,
    updated_by: Any = None,
    ) -> str:
        for user in data.get("users", {}).values():
            if user.get("user_id") == user_id:
                user["status"] = status
                payload = {"user_id": user_id, "status": status}
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserStatus",
                "description": "Updates the status of a user's account (e.g., ACTIVE, DISABLED).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status for the user account.",
                        },
                    },
                    "required": ["user_id", "status"],
                },
            },
        }
