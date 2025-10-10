# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserContactInfo(Tool):
    """Retrieves a user's contact details (email, Slack) by their user ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        for contact in data.get('user_contacts', []):
            if contact.get('user_id') == user_id:
                return json.dumps(contact)
        return json.dumps({"error": f"Contact info for user ID '{user_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_contact_info", "description": "Fetches a user's contact details (email, Slack handle) for notifications.", "parameters": {"type": "object", "properties": {"user_id": {"type": "string"}}, "required": ["user_id"]}}}
