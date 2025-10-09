from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_name: str = None) -> str:
        users = data.get("users", [])

        for user in users:
            if user.get("name") == user_name:
                payload = {"user_id": user.get("user_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetUserId",
                "description": "Search for user by name",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_name": {
                            "type": "string",
                            "description": "The full name of the user.",
                        }
                    },
                    "required": ["user_name"],
                },
            },
        }
