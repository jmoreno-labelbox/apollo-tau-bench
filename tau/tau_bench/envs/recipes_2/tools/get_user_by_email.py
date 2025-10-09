from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserByEmail(Tool):
    """Fetches a user's information using their email address."""

    @staticmethod
    def invoke(data: dict[str, Any], email: str = None) -> str:
        users = data.get("users", {}).values()
        for user in users.values():
            if user.get("email") == email:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": f"User with email '{email}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUserByEmail",
                "description": "Retrieves a user's details by their email address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "The email address of the user to find.",
                        }
                    },
                    "required": ["email"],
                },
            },
        }
