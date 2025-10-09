from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], first_name: str = "", last_name: str = "") -> str:
        first_name = first_name.lower()
        last_name = last_name.lower()
        username_to_find = f"{first_name[0]}{last_name}" if first_name else last_name
        for user in data.get("users", []):
            if user.get("username") == username_to_find:
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
                "name": "GetUserByName",
                "description": "Retrieves user details based on their first and last name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "The first name of the user.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The last name of the user.",
                        },
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }
