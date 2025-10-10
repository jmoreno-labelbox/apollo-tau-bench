# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserByName(Tool):
    """Retrieves a user by their name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        users = list(data.get("users", {}).values())
        for user in users:
            if user.get("name") == name:
                return json.dumps(user)
        return json.dumps({"error": f"User with name '{name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_by_name",
                "description": "Retrieves a user by their name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
