# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserDepartment(Tool):
    """ Updates the 'department' field for a specific user in the database. """

    @staticmethod
    def invoke(data: Dict[str, Any], new_department, user_id) -> str:
        user_id_to_update = user_id

        try:
            users = list(data.get('users', {}).values())
        except (KeyError, json.JSONDecodeError):
            users = []

        user_to_update = None
        for user in users:
            if user.get("user_id") == user_id_to_update:
                user["department"] = new_department
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
                "name": "update_user_department",
                "description": "Updates the department for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose department needs to be updated."
                        },
                        "new_department": {
                            "type": "string",
                            "description": "The new department to assign to the user."
                        }
                    },
                    "required": ["user_id", "new_department"]
                }
            }
        }
