from domains.dto import Tool
from typing import Any, Dict, List, Optional, Tuple
import json
from datetime import datetime

_HARD_TS = "2024-06-26 16:05:00+00:00"


def _parse_iso(ts: Optional[str]) -> Optional[datetime]:
    """Robust ISO8601 parse: supports 'Z' and offsets; returns None if missing."""
    if not ts:
        return None
    ts = ts.replace("Z", "+00:00")
    return datetime.fromisoformat(ts)


def _eq(a: Optional[str], b: Optional[str]) -> bool:
    return (a or "") == (b or "")


class GetAccessRequestTool(Tool):
    """Fetch a single access request record by ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        if not request_id:
            return json.dumps({"error": "request_id is required"}, indent=2)

        requests: List[Dict[str, Any]] = data.get("access_requests", [])
        rec = next((r for r in requests if r.get("request_id") == request_id), None)
        if rec is None:
            return json.dumps(
                {"error": f"Access request {request_id} not found"}, indent=2
            )

        # normalize shape + provide stable defaults
        out = {
            "request_id": rec.get("request_id", request_id),
            "user_id": rec.get("user_id"),
            "resource_id": rec.get("resource_id"),
            "requested_role_id": rec.get("requested_role_id"),
            "justification": rec.get("justification"),
            "submitted_at": rec.get("submitted_at"),
            "status": rec.get("status"),
            "reviewed_by": rec.get("reviewed_by"),
            "decision_notes": rec.get("decision_notes"),
            "decision_at": rec.get("decision_at"),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_access_request",
                "description": "Return a single access request by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": (
                                "Unique access request identifier (e.g., AR-008)"
                            ),
                        }
                    },
                    "required": ["request_id"],
                },
            },
        }


class ReviewAccessRequestTool(Tool):
    """Approve or reject an access request with reviewer notes (deterministic decision_at + returns audit payload)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        reviewer_id = kwargs.get("reviewer_id")
        approve = kwargs.get("approve")
        notes = kwargs.get("notes")

        requests = data.get("access_requests", [])
        for req in requests:
            if req.get("request_id") == request_id:
                req["status"] = "APPROVED" if approve else "REJECTED"
                req["reviewed_by"] = reviewer_id
                req["decision_notes"] = notes
                req["decision_at"] = _HARD_TS
                # Idempotent audit entry so downstream list/filters never come
                # up empty
                logs = data.setdefault("audit_logs", [])
                log_id = f"LOG-{request_id}-decision"
                audit_entry = {
                    "log_id": log_id,
                    "actor_id": reviewer_id,
                    "action_type": "review_access_request",
                    "target_id": request_id,
                    "timestamp": _HARD_TS,
                    "details": req["status"],
                }
                existing = next((l for l in logs if l.get("log_id") == log_id), None)
                if existing:
                    existing.update(audit_entry)
                else:
                    logs.append(audit_entry)
                out = dict(req)
                out["audit_log"] = audit_entry
                # Add subject and body as requested
                status = req["status"]
                out["subject"] = f"{request_id} {status}"
                out["body"] = f"{reviewer_id} {_HARD_TS}"
                return json.dumps(out, indent=2)

        return json.dumps({"error": f"Access request {request_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "review_access_request",
                "description": (
                    "Approve or reject an access request by ID with reviewer notes."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "Unique request identifier",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "Reviewer's user ID (e.g., U-010)",
                        },
                        "approve": {
                            "type": "boolean",
                            "description": "True to approve, False to reject",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Decision notes explaining the reason",
                        },
                        "decision_at": {
                            "type": "string",
                            "description": (
                                "ISO 8601 timestamp of the decision (pass explicitly for determinism)"
                            ),
                        },
                    },
                    "required": ["request_id", "reviewer_id", "approve", "notes"],
                },
            },
        }


class GetUserRolesTool(Tool):
    """Retrieve all roles assigned to a given user (echo user_id for chaining)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        roles: List[str] = []
        assignments = data.get("user_roles", [])
        for assignment in assignments:
            if assignment.get("user_id") == user_id and not assignment.get(
                "expires_on"
            ):
                roles.append(assignment.get("role_id"))
        return json.dumps({"user_id": user_id, "roles": roles}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_roles",
                "description": "Get all active role IDs assigned to a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Unique user identifier (e.g., U-007)",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


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


class ListAuditLogsTool(Tool):
    """List audit logs with optional filters: action_type, user_id (actor_id), target_id, date range.
    Backward-compatible alias: filter_by == action_type.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        action_type = kwargs.get("action_type") or kwargs.get("filter_by")
        user_id = kwargs.get("user_id")
        target_id = kwargs.get("target_id")
        date_from = kwargs.get("date_from")
        date_to = kwargs.get("date_to")

        logs = data.get("audit_logs", [])
        out = []

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        for log in logs:
            if action_type and not _eq(log.get("action_type"), action_type):
                continue
            if user_id and not _eq(log.get("actor_id"), user_id):
                continue
            if target_id and not _eq(log.get("target_id"), target_id):
                continue

            if dt_from or dt_to:
                ts = _parse_iso(log.get("timestamp"))
                if dt_from and (not ts or ts < dt_from):
                    continue
                if dt_to and (not ts or ts > dt_to):
                    continue

            out.append(log)

        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_audit_logs",
                "description": "List audit logs with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action_type": {
                            "type": "string",
                            "description": "e.g., ACCESS_GRANTED, ACCESS_REJECTED",
                        },
                        "filter_by": {
                            "type": "string",
                            "description": "(alias) same as action_type",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Actor ID (maps to audit_logs.actor_id)",
                        },
                        "target_id": {"type": "string"},
                        "date_from": {
                            "type": "string",
                            "description": "ISO 8601 inclusive lower bound",
                        },
                        "date_to": {
                            "type": "string",
                            "description": "ISO 8601 inclusive upper bound",
                        },
                    },
                    "required": [],
                },
            },
        }


class ListActiveSessionsTool(Tool):
    """Return sessions with end_time == null (active sessions). Optional user_id filter. Echo user_id for chaining."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        sessions = data.get("sessions", [])
        active = [s for s in sessions if not s.get("end_time")]
        if user_id:
            active = [s for s in active if s.get("user_id") == user_id]
        return json.dumps({"user_id": user_id, "sessions": active}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_active_sessions",
                "description": (
                    "List active sessions where end_time is null; optionally filter by user_id."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Optional user filter (e.g., U-030)",
                        }
                    },
                    "required": [],
                },
            },
        }


class CreateAccessRequestTool(Tool):
    """create_access_request"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = {
            "request_id": kwargs["request_id"],
            "user_id": kwargs["user_id"],
            "resource_id": kwargs["resource_id"],
            "role": kwargs["requested_role_id"],
            "requested_role_id": kwargs["requested_role_id"],
            "justification": kwargs["justification"],
            "submitted_at": _HARD_TS,
            "status": "PENDING",
            "reviewed_by": None,
            "decision_notes": None,
            "decision_at": None,
        }
        ar = data.setdefault("access_requests", [])
        existing = next(
            (r for r in ar if r.get("request_id") == req["request_id"]), None
        )
        if existing is None:
            ar.append(req)
            out = req
        else:
            out = existing
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_access_request",
                "description": "Append a new access request (status=PENDING).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "requested_role_id": {"type": "string"},
                        "justification": {"type": "string"},
                        "submitted_at": {"type": "string"},
                    },
                    "required": [
                        "request_id",
                        "user_id",
                        "resource_id",
                        "requested_role_id",
                        "justification",
                        "submitted_at",
                    ],
                },
            },
        }


class ListAccessRequestsByStatusTool(Tool):
    """list_access_requests_by_status"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs["status"]
        out = [r for r in data.get("access_requests", []) if r.get("status") == status]
        out = sorted(
            out, key=lambda r: (r.get("submitted_at") or "", r.get("request_id") or "")
        )
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_access_requests_by_status",
                "description": "Filter access_requests by status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "enum": ["PENDING", "APPROVED", "REJECTED"],
                        }
                    },
                    "required": ["status"],
                },
            },
        }


class ListAccessRequestsByUserTool(Tool):
    """list_access_requests_by_user"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs["user_id"]
        out = [
            r for r in data.get("access_requests", []) if r.get("user_id") == user_id
        ]
        out = sorted(
            out, key=lambda r: (r.get("submitted_at") or "", r.get("request_id") or "")
        )
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_access_requests_by_user",
                "description": "Filter access_requests by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class AssignUserRoleTool(Tool):
    """assign_user_role"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_role_id = kwargs["user_role_id"]
        user_id = kwargs["user_id"]
        role_id = kwargs["role_id"]
        assigned_by = kwargs["assigned_by"]
        expires_on = kwargs.get("expires_on")
        roles = data.setdefault("user_roles", [])
        existing_active = next(
            (
                r
                for r in roles
                if r.get("user_id") == user_id
                and r.get("role_id") == role_id
                and not r.get("expires_on")
            ),
            None,
        )
        if existing_active:
            record = existing_active
        else:
            existing_by_id = next(
                (r for r in roles if r.get("user_role_id") == user_role_id), None
            )
            if existing_by_id:
                record = existing_by_id
            else:
                record = {
                    "user_role_id": user_role_id,
                    "user_id": user_id,
                    "role_id": role_id,
                    "assigned_by": assigned_by,
                    "assigned_on": _HARD_TS,
                    "expires_on": expires_on,
                }
                roles.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_user_role",
                "description": "Create a user_role assignment if not already active.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_role_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "assigned_by": {"type": "string"},
                        "assigned_on": {"type": "string"},
                        "expires_on": {"type": ["string", "null"]},
                    },
                    "required": [
                        "user_role_id",
                        "user_id",
                        "role_id",
                        "assigned_by",
                        "assigned_on",
                    ],
                },
            },
        }


class ListRolePermissionsTool(Tool):
    """list_role_permissions"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs["role_id"]
        role_perms = data.get("role_permissions", [])
        perms = data.get("permissions", [])
        perm_map = {p.get("permission_id"): p for p in perms}
        out = []
        for rp in role_perms:
            if rp.get("role_id") == role_id:
                p = perm_map.get(rp.get("permission_id"))
                if p:
                    out.append(
                        {
                            "permission_id": p.get("permission_id"),
                            "action": p.get("action"),
                            "resource_id": p.get("resource_id"),
                        }
                    )
        out = sorted(out, key=lambda p: (p.get("permission_id") or ""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_role_permissions",
                "description": "List permissions for a role.",
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }


class GetRoleNameTool(Tool):
    """get_role_name
    Lookup a role by role_id and return its role_name and metadata.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        if not role_id:
            return json.dumps({"error": "role_id is required"}, indent=2)

        roles: List[Dict[str, Any]] = data.get("roles", [])
        rec = next((r for r in roles if r.get("role_id") == role_id), None)
        if not rec:
            return json.dumps({"error": f"Role {role_id} not found"}, indent=2)

        out = {
            "role_id": rec.get("role_id"),
            "role_name": rec.get("role_name"),
            "description": rec.get("description"),
            "is_temporary": rec.get("is_temporary"),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_name",
                "description": "Return role_name and metadata for a given role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "Unique role identifier (e.g., ROL-001)",
                        }
                    },
                    "required": ["role_id"],
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


class LogRevokeDecisionTool(Tool):
    """log_revoke_decision
    Exclusively log revoke decisions using deterministic log_id and timestamp.
    - log_id format: LOG-<user_id>-<role_id>-decision
    - action_type: revoke_role
    - target_id: <user_id>:<role_id>
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        role_id = kwargs.get("role_id")
        actor_id = kwargs.get("actor_id")
        details = kwargs.get("details")
        revoked = kwargs.get("revoked")

        if not user_id or not role_id:
            return json.dumps({"error": "user_id and role_id are required"}, indent=2)

        log_id = f"LOG-{user_id}-{role_id}-decision"
        # Derive default details if not explicitly provided
        if details is None:
            if revoked is True:
                details = "REMOVED"
            elif revoked is False:
                details = "NOOP"
            else:
                details = ""

        entry = {
            "log_id": log_id,
            "actor_id": actor_id,
            "action_type": "revoke_role",
            "target_id": f"{user_id}:{role_id}",
            "timestamp": _HARD_TS,
            "details": details,
        }

        logs: List[Dict[str, Any]] = data.setdefault("audit_logs", [])
        existing = next((l for l in logs if l.get("log_id") == log_id), None)
        if existing:
            existing.update(entry)
            out = existing
        else:
            logs.append(entry)
            out = entry
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_revoke_decision",
                "description": (
                    "Append an audit log entry for a revoke decision with deterministic id and timestamp."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "actor_id": {"type": "string"},
                        "details": {"type": "string"},
                        "revoked": {
                            "type": "boolean",
                            "description": (
                                "If provided and details omitted, sets details to REMOVED/NOOP accordingly."
                            ),
                        },
                    },
                    "required": ["user_id", "role_id"],
                },
            },
        }


class GetAccessRequestDetailsTool(Tool):
    """get_access_request_details: richer alias for getting AR details."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return GetAccessRequestTool.invoke(data, **kwargs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_access_request_details",
                "description": "Return detailed access request info by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"request_id": {"type": "string"}},
                    "required": ["request_id"],
                },
            },
        }


class UpdateAccessRequestStatusTool(Tool):
    """update_access_request_status: approve/reject with notes and audit."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # support either approve/notes or explicit status
        status = kwargs.get("status")
        approve = kwargs.get("approve")
        notes = kwargs.get("notes")
        if status is not None and approve is None:
            approve = True if str(status).upper() == "APPROVED" else False
        return ReviewAccessRequestTool.invoke(
            data,
            request_id=kwargs.get("request_id"),
            reviewer_id=kwargs.get("reviewer_id"),
            approve=approve,
            notes=notes,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_access_request_status",
                "description": (
                    "Approve or reject an access request with reviewer notes and audit."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "approve": {"type": "boolean"},
                        "status": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["request_id", "reviewer_id"],
                },
            },
        }


class GrantRoleTool(Tool):
    """grant_role: assign a role either by request_id or direct user_id/role_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        assigned_by = kwargs.get("assigned_by")
        if request_id:
            return AssignRoleOnApprovalTool.invoke(
                data, request_id=request_id, assigned_by=assigned_by
            )
        # direct
        return AssignUserRoleTool.invoke(
            data,
            user_role_id=kwargs.get("user_role_id"),
            user_id=kwargs.get("user_id"),
            role_id=kwargs.get("role_id"),
            assigned_by=assigned_by,
            expires_on=kwargs.get("expires_on"),
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "grant_role",
                "description": "Assign a role by request_id or direct user/role pair.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "user_role_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "assigned_by": {"type": "string"},
                        "expires_on": {"type": ["string", "null"]},
                    },
                    "required": ["assigned_by"],
                },
            },
        }


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


class SendEmailTool(Tool):
    """send_email: convenience wrapper around upsert for creation-only."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email_id = kwargs.get("email_id")
        receiver = kwargs.get("receiver")
        user_id = kwargs.get("user_id")
        subject = kwargs.get("subject")
        text_content = kwargs.get("text_content")
        sender = kwargs.get("sender")

        if not email_id or not subject or not text_content:
            return json.dumps(
                {"error": "email_id, subject, and text_content are required"},
                indent=2,
            )

        # If receiver not provided, try to resolve from user_id
        if not receiver and user_id:
            users: List[Dict[str, Any]] = data.get("users", [])
            user = next((u for u in users if u.get("user_id") == user_id), None)
            if not user or not user.get("email"):
                return json.dumps(
                    {"error": f"Could not resolve email for user_id {user_id}"},
                    indent=2,
                )
            receiver = user.get("email")

        if not receiver:
            return json.dumps(
                {"error": "receiver or user_id must be provided"}, indent=2
            )

        return UpsertEmailTool.invoke(
            data,
            email_id=email_id,
            receiver=receiver,
            subject=subject,
            text_content=text_content,
            sender=sender,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email",
                "description": (
                    "Send an email record (deterministic timestamp). Provide receiver or user_id to resolve email."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email_id": {"type": "string"},
                        "user_id": {
                            "type": "string",
                            "description": (
                                "If provided, resolves receiver from users[].email"
                            ),
                        },
                        "receiver": {"type": "string"},
                        "subject": {"type": "string"},
                        "text_content": {"type": "string"},
                        "sender": {"type": "string"},
                    },
                    "required": ["email_id", "subject", "text_content"],
                },
            },
        }


class GetUserSessionsTool(Tool):
    """get_user_sessions: alias to list active sessions for a user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return ListActiveSessionsTool.invoke(data, **kwargs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_sessions",
                "description": "Return active sessions for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class UpdateHubspotTicketStatusTool(Tool):
    """update_hubspot_ticket_status: set status with audit."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return UpdateHubspotTicketTool.invoke(
            data,
            ticket_id=kwargs.get("ticket_id"),
            status=kwargs.get("status"),
            actor_id=kwargs.get("actor_id"),
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_hubspot_ticket_status",
                "description": "Update a HubSpot ticket status (writes audit entry).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "status": {"type": "string"},
                        "actor_id": {"type": "string"},
                    },
                    "required": ["ticket_id", "status"],
                },
            },
        }


class UpdateHubspotTicketAssigneeTool(Tool):
    """update_hubspot_ticket_assignee: set assignee with audit."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return UpdateHubspotTicketTool.invoke(
            data,
            ticket_id=kwargs.get("ticket_id"),
            assignee_id=kwargs.get("assignee_id"),
            actor_id=kwargs.get("actor_id"),
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_hubspot_ticket_assignee",
                "description": "Update a HubSpot ticket assignee (writes audit entry).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "assignee_id": {"type": "string"},
                        "actor_id": {"type": "string"},
                    },
                    "required": ["ticket_id", "assignee_id"],
                },
            },
        }


class GetCurrentTimeTool(Tool):
    """get_current_time: returns deterministic timestamp used across writes."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"timestamp": _HARD_TS}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Return deterministic current time used for writes.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class GetUsersByRoleTool(Tool):
    """get_users_by_role: list user_ids having a role assigned (active only)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        result = [
            ur.get("user_id")
            for ur in data.get("user_roles", [])
            if ur.get("role_id") == role_id and not ur.get("expires_on")
        ]
        return json.dumps({"role_id": role_id, "user_ids": sorted(result)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_users_by_role",
                "description": (
                    "List users with an active assignment of the given role."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }


class GetRolePermissionsAliasTool(Tool):
    """get_role_permissions: alias for list_role_permissions."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return ListRolePermissionsTool.invoke(data, **kwargs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_permissions",
                "description": "Return permissions for a role.",
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }


class GetHubspotTicketsByRequesterTool(Tool):
    """get_hubspot_tickets_by_requester: filter tickets by requester."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return ListHubspotTicketsTool.invoke(
            data, requester_id=kwargs.get("requester_id")
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_hubspot_tickets_by_requester",
                "description": "List HubSpot tickets for a requester.",
                "parameters": {
                    "type": "object",
                    "properties": {"requester_id": {"type": "string"}},
                    "required": ["requester_id"],
                },
            },
        }


class GetHubspotTicketsByAssigneeTool(Tool):
    """get_hubspot_tickets_by_assignee: filter tickets by assignee."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # reuse list tool with post-filter
        tickets = json.loads(ListHubspotTicketsTool.invoke(data))
        assignee_id = kwargs.get("assignee_id")
        return json.dumps(
            [t for t in tickets if t.get("assignee_id") == assignee_id], indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_hubspot_tickets_by_assignee",
                "description": "List HubSpot tickets for an assignee.",
                "parameters": {
                    "type": "object",
                    "properties": {"assignee_id": {"type": "string"}},
                    "required": ["assignee_id"],
                },
            },
        }


class CompleteCertificationTool(Tool):
    """complete_certification"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cert_id = kwargs["certification_id"]
        reviewer_id = kwargs.get("reviewer_id")

        certs = data.get("certifications", [])
        c = None
        for x in certs:
            if x.get("certification_id") == cert_id:
                c = x
                break
        c["status"] = "COMPLETED"
        c["completed_on"] = _HARD_TS
        if reviewer_id:
            c["reviewer_id"] = reviewer_id
        return json.dumps(c, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_certification",
                "description": (
                    "Mark a certification as COMPLETED with completed_on timestamp."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"},
                        "completed_on": {"type": "string"},
                        "reviewer_id": {
                            "type": "string",
                            "description": (
                                "Optional reviewer ID to reassign certification (e.g., U-005)"
                            ),
                        },
                    },
                    "required": ["certification_id", "completed_on"],
                },
            },
        }


class StartCertificationTool(Tool):
    """start_certification"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cert_id = kwargs["certification_id"]
        reviewer_id = kwargs.get("reviewer_id")
        certs = data.get("certifications", [])
        c = None
        for x in certs:
            if x.get("certification_id") == cert_id:
                c = x
                break
        c["status"] = "IN_PROGRESS"
        c["completed_on"] = None
        if reviewer_id:
            c["reviewer_id"] = reviewer_id
        return json.dumps(c, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "start_certification",
                "description": "Set a certification status to IN_PROGRESS.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"},
                        "reviewer_id": {
                            "type": "string",
                            "description": (
                                "Optional reviewer ID to reassign certification (e.g., U-005)"
                            ),
                        },
                    },
                    "required": ["certification_id"],
                },
            },
        }


class ListCertificationsByStatusTool(Tool):
    """list_certifications_by_status"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        certification_id = kwargs.get("certification_id")

        out = [
            c
            for c in data.get("certifications", [])
            if (status is None or c.get("status") == status)
            and (
                certification_id is None
                or c.get("certification_id") == certification_id
            )
        ]
        out = sorted(out, key=lambda c: (c.get("certification_id") or ""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_certifications_by_status",
                "description": (
                    "Filter certifications by optional status and/or certification_id."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "enum": ["PENDING", "IN_PROGRESS", "COMPLETED"],
                        },
                        "certification_id": {
                            "type": "string",
                            "description": (
                                "Optional certification identifier to further filter results."
                            ),
                        },
                    },
                    "required": [],
                },
            },
        }


class GetPermissionsForUserTool(Tool):
    """get_permissions_for_user"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs["user_id"]
        roles_active = [
            r.get("role_id")
            for r in data.get("user_roles", [])
            if r.get("user_id") == user_id and not r.get("expires_on")
        ]
        role_perms = data.get("role_permissions", [])
        perms = data.get("permissions", [])
        perm_map = {p.get("permission_id"): p for p in perms}
        seen = set()
        result: List[Dict[str, Any]] = []
        for rp in role_perms:
            if rp.get("role_id") in roles_active:
                p = perm_map.get(rp.get("permission_id"))
                if p and p.get("permission_id") not in seen:
                    seen.add(p.get("permission_id"))
                    result.append(
                        {
                            "permission_id": p.get("permission_id"),
                            "action": p.get("action"),
                            "resource_id": p.get("resource_id"),
                        }
                    )
        result = sorted(result, key=lambda p: (p.get("permission_id") or ""))
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_permissions_for_user",
                "description": (
                    "Resolve permissions for a user via user_roles → role_permissions → permissions."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class CheckUserStatusTool(Tool):
    """
    check_user_status
    DB-driven gate: returns a literal boolean `approve` plus literals needed for the next actions.

    Policy (derived from DB state):
      1) Request must have status='PENDING'
      2) If the requested role is ALREADY assigned to the user -> approve=False, notes='Already assigned.'
      3) Admin-like roles are derived dynamically from the DB:
         - any role whose role_name ends with '-lead' (e.g., engineering-lead, operations-lead, ...), OR
         - any role whose role_name contains '-admin' (e.g., hr-payroll-admin, finance-budget-admin, ...).
      4) Exception: ROL-032 (finance-budget-admin) may be approved iff the user already has ROL-029 (finance-base).
      5) Check resource coverage: requested role must grant permissions on target resource
      6) Check certification requirements for target resource
      7) Check for active policy exceptions
      8) Otherwise -> approve=True.
    All decisions use the actual request record and current assignments in `data`.
    """

    @staticmethod
    def _admin_like_roles(data: Dict[str, Any]) -> set:
        roles = data.get("roles", [])
        admin_like = set()
        for r in roles:
            name = (r.get("role_name") or "").lower()
            rid = r.get("role_id")
            if not rid or not name:
                continue
            # Leadership roles: strict suffix '-lead' (avoids
            # 'sales-lead-manager' false-positive)
            if name.endswith("-lead"):
                admin_like.add(rid)
            # Administrative roles: any containing '-admin'
            if "-admin" in name:
                admin_like.add(rid)
        return admin_like

    @staticmethod
    def _check_resource_coverage(
        data: Dict[str, Any], role_id: str, resource_id: str
    ) -> bool:
        """Check if role grants any permissions on the target resource."""
        role_permissions = [
            rp.get("permission_id")
            for rp in data.get("role_permissions", [])
            if rp.get("role_id") == role_id
        ]

        for perm_id in role_permissions:
            permission = next(
                (
                    p
                    for p in data.get("permissions", [])
                    if p.get("permission_id") == perm_id
                ),
                None,
            )
            if permission and permission.get("resource_id") == resource_id:
                return True
        return False

    @staticmethod
    def _check_certifications(
        data: Dict[str, Any], user_id: str, resource_id: Optional[str]
    ) -> tuple:
        """Check certification requirements for a resource. Returns (has_requirements, all_completed, reviewer_id)."""
        required_certs = []
        if resource_id:
            required_certs = [
                cert
                for cert in data.get("certifications", [])
                if cert.get("resource_id") == resource_id
            ]

        if not required_certs:
            return (False, True, None)

        all_completed = True
        reviewer_id = None
        for cert in required_certs:
            if cert.get("status") != "COMPLETED":
                all_completed = False
            if not reviewer_id:
                reviewer_id = cert.get("reviewer_id")
        return (True, all_completed, reviewer_id)

    @staticmethod
    def _check_certifications_for_role(
        data: Dict[str, Any],
        user_id: str,
        role_id: Optional[str],
        role_permissions_resource_ids: List[str],
    ) -> tuple:
        """Check certifications either tied to role_id (if present) or implied via role's resources. Returns (has_requirements, all_completed, reviewer_id)."""
        certs = data.get("certifications", [])
        required = []
        if role_id:
            required = [c for c in certs if c.get("role_id") == role_id]
        if not required and role_permissions_resource_ids:
            required = [
                c
                for c in certs
                if c.get("resource_id") in role_permissions_resource_ids
            ]
        if not required:
            return (False, True, None)
        all_completed = True
        reviewer_id = None
        for cert in required:
            if cert.get("status") != "COMPLETED":
                all_completed = False
            if not reviewer_id:
                reviewer_id = cert.get("reviewer_id")
        return (True, all_completed, reviewer_id)

    @staticmethod
    def _reviewer_authorized(data: Dict[str, Any], reviewer_id: Optional[str]) -> bool:
        if not reviewer_id:
            return True
        lead_roles = {"ROL-034", "ROL-035", "ROL-036", "ROL-037", "ROL-038", "ROL-039"}
        return any(
            ur.get("user_id") == reviewer_id
            and ur.get("role_id") in lead_roles
            and not ur.get("expires_on")
            for ur in data.get("user_roles", [])
        )

    @staticmethod
    def _check_policy_exceptions(
        data: Dict[str, Any], user_id: str, role_id: str, resource_id: str
    ) -> bool:
        """Check for active policy exceptions for user/permission combination."""
        # Get permissions for the requested role
        role_permissions = [
            rp.get("permission_id")
            for rp in data.get("role_permissions", [])
            if rp.get("role_id") == role_id
        ]

        # Check if user has active policy exceptions for any of these permissions
        for perm_id in role_permissions:
            exception = next(
                (
                    pe
                    for pe in data.get("policy_exceptions", [])
                    if (
                        pe.get("user_id") == user_id
                        and pe.get("permission_id") == perm_id
                        and pe.get("status") == "APPROVED"
                        and (
                            pe.get("expires_on") is None
                            or pe.get("expires_on") > _HARD_TS
                        )
                    )
                ),
                None,
            )
            if exception:
                return True
        return False

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        mode = (kwargs.get("mode") or "access_request").lower()

        # Branch: revoke evaluation
        if mode in ("revoke", "revoke_evaluation"):
            user_id = kwargs.get("user_id")
            role_id = kwargs.get("role_id")
            resource_id = kwargs.get("resource_id")
            if not user_id or not role_id:
                return json.dumps(
                    {"error": "user_id and role_id are required for revoke evaluation"},
                    indent=2,
                )

            # Verify assignment exists
            active_assignment = any(
                ur.get("user_id") == user_id
                and ur.get("role_id") == role_id
                and not ur.get("expires_on")
                for ur in data.get("user_roles", [])
            )
            if not active_assignment:
                return json.dumps(
                    {
                        "user_id": user_id,
                        "role_id": role_id,
                        "revoke": False,
                        "notes": "Already assigned." if False else "Role not assigned.",
                        "details": "NOOP",
                    },
                    indent=2,
                )

            # Determine role permissions resource IDs
            role_perm_ids = [
                rp.get("permission_id")
                for rp in data.get("role_permissions", [])
                if rp.get("role_id") == role_id
            ]
            perm_resource_ids = [
                p.get("resource_id")
                for p in data.get("permissions", [])
                if p.get("permission_id") in role_perm_ids
            ]

            # Resource coverage check (if resource_id provided)
            if resource_id and not CheckUserStatusTool._check_resource_coverage(
                data, role_id, resource_id
            ):
                return json.dumps(
                    {
                        "user_id": user_id,
                        "role_id": role_id,
                        "revoke": True,
                        "notes": "Requested role does not cover target resource.",
                        "details": "REVOKE_RESOURCE_MISMATCH",
                    },
                    indent=2,
                )

            # Certification requirements
            has_req, all_completed, _ = (
                CheckUserStatusTool._check_certifications_for_role(
                    data, user_id, role_id, perm_resource_ids
                )
            )
            if has_req and not all_completed:
                return json.dumps(
                    {
                        "user_id": user_id,
                        "role_id": role_id,
                        "revoke": True,
                        "notes": "Required certification not completed.",
                        "details": "REVOKE_CERT_INCOMPLETE",
                    },
                    indent=2,
                )

            # Admin-like roles can be candidates for right-sizing
            if role_id in CheckUserStatusTool._admin_like_roles(data):
                return json.dumps(
                    {
                        "user_id": user_id,
                        "role_id": role_id,
                        "revoke": True,
                        "notes": "Admin-like role blocked by policy.",
                        "details": "REVOKE_ADMINLIKE",
                    },
                    indent=2,
                )

            # Default: do not revoke
            return json.dumps(
                {
                    "user_id": user_id,
                    "role_id": role_id,
                    "revoke": False,
                    "notes": "Within clearance and least-privilege.",
                    "details": "NO_REVOKE",
                },
                indent=2,
            )

        # Default branch: access request decision
        request_id = kwargs.get("request_id")
        reviewer_id = kwargs.get("reviewer_id")
        if not request_id:
            return json.dumps({"error": "request_id is required"}, indent=2)
        req = next(
            (
                r
                for r in data.get("access_requests", [])
                if r.get("request_id") == request_id
            ),
            None,
        )
        if not req:
            return json.dumps(
                {"error": f"Access request {request_id} not found"}, indent=2
            )

        # Check request status first (Rule 1)
        if req.get("status") != "PENDING":
            return json.dumps(
                {
                    "error": (
                        f"Access request {request_id} is not PENDING (status: {req.get('status')})"
                    )
                },
                indent=2,
            )

        # Reviewer authorization (if provided)
        if reviewer_id and not CheckUserStatusTool._reviewer_authorized(
            data, reviewer_id
        ):
            return json.dumps(
                {
                    "error": (
                        f"Reviewer {reviewer_id} not authorized (lead role required)."
                    )
                },
                indent=2,
            )

        user_id = req.get("user_id")
        role_id = req.get("role") or req.get("requested_role_id")
        resource_id = req.get("resource_id")
        submitted_at = req.get("submitted_at")

        # Current roles from DB
        current_roles = [
            ur.get("role_id")
            for ur in data.get("user_roles", [])
            if ur.get("user_id") == user_id and not ur.get("expires_on")
        ]

        # Rule 2: duplicate request
        if role_id in current_roles:
            approve = False
            notes = "Already assigned."
        else:
            # Check resource coverage first (Rule 5)
            if not CheckUserStatusTool._check_resource_coverage(
                data, role_id, resource_id
            ):
                approve = False
                notes = "Requested role does not cover target resource."
            else:
                admin_like_block = CheckUserStatusTool._admin_like_roles(data)

                # Rule 4 (placed before generic admin-like block): ROL-032 prereq
                if role_id == "ROL-032":
                    approve = "ROL-029" in current_roles
                    notes = (
                        "Met prerequisite finance-base (ROL-029)."
                        if approve
                        else "Missing prerequisite finance-base (ROL-029)."
                    )
                # Rule 3: dynamic admin-like block
                elif role_id in admin_like_block:
                    approve = False
                    notes = "Admin-like role blocked by policy."
                else:
                    # Rule 6: Check certification requirements
                    has_cert_reqs, all_certs_completed, cert_reviewer_id = (
                        CheckUserStatusTool._check_certifications(
                            data, user_id, resource_id
                        )
                    )

                    if has_cert_reqs and not all_certs_completed:
                        approve = False
                        notes = "Required certification not completed."
                    else:
                        # Rule 7: Check policy exceptions
                        has_policy_exception = (
                            CheckUserStatusTool._check_policy_exceptions(
                                data, user_id, role_id, resource_id
                            )
                        )

                        if has_policy_exception:
                            approve = True
                            notes = "Policy exception approved."
                        else:
                            # Rule 8: Default approval with appropriate notes
                            approve = True
                            if has_cert_reqs and all_certs_completed:
                                notes = "Certification verified; within clearance and least-privilege."
                            else:
                                notes = "Within clearance and least-privilege."

        decision_at = submitted_at
        details = "APPROVED" if approve else "REJECTED"
        out = {
            "request_id": request_id,
            "user_id": user_id,
            "resource_id": resource_id,
            "requested_role_id": role_id,
            "approve": bool(approve),
            "notes": notes,
            "decision_at": _HARD_TS,
            "log_id": f"LOG-{request_id}-decision",
            "details": details,
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_user_status",
                "description": (
                    "Policy evaluation. mode='access_request' to evaluate an access request (approve/deny) or "
                    "mode='revoke' to recommend role revocation (revoke/do-not-revoke) with decision notes."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode": {
                            "type": "string",
                            "enum": ["access_request", "revoke", "revoke_evaluation"],
                        },
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class AssignRoleOnApprovalTool(Tool):
    """
    Idempotently assign the role from an approved access request and ALWAYS
    return a user_role_id. Also heals existing assignments missing user_role_id.
    """

    @staticmethod
    def _derive_user_role_id(request_id: str, user_id: str, role_id: str) -> str:
        # Stable, deterministic; keeps it short if you prefer only digits
        import re

        digits = "".join(re.findall(r"\d+", request_id)) or "000"
        return f"UR-{digits}"

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import json as _json

        request_id = kwargs.get("request_id")
        assigned_by = kwargs.get("assigned_by")
        provided_urid = kwargs.get("user_role_id")

        if not request_id or not assigned_by:
            return _json.dumps(
                {"error": "request_id and assigned_by are required"}, indent=2
            )

        # Locate the access request
        requests = data.get("access_requests", [])
        req = next((r for r in requests if r.get("request_id") == request_id), None)
        if not req:
            return _json.dumps(
                {"error": f"Access request {request_id} not found"}, indent=2
            )

        user_id = req.get("user_id")
        role_id = req.get("requested_role_id")

        if not user_id or not role_id:
            return _json.dumps(
                {"error": f"Request {request_id} missing user_id/requested_role_id"},
                indent=2,
            )

        assignments: List[Dict[str, Any]] = data.setdefault("user_roles", [])

        # Try to find an active existing assignment
        existing = next(
            (
                a
                for a in assignments
                if a.get("user_id") == user_id
                and a.get("role_id") == role_id
                and not a.get("expires_on")
            ),
            None,
        )

        if existing:
            # Heal missing user_role_id if necessary
            if "user_role_id" not in existing or not existing["user_role_id"]:
                existing["user_role_id"] = (
                    provided_urid
                    or AssignRoleOnApprovalTool._derive_user_role_id(
                        request_id, user_id, role_id
                    )
                )
            # Ensure required fields are present
            existing.setdefault("assigned_by", assigned_by)
            existing.setdefault("assigned_on", _HARD_TS)
            existing.setdefault("expires_on", None)

            out = {
                "user_role_id": existing["user_role_id"],
                "user_id": user_id,
                "role_id": role_id,
                "assigned_by": existing["assigned_by"],
                "assigned_on": _HARD_TS,
                "expires_on": existing["expires_on"],
            }
            return _json.dumps(out, indent=2)

        # Create a brand-new assignment
        user_role_id = provided_urid or AssignRoleOnApprovalTool._derive_user_role_id(
            request_id, user_id, role_id
        )

        record = {
            "user_role_id": user_role_id,
            "user_id": user_id,
            "role_id": role_id,
            "assigned_by": assigned_by,
            "assigned_on": _HARD_TS,
            "expires_on": None,
        }
        assignments.append(record)

        out = {
            "user_role_id": user_role_id,
            "user_id": user_id,
            "role_id": role_id,
            "assigned_by": assigned_by,
            "assigned_on": _HARD_TS,
            "expires_on": None,
        }
        return _json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_role_on_approval",
                "description": (
                    "Assign the role from an approved access request (idempotent; always returns user_role_id)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "Access request ID (e.g., AR-008)",
                        },
                        "assigned_by": {
                            "type": "string",
                            "description": (
                                "Reviewer's user ID who approved the request (e.g., U-010)"
                            ),
                        },
                        "user_role_id": {
                            "type": "string",
                            "description": (
                                "Optional stable assignment ID to use (e.g., reuse audit log id)"
                            ),
                        },
                    },
                    "required": ["request_id", "assigned_by"],
                },
            },
        }


class ListPolicyExceptionsTool(Tool):
    """
    list_policy_exceptions

    Lists policy exception records with optional filters:
      - user_id:       filter to a specific user
      - permission_id: filter to a specific permission
      - status:        filter by exception status (e.g., APPROVED, DENIED, EXPIRED, PENDING)
      - requested_on_from / requested_on_to: inclusive ISO-8601 bounds on requested_on
      - active_only:   if True, return only non-denied/non-expired records

    Results are returned sorted by requested_on, then exception_id for determinism.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        permission_id = kwargs.get("permission_id")
        status = kwargs.get("status")
        active_only = bool(kwargs.get("active_only", False))

        # Support both specific and generic names for date filters (parity with
        # other tools)
        date_from = kwargs.get("requested_on_from") or kwargs.get("date_from")
        date_to = kwargs.get("requested_on_to") or kwargs.get("date_to")

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        exceptions: List[Dict[str, Any]] = data.get("policy_exceptions", [])
        out: List[Dict[str, Any]] = []

        for rec in exceptions:
            if user_id and not _eq(rec.get("user_id"), user_id):
                continue
            if permission_id and not _eq(rec.get("permission_id"), permission_id):
                continue
            if status and not _eq(rec.get("status"), status):
                continue
            if active_only and (rec.get("status") in ("DENIED", "EXPIRED")):
                continue

            # Date filter on requested_on
            if dt_from or dt_to:
                ts = _parse_iso(rec.get("requested_on"))
                if dt_from and (not ts or ts < dt_from):
                    continue
                if dt_to and (not ts or ts > dt_to):
                    continue

            out.append(rec)

        out.sort(
            key=lambda r: ((r.get("requested_on") or ""), (r.get("exception_id") or ""))
        )
        import json as _json

        return _json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_policy_exceptions",
                "description": (
                    "List policy exceptions with optional filters (user_id, permission_id, status, requested_on bounds, active_only)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Filter by user (e.g., U-026)",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "Filter by permission (e.g., P-014)",
                        },
                        "status": {
                            "type": "string",
                            "description": (
                                "Filter by status (e.g., APPROVED, DENIED, EXPIRED, PENDING)"
                            ),
                        },
                        "requested_on_from": {
                            "type": "string",
                            "description": (
                                "ISO 8601 inclusive lower bound for requested_on"
                            ),
                        },
                        "requested_on_to": {
                            "type": "string",
                            "description": (
                                "ISO 8601 inclusive upper bound for requested_on"
                            ),
                        },
                        "date_from": {
                            "type": "string",
                            "description": (
                                "(alias) inclusive lower bound for requested_on"
                            ),
                        },
                        "date_to": {
                            "type": "string",
                            "description": (
                                "(alias) inclusive upper bound for requested_on"
                            ),
                        },
                        "active_only": {
                            "type": "boolean",
                            "description": (
                                "If true, exclude DENIED and EXPIRED records"
                            ),
                        },
                    },
                    "required": [],
                },
            },
        }


from datetime import datetime, timedelta


class GetTimeWindowTool(Tool):
    """
    get_time_window
    Given an ISO8601 timestamp and one or both of:
      - days:  e.g., "1d", "5d", "-5d"
      - hours: e.g., "1h", "3h", "4.5h", "-1h"
    returns {"date_from": <ts>, "date_to": <ts + delta>} (both ISO-8601, preserving offset).
    If only negative values are provided, date_to will be the original ts and date_from will be ts + delta.
    """

    @staticmethod
    def _parse_iso(ts: str) -> datetime:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))

    @staticmethod
    def _parse_offset(s: Optional[str], unit: str) -> float:
        if not s:
            return 0.0
        s = s.strip().lower()
        assert s.endswith(unit), f"Offset must end with '{unit}'"
        return float(s[:-1])

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import json

        ts = kwargs.get("timestamp")
        days = kwargs.get("days")
        hours = kwargs.get("hours")
        if not ts:
            return json.dumps({"error": "timestamp is required"}, indent=2)

        base = GetTimeWindowTool._parse_iso(ts)
        d = GetTimeWindowTool._parse_offset(days, "d") if days else 0.0
        h = GetTimeWindowTool._parse_offset(hours, "h") if hours else 0.0
        delta = timedelta(days=d, hours=h)

        # Determine window direction
        if d < 0 or h < 0:
            start, end = base + delta, base
        else:
            start, end = base, base + delta

        # Keep the exact "+00:00" style if present in input
        def fmt(dt: datetime) -> str:
            s = dt.isoformat()
            if s.endswith("+00:00"):
                return s
            if s[-6] in ["+", "-"] and s[-3] == ":":
                return s
            return s

        out = {"date_from": fmt(start), "date_to": fmt(end)}
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_time_window",
                "description": (
                    "Derive a time window from a base timestamp and offsets (days/hours)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": (
                                "ISO 8601 timestamp (e.g., 2024-06-01T00:00:00+00:00)"
                            ),
                        },
                        "days": {
                            "type": "string",
                            "description": "Relative days like '5d', '-5d'",
                        },
                        "hours": {
                            "type": "string",
                            "description": "Relative hours like '3h', '4.5h', '-1h'",
                        },
                    },
                    "required": ["timestamp"],
                },
            },
        }


class GetUserEmailTool(Tool):
    """get_user_email"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        if not user_id:
            return json.dumps({"error": "user_id is required"}, indent=2)

        users: List[Dict[str, Any]] = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({"error": f"User {user_id} not found"}, indent=2)

        out = {
            "user_id": user.get("user_id"),
            "username": user.get("username"),
            "email": user.get("email"),
            "status": user.get("status"),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_email",
                "description": (
                    "Return the email address and username for a given user_id."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Unique user identifier (e.g., U-007)",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class ListEmailsTool(Tool):
    """list_emails"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        receiver = kwargs.get("receiver")
        email_id = kwargs.get("email_id")
        date_from = kwargs.get("date_from")
        date_to = kwargs.get("date_to")

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        emails: List[Dict[str, Any]] = data.get("emails", [])
        out: List[Dict[str, Any]] = []

        for e in emails:
            if receiver and not _eq(e.get("receiver"), receiver):
                continue
            if email_id and not _eq(e.get("email_id"), email_id):
                continue

            if dt_from or dt_to:
                ts = _parse_iso(e.get("timestamp"))
                if dt_from and (not ts or ts < dt_from):
                    continue
                if dt_to and (not ts or ts > dt_to):
                    continue

            out.append(e)

        out.sort(key=lambda r: ((r.get("timestamp") or ""), (r.get("email_id") or "")))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_emails",
                "description": (
                    "List email records with optional filters for receiver, email_id, and date range."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "receiver": {
                            "type": "string",
                            "description": "Email address of the recipient.",
                        },
                        "email_id": {
                            "type": "string",
                            "description": "Specific email record ID (e.g., EM-001)",
                        },
                        "date_from": {
                            "type": "string",
                            "description": "ISO 8601 lower bound for timestamp.",
                        },
                        "date_to": {
                            "type": "string",
                            "description": "ISO 8601 upper bound for timestamp.",
                        },
                    },
                    "required": [],
                },
            },
        }


class ListSiemAlertsTool(Tool):
    """list_siem_alerts"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        resource_id = kwargs.get("resource_id")
        severity = kwargs.get("severity")
        alert_type = kwargs.get("alert_type")
        alert_id = kwargs.get("alert_id")
        date_from = kwargs.get("date_from")
        date_to = kwargs.get("date_to")

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        alerts: List[Dict[str, Any]] = data.get("siem_alerts", [])
        out: List[Dict[str, Any]] = []
        for a in alerts:
            if user_id and not _eq(a.get("user_id"), user_id):
                continue
            if resource_id and not _eq(a.get("resource_id"), resource_id):
                continue
            if severity and not _eq(a.get("severity"), severity):
                continue
            if alert_type and not _eq(a.get("alert_type"), alert_type):
                continue
            if alert_id and not _eq(a.get("alert_id"), alert_id):
                continue
            if dt_from or dt_to:
                ts = _parse_iso(a.get("timestamp"))
                if dt_from and (not ts or ts < dt_from):
                    continue
                if dt_to and (not ts or ts > dt_to):
                    continue
            out.append(a)

        out.sort(key=lambda r: ((r.get("timestamp") or ""), (r.get("alert_id") or "")))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_siem_alerts",
                "description": "List SIEM alerts with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "severity": {
                            "type": "string",
                            "description": "CRITICAL, HIGH, MEDIUM, LOW",
                        },
                        "alert_type": {"type": "string"},
                        "alert_id": {
                            "type": "string",
                            "description": "Specific alert ID to filter by",
                        },
                        "date_from": {
                            "type": "string",
                            "description": "ISO 8601 lower bound",
                        },
                        "date_to": {
                            "type": "string",
                            "description": "ISO 8601 upper bound",
                        },
                    },
                    "required": [],
                },
            },
        }


class AcknowledgeSiemAlertTool(Tool):
    """acknowledge_siem_alert
    Writes to data['siem_acknowledgments'] with: alert_id, ack_by, status, note, ack_at(HARD_TS)
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alert_id = kwargs.get("alert_id")
        ack_by = kwargs.get("ack_by")
        status = kwargs.get("status") or "ACKNOWLEDGED"
        note = kwargs.get("note")
        ack_at = _HARD_TS

        if not alert_id or not ack_by:
            return json.dumps({"error": "alert_id and ack_by are required"}, indent=2)

        alerts: List[Dict[str, Any]] = data.setdefault("siem_alerts", [])
        rec = next((a for a in alerts if a.get("alert_id") == alert_id), None)
        if not rec:
            return json.dumps({"error": f"Alert {alert_id} not found"}, indent=2)

        acks: List[Dict[str, Any]] = data.setdefault("siem_acknowledgments", [])
        ack = next((x for x in acks if x.get("alert_id") == alert_id), None)
        if not ack:
            ack = {"alert_id": alert_id}

        ack["ack_by"] = ack_by
        ack["status"] = status
        ack["note"] = note
        ack["ack_at"] = ack_at

        # upsert
        replaced = False
        for i, x in enumerate(acks):
            if x.get("alert_id") == alert_id:
                acks[i] = ack
                replaced = True
                break
        if not replaced:
            acks.append(ack)

        return json.dumps(ack, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "acknowledge_siem_alert",
                "description": (
                    "Record an acknowledgment for a SIEM alert in a separate store (no changes to alert record)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string"},
                        "ack_by": {
                            "type": "string",
                            "description": "User ID acknowledging",
                        },
                        "status": {
                            "type": "string",
                            "description": "ACKNOWLEDGED, CLOSED, etc.",
                        },
                        "note": {"type": "string"},
                    },
                    "required": ["alert_id", "ack_by"],
                },
            },
        }


class ListHubspotTicketsTool(Tool):
    """list_hubspot_tickets"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        category = kwargs.get("category")
        requester_id = kwargs.get("requester_id")
        date_from = kwargs.get("date_from")
        date_to = kwargs.get("date_to")

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        tickets: List[Dict[str, Any]] = data.get("hubspot_tickets", [])
        ticket_id = kwargs.get("ticket_id")
        out: List[Dict[str, Any]] = []
        for t in tickets:
            if ticket_id and not _eq(t.get("ticket_id"), ticket_id):
                continue
            if status and not _eq(t.get("status"), status):
                continue
            if category and not _eq(t.get("category"), category):
                continue
            if requester_id and not _eq(t.get("requester_id"), requester_id):
                continue
            if dt_from or dt_to:
                ts = _parse_iso(t.get("created_at"))
                if dt_from and (not ts or ts < dt_from):
                    continue
                if dt_to and (not ts or ts > dt_to):
                    continue
            out.append(t)

        out.sort(
            key=lambda r: ((r.get("created_at") or ""), (r.get("ticket_id") or ""))
        )
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_hubspot_tickets",
                "description": "List HubSpot tickets with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "status": {"type": "string"},
                        "category": {"type": "string"},
                        "requester_id": {"type": "string"},
                        "date_from": {
                            "type": "string",
                            "description": "ISO 8601 lower bound",
                        },
                        "date_to": {
                            "type": "string",
                            "description": "ISO 8601 upper bound",
                        },
                    },
                    "required": [],
                },
            },
        }


class UpdateHubspotTicketTool(Tool):
    """update_hubspot_ticket
    Updates ticket fields; sets updated_at deterministically and closed_at when status == CLOSED.
    If actor_id is provided, also writes an idempotent audit log (like review_access_request) and
    returns it under 'audit_log' in the response.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get("ticket_id")
        if not ticket_id:
            return json.dumps({"error": "ticket_id is required"}, indent=2)

        updatable_fields = {
            "subject": kwargs.get("subject"),
            "description": kwargs.get("description"),
            "status": kwargs.get("status"),
            "priority": kwargs.get("priority"),
            "assignee_id": kwargs.get("assignee_id"),
            "requester_id": kwargs.get("requester_id"),
            "category": kwargs.get("category"),
        }

        tickets: List[Dict[str, Any]] = data.setdefault("hubspot_tickets", [])
        t = next((x for x in tickets if x.get("ticket_id") == ticket_id), None)
        if not t:
            return json.dumps({"error": f"Ticket {ticket_id} not found"}, indent=2)

        # Track changed fields for audit details
        changed_fields: List[str] = []
        for k, v in updatable_fields.items():
            if v is not None and t.get(k) != v:
                t[k] = v
                changed_fields.append(k)

        if changed_fields:
            t["updated_at"] = _HARD_TS

        if t.get("status") == "CLOSED":
            t["closed_at"] = _HARD_TS

        actor_id = kwargs.get("actor_id")
        note = kwargs.get("note")
        audit_entry = None
        if actor_id:
            logs = data.setdefault("audit_logs", [])
            log_id = f"LOG-{ticket_id}-update"

            parts = []
            if changed_fields:
                parts.append(f"updated: {', '.join(sorted(changed_fields))}")
            if t.get("status") == "CLOSED":
                parts.append("closed")
            if note:
                parts.append(f"note: {note}")
            details = (
                f"Ticket {ticket_id} " + "; ".join(parts)
                if parts
                else f"Ticket {ticket_id} no changes"
            )

            audit_entry = {
                "log_id": log_id,
                "actor_id": actor_id,
                "action_type": "HUBSPOT_TICKET_UPDATED",
                "target_id": ticket_id,
                "timestamp": _HARD_TS,
                "details": details,
            }
            existing = next((l for l in logs if l.get("log_id") == log_id), None)
            if existing:
                existing.update(audit_entry)
            else:
                logs.append(audit_entry)

        out = dict(t)
        if audit_entry:
            out["audit_log"] = audit_entry
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_hubspot_ticket",
                "description": (
                    "Update HubSpot ticket fields; sets updated_at deterministically and closed_at when status == CLOSED. "
                    "If actor_id is provided, also records an idempotent audit log and returns it as 'audit_log'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "description": {"type": "string"},
                        "status": {"type": "string"},
                        "priority": {"type": "string"},
                        "assignee_id": {"type": "string"},
                        "requester_id": {"type": "string"},
                        "category": {"type": "string"},
                        "actor_id": {
                            "type": "string",
                            "description": (
                                "User ID recording the update for audit (e.g., U-005)."
                            ),
                        },
                        "note": {
                            "type": "string",
                            "description": "Optional note to include in the audit log.",
                        },
                    },
                    "required": ["ticket_id"],
                },
            },
        }


class ListSlackMessagesTool(Tool):
    """list_slack_messages"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        channel = kwargs.get("channel")
        date_from = kwargs.get("date_from")
        date_to = kwargs.get("date_to")

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        msgs: List[Dict[str, Any]] = data.get("slack_messages", [])
        out: List[Dict[str, Any]] = []
        for m in msgs:
            if channel and not _eq(m.get("channel"), channel):
                continue
            if dt_from or dt_to:
                ts = _parse_iso(m.get("timestamp"))
                if dt_from and (not ts or ts < dt_from):
                    continue
                if dt_to and (not ts or ts > dt_to):
                    continue
            out.append(m)

        out.sort(
            key=lambda r: ((r.get("timestamp") or ""), (r.get("message_id") or ""))
        )
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_slack_messages",
                "description": (
                    "List Slack messages with optional channel and time filters."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "e.g., #access-requests",
                        },
                        "date_from": {
                            "type": "string",
                            "description": "ISO 8601 lower bound",
                        },
                        "date_to": {
                            "type": "string",
                            "description": "ISO 8601 upper bound",
                        },
                    },
                    "required": [],
                },
            },
        }


class ListUsersByMfaTool(Tool):
    """list_users_by_mfa"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        enabled = kwargs.get("enabled")
        status = kwargs.get("status")

        users: List[Dict[str, Any]] = data.get("users", [])
        out: List[Dict[str, Any]] = []

        def _effective_enabled_and_source(
            u: Dict[str, Any],
        ) -> Tuple[Optional[bool], str]:
            mfa = u.get("mfa")
            if isinstance(mfa, dict) and "enabled" in mfa:
                return bool(mfa.get("enabled")), "new"
            if "mfa_enabled" in u:
                return bool(u.get("mfa_enabled")), "legacy"
            return None, "unknown"

        for u in users:
            if status and not _eq(u.get("status"), status):
                continue

            eff, source = _effective_enabled_and_source(u)
            if enabled is not None:
                if eff is None or bool(eff) != bool(enabled):
                    continue

            rec = dict(u)
            rec.setdefault("mfa", {})
            rec["mfa"] = dict(rec["mfa"]) if isinstance(rec["mfa"], dict) else {}
            if eff is not None:
                rec["mfa"]["enabled"] = bool(eff)
            rec["mfa"]["source"] = source
            out.append(rec)

        out.sort(key=lambda r: (r.get("user_id") or ""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_users_by_mfa",
                "description": "Find users by MFA state and optional account status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "enabled": {"type": "boolean"},
                    },
                    "required": ["enabled"],
                },
            },
        }


class SetUserMfaTool(Tool):
    """set_user_mfa
    Updates users[].mfa.enabled and users[].mfa.method; keeps legacy users[].mfa_enabled in sync.
    Idempotent: no-op if state already matches.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        enabled = kwargs.get("enabled")
        method = kwargs.get("method")

        if user_id is None or enabled is None:
            return json.dumps({"error": "user_id and enabled are required"}, indent=2)

        users: List[Dict[str, Any]] = data.setdefault("users", [])
        u = next((x for x in users if x.get("user_id") == user_id), None)
        if not u:
            return json.dumps({"error": f"User {user_id} not found"}, indent=2)

        mfa = u.get("mfa") or {}
        current_enabled = (
            bool(mfa.get("enabled")) if "enabled" in mfa else u.get("mfa_enabled")
        )

        if current_enabled == bool(enabled):
            return json.dumps(
                {
                    "user_id": user_id,
                    "mfa_enabled": bool(enabled),
                    "updated_at": _HARD_TS,
                },
                indent=2,
            )

        mfa["enabled"] = bool(enabled)
        u["mfa"] = mfa
        u["mfa_enabled"] = bool(enabled)

        return json.dumps(
            {
                "user_id": user_id,
                "mfa": {"enabled": mfa.get("enabled")},
                "mfa_enabled": u.get("mfa_enabled"),
                "updated_at": _HARD_TS,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_user_mfa",
                "description": (
                    "Update a user's MFA state and method; idempotent and back-compatible."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "enabled": {"type": "boolean"},
                    },
                    "required": ["user_id", "enabled"],
                },
            },
        }


class UpsertEmailTool(Tool):
    """upsert_email
    Create or update an email record deterministically with exclusive fields only.
    - Create when email_id not present; sets timestamp to HARD_TS.
    - Update when email_id exists; modifies only provided fields (no updated_at).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email_id = kwargs.get("email_id")
        if not email_id:
            return json.dumps({"error": "email_id is required"}, indent=2)

        emails: List[Dict[str, Any]] = data.setdefault("emails", [])
        rec = next((e for e in emails if e.get("email_id") == email_id), None)

        sender = kwargs.get("sender")
        receiver = kwargs.get("receiver")
        subject = kwargs.get("subject")
        text_content = kwargs.get("text_content")

        if rec is None:
            if not receiver or not subject or not text_content:
                return json.dumps(
                    {
                        "error": (
                            "receiver, subject, and text_content are required for creation"
                        )
                    },
                    indent=2,
                )
            rec = {
                "email_id": email_id,
                "timestamp": _HARD_TS,
                "sender": sender or "rbac-bot@taucorp.com",
                "receiver": receiver,
                "subject": subject,
                "text_content": text_content,
            }
            emails.append(rec)
            return json.dumps(rec, indent=2)

        # UPDATE (exclusive fields only)
        if sender is not None:
            rec["sender"] = sender
        if receiver is not None:
            rec["receiver"] = receiver
        if subject is not None:
            rec["subject"] = subject
        if text_content is not None:
            rec["text_content"] = text_content

        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_email",
                "description": (
                    "Create or update an email record deterministically (exclusive fields only)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email_id": {"type": "string"},
                        "sender": {"type": "string"},
                        "receiver": {"type": "string"},
                        "subject": {"type": "string"},
                        "text_content": {"type": "string"},
                    },
                    "required": ["email_id"],
                },
            },
        }


class ReviewPolicyExceptionTool(Tool):
    """review_policy_exception
    Deterministically approve or reject a policy exception record by ID. Mirrors the behaviour of ReviewAccessRequestTool.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exception_id = kwargs.get("exception_id")
        reviewer_id = kwargs.get("reviewer_id")
        approve = kwargs.get("approve")
        notes = kwargs.get("notes")

        exceptions = data.get("policy_exceptions", [])
        for pe in exceptions:
            if pe.get("exception_id") == exception_id:
                pe["status"] = "APPROVED" if approve else "DENIED"
                pe["reviewed_by"] = reviewer_id
                pe["reviewed_on"] = _HARD_TS
                if notes:
                    pe["decision_notes"] = notes
                # audit
                logs = data.setdefault("audit_logs", [])
                log_id = f"LOG-{exception_id}-decision"
                audit_entry = {
                    "log_id": log_id,
                    "actor_id": reviewer_id,
                    "action_type": "review_policy_exception",
                    "target_id": exception_id,
                    "timestamp": _HARD_TS,
                    "details": pe["status"],
                }
                existing = next((l for l in logs if l.get("log_id") == log_id), None)
                if existing:
                    existing.update(audit_entry)
                else:
                    logs.append(audit_entry)
                out = dict(pe)
                out["audit_log"] = audit_entry
                return json.dumps(out, indent=2)
        return json.dumps(
            {"error": f"Policy exception {exception_id} not found"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "review_policy_exception",
                "description": (
                    "Approve or reject a policy exception by ID with reviewer notes."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "approve": {"type": "boolean"},
                        "notes": {"type": "string"},
                    },
                    "required": ["exception_id", "reviewer_id", "approve"],
                },
            },
        }


class ProcessAccessRequestE2ETool(Tool):
    """
    process_access_request_e2e
    End-to-end processing of an access request:
      - Evaluate policy (duplicate, admin-like, coverage, certifications, exceptions)
      - Record decision with audit log
      - If approved, assign role idempotently
      - Return decision, notes, roles and active sessions for the requester, and audit log id
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        reviewer_id = kwargs.get("reviewer_id")
        if not request_id or not reviewer_id:
            return json.dumps(
                {"error": "request_id and reviewer_id are required"}, indent=2
            )

        # Evaluate policy using existing logic
        decision_raw = json.loads(
            CheckUserStatusTool.invoke(data, request_id=request_id)
        )
        if "error" in decision_raw:
            return json.dumps(decision_raw, indent=2)

        approve = bool(decision_raw.get("approve"))
        notes = decision_raw.get("notes")

        # Record decision with audit log
        reviewed_raw = json.loads(
            ReviewAccessRequestTool.invoke(
                data,
                request_id=request_id,
                reviewer_id=reviewer_id,
                approve=approve,
                notes=notes,
            )
        )
        if "error" in reviewed_raw:
            return json.dumps(reviewed_raw, indent=2)

        # If approved, assign role idempotently
        assignment_info = None
        if approve:
            assignment_info = json.loads(
                AssignRoleOnApprovalTool.invoke(
                    data, request_id=request_id, assigned_by=reviewer_id
                )
            )

        # Collect final requester state
        req = next(
            (
                r
                for r in data.get("access_requests", [])
                if r.get("request_id") == request_id
            ),
            None,
        )
        user_id = req.get("user_id") if req else None

        roles_after = [
            ur.get("role_id")
            for ur in data.get("user_roles", [])
            if user_id and ur.get("user_id") == user_id and not ur.get("expires_on")
        ]
        sessions_after = [
            s
            for s in data.get("sessions", [])
            if user_id and s.get("user_id") == user_id and not s.get("end_time")
        ]

        out = {
            "request_id": request_id,
            "user_id": user_id,
            "decision": "APPROVED" if approve else "REJECTED",
            "notes": notes,
            "roles": roles_after,
            "sessions": sessions_after,
            "audit_log_id": f"LOG-{request_id}-decision",
        }
        if assignment_info and isinstance(assignment_info, dict):
            out["assignment"] = assignment_info
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_access_request_e2e",
                "description": (
                    "End-to-end processing of an access request with audit and optional assignment."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                    },
                    "required": ["request_id", "reviewer_id"],
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        role_id = kwargs.get("role_id")
        revoked_by = kwargs.get("revoked_by")
        if not user_id or not role_id or not revoked_by:
            return json.dumps(
                {"error": "user_id, role_id, revoked_by are required"}, indent=2
            )

        revoke_res = json.loads(
            RevokeUserRoleTool.invoke(
                data, user_id=user_id, role_id=role_id, revoked_by=revoked_by
            )
        )

        # Ensure audit entry (deterministic id)
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


class CloseHubspotTicketBasicTool(Tool):
    """
    close_hubspot_ticket_basic
    Assign a ticket to actor, set priority to LOW, set status to CLOSED, and return audit log id.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get("ticket_id")
        actor_id = kwargs.get("actor_id")
        if not ticket_id or not actor_id:
            return json.dumps(
                {"error": "ticket_id and actor_id are required"}, indent=2
            )

        updated = json.loads(
            UpdateHubspotTicketTool.invoke(
                data,
                ticket_id=ticket_id,
                assignee_id=actor_id,
                priority="LOW",
                status="CLOSED",
                actor_id=actor_id,
                note="auto-close",
            )
        )

        out = {
            "ticket_id": ticket_id,
            "status": updated.get("status"),
            "assignee_id": updated.get("assignee_id"),
            "priority": updated.get("priority"),
            "audit_log_id": f"LOG-{ticket_id}-update",
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "close_hubspot_ticket_basic",
                "description": "Assign and close a HubSpot ticket with audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "actor_id": {"type": "string"},
                    },
                    "required": ["ticket_id", "actor_id"],
                },
            },
        }


class CompleteCertificationsAndAuditTool(Tool):
    """
    complete_certifications_and_audit
    Complete all IN_PROGRESS certifications and write a single audit log.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_id = kwargs.get("log_id") or "LOG-CERT-CLOSE"
        actor_id = kwargs.get("actor_id")
        target_id = kwargs.get("target_id") or "CERT:ALL"
        details = kwargs.get("details") or "Certifications completed."
        if not actor_id:
            return json.dumps({"error": "actor_id is required"}, indent=2)

        completed: List[str] = []
        for cert in data.get("certifications", []):
            if cert.get("status") == "IN_PROGRESS":
                cert["status"] = "COMPLETED"
                cert["completed_on"] = _HARD_TS
                completed.append(cert.get("certification_id"))

        audit = json.loads(
            AppendAuditLogTool.invoke(
                data,
                log_id=log_id,
                access_request=log_id,
                actor_id=actor_id,
                action_type="certification_close",
                target_id=target_id,
                timestamp=_HARD_TS,
                details=details,
            )
        )

        return json.dumps(
            {
                "completed_ids": completed,
                "audit_log_id": audit.get("log_id"),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_certifications_and_audit",
                "description": (
                    "Complete all IN_PROGRESS certifications and write a single audit log."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {"type": "string"},
                        "actor_id": {"type": "string"},
                        "target_id": {"type": "string"},
                        "details": {"type": "string"},
                    },
                    "required": ["actor_id"],
                },
            },
        }


class CreateAndReviewAccessRequestTool(Tool):
    """
    create_and_review_access_request
    Create an access request and immediately review it per policy (with audit). If approved, assign role.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        user_id = kwargs.get("user_id")
        resource_id = kwargs.get("resource_id")
        requested_role_id = kwargs.get("requested_role_id")
        justification = kwargs.get("justification") or ""
        reviewer_id = kwargs.get("reviewer_id")

        missing = [
            k
            for k in [
                "request_id",
                "user_id",
                "resource_id",
                "requested_role_id",
                "reviewer_id",
            ]
            if not kwargs.get(k)
        ]
        if missing:
            return json.dumps(
                {"error": f"Missing required: {', '.join(missing)}"}, indent=2
            )

        # Create if absent
        json.loads(
            CreateAccessRequestTool.invoke(
                data,
                request_id=request_id,
                user_id=user_id,
                resource_id=resource_id,
                requested_role_id=requested_role_id,
                justification=justification,
                submitted_at=_HARD_TS,
            )
        )

        # Process end-to-end using existing composite
        return ProcessAccessRequestE2ETool.invoke(
            data, request_id=request_id, reviewer_id=reviewer_id
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_and_review_access_request",
                "description": (
                    "Create an access request and process it end-to-end per policy."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "requested_role_id": {"type": "string"},
                        "justification": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                    },
                    "required": [
                        "request_id",
                        "user_id",
                        "resource_id",
                        "requested_role_id",
                        "reviewer_id",
                    ],
                },
            },
        }


TOOLS = [
    GetAccessRequestTool(),
    GetAccessRequestDetailsTool(),
    UpdateAccessRequestStatusTool(),
    ReviewAccessRequestTool(),
    CheckUserStatusTool(),
    GetUserRolesTool(),
    GrantRoleTool(),
    RevokeUserRoleTool(),
    RevokeRoleTool(),
    ListAuditLogsTool(),
    ListActiveSessionsTool(),
    GetUserSessionsTool(),
    CreateAccessRequestTool(),
    ListAccessRequestsByStatusTool(),
    ListAccessRequestsByUserTool(),
    AssignRoleOnApprovalTool(),
    AssignUserRoleTool(),
    ListRolePermissionsTool(),
    GetRolePermissionsAliasTool(),
    GetRoleNameTool(),
    AppendAuditLogTool(),
    CompleteCertificationTool(),
    StartCertificationTool(),
    ListCertificationsByStatusTool(),
    GetPermissionsForUserTool(),
    ListPolicyExceptionsTool(),
    ReviewPolicyExceptionTool(),
    GetTimeWindowTool(),
    ListEmailsTool(),
    SendEmailTool(),
    GetCurrentTimeTool(),
    GetUserEmailTool(),
    ListSiemAlertsTool(),
    AcknowledgeSiemAlertTool(),
    ListHubspotTicketsTool(),
    UpdateHubspotTicketTool(),
    CloseHubspotTicketBasicTool(),
    UpdateHubspotTicketStatusTool(),
    UpdateHubspotTicketAssigneeTool(),
    GetHubspotTicketsByRequesterTool(),
    GetHubspotTicketsByAssigneeTool(),
    ListSlackMessagesTool(),
    ListUsersByMfaTool(),
    SetUserMfaTool(),
    UpsertEmailTool(),
    LogRevokeDecisionTool(),
]
