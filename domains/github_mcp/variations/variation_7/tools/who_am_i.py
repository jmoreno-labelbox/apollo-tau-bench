from tau_bench.envs.tool import Tool
import json
from typing import Any

class WhoAmI(Tool):
    """Retrieve the active user based on authentication."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        auth = data.get("authentication") or [{}]
        user = auth[0]
        payload = {"username": user.get("username"), "email": user.get("email")}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "whoAmI",
                "description": "Return the authenticated username and email.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
