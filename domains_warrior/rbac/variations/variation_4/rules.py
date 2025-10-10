# domains/rbac/variations/variation_4/rules.py

"""
GLOBAL WORKFLOW RULESET FOR RBAC VARIATION 4

All tasks, API invocations, and Assistant actions must follow these rules.
These enforce user, privilege, departmental, and resource constraints as codified
in the dataset for all operational, compliance, SIEM, and exception management workflows.

The policy must be referenced by any agentic workflow, and non-compliance invalidates the task.
"""

RULES = [

    # USER ACTIVATION & STATUS
    "Only users with 'status' == 'ACTIVE' or 'PENDING_ACCESS' may be subjects of new approvals, assignments, or workflow actions.",
    "No operation (approval/assignment/exception/certification/completion/session/alert) can be performed on users with 'DISABLED' or 'SUSPENDED' status.",
    "A reviewer or approver must have status 'ACTIVE', belong to a department relevant to the resource (see below), and cannot be the same as the requesting user unless the dataset explicitly models self-service.",
    "Task parameters must use canonical user_id, role_id, resource_id, and permission_id values from the dataset; use of names, emails, or nicknames is prohibited.",

    # ROLE/PERMISSION ASSIGNMENT
    "Before executing any revoke_role action, first use get_user_roles (or get_user_details if it returns current roles) to confirm the user currently holds the role in question."
    "A user cannot be assigned the same role_id more than once concurrently. If a user already holds the role (with expiry == null or expiry in the future), further assignments are prohibited.",
    "Assignments to roles for a given resource must correspond to valid entries in both roles.json and role_permissions.json, and the permissions conveyed must match the resource's policy scope.",
    "Roles that confer access to resources with 'criticality' == 'CRITICAL' can only be approved or assigned for users with 'mfa_enabled' == true.",
    "Assignment must set 'assigned_by', 'assigned_on' deterministically (supplied in task), and 'expires_on' as specified in the workflow. No random timestamps are allowed.",

    # ACCESS REQUESTS
    "Access requests are only eligible for approval or rejection if their status is 'PENDING' in access_requests.json.",
    "An approval must not assign a role different from 'requested_role_id' in the access_request record.",
    "The reviewer (reviewed_by) must be an ACTIVE user and must belong either to the same department as resource_owner or be resource_owner (from resources.json), unless the dataset models explicit escalation.",
    "Rejects and approvals update 'status' and review fields (reviewed_by, decision_at) deterministically only as per the action sequence.",

    # POLICY EXCEPTION MANAGEMENT
    "Only exceptions with status 'PENDING_REVIEW' may be approved or denied, and only exceptions with status 'ACTIVE' may be expired.",
    "Exception approval must set 'reviewed_by', 'reviewed_on', and 'expires_on' exactly as given in the task actions.",
    "Reviewer cannot be the requester for their own exception unless dataset explicitly models self-approval.",
    "Exceptions referencing permission_ids or user_ids not present in the dataset are invalid and must not be processed.",

    # CERTIFICATIONS
    "Certification completion is only permitted for statuses 'PENDING' or 'IN_PROGRESS'. The reviewer must match reviewer_id in certifications.json.",
    "Completed certifications must update 'completed_on' and 'status' exactly as specified in the task.",

    # SESSIONS
    "Only sessions where 'end_time' is null may be terminated. A session's 'user_id' must match an ACTIVE user.",
    "Session termination must set 'end_time' exactly to the value provided in the workflow action.",
    "No user may terminate another user's session unless the workflow represents administrative intervention and is permitted in the dataset.",

    # SIEM ALERTS & INVESTIGATIONS
    "Only an ACTIVE user may create investigation records for SIEM alerts, and only for alert_ids present in siem_alerts.json.",
    "SIEM rule creation and investigations must set all fields (created_by, conditions, notes, investigated_on) to the fixed deterministic values supplied in the workflow.",
    "No new SIEM alerts may be created outside workflow steps explicitly modeled in tasks."

]
