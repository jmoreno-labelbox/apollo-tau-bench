from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUserByEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], email: str) -> str:
        users = _get_table(data, "users")
        user = next((u for u in users if u.get("email") == email), None)
        payload = {"user": user}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUserByEmail",
                "description": "Returns the user row with the specified email.",
                "parameters": {
                    "type": "object",
                    "properties": {"email": {"type": "string"}},
                    "required": ["email"],
                },
            },
        }
