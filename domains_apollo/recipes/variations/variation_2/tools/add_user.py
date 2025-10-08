from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class AddUser(Tool):
    """Incorporates a new user."""

    @staticmethod
    def invoke(data: dict[str, Any], email: str = None, full_name: str = None) -> str:
        users = data.get("users", [])
        if any(user.get("email") == email for user in users):
            payload = {"error": f"User with email '{email}' already exists."}
            out = json.dumps(payload)
            return out
        new_id = max([u.get("user_id", 0) for u in users]) + 1 if users else 101
        new_user = {
            "user_id": new_id,
            "email": email,
            "full_name": full_name,
            "created_at": "2025-08-22T10:00:00Z",
        }
        data["users"].append(new_user)
        payload = new_user
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addUser",
                "description": "Adds a new user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string"},
                        "full_name": {"type": "string"},
                    },
                    "required": ["email", "full_name"],
                },
            },
        }
