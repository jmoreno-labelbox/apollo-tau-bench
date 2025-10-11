# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindResearcherProfiles(Tool):
    """Searches for users by their name, research field, or user_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], name, research_field, user_id) -> str:
        name, research_field, user_id = name, research_field, user_id
        if not any([name, research_field, user_id]):
            return json.dumps(list(data.get('users', {}).values()), indent=2)

        users = list(data.get('users', {}).values())
        results = [
            user for user in users if
            (not name or name.lower() in user.get('name', '').lower()) and
            (not research_field or research_field.lower() in user.get('research_field', '').lower()) and
            (not user_id or user.get('user_id') == user_id)
        ]
        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_researcher_profiles", "description": "Searches for users by their name, research field, or user_id.", "parameters": {"type": "object", "properties": {"name": {"type": "string"}, "research_field": {"type": "string"}, "user_id": {"type": "string"}}}}}
