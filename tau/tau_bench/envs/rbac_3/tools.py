import json
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool

_HARD_TS = "2024-06-26 16:05:00+00:00"




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


def _eq(a: str | None, b: str | None) -> bool:
    pass
    return (a or "") == (b or "")


def _parse_iso(ts: str | None) -> datetime | None:
    """Strong ISO8601 parsing: accommodates 'Z' and offsets; yields None if absent."""
    pass
    if not ts:
        return None
    ts = ts.replace("Z", "+00:00")
    return datetime.fromisoformat(ts)


class GetAccessRequestTool(Tool):
    """Retrieve a single access request entry using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None) -> str:
        if not request_id:
            payload = {"error": "request_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        requests: list[dict[str, Any]] = data.get("access_requests", [])
        rec = next((r for r in requests if r.get("request_id") == request_id), None)
        if rec is None:
            payload = {"error": f"Access request {request_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #standardize structure and ensure reliable defaults
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccessRequest",
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
    """Authorize or deny an access request with reviewer comments (deterministic decision_at + returns audit data)."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, reviewer_id: str = None, approve: bool = None, notes: str = None) -> str:
        requests = data.get("access_requests", [])
        for req in requests:
            if req.get("request_id") == request_id:
                req["status"] = "APPROVED" if approve else "REJECTED"
                req["reviewed_by"] = reviewer_id
                req["decision_notes"] = notes
                req["decision_at"] = _HARD_TS
                # Idempotent audit record to prevent downstream lists/filters from appearing
                # clear out
                logs = data.setdefault("audit_logs", [])
                log_id = f"LOG-{request_id}-decision"
                audit_entry = {
                    "log_id": log_id,
                    "actor_id": reviewer_id,
                    "action_type": "ReviewAccessRequest",
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
                # Include subject and body as specified
                status = req["status"]
                out["subject"] = f"{request_id} {status}"
                out["body"] = f"{reviewer_id} {_HARD_TS}"
                payload = out
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Access request {request_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReviewAccessRequest",
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
    """Get all roles assigned to a specific user (echo user_id for chaining)."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        roles: list[str] = []
        assignments = data.get("user_roles", [])
        for assignment in assignments:
            if assignment.get("user_id") == user_id and not assignment.get(
                "expires_on"
            ):
                roles.append(assignment.get("role_id"))
        payload = {"user_id": user_id, "roles": roles}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRoles",
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
    Revoke a user's role (compliant with specifications).
    - Parameters: user_id, role_id, revoked_by
    - Functionality: delete the corresponding user_roles entry if it exists; if you prefer a soft-revoke for consistency,
      set expires_on to the assignment's assigned_on.
    - Result: {"removed": true/false}
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None, revoked_by: str = None) -> str:
        assignments = data.get("user_roles", [])
        removed = False

        kept: list[dict[str, Any]] = []
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

        # Set up information for the audit log
        action_details = "REMOVED" if removed else "NOOP"
        log_info = {
            "log_id": f"LOG-{user_id}-{role_id}-revoke",
            "actor_id": revoked_by,
            "action_type": "RevokeRole",
            "target_id": f"{user_id}:{role_id}",
            "timestamp": _HARD_TS,
            "details": action_details,
        }
        payload = {
            "removed": bool(removed),
            "user_id": user_id,
            "role_id": role_id,
            "log_info": log_info,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revokeUserRole",
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
    """Display audit logs with optional filters: action_type, user_id (actor_id), target_id, date range.
    Backward-compatible alias: filter_by == action_type.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action_type: str = None,
        user_id: str = None,
        target_id: str = None,
        date_from: str = None,
        date_to: str = None,
        filter_by: str = None,
        actor_id: str = None
    ) -> str:
        # Support filter_by as alias for action_type, actor_id as alias for user_id
        action_type = action_type or filter_by
        user_id = user_id or actor_id
        user_id = user_id
        target_id = target_id
        date_from = date_from
        date_to = date_to

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAuditLogs",
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
    """Provide sessions where end_time == null (active sessions). Optional user_id filter. Echo user_id for chaining."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, param1: str = None, param2: str = None) -> str:
        # Support param1 as alias for user_id
        user_id = user_id or param1
        sessions = data.get("sessions", [])
        active = [s for s in sessions if not s.get("end_time")]
        if user_id:
            active = [s for s in active if s.get("user_id") == user_id]
        payload = {"user_id": user_id, "sessions": active}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listActiveSessions",
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
    """CreateAccessRequest"""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        request_id: str,
        user_id: str,
        resource_id: str,
        requested_role_id: str,
        justification: str
,
    submitted_at: Any = None,
    ) -> str:
        req = {
            "request_id": request_id,
            "user_id": user_id,
            "resource_id": resource_id,
            "role": requested_role_id,
            "requested_role_id": requested_role_id,
            "justification": justification,
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAccessRequest",
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
    """ListAccessRequestsByStatus"""

    @staticmethod
    def invoke(data: dict[str, Any], status: str) -> str:
        out = [r for r in data.get("access_requests", []) if r.get("status") == status]
        out = sorted(
            out, key=lambda r: (r.get("submitted_at") or "", r.get("request_id") or "")
        )
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAccessRequestsByStatus",
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
    """ListAccessRequestsByUser"""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        out = [
            r for r in data.get("access_requests", []) if r.get("user_id") == user_id
        ]
        out = sorted(
            out, key=lambda r: (r.get("submitted_at") or "", r.get("request_id") or "")
        )
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAccessRequestsByUser",
                "description": "Filter access_requests by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class AssignUserRoleTool(Tool):
    """AssignUserRole"""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_role_id: str,
        user_id: str,
        role_id: str,
        assigned_by: str,
        expires_on: str = None,
        assigned_on: str = None
    ) -> str:
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
        payload = record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignUserRole",
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
    def invoke(data: dict[str, Any], role_id: str = None, param1: str = None, param2: str = None) -> str:
        # Support both role_id and param1 (alias)
        role_id = role_id or param1
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRolePermissions",
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
    Find a role using role_id and return its role_name and metadata.
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        if not role_id:
            payload = {"error": "role_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        roles: list[dict[str, Any]] = data.get("roles", [])
        rec = next((r for r in roles if r.get("role_id") == role_id), None)
        if not rec:
            payload = {"error": f"Role {role_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        out = {
            "role_id": rec.get("role_id"),
            "role_name": rec.get("role_name"),
            "description": rec.get("description"),
            "is_temporary": rec.get("is_temporary"),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRoleName",
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
    """AppendAuditLog"""

    @staticmethod
    def invoke(data: dict[str, Any], access_request: str = None, actor_id: str = None, action_type: str = None, target_id: str = None, log_id: str = None, details: str = "",
    timestamp: Any = None
    ) -> str:
        # Create log_id if it hasn't been supplied
        if log_id is None:
            log_id = f"LOG-{access_request or 'unknown'}-decision"

        entry = {
            "log_id": log_id,
            "actor_id": actor_id,
            "action_type": action_type,
            "target_id": target_id,
            "timestamp": _HARD_TS,
            "details": details,
        }
        logs = data.setdefault("audit_logs", [])
        existing = next((l for l in logs if l.get("log_id") == entry["log_id"]), None)
        if existing is None:
            logs.append(entry)
            out = entry
        else:
            out = existing
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendAuditLog",
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
    Solely log revoke decisions using a deterministic log_id and timestamp.
    - log_id format: LOG-<user_id>-<role_id>-decision
    - action_type: revoke_role
    - target_id: <user_id>:<role_id>
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None, actor_id: str = None, details: str = None, revoked: bool = None) -> str:
        if not user_id or not role_id:
            payload = {"error": "user_id and role_id are required"}
            out = json.dumps(payload, indent=2)
            return out

        log_id = f"LOG-{user_id}-{role_id}-decision"
        # Extract default information if not specifically given
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
            "action_type": "RevokeRole",
            "target_id": f"{user_id}:{role_id}",
            "timestamp": _HARD_TS,
            "details": details,
        }

        logs: list[dict[str, Any]] = data.setdefault("audit_logs", [])
        existing = next((l for l in logs if l.get("log_id") == log_id), None)
        if existing:
            existing.update(entry)
            out = existing
        else:
            logs.append(entry)
            out = entry
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogRevokeDecision",
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
    """GetAccessRequest_details: enhanced alias for retrieving AR details."""

    @staticmethod
    def invoke(data: dict[str, Any],
    request_id: Any = None,
    ) -> str:
        return GetAccessRequestTool.invoke(data)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccessRequestDetails",
                "description": "Return detailed access request info by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"request_id": {"type": "string"}},
                    "required": ["request_id"],
                },
            },
        }


class UpdateAccessRequestStatusTool(Tool):
    """update_access_request_status: authorize/deny with comments and audit."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        status: str = None, 
        request_id: str = None, 
        reviewer_id: str = None, 
        approve: bool = None, 
        notes: str = None,
        decision_at: str = None
    ) -> str:
        # allow for either approval/notes or a clear status
        if status is not None and approve is None:
            approve = True if str(status).upper() == "APPROVED" else False
        return ReviewAccessRequestTool.invoke(
            data,
            request_id=request_id,
            reviewer_id=reviewer_id,
            approve=approve,
            notes=notes,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAccessRequestStatus",
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
    """grant_role: allocate a role either via request_id or directly using user_id/role_id."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        request_id: str = None,
        assigned_by: str = None,
        user_role_id: str = None,
        user_id: str = None,
        role_id: str = None,
        expires_on: str = None
    ) -> str:
        if request_id:
            return AssignRoleOnApprovalTool.invoke(
                data, request_id=request_id, assigned_by=assigned_by
            )
        #straightforward
        return AssignUserRoleTool.invoke(
            data,
            user_role_id=user_role_id,
            user_id=user_id,
            role_id=role_id,
            assigned_by=assigned_by,
            expires_on=expires_on,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GrantRole",
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
    """revoke_role: rescind a role and create a deterministic audit log."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None, actor_id: str = None, revoked_by: str = None) -> str:
        actor_id = actor_id or revoked_by
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


class SendEmailTool(Tool):
    """send_email: convenient wrapper around upsert for creation purposes only."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        email_id: str = None, 
        receiver: str = None, 
        user_id: str = None, 
        subject: str = None, 
        text_content: str = None, 
        sender: str = None
    ) -> str:
        if not email_id or not subject or not text_content:
            payload = {"error": "email_id, subject, and text_content are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # If the receiver is not specified, attempt to determine it from user_id
        if not receiver and user_id:
            users: list[dict[str, Any]] = data.get("users", [])
            user = next((u for u in users if u.get("user_id") == user_id), None)
            if not user or not user.get("email"):
                payload = {"error": f"Could not resolve email for user_id {user_id}"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            receiver = user.get("email")

        if not receiver:
            payload = {"error": "receiver or user_id must be provided"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        return UpsertEmailTool.invoke(
            data,
            email_id=email_id,
            receiver=receiver,
            subject=subject,
            text_content=text_content,
            sender=sender,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
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
    """get_user_sessions: alias for listing active sessions of a user."""

    @staticmethod
    def invoke(data: dict[str, Any], param1: Any = None, param2: Any = None, user_id: str = None) -> str:
        # Support user_id as alias for param1
        param1 = param1 or user_id
        return ListActiveSessionsTool.invoke(data, param1=param1, param2=param2)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserSessions",
                "description": "Return active sessions for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class UpdateHubspotTicketStatusTool(Tool):
    """update_hubspot_ticket_status: adjust status with audit."""

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, status: str = None, actor_id: str = None,
        note: Any = None,
        closed_at: Any = None,
        description: Any = None,
    ) -> str:
        pass
        return UpdateHubspotTicketTool.invoke(
            data,
            ticket_id=ticket_id,
            status=status,
            actor_id=actor_id,
        )
        
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateHubspotTicketStatus",
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
    """update_hubspot_ticket_assignee: assign assignee with audit."""

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, assignee_id: str = None, actor_id: str = None, note: Any = None) -> str:
        pass
        return UpdateHubspotTicketTool.invoke(
            data,
            ticket_id=ticket_id,
            assignee_id=assignee_id,
            actor_id=actor_id,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateHubspotTicketAssignee",
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
    """get_current_time: provides a consistent timestamp utilized across writes."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"timestamp": _HARD_TS}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCurrentTime",
                "description": "Return deterministic current time used for writes.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class GetUsersByRoleTool(Tool):
    """get_users_by_role: enumerate user_ids with an assigned role (active only)."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        result = [
            ur.get("user_id")
            for ur in data.get("user_roles", [])
            if ur.get("role_id") == role_id and not ur.get("expires_on")
        ]
        payload = {"role_id": role_id, "user_ids": sorted(result)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUsersByRole",
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
    def invoke(data: dict[str, Any], param1: Any = None, param2: Any = None,
    role_id: Any = None,
    ) -> str:
        pass
        return ListRolePermissionsTool.invoke(data, param1=param1, param2=param2)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRolePermissions",
                "description": "Return permissions for a role.",
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }


class GetHubspotTicketsByRequesterTool(Tool):
    """get_hubspot_tickets_by_requester: filter tickets based on requester."""

    @staticmethod
    def invoke(data: dict[str, Any], requester_id: str = None, role_id: Any = None) -> str:
        return ListHubspotTicketsTool.invoke(
            data, requester_id=requester_id
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getHubspotTicketsByRequester",
                "description": "List HubSpot tickets for a requester.",
                "parameters": {
                    "type": "object",
                    "properties": {"requester_id": {"type": "string"}},
                    "required": ["requester_id"],
                },
            },
        }


class GetHubspotTicketsByAssigneeTool(Tool):
    """get_hubspot_tickets_by_assignee: filter tickets based on assignee."""

    @staticmethod
    def invoke(data: dict[str, Any], assignee_id: str = None) -> str:
        pass
        #utilize the list tool again with a post-filter
        tickets = json.loads(ListHubspotTicketsTool.invoke(data))
        payload = [t for t in tickets if t.get("assignee_id") == assignee_id]
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getHubspotTicketsByAssignee",
                "description": "List HubSpot tickets for an assignee.",
                "parameters": {
                    "type": "object",
                    "properties": {"assignee_id": {"type": "string"}},
                    "required": ["assignee_id"],
                },
            },
        }


class CompleteCertificationTool(Tool):
    """CompleteCertification"""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str, reviewer_id: str = None, completed_on: Any = None) -> str:
        cert_id = certification_id
        reviewer_id = reviewer_id

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
        payload = c
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompleteCertification",
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
    """StartCertification"""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str, reviewer_id: str = None) -> str:
        cert_id = certification_id
        reviewer_id = reviewer_id
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
        payload = c
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StartCertification",
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
    """ListCertificationsByStatus"""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None, certification_id: str = None) -> str:
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListCertificationsByStatus",
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
    """GetPermissionsForUser"""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        roles_active = [
            r.get("role_id")
            for r in data.get("user_roles", [])
            if r.get("user_id") == user_id and not r.get("expires_on")
        ]
        role_perms = data.get("role_permissions", [])
        perms = data.get("permissions", [])
        perm_map = {p.get("permission_id"): p for p in perms}
        seen = set()
        result: list[dict[str, Any]] = []
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
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermissionsForUser",
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
    Database-driven gate: returns a literal boolean `approve` along with literals necessary for subsequent actions.

    Policy (derived from database state):
      1) Request must have status='PENDING'
      2) If the requested role is ALREADY assigned to the user -> approve=False, notes='Already assigned.'
      3) Admin-like roles are dynamically derived from the database:
         - any role whose role_name ends with '-lead' (e.g., engineering-lead, operations-lead, ...), OR
         - any role whose role_name contains '-admin' (e.g., hr-payroll-admin, finance-budget-admin, ...).
      4) Exception: ROL-032 (finance-budget-admin) may be approved if the user already has ROL-029 (finance-base).
      5) Verify resource coverage: requested role must provide permissions on the target resource
      6) Verify certification requirements for the target resource
      7) Check for active policy exceptions
      8) Otherwise -> approve=True.
    All decisions utilize the actual request record and current assignments in `data`.
    """

    @staticmethod
    def _admin_like_roles(data: dict[str, Any]) -> set:
        pass
        roles = data.get("roles", [])
        admin_like = set()
        for r in roles:
            name = (r.get("role_name") or "").lower()
            rid = r.get("role_id")
            if not rid or not name:
                continue
            #Leadership positions: strict suffix '-lead' (prevents
            #'sales-lead-manager' false positive)
            if name.endswith("-lead"):
                admin_like.add(rid)
            #Administrative positions: any that include '-admin'
            if "-admin" in name:
                admin_like.add(rid)
        return admin_like

    @staticmethod
    def _check_resource_coverage(
        data: dict[str, Any], role_id: str, resource_id: str
    ) -> bool:
        """Verify if the role provides any permissions on the target resource."""
        pass
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
        data: dict[str, Any], user_id: str, resource_id: str | None
    ) -> tuple:
        """Verify certification requirements for a resource. Returns (has_requirements, all_completed, reviewer_id)."""
        pass
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
        data: dict[str, Any],
        user_id: str,
        role_id: str | None,
        role_permissions_resource_ids: list[str],
    ) -> tuple:
        """Verify certifications either linked to role_id (if available) or implied through the role's resources. Returns (has_requirements, all_completed, reviewer_id)."""
        pass
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
    def _reviewer_authorized(data: dict[str, Any], reviewer_id: str | None) -> bool:
        pass
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
        data: dict[str, Any], user_id: str, role_id: str, resource_id: str
    ) -> bool:
        """Verify for active policy exceptions concerning the user/permission combination."""
        pass
        #Retrieve permissions for the specified role
        role_permissions = [
            rp.get("permission_id")
            for rp in data.get("role_permissions", [])
            if rp.get("role_id") == role_id
        ]

        #Verify if the user has current policy exceptions for any of these permissions
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
    @staticmethod
    def invoke(
        data: dict[str, Any],
        mode: str = None,
        user_id: str = None,
        role_id: str = None,
        resource_id: str = None,
        request_id: str = None,
        reviewer_id: str = None
    ) -> str:
        mode = (mode or "access_request").lower()

        # Branch: evaluation of revocation
        if mode in ("revoke", "revoke_evaluation"):
            if not user_id or not role_id:
                payload = {"error": "user_id and role_id are required for revoke evaluation"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            # Confirm that the assignment is present
            active_assignment = any(
                ur.get("user_id") == user_id
                and ur.get("role_id") == role_id
                and not ur.get("expires_on")
                for ur in data.get("user_roles", [])
            )
            if not active_assignment:
                payload = {
                    "user_id": user_id,
                    "role_id": role_id,
                    "revoke": False,
                    "notes": "Already assigned." if False else "Role not assigned.",
                    "details": "NOOP",
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            # Identify resource IDs for role permissions
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

            # Check resource coverage (if resource_id is given)
            if resource_id and not CheckUserStatusTool._check_resource_coverage(
                data, role_id, resource_id
            ):
                payload = {
                    "user_id": user_id,
                    "role_id": role_id,
                    "revoke": True,
                    "notes": "Requested role does not cover target resource.",
                    "details": "REVOKE_RESOURCE_MISMATCH",
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            # Requirements for certification
            has_req, all_completed, _ = (
                CheckUserStatusTool._check_certifications_for_role(
                    data, user_id, role_id, perm_resource_ids
                )
            )
            if has_req and not all_completed:
                payload = {
                    "user_id": user_id,
                    "role_id": role_id,
                    "revoke": True,
                    "notes": "Required certification not completed.",
                    "details": "REVOKE_CERT_INCOMPLETE",
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            # Roles similar to admin may be suitable for right-sizing
            if role_id in CheckUserStatusTool._admin_like_roles(data):
                payload = {
                    "user_id": user_id,
                    "role_id": role_id,
                    "revoke": True,
                    "notes": "Admin-like role blocked by policy.",
                    "details": "REVOKE_ADMINLIKE",
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            payload = {
                "user_id": user_id,
                "role_id": role_id,
                "revoke": False,
                "notes": "Within clearance and least-privilege.",
                "details": "NO_REVOKE",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Default branch: decision on access request
        if not request_id:
            payload = {"error": "request_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        req = next(
            (
                r
                for r in data.get("access_requests", [])
                if r.get("request_id") == request_id
            ),
            None,
        )
        if not req:
            payload = {"error": f"Access request {request_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # First verify the status of the request (Rule 1)
        if req.get("status") != "PENDING":
            payload = {
                "error": (
                    f"Access request {request_id} is not PENDING (status: {req.get('status')})"
                )
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Authorization from reviewer (if available)
        if reviewer_id and not CheckUserStatusTool._reviewer_authorized(
            data, reviewer_id
        ):
            payload = {
                "error": (
                    f"Reviewer {reviewer_id} not authorized (lead role required)."
                )
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        user_id = req.get("user_id")
        role_id = req.get("role") or req.get("requested_role_id")
        resource_id = req.get("resource_id")
        req.get("submitted_at")

        # Roles currently from the database
        current_roles = [
            ur.get("role_id")
            for ur in data.get("user_roles", [])
            if ur.get("user_id") == user_id and not ur.get("expires_on")
        ]

        # Rule 2: request duplication
        if role_id in current_roles:
            approve = False
            notes = "Already assigned."
        else:
            # Initially verify resource coverage (Rule 5)
            if not CheckUserStatusTool._check_resource_coverage(
                data, role_id, resource_id
            ):
                approve = False
                notes = "Requested role does not cover target resource."
            else:
                admin_like_block = CheckUserStatusTool._admin_like_roles(data)

                # Rule 4 (positioned before the general admin-like block): ROL-032 prerequisite
                if role_id == "ROL-032":
                    approve = "ROL-029" in current_roles
                    notes = (
                        "Met prerequisite finance-base (ROL-029)."
                        if approve
                        else "Missing prerequisite finance-base (ROL-029)."
                    )
                # Rule 3: dynamic block resembling admin
                elif role_id in admin_like_block:
                    approve = False
                    notes = "Admin-like role blocked by policy."
                else:
                    # Rule 6: Verify certification requirements
                    has_cert_reqs, all_certs_completed, cert_reviewer_id = (
                        CheckUserStatusTool._check_certifications(
                            data, user_id, resource_id
                        )
                    )

                    if has_cert_reqs and not all_certs_completed:
                        approve = False
                        notes = "Required certification not completed."
                    else:
                        # Rule 7: Verify policy exceptions
                        has_policy_exception = (
                            CheckUserStatusTool._check_policy_exceptions(
                                data, user_id, role_id, resource_id
                            )
                        )

                        if has_policy_exception:
                            approve = True
                            notes = "Policy exception approved."
                        else:
                            # Rule 8: Standard approval with relevant notes
                            approve = True
                            if has_cert_reqs and all_certs_completed:
                                notes = "Certification verified; within clearance and least-privilege."
                            else:
                                notes = "Within clearance and least-privilege."

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckUserStatus",
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
    Idempotently allocate the role from an approved access request and ALWAYS
    return a user_role_id. Additionally, repairs existing assignments lacking user_role_id.
    """

    @staticmethod
    def _derive_user_role_id(request_id: str, user_id: str, role_id: str) -> str:
        pass
        #Consistent and predictable; maintains brevity if only digits are desired
        import re

        digits = "".join(re.findall(r"\d+", request_id)) or "000"
        return f"UR-{digits}"

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, assigned_by: str = None, provided_urid: str = None) -> str:
        import json as _json

        if not request_id or not assigned_by:
            return _json.dumps(
                {"error": "request_id and assigned_by are required"}, indent=2
            )

        # Find the access request
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

        assignments: list[dict[str, Any]] = data.setdefault("user_roles", [])

        # Attempt to locate an active existing assignment
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
            # Repair any missing user_role_id if needed
            if "user_role_id" not in existing or not existing["user_role_id"]:
                existing["user_role_id"] = (
                    provided_urid
                    or AssignRoleOnApprovalTool._derive_user_role_id(
                        request_id, user_id, role_id
                    )
                )
            # Confirm that necessary fields are included
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

        # Establish a completely new assignment
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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignRoleOnApproval",
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

    Enumerates policy exception records with optional filters:
      - user_id:       filter for a specific user
      - permission_id: filter for a specific permission
      - status:        filter by exception status (e.g., APPROVED, DENIED, EXPIRED, PENDING)
      - requested_on_from / requested_on_to: inclusive ISO-8601 bounds on requested_on
      - active_only:   if True, return solely non-denied/non-expired records

    Results are sorted by requested_on, then exception_id for consistency.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        permission_id: str = None,
        status: str = None,
        active_only: bool = False,
        requested_on_from: str = None,
        requested_on_to: str = None,
        date_from: str = None,
        date_to: str = None
    ) -> str:
        pass
        # Accommodate both specific and general names for date filters (matching with
        # other utilities)
        date_from = requested_on_from or date_from
        date_to = requested_on_to or date_to

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        exceptions: list[dict[str, Any]] = data.get("policy_exceptions", [])
        out: list[dict[str, Any]] = []

        for rec in exceptions:
            if user_id and not _eq(rec.get("user_id"), user_id):
                continue
            if permission_id and not _eq(rec.get("permission_id"), permission_id):
                continue
            if status and not _eq(rec.get("status"), status):
                continue
            if active_only and (rec.get("status") in ("DENIED", "EXPIRED")):
                continue

            # Date filter based on requested_on
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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPolicyExceptions",
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
    returns {"date_from": <ts>, "date_to": <ts + delta>} (both ISO-8601, maintaining offset).
    If only negative values are supplied, date_to will be the original ts and date_from will be ts + delta.
    """

    @staticmethod
    def _parse_iso(ts: str) -> datetime:
        pass
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))

    @staticmethod
    def _parse_offset(s: str | None, unit: str) -> float:
        pass
        if not s:
            return 0.0
        s = s.strip().lower()
        assert s.endswith(unit), f"Offset must end with '{unit}'"
        return float(s[:-1])

    @staticmethod
    def invoke(data: dict[str, Any], timestamp: str = None, days: float = None, hours: float = None) -> str:
        pass
        import json

        ts = timestamp
        if not ts:
            payload = {"error": "timestamp is required"}
            out = json.dumps(payload, indent=2)
            return out

        base = GetTimeWindowTool._parse_iso(ts)
        d = GetTimeWindowTool._parse_offset(days, "d") if days else 0.0
        h = GetTimeWindowTool._parse_offset(hours, "h") if hours else 0.0
        delta = timedelta(days=d, hours=h)

        # Ascertain the direction of the window
        if d < 0 or h < 0:
            start, end = base + delta, base
        else:
            start, end = base, base + delta

        # Maintain the precise "+00:00" format if included in the input
        def fmt(dt: datetime) -> str:
            pass
            s = dt.isoformat()
            if s.endswith("+00:00"):
                return s
            if s[-6] in ["+", "-"] and s[-3] == ":":
                return s
            return s

        out = {"date_from": fmt(start), "date_to": fmt(end)}
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTimeWindow",
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
    """GetUserEmail"""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        users: list[dict[str, Any]] = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        out = {
            "user_id": user.get("user_id"),
            "username": user.get("username"),
            "email": user.get("email"),
            "status": user.get("status"),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserEmail",
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
    """ListEmails"""

    @staticmethod
    def invoke(data: dict[str, Any], receiver: str = None, email_id: str = None, date_from: str = None, date_to: str = None) -> str:
        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        emails: list[dict[str, Any]] = data.get("emails", [])
        out: list[dict[str, Any]] = []

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListEmails",
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
    """ListSiemAlerts"""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        resource_id: str = None,
        severity: str = None,
        alert_type: str = None,
        alert_id: str = None,
        date_from: str = None,
        date_to: str = None
,
    severity_in: Any = None,
    ) -> str:
        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        alerts: list[dict[str, Any]] = data.get("siem_alerts", [])
        out: list[dict[str, Any]] = []
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSiemAlerts",
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
    Records in data['siem_acknowledgments'] with: alert_id, ack_by, status, note, ack_at(HARD_TS)
    """

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str = None, ack_by: str = None, status: str = "ACKNOWLEDGED", note: str = None, severity_in: Any = None) -> str:
        pass
        ack_at = _HARD_TS

        if not alert_id or not ack_by:
            payload = {"error": "alert_id and ack_by are required"}
            out = json.dumps(payload, indent=2)
            return out

        alerts: list[dict[str, Any]] = data.setdefault("siem_alerts", [])
        rec = next((a for a in alerts if a.get("alert_id") == alert_id), None)
        if not rec:
            payload = {"error": f"Alert {alert_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        acks: list[dict[str, Any]] = data.setdefault("siem_acknowledgments", [])
        ack = next((x for x in acks if x.get("alert_id") == alert_id), None)
        if not ack:
            ack = {"alert_id": alert_id}

        ack["ack_by"] = ack_by
        ack["status"] = status
        ack["note"] = note
        ack["ack_at"] = ack_at

        #insert or update
        replaced = False
        for i, x in enumerate(acks):
            if x.get("alert_id") == alert_id:
                acks[i] = ack
                replaced = True
                break
        if not replaced:
            acks.append(ack)
        payload = ack
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AcknowledgeSiemAlert",
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
    """ListHubspotTickets"""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        status: str = None,
        category: str = None,
        requester_id: str = None,
        date_from: str = None,
        date_to: str = None,
        ticket_id: str = None
    ) -> str:
        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        tickets: list[dict[str, Any]] = data.get("hubspot_tickets", [])
        out: list[dict[str, Any]] = []
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListHubspotTickets",
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
    Modifies ticket fields; deterministically sets updated_at and closed_at when status == CLOSED.
    If actor_id is supplied, also logs an idempotent audit (similar to review_access_request) and
    returns it under 'audit_log' in the response.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        ticket_id: str = None,
        subject: str = None,
        description: str = None,
        status: str = None,
        priority: str = None,
        assignee_id: str = None,
        requester_id: str = None,
        category: str = None,
        actor_id: str = None,
        note: str = None
    ) -> str:
        pass
        if not ticket_id:
            payload = {"error": "ticket_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        updatable_fields = {
            "subject": subject,
            "description": description,
            "status": status,
            "priority": priority,
            "assignee_id": assignee_id,
            "requester_id": requester_id,
            "category": category,
        }

        tickets: list[dict[str, Any]] = data.setdefault("hubspot_tickets", [])
        t = next((x for x in tickets if x.get("ticket_id") == ticket_id), None)
        if not t:
            payload = {"error": f"Ticket {ticket_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        # Monitor modified fields for audit information
        changed_fields: list[str] = []
        for k, v in updatable_fields.items():
            if v is not None and t.get(k) != v:
                t[k] = v
                changed_fields.append(k)

        if changed_fields:
            t["updated_at"] = _HARD_TS

        if t.get("status") == "CLOSED":
            t["closed_at"] = _HARD_TS

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateHubspotTicket",
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
    def invoke(data: dict[str, Any], channel: str = None, date_from: str = None, date_to: str = None) -> str:
        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        msgs: list[dict[str, Any]] = data.get("slack_messages", [])
        out: list[dict[str, Any]] = []
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listSlackMessages",
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
    """ListUsersByMfa"""

    @staticmethod
    def invoke(data: dict[str, Any], enabled: bool = None, status: str = None,
    user_id: Any = None,
    ) -> str:
        users: list[dict[str, Any]] = data.get("users", [])
        out: list[dict[str, Any]] = []

        def _effective_enabled_and_source(
            u: dict[str, Any],
        ) -> tuple[bool | None, str]:
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListUsersByMfa",
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
    Modifies users[].mfa.enabled and users[].mfa.method; synchronizes legacy users[].mfa_enabled.
    Idempotent: does nothing if the state already aligns.
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, enabled: bool = None, method: Any = None) -> str:
        if user_id is None or enabled is None:
            payload = {"error": "user_id and enabled are required"}
            out = json.dumps(payload, indent=2)
            return out

        users: list[dict[str, Any]] = data.setdefault("users", [])
        u = next((x for x in users if x.get("user_id") == user_id), None)
        if not u:
            payload = {"error": f"User {user_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        mfa = u.get("mfa") or {}
        current_enabled = (
            bool(mfa.get("enabled")) if "enabled" in mfa else u.get("mfa_enabled")
        )

        if current_enabled == bool(enabled):
            payload = {
                    "user_id": user_id,
                    "mfa_enabled": bool(enabled),
                    "updated_at": _HARD_TS,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        mfa["enabled"] = bool(enabled)
        u["mfa"] = mfa
        u["mfa_enabled"] = bool(enabled)
        payload = {
                "user_id": user_id,
                "mfa": {"enabled": mfa.get("enabled")},
                "mfa_enabled": u.get("mfa_enabled"),
                "updated_at": _HARD_TS,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetUserMfa",
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
    Create or update an email record in a deterministic manner with only exclusive fields.
    - Create when email_id is absent; sets timestamp to HARD_TS.
    - Update when email_id is present; alters only specified fields (no updated_at).
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        email_id: str = None,
        sender: str = None,
        receiver: str = None,
        subject: str = None,
        text_content: str = None
    ) -> str:
        if not email_id:
            payload = {"error": "email_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        emails: list[dict[str, Any]] = data.setdefault("emails", [])
        rec = next((e for e in emails if e.get("email_id") == email_id), None)

        if rec is None:
            if not receiver or not subject or not text_content:
                payload = {
                    "error": (
                        "receiver, subject, and text_content are required for creation"
                    )
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            rec = {
                "email_id": email_id,
                "timestamp": _HARD_TS,
                "sender": sender or "rbac-bot@sigmatech.com",
                "receiver": receiver,
                "subject": subject,
                "text_content": text_content,
            }
            emails.append(rec)
            payload = rec
            out = json.dumps(payload, indent=2)
            return out

        # UPDATE (only exclusive fields)
        if sender is not None:
            rec["sender"] = sender
        if receiver is not None:
            rec["receiver"] = receiver
        if subject is not None:
            rec["subject"] = subject
        if text_content is not None:
            rec["text_content"] = text_content
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsertEmail",
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
    Deterministically authorize or deny a policy exception record by ID. Reflects the behavior of ReviewAccessRequestTool.
    """

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None, reviewer_id: str = None, approve: bool = None, notes: str = None) -> str:
        exceptions = data.get("policy_exceptions", [])
        for pe in exceptions:
            if pe.get("exception_id") == exception_id:
                pe["status"] = "APPROVED" if approve else "DENIED"
                pe["reviewed_by"] = reviewer_id
                pe["reviewed_on"] = _HARD_TS
                if notes:
                    pe["decision_notes"] = notes
                # examine
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
                payload = out
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Policy exception {exception_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reviewPolicyException",
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
    Comprehensive processing of an access request:
      - Assess policy (duplicate, admin-like, coverage, certifications, exceptions)
      - Document decision in the audit log
      - If granted, assign role idempotently
      - Return decision, notes, roles, active sessions for the requester, and audit log id
    """

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, reviewer_id: str = None) -> str:
        if not request_id or not reviewer_id:
            payload = {"error": "request_id and reviewer_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Assess policy based on current logic
        decision_raw = json.loads(
            CheckUserStatusTool.invoke(data, request_id=request_id)
        )
        if "error" in decision_raw:
            payload = decision_raw
            out = json.dumps(payload, indent=2)
            return out

        approve = bool(decision_raw.get("approve"))
        notes = decision_raw.get("notes")

        # Document decision in the audit log
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
            payload = reviewed_raw
            out = json.dumps(payload, indent=2)
            return out

        # If granted, assign role idempotently
        assignment_info = None
        if approve:
            assignment_info = json.loads(
                AssignRoleOnApprovalTool.invoke(
                    data, request_id=request_id, assigned_by=reviewer_id
                )
            )

        # Gather the final state of the requester
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "processAccessRequestE2e",
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


class CloseHubspotTicketBasicTool(Tool):
    """
    close_hubspot_ticket_basic
    Assign a ticket to the actor, set priority to LOW, set status to CLOSED, and return the audit log id.
    """

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, actor_id: str = None) -> str:
        if not ticket_id or not actor_id:
            payload = {"error": "ticket_id and actor_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "closeHubspotTicketBasic",
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
    Finalize all IN_PROGRESS certifications and create a single audit log.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        log_id: str = "LOG-CERT-CLOSE", 
        actor_id: str = None, 
        target_id: str = "CERT:ALL", 
        details: str = "Certifications completed."
    ) -> str:
        if not actor_id:
            payload = {"error": "actor_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        completed: list[str] = []
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
        payload = {
                "completed_ids": completed,
                "audit_log_id": audit.get("log_id"),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "completeCertificationsAndAudit",
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
    Generate an access request and promptly review it according to policy (with audit). If authorized, assign role.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        request_id: str = None,
        user_id: str = None,
        resource_id: str = None,
        requested_role_id: str = None,
        justification: str = "",
        reviewer_id: str = None
    ) -> str:
        pass
        missing = [
            k
            for k in [
                "request_id",
                "user_id",
                "resource_id",
                "requested_role_id",
                "reviewer_id",
            ]
            if not locals().get(k)
        ]
        if missing:
            payload = {"error": f"Missing required: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Establish if not present
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

        # Execute end-to-end with the current composite
        return ProcessAccessRequestE2ETool.invoke(
            data, request_id=request_id, reviewer_id=reviewer_id
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createAndReviewAccessRequest",
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
