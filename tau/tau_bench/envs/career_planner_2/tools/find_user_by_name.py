from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class FindUserByName(Tool):
    """Locate a user's ID using their full name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        for u in data.get("users", {}).values():
            if u.get("name").lower() == name.lower():
                payload = {"user_id": u.get("user_id")}
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
                "name": "FindUserByName",
                "description": "Find a user's ID by their full name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
