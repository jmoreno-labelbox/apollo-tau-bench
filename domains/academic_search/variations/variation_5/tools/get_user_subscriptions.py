from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetUserSubscriptions(Tool):
    """Utility for retrieving a user's topic subscriptions."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None) -> str:
        if not user_id:
            payload = {"error": "user_id is required."}
            out = json.dumps(payload)
            return out

        subscriptions = data.get("subscriptions", [])
        user_subs = [sub for sub in subscriptions if sub.get("user_id") == user_id]
        payload = user_subs
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserSubscriptions",
                "description": "Retrieves the list of topics a specific user is subscribed to.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user whose subscriptions to retrieve.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
