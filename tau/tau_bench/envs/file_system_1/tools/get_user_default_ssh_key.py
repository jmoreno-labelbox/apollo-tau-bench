# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserDefaultSshKey(Tool):
    """Finds a user's default SSH key ID from their preferences."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        for user in data.get('user_preferences', []):
            if user.get('user_id') == user_id and 'default_ssh_key' in user:
                return json.dumps({"user_id": user_id, "default_ssh_key": user['default_ssh_key']})
        return json.dumps({"error": f"Default SSH key for user ID '{user_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_default_ssh_key", "description": "Looks up the default SSH key associated with a user's profile.", "parameters": {"type": "object", "properties": {"user_id": {"type": "string"}}, "required": ["user_id"]}}}
