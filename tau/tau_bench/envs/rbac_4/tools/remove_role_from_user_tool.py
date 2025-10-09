from tau_bench.envs.tool import Tool
import json
from typing import Any

class RemoveRoleFromUserTool(Tool):
    """Eliminate a specific role assignment from a user (write operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None) -> str:
        user_roles = data.get("user_roles", [])
        if not isinstance(user_roles, list):
            payload = {"error": "user_roles must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        for fld, val in [("user_id", user_id), ("role_id", role_id)]:
            if not isinstance(val, str) or not val.strip():
                payload = {"error": f"{fld} must be a non-empty string"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        before = len(user_roles)
        data["user_roles"] = [
            ur
            for ur in user_roles
            if not (ur.get("user_id") == user_id and ur.get("role_id") == role_id)
        ]
        removed = before - len(data["user_roles"])

        if removed == 0:
            payload = {"error": f"No assignment of {role_id} found for {user_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"success": f"Removed {removed} assignment(s) of {role_id} from {user_id}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveRoleFromUser",
                "description": "Remove a role assignment for a user. Deletes matching rows from user_roles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                    },
                    "required": ["user_id", "role_id"],
                },
            },
        }
