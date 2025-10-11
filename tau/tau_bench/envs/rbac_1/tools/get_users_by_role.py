# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUsersByRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], role_id, role_name) -> str:

        if not role_id and not role_name:
            return json.dumps({"error": "Either role_id or role_name must be provided"})

        if role_name and not role_id:
            for role in list(data.get('roles', {}).values()):
                if role.get('role_name') == role_name:
                    role_id = role.get('role_id')
                    break
            if not role_id:
                return json.dumps({"error": f"Role '{role_name}' not found"})

        user_ids = [
                ur['user_id'] for ur in data.get('user_roles', [])
                if ur.get('role_id') == role_id
        ]
        return json.dumps({"users": user_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_users_by_role",
                        "description": "Retrieves all users assigned a specific role, searching by either role_id or role_name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_id": {
                                                "type": "string",
                                                "description": "The ID of the role to search for."
                                        },
                                        "role_name": {
                                                "type": "string",
                                                "description": "The name of the role to search for (e.g., 'operations-lead')."
                                        }
                                }
                        }
                }
        }
