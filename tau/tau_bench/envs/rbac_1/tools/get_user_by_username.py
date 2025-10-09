from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserByUsername(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], username: str = None, actor_id: Any = None) -> str:
        for user in data.get("users", {}).values():
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
                "name": "GetUserByUsername",
                "description": "Retrieves user details based on their username.",
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
