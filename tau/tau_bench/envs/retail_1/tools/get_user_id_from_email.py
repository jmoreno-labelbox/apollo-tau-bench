from tau_bench.envs.tool import Tool
import json
from typing import Any
from tau_bench.envs.retail_1.tools import _match




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserIdFromEmail(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], email: str) -> str:
        pass
        db = _convert_db_to_list(data.get("users", {}))
        filter_params = {"email": email}

        user = [row for row in db if _match(row, filter_params)]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        return (
            json.dumps(user[0]["user_id"])
            if user
            else json.dumps({"error": "User not found"})
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserIdFromEmail",
                "description": "Retrieve user information by email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "The user's email address.",
                        },
                    },
                    "required": ["email"],
                },
            },
        }
