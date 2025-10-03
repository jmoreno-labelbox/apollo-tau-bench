from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetRoleMembersTool(Tool):
    """Provide user records for individuals in a specified role (read operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str, status: str = None) -> str:
        users = data.get("users", [])
        user_roles = data.get("user_roles", [])

        if not isinstance(user_roles, list) or not isinstance(users, list):
            payload = {"error": "users and user_roles must be lists"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(role_id, str) or not role_id.strip():
            payload = {"error": "role_id must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out

        member_user_ids = {
            ur["user_id"] for ur in user_roles if ur.get("role_id") == role_id
        }
        results = []
        for u in users:
            if u.get("user_id") in member_user_ids:
                if status and u.get("status") != status:
                    continue
                results.append(u)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoleMembers",
                "description": "List user records for members assigned to a role. Optional filter by user status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The role_id to lookup",
                        },
                        "status": {
                            "type": "string",
                            "description": "Optional user status filter, e.g. ACTIVE",
                        },
                    },
                    "required": ["role_id"],
                },
            },
        }
