# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RevokeRoleTool(Tool):
    """revoke_role: revoke a role and write a deterministic audit log."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        role_id = kwargs.get("role_id")
        actor_id = kwargs.get("actor_id") or kwargs.get("revoked_by")
        base = json.loads(
            RevokeUserRoleTool.invoke(
                data, user_id=user_id, role_id=role_id, revoked_by=actor_id
            )
        )
        details = base.get("log_info", {}).get("details") or (
            "REMOVED" if base.get("removed") else "NOOP"
        )
        audit = json.loads(
            AppendAuditLogTool.invoke(
                data,
                log_id=f"LOG-{user_id}-{role_id}-revoke",
                access_request=f"{user_id}-{role_id}-revoke",
                actor_id=actor_id,
                action_type="revoke_role",
                target_id=f"{user_id}:{role_id}",
                timestamp=_HARD_TS,
                details=details,
            )
        )
        out = dict(base)
        out["audit_log_id"] = audit.get("log_id")
        # Surface action_type so downstream validators see the literal before use
        out["action_type"] = "revoke_role"
        # Add subject and body as requested
        # For revoke operations, we use APPROVED since the revocation was successfully processed
        out["subject"] = f"{role_id} APPROVED"
        out["body"] = f"{actor_id} {_HARD_TS}"
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_role",
                "description": (
                    "Revoke a role from a user and record a deterministic audit log."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "actor_id": {"type": "string"},
                    },
                    "required": ["user_id", "role_id", "actor_id"],
                },
            },
        }
