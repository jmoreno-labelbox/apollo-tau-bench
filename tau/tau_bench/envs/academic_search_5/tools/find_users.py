# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindUsers(Tool):
    """
    Tool to search for users by name or research field, OR to get a single user's details by their ID.
    This tool replaces GetUserDetails.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        name = kwargs.get('name')
        research_field = kwargs.get('research_field')

        users = list(data.get('users', {}).values())

        if user_id:
            for user in users:
                if user.get('user_id') == user_id:
                    return json.dumps(user, indent=2)
            return json.dumps({"error": f"User with ID '{user_id}' not found."})

        if not name and not research_field:
            return json.dumps({"error": "For a general search, 'name' or 'research_field' is required."})

        results = [
            user for user in users
            if (not name or name.lower() in user.get('name', '').lower())
            and (not research_field or research_field.lower() in user.get('research_field', '').lower())
        ]

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_users",
                "description": "Searches for users by name or research field, or retrieves a single user by their specific ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The specific ID of the user to retrieve."},
                        "name": {"type": "string", "description": "The name of the user to search for."},
                        "research_field": {"type": "string", "description": "The research field of the user."}
                    }
                }
            }
        }
