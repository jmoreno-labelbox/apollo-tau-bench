# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindUsersByCriteria(Tool):
    """Tool to find users by various criteria."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        users = list(data.get('users', {}).values())
        results = []
        for user in users:
            match = True
            if kwargs.get('user_id') and kwargs['user_id'] != user.get('user_id'): match = False
            if kwargs.get('name') and kwargs['name'].lower() not in user.get('name', '').lower(): match = False
            if kwargs.get('research_field') and kwargs['research_field'].lower() not in user.get('research_field', '').lower(): match = False
            if kwargs.get('availability') and kwargs['availability'] != user.get('availability'): match = False
            if kwargs.get('institution') and kwargs.get('institution') == user.get('institution'): match = False
            if match:
                results.append(user)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_users_by_criteria", "description": "Finds researchers by ID, name, research field, availability, or to exclude an institution.", "parameters": {"type": "object", "properties": {
            "user_id": {"type": "string", "description": "The unique ID of the user."},
            "name": {"type": "string", "description": "The name of the user."},
            "research_field": {"type": "string", "description": "A research field to filter by."},
            "availability": {"type": "string", "description": "The availability status (e.g., 'available')."},
            "institution": {"type": "string", "description": "Excludes users who belong to this institution."}
        }, "required": []}}}
