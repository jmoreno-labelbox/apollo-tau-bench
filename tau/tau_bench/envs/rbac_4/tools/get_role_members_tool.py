# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRoleMembersTool(Tool):
    """Return user records for members of a given role (read operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        users = list(data.get("users", {}).values())
        user_roles = data.get("user_roles", [])

        role_id = kwargs.get("role_id")
        status_filter = kwargs.get("status")  # optional: e.g., "ACTIVE"

        if not isinstance(user_roles, list) or not isinstance(users, list):
            return json.dumps({"error": "users and user_roles must be lists"}, indent=2)
        if not isinstance(role_id, str) or not role_id.strip():
            return json.dumps({"error": "role_id must be a non-empty string"}, indent=2)

        member_user_ids = {ur["user_id"] for ur in user_roles if ur.get("role_id") == role_id}
        results = []
        for u in users:
            if u.get("user_id") in member_user_ids:
                if status_filter and u.get("status") != status_filter:
                    continue
                results.append(u)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_members",
                "description": "List user records for members assigned to a role. Optional filter by user status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string", "description": "The role_id to lookup"},
                        "status": {"type": "string", "description": "Optional user status filter, e.g. ACTIVE"}
                    },
                    "required": ["role_id"]
                },
            },
        }
