# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignRoleToUserTool(Tool):
    """Assign a role to a user (write operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_roles = data.get("user_roles", [])
        users = list(data.get("users", {}).values())
        roles = list(data.get("roles", {}).values())
        if not isinstance(user_roles, list):
            return json.dumps({"error": "user_roles must be a list"}, indent=2)
        if not isinstance(users, list):
            return json.dumps({"error": "users must be a list"}, indent=2)
        if not isinstance(roles, list):
            return json.dumps({"error": "roles must be a list"}, indent=2)

        user_id = kwargs.get("user_id")
        role_id = kwargs.get("role_id")
        assigned_by = kwargs.get("assigned_by")
        assigned_on = kwargs.get("assigned_on")

        # Basic validation
        for fld, val in [("user_id", user_id), ("role_id", role_id), ("assigned_by", assigned_by), ("assigned_on", assigned_on)]:
            if not isinstance(val, str) or not val.strip():
                return json.dumps({"error": f"{fld} must be a non-empty string"}, indent=2)

        if not any(u.get("user_id") == user_id for u in users):
            return json.dumps({"error": f"user_id {user_id} not found"}, indent=2)
        if not any(r.get("role_id") == role_id for r in roles):
            return json.dumps({"error": f"role_id {role_id} not found"}, indent=2)

        # Prevent duplicate active assignment (no expires_on or expires_on in the future)
        existing = [ur for ur in user_roles if ur.get("user_id") == user_id and ur.get("role_id") == role_id]
        if existing:
            # If any existing record is still active (no expires or expires later), block
            from datetime import datetime, timezone
            for ur in existing:
                exp = ur.get("expires_on")
                if exp is None:
                    return json.dumps({"error": "Role already assigned"}, indent=2)
                try:
                    exp_dt = datetime.fromisoformat(exp.replace("Z", "+00:00"))
                except Exception:
                    # Unknown date format; be conservative and block
                    return json.dumps({"error": "Role already assigned"}, indent=2)
                now_tz = exp_dt.tzinfo or timezone.utc
                if exp_dt > datetime.now(tz=now_tz):
                    return json.dumps({"error": "Role already assigned"}, indent=2)

        new_id = f"UR-{len(user_roles) + 1:03d}"
        record = {
            "user_role_id": new_id,
            "user_id": user_id,
            "role_id": role_id,
            "assigned_by": assigned_by,
            "assigned_on": assigned_on,
            "expires_on": kwargs.get("expires_on")  # optional
        }
        user_roles.append(record)
        return json.dumps({"success": f"Role {role_id} assigned to {user_id}", "user_role_id": new_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_role_to_user",
                "description": "Assign a role to a user with deterministic fields; blocks if an active assignment exists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "assigned_by": {"type": "string"},
                        "assigned_on": {"type": "string"},
                        "expires_on": {"type": "string", "description": "Optional ISO8601 end timestamp"}
                    },
                    "required": ["user_id", "role_id", "assigned_by", "assigned_on"]
                }
            }
        }
