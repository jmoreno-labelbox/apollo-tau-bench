from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
        roles = data.get("roles", {}).values()
        admin_like = set()
        for r in roles.values():
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
            for rp in data.get("role_permissions", {}).values()
            if rp.get("role_id") == role_id
        ]

        for perm_id in role_permissions:
            permission = next(
                (
                    p
                    for p in data.get("permissions", {}).values()
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
                for cert in data.get("certifications", {}).values()
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
        certs = data.get("certifications", {}).values()
        required = []
        if role_id:
            required = [c for c in certs.values() if c.get("role_id") == role_id]
        if not required and role_permissions_resource_ids:
            required = [
                c
                for c in certs.values() if c.get("resource_id") in role_permissions_resource_ids
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
            for ur in data.get("user_roles", {}).values()
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
            for rp in data.get("role_permissions", {}).values()
            if rp.get("role_id") == role_id
        ]

        #Verify if the user has current policy exceptions for any of these permissions
        for perm_id in role_permissions:
            exception = next(
                (
                    pe
                    for pe in data.get("policy_exceptions", {}).values()
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
                for ur in data.get("user_roles", {}).values()
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
                for rp in data.get("role_permissions", {}).values()
                if rp.get("role_id") == role_id
            ]
            perm_resource_ids = [
                p.get("resource_id")
                for p in data.get("permissions", {}).values()
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
                for r in data.get("access_requests", {}).values()
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
            for ur in data.get("user_roles", {}).values()
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
