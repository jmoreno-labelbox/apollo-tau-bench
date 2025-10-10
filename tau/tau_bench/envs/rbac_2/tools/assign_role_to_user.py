# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignRoleToUser(Tool):
    """ Directly assigning a role to an user. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        try:
            user_roles = data.get('user_roles', [])
        except (KeyError, json.JSONDecodeError):
            user_roles = []
        existing_ids = [int(ur["user_role_id"].replace("UR-", "")) for ur in user_roles if ur.get("user_role_id", "").startswith("UR-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        user_role_id = f"UR-{next_id_num:03d}"

        new_assignment = {
            "user_role_id": user_role_id,
            "user_id": kwargs.get("user_id"),
            "role_id": kwargs.get("role_id"),
            "assigned_by": kwargs.get("assigned_by"),
            "expires_on": kwargs.get("expires_on", None) # Optional: for temporary roles
        }

        user_roles.append(new_assignment)
        data["user_roles.json"] = json.dumps(user_roles, indent=4)

        return json.dumps(new_assignment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_role_to_user",
                "description": "Directly assigns a specific role to a user. This is a privileged action for processes like onboarding.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user to whom the role will be assigned."
                        },
                        "role_id": {
                            "type": "string",
                            "description": "The unique ID of the role to be assigned."
                        },
                        "assigned_by": {
                            "type": "string",
                            "description": "The user ID of the administrator or manager performing the assignment."
                        },
                        "expires_on": {
                            "type": "string",
                            "description": "Optional: The timestamp when the role assignment expires. Use null for permanent roles."
                        }
                    },
                    "required": ["user_id", "role_id", "assigned_by"]
                }
            }
        }
