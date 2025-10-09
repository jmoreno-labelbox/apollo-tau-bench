from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateUserDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, new_username: str = None, new_email: str = None) -> str:
        for user in data.get("users", []):
            if user.get("user_id") == user_id:
                if new_username:
                    user["username"] = new_username
                if new_email:
                    user["email"] = new_email
                payload = user
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
                "name": "UpdateUserDetails",
                "description": "Updates a user's username and/or email address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "new_username": {"type": "string"},
                        "new_email": {"type": "string"},
                    },
                    "required": ["user_id"],
                },
            },
        }
