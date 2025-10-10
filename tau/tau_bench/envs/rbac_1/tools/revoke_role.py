# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RevokeRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        role_id = kwargs.get("role_id")
        data['user_roles'] = [
                ur for ur in data.get('user_roles', [])
                if not (ur.get('user_id') == user_id and ur.get('role_id') == role_id)
        ]
        return json.dumps({"user_id": user_id, "role_id": role_id, "status": "revoked"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "revoke_role",
                        "description": "Removes a role from a user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "role_id": {"type": "string"}
                                },
                                "required": ["user_id", "role_id"]
                        }
                }
        }
