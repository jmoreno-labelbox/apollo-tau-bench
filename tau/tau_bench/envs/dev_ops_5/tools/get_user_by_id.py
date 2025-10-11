# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserById(Tool):
    """Retrieves a user by their ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], id) -> str:
        user_id = id
        users = list(data.get("users", {}).values())
        for user in users:
            if user.get("id") == user_id:
                return json.dumps(user)
        return json.dumps({"error": f"User with ID '{user_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_by_id",
                "description": "Retrieves a user by their ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
