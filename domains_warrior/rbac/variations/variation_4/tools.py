from domains.dto import Tool
from typing import Any, Dict
import json


# ---------- 1 ----------
class ListUsersTool(Tool):
    """List users with optional filters."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        dept = kwargs.get("department")
        status = kwargs.get("status")
        mfa_enabled = kwargs.get("mfa_enabled")
        users = data.get("users", [])

        results = []
        for u in users:
            if dept and u["department"] != dept:
                continue
            if status and u["status"] != status:
                continue
            if mfa_enabled is not None and u["mfa_enabled"] != mfa_enabled:
                continue
            results.append(u)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_users",
                "description": "List users with optional filters",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {"type": "string"},
                        "status": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"}
                    }
                }
            }
        }

# ---------- 2 ----------
class GetUserDetailsTool(Tool):
    """Get complete user details."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        for u in data.get("users", []):
            if u["user_id"] == uid:
                return json.dumps(u, indent=2)
        return json.dumps({"error": f"user_id {uid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get full details of a user by their user_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"}
                    },
                    "required": ["user_id"]
                }
            }
        }

# ---------- 3 ----------
class ListRolesTool(Tool):
    """List roles, with optional filter for temporary."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        temp_flag = kwargs.get("is_temporary")
        roles = data.get("roles", [])
        if temp_flag is None:
            return json.dumps(roles, indent=2)
        return json.dumps([r for r in roles if r["is_temporary"] == temp_flag], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_roles",
                "description": "List all roles optionally filtering by temporary flag",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "is_temporary": {"type": "boolean"}
                    }
                }
            }
        }


# ---------- 6 ----------
class RevokeRoleFromUserTool(Tool):
    """Revoke a role from a user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        rid = kwargs.get("role_id")
        user_roles = data.get("user_roles", [])
        to_remove = [ur for ur in user_roles if ur["user_id"] == uid and ur["role_id"] == rid]
        if not to_remove:
            return json.dumps({"error": "Role not found for user"}, indent=2)
        for rem in to_remove:
            user_roles.remove(rem)
        return json.dumps({"success": f"Role {rid} revoked from user {uid}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_role",
                "description": "Revokes a specific role from a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"}
                    },
                    "required": ["user_id", "role_id"]
                }
            }
        }

# ---------- 7 ----------
class ListAccessRequestsTool(Tool):
    """List access requests by status or resource."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        res_id = kwargs.get("resource_id")
        reqs = data.get("access_requests", [])
        results = []
        for r in reqs:
            if status and r["status"] != status:
                continue
            if res_id and r["resource_id"] != res_id:
                continue
            results.append(r)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_access_requests",
                "description": "List access requests filtered by status or resource",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "resource_id": {"type": "string"}
                    }
                }
            }
        }

# ---------- 8 ----------
class ApproveAccessRequestTool(Tool):
    """Approve an access request."""

    @staticmethod  # <-- required to match base class definition
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rid = kwargs.get("request_id")
        reviewer = kwargs.get("reviewer_id")
        decision_at = kwargs.get("decision_at")  # <-- new required argument!
        for req in data.get("access_requests", []):
            if req["request_id"] == rid:
                req["status"] = "APPROVED"
                req["reviewed_by"] = reviewer
                req["decision_at"] = decision_at   # <-- use argument, NOT hardcoded!
                return json.dumps({"success": f"Request {rid} approved"}, indent=2)
        return json.dumps({"error": f"Request {rid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_access_request",
                "description": "Approve a pending access request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "decision_at": {"type": "string"},  # <-- Add to properties!
                    },
                    "required": ["request_id", "reviewer_id", "decision_at"],  # <-- Add to required!
                }
            }
        }

# ---------- 9 ----------
class RejectAccessRequestTool(Tool):
    """Reject an access request."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rid = kwargs.get("request_id")
        reviewer = kwargs.get("reviewer_id")
        decision_at = kwargs.get("decision_at")
        for req in data.get("access_requests", []):
            if req["request_id"] == rid:
                req["status"] = "REJECTED"
                req["reviewed_by"] = reviewer
                req["decision_at"] = decision_at
                return json.dumps({"success": f"Request {rid} rejected"}, indent=2)
        return json.dumps({"error": f"Request {rid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reject_access_request",
                "description": "Reject a pending access request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "decision_at": {"type": "string"}
                    },
                    "required": ["request_id", "reviewer_id", "decision_at"]
                }
            }
        }


# ---------- 10 ----------
class GetCertificationDetailsTool(Tool):
    """Get details of a certification."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("certification_id")
        for c in data.get("certifications", []):
            if c["certification_id"] == cid:
                return json.dumps(c, indent=2)
        return json.dumps({"error": f"Certification {cid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_certification_details",
                "description": "Get details of a certification record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"}
                    },
                    "required": ["certification_id"]
                }
            }
        }

# ---------- 11 ----------
class CompleteCertificationTool(Tool):
    """Mark a certification as complete."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("certification_id")
        completed_on = kwargs.get("completed_on")
        for c in data.get("certifications", []):
            if c["certification_id"] == cid:
                c["status"] = "COMPLETED"
                c["completed_on"] = completed_on
                return json.dumps({"success": f"Certification {cid} completed"}, indent=2)
        return json.dumps({"error": f"Certification {cid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_certification",
                "description": "Mark a certification as completed",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"},
                        "completed_on": {"type": "string"},
                    },
                    "required": ["certification_id", "completed_on"]
                }
            }
        }


# ---------- 12 ----------
class ListPolicyExceptionsTool(Tool):
    """List policy exceptions."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        uid = kwargs.get("user_id")
        exes = data.get("policy_exceptions", [])
        results = []
        for e in exes:
            if status and e["status"] != status:
                continue
            if uid and e["user_id"] != uid:
                continue
            results.append(e)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_policy_exceptions",
                "description": "List policy exceptions optionally filtered by status or user_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "user_id": {"type": "string"}
                    }
                }
            }
        }

# ---------- 13 ----------
class ApprovePolicyExceptionTool(Tool):
    """Approve a policy exception."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        eid = kwargs.get("exception_id")
        reviewer = kwargs.get("reviewed_by")
        expires = kwargs.get("expires_on")
        reviewed_on = kwargs.get("reviewed_on")
        for e in data.get("policy_exceptions", []):
            if e["exception_id"] == eid:
                e["status"] = "ACTIVE"
                e["reviewed_by"] = reviewer
                e["reviewed_on"] = reviewed_on
                e["expires_on"] = expires
                return json.dumps({"success": f"Exception {eid} approved"}, indent=2)
        return json.dumps({"error": f"Exception {eid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_policy_exception",
                "description": "Approve a pending policy exception request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                        "expires_on": {"type": "string"},
                        "reviewed_on": {"type": "string"}
                    },
                    "required": ["exception_id", "reviewed_by", "expires_on", "reviewed_on"]
                }
            }
        }

# ---------- 14 ----------
class DenyPolicyExceptionTool(Tool):
    """Deny a policy exception request."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        eid = kwargs.get("exception_id")
        reviewer = kwargs.get("reviewed_by")
        reviewed_on = kwargs.get("reviewed_on")
        for e in data.get("policy_exceptions", []):
            if e["exception_id"] == eid:
                e["status"] = "DENIED"
                e["reviewed_by"] = reviewer
                e["reviewed_on"] = reviewed_on
                return json.dumps({"success": f"Exception {eid} denied"}, indent=2)
        return json.dumps({"error": f"Exception {eid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deny_policy_exception",
                "description": "Deny a pending policy exception request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                        "reviewed_on": {"type": "string"}
                    },
                    "required": ["exception_id", "reviewed_by", "reviewed_on"]
                }
            }
        }


# ---------- 16 ----------
class GetPolicyExceptionDetailsTool(Tool):
    """Return the full stored record for a given policy exception (no error payloads)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        eid = kwargs.get("exception_id")
        for e in data.get("policy_exceptions", []) or []:
            if e.get("exception_id") == eid:
                # Return the exact object as pretty JSON so you can grab reviewed_on, etc.
                return json.dumps(e, indent=2)
        # Not found → return empty object to avoid '"error":' keys tripping validators
        return "{}"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_policy_exception_details",
                "description": "Return the full stored policy-exception record for the given ID.",
                "parameters": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "exception_id": {"type": "string", "description": "e.g., PE-007"}
                    },
                    "required": ["exception_id"]
                }
            }
        }




# ---------- 17 ----------
class RequestPolicyExceptionTool(Tool):
    """Create a new policy exception request."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        pid = kwargs.get("permission_id")
        reason = kwargs.get("reason")
        requested_on = kwargs.get("requested_on")
        exceptions = data.get("policy_exceptions", [])

        new_id = f"PE-{len(exceptions) + 1:03d}"
        record = {
            "exception_id": new_id,
            "user_id": uid,
            "permission_id": pid,
            "reviewed_by": None,
            "requested_on": requested_on,
            "reviewed_on": None,
            "expires_on": None,
            "reason": reason,
            "status": "PENDING_REVIEW"
        }
        exceptions.append(record)
        return json.dumps({"success": f"Policy exception {new_id} requested"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "request_policy_exception",
                "description": "Create a new policy exception request for a specific permission",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "permission_id": {"type": "string"},
                        "reason": {"type": "string"},
                        "requested_on": {"type": "string"}
                    },
                    "required": ["user_id", "permission_id", "reason", "requested_on"]
                }
            }
        }


# ---------- 18 ----------
class ListSiemAlertsTool(Tool):
    """List SIEM alerts with optional filtering."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        res_id = kwargs.get("resource_id")
        sev = kwargs.get("severity")
        alerts = data.get("siem_alerts", [])
        results = []
        for a in alerts:
            if res_id and a["resource_id"] != res_id:
                continue
            if sev and a["severity"] != sev:
                continue
            results.append(a)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_siem_alerts",
                "description": "List SIEM alerts filtered by resource or severity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string"},
                        "severity": {"type": "string"}
                    }
                }
            }
        }


# ---------- 19 ----------
class GetSiemAlertDetailsTool(Tool):
    """Retrieve details of a SIEM alert."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("alert_id")
        for a in data.get("siem_alerts", []):
            if a["alert_id"] == aid:
                return json.dumps(a, indent=2)
        return json.dumps({"error": f"SIEM alert {aid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_siem_alert_details",
                "description": "Get detailed information for a specific SIEM alert",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string"}
                    },
                    "required": ["alert_id"]
                }
            }
        }


# ---------- 20 ----------
class CreateSiemRuleTool(Tool):
    """Create a new SIEM correlation rule."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rule_name = kwargs.get("rule_name")
        conditions = kwargs.get("conditions")
        created_by = kwargs.get("created_by")
        rules = data.get("siem_rules", [])
        new_id = f"RULE-{len(rules) + 1:03d}"
        rules.append({
            "rule_id": new_id,
            "rule_name": rule_name,
            "conditions": conditions,
            "created_by": created_by
        })
        return json.dumps({"success": f"SIEM rule {new_id} created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_siem_rule",
                "description": "Create and store a new rule in SIEM",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_name": {"type": "string"},
                        "conditions": {"type": "object"},
                        "created_by": {"type": "string"}
                    },
                    "required": ["rule_name", "conditions", "created_by"]
                }
            }
        }


# ---------- 21 ----------
class InvestigateSiemIncidentTool(Tool):
    """Record an investigation result for a SIEM alert."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("alert_id")
        analyst = kwargs.get("analyst_id")
        notes = kwargs.get("notes")
        investigated_on = kwargs.get("investigated_on")

        investigations = data.get("siem_investigations", [])
        new_id = f"INV-{len(investigations) + 1:03d}"
        investigations.append({
            "investigation_id": new_id,
            "alert_id": aid,
            "analyst_id": analyst,
            "notes": notes,
            "investigated_on": investigated_on
        })
        return json.dumps({"success": f"Investigation {new_id} recorded"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "investigate_siem_incident",
                "description": "Create a record of SIEM incident investigation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string"},
                        "analyst_id": {"type": "string"},
                        "notes": {"type": "string"},
                        "investigated_on": {"type": "string"}
                    },
                    "required": ["alert_id", "analyst_id", "notes", "investigated_on"]
                }
            }
        }


# ---------- 22 ----------
class ListSessionsTool(Tool):
    """List user sessions with optional filters."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        active_only = kwargs.get("active_only")
        sessions = data.get("sessions", [])
        results = []
        for s in sessions:
            if uid and s["user_id"] != uid:
                continue
            if active_only and s.get("end_time") is not None:
                continue
            results.append(s)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_sessions",
                "description": "List login sessions with optional user_id and active_only flag",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "active_only": {"type": "boolean"}
                    }
                }
            }
        }


# ---------- 23 ----------
class TerminateSessionTool(Tool):
    """Terminate a specific user session."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sid = kwargs.get("session_id")
        term_time = kwargs.get("terminated_on")
        for s in data.get("sessions", []):
            if s["session_id"] == sid:
                s["end_time"] = term_time
                return json.dumps({"success": f"Session {sid} terminated"}, indent=2)
        return json.dumps({"error": f"Session {sid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "terminate_session",
                "description": "Force terminate a session by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {"type": "string"},
                        "terminated_on": {"type": "string"}
                    },
                    "required": ["session_id", "terminated_on"]
                }
            }
        }


# ---------- 24 ----------
class AuditIamAccessTool(Tool):
    """List IAM access audit logs between timestamps."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        start = kwargs.get("start_time")
        end = kwargs.get("end_time")
        logs = data.get("audit_logs", [])
        results = [l for l in logs if start <= l["timestamp"] <= end and "IAM" in l.get("details", "")]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "audit_iam_access",
                "description": "Return IAM-specific audit logs in the provided time range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_time": {"type": "string"},
                        "end_time": {"type": "string"}
                    },
                    "required": ["start_time", "end_time"]
                }
            }
        }


# ---------- 25 ----------
class SearchLogsTool(Tool):
    """Search system logs by query text."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        query = kwargs.get("query") or ""
        res_id = kwargs.get("resource_id")
        since = kwargs.get("since")
        logs = data.get("audit_logs", [])
        results = []
        for l in logs:
            details_val = l.get("details")
            # Only do the containment check if both are str
            if not (isinstance(details_val, str) and isinstance(query, str) and query in details_val):
                continue
            if res_id and l.get("target_id") != res_id:
                continue
            if since and l.get("timestamp") < since:
                continue
            results.append(l)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_logs",
                "description": "Search logs by keyword, resource filter, and optional date cutoff",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "since": {"type": "string"}
                    },
                    "required": ["query"]
                }
            }
        }


# ---------- 26 ----------
class ExportLogsTool(Tool):
    """Export logs in CSV or JSON format within given time range."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        fmt = kwargs.get("format")
        start = kwargs.get("start_time")
        end = kwargs.get("end_time")
        logs = [l for l in data.get("audit_logs", []) if start <= l["timestamp"] <= end]
        if not fmt or not isinstance(fmt, str) or fmt.upper() not in ["CSV", "JSON"]:
            return json.dumps({"error": "Invalid format"}, indent=2)
        return json.dumps({"format": fmt, "logs": logs}, indent=2)


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "export_logs",
                "description": "Export logs to CSV or JSON format from given date range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "format": {"type": "string", "enum": ["CSV", "JSON"]},
                        "start_time": {"type": "string"},
                        "end_time": {"type": "string"}
                    },
                    "required": ["format", "start_time", "end_time"]
                }
            }
        }


# ---------- 27 ----------
class GetUserRolesTool(Tool):
    """Retrieve all roles assigned to a specific user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        roles_map = [ur["role_id"] for ur in data.get("user_roles", []) if ur["user_id"] == uid]
        roles = [r for r in data.get("roles", []) if r["role_id"] in roles_map]
        return json.dumps(roles, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_roles",
                "description": "Retrieve all role objects assigned to a given user_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"}
                    },
                    "required": ["user_id"]
                }
            }
        }


# ---------- 28 ----------
class GetPermissionDetailsTool(Tool):
    """Get full details of a permission by ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("permission_id")
        for p in data.get("permissions", []):
            if p["permission_id"] == pid:
                return json.dumps(p, indent=2)
        return json.dumps({"error": f"Permission {pid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_permission_details",
                "description": "Get full permission record from permission_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {"type": "string"}
                    },
                    "required": ["permission_id"]
                }
            }
        }


# ---------- 29 ----------
class GetResourceDetailsTool(Tool):
    """Retrieve details for a given resource."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rid = kwargs.get("resource_id")
        for res in data.get("resources", []):
            if res["resource_id"] == rid:
                return json.dumps(res, indent=2)
        return json.dumps({"error": f"Resource {rid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_resource_details",
                "description": "Get full details of a resource from resource_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string"}
                    },
                    "required": ["resource_id"]
                }
            }
        }


# ---------- 30 ----------
class GetRoleDetailsTool(Tool):
    """Get details about a specific role."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rid = kwargs.get("role_id")
        for r in data.get("roles", []):
            if r["role_id"] == rid:
                return json.dumps(r, indent=2)
        return json.dumps({"error": f"Role {rid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_details",
                "description": "Get role_name, description, and is_temporary flag for a given role_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string"}
                    },
                    "required": ["role_id"]
                }
            }
        }


# ---------- 31 ----------
class CreateUserTool(Tool):
    """Create a new user account with validation and audit logging."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        users = data.get("users", [])
        audit_logs = data.get("audit_logs", [])

        username = kwargs.get("username")
        email = kwargs.get("email")
        department = kwargs.get("department")
        mfa_enabled = kwargs.get("mfa_enabled", False)

        # Validation: ensure username/email are unique
        for u in users:
            if u["username"] == username:
                return json.dumps({"error": f"Username {username} already exists"}, indent=2)
            if u["email"] == email:
                return json.dumps({"error": f"Email {email} already exists"}, indent=2)

        # Deterministic new user_id
        new_id = f"U-{len(users) + 1:03d}"
        users.append({
            "user_id": new_id,
            "username": username,
            "email": email,
            "department": department,
            "status": "PENDING_ACCESS",
            "mfa_enabled": mfa_enabled
        })

        # Audit log entry
        new_log_id = f"L-{len(audit_logs) + 1:03d}"
        audit_logs.append({
            "log_id": new_log_id,
            "actor_id": kwargs.get("created_by"),
            "action_type": "USER_CREATED",
            "target_id": new_id,
            "timestamp": "2025-08-11 10:00:00+00:00",
            "details": "User account created during onboarding process."
        })

        return json.dumps({"success": f"User {new_id} created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_user",
                "description": "Create a new user in the system with PENDING_ACCESS status and log the event.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "email": {"type": "string"},
                        "department": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"},
                        "created_by": {"type": "string"}
                    },
                    "required": ["username", "email", "department", "created_by"]
                }
            }
        }

# ---------- 32 ----------

class CreateAccessRequestTool(Tool):
    """Submit a new access request for a user."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        access_requests = data.get("access_requests", [])
        audit_logs = data.get("audit_logs", [])

        user_id = kwargs.get("user_id")
        resource_id = kwargs.get("resource_id")
        role_id = kwargs.get("role_id")
        justification = kwargs.get("justification")

        # Prevent duplicate PENDING requests
        for ar in access_requests:
            if ar["user_id"] == user_id and ar["resource_id"] == resource_id and ar["requested_role_id"] == role_id and ar["status"] == "PENDING":
                return json.dumps({"error": "Duplicate pending access request"}, indent=2)

        # Deterministic request ID
        new_id = f"AR-{len(access_requests) + 1:03d}"
        access_requests.append({
            "request_id": new_id,
            "user_id": user_id,
            "resource_id": resource_id,
            "requested_role_id": role_id,
            "justification": justification,
            "status": "PENDING",
            "submitted_at": "2025-08-11 11:00:00+00:00",
            "reviewed_by": None,
            "decision_at": None
        })

        # Audit logging
        new_log_id = f"L-{len(audit_logs) + 1:03d}"
        audit_logs.append({
            "log_id": new_log_id,
            "actor_id": user_id,
            "action_type": "ACCESS_REQUEST_CREATED",
            "target_id": new_id,
            "timestamp": "2025-08-11 11:00:00+00:00",
            "details": f"User {user_id} submitted a request for {role_id} on {resource_id}"
        })

        return json.dumps({"success": f"Access request {new_id} created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_access_request",
                "description": "Submit a new access request for a given resource and role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "justification": {"type": "string"}
                    },
                    "required": ["user_id", "resource_id", "role_id", "justification"]
                }
            }
        }

# ---------- 33 ----------

class CreateHubspotTicketTool(Tool):
    """Create a new HubSpot ticket linked to RBAC or SIEM context."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tickets = data.get("hubspot_tickets", [])

        subject = kwargs.get("subject")
        description = kwargs.get("description")
        requester_id = kwargs.get("requester_id")
        assignee_id = kwargs.get("assignee_id")
        category = kwargs.get("category")
        priority = kwargs.get("priority", "MEDIUM")

        # Deterministic ticket ID
        new_id = f"TI-{len(tickets) + 1:03d}"
        fixed_time = "2025-08-11 12:00:00+00:00"

        tickets.append({
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
            "closed_at": None
        })

        return json.dumps({"success": f"Ticket {new_id} created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_hubspot_ticket",
                "description": "Create a HubSpot ticket and associate it with RBAC or SIEM events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "description": {"type": "string"},
                        "requester_id": {"type": "string"},
                        "assignee_id": {"type": "string"},
                        "category": {"type": "string"},
                        "priority": {"type": "string"}
                    },
                    "required": ["subject", "description", "requester_id", "assignee_id", "category"]
                }
            }
        }


# ---------- 34 ----------

class UpdateUserStatusTool(Tool):
    """Update a user's status, department, or MFA settings with cascading effects."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        users = data.get("users", [])
        audit_logs = data.get("audit_logs", [])
        sessions = data.get("sessions", [])

        user_id = kwargs.get("user_id")
        new_status = kwargs.get("status")
        department = kwargs.get("department")
        mfa_enabled = kwargs.get("mfa_enabled")

        # Locate user
        user = next((u for u in users if u["user_id"] == user_id), None)
        if not user:
            return json.dumps({"error": f"User {user_id} not found"}, indent=2)

        # Update details
        if new_status:
            user["status"] = new_status
            if new_status in ["SUSPENDED", "DISABLED"]:
                for s in sessions:
                    if s["user_id"] == user_id and s.get("end_time") is None:
                        s["end_time"] = "2025-08-11 13:00:00+00:00"
        if department:
            user["department"] = department
        if mfa_enabled is not None:
            user["mfa_enabled"] = mfa_enabled

        # Audit
        log_id = f"L-{len(audit_logs) + 1:03d}"
        audit_logs.append({
            "log_id": log_id,
            "actor_id": kwargs.get("updated_by"),
            "action_type": "USER_UPDATED",
            "target_id": user_id,
            "timestamp": "2025-08-11 13:00:00+00:00",
            "details": "User status/attributes updated"
        })

        return json.dumps({"success": f"User {user_id} updated"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_status",
                "description": "Update a user's status/department/MFA. Terminates sessions if suspended/disabled.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "status": {"type": "string"},
                        "department": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"},
                        "updated_by": {"type": "string"}
                    },
                    "required": ["user_id", "updated_by"]
                }
            }
        }

# ---------- 35 ----------
class EscalateSiemAlertTool(Tool):
    """Escalate the severity of a SIEM alert and optionally create an incident ticket."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alerts = data.get("siem_alerts", [])

        alert_id = kwargs.get("alert_id")
        new_severity = kwargs.get("severity")
        reason = kwargs.get("reason")

        alert = next((a for a in alerts if a["alert_id"] == alert_id), None)
        if not alert:
            return json.dumps({"error": f"Alert {alert_id} not found"}, indent=2)

        severity_order = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

        # Robustly check severity value before using .index()
        if not new_severity or new_severity not in severity_order:
            return json.dumps({"error": "Invalid severity level"}, indent=2)
        if alert["severity"] not in severity_order:
            return json.dumps({"error": "Existing severity value invalid"}, indent=2)
        if severity_order.index(new_severity) <= severity_order.index(alert["severity"]):
            return json.dumps({"error": "Only escalation permitted"}, indent=2)

        alert["severity"] = new_severity

        return json.dumps({"success": f"Alert {alert_id} escalated to {new_severity}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "escalate_siem_alert",
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
            }
        }

# ---------- 36 ----------
class SearchSlackMessagesTool(Tool):
    """Search Slack messages by channel, user, time range, keywords, regex, or thread context."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        messages = data.get("slack_messages", [])
        channel = kwargs.get("channel")
        username = kwargs.get("username")
        start_time = kwargs.get("start_time")
        end_time = kwargs.get("end_time")
        keywords = kwargs.get("keywords", [])
        regex = kwargs.get("regex")
        thread_id = kwargs.get("thread_id")
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
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_slack_messages",
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
                        "thread_id": {"type": "string"}
                    }
                }
            }
        }

# ---------- 37 ----------
class ModerateSlackChannelTool(Tool):
    """Moderate Slack channel: archive, pin, unpin, or move canonical messages (bulk support)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        messages = data.get("slack_messages", [])
        channel = kwargs.get("channel")
        action = kwargs.get("action")  # "archive", "pin", "unpin", "move"
        message_ids = kwargs.get("message_ids", [])
        target_channel = kwargs.get("target_channel")
        moderator_id = kwargs.get("moderator_id")

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
        return json.dumps(status, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "moderate_slack_channel",
                "description": "Archive, pin, unpin, or move canonical Slack messages with proper RBAC moderation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {"type": "string"},
                        "action": {"type": "string", "enum": ["archive", "pin", "unpin", "move"]},
                        "message_ids": {"type": "array", "items": {"type": "string"}},
                        "target_channel": {"type": "string"},
                        "moderator_id": {"type": "string"}
                    },
                    "required": ["channel", "action", "message_ids", "moderator_id"]
                }
            }
        }

# ---------- 38 ----------
class CreateIncidentRecordTool(Tool):
    """Create a new incident record for tracking security or operational events."""

    @staticmethod
    def invoke(data, **kwargs):
        incident_id = f"INC-{len(data.get('incidents', [])) + 1:03d}"
        record = {
            "incident_id": incident_id,
            "timestamp": kwargs["timestamp"],
            "created_by": kwargs["created_by"],
            "summary": kwargs["summary"],
            "linked_alerts": kwargs.get("linked_alerts", []),
            "linked_users": kwargs.get("linked_users", []),
            "linked_resources": kwargs.get("linked_resources", []),
            "status": "OPEN"
        }
        data.setdefault("incidents", []).append(record)

        return json.dumps(
            {
                "success": f"Incident {incident_id} created",
                "incident_id": incident_id
            },
            indent=2
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_incident_record",
                "description": "Create a new incident record with linked alerts, users, and resources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {"type": "string", "description": "ISO 8601 UTC timestamp."},
                        "created_by": {"type": "string", "description": "user_id of creator."},
                        "summary": {"type": "string", "description": "Brief summary of the incident."},
                        "linked_alerts": {"type": "array", "items": {"type": "string"}},
                        "linked_users": {"type": "array", "items": {"type": "string"}},
                        "linked_resources": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["timestamp", "created_by", "summary"]
                }
            }
        }




class CreateAuditLogTool(Tool):
    """Create an immutable, deterministic audit log entry."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Required fields
        actor_id = kwargs.get("actor_id")
        action_type = kwargs.get("action_type")
        target_id = kwargs.get("target_id")
        timestamp = kwargs.get("timestamp")
        details = kwargs.get("details")

        # Generate log_id deterministically (e.g., sequential or hash of inputs)
        logs = data.get("audit_logs", [])
        next_id = f"L-{len(logs) + 1:03d}"

        log = {
            "log_id": next_id,
            "actor_id": actor_id,
            "action_type": action_type,
            "target_id": target_id,
            "timestamp": timestamp,
            "details": details
        }
        logs.append(log)
        data["audit_logs"] = logs
        return json.dumps(log, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_audit_log",
                "description": "Create a deterministic, immutable audit log entry in the audit_logs table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {
                            "type": "string",
                            "description": "User ID performing the action"
                        },
                        "action_type": {
                            "type": "string",
                            "description": "Type of action performed (e.g. ROLE_REVOKED, ACCESS_GRANTED, POLICY_EXCEPTION_REQUESTED)"
                        },
                        "target_id": {
                            "type": "string",
                            "description": "ID of the affected entity (role, resource, user, or policy exception ID)"
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "Deterministic ISO8601 UTC timestamp"
                        },
                        "details": {
                            "type": "string",
                            "description": "Deterministic, canonical event description"
                        }
                    },
                    "required": [
                        "actor_id",
                        "action_type",
                        "target_id",
                        "timestamp",
                        "details"
                    ]
                }
            }
        }



class SendEmailTool(Tool):
    """Send an email from a deterministic sender to a receiver, logging the event for compliance."""

    @staticmethod
    def invoke(data, **kwargs):
        sender = kwargs["sender"]        # user_id of sender
        receiver = kwargs["receiver"]    # user_id of receiver
        subject = kwargs["subject"]
        body = kwargs["body"]
        timestamp = kwargs["timestamp"]

        # Validate sender exists
        sender_user = next((u for u in data.get("users", []) if u.get("user_id") == sender), None)
        if not sender_user:
            return json.dumps({"error": f"Sender '{sender}' not found in users.json."}, indent=2)

        # Validate receiver exists
        receiver_user = next((u for u in data.get("users", []) if u.get("user_id") == receiver), None)
        if not receiver_user:
            return json.dumps({"error": f"Receiver '{receiver}' not found in users.json."}, indent=2)

        # Receiver must be ACTIVE or PENDING_ACCESS
        if receiver_user.get("status") not in ("ACTIVE", "PENDING_ACCESS"):
            return json.dumps(
                {"error": f"Receiver '{receiver}' has status '{receiver_user.get('status')}', not allowed."},
                indent=2
            )

        # Validate subject/body
        if not isinstance(subject, str) or not subject.strip():
            return json.dumps({"error": "Subject must be a non-empty string."}, indent=2)
        if not isinstance(body, str) or not body.strip():
            return json.dumps({"error": "Body must be a non-empty string."}, indent=2)

        # Append to emails.json
        emails = data.setdefault("emails", [])
        email_id = f"EM-{len(emails) + 1:03d}"
        record = {
            "email_id": email_id,
            "timestamp": timestamp,
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "text_content": body
        }
        emails.append(record)

        return json.dumps(
            {
                "success": f"Email {email_id} sent to {receiver}",
                "email_id": email_id
            },
            indent=2
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "send_email",
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
                            "description": "Sender's user_id (must exist in users.json)."
                        },
                        "receiver": {
                            "type": "string",
                            "description": "Receiver's user_id (must be ACTIVE or PENDING_ACCESS)."
                        },
                        "subject": {
                            "type": "string",
                            "description": "Email subject, policy/compliance driven."
                        },
                        "body": {
                            "type": "string",
                            "description": "Email body text, deterministic."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO 8601 UTC timestamp, deterministic."
                        }
                    },
                    "required": ["sender", "receiver", "subject", "body", "timestamp"]
                }
            }
        }


class GetAccessRequestTool(Tool):
    """Retrieve a single access request by ID (read-only, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Expect: data["access_requests"] is a list of dicts from /mnt/data/access_requests.json
        access_requests = data.get("access_requests", [])
        if not isinstance(access_requests, list):
            return json.dumps({"error": "access_requests must be a list"}, indent=2)

        request_id = kwargs.get("request_id")
        if not isinstance(request_id, str) or not request_id.strip():
            return json.dumps({"error": "request_id must be a non-empty string"}, indent=2)

        # Read-only lookup
        for row in access_requests:
            if isinstance(row, dict) and row.get("request_id") == request_id:
                return json.dumps({"access_request": row}, indent=2)

        return json.dumps({"error": f"Access request {request_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_access_request",
                "description": "Retrieve a single access request by ID (read-only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "Access request ID, e.g. AR-004"
                        }
                    },
                    "required": ["request_id"],
                },
            },
        }

class PostSlackMessageTool(Tool):
    """Post a new message into a Slack channel (write operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Expect: data["slack_messages"] is a list of dicts from /mnt/data/slack_messages.json
        slack_messages = data.get("slack_messages", [])
        if not isinstance(slack_messages, list):
            return json.dumps({"error": "slack_messages must be a list"}, indent=2)

        channel = kwargs.get("channel")
        message = kwargs.get("message")

        if not isinstance(channel, str) or not channel.strip():
            return json.dumps({"error": "channel must be a non-empty string"}, indent=2)
        if not isinstance(message, str) or not message.strip():
            return json.dumps({"error": "message must be a non-empty string"}, indent=2)

        # Append a new message to the log (mock posting)
        new_entry = {
            "channel": channel,
            "message": message,
        }
        slack_messages.append(new_entry)

        return json.dumps({"success": f"Message posted to {channel}", "message": new_entry}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "post_slack_message",
                "description": "Post a new message into a Slack channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "Slack channel name or ID, e.g. #general"
                        },
                        "message": {
                            "type": "string",
                            "description": "Text content of the message to post"
                        }
                    },
                    "required": ["channel", "message"],
                },
            },
        }

class GetRoleMembersTool(Tool):
    """Return user records for members of a given role (read operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        users = data.get("users", [])
        user_roles = data.get("user_roles", [])

        role_id = kwargs.get("role_id")
        status_filter = kwargs.get("status")  # optional: e.g., "ACTIVE"

        if not isinstance(user_roles, list) or not isinstance(users, list):
            return json.dumps({"error": "users and user_roles must be lists"}, indent=2)
        if not isinstance(role_id, str) or not role_id.strip():
            return json.dumps({"error": "role_id must be a non-empty string"}, indent=2)

        member_user_ids = {ur["user_id"] for ur in user_roles if ur.get("role_id") == role_id}
        results = []
        for u in users:
            if u.get("user_id") in member_user_ids:
                if status_filter and u.get("status") != status_filter:
                    continue
                results.append(u)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_members",
                "description": "List user records for members assigned to a role. Optional filter by user status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string", "description": "The role_id to lookup"},
                        "status": {"type": "string", "description": "Optional user status filter, e.g. ACTIVE"}
                    },
                    "required": ["role_id"]
                },
            },
        }


class AssignCertificationTool(Tool):
    """Create/assign a certification record to a user (write operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certifications = data.get("certifications", [])
        users = data.get("users", [])

        if not isinstance(certifications, list):
            return json.dumps({"error": "certifications must be a list"}, indent=2)
        if not isinstance(users, list):
            return json.dumps({"error": "users must be a list"}, indent=2)

        certification_id = kwargs.get("certification_id")
        user_id = kwargs.get("user_id")
        assigned_on = kwargs.get("assigned_on")  # ISO8601 or similar deterministic string
        status = kwargs.get("status") or "ASSIGNED"

        if not isinstance(certification_id, str) or not certification_id.strip():
            return json.dumps({"error": "certification_id must be a non-empty string"}, indent=2)
        if not isinstance(user_id, str) or not user_id.strip():
            return json.dumps({"error": "user_id must be a non-empty string"}, indent=2)
        if assigned_on is not None and not isinstance(assigned_on, str):
            return json.dumps({"error": "assigned_on must be a string if provided"}, indent=2)
        if not isinstance(status, str) or not status.strip():
            return json.dumps({"error": "status must be a non-empty string"}, indent=2)

        # Validate user exists
        user = next((u for u in users if u.get("user_id") == user_id), None)
        if not user:
            return json.dumps({"error": f"user_id {user_id} not found in users"}, indent=2)

        # Ensure certification_id is unique
        if any(c.get("certification_id") == certification_id for c in certifications):
            return json.dumps({"error": f"certification_id {certification_id} already exists"}, indent=2)

        # Append minimal, schema-safe record using only known field names from datasets
        new_record = {
            "certification_id": certification_id,
            "user_id": user_id,
            "status": status,
        }
        if assigned_on:
            new_record["assigned_on"] = assigned_on  # field name exists in project datasets (e.g., user_roles)

        certifications.append(new_record)
        return json.dumps(
            {"success": f"Certification {certification_id} assigned to user {user_id}", "certification": new_record},
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_certification",
                "description": "Create/assign a certification record to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string", "description": "Unique certification identifier"},
                        "user_id": {"type": "string", "description": "Target user_id"},
                        "assigned_on": {"type": "string", "description": "Deterministic assignment timestamp"},
                        "status": {"type": "string", "description": "Initial status (defaults to ASSIGNED)"}
                    },
                    "required": ["certification_id", "user_id"]
                },
            },
        }


class RevokeCertificationTool(Tool):
    """Revoke an existing certification from a user (write operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certifications = data.get("certifications", [])
        if not isinstance(certifications, list):
            return json.dumps({"error": "certifications must be a list"}, indent=2)

        certification_id = kwargs.get("certification_id")
        # Optional timestamp field name chosen from existing datasets; avoids inventing new keys
        expires_on = kwargs.get("expires_on")

        if not isinstance(certification_id, str) or not certification_id.strip():
            return json.dumps({"error": "certification_id must be a non-empty string"}, indent=2)
        if expires_on is not None and not isinstance(expires_on, str):
            return json.dumps({"error": "expires_on must be a string if provided"}, indent=2)

        cert = next((c for c in certifications if c.get("certification_id") == certification_id), None)
        if not cert:
            return json.dumps({"error": f"Certification {certification_id} not found"}, indent=2)

        cert["status"] = "REVOKED"
        # Clear completion if present
        if "completed_on" in cert:
            cert["completed_on"] = None
        # Optionally stamp an end marker using an existing field name used in other datasets
        if expires_on:
            cert["expires_on"] = expires_on

        return json.dumps({"success": f"Certification {certification_id} revoked"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_certification",
                "description": "Revoke a certification by certification_id; clears completed_on and can set expires_on.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"},
                        "expires_on": {"type": "string", "description": "Optional deterministic end timestamp"}
                    },
                    "required": ["certification_id"]
                },
            },
        }


class LinkAlertToIncidentTool(Tool):
    """Link an existing SIEM alert to an incident record (write operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        incidents = data.get("incidents", [])
        alerts = data.get("siem_alerts", [])

        if not isinstance(incidents, list):
            return json.dumps({"error": "incidents must be a list"}, indent=2)
        if not isinstance(alerts, list):
            return json.dumps({"error": "siem_alerts must be a list"}, indent=2)

        incident_id = kwargs.get("incident_id")
        alert_id = kwargs.get("alert_id")

        if not isinstance(incident_id, str) or not incident_id.strip():
            return json.dumps({"error": "incident_id must be a non-empty string"}, indent=2)
        if not isinstance(alert_id, str) or not alert_id.strip():
            return json.dumps({"error": "alert_id must be a non-empty string"}, indent=2)

        incident = next((i for i in incidents if i.get("incident_id") == incident_id), None)
        if not incident:
            return json.dumps({"error": f"Incident {incident_id} not found"}, indent=2)

        alert = next((a for a in alerts if a.get("alert_id") == alert_id), None)
        if not alert:
            return json.dumps({"error": f"Alert {alert_id} not found"}, indent=2)

        linked = incident.setdefault("linked_alerts", [])
        if alert_id not in linked:
            linked.append(alert_id)

        return json.dumps(
            {"success": f"Linked alert {alert_id} to incident {incident_id}",
             "incident_id": incident_id,
             "alert_id": alert_id},
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_alert_to_incident",
                "description": "Append an alert_id to an incident's linked_alerts after validating existence.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "incident_id": {"type": "string"},
                        "alert_id": {"type": "string"}
                    },
                    "required": ["incident_id", "alert_id"]
                },
            },
        }



class ListCertificationsForReviewerTool(Tool):
    """List all certifications assigned to a given reviewer (read operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        reviewer_id = kwargs.get("reviewer_id")
        certifications = data.get("certifications", [])
        if not isinstance(certifications, list):
            return json.dumps({"error": "certifications must be a list"}, indent=2)

        if not isinstance(reviewer_id, str) or not reviewer_id.strip():
            return json.dumps({"error": "reviewer_id must be a non-empty string"}, indent=2)

        results = [c for c in certifications if c.get("reviewer_id") == reviewer_id]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_certifications_for_reviewer",
                "description": "List all certifications assigned to a specific reviewer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reviewer_id": {"type": "string", "description": "The reviewer’s user_id"}
                    },
                    "required": ["reviewer_id"]
                }
            }
        }



class GetTicketDetailsTool(Tool):
    """Retrieve a HubSpot ticket by ticket_id (read-only, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get("ticket_id")
        tickets = data.get("hubspot_tickets", [])
        if not isinstance(tickets, list):
            return json.dumps({"error": "hubspot_tickets must be a list"}, indent=2)

        if not isinstance(ticket_id, str) or not ticket_id.strip():
            return json.dumps({"error": "ticket_id must be a non-empty string"}, indent=2)

        for t in tickets:
            if t.get("ticket_id") == ticket_id:
                return json.dumps(t, indent=2)

        return json.dumps({"error": f"ticket_id {ticket_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_ticket_details",
                "description": "Retrieve details of a HubSpot ticket by ticket_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"}
                    },
                    "required": ["ticket_id"]
                }
            }
        }



class GetAuditLogsForTargetTool(Tool):
    """Get audit logs filtered by target_id (read-only, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target_id = kwargs.get("target_id")
        audit_logs = data.get("audit_logs", [])
        if not isinstance(audit_logs, list):
            return json.dumps({"error": "audit_logs must be a list"}, indent=2)

        if not isinstance(target_id, str) or not target_id.strip():
            return json.dumps({"error": "target_id must be a non-empty string"}, indent=2)

        results = [log for log in audit_logs if log.get("target_id") == target_id]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_audit_logs_for_target",
                "description": "Retrieve audit logs filtered by target_id (user, resource, role, alert, etc.).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_id": {"type": "string", "description": "The target entity ID (e.g., U-001, RES-021, ALRT-003)"}
                    },
                    "required": ["target_id"]
                }
            }
        }



class GetSiemAlertTool(Tool):
    """Retrieve details of a specific SIEM alert (read-only, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alert_id = kwargs.get("alert_id")
        alerts = data.get("siem_alerts", [])
        if not isinstance(alerts, list):
            return json.dumps({"error": "siem_alerts must be a list"}, indent=2)

        if not isinstance(alert_id, str) or not alert_id.strip():
            return json.dumps({"error": "alert_id must be a non-empty string"}, indent=2)

        for a in alerts:
            if a.get("alert_id") == alert_id:
                return json.dumps(a, indent=2)

        return json.dumps({"error": f"alert_id {alert_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_siem_alert",
                "description": "Retrieve SIEM alert details by alert_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string"}
                    },
                    "required": ["alert_id"]
                }
            }
        }


class ListUserSessionsTool(Tool):
    """List sessions for a specific user with optional active-only filter (read operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sessions = data.get("sessions", [])
        if not isinstance(sessions, list):
            return json.dumps({"error": "sessions must be a list"}, indent=2)

        user_id = kwargs.get("user_id")
        active_only = kwargs.get("active_only", False)

        if not isinstance(user_id, str) or not user_id.strip():
            return json.dumps({"error": "user_id must be a non-empty string"}, indent=2)

        if active_only not in (True, False):
            return json.dumps({"error": "active_only must be a boolean if provided"}, indent=2)

        results = []
        for s in sessions:
            if s.get("user_id") != user_id:
                continue
            if active_only and s.get("end_time") is not None:
                continue
            results.append(s)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_user_sessions",
                "description": "List sessions for a user; optionally filter to only active sessions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id"},
                        "active_only": {"type": "boolean", "description": "If true, only return sessions without end_time"}
                    },
                    "required": ["user_id"]
                }
            }
        }


class AssignRoleToUserTool(Tool):
    """Assign a role to a user (write operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_roles = data.get("user_roles", [])
        users = data.get("users", [])
        roles = data.get("roles", [])
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


class ListPermissionsForRoleTool(Tool):
    """List permissions bound to a role_id (read operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_permissions = data.get("role_permissions", [])
        permissions = data.get("permissions", [])
        if not isinstance(role_permissions, list):
            return json.dumps({"error": "role_permissions must be a list"}, indent=2)
        if not isinstance(permissions, list):
            return json.dumps({"error": "permissions must be a list"}, indent=2)

        role_id = kwargs.get("role_id")
        roles = data.get("roles", [])
        if not any(r.get("role_id")==role_id for r in roles):
            return json.dumps({"error": f"role_id {role_id} not found"}, indent=2)
        if not isinstance(role_id, str) or not role_id.strip():
            return json.dumps({"error": "role_id must be a non-empty string"}, indent=2)

        perm_ids = [rp.get("permission_id") for rp in role_permissions if rp.get("role_id") == role_id]
        results = [p for p in permissions if p.get("permission_id") in perm_ids]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_permissions_for_role",
                "description": "List permission records attached to the given role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string"}
                    },
                    "required": ["role_id"]
                }
            }
        }


class GetCertificationTool(Tool):
    """Return a single certification record by certification_id (read operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certifications = data.get("certifications", [])
        if not isinstance(certifications, list):
            return json.dumps({"error": "certifications must be a list"}, indent=2)

        certification_id = kwargs.get("certification_id")
        if not isinstance(certification_id, str) or not certification_id.strip():
            return json.dumps({"error": "certification_id must be a non-empty string"}, indent=2)

        for c in certifications:
            if c.get("certification_id") == certification_id:
                return json.dumps(c, indent=2)
        return json.dumps({"error": f"Certification {certification_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_certification",
                "description": "Retrieve a certification by certification_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"}
                    },
                    "required": ["certification_id"]
                }
            }
        }


class RemoveRoleFromUserTool(Tool):
    """Remove a specific role assignment from a user (write operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_roles = data.get("user_roles", [])
        if not isinstance(user_roles, list):
            return json.dumps({"error": "user_roles must be a list"}, indent=2)

        user_id = kwargs.get("user_id")
        role_id = kwargs.get("role_id")

        for fld, val in [("user_id", user_id), ("role_id", role_id)]:
            if not isinstance(val, str) or not val.strip():
                return json.dumps({"error": f"{fld} must be a non-empty string"}, indent=2)

        before = len(user_roles)
        data["user_roles"] = [ur for ur in user_roles if not (ur.get("user_id") == user_id and ur.get("role_id") == role_id)]
        removed = before - len(data["user_roles"])

        if removed == 0:
            return json.dumps({"error": f"No assignment of {role_id} found for {user_id}"}, indent=2)
        return json.dumps({"success": f"Removed {removed} assignment(s) of {role_id} from {user_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_role_from_user",
                "description": "Remove a role assignment for a user. Deletes matching rows from user_roles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"}
                    },
                    "required": ["user_id", "role_id"]
                }
            }
        }


class UpdateTicketStatusTool(Tool):
    """Update the status of a HubSpot ticket (write operation)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tickets = data.get("hubspot_tickets", [])
        ticket_id = kwargs.get("ticket_id")
        new_status = kwargs.get("status")
        updated_at = kwargs.get("updated_at")

        if not isinstance(ticket_id, str):
            return json.dumps({"error": "ticket_id must be provided"}, indent=2)
        if not isinstance(new_status, str):
            return json.dumps({"error": "status must be provided"}, indent=2)

        for t in tickets:
            if t.get("ticket_id") == ticket_id:
                t["status"] = new_status
                if updated_at:
                    t["updated_at"] = updated_at
                return json.dumps({"success": f"Ticket {ticket_id} updated", "ticket": t}, indent=2)

        return json.dumps({"error": f"Ticket {ticket_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_ticket_status",
                "description": "Update the status of a HubSpot ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string", "description": "Unique ID of the ticket"},
                        "status": {"type": "string", "description": "New status of the ticket (e.g., OPEN, CLOSED, IN_PROGRESS)"},
                        "updated_at": {"type": "string", "description": "Optional ISO8601 timestamp of the update"}
                    },
                    "required": ["ticket_id", "status"]
                }
            }
        }


class UpdateCertificationStatusTool(Tool):
    """Update the status of a certification review (write operation)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certs = data.get("certifications", [])
        cert_id = kwargs.get("certification_id")
        new_status = kwargs.get("status")
        completed_on = kwargs.get("completed_on")

        if not isinstance(cert_id, str):
            return json.dumps({"error": "certification_id must be provided"}, indent=2)
        if not isinstance(new_status, str):
            return json.dumps({"error": "status must be provided"}, indent=2)

        for c in certs:
            if c.get("certification_id") == cert_id:
                c["status"] = new_status
                if completed_on:
                    c["completed_on"] = completed_on
                return json.dumps({"success": f"Certification {cert_id} updated", "certification": c}, indent=2)

        return json.dumps({"error": f"Certification {cert_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_certification_status",
                "description": "Update the status of a certification review.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string", "description": "Unique ID of the certification"},
                        "status": {"type": "string", "description": "New status (e.g., PENDING, IN_PROGRESS, COMPLETED)"},
                        "completed_on": {"type": "string", "description": "Optional ISO8601 timestamp when completed"}
                    },
                    "required": ["certification_id", "status"]
                }
            }
        }


class EnableUserMFATool(Tool):
    """Enable MFA for a given user (write operation)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        users = data.get("users", [])
        user_id = kwargs.get("user_id")

        if not isinstance(user_id, str):
            return json.dumps({"error": "user_id must be provided"}, indent=2)

        for u in users:
            if u.get("user_id") == user_id:
                u["mfa_enabled"] = True
                return json.dumps({"success": f"MFA enabled for {user_id}", "user": u}, indent=2)

        return json.dumps({"error": f"User {user_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "enable_user_mfa",
                "description": "Enable MFA for a given user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to enable MFA for"}
                    },
                    "required": ["user_id"]
                }
            }
        }


import json
from typing import Dict, Any

class UpdateAccessRequestTool(Tool):
    """Basic: update an access request's status and metadata (no side effects)."""

    _ALLOWED = {"PENDING", "APPROVED", "REJECTED", "DEFERRED"}

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        status = kwargs.get("status")
        updated_on = kwargs.get("updated_on")
        updated_by = kwargs.get("updated_by")

        # Required parameters
        missing = [k for k in ("request_id","status","updated_on","updated_by") if kwargs.get(k) is None]
        if missing:
            return json.dumps({"error": f"Missing: {', '.join(missing)}"}, indent=2)

        # Basic status check
        if status not in UpdateAccessRequestTool._ALLOWED:
            return json.dumps({"error": f"Invalid status '{status}'. Allowed: {sorted(UpdateAccessRequestTool._ALLOWED)}"}, indent=2)

        # Load tables
        access_requests = data.get("access_requests", [])
        users = data.get("users", [])

        # Anchors
        req = next((r for r in access_requests if r.get("request_id") == request_id), None)
        if not req:
            return json.dumps({"error": f"Unknown request_id '{request_id}'"}, indent=2)

        if not any(u.get("user_id") == updated_by for u in users):
            return json.dumps({"error": f"Unknown updated_by '{updated_by}'"}, indent=2)

        # Update in place (basic)
        req["status"] = status
        req["updated_on"] = updated_on
        req["updated_by"] = updated_by

        return json.dumps(req, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_access_request",
                "description": "Basic update of an access request's status and metadata (no side effects).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string", "description": "e.g., AR-007"},
                        "status": {"type": "string", "enum": ["PENDING","APPROVED","REJECTED","DEFERRED"]},
                        "updated_on": {"type": "string", "description": "ISO 8601 timestamp"},
                        "updated_by": {"type": "string", "description": "User ID performing the update"}
                    },
                    "required": ["request_id","status","updated_on","updated_by"]
                }
            }
        }



class ExportAuditLogsTool(Tool):
    """Export audit logs with optional filters."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        actor_id = kwargs.get("actor_id")
        action_type = kwargs.get("action_type")
        target_id = kwargs.get("target_id")
        start_time = kwargs.get("start_time")
        end_time = kwargs.get("end_time")

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

        # Deterministic export format (JSON string list of logs)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "export_audit_logs",
                "description": "Export audit logs with optional filters for actor, action, target, and time range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {"type": "string"},
                        "action_type": {"type": "string"},
                        "target_id": {"type": "string"},
                        "start_time": {"type": "string", "description": "ISO8601 lower bound"},
                        "end_time": {"type": "string", "description": "ISO8601 upper bound"}
                    }
                }
            }
        }

class GetCurrentTimeTool(Tool):
    """
    Returns the fixed canonical current time used in evaluation.
    """

    @staticmethod
    def invoke(data: dict, **kwargs) -> str:
        # always return the same canonical time
        return json.dumps({"current_time": "2025-08-17T00:00:00Z"})

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Return the canonical current time for use in audit logs and decisions.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
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
    UpdateAccessRequestTool()
]
