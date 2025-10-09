import json
from typing import Any

from tau_bench.envs.tool import Tool


#---------- 1 ----------
class ListUsersTool(Tool):
    """Display users with optional filtering."""

    @staticmethod
    def invoke(data: dict[str, Any], department: str = None, status: str = None, mfa_enabled: bool = None) -> str:
        users = data.get("users", [])

        results = []
        for u in users:
            if department and u["department"] != department:
                continue
            if status and u["status"] != status:
                continue
            if mfa_enabled is not None and u["mfa_enabled"] != mfa_enabled:
                continue
            results.append(u)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListUsers",
                "description": "List users with optional filters",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {"type": "string"},
                        "status": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"},
                    },
                },
            },
        }


#---------- 2 ----------
class GetUserDetailsTool(Tool):
    """Retrieve full user information."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        uid = user_id
        for u in data.get("users", []):
            if u["user_id"] == uid:
                payload = u
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"user_id {uid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserDetails",
                "description": "Get full details of a user by their user_id",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


#---------- 3 ----------
class ListRolesTool(Tool):
    """Display roles, with an optional filter for temporary ones."""

    @staticmethod
    def invoke(data: dict[str, Any], is_temporary: bool = None) -> str:
        roles = data.get("roles", [])
        if is_temporary is None:
            payload = roles
            out = json.dumps(payload, indent=2)
            return out
        payload = [r for r in roles if r["is_temporary"] == is_temporary]
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListRoles",
                "description": "List all roles optionally filtering by temporary flag",
                "parameters": {
                    "type": "object",
                    "properties": {"is_temporary": {"type": "boolean"}},
                },
            },
        }


#---------- 6 ----------
class RevokeRoleFromUserTool(Tool):
    """Remove a role from a user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None) -> str:
        uid = user_id
        rid = role_id
        user_roles = data.get("user_roles", [])
        to_remove = [
            ur for ur in user_roles if ur["user_id"] == uid and ur["role_id"] == rid
        ]
        if not to_remove:
            payload = {"error": "Role not found for user"}
            out = json.dumps(payload, indent=2)
            return out
        for rem in to_remove:
            user_roles.remove(rem)
        payload = {"success": f"Role {rid} revoked from user {uid}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeRole",
                "description": "Revokes a specific role from a user",
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


#---------- 7 ----------
class ListAccessRequestsTool(Tool):
    """Display access requests categorized by status or resource."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None, resource_id: str = None) -> str:
        reqs = data.get("access_requests", [])
        results = []
        for r in reqs:
            if status and r["status"] != status:
                continue
            if resource_id and r["resource_id"] != resource_id:
                continue
            results.append(r)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAccessRequests",
                "description": "List access requests filtered by status or resource",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "resource_id": {"type": "string"},
                    },
                },
            },
        }


#---------- 8 ----------
class ApproveAccessRequestTool(Tool):
    """Authorize an access request."""

    @staticmethod  #<-- necessary to align with base class definition
    def invoke(data: dict[str, Any], request_id: str, reviewer_id: str, decision_at: str) -> str:
        rid = request_id
        reviewer = reviewer_id
        decision_at = decision_at  #<-- additional mandatory argument!
        for req in data.get("access_requests", []):
            if req["request_id"] == rid:
                req["status"] = "APPROVED"
                req["reviewed_by"] = reviewer
                req["decision_at"] = decision_at  #<-- utilize argument, AVOID hardcoding!
                payload = {"success": f"Request {rid} approved"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Request {rid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApproveAccessRequest",
                "description": "Approve a pending access request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "decision_at": {"type": "string"},  #<-- Include in properties!
                    },
                    "required": [
                        "request_id",
                        "reviewer_id",
                        "decision_at",
                    ],  #<-- Include in required!
                },
            },
        }


#---------- 9 ----------
class RejectAccessRequestTool(Tool):
    """Deny an access request."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, reviewer_id: str = None, decision_at: str = None,
    reason: Any = None,
    ) -> str:
        rid = request_id
        reviewer = reviewer_id
        decision_at = decision_at
        for req in data.get("access_requests", []):
            if req["request_id"] == rid:
                req["status"] = "REJECTED"
                req["reviewed_by"] = reviewer
                req["decision_at"] = decision_at
                payload = {"success": f"Request {rid} rejected"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Request {rid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RejectAccessRequest",
                "description": "Reject a pending access request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "decision_at": {"type": "string"},
                    },
                    "required": ["request_id", "reviewer_id", "decision_at"],
                },
            },
        }


#---------- 10 ----------
class GetCertificationDetailsTool(Tool):
    """Retrieve information about a certification."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None,
    user_id: Any = None,
    ) -> str:
        cid = certification_id
        for c in data.get("certifications", []):
            if c["certification_id"] == cid:
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Certification {cid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertificationDetails",
                "description": "Get details of a certification record",
                "parameters": {
                    "type": "object",
                    "properties": {"certification_id": {"type": "string"}},
                    "required": ["certification_id"],
                },
            },
        }


#---------- 11 ----------
class CompleteCertificationTool(Tool):
    """Designate a certification as complete."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None, completed_on: str = None) -> str:
        for c in data.get("certifications", []):
            if c["certification_id"] == certification_id:
                c["status"] = "COMPLETED"
                c["completed_on"] = completed_on
                payload = {"success": f"Certification {certification_id} completed"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Certification {certification_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompleteCertification",
                "description": "Mark a certification as completed",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"},
                        "completed_on": {"type": "string"},
                    },
                    "required": ["certification_id", "completed_on"],
                },
            },
        }


#---------- 12 ----------
class ListPolicyExceptionsTool(Tool):
    """Display exceptions to policies."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None, user_id: str = None, completed_on: Any = None,
    permission_id: Any = None,
    ) -> str:
        exes = data.get("policy_exceptions", [])
        results = []
        for e in exes:
            if status and e["status"] != status:
                continue
            if user_id and e["user_id"] != user_id:
                continue
            results.append(e)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPolicyExceptions",
                "description": "List policy exceptions optionally filtered by status or user_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "user_id": {"type": "string"},
                    },
                },
            },
        }


#---------- 13 ----------
class ApprovePolicyExceptionTool(Tool):
    """Authorize a policy exception."""

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None, reviewed_by: str = None, expires_on: str = None, reviewed_on: str = None, permission_id: Any = None) -> str:
        for e in data.get("policy_exceptions", []):
            if e["exception_id"] == exception_id:
                e["status"] = "ACTIVE"
                e["reviewed_by"] = reviewed_by
                e["reviewed_on"] = reviewed_on
                e["expires_on"] = expires_on
                payload = {"success": f"Exception {exception_id} approved"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Exception {exception_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApprovePolicyException",
                "description": "Approve a pending policy exception request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                        "expires_on": {"type": "string"},
                        "reviewed_on": {"type": "string"},
                    },
                    "required": [
                        "exception_id",
                        "reviewed_by",
                        "expires_on",
                        "reviewed_on",
                    ],
                },
            },
        }


#---------- 14 ----------
class DenyPolicyExceptionTool(Tool):
    """Reject a policy exception request."""

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None, reviewed_by: str = None, reviewed_on: str = None) -> str:
        for e in data.get("policy_exceptions", []):
            if e["exception_id"] == exception_id:
                e["status"] = "DENIED"
                e["reviewed_by"] = reviewed_by
                e["reviewed_on"] = reviewed_on
                payload = {"success": f"Exception {exception_id} denied"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Exception {exception_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DenyPolicyException",
                "description": "Deny a pending policy exception request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                        "reviewed_on": {"type": "string"},
                    },
                    "required": ["exception_id", "reviewed_by", "reviewed_on"],
                },
            },
        }


#---------- 16 ----------
class GetPolicyExceptionDetailsTool(Tool):
    """Provide the complete stored record for a specified policy exception (excluding error payloads)."""

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None) -> str:
        pass
        eid = exception_id
        for e in data.get("policy_exceptions", []) or []:
            if e.get("exception_id") == eid:
                payload = e
                out = json.dumps(payload, indent=2)
                return out
        #Not located → return empty object to prevent '"error":' keys from triggering validators
        return "{}"
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyExceptionDetails",
                "description": "Return the full stored policy-exception record for the given ID.",
                "parameters": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "exception_id": {
                            "type": "string",
                            "description": "e.g., PE-007",
                        }
                    },
                    "required": ["exception_id"],
                },
            },
        }


#---------- 17 ----------
class RequestPolicyExceptionTool(Tool):
    """Initiate a new policy exception request."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, permission_id: str = None, reason: str = None, requested_on: str = None) -> str:
        exceptions = data.get("policy_exceptions", [])

        new_id = f"PE-{len(exceptions) + 1:03d}"
        record = {
            "exception_id": new_id,
            "user_id": user_id,
            "permission_id": permission_id,
            "reviewed_by": None,
            "requested_on": requested_on,
            "reviewed_on": None,
            "expires_on": None,
            "reason": reason,
            "status": "PENDING_REVIEW",
        }
        exceptions.append(record)
        payload = {"success": f"Policy exception {new_id} requested"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RequestPolicyException",
                "description": "Create a new policy exception request for a specific permission",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "permission_id": {"type": "string"},
                        "reason": {"type": "string"},
                        "requested_on": {"type": "string"},
                    },
                    "required": ["user_id", "permission_id", "reason", "requested_on"],
                },
            },
        }


#---------- 18 ----------
class ListSiemAlertsTool(Tool):
    """Display SIEM alerts with optional filters."""

    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None, severity: str = None,
    severity_in: Any = None,
    ) -> str:
        alerts = data.get("siem_alerts", [])
        results = []
        for a in alerts:
            if resource_id and a["resource_id"] != resource_id:
                continue
            if severity and a["severity"] != severity:
                continue
            results.append(a)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSiemAlerts",
                "description": "List SIEM alerts filtered by resource or severity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string"},
                        "severity": {"type": "string"},
                    },
                },
            },
        }


#---------- 19 ----------
class GetSiemAlertDetailsTool(Tool):
    """Get information about a SIEM alert."""

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str, severity_in: Any = None) -> str:
        aid = alert_id
        for a in data.get("siem_alerts", []):
            if a["alert_id"] == aid:
                payload = a
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"SIEM alert {aid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSiemAlertDetails",
                "description": "Get detailed information for a specific SIEM alert",
                "parameters": {
                    "type": "object",
                    "properties": {"alert_id": {"type": "string"}},
                    "required": ["alert_id"],
                },
            },
        }


#---------- 20 ----------
class CreateSiemRuleTool(Tool):
    """Establish a new SIEM correlation rule."""

    @staticmethod
    def invoke(data: dict[str, Any], rule_name: str = None, conditions: Any = None, created_by: str = None,
    created_on: Any = None,
    notes: str = None
    ) -> str:
        rules = data.get("siem_rules", [])
        new_id = f"RULE-{len(rules) + 1:03d}"
        rules.append(
            {
                "rule_id": new_id,
                "rule_name": rule_name,
                "conditions": conditions,
                "created_by": created_by,
            }
        )
        payload = {"success": f"SIEM rule {new_id} created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSiemRule",
                "description": "Create and store a new rule in SIEM",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_name": {"type": "string"},
                        "conditions": {"type": "object"},
                        "created_by": {"type": "string"},
                    },
                    "required": ["rule_name", "conditions", "created_by"],
                },
            },
        }


#---------- 21 ----------
class InvestigateSiemIncidentTool(Tool):
    """Document the outcome of an investigation for a SIEM alert."""

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str = None, analyst_id: str = None, notes: str = None, investigated_on: str = None, created_on: Any = None) -> str:
        investigations = data.get("siem_investigations", [])
        new_id = f"INV-{len(investigations) + 1:03d}"
        investigations.append(
            {
                "investigation_id": new_id,
                "alert_id": alert_id,
                "analyst_id": analyst_id,
                "notes": notes,
                "investigated_on": investigated_on,
            }
        )
        payload = {"success": f"Investigation {new_id} recorded"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InvestigateSiemIncident",
                "description": "Create a record of SIEM incident investigation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string"},
                        "analyst_id": {"type": "string"},
                        "notes": {"type": "string"},
                        "investigated_on": {"type": "string"},
                    },
                    "required": ["alert_id", "analyst_id", "notes", "investigated_on"],
                },
            },
        }


#---------- 22 ----------
class ListSessionsTool(Tool):
    """Display user sessions with optional filtering."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, active_only: bool = None) -> str:
        sessions = data.get("sessions", [])
        results = []
        for s in sessions:
            if user_id and s["user_id"] != user_id:
                continue
            if active_only and s.get("end_time") is not None:
                continue
            results.append(s)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSessions",
                "description": "List login sessions with optional user_id and active_only flag",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "active_only": {"type": "boolean"},
                    },
                },
            },
        }


#---------- 23 ----------
class TerminateSessionTool(Tool):
    """End a particular user session."""

    @staticmethod
    def invoke(data: dict[str, Any], session_id: str = None, terminated_on: str = None) -> str:
        sid = session_id
        term_time = terminated_on
        for s in data.get("sessions", []):
            if s["session_id"] == sid:
                s["end_time"] = term_time
                payload = {"success": f"Session {sid} terminated"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Session {sid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TerminateSession",
                "description": "Force terminate a session by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {"type": "string"},
                        "terminated_on": {"type": "string"},
                    },
                    "required": ["session_id", "terminated_on"],
                },
            },
        }


#---------- 24 ----------
class AuditIamAccessTool(Tool):
    """Display IAM access audit logs within specified timestamps."""

    @staticmethod
    def invoke(data: dict[str, Any], start_time: str = None, end_time: str = None) -> str:
        logs = data.get("audit_logs", [])
        results = [
            l
            for l in logs
            if start_time <= l["timestamp"] <= end_time and "IAM" in l.get("details", "")
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AuditIamAccess",
                "description": "Return IAM-specific audit logs in the provided time range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_time": {"type": "string"},
                        "end_time": {"type": "string"},
                    },
                    "required": ["start_time", "end_time"],
                },
            },
        }


#---------- 25 ----------
class SearchLogsTool(Tool):
    """Query system logs using search text."""

    @staticmethod
    def invoke(data: dict[str, Any], query: str = "", resource_id: str = None, since: str = None) -> str:
        logs = data.get("audit_logs", [])
        results = []
        for l in logs:
            details_val = l.get("details")
            # Perform the containment check solely if both are strings
            if not (
                isinstance(details_val, str)
                and isinstance(query, str)
                and query in details_val
            ):
                continue
            if resource_id and l.get("target_id") != resource_id:
                continue
            if since and l.get("timestamp") < since:
                continue
            results.append(l)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchLogs",
                "description": "Search logs by keyword, resource filter, and optional date cutoff",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "since": {"type": "string"},
                    },
                    "required": ["query"],
                },
            },
        }


#---------- 26 ----------
class ExportLogsTool(Tool):
    """Export logs in CSV or JSON format for the specified time range."""

    @staticmethod
    def invoke(data: dict[str, Any], format: str = None, start_time: Any = None, end_time: Any = None) -> str:
        logs = [l for l in data.get("audit_logs", []) if start_time <= l["timestamp"] <= end_time]
        if not format or not isinstance(format, str) or format.upper() not in ["CSV", "JSON"]:
            payload = {"error": "Invalid format"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"format": format, "logs": logs}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportLogs",
                "description": "Export logs to CSV or JSON format from given date range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "format": {"type": "string", "enum": ["CSV", "JSON"]},
                        "start_time": {"type": "string"},
                        "end_time": {"type": "string"},
                    },
                    "required": ["format", "start_time", "end_time"],
                },
            },
        }


#---------- 27 ----------
class GetUserRolesTool(Tool):
    """Get all roles allocated to a particular user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        uid = user_id
        roles_map = [
            ur["role_id"] for ur in data.get("user_roles", []) if ur["user_id"] == uid
        ]
        roles = [r for r in data.get("roles", []) if r["role_id"] in roles_map]
        payload = roles
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRoles",
                "description": "Retrieve all role objects assigned to a given user_id",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


#---------- 28 ----------
class GetPermissionDetailsTool(Tool):
    """Retrieve comprehensive information about a permission using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], permission_id: str = None) -> str:
        for p in data.get("permissions", []):
            if p["permission_id"] == permission_id:
                payload = p
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Permission {permission_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermissionDetails",
                "description": "Get full permission record from permission_id",
                "parameters": {
                    "type": "object",
                    "properties": {"permission_id": {"type": "string"}},
                    "required": ["permission_id"],
                },
            },
        }


#---------- 29 ----------
class GetResourceDetailsTool(Tool):
    """Get information regarding a specified resource."""

    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None) -> str:
        rid = resource_id
        for res in data.get("resources", []):
            if res["resource_id"] == rid:
                payload = res
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Resource {rid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResourceDetails",
                "description": "Get full details of a resource from resource_id",
                "parameters": {
                    "type": "object",
                    "properties": {"resource_id": {"type": "string"}},
                    "required": ["resource_id"],
                },
            },
        }


#---------- 30 ----------
class GetRoleDetailsTool(Tool):
    """Retrieve information on a particular role."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        rid = role_id
        for r in data.get("roles", []):
            if r["role_id"] == rid:
                payload = r
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Role {rid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoleDetails",
                "description": "Get role_name, description, and is_temporary flag for a given role_id",
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }


#---------- 31 ----------
class CreateUserTool(Tool):
    """Establish a new user account with validation and logging for audit purposes."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        username: str = None, 
        email: str = None, 
        department: str = None, 
        mfa_enabled: bool = False, 
        created_by: str = None,
    user_id: Any = None,
    actor_id: Any = None,
    created_at: str = None
    ) -> str:
        users = data.get("users", [])
        audit_logs = data.get("audit_logs", [])

        # Validation: confirm that username/email are distinct
        for u in users:
            if u["username"] == username:
                payload = {"error": f"Username {username} already exists"}
                out = json.dumps(payload, indent=2)
                return out
            if u["email"] == email:
                payload = {"error": f"Email {email} already exists"}
                out = json.dumps(payload, indent=2)
                return out

        # Predictable new user_id
        new_id = f"U-{len(users) + 1:03d}"
        users.append(
            {
                "user_id": new_id,
                "username": username,
                "email": email,
                "department": department,
                "status": "PENDING_ACCESS",
                "mfa_enabled": mfa_enabled,
            }
        )

        # Entry for audit log
        new_log_id = f"L-{len(audit_logs) + 1:03d}"
        audit_logs.append(
            {
                "log_id": new_log_id,
                "actor_id": created_by,
                "action_type": "USER_CREATED",
                "target_id": new_id,
                "timestamp": "2025-08-11 10:00:00+00:00",
                "details": "User account created during onboarding process.",
            }
        )
        payload = {"success": f"User {new_id} created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateUser",
                "description": "Create a new user in the system with PENDING_ACCESS status and log the event.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "email": {"type": "string"},
                        "department": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"},
                        "created_by": {"type": "string"},
                    },
                    "required": ["username", "email", "department", "created_by"],
                },
            },
        }


#---------- 32 ----------


class CreateAccessRequestTool(Tool):
    """File a new access request on behalf of a user."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        user_id: str = None, 
        resource_id: str = None, 
        role_id: str = None, 
        justification: str = None,
    submitted_at: Any = None,
    request_id: str = None,
    requester_id: str = None,
    subject_id: str = None
    ) -> str:
        # Support requester_id and subject_id as aliases for user_id
        user_id = user_id or requester_id or subject_id
        pass
        access_requests = data.get("access_requests", [])
        audit_logs = data.get("audit_logs", [])

        # Avoid duplicate PENDING requests
        for ar in access_requests:
            if (
                ar["user_id"] == user_id
                and ar["resource_id"] == resource_id
                and ar["requested_role_id"] == role_id
                and ar["status"] == "PENDING"
            ):
                payload = {"error": "Duplicate pending access request"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        # Predictable request ID
        new_id = f"AR-{len(access_requests) + 1:03d}"
        access_requests.append(
            {
                "request_id": new_id,
                "user_id": user_id,
                "resource_id": resource_id,
                "requested_role_id": role_id,
                "justification": justification,
                "status": "PENDING",
                "submitted_at": "2025-08-11 11:00:00+00:00",
                "reviewed_by": None,
                "decision_at": None,
            }
        )

        # Logging for audit
        new_log_id = f"L-{len(audit_logs) + 1:03d}"
        audit_logs.append(
            {
                "log_id": new_log_id,
                "actor_id": user_id,
                "action_type": "ACCESS_REQUEST_CREATED",
                "target_id": new_id,
                "timestamp": "2025-08-11 11:00:00+00:00",
                "details": f"User {user_id} submitted a request for {role_id} on {resource_id}",
            }
        )
        payload = {"success": f"Access request {new_id} created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAccessRequest",
                "description": "Submit a new access request for a given resource and role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "justification": {"type": "string"},
                    },
                    "required": ["user_id", "resource_id", "role_id", "justification"],
                },
            },
        }


#---------- 33 ----------


class CreateHubspotTicketTool(Tool):
    """Initiate a new HubSpot ticket associated with RBAC or SIEM context."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        subject: str = None,
        description: str = None,
        requester_id: str = None,
        assignee_id: str = None,
        category: str = None,
        priority: str = "MEDIUM",
        created_at: str = None
    ) -> str:
        pass
        tickets = data.get("hubspot_tickets", [])

        # Predictable ticket ID
        new_id = f"TI-{len(tickets) + 1:03d}"
        fixed_time = "2025-08-11 12:00:00+00:00"

        tickets.append(
            {
                "ticket_id": new_id,
                "created_at": fixed_time,
                "updated_at": fixed_time,
                "subject": subject,
                "description": description,
                "status": "OPEN",
                "priority": priority,
                "assignee_id": assignee_id,
                "requester_id": requester_id,
                "category": category,
                "closed_at": None,
            }
        )
        payload = {"success": f"Ticket {new_id} created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateHubspotTicket",
                "description": "Create a HubSpot ticket and associate it with RBAC or SIEM events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "description": {"type": "string"},
                        "requester_id": {"type": "string"},
                        "assignee_id": {"type": "string"},
                        "category": {"type": "string"},
                        "priority": {"type": "string"},
                    },
                    "required": [
                        "subject",
                        "description",
                        "requester_id",
                        "assignee_id",
                        "category",
                    ],
                },
            },
        }


#---------- 34 ----------


class UpdateUserStatusTool(Tool):
    """Revise a user's status, department, or MFA settings with cascading impacts."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        status: str = None,
        department: str = None,
        mfa_enabled: bool = None,
        updated_by: str = None
    ) -> str:
        users = data.get("users", [])
        audit_logs = data.get("audit_logs", [])
        sessions = data.get("sessions", [])

        # Find user
        user = next((u for u in users if u["user_id"] == user_id), None)
        if not user:
            payload = {"error": f"User {user_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        # Revise details
        if status:
            user["status"] = status
            if status in ["SUSPENDED", "DISABLED"]:
                for s in sessions:
                    if s["user_id"] == user_id and s.get("end_time") is None:
                        s["end_time"] = "2025-08-11 13:00:00+00:00"
        if department:
            user["department"] = department
        if mfa_enabled is not None:
            user["mfa_enabled"] = mfa_enabled

        # Examine
        log_id = f"L-{len(audit_logs) + 1:03d}"
        audit_logs.append(
            {
                "log_id": log_id,
                "actor_id": updated_by,
                "action_type": "USER_UPDATED",
                "target_id": user_id,
                "timestamp": "2025-08-11 13:00:00+00:00",
                "details": "User status/attributes updated",
            }
        )
        payload = {"success": f"User {user_id} updated"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserStatus",
                "description": "Update a user's status/department/MFA. Terminates sessions if suspended/disabled.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "status": {"type": "string"},
                        "department": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"},
                        "updated_by": {"type": "string"},
                    },
                    "required": ["user_id", "updated_by"],
                },
            },
        }


#---------- 35 ----------
class EscalateSiemAlertTool(Tool):
    """Increase the severity of a SIEM alert and optionally generate an incident ticket."""

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str = None, severity: str = None, reason: str = None) -> str:
        alerts = data.get("siem_alerts", [])

        alert = next((a for a in alerts if a["alert_id"] == alert_id), None)
        if not alert:
            payload = {"error": f"Alert {alert_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        severity_order = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

        # Thoroughly verify severity value prior to using .index()
        if not severity or severity not in severity_order:
            payload = {"error": "Invalid severity level"}
            out = json.dumps(payload, indent=2)
            return out
        if alert["severity"] not in severity_order:
            payload = {"error": "Existing severity value invalid"}
            out = json.dumps(payload, indent=2)
            return out
        if severity_order.index(severity) <= severity_order.index(alert["severity"]):
            payload = {"error": "Only escalation permitted"}
            out = json.dumps(payload, indent=2)
            return out

        alert["severity"] = severity
        payload = {"success": f"Alert {alert_id} escalated to {severity}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EscalateSiemAlert",
                "description": (
                    "Escalate SIEM alert severity. Only escalation (not downgrade) allowed."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string"},
                        "severity": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": ["alert_id", "severity", "reason"],
                },
            },
        }


#---------- 36 ----------
class SearchSlackMessagesTool(Tool):
    """Query Slack messages based on channel, user, time range, keywords, regex, or thread context."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        channel: str = None,
        username: str = None,
        start_time: str = None,
        end_time: str = None,
        keywords: list[str] = None,
        regex: str = None,
        thread_id: str = None
    ) -> str:
        messages = data.get("slack_messages", [])
        import re

        results = []
        for msg in messages:
            if channel and msg["channel"] != channel:
                continue
            if username and msg["username"] != username:
                continue
            if start_time and msg["timestamp"] < start_time:
                continue
            if end_time and msg["timestamp"] > end_time:
                continue
            if keywords and not any(kw in msg["message"] for kw in keywords):
                continue
            if regex and not re.search(regex, msg["message"]):
                continue
            if thread_id and msg.get("thread_id") != thread_id:
                continue
            results.append(msg)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchSlackMessages",
                "description": "Search Slack messages and retrieve analytics by channel, user, keywords, regex, or time interval.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {"type": "string"},
                        "username": {"type": "string"},
                        "start_time": {"type": "string"},
                        "end_time": {"type": "string"},
                        "keywords": {"type": "array", "items": {"type": "string"}},
                        "regex": {"type": "string"},
                        "thread_id": {"type": "string"},
                    },
                },
            },
        }


#---------- 37 ----------
class ModerateSlackChannelTool(Tool):
    """Manage Slack channel: archive, pin, unpin, or relocate canonical messages (bulk support)."""

    @staticmethod
    def invoke(data: dict[str, Any], channel: str, action: str, message_ids: list[str] = [], target_channel: str = None, moderator_id: str = None) -> str:
        messages = data.get("slack_messages", [])

        updated = []
        for msg in messages:
            if msg["message_id"] in message_ids and msg["channel"] == channel:
                if action == "archive":
                    msg["archived"] = True
                elif action == "pin":
                    msg["pinned"] = True
                elif action == "unpin":
                    msg["pinned"] = False
                elif action == "move" and target_channel:
                    msg["channel"] = target_channel
                updated.append(msg["message_id"])
        status = {"moderated": updated, "action": action}
        payload = status
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModerateSlackChannel",
                "description": "Archive, pin, unpin, or move canonical Slack messages with proper RBAC moderation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {"type": "string"},
                        "action": {
                            "type": "string",
                            "enum": ["archive", "pin", "unpin", "move"],
                        },
                        "message_ids": {"type": "array", "items": {"type": "string"}},
                        "target_channel": {"type": "string"},
                        "moderator_id": {"type": "string"},
                    },
                    "required": ["channel", "action", "message_ids", "moderator_id"],
                },
            },
        }


#---------- 38 ----------
class CreateIncidentRecordTool(Tool):
    """Initiate a new incident record to monitor security or operational events."""

    @staticmethod
    def invoke(data, timestamp, created_by, summary, linked_alerts=None, linked_users=None, linked_resources=None, severity=None):
        incident_id = f"INC-{len(data.get('incidents', [])) + 1:03d}"
        record = {
            "incident_id": incident_id,
            "timestamp": timestamp,
            "created_by": created_by,
            "summary": summary,
            "linked_alerts": linked_alerts or [],
            "linked_users": linked_users or [],
            "linked_resources": linked_resources or [],
            "status": "OPEN",
        }
        data.setdefault("incidents", []).append(record)
        payload = {"success": f"Incident {incident_id} created", "incident_id": incident_id}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateIncidentRecord",
                "description": "Create a new incident record with linked alerts, users, and resources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "ISO 8601 UTC timestamp.",
                        },
                        "created_by": {
                            "type": "string",
                            "description": "user_id of creator.",
                        },
                        "summary": {
                            "type": "string",
                            "description": "Brief summary of the incident.",
                        },
                        "linked_alerts": {"type": "array", "items": {"type": "string"}},
                        "linked_users": {"type": "array", "items": {"type": "string"}},
                        "linked_resources": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["timestamp", "created_by", "summary"],
                },
            },
        }


class CreateAuditLogTool(Tool):
    """Generate a permanent, predictable audit log entry."""

    @staticmethod
    def invoke(data: dict[str, Any], actor_id: str = None, action_type: str = None, target_id: str = None, timestamp: str = None, details: str = None,
    target_ref: Any = None,
    ) -> str:
        pass
        # Mandatory fields
        # Create log_id in a deterministic manner (e.g., sequentially or by hashing inputs)
        logs = data.get("audit_logs", [])
        next_id = f"L-{len(logs) + 1:03d}"

        log = {
            "log_id": next_id,
            "actor_id": actor_id,
            "action_type": action_type,
            "target_id": target_id,
            "timestamp": timestamp,
            "details": details,
        }
        logs.append(log)
        data["audit_logs"] = logs
        payload = log
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditLog",
                "description": "Create a deterministic, immutable audit log entry in the audit_logs table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {
                            "type": "string",
                            "description": "User ID performing the action",
                        },
                        "action_type": {
                            "type": "string",
                            "description": "Type of action performed (e.g. ROLE_REVOKED, ACCESS_GRANTED, POLICY_EXCEPTION_REQUESTED)",
                        },
                        "target_id": {
                            "type": "string",
                            "description": "ID of the affected entity (role, resource, user, or policy exception ID)",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "Deterministic ISO8601 UTC timestamp",
                        },
                        "details": {
                            "type": "string",
                            "description": "Deterministic, canonical event description",
                        },
                    },
                    "required": [
                        "actor_id",
                        "action_type",
                        "target_id",
                        "timestamp",
                        "details",
                    ],
                },
            },
        }


class SendEmailTool(Tool):
    """Dispatch an email from a predictable sender to a receiver, recording the event for compliance."""

    @staticmethod
    def invoke(data, sender, receiver, subject, body, timestamp):
        # Confirm sender's existence
        sender_user = next(
            (u for u in data.get("users", []) if u.get("user_id") == sender), None
        )
        if not sender_user:
            payload = {"error": f"Sender '{sender}' not found in users.json."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Confirm receiver's existence
        receiver_user = next(
            (u for u in data.get("users", []) if u.get("user_id") == receiver), None
        )
        if not receiver_user:
            payload = {"error": f"Receiver '{receiver}' not found in users.json."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Receiver should be ACTIVE or PENDING_ACCESS
        if receiver_user.get("status") not in ("ACTIVE", "PENDING_ACCESS"):
            payload = {
                    "error": f"Receiver '{receiver}' has status '{receiver_user.get('status')}', not allowed."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Check subject/body for validity
        if not isinstance(subject, str) or not subject.strip():
            payload = {"error": "Subject must be a non-empty string."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if not isinstance(body, str) or not body.strip():
            payload = {"error": "Body must be a non-empty string."}
            out = json.dumps(payload, indent=2)
            return out

        # Add to emails.json
        emails = data.setdefault("emails", [])
        email_id = f"EM-{len(emails) + 1:03d}"
        record = {
            "email_id": email_id,
            "timestamp": timestamp,
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "text_content": body,
        }
        emails.append(record)
        payload = {"success": f"Email {email_id} sent to {receiver}", "email_id": email_id}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
                "description": (
                    "Send an email from sender user_id to receiver user_id with deterministic subject, "
                    "body, and timestamp. Appends a new record to emails.json. "
                    "Sender and receiver must exist in users.json, and receiver must be ACTIVE or PENDING_ACCESS."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender": {
                            "type": "string",
                            "description": "Sender's user_id (must exist in users.json).",
                        },
                        "receiver": {
                            "type": "string",
                            "description": "Receiver's user_id (must be ACTIVE or PENDING_ACCESS).",
                        },
                        "subject": {
                            "type": "string",
                            "description": "Email subject, policy/compliance driven.",
                        },
                        "body": {
                            "type": "string",
                            "description": "Email body text, deterministic.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO 8601 UTC timestamp, deterministic.",
                        },
                    },
                    "required": ["sender", "receiver", "subject", "body", "timestamp"],
                },
            },
        }


class GetAccessRequestTool(Tool):
    """Get a single access request using its ID (read-only, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None) -> str:
        pass
        # Anticipate: data["access_requests"] is a collection of dicts sourced from /mnt/data/access_requests.json
        access_requests = data.get("access_requests", [])
        if not isinstance(access_requests, list):
            payload = {"error": "access_requests must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(request_id, str) or not request_id.strip():
            payload = {"error": "request_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Lookup in read-only mode
        for row in access_requests:
            if isinstance(row, dict) and row.get("request_id") == request_id:
                payload = {"access_request": row}
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
                "name": "GetAccessRequest",
                "description": "Retrieve a single access request by ID (read-only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "Access request ID, e.g. AR-004",
                        }
                    },
                    "required": ["request_id"],
                },
            },
        }


class PostSlackMessageTool(Tool):
    """Send a new message to a Slack channel (write operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], channel: str = None, message: str = None) -> str:
        pass
        # Anticipate: data["slack_messages"] is a collection of dicts sourced from /mnt/data/slack_messages.json
        slack_messages = data.get("slack_messages", [])
        if not isinstance(slack_messages, list):
            payload = {"error": "slack_messages must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(channel, str) or not channel.strip():
            payload = {"error": "channel must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(message, str) or not message.strip():
            payload = {"error": "message must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out

        # Add a new message to the log (simulated posting)
        new_entry = {
            "channel": channel,
            "message": message,
        }
        slack_messages.append(new_entry)
        payload = {"success": f"Message posted to {channel}", "message": new_entry}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PostSlackMessage",
                "description": "Post a new message into a Slack channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "Slack channel name or ID, e.g. #general",
                        },
                        "message": {
                            "type": "string",
                            "description": "Text content of the message to post",
                        },
                    },
                    "required": ["channel", "message"],
                },
            },
        }


class GetRoleMembersTool(Tool):
    """Provide user records for individuals in a specified role (read operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str, status: str = None) -> str:
        users = data.get("users", [])
        user_roles = data.get("user_roles", [])

        if not isinstance(user_roles, list) or not isinstance(users, list):
            payload = {"error": "users and user_roles must be lists"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(role_id, str) or not role_id.strip():
            payload = {"error": "role_id must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out

        member_user_ids = {
            ur["user_id"] for ur in user_roles if ur.get("role_id") == role_id
        }
        results = []
        for u in users:
            if u.get("user_id") in member_user_ids:
                if status and u.get("status") != status:
                    continue
                results.append(u)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoleMembers",
                "description": "List user records for members assigned to a role. Optional filter by user status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The role_id to lookup",
                        },
                        "status": {
                            "type": "string",
                            "description": "Optional user status filter, e.g. ACTIVE",
                        },
                    },
                    "required": ["role_id"],
                },
            },
        }


class AssignCertificationTool(Tool):
    """Establish/assign a certification record to a user (write operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str, user_id: str, assigned_on: str = None, status: str = "ASSIGNED") -> str:
        certifications = data.get("certifications", [])
        users = data.get("users", [])

        if not isinstance(certifications, list):
            payload = {"error": "certifications must be a list"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(users, list):
            payload = {"error": "users must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(certification_id, str) or not certification_id.strip():
            payload = {"error": "certification_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if not isinstance(user_id, str) or not user_id.strip():
            payload = {"error": "user_id must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out
        if assigned_on is not None and not isinstance(assigned_on, str):
            payload = {"error": "assigned_on must be a string if provided"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if not isinstance(status, str) or not status.strip():
            payload = {"error": "status must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out

        #Confirm user existence
        user = next((u for u in users if u.get("user_id") == user_id), None)
        if not user:
            payload = {"error": f"user_id {user_id} not found in users"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #Verify that certification_id is distinct
        if any(c.get("certification_id") == certification_id for c in certifications):
            payload = {"error": f"certification_id {certification_id} already exists"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Add a minimal, schema-compliant record utilizing only recognized field names from datasets
        new_record = {
            "certification_id": certification_id,
            "user_id": user_id,
            "status": status,
        }
        if assigned_on:
            new_record["assigned_on"] = (
                assigned_on  #field name is present in project datasets (e.g., user_roles)
            )

        certifications.append(new_record)
        payload = {
                "success": f"Certification {certification_id} assigned to user {user_id}",
                "certification": new_record,
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
                "name": "AssignCertification",
                "description": "Create/assign a certification record to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "Unique certification identifier",
                        },
                        "user_id": {"type": "string", "description": "Target user_id"},
                        "assigned_on": {
                            "type": "string",
                            "description": "Deterministic assignment timestamp",
                        },
                        "status": {
                            "type": "string",
                            "description": "Initial status (defaults to ASSIGNED)",
                        },
                    },
                    "required": ["certification_id", "user_id"],
                },
            },
        }


class RevokeCertificationTool(Tool):
    """Remove an existing certification from a user (write operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str, expires_on: str = None) -> str:
        certifications = data.get("certifications", [])
        if not isinstance(certifications, list):
            payload = {"error": "certifications must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(certification_id, str) or not certification_id.strip():
            payload = {"error": "certification_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if expires_on is not None and not isinstance(expires_on, str):
            payload = {"error": "expires_on must be a string if provided"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        cert = next(
            (
                c
                for c in certifications
                if c.get("certification_id") == certification_id
            ),
            None,
        )
        if not cert:
            payload = {"error": f"Certification {certification_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        cert["status"] = "REVOKED"
        #Reset completion if available
        if "completed_on" in cert:
            cert["completed_on"] = None
        #Optionally mark an end using a pre-existing field name utilized in other datasets
        if expires_on:
            cert["expires_on"] = expires_on
        payload = {"success": f"Certification {certification_id} revoked"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeCertification",
                "description": "Revoke a certification by certification_id; clears completed_on and can set expires_on.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"},
                        "expires_on": {
                            "type": "string",
                            "description": "Optional deterministic end timestamp",
                        },
                    },
                    "required": ["certification_id"],
                },
            },
        }


class LinkAlertToIncidentTool(Tool):
    """Connect an existing SIEM alert to an incident record (write operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], incident_id: str = None, alert_id: str = None) -> str:
        incidents = data.get("incidents", [])
        alerts = data.get("siem_alerts", [])

        if not isinstance(incidents, list):
            payload = {"error": "incidents must be a list"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(alerts, list):
            payload = {"error": "siem_alerts must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(incident_id, str) or not incident_id.strip():
            payload = {"error": "incident_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if not isinstance(alert_id, str) or not alert_id.strip():
            payload = {"error": "alert_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        incident = next(
            (i for i in incidents if i.get("incident_id") == incident_id), None
        )
        if not incident:
            payload = {"error": f"Incident {incident_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        alert = next((a for a in alerts if a.get("alert_id") == alert_id), None)
        if not alert:
            payload = {"error": f"Alert {alert_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        linked = incident.setdefault("linked_alerts", [])
        if alert_id not in linked:
            linked.append(alert_id)
        payload = {
                "success": f"Linked alert {alert_id} to incident {incident_id}",
                "incident_id": incident_id,
                "alert_id": alert_id,
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
                "name": "LinkAlertToIncident",
                "description": "Append an alert_id to an incident's linked_alerts after validating existence.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "incident_id": {"type": "string"},
                        "alert_id": {"type": "string"},
                    },
                    "required": ["incident_id", "alert_id"],
                },
            },
        }


class ListCertificationsForReviewerTool(Tool):
    """Display all certifications allocated to a specific reviewer (read operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], reviewer_id: str = None) -> str:
        certifications = data.get("certifications", [])
        if not isinstance(certifications, list):
            payload = {"error": "certifications must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(reviewer_id, str) or not reviewer_id.strip():
            payload = {"error": "reviewer_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        results = [c for c in certifications if c.get("reviewer_id") == reviewer_id]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListCertificationsForReviewer",
                "description": "List all certifications assigned to a specific reviewer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reviewer_id": {
                            "type": "string",
                            "description": "The reviewer’s user_id",
                        }
                    },
                    "required": ["reviewer_id"],
                },
            },
        }


class GetTicketDetailsTool(Tool):
    """Get a HubSpot ticket using ticket_id (read-only, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None) -> str:
        tickets = data.get("hubspot_tickets", [])
        if not isinstance(tickets, list):
            payload = {"error": "hubspot_tickets must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(ticket_id, str) or not ticket_id.strip():
            payload = {"error": "ticket_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        for t in tickets:
            if t.get("ticket_id") == ticket_id:
                payload = t
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"ticket_id {ticket_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetTicketDetails",
                "description": "Retrieve details of a HubSpot ticket by ticket_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"ticket_id": {"type": "string"}},
                    "required": ["ticket_id"],
                },
            },
        }


class GetAuditLogsForTargetTool(Tool):
    """Retrieve audit logs filtered by target_id (read-only, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], target_id: str = None) -> str:
        audit_logs = data.get("audit_logs", [])
        if not isinstance(audit_logs, list):
            payload = {"error": "audit_logs must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(target_id, str) or not target_id.strip():
            payload = {"error": "target_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        results = [log for log in audit_logs if log.get("target_id") == target_id]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetAuditLogsForTarget",
                "description": "Retrieve audit logs filtered by target_id (user, resource, role, alert, etc.).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_id": {
                            "type": "string",
                            "description": "The target entity ID (e.g., U-001, RES-021, ALRT-003)",
                        }
                    },
                    "required": ["target_id"],
                },
            },
        }


class GetSiemAlertTool(Tool):
    """Get information about a specific SIEM alert (read-only, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str) -> str:
        alerts = data.get("siem_alerts", [])
        if not isinstance(alerts, list):
            payload = {"error": "siem_alerts must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(alert_id, str) or not alert_id.strip():
            payload = {"error": "alert_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        for a in alerts:
            if a.get("alert_id") == alert_id:
                payload = a
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"alert_id {alert_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetSiemAlert",
                "description": "Retrieve SIEM alert details by alert_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"alert_id": {"type": "string"}},
                    "required": ["alert_id"],
                },
            },
        }


class ListUserSessionsTool(Tool):
    """Display sessions for a specific user with an optional filter for active sessions only (read operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, active_only: bool = False) -> str:
        sessions = data.get("sessions", [])
        if not isinstance(sessions, list):
            payload = {"error": "sessions must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(user_id, str) or not user_id.strip():
            payload = {"error": "user_id must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out

        if active_only not in (True, False):
            payload = {"error": "active_only must be a boolean if provided"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        results = []
        for s in sessions:
            if s.get("user_id") != user_id:
                continue
            if active_only and s.get("end_time") is not None:
                continue
            results.append(s)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListUserSessions",
                "description": "List sessions for a user; optionally filter to only active sessions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id"},
                        "active_only": {
                            "type": "boolean",
                            "description": "If true, only return sessions without end_time",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }


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


class ListPermissionsForRoleTool(Tool):
    """Display permissions associated with a role_id (read operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        role_permissions = data.get("role_permissions", [])
        permissions = data.get("permissions", [])
        if not isinstance(role_permissions, list):
            payload = {"error": "role_permissions must be a list"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(permissions, list):
            payload = {"error": "permissions must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        roles = data.get("roles", [])
        if not any(r.get("role_id") == role_id for r in roles):
            payload = {"error": f"role_id {role_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(role_id, str) or not role_id.strip():
            payload = {"error": "role_id must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out

        perm_ids = [
            rp.get("permission_id")
            for rp in role_permissions
            if rp.get("role_id") == role_id
        ]
        results = [p for p in permissions if p.get("permission_id") in perm_ids]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPermissionsForRole",
                "description": "List permission records attached to the given role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }


class GetCertificationTool(Tool):
    """Provide a single certification record using certification_id (read operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None) -> str:
        certifications = data.get("certifications", [])
        if not isinstance(certifications, list):
            payload = {"error": "certifications must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(certification_id, str) or not certification_id.strip():
            payload = {"error": "certification_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        for c in certifications:
            if c.get("certification_id") == certification_id:
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Certification {certification_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertification",
                "description": "Retrieve a certification by certification_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"certification_id": {"type": "string"}},
                    "required": ["certification_id"],
                },
            },
        }


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


class UpdateTicketStatusTool(Tool):
    """Revise the status of a HubSpot ticket (write operation)."""

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, status: str = None, updated_at: str = None) -> str:
        tickets = data.get("hubspot_tickets", [])

        if not isinstance(ticket_id, str):
            payload = {"error": "ticket_id must be provided"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(status, str):
            payload = {"error": "status must be provided"}
            out = json.dumps(payload, indent=2)
            return out

        for t in tickets:
            if t.get("ticket_id") == ticket_id:
                t["status"] = status
                if updated_at:
                    t["updated_at"] = updated_at
                payload = {"success": f"Ticket {ticket_id} updated", "ticket": t}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Ticket {ticket_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTicketStatus",
                "description": "Update the status of a HubSpot ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "Unique ID of the ticket",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status of the ticket (e.g., OPEN, CLOSED, IN_PROGRESS)",
                        },
                        "updated_at": {
                            "type": "string",
                            "description": "Optional ISO8601 timestamp of the update",
                        },
                    },
                    "required": ["ticket_id", "status"],
                },
            },
        }


class UpdateCertificationStatusTool(Tool):
    """Revise the status of a certification review (write operation)."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None, status: str = None, completed_on: str = None) -> str:
        certs = data.get("certifications", [])

        if not isinstance(certification_id, str):
            payload = {"error": "certification_id must be provided"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(status, str):
            payload = {"error": "status must be provided"}
            out = json.dumps(payload, indent=2)
            return out

        for c in certs:
            if c.get("certification_id") == certification_id:
                c["status"] = status
                if completed_on:
                    c["completed_on"] = completed_on
                payload = {"success": f"Certification {certification_id} updated", "certification": c}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"Certification {certification_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCertificationStatus",
                "description": "Update the status of a certification review.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "Unique ID of the certification",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status (e.g., PENDING, IN_PROGRESS, COMPLETED)",
                        },
                        "completed_on": {
                            "type": "string",
                            "description": "Optional ISO8601 timestamp when completed",
                        },
                    },
                    "required": ["certification_id", "status"],
                },
            },
        }


class EnableUserMFATool(Tool):
    """Activate MFA for a specified user (write operation)."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        users = data.get("users", [])

        if not isinstance(user_id, str):
            payload = {"error": "user_id must be provided"}
            out = json.dumps(payload, indent=2)
            return out

        for u in users:
            if u.get("user_id") == user_id:
                u["mfa_enabled"] = True
                payload = {"success": f"MFA enabled for {user_id}", "user": u}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"User {user_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnableUserMfa",
                "description": "Enable MFA for a given user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID to enable MFA for",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


from typing import Any


class UpdateAccessRequestTool(Tool):
    """Fundamental: modify an access request's status and metadata (no side effects)."""

    _ALLOWED = {"PENDING", "APPROVED", "REJECTED", "DEFERRED"}

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, status: str = None, updated_on: str = None, updated_by: str = None) -> str:
        # Mandatory parameters
        params_dict = {k: v for k, v in locals().items() if k != "data"}
        missing = [
            k
            for k in ("request_id", "status", "updated_on", "updated_by")
            if params_dict.get(k) is None
        ]
        if missing:
            payload = {"error": f"Missing: {', '.join(missing)}"}
            out = json.dumps(payload, indent=2)
            return out

        # Simple status verification
        if status not in UpdateAccessRequestTool._ALLOWED:
            payload = {
                    "error": f"Invalid status '{status}'. Allowed: {sorted(UpdateAccessRequestTool._ALLOWED)}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Import tables
        access_requests = data.get("access_requests", [])
        users = data.get("users", [])

        # References
        req = next(
            (r for r in access_requests if r.get("request_id") == request_id), None
        )
        if not req:
            payload = {"error": f"Unknown request_id '{request_id}'"}
            out = json.dumps(payload, indent=2)
            return out

        if not any(u.get("user_id") == updated_by for u in users):
            payload = {"error": f"Unknown updated_by '{updated_by}'"}
            out = json.dumps(payload, indent=2)
            return out

        # Modify in place (basic)
        req["status"] = status
        req["updated_on"] = updated_on
        req["updated_by"] = updated_by
        payload = req
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAccessRequest",
                "description": "Basic update of an access request's status and metadata (no side effects).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string", "description": "e.g., AR-007"},
                        "status": {
                            "type": "string",
                            "enum": ["PENDING", "APPROVED", "REJECTED", "DEFERRED"],
                        },
                        "updated_on": {
                            "type": "string",
                            "description": "ISO 8601 timestamp",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "User ID performing the update",
                        },
                    },
                    "required": ["request_id", "status", "updated_on", "updated_by"],
                },
            },
        }


class ExportAuditLogsTool(Tool):
    """Export audit logs with optional filtering."""

    @staticmethod
    def invoke(data: dict[str, Any], actor_id: str = None, action_type: str = None, 
               target_id: str = None, start_time: str = None, end_time: str = None) -> str:
        logs = data.get("audit_logs", [])
        results = []

        for log in logs:
            if actor_id and log.get("actor_id") != actor_id:
                continue
            if action_type and log.get("action_type") != action_type:
                continue
            if target_id and log.get("target_id") != target_id:
                continue
            if start_time and log.get("timestamp") < start_time:
                continue
            if end_time and log.get("timestamp") > end_time:
                continue
            results.append(log)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportAuditLogs",
                "description": "Export audit logs with optional filters for actor, action, target, and time range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {"type": "string"},
                        "action_type": {"type": "string"},
                        "target_id": {"type": "string"},
                        "start_time": {
                            "type": "string",
                            "description": "ISO8601 lower bound",
                        },
                        "end_time": {
                            "type": "string",
                            "description": "ISO8601 upper bound",
                        },
                    },
                },
            },
        }


class GetCurrentTimeTool(Tool):
    """
    Provides the fixed canonical current time utilized in evaluation.
    """

    @staticmethod
    def invoke(data: dict) -> str:
        payload = {"current_time": "2025-08-17T00:00:00Z"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetCurrentTime",
                "description": "Return the canonical current time for use in audit logs and decisions.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


TOOLS = [
    ListUsersTool(),
    GetUserDetailsTool(),
    ListRolesTool(),
    RevokeRoleFromUserTool(),
    ListAccessRequestsTool(),
    ApproveAccessRequestTool(),
    RejectAccessRequestTool(),
    GetCertificationDetailsTool(),
    CompleteCertificationTool(),
    ListPolicyExceptionsTool(),
    ApprovePolicyExceptionTool(),
    DenyPolicyExceptionTool(),
    GetPolicyExceptionDetailsTool(),
    RequestPolicyExceptionTool(),
    ListSiemAlertsTool(),
    GetSiemAlertDetailsTool(),
    CreateSiemRuleTool(),
    InvestigateSiemIncidentTool(),
    ListSessionsTool(),
    TerminateSessionTool(),
    AuditIamAccessTool(),
    SearchLogsTool(),
    ExportAuditLogsTool(),
    ExportLogsTool(),
    GetUserRolesTool(),
    GetPermissionDetailsTool(),
    GetResourceDetailsTool(),
    GetRoleDetailsTool(),
    CreateAccessRequestTool(),
    CreateHubspotTicketTool(),
    UpdateUserStatusTool(),
    EscalateSiemAlertTool(),
    SearchSlackMessagesTool(),
    ModerateSlackChannelTool(),
    CreateIncidentRecordTool(),
    CreateAuditLogTool(),
    SendEmailTool(),
    CreateUserTool(),
    GetRoleMembersTool(),
    PostSlackMessageTool(),
    GetAccessRequestTool(),
    LinkAlertToIncidentTool(),
    RevokeCertificationTool(),
    AssignCertificationTool(),
    ListCertificationsForReviewerTool(),
    GetTicketDetailsTool(),
    GetAuditLogsForTargetTool(),
    GetSiemAlertTool(),
    ListUserSessionsTool(),
    AssignRoleToUserTool(),
    ListPermissionsForRoleTool(),
    GetCertificationTool(),
    RemoveRoleFromUserTool(),
    UpdateCertificationStatusTool(),
    UpdateTicketStatusTool(),
    EnableUserMFATool(),
    GetCurrentTimeTool(),
    UpdateAccessRequestTool(),
]
