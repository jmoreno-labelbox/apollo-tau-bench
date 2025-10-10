# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveRoleFromUserTool(Tool):
    """Remove a specific role assignment from a user (write operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], role_id, user_id) -> str:
        user_roles = data.get("user_roles", [])
        if not isinstance(user_roles, list):
            return json.dumps({"error": "user_roles must be a list"}, indent=2)

        for fld, val in [("user_id", user_id), ("role_id", role_id)]:
            if not isinstance(val, str) or not val.strip():
                return json.dumps({"error": f"{fld} must be a non-empty string"}, indent=2)

        before = len(user_roles)
        data["user_roles"] = [ur for ur in user_roles if not (ur.get("user_id") == user_id and ur.get("role_id") == role_id)]
        removed = before - len(data["user_roles"])

        if removed == 0:
            return json.dumps({"error": f"No assignment of {role_id} found for {user_id}"}, indent=2)
        return json.dumps({"success": f"Removed {removed} assignment(s) of {role_id} from {user_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_role_from_user",
                "description": "Remove a role assignment for a user. Deletes matching rows from user_roles.",
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
