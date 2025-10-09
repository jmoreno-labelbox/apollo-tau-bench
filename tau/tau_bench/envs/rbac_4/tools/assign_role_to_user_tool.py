from tau_bench.envs.tool import Tool
import json
from typing import Any

class AssignRoleToUserTool(Tool):
    """Allocate a role to a user (write operation, predictable)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        role_id: str,
        assigned_by: str,
        assigned_on: str,
        expires_on: str = None
,
    expiry_policy: Any = None,
    ) -> str:
        user_roles = data.get("user_roles", [])
        users = data.get("users", [])
        roles = data.get("roles", [])
        if not isinstance(user_roles, list):
            payload = {"error": "user_roles must be a list"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(users, list):
            payload = {"error": "users must be a list"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(roles, list):
            payload = {"error": "roles must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        # Fundamental validation
        for fld, val in [
            ("user_id", user_id),
            ("role_id", role_id),
            ("assigned_by", assigned_by),
            ("assigned_on", assigned_on),
        ]:
            if not isinstance(val, str) or not val.strip():
                payload = {"error": f"{fld} must be a non-empty string"}
                out = json.dumps(payload, indent=2)
                return out

        if not any(u.get("user_id") == user_id for u in users):
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if not any(r.get("role_id") == role_id for r in roles):
            payload = {"error": f"role_id {role_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        # Avoid duplicate active assignments (no expires_on or expires_on set in the future)
        existing = [
            ur
            for ur in user_roles
            if ur.get("user_id") == user_id and ur.get("role_id") == role_id
        ]
        if existing:
            # If any current record remains active (no expiration or expiration set for later), prevent
            from datetime import datetime, timezone

            for ur in existing:
                exp = ur.get("expires_on")
                if exp is None:
                    payload = {"error": "Role already assigned"}
                    out = json.dumps(payload, indent=2)
                    return out
                try:
                    exp_dt = datetime.fromisoformat(exp.replace("Z", "+00:00"))
                except Exception:
                    payload = {"error": "Role already assigned"}
                    out = json.dumps(payload, indent=2)
                    return out
                now_tz = exp_dt.tzinfo or timezone.utc
                if exp_dt > datetime.now(tz=now_tz):
                    payload = {"error": "Role already assigned"}
                    out = json.dumps(payload, indent=2)
                    return out

        new_id = f"UR-{len(user_roles) + 1:03d}"
        record = {
            "user_role_id": new_id,
            "user_id": user_id,
            "role_id": role_id,
            "assigned_by": assigned_by,
            "assigned_on": assigned_on,
            "expires_on": expires_on,  # not mandatory
        }
        user_roles.append(record)
        payload = {
            "success": f"Role {role_id} assigned to {user_id}",
            "user_role_id": new_id,
        }
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignRoleToUser",
                "description": "Assign a role to a user with deterministic fields; blocks if an active assignment exists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "assigned_by": {"type": "string"},
                        "assigned_on": {"type": "string"},
                        "expires_on": {
                            "type": "string",
                            "description": "Optional ISO8601 end timestamp",
                        },
                    },
                    "required": ["user_id", "role_id", "assigned_by", "assigned_on"],
                },
            },
        }
