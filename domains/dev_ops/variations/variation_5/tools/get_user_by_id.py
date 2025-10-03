from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUserById(Tool):
    """Fetches a user using their ID."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        user_id: str = None
    ) -> str:
        users = data.get("users", [])
        for user in users:
            if user.get("id") == user_id:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": f"User with ID '{user_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserById",
                "description": "Retrieves a user by their ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
