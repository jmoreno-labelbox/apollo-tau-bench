from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserDetailsByEmail(Tool):
    """Acquires a user's full details using their email address."""

    @staticmethod
    def invoke(data: dict[str, Any], email: str = None) -> str:
        try:
            users = data.get("users", {}).values()
        except (KeyError, json.JSONDecodeError):
            users = []

        for user in users.values():
            if user.get("email") == email:
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
                "name": "GetUserDetailsByEmail",
                "description": "Retrieves full user details based on their email address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "The email address to search for.",
                        }
                    },
                    "required": ["email"],
                },
            },
        }
