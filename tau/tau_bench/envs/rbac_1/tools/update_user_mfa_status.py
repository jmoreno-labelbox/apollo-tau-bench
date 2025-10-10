# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserMfaStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        mfa_enabled = kwargs.get("mfa_enabled")
        for user in list(data.get('users', {}).values()):
            if user.get('user_id') == user_id:
                user['mfa_enabled'] = mfa_enabled
                return json.dumps(user)
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_user_mfa_status",
                        "description": "Enables or disables multi-factor authentication for a user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "mfa_enabled": {"type": "boolean"}
                                },
                                "required": ["user_id", "mfa_enabled"]
                        }
                }
        }
