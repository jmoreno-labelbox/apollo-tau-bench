from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class RevokeRoleE2ETool(Tool):
    """
    revoke_role_e2e
    Comprehensive right-sizing revocation:
      - Rescind the role (idempotent)
      - Add to audit log with a deterministic id
      - Return roles and active sessions for the user along with audit log id
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None, revoked_by: str = None) -> str:
        if not user_id or not role_id or not revoked_by:
            payload = {"error": "user_id, role_id, revoked_by are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        revoke_res = json.loads(
            RevokeUserRoleTool.invoke(
                data, user_id=user_id, role_id=role_id, revoked_by=revoked_by
            )
        )

        # Confirm audit entry (predictable id)
        audit = json.loads(
            AppendAuditLogTool.invoke(
                data,
                log_id=f"LOG-{user_id}-{role_id}-revoke",
                access_request=f"{user_id}-{role_id}-revoke",
                actor_id=revoked_by,
                action_type="RevokeRole",
                target_id=f"{user_id}:{role_id}",
                timestamp=_HARD_TS,
                details=revoke_res.get("log_info", {}).get("details")
                or ("REMOVED" if revoke_res.get("removed") else "NOOP"),
            )
        )

        roles_after = [
            ur.get("role_id")
            for ur in data.get("user_roles", [])
            if ur.get("user_id") == user_id and not ur.get("expires_on")
        ]
        sessions_after = [
            s
            for s in data.get("sessions", [])
            if s.get("user_id") == user_id and not s.get("end_time")
        ]

        out = {
            "user_id": user_id,
            "role_id": role_id,
            "removed": bool(revoke_res.get("removed")),
            "roles": roles_after,
            "sessions": sessions_after,
            "audit_log_id": audit.get("log_id"),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revokeRoleE2e",
                "description": (
                    "End-to-end right-sizing revoke with audit and verification outputs."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "revoked_by": {"type": "string"},
                    },
                    "required": ["user_id", "role_id", "revoked_by"],
                },
            },
        }
