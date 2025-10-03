from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class SearchUsersByName(Tool):
    """Looks for users whose full names include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        if not name_query:
            payload = {"error": "name_query parameter is required."}
            out = json.dumps(payload)
            return out

        users = data.get("users", [])

        matching_users = [
            user
            for user in users
            if name_query.lower() in user.get("full_name", "").lower()
        ]
        payload = matching_users
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchUsersByName",
                "description": "Searches for users with full names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in user full names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }
