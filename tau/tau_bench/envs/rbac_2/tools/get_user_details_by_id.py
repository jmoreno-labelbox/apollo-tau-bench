from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserDetailsById(Tool):
    """Fetches complete details of a user by their unique user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, actor_id: Any = None) -> str:
        try:
            users = data.get("users", {}).values()
        except (KeyError, json.JSONDecodeError):
            users = []

        for user in users.values():
            if user.get("user_id") == user_id:
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
                "name": "GetUserDetailsById",
                "description": "Retrieves full user details based on their unique user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user (e.g., U-001).",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
