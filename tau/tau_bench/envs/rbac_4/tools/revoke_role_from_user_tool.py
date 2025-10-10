# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RevokeRoleFromUserTool(Tool):
    """Revoke a role from a user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        rid = kwargs.get("role_id")
        user_roles = data.get("user_roles", [])
        to_remove = [ur for ur in user_roles if ur["user_id"] == uid and ur["role_id"] == rid]
        if not to_remove:
            return json.dumps({"error": "Role not found for user"}, indent=2)
        for rem in to_remove:
            user_roles.remove(rem)
        return json.dumps({"success": f"Role {rid} revoked from user {uid}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_role",
                "description": "Revokes a specific role from a user",
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
