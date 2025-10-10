# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        users = list(data.get("users", {}).values())

        for user in users:
            if user.get("user_id") == user_id:
                profile_data = {
                    "user_id": user.get("user_id"),
                    "name": user.get("name"),
                    "current_role": user.get("current_role"),
                    "department": user.get("department"),
                    "team_id": user.get("team_id"),
                }
                return json.dumps(profile_data, indent=2)

        return json.dumps({"error": f"User profile not found for {user_id}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_profile",
                "description": "Retrieves key profile information for a user, such as their current role and department.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
