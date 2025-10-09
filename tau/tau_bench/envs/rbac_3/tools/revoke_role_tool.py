from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class RevokeRoleTool(Tool):
    """revoke_role: rescind a role and create a deterministic audit log."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None, actor_id: str = None, revoked_by: str = None) -> str:
        actor_id = actor_id or revoked_by
        base = json.loads(
            RevokeUserRoleTool.invoke(
                data, user_id=user_id, role_id=role_id, revoked_by=actor_id
            )
        )
        details = base.get("log_info", {}).values().get("details") or (
            "REMOVED" if base.get("removed") else "NOOP"
        )
        audit = json.loads(
            AppendAuditLogTool.invoke(
                data,
                log_id=f"LOG-{user_id}-{role_id}-revoke",
                access_request=f"{user_id}-{role_id}-revoke",
                actor_id=actor_id,
                action_type="RevokeRole",
                target_id=f"{user_id}:{role_id}",
                timestamp=_HARD_TS,
                details=details,
            )
        )
        out = dict(base)
        out["audit_log_id"] = audit.get("log_id")
        #Expose action_type for downstream validators to view the literal prior to utilization
        out["action_type"] = "RevokeRole"
        #Incorporate subject and body as requested
        #In revocation actions, we utilize APPROVED as the revocation was completed successfully
        out["subject"] = f"{role_id} APPROVED"
        out["body"] = f"{actor_id} {_HARD_TS}"
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeRole",
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
