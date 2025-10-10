# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RevokeRoleE2ETool(Tool):
    """
    revoke_role_e2e
    End-to-end right-sizing revoke:
      - Revoke the role (idempotent)
      - Append audit log with deterministic id
      - Return roles and active sessions for the user plus audit log id
    """

    @staticmethod
    def invoke(data: Dict[str, Any], revoked_by, role_id, user_id) -> str:
        if not user_id or not role_id or not revoked_by:
            return json.dumps(
                {"error": "user_id, role_id, revoked_by are required"}, indent=2
            )

        revoke_res = json.loads(
            RevokeUserRoleTool.invoke(
                data, user_id=user_id, role_id=role_id, revoked_by=revoked_by
            )
        )

        # Guarantee audit log entry (fixed identifier)
        audit = json.loads(
            AppendAuditLogTool.invoke(
                data,
                log_id=f"LOG-{user_id}-{role_id}-revoke",
                access_request=f"{user_id}-{role_id}-revoke",
                actor_id=revoked_by,
                action_type="revoke_role",
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_role_e2e",
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
