# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUsersByRoleTool(Tool):
    """get_users_by_role: list user_ids having a role assigned (active only)."""

    @staticmethod
    def invoke(data: Dict[str, Any], role_id) -> str:
        result = [
            ur.get("user_id")
            for ur in data.get("user_roles", [])
            if ur.get("role_id") == role_id and not ur.get("expires_on")
        ]
        return json.dumps({"role_id": role_id, "user_ids": sorted(result)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_users_by_role",
                "description": (
                    "List users with an active assignment of the given role."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }
