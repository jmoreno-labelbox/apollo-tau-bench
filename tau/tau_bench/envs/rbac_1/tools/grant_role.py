# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GrantRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], assigned_by, expires_on, role_id, user_id) -> str:
        user_roles = data.get('user_roles', [])

        new_id_num = max([int(ur["user_role_id"][3:]) for ur in user_roles], default=0) + 1
        new_user_role_id = f"UR-{new_id_num:03d}"
        new_assignment = {
                "user_role_id": new_user_role_id,
                "user_id": user_id,
                "role_id": role_id,
                "assigned_by": assigned_by,
                "expires_on": expires_on
        }
        user_roles.append(new_assignment)
        data['user_roles'] = user_roles
        return json.dumps(new_assignment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "grant_role",
                        "description": "Assigns a role to a user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "role_id": {"type": "string"},
                                        "assigned_by": {"type": "string"},
                                        "expires_on": {"type": "string", "format": "date-time"}
                                },
                                "required": ["user_id", "role_id", "assigned_by"]
                        }
                }
        }
