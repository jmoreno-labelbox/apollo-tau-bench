from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserInfoByID(Tool):
    """Fetches a user's profile, encompassing their role and permissions."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        for user in data.get("user_preferences", {}).values():
            if user.get("user_id") == user_id:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": f"User with ID '{user_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserInfoById",
                "description": "Fetches user details like role and permissions using their unique user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user (e.g., 'user_001').",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
