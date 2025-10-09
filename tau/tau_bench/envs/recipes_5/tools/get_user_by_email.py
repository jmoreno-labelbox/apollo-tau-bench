from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserByEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], email: str = None, user_id: int = None) -> str:
        user = None
        if email:
            user = next(
                (u for u in data.get("users", []) if u.get("email") == email), None
            )
        if user is None and user_id is not None:
            user = next(
                (u for u in data.get("users", []) if u.get("user_id") == user_id), None
            )
        if user is None:
            fid = _first_user_id(data)
            user = next(
                (u for u in data.get("users", []) if u.get("user_id") == fid), None
            )
        if not user:
            return _json_dump({"error": "no users available"})
        return _json_dump(user)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserByEmail",
                "description": "Retrieve a user by email or user_id; defaults to the first user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string"},
                        "user_id": {"type": "integer"},
                    },
                    "required": [],
                },
            },
        }
