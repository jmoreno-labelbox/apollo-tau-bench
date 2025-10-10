# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        """Retrieve the full profile for a given user ID."""
        users = list(data.get("users", {}).values())
        user_profile = next((u for u in users if u.get("user_id") == user_id), None)

        if user_profile:
            return json.dumps(user_profile, indent=2)
        else:
            return json.dumps({"error": f"User with ID {user_id} not found."}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_user_profile",
                "description": "Retrieve the full profile of a user by their user ID, including their team ID, role, and manager.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID to retrieve the profile for.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
