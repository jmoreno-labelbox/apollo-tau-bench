from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class SearchUsers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], email: str = None, name: str = None, user_id: str = None) -> str:
        if not any([email, name, user_id]):
            payload = {"error": "email, name, or user_id is required"}
            out = json.dumps(payload)
            return out

        users = data["users"]

        if user_id:
            user = next((u for u in users.values() if u["user_id"] == user_id), None)
            if not user:
                payload = {"error": "User not found"}
                out = json.dumps(payload)
                return out
            payload = user
            out = json.dumps(payload, indent=2)
            return out

        matching_users = []
        for user in users.values():
            if email and email.lower() in user["email"].lower():
                matching_data["users"][user_id] = user
            elif name:
                full_name = (
                    f"{user['name']['first_name']} {user['name']['last_name']}".lower()
                )
                if name.lower() in full_name:
                    matching_data["users"][user_id] = user
        payload = matching_users
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchUsers",
                "description": "Search for users by email, name, or user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "Email address to search for",
                        },
                        "name": {
                            "type": "string",
                            "description": "Name to search for (partial match)",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Specific user ID to look up",
                        },
                    },
                },
            },
        }
