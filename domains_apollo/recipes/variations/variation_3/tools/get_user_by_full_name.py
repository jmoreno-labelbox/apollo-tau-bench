from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUserByFullName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], full_name: str) -> str:
        users = _get_table(data, "users")
        user = next((u for u in users if u.get("full_name") == full_name), None)
        payload = {"user": user}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserByFullName",
                "description": "Returns the user row with the specified full_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"full_name": {"type": "string"}},
                    "required": ["full_name"],
                },
            },
        }
