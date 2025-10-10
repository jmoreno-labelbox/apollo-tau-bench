# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserRolesTool(Tool):
    """Retrieve all roles assigned to a specific user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        roles_map = [ur["role_id"] for ur in data.get("user_roles", []) if ur["user_id"] == uid]
        roles = [r for r in list(data.get("roles", {}).values()) if r["role_id"] in roles_map]
        return json.dumps(roles, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_roles",
                "description": "Retrieve all role objects assigned to a given user_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"}
                    },
                    "required": ["user_id"]
                }
            }
        }
