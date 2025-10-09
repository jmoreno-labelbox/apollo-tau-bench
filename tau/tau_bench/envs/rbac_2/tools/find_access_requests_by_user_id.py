from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class FindAccessRequestsByUserId(Tool):
    """Identifies all access requests made by a specific user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        user_id_to_find = user_id
        try:
            all_requests = data.get("access_requests", [])
        except (KeyError, json.JSONDecodeError):
            all_requests = []

        user_requests = [
            request
            for request in all_requests
            if request.get("user_id") == user_id_to_find
        ]
        payload = user_requests
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAccessRequestsByUserId",
                "description": "Retrieves a list of all historical access requests submitted by a specific user, which can then be reviewed for patterns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose access requests are to be retrieved.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
