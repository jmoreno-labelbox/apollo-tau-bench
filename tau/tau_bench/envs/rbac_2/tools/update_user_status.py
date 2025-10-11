# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserStatus(Tool):
    """ Updating the 'status' field of a specific user in the database. """

    @staticmethod
    def invoke(data: Dict[str, Any], new_status, user_id) -> str:
        user_id_to_update = user_id

        try:
            users = list(data.get('users', {}).values())
        except:
            users = []

        user_to_update = None
        for user in users:
            if user.get("user_id") == user_id_to_update:
                user["status"] = new_status
                user_to_update = user
                break

        if not user_to_update:
            return json.dumps({"error": f"User with ID '{user_id_to_update}' not found."})

        data['users'] = users
        return json.dumps(user_to_update)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_status",
                "description": "Updates the status of a user account (e.g., to ACTIVE, DISABLED, SUSPENDED).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose status needs to be updated."
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the user. Must be one of: ACTIVE, INACTIVE, SUSPENDED, DISABLED."
                        }
                    },
                    "required": ["user_id", "new_status"]
                }
            }
        }
