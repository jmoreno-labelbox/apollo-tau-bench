# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








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
    def invoke(data: Dict[str, Any], request_id, reviewer_id) -> str:
        if not request_id or not reviewer_id:
            return json.dumps(
                {"error": "request_id and reviewer_id are required"}, indent=2
            )

        # Assess the policy utilizing current logic.
        decision_raw = json.loads(
            CheckUserStatusTool.invoke(data, request_id=request_id)
        )
        if "error" in decision_raw:
            return json.dumps(decision_raw, indent=2)

        approve = bool(decision_raw.get("approve"))
        notes = decision_raw.get("notes")

        # Log decision in the audit trail.
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

        # If granted, assign the role in an idempotent manner.
        assignment_info = None
        if approve:
            assignment_info = json.loads(
                AssignRoleOnApprovalTool.invoke(
                    data, request_id=request_id, assigned_by=reviewer_id
                )
            )

        # Gather the final state of the requester.
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