# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
        roles = list(data.get("roles", {}).values())
        admin_like = set()
        for r in roles:
            name = (r.get("role_name") or "").lower()
            rid = r.get("role_id")
            if not rid or not name:
                continue
            # Leadership positions: enforce the '-lead' suffix (prevents
            # 'sales-lead-manager' incorrect detection
            if name.endswith("-lead"):
                admin_like.add(rid)
            # Roles with '-admin' in their name.
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
                    for p in list(data.get("permissions", {}).values())
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
        # Obtain permissions for the specified role.
        role_permissions = [
            rp.get("permission_id")
            for rp in data.get("role_permissions", [])
            if rp.get("role_id") == role_id
        ]

        # Verify if the user possesses any active policy exceptions for the specified permissions.
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
    def invoke(data: Dict[str, Any], mode, request_id, resource_id, reviewer_id, role_id, user_id) -> str:
        mode = (mode or "access_request").lower()

        # Branch: cancel assessment
        if mode in ("revoke", "revoke_evaluation"):
            if not user_id or not role_id:
                return json.dumps(
                    {"error": "user_id and role_id are required for revoke evaluation"},
                    indent=2,
                )

            # Check if the assignment is present.
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

            # Identify resource IDs for role permissions.
            role_perm_ids = [
                rp.get("permission_id")
                for rp in data.get("role_permissions", [])
                if rp.get("role_id") == role_id
            ]
            perm_resource_ids = [
                p.get("resource_id")
                for p in list(data.get("permissions", {}).values())
                if p.get("permission_id") in role_perm_ids
            ]

            # Validation of resource coverage (when resource_id is supplied)
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

            # Certification criteria
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

            # Roles similar to admin can be considered for optimization.
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

            # Default: do not cancel
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

        # Verify the status of the request initially (Rule 1)
        if req.get("status") != "PENDING":
            return json.dumps(
                {
                    "error": (
                        f"Access request {request_id} is not PENDING (status: {req.get('status')})"
                    )
                },
                indent=2,
            )

        # Reviewer approval (if given)
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

        # Active roles retrieved from the database.
        current_roles = [
            ur.get("role_id")
            for ur in data.get("user_roles", [])
            if ur.get("user_id") == user_id and not ur.get("expires_on")
        ]

        # Rule 2: repeated request
        if role_id in current_roles:
            approve = False
            notes = "Already assigned."
        else:
            # Verify resource allocation initially (Rule 5)
            if not CheckUserStatusTool._check_resource_coverage(
                data, role_id, resource_id
            ):
                approve = False
                notes = "Requested role does not cover target resource."
            else:
                admin_like_block = CheckUserStatusTool._admin_like_roles(data)

                # Rule 4 (preceding the general admin block): ROL-032 prerequisite
                if role_id == "ROL-032":
                    approve = "ROL-029" in current_roles
                    notes = (
                        "Met prerequisite finance-base (ROL-029)."
                        if approve
                        else "Missing prerequisite finance-base (ROL-029)."
                    )
                # Rule 3: block resembling dynamic admin functionality
                elif role_id in admin_like_block:
                    approve = False
                    notes = "Admin-like role blocked by policy."
                else:
                    # Rule 6: Verify certification criteria
                    has_cert_reqs, all_certs_completed, cert_reviewer_id = (
                        CheckUserStatusTool._check_certifications(
                            data, user_id, resource_id
                        )
                    )

                    if has_cert_reqs and not all_certs_completed:
                        approve = False
                        notes = "Required certification not completed."
                    else:
                        # Rule 7: Verify exceptions to the policy.
                        has_policy_exception = (
                            CheckUserStatusTool._check_policy_exceptions(
                                data, user_id, role_id, resource_id
                            )
                        )

                        if has_policy_exception:
                            approve = True
                            notes = "Policy exception approved."
                        else:
                            # Rule 8: Standard approval accompanied by relevant annotations
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
