# domains/rbac/variations/variation_4/rules.py

"""
GLOBAL WORKFLOW RULESET FOR RBAC VARIATION 4

All tasks, API invocations, and Assistant actions must follow these rules.
These enforce user, privilege, departmental, and resource constraints as codified
in the dataset for all operational, compliance, SIEM, and exception management workflows.

The policy must be referenced by any agentic workflow, and non-compliance invalidates the task.
"""

RULES = [
    "New approvals, assignments, or workflow actions may only involve users whose 'status' is either 'ACTIVE' or 'PENDING_ACCESS'.",
    "Users with a 'DISABLED' or 'SUSPENDED' status are ineligible for any operation, including approval, assignment, exception, certification, completion, session, or alert.",
    "To act as a reviewer or approver, an individual must have an 'ACTIVE' status, be part of a department associated with the resource (see below), and must not be the requesting user unless the dataset specifically supports self-service.",
    "Task parameters are required to utilize canonical values for user_id, role_id, resource_id, and permission_id as defined in the dataset; the use of names, emails, or nicknames is not allowed.",
    "Prior to performing any revoke_role operation, you must first call GetUserRole (or GetUserDetails if it provides current roles) to verify that the user presently possesses the specified role. A user may not be assigned the same role_id more than once at the same time. If the user already has the role (where expiry is null or expiry is set to a future date), additional assignments are not permitted.",
    "Role assignments for a specific resource must align with valid records in both roles.json and role_permissions.json, and the permissions granted must be consistent with the policy scope defined for the resource.",
    "Only users with 'mfa_enabled' == true are eligible to be approved for or assigned roles that grant access to resources where 'criticality' == 'CRITICAL'.",
    "When assigning, 'assigned_by' and 'assigned_on' must be set deterministically using the values provided in the task, and 'expires_on' must be set according to the workflow specification; random timestamps are not permitted.",
    "Approval or rejection of access requests is permitted exclusively when their status in access_requests.json is 'PENDING'.",
    "An approval cannot allocate any role other than the 'requested_role_id' specified in the access_request record.",
    "The reviewer (reviewed_by) is required to be an ACTIVE user and must either be the resource_owner or belong to the same department as the resource_owner (as defined in resources.json), except when the dataset explicitly models escalation.",
    "Both rejects and approvals modify the 'status' and review fields (reviewed_by, decision_at) strictly according to the defined action sequence.",
    "Approving or denying exceptions is permitted solely for those with a status of 'PENDING_REVIEW', while expiring exceptions is allowed only for those with a status of 'ACTIVE'.",
    "When approving an exception, the fields 'reviewed_by', 'reviewed_on', and 'expires_on' must be set precisely to the values specified in the task actions.",
    "A reviewer is not allowed to approve their own exception unless the dataset explicitly allows for self-approval.",
    "Exceptions that reference permission_ids or user_ids absent from the dataset are considered invalid and should not be processed.",
    "Certification completion is allowed exclusively when the status is either 'PENDING' or 'IN_PROGRESS', and the reviewer must correspond to the reviewer_id specified in certifications.json.",
    "For completed certifications, both 'completed_on' and 'status' must be updated precisely according to the task specifications.",
    "Sessions are eligible for termination solely if their 'end_time' is null, and the session's 'user_id' corresponds to an ACTIVE user.",
    "When terminating a session, 'end_time' must be assigned precisely the value specified by the workflow action.",
    "A user is not allowed to terminate a session belonging to another user unless the workflow indicates administrative intervention and such action is authorized within the dataset.",
    "Investigation records for SIEM alerts can be created solely by an ACTIVE user, and exclusively for alert_ids that exist in siem_alerts.json.",
    "When creating SIEM rules or investigations, every field (created_by, conditions, notes, investigated_on) must be assigned the exact deterministic values provided within the workflow.",
    "The creation of new SIEM alerts is restricted to workflow steps that are explicitly defined within tasks; no SIEM alerts may be generated elsewhere.",
]
