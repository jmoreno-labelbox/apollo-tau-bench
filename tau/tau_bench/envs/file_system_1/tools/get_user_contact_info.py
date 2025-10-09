from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUserContactInfo(Tool):
    """Fetches a user's contact information (email, Slack) using their user ID."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        for contact in data.get("user_contacts", []):
            if contact.get("user_id") == user_id:
                payload = contact
                out = json.dumps(payload)
                return out
        payload = {"error": f"Contact info for user ID '{user_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserContactInfo",
                "description": "Fetches a user's contact details (email, Slack handle) for notifications.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
