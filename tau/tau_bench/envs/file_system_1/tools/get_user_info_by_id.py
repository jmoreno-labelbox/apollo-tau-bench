# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserInfoByID(Tool):
    """Retrieves a user's profile, including their role and permissions."""
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        for user in data.get('user_preferences', []):
            if user.get('user_id') == user_id:
                return json.dumps(user)
        return json.dumps({"error": f"User with ID '{user_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_info_by_id", "description": "Fetches user details like role and permissions using their unique user ID.", "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The unique ID of the user (e.g., 'user_001')."}}, "required": ["user_id"]}}}
