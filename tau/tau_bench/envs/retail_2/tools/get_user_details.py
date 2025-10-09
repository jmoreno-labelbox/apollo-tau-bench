from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserDetails(Tool):
    """Obtain complete user information from users.json using user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        users = data.get("users", {}).values()
        for user in users.values():
            if user.get("user_id") == user_id:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found", "user_id": user_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserDetails",
                "description": "Get user details from users.json by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
