# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddUser(Tool):
    """Adds a new user."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email = kwargs.get("email")
        full_name = kwargs.get("full_name")
        users = list(data.get("users", {}).values())
        if any(user.get("email") == email for user in users):
            return json.dumps({"error": f"User with email '{email}' already exists."})
        new_id = max([u.get("user_id", 0) for u in users]) + 1 if users else 101
        new_user = {
            "user_id": new_id, "email": email, "full_name": full_name,
            "created_at": "2025-08-22T10:00:00Z"
        }
        data["users"].append(new_user)
        return json.dumps(new_user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_user",
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
