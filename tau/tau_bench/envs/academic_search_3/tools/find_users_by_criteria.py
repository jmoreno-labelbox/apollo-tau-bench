# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindUsersByCriteria(Tool):
    """Tool to find users by various criteria."""
    @staticmethod
    def invoke(data: Dict[str, Any], availability, institution, name, research_field, user_id) -> str:
        users = list(data.get('users', {}).values())
        results = []
        for user in users:
            match = True
            if user_id and user_id != user.get('user_id'): match = False
            if name and name.lower() not in user.get('name', '').lower(): match = False
            if research_field and research_field.lower() not in user.get('research_field', '').lower(): match = False
            if availability and availability != user.get('availability'): match = False
            if institution and institution == user.get('institution'): match = False
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
