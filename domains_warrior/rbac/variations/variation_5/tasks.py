from domains.dto import Action, Task


TASKS = [
    Task(
        annotator="liam",
        user_id="liam_001",
        instruction=(
            "You're lead engineer Alex Johnson. "
            "You must review Brian Taylor's pending access request and approve it. "
            "Then, you must add the requested role to Brian's account."
        ),
        actions=[
            Action(
                name="get_user",
                kwargs={"first_name": "Alex", "last_name": "Johnson"},
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Brian", "last_name": "Taylor"},
            ),
            Action(
                name="get_access_request",
                kwargs={"user_id": "U-013", "status": "PENDING"},
            ),
            Action(
                name="decide_access_request",
                kwargs={
                    "request_id": "AR-020",
                    "reviewer_id": "U-001",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-013",
                    "role_id": "ROL-004",
                    "action": "ADD",
                    "assigned_by": "U-001",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-001",
                    "target_id": "U-013",
                    "details": "Role ROL-004 added to U-013",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ACCESS_GRANTED",
                    "actor_id": "U-001",
                    "target_id": "AR-020",
                    "details": "Access request AR-020 was approved by U-001",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "alex.johnson@taucorp.com",
                    "receiver": "brian.taylor@taucorp.com",
                    "subject": "Access Request APPROVED",
                    "text_content": "Your access request AR-020 has been APPROVED.",
                },
            ),
            Action(
                name="get_access_request",
                kwargs={"request_id": "AR-020"},
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-013",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="check_sod_conflicts",
                kwargs={
                    "user_id": "U-013",
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-013", "assignments": [{"role_id": "ROL-001", "role_name": "engineering-base", "description": "Basic access for engineering staff"}, {"role_id": "ROL-004", "role_name": "engineering-db-schema", "description": "Ability to modify database schemas"}]}',
            '{"ok": true, "user_id": "U-013", "has_sod_conflicts": false, "conflict_count": 0, "conflicts": [], "checked_on": "2025-08-08T12:00:00.000000Z"}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_002",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineer Brian Taylor is changing his last name to Talley and taking leave until EOD September 25th, 2025. "
            "Update his profile and set his account to inactive during leave. "
            "While Brian is on leave, assign Alex Johnson a temporary 'engineering-qa-test' role to support release management."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="is_admin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="get_user", kwargs={"first_name": "Brian", "last_name": "Taylor"}),
            Action(name="get_user", kwargs={"username": "btalley", "allow_missing": True}),
            Action(name="update_user", kwargs={"user_id": "U-013", "last_name": "Talley"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-013",
                    "details": "U-032 updated user U-013 name to Brian Talley; username set to btalley; email set to brian.talley@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#engineering",
                    "message": "User U-013 updated by U-032: username btaylor -> btalley; email set to brian.talley@taucorp.com; name set to Brian Talley.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="update_user", kwargs={"user_id": "U-013", "status": "INACTIVE"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-013",
                    "details": "HR_ONBOARD_BOT changed user U-013 status to INACTIVE",
                },
            ),
            Action(name="get_user", kwargs={"first_name": "Alex", "last_name": "Johnson"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-001", "only_active": True}),
            Action(name="get_role", kwargs={"role_name": "engineering-qa-test"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-001",
                    "role_id": "ROL-005",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-09-25T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-001",
                    "details": "Role ROL-005 added to U-001",
                },
            ),
            Action(name="get_user", kwargs={"username": "btalley"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-001", "only_active": True}),
        ],
        outputs=[
            '{"user_id": "U-013", "username": "btalley", "email": "brian.talley@taucorp.com", "department": "Engineering", "status": "INACTIVE", "mfa_enabled": true}',
            '{"user_id": "U-001", "assignments": [{"role_id": "ROL-001"}, {"role_id": "ROL-034"}, {"role_id": "ROL-005"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_003",
        instruction=(
            "You're lead engineer Alex Johnson. "
            "You must complete the scheduled access certification for the internal-documentation-wiki resource."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Alex", "last_name": "Johnson"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(name="get_resource", kwargs={"name": "internal-documentation-wiki"}),
            Action(
                name="get_certification",
                kwargs={
                    "reviewer_id": "U-001",
                    "status": "PENDING",
                    "resource_id": "RES-006",
                },
            ),
            Action(
                name="list_users_with_access_to_resource",
                kwargs={"resource_id": "RES-006", "include_role_details": True},
            ),
            Action(
                name="complete_certification",
                kwargs={"certification_id": "C-014", "reviewer_id": "U-001"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "CERTIFICATION_COMPLETED",
                    "actor_id": "U-001",
                    "target_id": "C-014",
                    "details": "Certification C-014 for RES-006 was completed",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#certifications",
                    "message": "C-014 for RES-006 completed by U-001.",
                },
            ),
        ],
        outputs=[
            '{"ok": true, "certification": {"certification_id": "C-014", "reviewer_id": "U-001", "resource_id": "RES-006", "status": "COMPLETED", "due_date": "2025-11-16 04:59:59+00:00", "completed_on": "2025-08-08T12:00:00.000000Z"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_004",
        instruction=(
            "You are RBAC_BOT. Operations manager Michael Davis has approved Jeffery Green's urgent policy exception request for production server access. "
            "You must update the policy exception request accordingly."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jeffery", "last_name": "Green"}
            ),
            Action(name="get_policy_exception", kwargs={"user_id": "U-023"}),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-012"}),
            Action(name="get_permission", kwargs={"permission_id": "P-089"}),
            Action(
                name="decide_policy_exception",
                kwargs={
                    "exception_id": "PE-012",
                    "reviewer_id": "U-005",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_APPROVED",
                    "actor_id": "U-005",
                    "target_id": "PE-012",
                    "details": "U-005 approved exception PE-012",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-012 approved by U-005",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "rbac@taucorp.com",
                    "receiver": "jeffery.green@taucorp.com",
                    "subject": "Policy Exception APPROVED",
                    "text_content": "Your policy exception request PE-012 has been APPROVED.",
                },
            ),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-012", "user_id": "U-023", "permission_id": "P-089", "reviewed_by": "U-005", "requested_on": "2025-08-04 18:00:00+00:00", "reviewed_on": "2025-08-08T12:00:00.000000Z", "expires_on": "2025-09-21 04:59:59+00:00", "reason": "Full administrative access to a specific production server for troubleshooting.", "status": "ACTIVE"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_005",
        instruction=(
            "You are RBAC_BOT. Finance analyst Stephanie Adams needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 15th, 2025). "
            "Stephanie claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Jessica Garcia as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Stephanie", "last_name": "Adams"},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-018",
                    "permission_id": "P-084",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-15",
                    "expires_on": "2025-10-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-018", "permission_id": "P-084", "reviewed_by": "U-006", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-10-15T23:59:59.000000Z", "reason": "Temporary access to perform submit-tax-filing until 2025-10-15", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_006",
        instruction=(
            "You are HR_ONBOARD_BOT. "
            "Nicole Thomas is transferring from Marketing to Sales department. "
            "you must remove her marketing-base role and marketing-analytics-read role, and add the base sales role."
        ),
        actions=[
            Action(
                name="get_user",
                kwargs={"username": "HR_ONBOARD_BOT"},
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Nicole", "last_name": "Thomas"},
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-014",
                    "only_active": False,
                },
            ),
            Action(
                name="update_user",
                kwargs={
                    "user_id": "U-014",
                    "department": "Sales",
                },
            ),
            Action(
                name="get_base_role_by_department", kwargs={"department": "Marketing"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-006",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "Role ROL-006 removed from U-014",
                },
            ),
            Action(
                name="get_role",
                kwargs={"role_name": "marketing-analytics-read"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-009",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "Role ROL-009 removed from U-014",
                },
            ),
            Action(
                name="get_base_role_by_department",
                kwargs={"department": "Sales"},
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-011",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "Role ROL-011 added to U-014",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-014",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-014", "assignments": [{"role_id": "ROL-011", "role_name": "sales-base", "description": "Basic access for sales staff"}]}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_007",
        instruction=(
            "You are operations incident responder Jeffery Green. "
            "You must investigate the unauthorized access attempt by Brian Taylor to the production database cluster (RES-026). "
            "You must create the SIEM alert with critical severity."
        ),
        actions=[
            Action(
                name="get_user",
                kwargs={"first_name": "Jeffery", "last_name": "Green"},
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-023", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Brian", "last_name": "Taylor"},
            ),
            Action(
                name="create_siem_alert",
                kwargs={
                    "user_id": "U-013",
                    "resource_id": "RES-026",
                    "alert_type": "UNAUTHORIZED_ACCESS_ATTEMPT",
                    "severity": "CRITICAL",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "SIEM_ALERT_CREATED",
                    "actor_id": "U-023",
                    "target_id": "ALRT-013",
                    "details": "SIEM alert ALRT-013 created for UNAUTHORIZED_ACCESS_ATTEMPT on RES-026",
                },
            ),
            Action(
                name="update_user",
                kwargs={
                    "user_id": "U-013",
                    "status": "SUSPENDED",
                    "updated_by": "U-023",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-023",
                    "target_id": "U-013",
                    "details": "U-023 changed user U-013 status to SUSPENDED",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-013",
                    "only_active": True,
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-013", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-023",
                    "target_id": "U-013",
                    "details": "Role ROL-001 removed from U-013",
                },
            ),
            Action(
                name="get_session",
                kwargs={"user_id": "U-013", "only_active": True}
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "SIEM Alert: Unauthorized Access Attempt",
                    "description": "SIEM Alert ALRT-013: CRITICAL severity alert for user U-013 attempting to access resource RES-026.",
                    "assignee_id": "U-005",
                    "requester_id": "U-013",
                    "priority": "HIGH",
                    "category": "SECURITY_INCIDENT",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#security-incidents",
                    "message": "ALRT-013 processed: U-013 suspended and security incident ticket created.",
                    "username": "jgreen",
                    "timestamp": "2025-08-08T12:00:00.000000Z",
                },
            ),
        ],
        outputs=[
            '{"ok": true, "siem_alert": {"alert_id": "ALRT-013", "user_id": "U-013", "resource_id": "RES-026", "alert_type": "UNAUTHORIZED_ACCESS_ATTEMPT", "severity": "CRITICAL"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_008",
        instruction=(
            "You are RBAC_BOT. Employee Ryan Baker is leaving the company today August 8th, 2025. "
            "You must offboard him following standard policy."
        ),
        actions=[
            Action(
                name="get_user",
                kwargs={"username": "RBAC_BOT"},
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Ryan", "last_name": "Baker"},
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-025",
                    "only_active": False,
                },
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-025", "status": "DISABLED"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-031",
                    "target_id": "U-025",
                    "details": "RBAC_BOT changed user U-025 status to DISABLED",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-025", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-025",
                    "details": "Role ROL-001 removed from U-025",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-025", "role_id": "ROL-003", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-025",
                    "details": "Role ROL-003 removed from U-025",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-025",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "Offboard employee Ryan Baker (rbaker)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-031",
                    "assignee_id": "U-005",
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-025"}),
        ],
        outputs=[
            '{"user_id": "U-025", "assignments": []}',
            '{"user_id": "U-025", "username": "rbaker", "email": "ryan.baker@taucorp.com", "department": "Engineering", "status": "DISABLED", "mfa_enabled": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_009",
        instruction=(
            "You are HR_ONBOARD_BOT. Marketing analyst Nicole Thomas is leaving the company today August 5th, 2025. "
            "Her replacement, David Wilson, is starting immediately. You must offboard Nicole and onboard David with identical access."
        ),
        actions=[
            Action(
                name="get_user",
                kwargs={"username": "HR_ONBOARD_BOT"},
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Nicole", "last_name": "Thomas"},
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-014",
                },
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-014", "status": "DISABLED"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "HR_ONBOARD_BOT changed user U-014 status to DISABLED",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-006",
                    "action": "REMOVE",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "Role ROL-006 removed from U-014",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-009",
                    "action": "REMOVE",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "Role ROL-009 removed from U-014",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "Offboard employee Nicole Thomas (nthomas)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "dwilson",
                    "email": "david.wilson@taucorp.com",
                    "department": "Marketing",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-006",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-006 added to U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-009",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-009 added to U-034",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "receiver": "david.wilson@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi David, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@taucorp.com",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="check_sod_conflicts",
                kwargs={
                    "user_id": "U-034",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-014",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-006", "role_name": "marketing-base", "description": "Basic access for marketing staff"}, {"role_id": "ROL-009", "role_name": "marketing-analytics-read", "description": "Read-only access to marketing analytics data"}]}',
            '{"ok": true, "user_id": "U-034", "has_sod_conflicts": false, "conflict_count": 0, "conflicts": [], "checked_on": "2025-08-08T12:00:00.000000Z"}',
            '{"user_id": "U-014", "assignments": []}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_010",
        instruction=(
            "You are RBAC_BOT responding to a critical security incident. SIEM alert ALRT-011 detected unauthorized access attempts "
            "on a resource. If the user has no active roles that allow them to access the resource,"
            " you must suspend the user that has been flagged and create a security incident ticket."
        ),
        actions=[
            Action(
                name="get_user",
                kwargs={"username": "RBAC_BOT"},
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_siem_alert",
                kwargs={"alert_id": "ALRT-011"},
            ),
            Action(
                name="can_access_resource",
                kwargs={"user_id": "U-007", "resource_id": "RES-020"},
            ),
            Action(
                name="update_user",
                kwargs={
                    "user_id": "U-007",
                    "status": "SUSPENDED",
                    "updated_by": "U-031",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-031",
                    "target_id": "U-007",
                    "details": "RBAC_BOT changed user U-007 status to SUSPENDED",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-007",
                    "only_active": False,
                    "include_role_details": False,
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-007", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-007",
                    "details": "Role ROL-001 removed from U-007",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-007", "role_id": "ROL-002", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-007",
                    "details": "Role ROL-002 removed from U-007",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-007", "role_id": "ROL-003", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-007",
                    "details": "Role ROL-003 removed from U-007",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "category": "SECURITY_INCIDENT",
                    "subject": "SIEM Alert: Unauthorized Access Attempt",
                    "description": "SIEM Alert ALRT-011: HIGH severity alert for user U-007 attempting to access resource RES-020.",
                    "priority": "HIGH",
                    "status": "OPEN",
                    "requester_id": "U-007",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#security-incidents",
                    "message": "ALRT-011 processed: U-007 suspended and security incident ticket created.",
                    "username": "RBAC_BOT",
                    "timestamp": "2025-08-08T12:00:00.000000Z",
                },
            ),
            Action(
                name="get_user",
                kwargs={"user_id": "U-007"},
            ),
            Action(
                name="get_user_roles",
                kwargs={"user_id": "U-007", "only_active": True},
            ),
            Action(
                name="get_session", kwargs={"user_id": "U-007", "only_active": True}
            ),
        ],
        outputs=[
            '{"ok": true, "user_id": "U-007", "resource_id": "RES-020", "can_access": false, "checked_on": "2025-08-08T12:00:00.000000Z", "reason": "User does not have any active roles that grant access to this resource"}',
            '{"user_id": "U-007", "username": "crodriguez", "email": "christopher.rodriguez@taucorp.com", "department": "Engineering", "status": "SUSPENDED", "mfa_enabled": true}',
            '{"user_id": "U-007", "assignments": []}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_011",
        instruction=(
            "You're lead engineer Michael Davis. You must review Brittany King's pending access request for read-only HR data and approve it per policy."
            "Then, if approved, add the requested role to her account and return Brittany King's updated roles."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Brittany", "last_name": "King"}
            ),
            Action(
                name="get_access_request",
                kwargs={"user_id": "U-022", "status": "PENDING"},
            ),
            Action(name="get_resource", kwargs={"resource_id": "RES-020"}),
            Action(name="get_role", kwargs={"role_id": "ROL-017"}),
            Action(
                name="decide_access_request",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-022",
                    "role_id": "ROL-017",
                    "action": "ADD",
                    "assigned_by": "U-005",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-005",
                    "target_id": "U-022",
                    "details": "Role ROL-017 added to U-022",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ACCESS_GRANTED",
                    "actor_id": "U-005",
                    "target_id": "AR-030",
                    "details": "Access request AR-030 was approved by U-005",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "michael.davis@taucorp.com",
                    "receiver": "brittany.king@taucorp.com",
                    "subject": "Access Request APPROVED",
                    "text_content": "Your access request AR-030 has been APPROVED.",
                },
            ),
            Action(name="get_access_request", kwargs={"request_id": "AR-030"}),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-022",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"access_request": {"request_id": "AR-030", "user_id": "U-022", "resource_id": "RES-020", "requested_role_id": "ROL-017", "justification": "Need read-only access to employee data.", "status": "APPROVED", "submitted_at": "2024-05-29 14:00:00+00:00", "reviewed_by": "U-005", "decision_at": "2025-08-08T12:00:00.000000Z"}}',
            '{"user_id": "U-022", "assignments": [{"role_id": "ROL-016", "role_name": "hr-base", "description": "Basic access for human resources staff"}, {"role_id": "ROL-017", "role_name": "hr-employee-data-read", "description": "Read-only access to employee records"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_012",
        instruction=(
            "You're finance lead Jessica Garcia."
            "You must review Stephanie Adams's pending access request for read-only finance data and approve it per policy."
            "Then, if approved, add the requested role to her account and return Stephanie's updated roles."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Stephanie", "last_name": "Adams"},
            ),
            Action(
                name="get_access_request",
                kwargs={"user_id": "U-018", "status": "PENDING"},
            ),
            Action(name="get_resource", kwargs={"resource_id": "RES-034"}),
            Action(name="get_role", kwargs={"role_id": "ROL-030"}),
            Action(
                name="decide_access_request",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-018",
                    "role_id": "ROL-030",
                    "action": "ADD",
                    "assigned_by": "U-006",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-006",
                    "target_id": "U-018",
                    "details": "Role ROL-030 added to U-018",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ACCESS_GRANTED",
                    "actor_id": "U-006",
                    "target_id": "AR-034",
                    "details": "Access request AR-034 was approved by U-006",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "jessica.garcia@taucorp.com",
                    "receiver": "stephanie.adams@taucorp.com",
                    "subject": "Access Request APPROVED",
                    "text_content": "Your access request AR-034 has been APPROVED.",
                },
            ),
            Action(name="get_access_request", kwargs={"request_id": "AR-034"}),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-018",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"request_id":"AR-034","user_id":"U-018","resource_id":"RES-034","requested_role_id":"ROL-030","justification":"Requesting read access to tax compliance software.","status":"APPROVED"}',
            '{"user_id": "U-018", "assignments": [{"role_id": "ROL-029", "role_name": "finance-base", "description": "Basic access for finance staff"}, {"role_id": "ROL-030", "role_name": "finance-read", "description": "Read-only access to finance data"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_013",
        instruction=(
            "You're lead engineer Alex Johnson. "
            "Christopher Rodriguez has a policy exception that is pending review. "
            "You must review it per policy, reject it, and record an audit entry for your decision."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Alex", "last_name": "Johnson"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Christopher", "last_name": "Rodriguez"},
            ),
            Action(
                name="get_policy_exception",
                kwargs={"user_id": "U-007", "status": "PENDING_REVIEW"},
            ),
            Action(name="get_permission", kwargs={"permission_id": "P-005"}),
            Action(name="get_resource", kwargs={"resource_id": "RES-002"}),
            Action(
                name="decide_policy_exception",
                kwargs={
                    "exception_id": "PE-018",
                    "reviewer_id": "U-001",
                    "decision": "DENIED",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_DENIED",
                    "actor_id": "U-001",
                    "target_id": "PE-018",
                    "details": "U-001 denied exception PE-018",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-018 denied by U-001",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "rbac@taucorp.com",
                    "receiver": "christopher.rodriguez@taucorp.com",
                    "subject": "Policy Exception DENIED",
                    "text_content": "Your policy exception request PE-018 has been DENIED.",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-018"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-018", "user_id": "U-007", "permission_id": "P-005", "reviewed_by": "U-001", "requested_on": "2025-08-06 15:00:00+00:00", "reviewed_on": "2025-08-08T12:00:00.000000Z", "expires_on": null, "reason": "Emergency configuration change to the CI/CD pipeline.", "status": "DENIED"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_014",
        instruction=(
            "You are RBAC_BOT. Finance analyst Stephanie Adams needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 15th, 2025). "
            "Stephanie claims her reason for the request is 'quarter-close filing requires elevated permission' and she needs the 'submit-tax-filing' permission."
            "You must create the exception and assign Jessica Garcia as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Stephanie", "last_name": "Adams"},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-018",
                    "permission_id": "P-084",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-15",
                    "expires_on": "2025-10-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="liam",
        user_id="liam_015",
        instruction=(
            "You're operations manager Michael Davis. "
            "You must complete the pending certification for the network firewall main resource (RES-027)."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="get_certification",
                kwargs={"user_id": "U-005", "status": "PENDING"},
            ),
            Action(
                name="list_users_with_access_to_resource",
                kwargs={"resource_id": "RES-027", "include_role_details": True},
            ),
            Action(
                name="can_access_resource",
                kwargs={"user_id": "U-005", "resource_id": "RES-027"},
            ),
            Action(
                name="can_access_resource",
                kwargs={"user_id": "U-023", "resource_id": "RES-027"},
            ),
            Action(
                name="complete_certification",
                kwargs={"certification_id": "C-020", "reviewer_id": "U-005"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "CERTIFICATION_COMPLETED",
                    "actor_id": "U-005",
                    "target_id": "C-020",
                    "details": "Certification C-020 for RES-027 was completed",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#certifications",
                    "message": "C-020 for RES-027 completed by U-005",
                },
            ),
        ],
        outputs=[
            '{"ok": true, "certification": {"certification_id": "C-020", "reviewer_id": "U-005", "resource_id": "RES-027", "status": "COMPLETED", "due_date": "2025-11-08 04:59:59+00:00", "completed_on": "2025-08-08T12:00:00.000000Z"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_016",
        instruction=(
            "You're finance lead Jessica Garcia. Marisa Cole is PENDING_ACCESS but has been cleared for activation. "
            "She has a pending request access request that is valid."
            "You must activate Marisa's account. "
            "You must approve the request and add the requested roles to Marisa's account."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Marisa", "last_name": "Cole"}
            ),
            Action(
                name="update_user",
                kwargs={
                    "user_id": "U-030",
                    "status": "ACTIVE",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-006",
                    "target_id": "U-030",
                    "details": "U-006 changed user U-030 status to ACTIVE",
                },
            ),
            Action(
                name="get_access_request",
                kwargs={"user_id": "U-030", "status": "PENDING"},
            ),
            Action(name="get_resource", kwargs={"resource_id": "RES-032"}),
            Action(name="get_role", kwargs={"role_id": "ROL-032"}),
            Action(
                name="decide_access_request",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-006",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-030",
                    "role_id": "ROL-032",
                    "action": "ADD",
                    "assigned_by": "U-006",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-006",
                    "target_id": "U-030",
                    "details": "Role ROL-032 added to U-030",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ACCESS_GRANTED",
                    "actor_id": "U-006",
                    "target_id": "AR-008",
                    "details": "Access request AR-008 was approved by U-006",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "jessica.garcia@taucorp.com",
                    "receiver": "marisa.cole@taucorp.com",
                    "subject": "Access Request APPROVED",
                    "text_content": "Your access request AR-008 has been APPROVED.",
                },
            ),
            Action(name="get_access_request", kwargs={"request_id": "AR-008"}),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-030",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"access_request": {"request_id": "AR-008", "user_id": "U-030", "resource_id": "RES-032", "requested_role_id": "ROL-032", "justification": "Need to create budgets for Q3 planning.", "status": "APPROVED", "submitted_at": "2024-05-20 15:00:00+00:00", "reviewed_by": "U-006", "decision_at": "2025-08-08T12:00:00.000000Z"}}',
            '{"user_id": "U-030", "assignments": [{"role_id": "ROL-029", "role_name": "finance-base", "description": "Basic access for finance staff"}, {"role_id": "ROL-032", "role_name": "finance-budget-admin", "description": "Administers departmental budgets"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_017",
        instruction=(
            "You're marketing lead Sarah Williams."
            "Angela Phillips has two pending access requests, "
            "you must approve or reject both requests according to policy "
            "then you must modify her roles accordingly."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Sarah", "last_name": "Williams"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-002"}),
            Action(
                name="get_user",
                kwargs={"first_name": "Angela", "last_name": "Phillips"},
            ),
            Action(
                name="get_user_roles", kwargs={"user_id": "U-026", "only_active": True}
            ),
            Action(
                name="get_access_request",
                kwargs={"user_id": "U-026", "status": "PENDING"},
            ),
            Action(name="get_resource", kwargs={"resource_id": "RES-008"}),
            Action(
                name="check_sod_conflicts",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-008",
                },
            ),
            Action(
                name="decide_access_request",
                kwargs={
                    "request_id": "AR-009",
                    "reviewer_id": "U-002",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ACCESS_GRANTED",
                    "actor_id": "U-002",
                    "target_id": "AR-009",
                    "details": "Access request AR-009 was approved by U-002",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-008",
                    "action": "ADD",
                    "assigned_by": "U-002",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-002",
                    "target_id": "U-026",
                    "details": "Role ROL-008 added to U-026",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "sarah.williams@taucorp.com",
                    "receiver": "angela.phillips@taucorp.com",
                    "subject": "Access Request APPROVED",
                    "text_content": "Your access request AR-009 has been APPROVED.",
                },
            ),
            Action(
                name="decide_access_request",
                kwargs={
                    "request_id": "AR-021",
                    "reviewer_id": "U-002",
                    "decision": "REJECTED",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ACCESS_REJECTED",
                    "actor_id": "U-002",
                    "target_id": "AR-021",
                    "details": "Access request AR-021 was rejected by U-002",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "sarah.williams@taucorp.com",
                    "receiver": "angela.phillips@taucorp.com",
                    "subject": "Access Request REJECTED",
                    "text_content": "Your access request AR-021 has been REJECTED.",
                },
            ),
            Action(name="get_access_request", kwargs={"request_id": "AR-009"}),
            Action(name="get_access_request", kwargs={"request_id": "AR-021"}),
            Action(
                name="get_user_roles", kwargs={"user_id": "U-026", "only_active": True}
            ),
        ],
        outputs=[
            '{"access_request": {"request_id": "AR-009", "user_id": "U-026", "resource_id": "RES-008", "requested_role_id": "ROL-008", "justification": "Temporary access to social media for a specific campaign launch.", "status": "APPROVED", "submitted_at": "2024-05-20 16:00:00+00:00", "reviewed_by": "U-002", "decision_at": "2025-08-08T12:00:00.000000Z"}}',
            '{"access_request": {"request_id": "AR-021", "user_id": "U-026", "resource_id": "RES-012", "requested_role_id": "ROL-010", "justification": "Requesting content editor access for the blog.", "status": "REJECTED", "submitted_at": "2024-05-26 15:00:00+00:00", "reviewed_by": "U-002", "decision_at": "2025-08-08T12:00:00.000000Z"}}',
            '{"user_id": "U-026", "assignments": [{"role_id": "ROL-006"}, {"role_id": "ROL-007"}, {"role_id": "ROL-010"}, {"role_id": "ROL-008"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_018",
        instruction=(
            "You are RBAC_BOT. Finance analyst Lisa Anderson needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 10th, 2025). "
            "Lisa claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Alex Johnson as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Lisa", "last_name": "Anderson"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Alex", "last_name": "Johnson"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-012",
                    "permission_id": "P-084",
                    "reviewed_by": "U-001",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-10",
                    "expires_on": "2025-10-10T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-012", "permission_id": "P-084", "reviewed_by": "U-001", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-10-10T23:59:59.000000Z", "reason": "Temporary access to perform submit-tax-filing until 2025-10-10", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_019",
        instruction=(
            "You are RBAC_BOT. Finance analyst Katherine Hall needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD September 30th, 2025). "
            "Katherine claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Sarah Williams as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Katherine", "last_name": "Hall"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Sarah", "last_name": "Williams"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-002", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-024",
                    "permission_id": "P-084",
                    "reviewed_by": "U-002",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-09-30",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-024", "permission_id": "P-084", "reviewed_by": "U-002", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-09-30T23:59:59.000000Z", "reason": "Temporary access to perform submit-tax-filing until 2025-09-30", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_020",
        instruction=(
            "You are RBAC_BOT. Engineer Alex Johnson needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD September 25th, 2025). "
            "Alex claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Michael Davis as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Alex", "last_name": "Johnson"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-001",
                    "permission_id": "P-084",
                    "reviewed_by": "U-005",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-09-25",
                    "expires_on": "2025-09-25T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-001", "permission_id": "P-084", "reviewed_by": "U-005", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-09-25T23:59:59.000000Z", "reason": "Temporary access to perform submit-tax-filing until 2025-09-25", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_021",
        instruction=(
            "You are RBAC_BOT. Finance lead Jessica Garcia has approved the pending policy exception for Katherine Hall. "
            "You must inspect the details of the request and approve the exception and proceed according to policy."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(name="is_admin", kwargs={"user_id": "U-031"}),
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Katherine", "last_name": "Hall"}
            ),
            Action(
                name="get_policy_exception",
                kwargs={"user_id": "U-024", "status": "PENDING_REVIEW"},
            ),
            Action(name="get_permission", kwargs={"permission_id": "P-088"}),
            Action(name="get_resource", kwargs={"resource_id": "RES-035"}),
            Action(
                name="decide_policy_exception",
                kwargs={
                    "exception_id": "PE-019",
                    "reviewer_id": "U-006",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_APPROVED",
                    "actor_id": "U-006",
                    "target_id": "PE-019",
                    "details": "U-006 approved exception PE-019",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-019 approved by U-006",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "rbac@taucorp.com",
                    "receiver": "katherine.hall@taucorp.com",
                    "subject": "Policy Exception Approved",
                    "text_content": "Your policy exception request PE-019 has been approved.",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-019"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-019", "user_id": "U-024", "permission_id": "P-088", "reviewed_by": "U-006", "requested_on": "2025-08-06 16:00:00+00:00", "reviewed_on": "2025-08-08T12:00:00.000000Z", "expires_on": "2025-11-21 04:59:59+00:00", "reason": "Approval of a large expense report for a new project.", "status": "ACTIVE"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_022",
        instruction=(
            "You are RBAC_BOT. You must promote HR specialist Ashley Wilson to HR Lead by adding the hr-lead role, there is no need to remove any roles. "
            "Update her role assignments accordingly and follow promotion policy for notifications."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Ashley", "last_name": "Wilson"}
            ),
            Action(name="get_role", kwargs={"role_name": "hr-lead"}),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-010",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-010",
                    "role_id": "ROL-037",
                    "action": "ADD",
                    "assigned_by": "U-031",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-010",
                    "details": "Role ROL-037 added to U-010",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#human-resources",
                    "message": "awilson promoted to hr-lead by RBAC_BOT.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "rbac@taucorp.com",
                    "receiver": "ashley.wilson@taucorp.com",
                    "subject": "Promotion: hr-lead",
                    "text_content": "Your role has been updated to include hr-lead. Congratulations.",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-010",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-010", "assignments": [{"role_id": "ROL-016", "role_name": "hr-base", "description": "Basic access for human resources staff"}, {"role_id": "ROL-019", "role_name": "hr-recruitment-manager", "description": "Manages job postings and candidate applications"}, {"role_id": "ROL-037", "role_name": "hr-lead", "description": "Lead role for the human resources department."}]}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_023",
        instruction=(
            "You are RBAC_BOT. You must swap leadership within Human Resources: demote Ashley Wilson from HR Recruitment Manager to base HR employee "
            "and promote Laura Jackson to HR Recruitment Manager with all of the same roles as Ashley. Record audit entries, notify the HR channel, email the promoted user, and return "
            "both users' updated roles."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031"},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Ashley", "last_name": "Wilson"}
            ),
            Action(
                name="get_user_roles", kwargs={"user_id": "U-010", "only_active": True}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-010",
                    "role_id": "ROL-019",
                    "action": "REMOVE",
                    "assigned_by": "U-031",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-010",
                    "details": "Role ROL-019 removed from U-010",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Laura", "last_name": "Jackson"}
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-016"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-016",
                    "role_id": "ROL-019",
                    "action": "ADD",
                    "assigned_by": "U-031",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-016",
                    "details": "Role ROL-019 added to U-016",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#human-resources",
                    "message": "ljackson promoted to hr-recruitment-manager by RBAC_BOT.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "rbac@taucorp.com",
                    "receiver": "laura.jackson@taucorp.com",
                    "subject": "Promotion: hr-recruitment-manager",
                    "text_content": "Your role has been updated to include hr-recruitment-manager. Congratulations.",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-010",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-016",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-010", "assignments": [{"role_id": "ROL-016", "role_name": "hr-base", "description": "Basic access for human resources staff"}]}',
            '{"user_id": "U-016", "assignments": [{"role_id": "ROL-016", "role_name": "hr-base", "description": "Basic access for human resources staff"}, {"role_id": "ROL-019", "role_name": "hr-recruitment-manager", "description": "Manages job postings and candidate applications"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_024",
        instruction=(
            "You are HR_ONBOARD_BOT. A new employee named Olivia Perez has just been hired to the Sales department to replace Kevin Harris, who has been promoted to sales-lead-manager."
            "You must onboard Olivia following the standard procedures, add all of Kevin's active roles to hers, and return Olivia's active roles."
            "You must carry out Kevin's promotion by adding the sales-lead-manager role to his account."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Kevin", "last_name": "Harris"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-015",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "operez",
                    "email": "olivia.perez@taucorp.com",
                    "department": "Sales",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-011",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-011 added to U-034",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "receiver": "olivia.perez@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Olivia, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@taucorp.com",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-032",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "sales-lead-manager"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-015",
                    "role_id": "ROL-013",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-015",
                    "details": "Role ROL-013 added to U-015",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#sales",
                    "message": "kharris promoted to sales-lead-manager by RBAC_BOT.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "rbac@taucorp.com",
                    "receiver": "kevin.harris@taucorp.com",
                    "subject": "Promotion: sales-lead-manager",
                    "text_content": "Your role has been updated to include sales-lead-manager. Congratulations.",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-015",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-011", "role_name": "sales-base", "description": "Basic access for sales staff"}]}',
            '{"user_id": "U-015", "assignments": [{"role_id": "ROL-011", "role_name": "sales-base", "description": "Basic access for sales staff"}, {"role_id": "ROL-013", "role_name": "sales-lead-manager", "description": "Manages sales leads and opportunities"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_025",
        instruction=(
            "You are RBAC_BOT. James Moore (Operations) has left the company. "
            "You must offboard James immediately, his account is already disabled. Ensure your actions are auditable."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "James", "last_name": "Moore"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-011",
                    "only_active": False,
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-011", "role_id": "ROL-021", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-011",
                    "details": "Role ROL-021 removed from U-011",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "Offboard employee James Moore (jmoore)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "requester_id": "U-031",
                    "category": "OFFBOARDING",
                    "assignee_id": "U-005",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-011",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=['{"user_id": "U-011", "assignments": []}'],
    ),
    Task(
        annotator="liam",
        user_id="liam_026",
        instruction=(
            "You are HR_ONBOARD_BOT. A new employee named Olivia Green has joined the Finance department. "
            "You must onboard her based on company policy, also give her the 'finance-read' role."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "ogreen",
                    "email": "olivia.green@taucorp.com",
                    "department": "Finance",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-032",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="get_base_role_by_department", kwargs={"department": "Finance"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-029",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-029 added to U-034",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "finance-read"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-030",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-030 added to U-034",
                },
            ),
            Action(name="check_sod_conflicts", kwargs={"user_id": "U-034"}),
            Action(
                name="send_email",
                kwargs={
                    "receiver": "olivia.green@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Olivia, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@taucorp.com",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Olivia", "last_name": "Green"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-029", "role_name": "finance-base", "description": "Basic access for finance staff"}]}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_027",
        instruction=(
            "You are Operations Lead Michael Davis. During an IT audit, you found Jeffery Green's 'operations-deployment-admin' role is redundant. "
            "You must remove it and open a remediation ticket."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jeffery", "last_name": "Green"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-023",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-023", "role_id": "ROL-025", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-005",
                    "target_id": "U-023",
                    "details": "Role ROL-025 removed from U-023",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "Audit Remediation",
                    "description": "Revoked redundant role 'operations-deployment-admin' from user 'jgreen' as per audit finding.",
                    "requester_id": "U-005",
                    "category": "COMPLIANCE",
                    "assignee_id": "U-005",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-023",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-023", "assignments": [{"role_id": "ROL-021", "role_name": "operations-base", "description": "Basic access for operations staff"}, {"role_id": "ROL-023", "role_name": "operations-incident-response", "description": "Responds to and resolves system incidents"}]}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_028",
        instruction=(
            "You are RBAC_BOT. Marketing analyst Sarah Williams needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD September 20th, 2025). "
            "Sarah claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Jessica Garcia as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Sarah", "last_name": "Williams"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-002",
                    "permission_id": "P-084",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-09-20",
                    "expires_on": "2025-09-20T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-002", "permission_id": "P-084", "reviewed_by": "U-006", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-09-20T23:59:59.000000Z", "reason": "Temporary access to perform submit-tax-filing until 2025-09-20", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_029",
        instruction=(
            "You're operations manager Michael Davis. You must review Patrick Carter's pending access request for operations-system-admin and approve it per policy. "
            "Then, add the requested role to his account and return Patrick's updated roles."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Patrick", "last_name": "Carter"}
            ),
            Action(
                name="get_user_roles", kwargs={"user_id": "U-029", "only_active": True}
            ),
            Action(
                name="get_access_request",
                kwargs={"user_id": "U-029", "status": "PENDING"},
            ),
            Action(name="get_resource", kwargs={"resource_id": "RES-025"}),
            Action(name="get_role", kwargs={"role_id": "ROL-026"}),
            Action(
                name="decide_access_request",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-026",
                    "action": "ADD",
                    "assigned_by": "U-005",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-005",
                    "target_id": "U-029",
                    "details": "Role ROL-026 added to U-029",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ACCESS_GRANTED",
                    "actor_id": "U-005",
                    "target_id": "AR-007",
                    "details": "Access request AR-007 was approved by U-005",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "michael.davis@taucorp.com",
                    "receiver": "patrick.carter@taucorp.com",
                    "subject": "Access Request APPROVED",
                    "text_content": "Your access request AR-007 has been APPROVED.",
                },
            ),
            Action(name="get_access_request", kwargs={"request_id": "AR-007"}),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-029",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"access_request": {"request_id": "AR-007", "user_id": "U-029", "resource_id": "RES-025", "requested_role_id": "ROL-026", "justification": "Urgent request for full system admin access for incident response.", "status": "APPROVED", "submitted_at": "2024-05-20 14:00:00+00:00", "reviewed_by": "U-005", "decision_at": "2025-08-08T12:00:00.000000Z"}}',
            '{"user_id": "U-029", "assignments": [{"role_id": "ROL-021", "role_name": "operations-base", "description": "Basic access for operations staff"}, {"role_id": "ROL-026", "role_name": "operations-system-admin", "description": "Full administrative access to all operations systems."}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_030",
        instruction=(
            "You are RBAC_BOT. Engineer Christopher Rodriguez needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 1st, 2025). "
            "Christopher claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Michael Davis as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Christopher", "last_name": "Rodriguez"},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-007",
                    "permission_id": "P-084",
                    "reviewed_by": "U-005",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-01",
                    "expires_on": "2025-10-01T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-007", "permission_id": "P-084", "reviewed_by": "U-005", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-10-01T23:59:59.000000Z", "reason": "Temporary access to perform submit-tax-filing until 2025-10-01", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_031",
        instruction=(
            "You are operations manager Michael Davis. SIEM Alert ALRT-012 has been resolved. "
            "You must find and close the open security incident ticket regarding ALRT-012. "
            "You must ensure the correct communication channels are updated."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="get_hubspot_ticket", kwargs={"alert_id": "ALRT-012"}),
            Action(
                name="update_hubspot_ticket",
                kwargs={"ticket_id": "TI-053", "status": "CLOSED"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "TICKET_CLOSED",
                    "actor_id": "U-005",
                    "target_id": "TI-053",
                    "details": "Closed security incident ticket TI-053",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#security-incidents",
                    "message": "Ticket TI-053 closed by U-005.",
                    "username": "RBAC_BOT",
                    "timestamp": "2025-08-08T12:00:00.000000Z",
                },
            ),
        ],
        outputs=[
            '{"ok": true, "ticket": {"ticket_id": "TI-053", "created_at": "2025-06-02 21:30:00+00:00", "updated_at": "2025-08-08T12:00:00.000000Z", "subject": "SIEM Alert: Unauthorized Access Attempt", "description": "SIEM Alert ALRT-012: Critical severity alert for user U-004 attempting to access resource RES-014.", "status": "CLOSED", "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-004", "category": "SECURITY_INCIDENT", "closed_at": "2025-08-08T12:00:00.000000Z"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_032",
        instruction=(
            "You are RBAC_BOT. Create a new certification for the IAM / RBAC portal to prepare for audit by reviewer Michael Davis, due EOD October 12th, 2025."
            "You must ensure Michael is in fact the owner of the IAM / RBAC portal, has authority to review it."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(name="is_admin", kwargs={"user_id": "U-031"}),
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="get_resource", kwargs={"name": "IAM / RBAC portal"}),
            Action(
                name="create_certification",
                kwargs={
                    "reviewer_id": "U-005",
                    "resource_id": "RES-042",
                    "status": "PENDING",
                    "due_date": "2025-10-12T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "CERTIFICATION_CREATED",
                    "actor_id": "U-031",
                    "target_id": "C-024",
                    "details": "Certification C-024 for RES-042 was created.",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#certifications",
                    "message": "C-024 created for RES-042 assigned to U-005.",
                },
            ),
        ],
        outputs=[
            '{"ok": true, "certification": {"certification_id": "C-024", "reviewer_id": "U-005", "resource_id": "RES-042", "status": "PENDING", "due_date": "2025-10-12T23:59:59.000000Z", "completed_on": null}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_033",
        instruction=(
            "You are engineering lead Alex Johnson. You must create a new permission 'approve-merge' on the 'main-application-repo' resource with "
            "description 'Allows approving merges on the main repository'. "
            "Then assign this permission to the existing 'engineering-lead' role."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Alex", "last_name": "Johnson"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(name="get_resource", kwargs={"name": "main-application-repo"}),
            Action(
                name="create_permission",
                kwargs={
                    "action": "approve-merge",
                    "resource_id": "RES-002",
                    "description": "Allows approving merges on the main repository",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-001",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-001.",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "engineering-lead"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-034", "permission_id": "P-113"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-001",
                    "target_id": "ROL-034",
                    "details": "Permission P-113 assigned to role ROL-034.",
                },
            ),
            Action(name="get_user", kwargs={"role_id": "ROL-034", "status": "ACTIVE"}),
            Action(name="check_sod_conflicts", kwargs={"user_id": "U-001"}),
            Action(
                name="get_role_permissions",
                kwargs={
                    "role_id": "ROL-034",
                    "permission_id": "P-113",
                    "include_role": True,
                    "include_permission": True,
                },
            ),
        ],
        outputs=[
            '{"ok": true, "permission": {"permission_id": "P-113", "action": "approve-merge", "resource_id": "RES-002", "description": "Allows approving merges on the main repository"}}',
            '{"ok": true, "role_permissions": [{"role_id": "ROL-034", "permission_id": "P-113", "role": {"role_id": "ROL-034", "role_name": "engineering-lead", "description": "Lead role for the engineering department.", "is_temporary": false}, "permission": {"permission_id": "P-113", "action": "approve-merge", "resource_id": "RES-002", "description": "Allows approving merges on the main repository"}}]}',
            '{"ok": true, "user_id": "U-001", "has_sod_conflicts": false, "conflict_count": 0, "conflicts": [], "checked_on": "2025-08-08T12:00:00.000000Z"}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_034",
        instruction=(
            "You are operations lead Michael Davis. You must create a new permission 'close-siem-incident' on the 'SIEM' resource with description 'Allows closing incidents in the SIEM'. "
            "Then assign this permission to the existing 'operations-lead' role."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="get_resource", kwargs={"name": "SIEM"}),
            Action(
                name="create_permission",
                kwargs={
                    "action": "close-siem-incident",
                    "resource_id": "RES-040",
                    "description": "Allows closing incidents in the SIEM",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-005",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-005.",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "operations-lead"}),
            Action(name="get_user", kwargs={"role_id": "ROL-038", "status": "ACTIVE"}),
            Action(name="check_sod_conflicts", kwargs={"user_id": "U-005"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-038", "permission_id": "P-113"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-005",
                    "target_id": "ROL-038",
                    "details": "Permission P-113 assigned to role ROL-038.",
                },
            ),
            Action(
                name="get_role_permissions",
                kwargs={
                    "role_id": "ROL-038",
                    "permission_id": "P-113",
                    "include_role": True,
                    "include_permission": True,
                },
            ),
        ],
        outputs=[
            '{"ok": true, "permission": {"permission_id": "P-113", "action": "close-siem-incident", "resource_id": "RES-040", "description": "Allows closing incidents in the SIEM"}}',
            '{"ok": true, "role_permissions": [{"role_id": "ROL-038", "permission_id": "P-113", "role": {"role_id": "ROL-038", "role_name": "operations-lead", "description": "Lead role for the operations department.", "is_temporary": false}, "permission": {"permission_id": "P-113", "action": "close-siem-incident", "resource_id": "RES-040", "description": "Allows closing incidents in the SIEM"}}]}',
            '{"ok": true, "user_id": "U-005", "has_sod_conflicts": false, "conflict_count": 0, "conflicts": [], "checked_on": "2025-08-08T12:00:00.000000Z"}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_035",
        instruction=(
            "You are marketing lead Sarah Williams. You must create a new permission 'approve-social-post' on the 'social-media-platform' resource with description 'Allows approving scheduled social posts'. "
            "Then assign this permission to the existing 'marketing-lead' role."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Sarah", "last_name": "Williams"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-002", "include_role_details": True},
            ),
            Action(name="get_resource", kwargs={"name": "social-media-platform"}),
            Action(
                name="create_permission",
                kwargs={
                    "action": "approve-social-post",
                    "resource_id": "RES-008",
                    "description": "Allows approving scheduled social posts",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-002",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-002.",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "marketing-lead"}),
            Action(name="get_user", kwargs={"role_id": "ROL-035", "status": "ACTIVE"}),
            Action(name="check_sod_conflicts", kwargs={"user_id": "U-002"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-035", "permission_id": "P-113"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-002",
                    "target_id": "ROL-035",
                    "details": "Permission P-113 assigned to role ROL-035.",
                },
            ),

            Action(
                name="get_role_permissions",
                kwargs={
                    "role_id": "ROL-035",
                    "permission_id": "P-113",
                    "include_role": True,
                    "include_permission": True,
                },
            ),
        ],
        outputs=[
            '{"ok": true, "permission": {"permission_id": "P-113", "action": "approve-social-post", "resource_id": "RES-008", "description": "Allows approving scheduled social posts"}}',
            '{"ok": true, "role_permissions": [{"role_id": "ROL-035", "permission_id": "P-113", "role": {"role_id": "ROL-035", "role_name": "marketing-lead", "description": "Lead role for the marketing department.", "is_temporary": false}, "permission": {"permission_id": "P-113", "action": "approve-social-post", "resource_id": "RES-008", "description": "Allows approving scheduled social posts"}}]}',
            '{"ok": true, "user_id": "U-002", "has_sod_conflicts": false, "conflict_count": 0, "conflicts": [], "checked_on": "2025-08-08T12:00:00.000000Z"}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_036",
        instruction=(
            "You are HR_ONBOARD_BOT. HR coordinator Laura Jackson is changing her last name to Jacobs and taking leave until EOD September 30th, 2025. "
            "Update her profile and set her account to inactive during leave. "
            "While Laura is on leave, create a policy exception to be reviewed by Emily Jones so that Heather Mitchell can temporarily 'Process payroll in the system' until EOD September 30th, 2025."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="is_admin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="get_user", kwargs={"first_name": "Laura", "last_name": "Jackson"}),
            Action(name="get_user", kwargs={"username": "ljacobs", "allow_missing": True}),
            Action(name="update_user", kwargs={"user_id": "U-016", "last_name": "Jacobs"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-016",
                    "details": "U-032 updated user U-016 name to Laura Jacobs; username set to ljacobs; email set to laura.jacobs@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#human-resources",
                    "message": "User U-016 updated by U-032: username ljackson -> ljacobs; email set to laura.jacobs@taucorp.com; name set to Laura Jacobs.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="update_user", kwargs={"user_id": "U-016", "status": "INACTIVE"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-016",
                    "details": "HR_ONBOARD_BOT changed user U-016 status to INACTIVE",
                },
            ),
            Action(name="get_user", kwargs={"first_name": "Heather", "last_name": "Mitchell"}),
            Action(name="get_user", kwargs={"first_name": "Emily", "last_name": "Jones"}),
            Action(name="is_admin", kwargs={"user_id": "U-004", "include_role_details": True}),
            Action(name="get_permission", kwargs={"description": "Process payroll in the system"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-028",
                    "permission_id": "P-051",
                    "reviewed_by": "U-004",
                    "reason": "Temporary access to perform process-payroll until 2025-09-30",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-032",
                    "target_id": "PE-021",
                    "details": "HR_ONBOARD_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-032",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="get_user", kwargs={"username": "ljacobs"}),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"user_id": "U-016", "username": "ljacobs", "email": "laura.jacobs@taucorp.com", "department": "Human Resources", "status": "INACTIVE", "mfa_enabled": false}',
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-028", "permission_id": "P-051", "reviewed_by": "U-004", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-09-30T23:59:59.000000Z", "reason": "Temporary access to perform process-payroll until 2025-09-30", "status": "PENDING_REVIEW"}}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_037",
        instruction=(
            "You are finance lead Jessica Garcia. You must create a new permission 'lock-ledger-period' on the 'general-ledger-db' resource with description 'Allows locking accounting periods in the ledger'. "
            "Then assign this permission to the existing 'finance-lead' role."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="get_resource", kwargs={"name": "general-ledger-db"}),
            Action(name="get_role", kwargs={"role_name": "finance-lead"}),
            Action(
                name="create_permission",
                kwargs={
                    "action": "lock-ledger-period",
                    "resource_id": "RES-031",
                    "description": "Allows locking accounting periods in the ledger",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-006",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-006.",
                },
            ),
            Action(name="get_user", kwargs={"role_id": "ROL-039", "status": "ACTIVE"}),
            Action(name="check_sod_conflicts", kwargs={"user_id": "U-006"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-039", "permission_id": "P-113"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-006",
                    "target_id": "ROL-039",
                    "details": "Permission P-113 assigned to role ROL-039.",
                },
            ),
            Action(
                name="get_role_permissions",
                kwargs={
                    "role_id": "ROL-039",
                    "permission_id": "P-113",
                    "include_role": True,
                    "include_permission": True,
                },
            ),
        ],
        outputs=[
            '{"ok": true, "permission": {"permission_id": "P-113", "action": "lock-ledger-period", "resource_id": "RES-031", "description": "Allows locking accounting periods in the ledger"}}',
            '{"ok": true, "role_permissions": [{"role_id": "ROL-039", "permission_id": "P-113", "role": {"role_id": "ROL-039", "role_name": "finance-lead", "description": "Lead role for the finance department.", "is_temporary": false}, "permission": {"permission_id": "P-113", "action": "lock-ledger-period", "resource_id": "RES-031", "description": "Allows locking accounting periods in the ledger"}}]}',
            '{"ok": true, "user_id": "U-006", "has_sod_conflicts": false, "conflict_count": 0, "conflicts": [], "checked_on": "2025-08-08T12:00:00.000000Z"}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_038",
        instruction=(
            "You are HR_ONBOARD_BOT. Finance analyst Lisa Anderson is changing her last name to Andrews and taking leave until EOD December 1st, 2025. "
            "Update her profile and set her account to inactive during the leave. "
            "Create a time-bound policy exception so that teammate Katherine Hall can 'restart-prod-service' until EOD December 1st, 2025, to be reviewed by Finance lead Jessica Garcia."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="is_admin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="get_user", kwargs={"first_name": "Lisa", "last_name": "Anderson"}),
            Action(name="get_user", kwargs={"username": "landrews", "allow_missing": True}),
            Action(name="update_user", kwargs={"user_id": "U-012", "last_name": "Andrews"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "U-032 updated user U-012 name to Lisa Andrews; username set to landrews; email set to lisa.andrews@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#finance",
                    "message": "User U-012 updated by U-032: username landerson -> landrews; email set to lisa.andrews@taucorp.com; name set to Lisa Andrews.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="update_user", kwargs={"user_id": "U-012", "status": "INACTIVE"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "HR_ONBOARD_BOT changed user U-012 status to INACTIVE",
                },
            ),
            Action(name="get_user", kwargs={"first_name": "Katherine", "last_name": "Hall"}),
            Action(name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}),
            Action(name="is_admin", kwargs={"user_id": "U-006", "include_role_details": True}),
            Action(name="get_permission", kwargs={"action": "restart-prod-service"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-024",
                    "permission_id": "P-061",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform restart-prod-service until 2025-12-01",
                    "expires_on": "2025-12-01T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-032",
                    "target_id": "PE-021",
                    "details": "HR_ONBOARD_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-032",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="get_user", kwargs={"username": "landrews"}),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "user": {"user_id": "U-012", "username": "landrews", "email": "lisa.andrews@taucorp.com", "department": "Finance", "status": "INACTIVE", "mfa_enabled": true}}',
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-024", "permission_id": "P-061", "reviewed_by": "U-006", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-12-01T23:59:59.000000Z", "reason": "Temporary access to perform restart-prod-service until 2025-12-01", "status": "PENDING_REVIEW"}}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_039",
        instruction=(
            "You are HR_ONBOARD_BOT. Operations engineer Patrick Carter is changing his last name to Carver and will be on leave until EOD October 31st, 2025. "
            "Update his profile and set his account to inactive during leave. "
            "While Patrick is on leave, assign a temporary 'operations-incident-response' role to Michael Davis for coverage."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="is_admin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="get_user", kwargs={"first_name": "Patrick", "last_name": "Carter"}),
            Action(name="get_user", kwargs={"username": "pcarver", "allow_missing": True}),
            Action(name="update_user", kwargs={"user_id": "U-029", "last_name": "Carver"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "U-032 updated user U-029 name to Patrick Carver; username set to pcarver; email set to patrick.carver@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#operations",
                    "message": "User U-029 updated by U-032: username pcarter -> pcarver; email set to patrick.carver@taucorp.com; name set to Patrick Carver.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="update_user", kwargs={"user_id": "U-029", "status": "INACTIVE"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "HR_ONBOARD_BOT changed user U-029 status to INACTIVE",
                },
            ),
            Action(name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-005", "only_active": True}),
            Action(name="get_role", kwargs={"role_name": "operations-incident-response"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-005",
                    "role_id": "ROL-023",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-10-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-005",
                    "details": "Role ROL-023 added to U-005",
                },
            ),
            Action(name="get_user", kwargs={"username": "pcarver"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-005", "only_active": True}),
        ],
        outputs=[
            '{"user_id": "U-029", "username": "pcarver", "email": "patrick.carver@taucorp.com", "department": "Operations", "status": "INACTIVE", "mfa_enabled": true}',
            '{"user_id": "U-005", "assignments": [{"role_id": "ROL-021"}, {"role_id": "ROL-038"}, {"role_id": "ROL-023"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_040",
        instruction=(
            "You're Operations lead Michael Davis. You must review Ashley Wilson's pending access request for recruitment manager access. "
            "Decide the access request according to policy, then return the updated request and Ashley's roles."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005"},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Ashley", "last_name": "Wilson"}
            ),
            Action(
                name="get_access_request",
                kwargs={"user_id": "U-010", "status": "PENDING"},
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-010",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="decide_access_request",
                kwargs={
                    "request_id": "AR-037",
                    "reviewer_id": "U-005",
                    "decision": "REJECTED",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ACCESS_REJECTED",
                    "actor_id": "U-005",
                    "target_id": "AR-037",
                    "details": "Access request AR-037 was rejected by U-005",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "michael.davis@taucorp.com",
                    "receiver": "ashley.wilson@taucorp.com",
                    "subject": "Access Request REJECTED",
                    "text_content": "Your access request AR-037 has been REJECTED.",
                },
            ),
            Action(name="get_access_request", kwargs={"request_id": "AR-037"}),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-010",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"access_request": {"request_id": "AR-037", "user_id": "U-010", "resource_id": "RES-041", "requested_role_id": "ROL-019", "justification": "Need to post a new job opening.", "status": "REJECTED", "submitted_at": "2024-05-30 19:00:00+00:00", "reviewed_by": "U-005", "decision_at": "2025-08-08T12:00:00.000000Z"}}',
            '{"user_id": "U-010", "assignments": [{"role_id": "ROL-016", "role_name": "hr-base", "description": "Basic access for human resources staff"}, {"role_id": "ROL-019", "role_name": "hr-recruitment-manager", "description": "Manages job postings and candidate applications"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_041",
        instruction=(
            "You are RBAC_BOT responding to a critical security incident tied to SIEM alert ALRT-012. "
            "You must consult the open ticket that regards ALRT-012."
            "You must ensure the flagged user is suspended and holds no active roles."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_hubspot_ticket",
                kwargs={"alert_id": "ALRT-012", "status": "OPEN"},
            ),
            Action(name="get_siem_alert", kwargs={"alert_id": "ALRT-012"}),
            Action(
                name="can_access_resource",
                kwargs={"user_id": "U-004", "resource_id": "RES-014"},
            ),
            Action(
                name="update_user",
                kwargs={
                    "user_id": "U-004",
                    "status": "SUSPENDED",
                    "updated_by": "U-031",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-031",
                    "target_id": "U-004",
                    "details": "RBAC_BOT changed user U-004 status to SUSPENDED",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-004",
                    "only_active": False,
                    "include_role_details": False,
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-004",
                    "role_id": "ROL-016",
                    "action": "REMOVE",
                    "assigned_by": "U-031",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-004",
                    "details": "Role ROL-016 removed from U-004",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-004",
                    "role_id": "ROL-037",
                    "action": "REMOVE",
                    "assigned_by": "U-031",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-004",
                    "details": "Role ROL-037 removed from U-004",
                },
            ),
            Action(
                name="update_hubspot_ticket",
                kwargs={"ticket_id": "TI-053", "status": "CLOSED"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "TICKET_CLOSED",
                    "actor_id": "U-031",
                    "target_id": "TI-053",
                    "details": "Closed security incident ticket TI-053",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#security-incidents",
                    "message": "ALRT-012 processed: U-004 suspended and security incident ticket closed.",
                    "username": "RBAC_BOT",
                    "timestamp": "2025-08-08T12:00:00.000000Z",
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-004"}),
            Action(
                name="get_user_roles", kwargs={"user_id": "U-004", "only_active": True}
            ),
            Action(
                name="get_session", kwargs={"user_id": "U-004", "only_active": True}
            ),
        ],
        outputs=[
            '{"ok": true, "ticket": {"ticket_id": "TI-053", "created_at": "2025-06-02 21:30:00+00:00", "updated_at": "2025-08-08T12:00:00.000000Z", "subject": "SIEM Alert: Unauthorized Access Attempt", "description": "SIEM Alert ALRT-012: Critical severity alert for user U-004 attempting to access resource RES-014.", "status": "CLOSED", "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-004", "category": "SECURITY_INCIDENT", "closed_at": "2025-08-08T12:00:00.000000Z"}}',
            '{"user_id": "U-004", "username": "ejones", "email": "emily.jones@taucorp.com", "department": "Human Resources", "status": "SUSPENDED", "mfa_enabled": true}',
            '{"user_id": "U-004", "assignments": []}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_042",
        instruction=(
            "You are RBAC_BOT. Sales analyst Matthew Lopez needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 5th, 2025). "
            "Matthew claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Jessica Garcia as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Matthew", "last_name": "Lopez"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-009",
                    "permission_id": "P-084",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-05",
                    "expires_on": "2025-10-05T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-009", "permission_id": "P-084", "reviewed_by": "U-006", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-10-05T23:59:59.000000Z", "reason": "Temporary access to perform submit-tax-filing until 2025-10-05", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_043",
        instruction=(
            "You are RBAC_BOT. There has been a detected security breach and you must enforce MFA for the Operations department (exclude bots). "
            "Enable MFA for any ACTIVE Operations user who has it disabled and is not a bot (U-031 or U-033), "
            "additionally, remove any active (non base) roles they may have."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={
                    "department": "Operations",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-005", "mfa_enabled": True, "status": "INACTIVE"},
            ),
            Action(
                name="get_session", kwargs={"user_id": "U-005", "only_active": True}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_MFA_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-005",
                    "details": "RBAC_BOT changed user U-005 mfa_enabled to True",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "rbac@taucorp.com",
                    "receiver": "michael.davis@taucorp.com",
                    "subject": "MFA Updated",
                    "text_content": "Your MFA setting has been updated to True. Please review your account settings.",
                },
            ),
            Action(
                name="get_user_roles", kwargs={"user_id": "U-005", "only_active": True}
            ),
            Action(
                name="get_base_role_by_department",
                kwargs={"department": "Operations"},
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-005", "role_id": "ROL-038", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-005",
                    "details": "Role ROL-038 removed from U-005",
                },
            ),
            Action(
                name="get_user_roles", kwargs={"user_id": "U-005", "only_active": True}
            ),
        ],
        outputs=[
            '{"ok": true, "user": {"user_id": "U-005", "username": "mdavis", "email": "michael.davis@taucorp.com", "department": "Operations", "status": "INACTIVE", "mfa_enabled": true}}',
            '{"user_id": "U-005", "assignments": [{"role_id": "ROL-021"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_044",
        instruction=(
            "You are RBAC_BOT. HR partner Ashley Wilson needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 12th, 2025). "
            "Ashley claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Michael Davis as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Ashley", "last_name": "Wilson"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-010",
                    "permission_id": "P-084",
                    "reviewed_by": "U-005",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-12",
                    "expires_on": "2025-10-12T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-010", "permission_id": "P-084", "reviewed_by": "U-005", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-10-12T23:59:59.000000Z", "reason": "Temporary access to perform submit-tax-filing until 2025-10-12", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_045",
        instruction=(
            "You are RBAC_BOT. Engineer Daniel Taylor needs a time-bound policy exception to 'Configure CI/CD pipeline'. "
            "You must create the exception for the appropriate engineering permission, set to expire EOD a week from today August 8th, 2025 with Alex Johnson as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Daniel", "last_name": "Taylor"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Alex", "last_name": "Johnson"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="get_permission",
                kwargs={"description": "Configure CI/CD pipeline"},
            ),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-019",
                    "permission_id": "P-005",
                    "reviewed_by": "U-001",
                    "reason": "Temporary access to perform configure-pipeline until 2025-08-15",
                    "expires_on": "2025-08-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                    "username": "RBAC_BOT",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-019", "permission_id": "P-005", "reviewed_by": "U-001", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-08-15T23:59:59.000000Z", "reason": "Temporary access to perform configure-pipeline until 2025-08-15", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_046",
        instruction=(
            "You are RBAC_BOT. Operations engineer Jeffery Green needs a time-bound policy exception to 'Modify network firewall rules'. "
            "You must create the exception for the appropriate operations permission set to expire EOD September 15th 2025 with Michael Davis as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jeffery", "last_name": "Green"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="get_permission",
                kwargs={"description": "Modify network firewall rules"},
            ),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-023",
                    "permission_id": "P-067",
                    "reviewed_by": "U-005",
                    "reason": "Temporary access to perform modify-firewall-rules until 2025-09-15",
                    "expires_on": "2025-09-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            ' {"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-023", "permission_id": "P-067", "reviewed_by": "U-005", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-09-15T23:59:59.000000Z", "reason": "Temporary access to perform modify-firewall-rules until 2025-09-15", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_047",
        instruction=(
            "You are RBAC_BOT. HR specialist Brittany King needs a time-bound policy exception to 'Modify employee benefits in system'. "
            "You must create the exception for the appropriate HR permission set to expire EOD October 31st, 2025 with Michael Davis as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Brittany", "last_name": "King"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="get_permission",
                kwargs={"description": "Modify employee benefits in system"},
            ),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-022",
                    "permission_id": "P-057",
                    "reviewed_by": "U-005",
                    "reason": "Temporary access to perform modify-benefits until 2025-10-31",
                    "expires_on": "2025-10-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-022", "permission_id": "P-057", "reviewed_by": "U-005", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-10-31T23:59:59.000000Z", "reason": "Temporary access to perform modify-benefits until 2025-10-31", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_048",
        instruction=(
            "You are RBAC_BOT. Engineer Brian Taylor needs a time-bound policy exception to 'Deploy updates to customer-facing API'. "
            "You must create the exception for the appropriate engineering permission with Alex Johnson as the reviewer. "
            "The exception should expire at EOD August 31st, 2025."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Brian", "last_name": "Taylor"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Alex", "last_name": "Johnson"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="get_permission",
                kwargs={"description": "Deploy updates to customer-facing API"},
            ),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-013",
                    "permission_id": "P-012",
                    "reviewed_by": "U-001",
                    "reason": "Temporary access to perform deploy-api until 2025-08-31",
                    "expires_on": "2025-08-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                    "username": "RBAC_BOT",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-013", "permission_id": "P-012", "reviewed_by": "U-001", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-08-31T23:59:59.000000Z", "reason": "Temporary access to perform deploy-api until 2025-08-31", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_049",
        instruction=(
            "You are RBAC_BOT. Marketing specialist Angela Phillips needs a time-bound policy exception to 'Send email marketing campaigns'. "
            "You must create the exception for the appropriate marketing permission with Sarah Williams as the reviewer. "
            "The exception should expire at EOD September 30th, 2025."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Angela", "last_name": "Phillips"},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Sarah", "last_name": "Williams"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-002", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "send-email-campaign"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-026",
                    "permission_id": "P-022",
                    "reviewed_by": "U-002",
                    "reason": "Temporary access to perform send-email-campaign until 2025-09-30",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                    "username": "RBAC_BOT",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="liam",
        user_id="liam_050",
        instruction=(
            "You are RBAC_BOT. Finance analyst Lisa Anderson needs a time-bound policy exception to 'Approve invoices in invoicing system'. "
            "You must create the exception for the appropriate finance permission with Jessica Garcia as the reviewer. "
            "The exception should expire at EOD September 15th, 2025."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Lisa", "last_name": "Anderson"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "approve-invoice"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-012",
                    "permission_id": "P-078",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform approve-invoice until 2025-09-15",
                    "expires_on": "2025-09-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                    "username": "RBAC_BOT",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="liam",
        user_id="liam_051",
        instruction=(
            "You are HR_ONBOARD_BOT. Stephanie Adams has just gotten married and changed her last name to Rodriguez. "
            "You must update her user profile to accurately represent her new name. Because of her marriage, she is also taking time off until EOD August 31st, 2025."
            "You must ensure her account is inactive during her leave. During her leave, Katherine Hall will be taking over her auditing duties."
            "Katherine needs the 'finance-audit-access' role."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Stephanie", "last_name": "Adams"},
            ),
            Action(
                name="get_user",
                kwargs={"username": "srodriguez", "allow_missing": True},
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-018", "last_name": "Rodriguez"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-018",
                    "details": "U-032 updated user U-018 name to Stephanie Rodriguez; username set to srodriguez; email set to stephanie.rodriguez@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#finance",
                    "message": "User U-018 updated by U-032: username sadams -> srodriguez; email set to stephanie.rodriguez@taucorp.com; name set to Stephanie Rodriguez.",
                    "username": "RBAC_BOT",
                },
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-018", "status": "INACTIVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-018",
                    "details": "HR_ONBOARD_BOT changed user U-018 status to INACTIVE",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Katherine", "last_name": "Hall"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-024",
                    "only_active": True,
                },
            ),
            Action(
                name="get_role",
                kwargs={"role_name": "finance-audit-access"},
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-024",
                    "role_id": "ROL-033",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-08-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-024",
                    "details": "Role ROL-033 added to U-024",
                },
            ),
            Action(name="get_user", kwargs={"username": "srodriguez"}),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-024",
                    "only_active": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-018", "username": "srodriguez", "email": "stephanie.rodriguez@taucorp.com", "department": "Finance", "status": "INACTIVE", "mfa_enabled": true}',
            '{"user_id": "U-024", "assignments": [{"role_id": "ROL-029"}, {"role_id": "ROL-033"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_052",
        instruction=(
            "You are HR_ONBOARD_BOT. Ashley Wilson has transitioned and updated their first name to Noah. "
            "You must update the user profile to reflect the new first name. Because they are taking leave, set her account to inactive during the leave. "
            "While they are on leave, Laura Jackson needs a time-bound policy exception until EOD September 30th, 2025 to be reviewed by Emily Jones so that she can temporarily "
            "'Process payroll in the system' to cover duties."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Ashley", "last_name": "Wilson"}
            ),
            Action(
                name="get_user", kwargs={"username": "nwilson", "allow_missing": True}
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-010", "first_name": "Noah"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-010",
                    "details": "U-032 updated user U-010 name to Noah Wilson; username set to nwilson; email set to noah.wilson@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#human-resources",
                    "message": "User U-010 updated by U-032: username awilson -> nwilson; email set to noah.wilson@taucorp.com; name set to Noah Wilson.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-010", "status": "INACTIVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-010",
                    "details": "HR_ONBOARD_BOT changed user U-010 status to INACTIVE",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Laura", "last_name": "Jackson"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Emily", "last_name": "Jones"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-004", "include_role_details": True},
            ),
            Action(
                name="get_permission",
                kwargs={"description": "Process payroll in the system"},
            ),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-016",
                    "permission_id": "P-051",
                    "reviewed_by": "U-004",
                    "reason": "Temporary access to perform process-payroll until 2025-09-30",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-032",
                    "target_id": "PE-021",
                    "details": "HR_ONBOARD_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-032",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="get_user", kwargs={"username": "nwilson"}),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "user": {"user_id": "U-010", "username": "nwilson", "email": "noah.wilson@taucorp.com", "department": "Human Resources", "status": "INACTIVE", "mfa_enabled": true}}',
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-016", "permission_id": "P-051", "reviewed_by": "U-004", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-09-30T23:59:59.000000Z", "reason": "Temporary access to perform process-payroll until 2025-09-30", "status": "PENDING_REVIEW"}}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_053",
        instruction=(
            "You are HR_ONBOARD_BOT. Sales rep Kevin Harris is changing his last name to Nguyen and taking a leave of absence. "
            "You must update his profile accordingly and set his account to inactive while he is on leave. "
            "While Kevin is on leave, you must create a policy exception until EOD October 15th, 2025 to be reviewed by David Brown "
            "so Sales teammate Paul Ellis can temporarily 'Calculate commissions with the tool' to cover duties."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Kevin", "last_name": "Harris"}
            ),
            Action(
                name="get_user", kwargs={"username": "knguyen", "allow_missing": True}
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-015", "last_name": "Nguyen"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-015",
                    "details": "U-032 updated user U-015 name to Kevin Nguyen; username set to knguyen; email set to kevin.nguyen@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#sales",
                    "message": "User U-015 updated by U-032: username kharris -> knguyen; email set to kevin.nguyen@taucorp.com; name set to Kevin Nguyen.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-015", "status": "INACTIVE"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-015",
                    "details": "HR_ONBOARD_BOT changed user U-015 status to INACTIVE",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Paul", "last_name": "Ellis"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "David", "last_name": "Brown"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-003", "include_role_details": True},
            ),
            Action(
                name="get_permission",
                kwargs={"description": "Calculate commissions with the tool"},
            ),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-021",
                    "permission_id": "P-043",
                    "reviewed_by": "U-003",
                    "reason": "Temporary access to perform calculate-commission until 2025-10-15",
                    "expires_on": "2025-10-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-032",
                    "target_id": "PE-021",
                    "details": "HR_ONBOARD_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-032",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="get_user", kwargs={"username": "knguyen"}),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"user_id": "U-015", "username": "knguyen", "email": "kevin.nguyen@taucorp.com", "department": "Sales", "status": "INACTIVE", "mfa_enabled": true}',
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-021", "permission_id": "P-043", "reviewed_by": "U-003", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-10-15T23:59:59.000000Z", "reason": "Temporary access to perform calculate-commission until 2025-10-15", "status": "PENDING_REVIEW"}}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_054",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineer Daniel Taylor is changing his first name to Nathan and taking a leave of absense until September 30th, 2025. "
            "You must update his profile and set his account to inactive during leave. "
            "While Daniel is on leave, grant a temporary 'engineering-db-schema' role to Ryan Baker until EOD September 30th, 2025 to cover production debugging."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Daniel", "last_name": "Taylor"}
            ),
            Action(
                name="get_user", kwargs={"username": "ntaylor", "allow_missing": True}
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-019", "first_name": "Nathan"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "U-032 updated user U-019 name to Nathan Taylor; username set to ntaylor; email set to nathan.taylor@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#engineering",
                    "message": "User U-019 updated by U-032: username dtaylor -> ntaylor; email set to nathan.taylor@taucorp.com; name set to Nathan Taylor.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-019", "status": "INACTIVE"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "HR_ONBOARD_BOT changed user U-019 status to INACTIVE",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Ryan", "last_name": "Baker"}
            ),
            Action(
                name="get_user_roles", kwargs={"user_id": "U-025", "only_active": True}
            ),
            Action(name="get_role", kwargs={"role_name": "engineering-db-schema"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-025",
                    "role_id": "ROL-004",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-025",
                    "details": "Role ROL-004 added to U-025",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-025",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"username": "ntaylor"}),
        ],
        outputs=[
            '{"user_id": "U-025", "assignments": [{"role_id": "ROL-001", "role_name": "engineering-base", "description": "Basic access for engineering staff"}, {"role_id": "ROL-004", "role_name": "engineering-db-schema", "description": "Ability to modify database schemas"}]}',
            '{"user_id": "U-019", "username": "ntaylor", "email": "nathan.taylor@taucorp.com", "department": "Engineering", "status": "INACTIVE", "mfa_enabled": false}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_055",
        instruction=(
            "You are HR_ONBOARD_BOT. Operations engineer Jeffery Green is changing his first name to Geoffrey and taking leave. "
            "You must update his profile accordingly and set his account to inactive during leave. "
            "While Jeffery is on leave, grant a temporary 'operations-incident-response' coverage role to Operations teammate Patrick Carter until EOD October 31st, 2025."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jeffery", "last_name": "Green"}
            ),
            Action(
                name="get_user", kwargs={"username": "ggreen", "allow_missing": True}
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-023", "first_name": "Geoffrey"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-023",
                    "details": "U-032 updated user U-023 name to Geoffrey Green; username set to ggreen; email set to geoffrey.green@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#operations",
                    "message": "User U-023 updated by U-032: username jgreen -> ggreen; email set to geoffrey.green@taucorp.com; name set to Geoffrey Green.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-023", "status": "INACTIVE"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-023",
                    "details": "HR_ONBOARD_BOT changed user U-023 status to INACTIVE",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Patrick", "last_name": "Carter"}
            ),
            Action(
                name="get_role", kwargs={"role_name": "operations-incident-response"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-023",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-10-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "Role ROL-023 added to U-029",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-029",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"username": "ggreen"}),
        ],
        outputs=[
            '{"user_id": "U-029", "assignments": [{"role_id": "ROL-021", "role_name": "operations-base", "description": "Basic access for operations staff"}, {"role_id": "ROL-023", "role_name": "operations-incident-response", "description": "Responds to and resolves system incidents"}]}',
            '{"user_id": "U-023", "username": "ggreen", "email": "geoffrey.green@taucorp.com", "department": "Operations", "status": "INACTIVE", "mfa_enabled": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_056",
        instruction=(
            "You are HR_ONBOARD_BOT. Marketing analyst Nicole Thomas is changing her last name to Thompson and going on leave. "
            "You must update her profile and set her account to inactive during leave. "
            "While Nicole is on leave, you must create a policy exception to be reviewed by Sarah Williams so Marketing teammate Angela Phillips can temporarily 'export-marketing-data' until EOD October 10th, 2025."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Nicole", "last_name": "Thomas"}
            ),
            Action(
                name="get_user", kwargs={"username": "nthompson", "allow_missing": True}
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-014", "last_name": "Thompson"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "U-032 updated user U-014 name to Nicole Thompson; username set to nthompson; email set to nicole.thompson@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#marketing",
                    "message": "User U-014 updated by U-032: username nthomas -> nthompson; email set to nicole.thompson@taucorp.com; name set to Nicole Thompson.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-014", "status": "INACTIVE"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "HR_ONBOARD_BOT changed user U-014 status to INACTIVE",
                },
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Angela", "last_name": "Phillips"},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Sarah", "last_name": "Williams"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-002", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "export-marketing-data"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-026",
                    "permission_id": "P-026",
                    "reviewed_by": "U-002",
                    "reason": "Temporary access to perform export-marketing-data until 2025-10-10",
                    "expires_on": "2025-10-10T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-032",
                    "target_id": "PE-021",
                    "details": "HR_ONBOARD_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-032",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="get_user", kwargs={"username": "nthompson"}),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "user": {"user_id": "U-014", "username": "nthompson", "email": "nicole.thompson@taucorp.com", "department": "Marketing", "status": "INACTIVE", "mfa_enabled": false}}',
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-026", "permission_id": "P-026", "reviewed_by": "U-002", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-10-10T23:59:59.000000Z", "reason": "Temporary access to perform export-marketing-data until 2025-10-10", "status": "PENDING_REVIEW"}}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_057",
        instruction=(
            "You are HR_ONBOARD_BOT. Finance analyst Lisa Anderson is changing her first name to Elisabeth and taking leave until November 15th, 2025. "
            "You must update her profile and set her account to inactive during leave. "
            "While Lisa is on leave, you must grant a temporary 'finance-invoice-processor' role to teammate Katherine Hall to cover responsibilities."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Lisa", "last_name": "Anderson"}
            ),
            Action(
                name="get_user", kwargs={"username": "eanderson", "allow_missing": True}
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-012", "first_name": "Elisabeth"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "U-032 updated user U-012 name to Elisabeth Anderson; username set to eanderson; email set to elisabeth.anderson@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#finance",
                    "message": "User U-012 updated by U-032: username landerson -> eanderson; email set to elisabeth.anderson@taucorp.com; name set to Elisabeth Anderson.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-012", "status": "INACTIVE"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "HR_ONBOARD_BOT changed user U-012 status to INACTIVE",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Katherine", "last_name": "Hall"}
            ),
            Action(
                name="get_user_roles", kwargs={"user_id": "U-024", "only_active": True}
            ),
            Action(name="get_role", kwargs={"role_name": "finance-invoice-processor"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-024",
                    "role_id": "ROL-031",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-11-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-024",
                    "details": "Role ROL-031 added to U-024",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-024",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"username": "eanderson"}),
        ],
        outputs=[
            '{"user_id": "U-024", "assignments": [{"role_id": "ROL-029", "role_name": "finance-base", "description": "Basic access for finance staff"}, {"role_id": "ROL-031", "role_name": "finance-invoice-processor", "description": "Processes customer invoices and payments"}]}',
            '{"user_id": "U-012", "username": "eanderson", "email": "elisabeth.anderson@taucorp.com", "department": "Finance", "status": "INACTIVE", "mfa_enabled": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_058",
        instruction=(
            "You are HR_ONBOARD_BOT. Senior Marketing Lead Sarah Williams (Marketing department) is beginning a 12-month pregnancy leave effective today 2025-08-08. "
            "You must set her account to inactive, remove only her marketing-lead role."
            "We're onboarding a temporary contractor replacement named Julia Perez, "
            "she needs a temporary marketing-lead role that expires EOD 2026-08-08. "
            "Return the replacement's active roles and Sarah's updated inactive user record."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Sarah", "last_name": "Williams"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-002",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-002", "status": "INACTIVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-002",
                    "details": "HR_ONBOARD_BOT changed user U-002 status to INACTIVE",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-002",
                    "role_id": "ROL-035",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-002",
                    "details": "Role ROL-035 removed from U-002",
                },
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "jperez",
                    "email": "julia.perez@taucorp.com",
                    "department": "Marketing",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="get_base_role_by_department",
                kwargs={"department": "Marketing"},
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-006",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-006 added to U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-035",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2026-08-08T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-035 added to U-034",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "onboarding@taucorp.com",
                    "receiver": "julia.perez@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Julia, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-002"}),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-006", "role_name": "marketing-base", "description": "Basic access for marketing staff"}, {"role_id": "ROL-035", "role_name": "marketing-lead", "description": "Lead role for the marketing department."}]}',
            '{"user_id": "U-002", "username": "swilliams", "email": "sarah.williams@taucorp.com", "department": "Marketing", "status": "INACTIVE", "mfa_enabled": false}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_059",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineering Lead Alex Johnson (Engineering department) is beginning a 12-month pregnancy leave effective today 2025-08-08. "
            "You must set his account to inactive and remove his engineering-lead role. "
            "We're onboarding a temporary contractor replacement for Alex named Olivia Martin. "
            "You must assign Olivia a temporary engineering-lead role that expires when Alex returns EOD 2026-08-08. "
            "Return the replacement's active roles and Alex's updated inactive user record."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Alex", "last_name": "Johnson"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-001",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-001", "status": "INACTIVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-001",
                    "details": "HR_ONBOARD_BOT changed user U-001 status to INACTIVE",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-001",
                    "role_id": "ROL-034",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-001",
                    "details": "Role ROL-034 removed from U-001",
                },
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "omartin",
                    "email": "olivia.martin@taucorp.com",
                    "department": "Engineering",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="get_base_role_by_department", kwargs={"department": "Engineering"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-001",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-001 added to U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-034",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2026-08-08T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-034 added to U-034",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "onboarding@taucorp.com",
                    "receiver": "olivia.martin@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Olivia, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-001"}),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-001", "role_name": "engineering-base", "description": "Basic access for engineering staff"}, {"role_id": "ROL-034", "role_name": "engineering-lead", "description": "Lead role for the engineering department."}]}',
            '{"user_id": "U-001", "username": "ajohnson", "email": "alex.johnson@taucorp.com", "department": "Engineering", "status": "INACTIVE", "mfa_enabled": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_060",
        instruction=(
            "You are HR_ONBOARD_BOT. Operations Lead Michael Davis (Operations department) is beginning a 12-month pregnancy leave effective today 2025-08-08. "
            "You must set his account to inactive and remove his operations-lead role. "
            "We're onboarding a temporary contractor replacement named Hannah Scott for Operations. "
            "You must assign Hannah a temporary operations-lead role that expires EOD 2026-08-08. "
            "Return the replacement's active roles and Michael's updated inactive user record."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032"},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-005",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-005", "status": "INACTIVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-005",
                    "details": "HR_ONBOARD_BOT changed user U-005 status to INACTIVE",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-005",
                    "role_id": "ROL-038",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-005",
                    "details": "Role ROL-038 removed from U-005",
                },
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "hscott",
                    "email": "hannah.scott@taucorp.com",
                    "department": "Operations",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="get_base_role_by_department", kwargs={"department": "Operations"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-021",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-021 added to U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-038",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2026-08-08T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-038 added to U-034",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "onboarding@taucorp.com",
                    "receiver": "hannah.scott@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Hannah, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-005"}),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-021", "role_name": "operations-base", "description": "Basic access for operations staff"}, {"role_id": "ROL-038", "role_name": "operations-lead", "description": "Lead role for the operations department."}]}',
            '{"user_id": "U-005", "username": "mdavis", "email": "michael.davis@taucorp.com", "department": "Operations", "status": "INACTIVE", "mfa_enabled": false}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_061",
        instruction=(
            "You are HR_ONBOARD_BOT. Finance Lead Jessica Garcia (Finance department) is beginning a 12-month pregnancy leave effective today 2025-08-08. "
            "You must set her account to inactive and remove her finance-lead role."
            "We're onboarding a temporary contractor replacement named Megan Foster, "
            "she needs a temporary finance-lead role that expires EOD 2026-08-08. "
            "Return the replacement's active roles and Jessica's updated inactive user record."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-006",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-006", "status": "INACTIVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-006",
                    "details": "HR_ONBOARD_BOT changed user U-006 status to INACTIVE",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-006",
                    "role_id": "ROL-039",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-006",
                    "details": "Role ROL-039 removed from U-006",
                },
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "mfoster",
                    "email": "megan.foster@taucorp.com",
                    "department": "Finance",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="get_base_role_by_department", kwargs={"department": "Finance"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-029",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-029 added to U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-039",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2026-08-08T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-039 added to U-034",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "onboarding@taucorp.com",
                    "receiver": "megan.foster@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Megan, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-006"}),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-029", "role_name": "finance-base", "description": "Basic access for finance staff"}, {"role_id": "ROL-039", "role_name": "finance-lead", "description": "Lead role for the finance department."}]}',
            '{"user_id": "U-006", "username": "jgarcia", "email": "jessica.garcia@taucorp.com", "department": "Finance", "status": "INACTIVE", "mfa_enabled": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_062",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineer Daniel Taylor is transferring from Engineering to Operations. "
            "You must remove Daniel's prior engineering roles, he now needs the base role for Operations and operations-server-monitor role. "
            "Return his updated active roles and updated user record."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Daniel", "last_name": "Taylor"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-019",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-019", "department": "Operations"},
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-019", "role_id": "ROL-004", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "Role ROL-004 removed from U-019",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-019", "role_id": "ROL-005", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "Role ROL-005 removed from U-019",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-019", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "Role ROL-001 removed from U-019",
                },
            ),
            Action(
                name="get_base_role_by_department", kwargs={"department": "Operations"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-019",
                    "role_id": "ROL-021",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "Role ROL-021 added to U-019",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "operations-server-monitor"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-019",
                    "role_id": "ROL-022",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "Role ROL-022 added to U-019",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-019",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-019"}),
        ],
        outputs=[
            '{"user_id": "U-019", "assignments": [{"role_id": "ROL-021", "role_name": "operations-base", "description": "Basic access for operations staff"}, {"role_id": "ROL-022", "role_name": "operations-server-monitor", "description": "Monitors server health and performance"}]}',
            '{"user_id": "U-019", "username": "dtaylor", "email": "daniel.taylor@taucorp.com", "department": "Operations", "status": "ACTIVE", "mfa_enabled": false}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_063",
        instruction=(
            "You are HR_ONBOARD_BOT. Finance specialist Lisa Anderson is transferring from Finance to Human Resources. "
            "You must remove Lisa's finance roles, then assign hr-base and hr-benefits-admin. "
            "Return her updated active roles and updated user record."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Lisa", "last_name": "Anderson"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-012",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-012", "department": "Human Resources"},
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-012", "role_id": "ROL-032", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "Role ROL-032 removed from U-012",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-012", "role_id": "ROL-031", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "Role ROL-031 removed from U-012",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-012", "role_id": "ROL-029", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "Role ROL-029 removed from U-012",
                },
            ),
            Action(
                name="get_base_role_by_department",
                kwargs={"department": "Human Resources"},
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-012",
                    "role_id": "ROL-016",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "Role ROL-016 added to U-012",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "hr-benefits-admin"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-012",
                    "role_id": "ROL-020",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "Role ROL-020 added to U-012",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-012",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-012"}),
        ],
        outputs=[
            '{"user_id": "U-012", "assignments": [{"role_id": "ROL-016", "role_name": "hr-base", "description": "Basic access for human resources staff"}, {"role_id": "ROL-020", "role_name": "hr-benefits-admin", "description": "Administers employee benefits programs"}]}',
            '{"user_id": "U-012", "username": "landerson", "email": "lisa.anderson@taucorp.com", "department": "Human Resources", "status": "ACTIVE", "mfa_enabled": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_064",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineer Brian Taylor is transferring from Engineering to Sales. "
            "You must remove Brian's engineering roles, he now needs the base role for Sales and the sales-reporting role. "
            "Return his updated active roles and updated user record."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Brian", "last_name": "Taylor"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-013",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-013", "department": "Sales"}
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-013", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-013",
                    "details": "Role ROL-001 removed from U-013",
                },
            ),
            Action(
                name="get_base_role_by_department",
                kwargs={"department": "Sales"},
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-013",
                    "role_id": "ROL-011",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-013",
                    "details": "Role ROL-011 added to U-013",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "sales-reporting"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-013",
                    "role_id": "ROL-014",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-013",
                    "details": "Role ROL-014 added to U-013",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-013",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-013"}),
        ],
        outputs=[
            '{"user_id": "U-013", "assignments": [{"role_id": "ROL-011", "role_name": "sales-base", "description": "Basic access for sales staff"}, {"role_id": "ROL-014", "role_name": "sales-reporting", "description": "Generates sales performance reports"}]}',
            '{"user_id": "U-013", "username": "btaylor", "email": "brian.taylor@taucorp.com", "department": "Sales", "status": "ACTIVE", "mfa_enabled": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_065",
        instruction=(
            "You are HR_ONBOARD_BOT. Marketing specialist Angela Phillips is transferring from Marketing to Engineering. "
            "You must update her department and remove all of her previous roles, then add engineering-base, engineering-code-commit, and engineering-qa-test. "
            "Return her updated active roles and updated user record."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Angela", "last_name": "Phillips"},
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-026",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="update_user",
                kwargs={"user_id": "U-026", "department": "Engineering"},
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-026", "role_id": "ROL-010", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-010 removed from U-026",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-026", "role_id": "ROL-007", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-007 removed from U-026",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-026", "role_id": "ROL-006", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-006 removed from U-026",
                },
            ),
            Action(
                name="get_base_role_by_department", kwargs={"department": "Engineering"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-001",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-001 added to U-026",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "engineering-code-commit"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-002",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-002 added to U-026",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "engineering-qa-test"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-005",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-005 added to U-026",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-026",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-026"}),
        ],
        outputs=[
            '{"user_id": "U-026", "assignments": [{"role_id": "ROL-001", "role_name": "engineering-base", "description": "Basic access for engineering staff"}, {"role_id": "ROL-002", "role_name": "engineering-code-commit", "description": "Permission to commit code to repositories"}, {"role_id": "ROL-005", "role_name": "engineering-qa-test", "description": "Access to QA testing environments"}]}',
            '{"user_id": "U-026", "username": "aphillips", "email": "angela.phillips@taucorp.com", "department": "Engineering", "status": "ACTIVE", "mfa_enabled": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_066",
        instruction=(
            "You are HR_ONBOARD_BOT. Operations engineer Patrick Carter is transferring from Operations to Finance. "
            "You must remove his currently held roles, he now needs the base role for finance and finance-read. "
            "Return his updated active roles and updated user record."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Patrick", "last_name": "Carter"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-029",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-029", "department": "Finance"}
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-029", "role_id": "ROL-021", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "Role ROL-021 removed from U-029",
                },
            ),
            Action(
                name="get_base_role_by_department", kwargs={"department": "Finance"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-029",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "Role ROL-029 added to U-029",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "finance-read"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-030",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "Role ROL-030 added to U-029",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-029",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-029"}),
        ],
        outputs=[
            '{"user_id": "U-029", "assignments": [{"role_id": "ROL-029", "role_name": "finance-base", "description": "Basic access for finance staff"}, {"role_id": "ROL-030", "role_name": "finance-read", "description": "Read-only access to finance data"}]}',
            '{"user_id": "U-029", "username": "pcarter", "email": "patrick.carter@taucorp.com", "department": "Finance", "status": "ACTIVE", "mfa_enabled": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_067",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineer Ryan Baker is transferring from Engineering to Finance. "
            "You must update his department on his user account, remove his engineering roles, "
            "for the transfer he needs the base finance role and the finance-invoice-processor role. "
            "Return his updated active roles and updated user record."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Ryan", "last_name": "Baker"}
            ),
            Action(
                name="get_user_roles",
                kwargs={"user_id": "U-025", "only_active": False},
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-025", "department": "Finance"}
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-025", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-025",
                    "details": "Role ROL-001 removed from U-025",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-025", "role_id": "ROL-003", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-025",
                    "details": "Role ROL-003 removed from U-025",
                },
            ),
            Action(
                name="get_base_role_by_department", kwargs={"department": "Finance"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-025",
                    "role_id": "ROL-029",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-025",
                    "details": "Role ROL-029 added to U-025",
                },
            ),
            Action(
                name="get_role",
                kwargs={"role_name": "finance-invoice-processor"},
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-025",
                    "role_id": "ROL-031",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-025",
                    "details": "Role ROL-031 added to U-025",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-025",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-025"}),
        ],
        outputs=[
            '{"user_id": "U-025", "assignments": [{"role_id": "ROL-029", "role_name": "finance-base", "description": "Basic access for finance staff"}, {"role_id": "ROL-031", "role_name": "finance-invoice-processor", "description": "Processes customer invoices and payments"}]}',
            '{"user_id": "U-025", "username": "rbaker", "email": "ryan.baker@taucorp.com", "department": "Finance", "status": "ACTIVE", "mfa_enabled": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_068",
        instruction=(
            "You are HR_ONBOARD_BOT. Sales rep Matthew Lopez is leaving the company effective today 2025-08-08. "
            "You must offboard Matthew and immediately onboard his replacement Sophia Turner (Sales). "
            "You must replicate Matthew's roles to Sophia. "
            "Return Sophia's active roles and Matthew's now-empty assignments."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Matthew", "last_name": "Lopez"}
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-009",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-009", "status": "DISABLED"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-009",
                    "details": "HR_ONBOARD_BOT changed user U-009 status to DISABLED",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-009", "role_id": "ROL-011", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-009",
                    "details": "Role ROL-011 removed from U-009",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-009", "role_id": "ROL-012", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-009",
                    "details": "Role ROL-012 removed from U-009",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-009", "role_id": "ROL-013", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-009",
                    "details": "Role ROL-013 removed from U-009",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "Offboard employee Matthew Lopez (mlopez)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "sturner",
                    "email": "sophia.turner@taucorp.com",
                    "department": "Sales",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-011",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-011 added to U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-012",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-012 added to U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-013",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-013 added to U-034",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "receiver": "sophia.turner@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Sophia, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@taucorp.com",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-009",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-011", "role_name": "sales-base", "description": "Basic access for sales staff"}, {"role_id": "ROL-012", "role_name": "sales-crm-access", "description": "Access to CRM system for customer data"}, {"role_id": "ROL-013", "role_name": "sales-lead-manager", "description": "Manages sales leads and opportunities"}]}',
            '{"user_id": "U-009", "assignments": []}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_069",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineer Christopher Rodriguez is leaving the company (effective 2025-08-08). "
            "You must offboard him and onboard replacement engineer Ethan Clark, replicating his roles (engineering-base, engineering-code-commit, engineering-prod-access). "
            "Return Ethan's roles and Christopher's empty assignments."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Christopher", "last_name": "Rodriguez"},
            ),
            Action(
                name="get_user_roles",
                kwargs={"user_id": "U-007", "only_active": False},
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-007", "status": "DISABLED"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-007",
                    "details": "HR_ONBOARD_BOT changed user U-007 status to DISABLED",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-007", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-007",
                    "details": "Role ROL-001 removed from U-007",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-007", "role_id": "ROL-002", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-007",
                    "details": "Role ROL-002 removed from U-007",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-007", "role_id": "ROL-003", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-007",
                    "details": "Role ROL-003 removed from U-007",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "Offboard employee Christopher Rodriguez (crodriguez)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "eclark",
                    "email": "ethan.clark@taucorp.com",
                    "department": "Engineering",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-001",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-001 added to U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-002",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-002 added to U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-003",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-003 added to U-034",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "receiver": "ethan.clark@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Ethan, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@taucorp.com",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-007",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-001", "role_name": "engineering-base", "description": "Basic access for engineering staff"}, {"role_id": "ROL-002", "role_name": "engineering-code-commit", "description": "Permission to commit code to repositories"}, {"role_id": "ROL-003", "role_name": "engineering-prod-access", "description": "Access to production environments for debugging"}]}',
            '{"user_id": "U-007", "assignments": []}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_070",
        instruction=(
            "You are HR_ONBOARD_BOT. HR specialist Brittany King is leaving the company. "
            "You must offboard Brittany and onboard her replacement Hannah Lee (HR) replicating Brittany's hr-base role. "
            "Return Hannah's roles and Brittany's empty assignments."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Brittany", "last_name": "King"}
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-022", "status": "DISABLED"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-022",
                    "details": "HR_ONBOARD_BOT changed user U-022 status to DISABLED",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={"user_id": "U-022", "only_active": False},
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-022", "role_id": "ROL-016", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-022",
                    "details": "Role ROL-016 removed from U-022",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "Offboard employee Brittany King (bking)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "hlee",
                    "email": "hannah.lee@taucorp.com",
                    "department": "Human Resources",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-016",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-016 added to U-034",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "receiver": "hannah.lee@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Hannah, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@taucorp.com",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-022",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-016", "role_name": "hr-base", "description": "Basic access for human resources staff"}]}',
            '{"user_id": "U-022", "assignments": []}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_071",
        instruction=(
            "You are HR_ONBOARD_BOT. Operations engineer Patrick Carter is leaving the company. "
            "You must offboard him and onboard replacement Liam Brooks replicating operations-base and operations-system-admin. "
            "Return Liam's roles and Patrick's empty assignments."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Patrick", "last_name": "Carter"}
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-029", "status": "DISABLED"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "HR_ONBOARD_BOT changed user U-029 status to DISABLED",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={"user_id": "U-029", "only_active": False},
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-029", "role_id": "ROL-021", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "Role ROL-021 removed from U-029",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "Offboard employee Patrick Carter (pcarter)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "lbrooks",
                    "email": "liam.brooks@taucorp.com",
                    "department": "Operations",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-021",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-021 added to U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-026",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-026 added to U-034",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "receiver": "liam.brooks@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Liam, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@taucorp.com",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-029",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-021", "role_name": "operations-base", "description": "Basic access for operations staff"}, {"role_id": "ROL-026", "role_name": "operations-system-admin", "description": "Full administrative access to all operations systems."}]}',
            '{"user_id": "U-029", "assignments": []}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_072",
        instruction=(
            "You are HR_ONBOARD_BOT. Finance analyst Marisa Cole is leaving the company. "
            "You must offboard her and onboard replacement Daniel Evans (Finance) replicating Marisa's roles for Daniel. "
            "Return Daniel's roles and Marisa's empty assignments."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Marisa", "last_name": "Cole"}
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-030", "status": "DISABLED"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-030",
                    "details": "HR_ONBOARD_BOT changed user U-030 status to DISABLED",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={"user_id": "U-030", "only_active": False},
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-030", "role_id": "ROL-029", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-030",
                    "details": "Role ROL-029 removed from U-030",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "Offboard employee Marisa Cole (mcole)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "devans",
                    "email": "daniel.evans@taucorp.com",
                    "department": "Finance",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-029",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-029 added to U-034",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "receiver": "daniel.evans@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Daniel, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@taucorp.com",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-030",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-029", "role_name": "finance-base", "description": "Basic access for finance staff"}]}',
            '{"user_id": "U-030", "assignments": []}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_073",
        instruction=(
            "You are HR_ONBOARD_BOT. Marketing specialist Angela Phillips is leaving the company. "
            "You must offboard Angela and onboard Carla Ramirez (Marketing) replicating all her active marketing roles. "
            "Return Carla's roles and Angela's empty assignments."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Angela", "last_name": "Phillips"},
            ),
            Action(
                name="update_user", kwargs={"user_id": "U-026", "status": "DISABLED"}
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "HR_ONBOARD_BOT changed user U-026 status to DISABLED",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={"user_id": "U-026", "only_active": False},
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-026", "role_id": "ROL-006", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-006 removed from U-026",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-026", "role_id": "ROL-007", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-007 removed from U-026",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={"user_id": "U-026", "role_id": "ROL-010", "action": "REMOVE"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-010 removed from U-026",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "Offboard employee Angela Phillips (aphillips)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="create_user",
                kwargs={
                    "actor_id": "U-032",
                    "username": "cramirez",
                    "email": "carla.ramirez@taucorp.com",
                    "department": "Marketing",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-006",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-006 added to U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-007",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-007 added to U-034",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-010",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-010 added to U-034",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "receiver": "carla.ramirez@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Carla, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@taucorp.com",
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-026",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-034", "assignments": [{"role_id": "ROL-006", "role_name": "marketing-base", "description": "Basic access for marketing staff"}, {"role_id": "ROL-007", "role_name": "marketing-campaign-manager", "description": "Manages marketing campaigns"}, {"role_id": "ROL-010", "role_name": "marketing-content-editor", "description": "Edits website and marketing content"}]}',
            '{"user_id": "U-026", "assignments": []}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_074",
        instruction=(
            "You are engineering lead Alex Johnson. The engineering team needs a new API gateway resource for microservices management. "
            "You must create a new resource called 'api-gateway-microservices' with HIGH criticality and ISO-27001 compliance, owned by Daniel Taylor. "
            "The resource needs: an associated role 'engineering-api-gateway-admin' with the description 'Manages API gateway configuration and routing for microservices'. "
            "and the permission 'configure-api-gateway' with the description: 'Configure routing and load balancing in API gateway' for the new role; give the role to Daniel Taylor. "
            "Return the new resource, role, permission, and Daniel's updated roles."
        ),
        actions=[
            Action(
                name="get_user",
                kwargs={"first_name": "Alex", "last_name": "Johnson"},
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Daniel", "last_name": "Taylor"},
            ),
            Action(
                name="create_resource",
                kwargs={
                    "name": "api-gateway-microservices",
                    "owner_id": "U-019",
                    "criticality": "HIGH",
                    "compliance_scope": "ISO-27001",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "RESOURCE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "RES-043",
                    "details": "Resource RES-043 created by U-001",
                },
            ),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "engineering-api-gateway-admin",
                    "description": "Manages API gateway configuration and routing for microservices",
                    "is_temporary": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ROLE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-001",
                },
            ),
            Action(
                name="create_permission",
                kwargs={
                    "action": "configure-api-gateway",
                    "resource_id": "RES-043",
                    "description": "Configure routing and load balancing in API gateway",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-001",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-001",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={
                    "role_id": "ROL-043",
                    "permission_id": "P-113",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Permission P-113 assigned to role ROL-043.",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-019",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-001",
                    "target_id": "U-019",
                    "details": "Role ROL-043 added to U-019",
                },
            ),
            Action(
                name="get_resource",
                kwargs={"resource_id": "RES-043"},
            ),
            Action(
                name="get_role",
                kwargs={"role_id": "ROL-043"},
            ),
            Action(
                name="get_permission",
                kwargs={"permission_id": "P-113"},
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-019",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"ok": true, "resource": {"resource_id": "RES-043", "name": "api-gateway-microservices", "owner_id": "U-019", "criticality": "HIGH", "compliance_scope": "ISO-27001"}}',
            '{"role_id": "ROL-043", "role_name": "engineering-api-gateway-admin", "description": "Manages API gateway configuration and routing for microservices", "is_temporary": false}',
            '{"ok": true, "permission": {"permission_id": "P-113", "action": "configure-api-gateway", "resource_id": "RES-043", "description": "Configure routing and load balancing in API gateway"}}',
            '{"user_id": "U-019", "assignments": [{"role_id": "ROL-001", "role_name": "engineering-base", "description": "Basic access for engineering staff"}, {"role_id": "ROL-004", "role_name": "engineering-db-schema", "description": "Ability to modify database schemas"}, {"role_id": "ROL-005", "role_name": "engineering-qa-test", "description": "Access to QA testing environments"}, {"role_id": "ROL-043", "role_name": "engineering-api-gateway-admin", "description": "Manages API gateway configuration and routing for microservices"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_075",
        instruction=(
            "You are engineering lead Alex Johnson. The sales team needs a new customer support ticketing system for better customer service management. "
            "You must create a new resource called 'customer-support-portal' with MEDIUM criticality and GDPR compliance, owned by Matthew Lopez from Sales. "
            "This resource needs: an associated role 'support-ticket-manager' for managing customer support tickets with the description 'Manages customer support tickets and escalations' "
            "and a permission 'manage-support-tickets' with the description: 'Create, update, and resolve customer support tickets' for the new role; give the role to Matthew Lopez. "
            "Return the new resource, role, permission, and Matthew's updated roles."
        ),
        actions=[
            Action(
                name="get_user",
                kwargs={"first_name": "Alex", "last_name": "Johnson"},
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Matthew", "last_name": "Lopez"},
            ),
            Action(
                name="create_resource",
                kwargs={
                    "name": "customer-support-portal",
                    "owner_id": "U-009",
                    "criticality": "MEDIUM",
                    "compliance_scope": "GDPR",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "RESOURCE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "RES-043",
                    "details": "Resource RES-043 created by U-001",
                },
            ),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "support-ticket-manager",
                    "description": "Manages customer support tickets and escalations",
                    "is_temporary": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ROLE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-001",
                },
            ),
            Action(
                name="create_permission",
                kwargs={
                    "action": "manage-support-tickets",
                    "resource_id": "RES-043",
                    "description": "Create, update, and resolve customer support tickets",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-001",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-001",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={
                    "role_id": "ROL-043",
                    "permission_id": "P-113",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Permission P-113 assigned to role ROL-043.",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-009",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-001",
                    "target_id": "U-009",
                    "details": "Role ROL-043 added to U-009",
                },
            ),
            Action(
                name="check_sod_conflicts",
                kwargs={
                    "user_id": "U-009",
                },
            ),
            Action(
                name="get_resource",
                kwargs={"resource_id": "RES-043"},
            ),
            Action(
                name="get_role",
                kwargs={"role_id": "ROL-043"},
            ),
            Action(
                name="get_permission",
                kwargs={"permission_id": "P-113"},
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-009",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"ok": true, "resource": {"resource_id": "RES-043", "name": "customer-support-portal", "owner_id": "U-009", "criticality": "MEDIUM", "compliance_scope": "GDPR"}}',
            '{"role_id": "ROL-043", "role_name": "support-ticket-manager", "description": "Manages customer support tickets and escalations", "is_temporary": false}',
            '{"ok": true, "permission": {"permission_id": "P-113", "action": "manage-support-tickets", "resource_id": "RES-043", "description": "Create, update, and resolve customer support tickets"}}',
            '{"user_id": "U-009", "assignments": [{"role_id": "ROL-011", "role_name": "sales-base", "description": "Basic access for sales staff"}, {"role_id": "ROL-012", "role_name": "sales-crm-access", "description": "Access to CRM system for customer data"}, {"role_id": "ROL-013", "role_name": "sales-lead-manager", "description": "Manages sales leads and opportunities"}, {"role_id": "ROL-043", "role_name": "support-ticket-manager", "description": "Manages customer support tickets and escalations"}]}',
            '{"ok": true, "user_id": "U-009", "has_sod_conflicts": false, "conflict_count": 0, "conflicts": [], "checked_on": "2025-08-08T12:00:00.000000Z"}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_076",
        instruction=(
            "You are engineering lead Alex Johnson. The engineering team needs a new code quality assurance tool for better code review processes. "
            "You must create a new resource called 'code-review-platform' with HIGH criticality and ISO-27001 compliance, owned by Christopher Rodriguez from Engineering. "
            "This resource needs: an associated role 'engineering-code-reviewer' for reviewing code submissions with the description 'Reviews code submissions and enforces quality standards' "
            "and a permission 'approve-code-reviews' for the new role with the description: 'Approve or reject code review submissions'; give the role to Christopher Rodriguez. "
            "Return the new resource, role, permission, and Christopher's updated roles."
        ),
        actions=[
            Action(
                name="get_user",
                kwargs={"first_name": "Alex", "last_name": "Johnson"},
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Christopher", "last_name": "Rodriguez"},
            ),
            Action(
                name="create_resource",
                kwargs={
                    "name": "code-review-platform",
                    "owner_id": "U-007",
                    "criticality": "HIGH",
                    "compliance_scope": "ISO-27001",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "RESOURCE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "RES-043",
                    "details": "Resource RES-043 created by U-001",
                },
            ),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "engineering-code-reviewer",
                    "description": "Reviews code submissions and enforces quality standards",
                    "is_temporary": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ROLE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-001",
                },
            ),
            Action(
                name="create_permission",
                kwargs={
                    "action": "approve-code-reviews",
                    "resource_id": "RES-043",
                    "description": "Approve or reject code review submissions",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-001",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-001",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={
                    "role_id": "ROL-043",
                    "permission_id": "P-113",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Permission P-113 assigned to role ROL-043.",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-007",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-001",
                    "target_id": "U-007",
                    "details": "Role ROL-043 added to U-007",
                },
            ),
            Action(name="check_sod_conflicts", kwargs={"user_id": "U-007"}),
            Action(
                name="get_resource",
                kwargs={"resource_id": "RES-043"},
            ),
            Action(
                name="get_role",
                kwargs={"role_id": "ROL-043"},
            ),
            Action(
                name="get_permission",
                kwargs={"permission_id": "P-113"},
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-007",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"ok": true, "resource": {"resource_id": "RES-043", "name": "code-review-platform", "owner_id": "U-007", "criticality": "HIGH", "compliance_scope": "ISO-27001"}}',
            '{"role_id": "ROL-043", "role_name": "engineering-code-reviewer", "description": "Reviews code submissions and enforces quality standards", "is_temporary": false}',
            '{"ok": true, "permission": {"permission_id": "P-113", "action": "approve-code-reviews", "resource_id": "RES-043", "description": "Approve or reject code review submissions"}}',
            '{"user_id": "U-007", "assignments": [{"role_id": "ROL-001", "role_name": "engineering-base", "description": "Basic access for engineering staff"}, {"role_id": "ROL-002", "role_name": "engineering-code-commit", "description": "Permission to commit code to repositories"}, {"role_id": "ROL-043", "role_name": "engineering-code-reviewer", "description": "Reviews code submissions and enforces quality standards"}]}',
            '{"ok": true, "user_id": "U-007", "has_sod_conflicts": false, "conflict_count": 0, "conflicts": [], "checked_on": "2025-08-08T12:00:00.000000Z"}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_077",
        instruction=(
            "You are engineering lead Alex Johnson. The marketing team needs a new marketing automation platform for managing campaigns and workflows. "
            "You must create a new resource called 'marketing-automation-platform' with HIGH criticality and GDPR compliance, owned by Nicole Thomas from Marketing. "
            "For that resource, you must create: an associated role 'marketing-automation-manager' for managing automated marketing with the description 'Manages automated marketing workflows and campaigns' "
            "and a permission 'configure-marketing-workflows' for the new role with the description: 'Create and modify automated marketing campaign workflows'; give the role to Nicole Thomas. "
            "Return the new resource, role, permission, and Nicole's updated roles."
        ),
        actions=[
            Action(
                name="get_user",
                kwargs={"first_name": "Alex", "last_name": "Johnson"},
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Nicole", "last_name": "Thomas"},
            ),
            Action(
                name="create_resource",
                kwargs={
                    "name": "marketing-automation-platform",
                    "owner_id": "U-014",
                    "criticality": "HIGH",
                    "compliance_scope": "GDPR",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "RESOURCE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "RES-043",
                    "details": "Resource RES-043 created by U-001",
                },
            ),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "marketing-automation-manager",
                    "description": "Manages automated marketing workflows and campaigns",
                    "is_temporary": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ROLE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-001",
                },
            ),
            Action(
                name="create_permission",
                kwargs={
                    "action": "configure-marketing-workflows",
                    "resource_id": "RES-043",
                    "description": "Create and modify automated marketing campaign workflows",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-001",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-001",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={
                    "role_id": "ROL-043",
                    "permission_id": "P-113",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Permission P-113 assigned to role ROL-043.",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-001",
                    "target_id": "U-014",
                    "details": "Role ROL-043 added to U-014",
                },
            ),
            Action(name="check_sod_conflicts", kwargs={"user_id": "U-014"}),
            Action(
                name="get_resource",
                kwargs={"resource_id": "RES-043"},
            ),
            Action(
                name="get_role",
                kwargs={"role_id": "ROL-043"},
            ),
            Action(
                name="get_permission",
                kwargs={"permission_id": "P-113"},
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-014",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"ok": true, "resource": {"resource_id": "RES-043", "name": "marketing-automation-platform", "owner_id": "U-014", "criticality": "HIGH", "compliance_scope": "GDPR"}}',
            '{"role_id": "ROL-043", "role_name": "marketing-automation-manager", "description": "Manages automated marketing workflows and campaigns", "is_temporary": false}',
            '{"ok": true, "permission": {"permission_id": "P-113", "action": "configure-marketing-workflows", "resource_id": "RES-043", "description": "Create and modify automated marketing campaign workflows"}}',
            '{"user_id": "U-014", "assignments": [{"role_id": "ROL-006", "role_name": "marketing-base", "description": "Basic access for marketing staff"}, {"role_id": "ROL-009", "role_name": "marketing-analytics-read", "description": "Read-only access to marketing analytics data"}, {"role_id": "ROL-043", "role_name": "marketing-automation-manager", "description": "Manages automated marketing workflows and campaigns"}]}',
            '{"ok": true, "user_id": "U-014", "has_sod_conflicts": false, "conflict_count": 0, "conflicts": [], "checked_on": "2025-08-08T12:00:00.000000Z"}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_078",
        instruction=(
            "You are engineering lead Alex Johnson. The finance team needs a new executive financial dashboard for sensitive financial reporting. "
            "You must create a new resource called 'executive-financial-dashboard' with CRITICAL criticality and SOX compliance, owned by Jessica Garcia from Finance. "
            "The resource needs: an associated role 'finance-executive-reporting' with the description 'Access to executive-level financial reports and dashboards'. "
            "and a permission 'view-executive-financials' for the new role with the description: 'View executive financial dashboards and sensitive reports'; give the role to Jessica Garcia. "
            "Return the new resource, role, permission, and Jessica's updated roles."
        ),
        actions=[
            Action(
                name="get_user",
                kwargs={"first_name": "Alex", "last_name": "Johnson"},
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Jessica", "last_name": "Garcia"},
            ),
            Action(
                name="create_resource",
                kwargs={
                    "name": "executive-financial-dashboard",
                    "owner_id": "U-006",
                    "criticality": "CRITICAL",
                    "compliance_scope": "SOX",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "RESOURCE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "RES-043",
                    "details": "Resource RES-043 created by U-001",
                },
            ),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "finance-executive-reporting",
                    "description": "Access to executive-level financial reports and dashboards",
                    "is_temporary": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "ROLE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-001",
                },
            ),
            Action(
                name="create_permission",
                kwargs={
                    "action": "view-executive-financials",
                    "resource_id": "RES-043",
                    "description": "View executive financial dashboards and sensitive reports",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-001",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-001",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={
                    "role_id": "ROL-043",
                    "permission_id": "P-113",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Permission P-113 assigned to role ROL-043.",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-006",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-001",
                    "target_id": "U-006",
                    "details": "Role ROL-043 added to U-006",
                },
            ),
            Action(name="check_sod_conflicts", kwargs={"user_id": "U-006"}),
            Action(
                name="get_resource",
                kwargs={"resource_id": "RES-043"},
            ),
            Action(
                name="get_role",
                kwargs={"role_id": "ROL-043"},
            ),
            Action(
                name="get_permission",
                kwargs={"permission_id": "P-113"},
            ),
            Action(
                name="get_user_roles",
                kwargs={
                    "user_id": "U-006",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[
            '{"ok": true, "resource": {"resource_id": "RES-043", "name": "executive-financial-dashboard", "owner_id": "U-006", "criticality": "CRITICAL", "compliance_scope": "SOX"}}',
            '{"role_id": "ROL-043", "role_name": "finance-executive-reporting", "description": "Access to executive-level financial reports and dashboards", "is_temporary": false}',
            '{"ok": true, "permission": {"permission_id": "P-113", "action": "view-executive-financials", "resource_id": "RES-043", "description": "View executive financial dashboards and sensitive reports"}}',
            '{"user_id": "U-006", "assignments": [{"role_id": "ROL-029", "role_name": "finance-base", "description": "Basic access for finance staff"}, {"role_id": "ROL-039", "role_name": "finance-lead", "description": "Lead role for the finance department."}, {"role_id": "ROL-043", "role_name": "finance-executive-reporting", "description": "Access to executive-level financial reports and dashboards"}]}',
            '{"ok": true, "user_id": "U-006", "has_sod_conflicts": false, "conflict_count": 0, "conflicts": [], "checked_on": "2025-08-08T12:00:00.000000Z"}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_079",
        instruction=(
            "You are RBAC_BOT. Operations engineer Patrick Carter needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD September 18th, 2025). "
            "Patrick claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Alex Johnson as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Patrick", "last_name": "Carter"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Alex", "last_name": "Johnson"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-029",
                    "permission_id": "P-084",
                    "reviewed_by": "U-001",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-09-18",
                    "expires_on": "2025-09-18T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-029", "permission_id": "P-084", "reviewed_by": "U-001", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-09-18T23:59:59.000000Z", "reason": "Temporary access to perform submit-tax-filing until 2025-09-18", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_080",  # Too simple??
        instruction=(
            "You are Michael Davis, Operations Lead. "
            "A new third-party vendor integration requires creating a service account 'VENDOR_INTEGRATION_BOT' in the Operations department with the email 'vendor-integration@taucorp.com'. "
            "You must create this account, it should have a new 'vendor-api-access' role with 'Limited access for third-party vendor integration to API gateway' role with the permission with the action 'read-api'."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-005"}),
            Action(
                name="create_user",
                kwargs={
                    "username": "VENDOR_INTEGRATION_BOT",
                    "email": "vendor-integration@taucorp.com",
                    "department": "Operations",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "User VENDOR_INTEGRATION_BOT created by U-005.",
                },
            ),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "vendor-api-access",
                    "description": "Limited access for third-party vendor integration to API gateway",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-005.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "read-api"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-010"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-010 assigned to role ROL-043.",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-005",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-034",
                    "details": "Role ROL-043 added to U-034",
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-034"}),
        ],
        outputs=[
            '{"user_id": "U-034", "username": "VENDOR_INTEGRATION_BOT", "email": "vendor-integration@taucorp.com", "department": "Operations", "status": "ACTIVE", "mfa_enabled": false}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_081",
        instruction=(
            "You are Operations Lead Michael Davis. "
            "A new marketing automation vendor requires creating a service account 'MARKETING_AUTOMATION_BOT' in the Marketing department with the email 'marketing-automation@taucorp.com', you must create this account. "
            "The account should have a new 'vendor-marketing-automation' role with 'Limited access for marketing automation vendor to manage campaigns' description with the permission with the action 'send-email-campaign'."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-005"}),
            Action(
                name="create_user",
                kwargs={
                    "username": "MARKETING_AUTOMATION_BOT",
                    "email": "marketing-automation@taucorp.com",
                    "department": "Marketing",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "User MARKETING_AUTOMATION_BOT created by U-005.",
                },
            ),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "vendor-marketing-automation",
                    "description": "Limited access for marketing automation vendor to manage campaigns",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-005.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "send-email-campaign"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-022"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-022 assigned to role ROL-043.",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-005",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-034",
                    "details": "Role ROL-043 added to U-034",
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-034"}),
        ],
        outputs=[
            '{"user_id": "U-034", "username": "MARKETING_AUTOMATION_BOT", "email": "marketing-automation@taucorp.com", "department": "Marketing", "status": "ACTIVE", "mfa_enabled": false}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_082",
        instruction=(
            "You are Finance Lead Jessica Garcia. "
            "A new payment processing vendor requires creating a service account 'PAYMENT_PROCESSOR_BOT' in the Finance department with the email 'payment-processor@taucorp.com', you must create this account. "
            "The account should have a new 'vendor-payment-processing' role with 'Limited access for payment processing vendor to handle invoices' description with the permission with the action 'view-payments'."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-006"}),
            Action(
                name="create_user",
                kwargs={
                    "username": "PAYMENT_PROCESSOR_BOT",
                    "email": "payment-processor@taucorp.com",
                    "department": "Finance",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "User PAYMENT_PROCESSOR_BOT created by U-006.",
                },
            ),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "vendor-payment-processing",
                    "description": "Limited access for payment processing vendor to handle invoices",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-006.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "view-payments"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-079"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-079 assigned to role ROL-043.",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-006",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-034",
                    "details": "Role ROL-043 added to U-034",
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-034"}),
        ],
        outputs=[
            '{"user_id": "U-034", "username": "PAYMENT_PROCESSOR_BOT", "email": "payment-processor@taucorp.com", "department": "Finance", "status": "ACTIVE", "mfa_enabled": false}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_083",
        instruction=(
            "You are Sales Lead David Brown. "
            "A new CRM analytics vendor requires creating a service account 'CRM_ANALYTICS_BOT' in the Sales department with the email 'crm-analytics@taucorp.com', you must create this account. "
            "The account should have a new 'vendor-crm-analytics' role with 'Limited access for CRM analytics vendor to read customer data' description with the permission with the action 'read-crm-customer'."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "David", "last_name": "Brown"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-003"}),
            Action(
                name="create_user",
                kwargs={
                    "username": "CRM_ANALYTICS_BOT",
                    "email": "crm-analytics@taucorp.com",
                    "department": "Sales",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-003",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "User CRM_ANALYTICS_BOT created by U-003.",
                },
            ),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "vendor-crm-analytics",
                    "description": "Limited access for CRM analytics vendor to read customer data",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-003",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-003.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "read-crm-customer"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-035"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-003",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-035 assigned to role ROL-043.",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-003",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-003",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-034",
                    "details": "Role ROL-043 added to U-034",
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-034"}),
        ],
        outputs=[
            '{"user_id": "U-034", "username": "CRM_ANALYTICS_BOT", "email": "crm-analytics@taucorp.com", "department": "Sales", "status": "ACTIVE", "mfa_enabled": false}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_084",
        instruction=(
            "You are Operations manager Michael Davis. "
            "A new recruitment automation vendor requires creating a service account 'RECRUITMENT_AUTOMATION_BOT' in the Human Resources department with the email 'recruitment-automation@taucorp.com'. "
            "You must create this account, it should have a new 'vendor-recruitment-automation' role with 'Limited access for recruitment vendor to manage job postings' description with the permission with the action 'create-job-posting'."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-005"}),
            Action(
                name="create_user",
                kwargs={
                    "username": "RECRUITMENT_AUTOMATION_BOT",
                    "email": "recruitment-automation@taucorp.com",
                    "department": "Human Resources",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "User RECRUITMENT_AUTOMATION_BOT created by U-005.",
                },
            ),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "vendor-recruitment-automation",
                    "description": "Limited access for recruitment vendor to manage job postings",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-005.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "create-job-posting"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-053"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-053 assigned to role ROL-043.",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-005",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-034",
                    "details": "Role ROL-043 added to U-034",
                },
            ),
            Action(name="get_user", kwargs={"user_id": "U-034"}),
        ],
        outputs=[
            '{"user_id": "U-034", "username": "RECRUITMENT_AUTOMATION_BOT", "email": "recruitment-automation@taucorp.com", "department": "Human Resources", "status": "ACTIVE", "mfa_enabled": false}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_085",
        instruction=(
            "You are Jessica Garcia, Finance Lead. "
            "The annual budget planning project requires temporary collaboration between Finance and Sales teams. "
            "You need to create a temporary role 'budget-planning-reviewer' with description 'Temporary cross-department role for budget planning collaboration' "
            "with the permissions view-financial-report and generate-sales-report. "
            "David Brown and Nicole Thomas need the role expiring EOD September 7th, 2025."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-006"}),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "budget-planning-reviewer",
                    "description": "Temporary cross-department role for budget planning collaboration",
                    "is_temporary": True,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-006.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "view-financial-report"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-085"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-085 assigned to role ROL-043.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "generate-sales-report"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-039"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-039 assigned to role ROL-043.",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "David", "last_name": "Brown"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-003",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-006",
                    "expires_on": "2025-09-07T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-003",
                    "details": "Role ROL-043 added to U-003",
                },
            ),
            Action(
                name="get_user_roles", kwargs={"user_id": "U-003"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Nicole", "last_name": "Thomas"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-006",
                    "expires_on": "2025-09-07T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-014",
                    "details": "Role ROL-043 added to U-014",
                },
            ),
            Action(
                name="get_user_roles", kwargs={"user_id": "U-014"}
            ),
            Action(name="get_role", kwargs={"role_id": "ROL-043"}),
        ],
        outputs=[
            '{"role_id": "ROL-043", "role_name": "budget-planning-reviewer", "description": "Temporary cross-department role for budget planning collaboration", "is_temporary": true}',
            '{"user_id": "U-003", "assignments": [{"role_id": "ROL-011"}, {"role_id": "ROL-036"}, {"role_id": "ROL-043"}]}',
            '{"user_id": "U-014", "assignments": [{"role_id": "ROL-006"}, {"role_id": "ROL-009"}, {"role_id": "ROL-043"}]}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_086",
        instruction=(
            "You are Alex Johnson, Engineering Lead. "
            "A new microservices deployment requires temporary collaboration between Engineering and Operations. "
            "Create a temporary role 'microservices-deployment-reviewer' with description 'Temporary cross-department role for microservices deployment' "
            "with permissions configure-pipeline and modify-firewall-rules. "
            "Daniel Taylor and Jeffery Green need the role, expiring EOD September 15th, 2025."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Alex", "last_name": "Johnson"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-001"}),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "microservices-deployment-reviewer",
                    "description": "Temporary cross-department role for microservices deployment",
                    "is_temporary": True,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-001.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "configure-pipeline"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-005"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-005 assigned to role ROL-043.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "modify-firewall-rules"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-067"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-067 assigned to role ROL-043.",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Daniel", "last_name": "Taylor"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-019",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                    "expires_on": "2025-09-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-019",
                    "details": "Role ROL-043 added to U-019",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jeffery", "last_name": "Green"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-023",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                    "expires_on": "2025-09-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-023",
                    "details": "Role ROL-043 added to U-023",
                },
            ),
            Action(name="get_role", kwargs={"role_id": "ROL-043"}),
        ],
        outputs=[
            '{"role_id": "ROL-043", "role_name": "microservices-deployment-reviewer", "description": "Temporary cross-department role for microservices deployment", "is_temporary": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_087",
        instruction=(
            "You are Michael Davis, Operations Lead. "
            "A quarterly audit requires temporary access for Finance and Operations to review backup storage. "
            "Create a temporary role 'backup-audit-reviewer' with description 'Temporary role for quarterly backup audit' "
            "with permissions restore-backup and upload-backup. "
            "Jessica Garcia and Patrick Carter need the role, expiring EOD September 30th, 2025."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-005"}),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "backup-audit-reviewer",
                    "description": "Temporary role for quarterly backup audit",
                    "is_temporary": True,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-005.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "restore-backup"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-069"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-069 assigned to role ROL-043.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "upload-backup"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-068"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-068 assigned to role ROL-043.",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-006",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-005",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-006",
                    "details": "Role ROL-043 added to U-006",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Patrick", "last_name": "Carter"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-005",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-029",
                    "details": "Role ROL-043 added to U-029",
                },
            ),
            Action(name="get_role", kwargs={"role_id": "ROL-043"}),
        ],
        outputs=[
            '{"role_id": "ROL-043", "role_name": "backup-audit-reviewer", "description": "Temporary role for quarterly backup audit", "is_temporary": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_088",  # Too simple?
        instruction=(
            "You are Sarah Williams, Marketing Lead. "
            "A cross-department campaign launch requires temporary collaboration between Marketing and Sales. "
            "Create a temporary role 'campaign-launch-reviewer' with description 'Temporary role for campaign launch collaboration' "
            "with permissions post-social-media and generate-sales-report. "
            "Angela Phillips and Paul Ellis need the role, expiring EOD October 1st, 2025."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Sarah", "last_name": "Williams"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-002"}),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "campaign-launch-reviewer",
                    "description": "Temporary role for campaign launch collaboration",
                    "is_temporary": True,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-002.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "post-social-media"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-019"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-019 assigned to role ROL-043.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "generate-sales-report"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-039"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-039 assigned to role ROL-043.",
                },
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Angela", "last_name": "Phillips"},
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-002",
                    "expires_on": "2025-10-01T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-026",
                    "details": "Role ROL-043 added to U-026",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Paul", "last_name": "Ellis"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-021",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-002",
                    "expires_on": "2025-10-01T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-021",
                    "details": "Role ROL-043 added to U-021",
                },
            ),
            Action(name="get_role", kwargs={"role_id": "ROL-043"}),
        ],
        outputs=[
            '{"role_id": "ROL-043", "role_name": "campaign-launch-reviewer", "description": "Temporary role for campaign launch collaboration", "is_temporary": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_089",
        instruction=(
            "You are Emily Jones, HR Lead. "
            "A compliance review requires temporary access for HR and Finance to the benefits administration system. "
            "Create a temporary role 'benefits-compliance-reviewer' with description 'Temporary role for benefits compliance review' "
            "with permissions enroll-in-benefits and view-onboarding-docs. "
            "Brittany King (HR) and Lisa Anderson (Finance) need the role, expiring EOD October 15th, 2025."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Emily", "last_name": "Jones"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-004"}),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "benefits-compliance-reviewer",
                    "description": "Temporary role for benefits compliance review",
                    "is_temporary": True,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-004",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-004.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "enroll-in-benefits"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-056"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-004",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-056 assigned to role ROL-043.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "view-onboarding-docs"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-058"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-004",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-058 assigned to role ROL-043.",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Brittany", "last_name": "King"}
            ),
            Action(
                name="check_sod_conflicts",
                kwargs={"user_id": "U-022", "role_id": "ROL-043"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-022",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-004",
                    "expires_on": "2025-10-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-004",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-022",
                    "details": "Role ROL-043 added to U-022",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Lisa", "last_name": "Anderson"}
            ),
            Action(
                name="check_sod_conflicts",
                kwargs={"user_id": "U-012", "role_id": "ROL-043"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-012",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-004",
                    "expires_on": "2025-10-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-004",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-012",
                    "details": "Role ROL-043 added to U-012",
                },
            ),
            Action(name="get_role", kwargs={"role_id": "ROL-043"}),
        ],
        outputs=[
            '{"role_id": "ROL-043", "role_name": "benefits-compliance-reviewer", "description": "Temporary role for benefits compliance review", "is_temporary": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_090",
        instruction=(
            "You are Jessica Garcia, Finance Lead. "
            "A special project requires temporary collaboration between Finance and Marketing to analyze quarterly financial reports and marketing analytics. "
            "Create a temporary role 'finance-marketing-analyst' with description 'Temporary cross-department role for financial and marketing analysis' "
            "with permissions view-financial-report and view-marketing-dashboard. "
            "Katherine Hall and Nicole Thomas need the role until EOD October 31st, 2025."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-006"}),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "finance-marketing-analyst",
                    "description": "Temporary cross-department role for financial and marketing analysis",
                    "is_temporary": True,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-006.",
                },
            ),
            Action(name="get_permission", kwargs={"action": "view-financial-report"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-085"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-085 assigned to role ROL-043.",
                },
            ),
            Action(
                name="get_permission", kwargs={"action": "view-marketing-dashboard"}
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-025"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-025 assigned to role ROL-043.",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Katherine", "last_name": "Hall"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-024",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-006",
                    "expires_on": "2025-10-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-024",
                    "details": "Role ROL-043 added to U-024",
                },
            ),
            Action(
                name="get_user", kwargs={"first_name": "Nicole", "last_name": "Thomas"}
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-006",
                    "expires_on": "2025-10-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-014",
                    "details": "Role ROL-043 added to U-014",
                },
            ),
            Action(name="get_role", kwargs={"role_id": "ROL-043"}),
        ],
        outputs=[
            '{"role_id": "ROL-043", "role_name": "finance-marketing-analyst", "description": "Temporary cross-department role for financial and marketing analysis", "is_temporary": true}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_091",
        instruction=(
            "You are Sarah Williams, Marketing Lead. Due to organizational changes, the 'marketing-analytics-read' and 'marketing-content-editor' roles "
            "are being consolidated into a single 'marketing-content-analyst' role with the description 'Consolidated role for marketing analytics and content editing'. "
            "Migrate all active users and permissions from both old roles to the new one. "
            "Then mark the old roles as 'Deprecated' in their description."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Sarah", "last_name": "Williams"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-002"}),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "marketing-content-analyst",
                    "description": "Consolidated role for marketing analytics and content editing",
                    "is_temporary": False,
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-002.",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "marketing-analytics-read"}),
            Action(name="get_role", kwargs={"role_name": "marketing-content-editor"}),
            Action(
                name="get_role_permissions",
                kwargs={"role_id": "ROL-009", "include_permission": True},
            ),
            Action(
                name="get_role_permissions",
                kwargs={"role_id": "ROL-010", "include_permission": True},
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-025"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-025 assigned to role ROL-043.",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-026"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-026 assigned to role ROL-043.",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-030"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-030 assigned to role ROL-043.",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-031"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-031 assigned to role ROL-043.",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-032"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-032 assigned to role ROL-043.",
                },
            ),
            Action(name="get_user", kwargs={"role_id": "ROL-009", "status": "ACTIVE"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-009",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-014",
                    "details": "Role ROL-009 removed from U-014",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-002",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-014",
                    "details": "Role ROL-043 added to U-014",
                },
            ),
            Action(name="get_user", kwargs={"role_id": "ROL-010", "status": "ACTIVE"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-010",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-026",
                    "details": "Role ROL-010 removed from U-026",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-002",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-026",
                    "details": "Role ROL-043 added to U-026",
                },
            ),
            Action(
                name="update_role",
                kwargs={"role_id": "ROL-009", "description": "Deprecated"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_DEPRECATED",
                    "target_id": "ROL-009",
                    "details": "Role ROL-009 marked as deprecated by U-002.",
                },
            ),
            Action(
                name="update_role",
                kwargs={"role_id": "ROL-010", "description": "Deprecated"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_DEPRECATED",
                    "target_id": "ROL-010",
                    "details": "Role ROL-010 marked as deprecated by U-002.",
                },
            ),
        ],
        outputs=[
            '{"ok": true, "role": {"role_id": "ROL-043", "role_name": "marketing-content-analyst", "description": "Consolidated role for marketing analytics and content editing", "is_temporary": false}}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_092",
        instruction=(
            "You are Jessica Garcia, Finance Lead. The 'finance-read' and 'finance-invoice-processor' roles are being consolidated into a single 'finance-data-analyst' role with the description 'Consolidated role for finance data analysis and invoice processing'. "
            "Migrate all active users and permissions from both old roles to the new one. Then mark the old roles as 'Deprecated' in their description."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-006"}),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "finance-data-analyst",
                    "description": "Consolidated role for finance data analysis and invoice processing",
                    "is_temporary": False,
                },
            ),
            Action(name="get_role", kwargs={"role_name": "finance-read"}),
            Action(name="get_role", kwargs={"role_name": "finance-invoice-processor"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-030"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-075"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-075 assigned to role ROL-043.",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-083"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-083 assigned to role ROL-043.",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-085"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-085 assigned to role ROL-043.",
                },
            ),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-031"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-077"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-077 assigned to role ROL-043.",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-078"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-078 assigned to role ROL-043.",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-079"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-079 assigned to role ROL-043.",
                },
            ),
            Action(name="get_user", kwargs={"role_id": "ROL-030", "status": "ACTIVE"}),
            Action(name="get_user", kwargs={"role_id": "ROL-031", "status": "ACTIVE"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-012",
                    "role_id": "ROL-031",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-012",
                    "details": "Role ROL-031 removed from U-012",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-012",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-006",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-012",
                    "details": "Role ROL-043 added to U-012",
                },
            ),
            Action(
                name="update_role",
                kwargs={
                    "role_id": "ROL-030",
                    "description": "Deprecated",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ROLE_DEPRECATED",
                    "target_id": "ROL-030",
                    "details": "Role ROL-030 marked as deprecated by U-006.",
                },
            ),
            Action(
                name="update_role",
                kwargs={
                    "role_id": "ROL-031",
                    "description": "Deprecated",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ROLE_DEPRECATED",
                    "target_id": "ROL-031",
                    "details": "Role ROL-031 marked as deprecated by U-006.",
                },
            ),
        ],
        outputs=[
            '{"ok": true, "role": {"role_id": "ROL-043", "role_name": "finance-data-analyst", "description": "Consolidated role for finance data analysis and invoice processing", "is_temporary": false}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_093",
        instruction=(
            "You are Sarah Williams, Marketing Lead. The 'marketing-campaign-manager' and 'marketing-social-media' roles are being consolidated into a single 'marketing-campaign-analyst' role "
            "with the description 'Consolidated role for campaign management and social media oversight'. "
            "Migrate all active users and permissions from both old roles to the new one. Then mark the old roles as 'Deprecated' in their description."
        ),
        actions=[
            Action(
                name="get_user", kwargs={"first_name": "Sarah", "last_name": "Williams"}
            ),
            Action(name="is_admin", kwargs={"user_id": "U-002"}),
            Action(
                name="create_role",
                kwargs={
                    "role_name": "marketing-campaign-analyst",
                    "description": "Consolidated role for campaign management and social media oversight",
                    "is_temporary": False,
                },
            ),
            Action(name="get_role", kwargs={"role_name": "marketing-campaign-manager"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-007"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-022"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-022 assigned to role ROL-043.",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-024"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-024 assigned to role ROL-043.",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-029"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-029 assigned to role ROL-043.",
                },
            ),
            Action(name="get_role", kwargs={"role_name": "marketing-social-media"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-008"}),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-019"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-019 assigned to role ROL-043.",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-020"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-020 assigned to role ROL-043.",
                },
            ),
            Action(
                name="assign_permission_to_role",
                kwargs={"role_id": "ROL-043", "permission_id": "P-021"},
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-021 assigned to role ROL-043.",
                },
            ),
            Action(name="get_user", kwargs={"role_id": "ROL-007", "status": "ACTIVE"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-007",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-026",
                    "details": "Role ROL-007 removed from U-026",
                },
            ),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-002",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-026",
                    "details": "Role ROL-043 added to U-026",
                },
            ),
            Action(name="get_user", kwargs={"role_id": "ROL-008", "status": "ACTIVE"}),
            Action(
                name="update_role",
                kwargs={
                    "role_id": "ROL-007",
                    "description": "Deprecated",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_DEPRECATED",
                    "target_id": "ROL-007",
                    "details": "Role ROL-007 marked as deprecated by U-002.",
                },
            ),
            Action(
                name="update_role",
                kwargs={
                    "role_id": "ROL-008",
                    "description": "Deprecated",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_DEPRECATED",
                    "target_id": "ROL-008",
                    "details": "Role ROL-008 marked as deprecated by U-002.",
                },
            ),
        ],
        outputs=[
            '{"user_id": "U-002", "username": "swilliams", "email": "sarah.williams@taucorp.com", "department": "Marketing", "status": "ACTIVE", "mfa_enabled": false}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_094",
        instruction=(
            "You are RBAC_BOT. Engineer Brian Taylor needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD September 22nd, 2025). "
            "Brian claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Sarah Williams as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Brian", "last_name": "Taylor"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Sarah", "last_name": "Williams"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-002", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-013",
                    "permission_id": "P-084",
                    "reviewed_by": "U-002",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-09-22",
                    "expires_on": "2025-09-22T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-013", "permission_id": "P-084", "reviewed_by": "U-002", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-09-22T23:59:59.000000Z", "reason": "Temporary access to perform submit-tax-filing until 2025-09-22", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_095",
        instruction=(
            "You are RBAC_BOT. Engineer Christopher Rodriguez needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 3rd, 2025). "
            "Christopher claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Michael Davis as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user",
                kwargs={"first_name": "Christopher", "last_name": "Rodriguez"},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Michael", "last_name": "Davis"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-007",
                    "permission_id": "P-084",
                    "reviewed_by": "U-005",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-03",
                    "expires_on": "2025-10-03T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-007", "permission_id": "P-084", "reviewed_by": "U-005", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-10-03T23:59:59.000000Z", "reason": "Temporary access to perform submit-tax-filing until 2025-10-03", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_096",
        instruction=(
            "You are RBAC_BOT. Sales analyst Paul Ellis needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 12th, 2025). "
            "Paul claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Jessica Garcia as the reviewer."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="get_user", kwargs={"first_name": "Paul", "last_name": "Ellis"}
            ),
            Action(
                name="get_user", kwargs={"first_name": "Jessica", "last_name": "Garcia"}
            ),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="get_permission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-021",
                    "permission_id": "P-084",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-12",
                    "expires_on": "2025-10-12T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-021", "permission_id": "P-084", "reviewed_by": "U-006", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-10-12T23:59:59.000000Z", "reason": "Temporary access to perform submit-tax-filing until 2025-10-12", "status": "PENDING_REVIEW"}}'
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_097",
        instruction=(
            "You are HR_ONBOARD_BOT. Sales rep Matthew Lopez is changing his last name to Lucero and will be on paternity leave until EOD November 1st, 2025. "
            "You must update his profile to reflect the new last name and set his account to inactive during the leave. "
            "While Matthew is on leave, Kevin Harris will handle quote approvals. "
            "Kevin needs the 'sales-commission-view' role."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="is_admin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(name="get_user", kwargs={"first_name": "Matthew", "last_name": "Lopez"}),
            Action(name="get_user", kwargs={"username": "mlucero", "allow_missing": True}),
            Action(name="update_user", kwargs={"user_id": "U-009", "last_name": "Lucero"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-009",
                    "details": "U-032 updated user U-009 name to Matthew Lucero; username set to mlucero; email set to matthew.lucero@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#sales",
                    "message": "User U-009 updated by U-032: username mlopez -> mlucero; email set to matthew.lucero@taucorp.com; name set to Matthew Lucero.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="update_user", kwargs={"user_id": "U-009", "status": "INACTIVE"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-009",
                    "details": "HR_ONBOARD_BOT changed user U-009 status to INACTIVE",
                },
            ),
            Action(name="get_user", kwargs={"first_name": "Kevin", "last_name": "Harris"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-015", "only_active": True}),
            Action(name="get_role", kwargs={"role_name": "sales-commission-view"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-015",
                    "role_id": "ROL-015",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-11-01T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-015",
                    "details": "Role ROL-015 added to U-015",
                },
            ),
            Action(name="get_user", kwargs={"username": "mlucero"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-015", "only_active": True}),
        ],
        outputs=[
            '{"user_id": "U-009", "username": "mlucero", "email": "matthew.lucero@taucorp.com", "department": "Sales", "status": "INACTIVE", "mfa_enabled": true}',
            '{"user_id": "U-015", "assignments": [{"role_id": "ROL-011"}, {"role_id": "ROL-015"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_098",
        instruction=(
            "You are HR_ONBOARD_BOT. HR specialist Brittany King is changing her first name to Riley and is taking leave until EOD September 5th, 2025. "
            "Update her profile and set her account to inactive during leave. "
            "While Riley is on leave, assign teammate Laura Jackson the temporary 'hr-employee-data-read' role."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="is_admin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="get_user", kwargs={"first_name": "Brittany", "last_name": "King"}),
            Action(name="get_user", kwargs={"username": "rking", "allow_missing": True}),
            Action(name="update_user", kwargs={"user_id": "U-022", "first_name": "Riley"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-022",
                    "details": "U-032 updated user U-022 name to Riley King; username set to rking; email set to riley.king@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#human-resources",
                    "message": "User U-022 updated by U-032: username bking -> rking; email set to riley.king@taucorp.com; name set to Riley King.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="update_user", kwargs={"user_id": "U-022", "status": "INACTIVE"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-022",
                    "details": "HR_ONBOARD_BOT changed user U-022 status to INACTIVE",
                },
            ),
            Action(name="get_user", kwargs={"first_name": "Laura", "last_name": "Jackson"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-016", "only_active": True}),
            Action(name="get_role", kwargs={"role_name": "hr-employee-data-read"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-016",
                    "role_id": "ROL-017",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-09-05T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-016",
                    "details": "Role ROL-017 added to U-016",
                },
            ),
            Action(name="get_user", kwargs={"username": "rking"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-016", "only_active": True}),
        ],
        outputs=[
            '{"user_id": "U-022", "username": "rking", "email": "riley.king@taucorp.com", "department": "Human Resources", "status": "INACTIVE", "mfa_enabled": true}',
            '{"user_id": "U-016", "assignments": [{"role_id": "ROL-016"}, {"role_id": "ROL-017"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_099",
        instruction=(
            "You are HR_ONBOARD_BOT. Operations analyst Robert White is changing his last name to Wyatt and is taking leave until EOD October 10th, 2025. "
            "Update his profile and set his account to inactive during the leave. "
            "During Robert's absence, assign a temporary 'operations-incident-response' role to Patrick Carter."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="is_admin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="get_user", kwargs={"first_name": "Robert", "last_name": "White"}),
            Action(name="get_user", kwargs={"username": "rwyatt", "allow_missing": True}),
            Action(name="update_user", kwargs={"user_id": "U-017", "last_name": "Wyatt"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-017",
                    "details": "U-032 updated user U-017 name to Robert Wyatt; username set to rwyatt; email set to robert.wyatt@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#operations",
                    "message": "User U-017 updated by U-032: username rwhite -> rwyatt; email set to robert.wyatt@taucorp.com; name set to Robert Wyatt.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="update_user", kwargs={"user_id": "U-017", "status": "INACTIVE"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-017",
                    "details": "HR_ONBOARD_BOT changed user U-017 status to INACTIVE",
                },
            ),
            Action(name="get_user", kwargs={"first_name": "Patrick", "last_name": "Carter"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-029", "only_active": True}),
            Action(name="get_role", kwargs={"role_name": "operations-incident-response"}),
            Action(
                name="update_user_role",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-023",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-10-10T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "Role ROL-023 added to U-029",
                },
            ),
            Action(name="get_user", kwargs={"username": "rwyatt"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-029", "only_active": True, "include_role_details": True}),
        ],
        outputs=[
            '{"user_id": "U-017", "username": "rwyatt", "email": "robert.wyatt@taucorp.com", "department": "Operations", "status": "INACTIVE", "mfa_enabled": true}',
            '{"user_id": "U-029", "assignments": [{"role_id": "ROL-021", "role_name": "operations-base", "description": "Basic access for operations staff"}, {"role_id": "ROL-023", "role_name": "operations-incident-response", "description": "Responds to and resolves system incidents"}]}',
        ],
    ),
    Task(
        annotator="liam",
        user_id="liam_100",
        instruction=(
            "You are HR_ONBOARD_BOT. Marketing specialist Angela Phillips is changing her last name to Phelps and is taking leave until EOD October 20th, 2025. "
            "Update her profile and set her account to inactive during leave. "
            "While Angela is on leave, create a time-bound policy exception for Sales teammate Matthew Lopez to temporarily 'search-logs' "
            "until EOD October 20th, 2025, to be reviewed by Marketing lead Sarah Williams."
        ),
        actions=[
            Action(name="get_user", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="is_admin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="get_user", kwargs={"first_name": "Angela", "last_name": "Phillips"}),
            Action(name="get_user", kwargs={"username": "aphelps", "allow_missing": True}),
            Action(name="update_user", kwargs={"user_id": "U-026", "last_name": "Phelps"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "U-032 updated user U-026 name to Angela Phelps; username set to aphelps; email set to angela.phelps@taucorp.com",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#marketing",
                    "message": "User U-026 updated by U-032: username aphillips -> aphelps; email set to angela.phelps@taucorp.com; name set to Angela Phelps.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="update_user", kwargs={"user_id": "U-026", "status": "INACTIVE"}),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "HR_ONBOARD_BOT changed user U-026 status to INACTIVE",
                },
            ),
            Action(name="get_user", kwargs={"first_name": "Matthew", "last_name": "Lopez"}),
            Action(name="get_user", kwargs={"first_name": "Sarah", "last_name": "Williams"}),
            Action(name="is_admin", kwargs={"user_id": "U-002", "include_role_details": True}),
            Action(name="get_permission", kwargs={"action": "search-logs"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-009",
                    "permission_id": "P-071",
                    "reviewed_by": "U-002",
                    "reason": "Temporary access to perform search-logs until 2025-10-20",
                    "expires_on": "2025-10-20T23:59:59.000000Z",
                },
            ),
            Action(
                name="create_audit_log_entry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-032",
                    "target_id": "PE-021",
                    "details": "HR_ONBOARD_BOT created exception request PE-021",
                },
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-032",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="get_user", kwargs={"username": "aphelps"}),
            Action(name="get_policy_exception", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[
            '{"ok": true, "user": {"user_id": "U-026", "username": "aphelps", "email": "angela.phelps@taucorp.com", "department": "Marketing", "status": "INACTIVE", "mfa_enabled": true}}',
            '{"ok": true, "policy_exception": {"exception_id": "PE-021", "user_id": "U-009", "permission_id": "P-071", "reviewed_by": "U-002", "requested_on": "2025-08-08T12:00:00.000000Z", "reviewed_on": null, "expires_on": "2025-10-20T23:59:59.000000Z", "reason": "Temporary access to perform publish-campaign-assets until 2025-10-20", "status": "PENDING_REVIEW"}}',
        ],
    ),
]
