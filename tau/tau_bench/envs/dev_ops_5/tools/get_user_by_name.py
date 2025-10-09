from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUserByName(Tool):
    """Obtains a user based on their name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        users = data.get("users", [])
        for user in users:
            if user.get("name") == name:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": f"User with name '{name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserByName",
                "description": "Retrieves a user by their name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
