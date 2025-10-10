# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchUsers(Tool):
    """Tool to search for users by ID, name, or research field."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        name = kwargs.get('name')
        research_field = kwargs.get('research_field')

        users = list(data.get('users', {}).values())

        if user_id:
            for user in users:
                if user.get('user_id') == user_id:
                    return json.dumps([user], indent=2)
            return json.dumps([])

        if not name and not research_field:
            return json.dumps({"error": "Either user_id, name, or research_field is required."})

        results = []
        for user in users:
            match = True
            if name and name.lower() not in user.get('name', '').lower():
                match = False
            if research_field and research_field.lower() not in user.get('research_field', '').lower():
                match = False
            if match:
                results.append(user)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "fetch_users","description": "Searches for users by their name or research field.","parameters": {"type": "object","properties": {"name": {"type": "string", "description": "The name of the user to search for."}, "research_field": {"type": "string", "description": "The research field of the user."}}}}}
