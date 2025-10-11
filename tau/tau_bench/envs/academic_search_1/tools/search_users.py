# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchUsers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name, research_field, user_id) -> str:
        """
        Executes user search.
        - If 'user_id' is provided, returns the details of that specific user.
        - Otherwise, filters users by 'name' and/or 'research_field'.
        - If no parameters are provided, returns all users.
        """

        users = list(data.get('users', {}).values())

        # When a user_id is supplied, it takes precedence and retrieves a specific user.
        if user_id:
            for user in users:
                if user.get('user_id') == user_id:
                    return json.dumps(user, indent=2)
            return json.dumps({"error": f"User with ID '{user_id}' not found."})

        # If user_id is absent, it performs the search using alternative fields and returns a list.
        if not name and not research_field:
            return json.dumps(users, indent=2)

        results = [
            user for user in users
            if (not name or name.lower() in user.get('name', '').lower()) and
               (not research_field or research_field.lower() in user.get('research_field', '').lower())
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """
        Returns the function schema to be used by the language model.
        """
        return {
            "type": "function",
            "function": {
                "name": "search_users",
                "description": "Searches for users by ID, name, or research field. If a user_id is provided, returns the details of that user. Otherwise, returns a list of users that match the other criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user to retrieve details for."},
                        "name": {"type": "string", "description": "The name of the user to search for."},
                        "research_field": {"type": "string", "description": "The research field of the user."}
                    }
                }
            }
        }
