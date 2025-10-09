from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserDefaultSshKey(Tool):
    """Identifies a user's default SSH key ID based on their preferences."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        for user in data.get("user_preferences", {}).values():
            if user.get("user_id") == user_id and "default_ssh_key" in user:
                payload = {"user_id": user_id, "default_ssh_key": user["default_ssh_key"]}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Default SSH key for user ID '{user_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserDefaultSshKey",
                "description": "Looks up the default SSH key associated with a user's profile.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
