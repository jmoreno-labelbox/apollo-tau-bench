from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        for user in data.get("users", {}).values():
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
                "name": "GetUserById",
                "description": "Retrieves user details based on user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID to search for.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
