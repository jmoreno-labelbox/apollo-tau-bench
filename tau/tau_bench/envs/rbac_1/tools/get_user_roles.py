# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserRoles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        assigned_role_ids = [
                ur['role_id'] for ur in data.get('user_roles', [])
                if ur.get('user_id') == user_id
        ]
        role_names = [
                role['role_name'] for role in list(data.get('roles', {}).values())
                if role['role_id'] in assigned_role_ids
        ]
        return json.dumps({"user_id": user_id, "roles": role_names})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_user_roles",
                        "description": "Retrieves all roles assigned to a specific user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"}
                                },
                                "required": ["user_id"]
                        }
                }
        }
