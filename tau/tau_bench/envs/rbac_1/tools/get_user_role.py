# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], role_name, user_id) -> str:
        role_id = None
        for role in list(data.get('roles', {}).values()):
            if role.get('role_name') == role_name:
                role_id = role.get('role_id')
                break
        if not role_id:
            return json.dumps({"error": "Role not found"})

        for ur in data.get('user_roles', []):
            if ur.get('user_id') == user_id and ur.get('role_id') == role_id:
                return json.dumps(ur)
        return json.dumps({"error": "User role assignment not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_user_role",
                        "description": "Retrieves a specific role assignment for a user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "role_name": {"type": "string"}
                                },
                                "required": ["user_id", "role_name"]
                        }
                }
        }
