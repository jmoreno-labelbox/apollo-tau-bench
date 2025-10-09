from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserDetailsByUsername(Tool):
    """Obtains a user's complete details via their username."""

    @staticmethod
    def invoke(data: dict[str, Any], username: str = None) -> str:
        try:
            users = data.get("users", [])
        except (KeyError, json.JSONDecodeError):
            users = []

        for user in users:
            if user.get("username") == username:
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
                "name": "GetUserDetailsByUsername",
                "description": "Retrieves full user details based on their username.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The username to search for.",
                        }
                    },
                    "required": ["username"],
                },
            },
        }
