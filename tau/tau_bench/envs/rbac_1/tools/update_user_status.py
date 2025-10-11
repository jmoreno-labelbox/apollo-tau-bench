# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], status, user_id) -> str:
        new_status = status
        for user in list(data.get('users', {}).values()):
            if user.get('user_id') == user_id:
                user['status'] = new_status
                return json.dumps({"user_id": user_id, "status": new_status})
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_user_status",
                        "description": "Updates the status of a user's account (e.g., ACTIVE, DISABLED).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {
                                                "type": "string",
                                                "description": "The ID of the user to update."
                                        },
                                        "status": {
                                                "type": "string",
                                                "description": "The new status for the user account."
                                        }
                                },
                                "required": ["user_id", "status"]
                        }
                }
        }
