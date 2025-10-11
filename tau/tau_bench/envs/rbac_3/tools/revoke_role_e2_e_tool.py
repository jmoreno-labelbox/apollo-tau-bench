# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






class RevokeUserRoleTool(Tool):
    """
    Revoke a user's role (spec-compliant).
    - Params: user_id, role_id, revoked_by
    - Behavior: remove matching user_roles entry if present; if you prefer soft-revoke for determinism,
      mark expires_on to the assignment's assigned_on.
    - Output: {"removed": true/false}
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        role_id = kwargs.get("role_id")
        revoked_by = kwargs.get("revoked_by")

        assignments = data.get("user_roles", [])
        removed = False

        kept: List[Dict[str, Any]] = []
        for assignment in assignments:
            if (
                assignment.get("user_id") == user_id
                and assignment.get("role_id") == role_id
                and not removed
            ):
                removed = True
            else:
                kept.append(assignment)

        if removed:
            data["user_roles"] = kept

        # Prepare audit log info
        action_details = "REMOVED" if removed else "NOOP"
        log_info = {
            "log_id": f"LOG-{user_id}-{role_id}-revoke",
            "actor_id": revoked_by,
            "action_type": "revoke_role",
            "target_id": f"{user_id}:{role_id}",
            "timestamp": _HARD_TS,
            "details": action_details,
        }

        return json.dumps(
            {
                "removed": bool(removed),
                "user_id": user_id,
                "role_id": role_id,
                "log_info": log_info,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_user_role",
                "description": (
                    "Revoke a specific role from a user (remove the assignment). Returns info for follow-up audit logging."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "revoked_by": {
                            "type": "string",
                            "description": "Reviewer/admin who revokes (e.g., U-010)",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": (
                                "ISO 8601 timestamp for when the revoke occurred"
                            ),
                        },
                    },
                    "required": ["user_id", "role_id", "revoked_by"],
                },
            },
        }

class AppendAuditLogTool(Tool):
    """append_audit_log"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Generate log_id if not provided
        if "log_id" not in kwargs or kwargs["log_id"] is None:
            access_request = kwargs["access_request"]
            log_id = f"LOG-{access_request}-decision"
        else:
            log_id = kwargs["log_id"]

        entry = {
            "log_id": log_id,
            "actor_id": kwargs["actor_id"],
            "action_type": kwargs["action_type"],
            "target_id": kwargs["target_id"],
            "timestamp": _HARD_TS,
            "details": kwargs.get("details", ""),
        }
        logs = data.setdefault("audit_logs", [])
        existing = next((l for l in logs if l.get("log_id") == entry["log_id"]), None)
        if existing is None:
            logs.append(entry)
            out = entry
        else:
            out = existing
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_audit_log",
                "description": "Append an audit log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {"type": "string"},
                        "access_request": {"type": "string"},
                        "actor_id": {"type": "string"},
                        "action_type": {"type": "string"},
                        "target_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "details": {"type": "string"},
                    },
                    "required": [
                        "access_request",
                        "actor_id",
                        "action_type",
                        "target_id",
                        "timestamp",
                    ],
                },
            },
        }

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