# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class search_users(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], filters: dict) -> str:
        users = list(data.get("users", {}).values())
        if "user_id" in filters:
            user = next(
                (u for u in users if u.get("user_id") == filters["user_id"]), None
            )
            return (
                json.dumps(user, indent=2)
                if user
                else json.dumps({"error": "User not found"}, indent=2)
            )
        return json.dumps({"users": users}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "search_users",
                "description": "Search for users by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }
