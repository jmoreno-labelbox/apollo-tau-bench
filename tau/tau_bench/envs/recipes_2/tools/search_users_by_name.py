# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchUsersByName(Tool):
    """Searches for users with full names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_query = kwargs.get("name_query")
        if not name_query:
            return json.dumps({"error": "name_query parameter is required."})

        users = list(data.get("users", {}).values())
        
        matching_users = [
            user for user in users 
            if name_query.lower() in user.get("full_name", "").lower()
        ]
        
        return json.dumps(matching_users)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_users_by_name",
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
