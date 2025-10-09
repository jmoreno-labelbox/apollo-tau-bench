from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUserById(Tool):
    """Retrieve a user row using user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        if user_id is None:
            return _json_dump({"error": "user_id is required"})
        row = _require(data, "users", "user_id", user_id)
        return _json_dump(row or {"error": f"user_id {user_id} not found"})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserById",
                "description": "Return user by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "integer"}},
                    "required": ["user_id"],
                },
            },
        }
