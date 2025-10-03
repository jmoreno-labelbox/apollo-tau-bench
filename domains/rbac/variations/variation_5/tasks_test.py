from tau_bench.types import Action, Task


TASKS = [
    Task(
        annotator="liam",
        user_id="liam_001",
        instruction=(
            "You're lead engineer Mason Martinez. "
            "You must review Nathan Thompson's pending access request and approve it. "
            "Then, you must add the requested role to Nathan's account."
        ),
        actions=[
            Action(
                name="GetUser",
                kwargs={"first_name": "Mason", "last_name": "Martinez"},
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Nathan", "last_name": "Thompson"},
            ),
            Action(
                name="GetAccessRequest",
                kwargs={"user_id": "U-013", "status": "PENDING"},
            ),
            Action(
                name="DecideAccessRequest",
                kwargs={
                    "request_id": "AR-020",
                    "reviewer_id": "U-001",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-013",
                    "role_id": "ROL-004",
                    "action": "ADD",
                    "assigned_by": "U-001",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-001",
                    "target_id": "U-013",
                    "details": "Role ROL-004 added to U-013",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ACCESS_GRANTED",
                    "actor_id": "U-001",
                    "target_id": "AR-020",
                    "details": "Access request AR-020 was approved by U-001",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "Mason.martinez@sigmatech.com",
                    "receiver": "nathan.Thompson@sigmatech.com",
                    "subject": "Access Request APPROVED",
                    "text_content": "Your access request AR-020 has been APPROVED.",
                },
            ),
            Action(
                name="GetAccessRequest",
                kwargs={"request_id": "AR-020"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-013",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="CheckSodConflicts",
                kwargs={
                    "user_id": "U-013",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_002",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineer Nathan Thompson is changing his last name to Talley and taking leave until EOD September 25th, 2025. "
            "Update his profile and set his account to inactive during leave. "
            "While Nathan is on leave, assign Mason Martinez a temporary 'engineering-qa-test' role to support release management."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="IsAdmin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="GetUser", kwargs={"first_name": "Nathan", "last_name": "Thompson"}),
            Action(name="GetUser", kwargs={"username": "btalley", "allow_missing": True}),
            Action(name="UpdateUser", kwargs={"user_id": "U-013", "last_name": "Talley"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-013",
                    "details": "U-032 updated user U-013 name to Nathan Talley; username set to btalley; email set to Nathan.talley@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#engineering",
                    "message": "User U-013 updated by U-032: username nwhite -> btalley; email set to Nathan.talley@sigmatech.com; name set to Nathan Talley.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="UpdateUser", kwargs={"user_id": "U-013", "status": "INACTIVE"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-013",
                    "details": "HR_ONBOARD_BOT changed user U-013 status to INACTIVE",
                },
            ),
            Action(name="GetUser", kwargs={"first_name": "Mason", "last_name": "Martinez"}),
            Action(name="GetUserRoles", kwargs={"user_id": "U-001", "only_active": True}),
            Action(name="GetRole", kwargs={"role_name": "engineering-qa-test"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-001",
                    "role_id": "ROL-005",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-09-25T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-001",
                    "details": "Role ROL-005 added to U-001",
                },
            ),
            Action(name="GetUser", kwargs={"username": "btalley"}),
            Action(name="GetUserRoles", kwargs={"user_id": "U-001", "only_active": True}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_003",
        instruction=(
            "You're lead engineer Mason Martinez. "
            "You must complete the scheduled access certification for the internal-documentation-wiki resource."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Mason", "last_name": "Martinez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(name="GetResource", kwargs={"name": "internal-documentation-wiki"}),
            Action(
                name="GetCertification",
                kwargs={
                    "reviewer_id": "U-001",
                    "status": "PENDING",
                    "resource_id": "RES-006",
                },
            ),
            Action(
                name="ListUsersWithAccessToResource",
                kwargs={"resource_id": "RES-006", "include_role_details": True},
            ),
            Action(
                name="CompleteCertification",
                kwargs={"certification_id": "C-014", "reviewer_id": "U-001"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "CERTIFICATION_COMPLETED",
                    "actor_id": "U-001",
                    "target_id": "C-014",
                    "details": "Certification C-014 for RES-006 was completed",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#certifications",
                    "message": "C-014 for RES-006 completed by U-001.",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_004",
        instruction=(
            "You are RBAC_BOT. Operations manager Noah Thompson has approved Jacob Allen's urgent policy exception request for production server access. "
            "You must update the policy exception request accordingly."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Jacob", "last_name": "Allen"}
            ),
            Action(name="GetPolicyException", kwargs={"user_id": "U-023"}),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-012"}),
            Action(name="GetPermission", kwargs={"permission_id": "P-089"}),
            Action(
                name="DecidePolicyException",
                kwargs={
                    "exception_id": "PE-012",
                    "reviewer_id": "U-005",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_APPROVED",
                    "actor_id": "U-005",
                    "target_id": "PE-012",
                    "details": "U-005 approved exception PE-012",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-012 approved by U-005",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "rbac@sigmatech.com",
                    "receiver": "jacob.allen@sigmatech.com",
                    "subject": "Policy Exception APPROVED",
                    "text_content": "Your policy exception request PE-012 has been APPROVED.",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_005",
        instruction=(
            "You are RBAC_BOT. Finance analyst Mia Robinson needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 15th, 2025). "
            "Mia claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Olivia Lee as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Mia", "last_name": "Robinson"},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Lee"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-018",
                    "permission_id": "P-084",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-15",
                    "expires_on": "2025-10-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_006",
        instruction=(
            "You are HR_ONBOARD_BOT. "
            "Madison Martinez is transferring from Marketing to Sales department. "
            "you must remove her marketing-base role and marketing-analytics-read role, and add the base sales role."
        ),
        actions=[
            Action(
                name="GetUser",
                kwargs={"username": "HR_ONBOARD_BOT"},
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Madison", "last_name": "Johnson"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-014",
                    "only_active": False,
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={
                    "user_id": "U-014",
                    "department": "Sales",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment", kwargs={"department": "Marketing"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-006",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "Role ROL-006 removed from U-014",
                },
            ),
            Action(
                name="GetRole",
                kwargs={"role_name": "marketing-analytics-read"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-009",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "Role ROL-009 removed from U-014",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment",
                kwargs={"department": "Sales"},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-011",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "Role ROL-011 added to U-014",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-014",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_007",
        instruction=(
            "You are operations incident responder Jacob Allen. "
            "You must investigate the unauthorized access attempt by Nathan Thompson to the production database cluster (RES-026). "
            "You must create the SIEM alert with critical severity."
        ),
        actions=[
            Action(
                name="GetUser",
                kwargs={"first_name": "Jacob", "last_name": "Allen"},
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-023", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Nathan", "last_name": "Thompson"},
            ),
            Action(
                name="CreateSiemAlert",
                kwargs={
                    "user_id": "U-013",
                    "resource_id": "RES-026",
                    "alert_type": "UNAUTHORIZED_ACCESS_ATTEMPT",
                    "severity": "CRITICAL",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "SIEM_ALERT_CREATED",
                    "actor_id": "U-023",
                    "target_id": "ALRT-013",
                    "details": "SIEM alert ALRT-013 created for UNAUTHORIZED_ACCESS_ATTEMPT on RES-026",
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={
                    "user_id": "U-013",
                    "status": "SUSPENDED",
                    "updated_by": "U-023",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-023",
                    "target_id": "U-013",
                    "details": "U-023 changed user U-013 status to SUSPENDED",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-013",
                    "only_active": True,
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-013", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-023",
                    "target_id": "U-013",
                    "details": "Role ROL-001 removed from U-013",
                },
            ),
            Action(
                name="GetSession",
                kwargs={"user_id": "U-013", "only_active": True}
            ),
            Action(
                name="CreateHubspotTicket",
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
                name="PostSlackMessage",
                kwargs={
                    "channel": "#security-incidents",
                    "message": "ALRT-013 processed: U-013 suspended and security incident ticket created.",
                    "username": "jallen",
                    "timestamp": "2025-08-08T12:00:00.000000Z",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_008",
        instruction=(
            "You are RBAC_BOT. Employee Mason Wright is leaving the company today August 8th, 2025. "
            "You must offboard him following standard policy."
        ),
        actions=[
            Action(
                name="GetUser",
                kwargs={"username": "RBAC_BOT"},
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Mason", "last_name": "Wright"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-025",
                    "only_active": False,
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-025", "status": "DISABLED"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-031",
                    "target_id": "U-025",
                    "details": "RBAC_BOT changed user U-025 status to DISABLED",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-025", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-025",
                    "details": "Role ROL-001 removed from U-025",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-025", "role_id": "ROL-003", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-025",
                    "details": "Role ROL-003 removed from U-025",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-025",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="CreateHubspotTicket",
                kwargs={
                    "subject": "Offboard employee Mason Wright (mwright)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-031",
                    "assignee_id": "U-005",
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_009",
        instruction=(
            "You are HR_ONBOARD_BOT. Marketing analyst Madison Martinez is leaving the company today August 5th, 2025. "
            "Her replacement, Noah Martinez, is starting immediately. You must offboard Madison and onboard Noah with identical access."
        ),
        actions=[
            Action(
                name="GetUser",
                kwargs={"username": "HR_ONBOARD_BOT"},
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Madison", "last_name": "Johnson"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-014",
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-014", "status": "DISABLED"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "HR_ONBOARD_BOT changed user U-014 status to DISABLED",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-006",
                    "action": "REMOVE",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "Role ROL-006 removed from U-014",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-009",
                    "action": "REMOVE",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "Role ROL-009 removed from U-014",
                },
            ),
            Action(
                name="CreateHubspotTicket",
                kwargs={
                    "subject": "Offboard employee Madison Martinez (mjackson)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "dwilson",
                    "email": "Noah.Martinez@sigmatech.com",
                    "department": "Marketing",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-006",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-006 added to U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-009",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-009 added to U-034",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "receiver": "Noah.Martinez@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Noah, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@sigmatech.com",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="CheckSodConflicts",
                kwargs={
                    "user_id": "U-034",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-014",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
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
                name="GetUser",
                kwargs={"username": "RBAC_BOT"},
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetSiemAlert",
                kwargs={"alert_id": "ALRT-011"},
            ),
            Action(
                name="CanAccessResource",
                kwargs={"user_id": "U-007", "resource_id": "RES-020"},
            ),
            Action(
                name="UpdateUser",
                kwargs={
                    "user_id": "U-007",
                    "status": "SUSPENDED",
                    "updated_by": "U-031",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-031",
                    "target_id": "U-007",
                    "details": "RBAC_BOT changed user U-007 status to SUSPENDED",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-007",
                    "only_active": False,
                    "include_role_details": False,
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-007", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-007",
                    "details": "Role ROL-001 removed from U-007",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-007", "role_id": "ROL-002", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-007",
                    "details": "Role ROL-002 removed from U-007",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-007", "role_id": "ROL-003", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-007",
                    "details": "Role ROL-003 removed from U-007",
                },
            ),
            Action(
                name="CreateHubspotTicket",
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
                name="PostSlackMessage",
                kwargs={
                    "channel": "#security-incidents",
                    "message": "ALRT-011 processed: U-007 suspended and security incident ticket created.",
                    "username": "RBAC_BOT",
                    "timestamp": "2025-08-08T12:00:00.000000Z",
                },
            ),
            Action(
                name="GetUser",
                kwargs={"user_id": "U-007"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={"user_id": "U-007", "only_active": True},
            ),
            Action(
                name="GetSession", kwargs={"user_id": "U-007", "only_active": True}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_011",
        instruction=(
            "You're lead engineer Noah Thompson. You must review Grace Young's pending access request for read-only HR data and approve it per policy."
            "Then, if approved, add the requested role to her account and return Grace Young's updated roles."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Rodriguez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Grace", "last_name": "Young"}
            ),
            Action(
                name="GetAccessRequest",
                kwargs={"user_id": "U-022", "status": "PENDING"},
            ),
            Action(name="GetResource", kwargs={"resource_id": "RES-020"}),
            Action(name="GetRole", kwargs={"role_id": "ROL-017"}),
            Action(
                name="DecideAccessRequest",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-022",
                    "role_id": "ROL-017",
                    "action": "ADD",
                    "assigned_by": "U-005",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-005",
                    "target_id": "U-022",
                    "details": "Role ROL-017 added to U-022",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ACCESS_GRANTED",
                    "actor_id": "U-005",
                    "target_id": "AR-030",
                    "details": "Access request AR-030 was approved by U-005",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "Noah.Thompson@sigmatech.com",
                    "receiver": "grace.young@sigmatech.com",
                    "subject": "Access Request APPROVED",
                    "text_content": "Your access request AR-030 has been APPROVED.",
                },
            ),
            Action(name="GetAccessRequest", kwargs={"request_id": "AR-030"}),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-022",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_012",
        instruction=(
            "You're finance lead Olivia Lee."
            "You must review Mia Robinson's pending access request for read-only finance data and approve it per policy."
            "Then, if approved, add the requested role to her account and return Mia's updated roles."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Lee"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Mia", "last_name": "Robinson"},
            ),
            Action(
                name="GetAccessRequest",
                kwargs={"user_id": "U-018", "status": "PENDING"},
            ),
            Action(name="GetResource", kwargs={"resource_id": "RES-034"}),
            Action(name="GetRole", kwargs={"role_id": "ROL-030"}),
            Action(
                name="DecideAccessRequest",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-018",
                    "role_id": "ROL-030",
                    "action": "ADD",
                    "assigned_by": "U-006",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-006",
                    "target_id": "U-018",
                    "details": "Role ROL-030 added to U-018",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ACCESS_GRANTED",
                    "actor_id": "U-006",
                    "target_id": "AR-034",
                    "details": "Access request AR-034 was approved by U-006",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "olivia.Lee@sigmatech.com",
                    "receiver": "mia.robinson@sigmatech.com",
                    "subject": "Access Request APPROVED",
                    "text_content": "Your access request AR-034 has been APPROVED.",
                },
            ),
            Action(name="GetAccessRequest", kwargs={"request_id": "AR-034"}),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-018",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_013",
        instruction=(
            "You're lead engineer Mason Martinez. "
            "William Thompson has a policy exception that is pending review. "
            "You must review it per policy, reject it, and record an audit entry for your decision."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Mason", "last_name": "Martinez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "William", "last_name": "Thompson"},
            ),
            Action(
                name="GetPolicyException",
                kwargs={"user_id": "U-007", "status": "PENDING_REVIEW"},
            ),
            Action(name="GetPermission", kwargs={"permission_id": "P-005"}),
            Action(name="GetResource", kwargs={"resource_id": "RES-002"}),
            Action(
                name="DecidePolicyException",
                kwargs={
                    "exception_id": "PE-018",
                    "reviewer_id": "U-001",
                    "decision": "DENIED",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_DENIED",
                    "actor_id": "U-001",
                    "target_id": "PE-018",
                    "details": "U-001 denied exception PE-018",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-018 denied by U-001",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "rbac@sigmatech.com",
                    "receiver": "william.thompson@sigmatech.com",
                    "subject": "Policy Exception DENIED",
                    "text_content": "Your policy exception request PE-018 has been DENIED.",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-018"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_014",
        instruction=(
            "You are RBAC_BOT. Finance analyst Mia Robinson needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 15th, 2025). "
            "Mia claims her reason for the request is 'quarter-close filing requires elevated permission' and she needs the 'submit-tax-filing' permission."
            "You must create the exception and assign Olivia Lee as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Mia", "last_name": "Robinson"},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Anderson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-018",
                    "permission_id": "P-084",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-15",
                    "expires_on": "2025-10-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_015",
        instruction=(
            "You're operations manager Noah Thompson. "
            "You must complete the pending certification for the network firewall main resource (RES-027)."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="GetCertification",
                kwargs={"user_id": "U-005", "status": "PENDING"},
            ),
            Action(
                name="ListUsersWithAccessToResource",
                kwargs={"resource_id": "RES-027", "include_role_details": True},
            ),
            Action(
                name="CanAccessResource",
                kwargs={"user_id": "U-005", "resource_id": "RES-027"},
            ),
            Action(
                name="CanAccessResource",
                kwargs={"user_id": "U-023", "resource_id": "RES-027"},
            ),
            Action(
                name="CompleteCertification",
                kwargs={"certification_id": "C-020", "reviewer_id": "U-005"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "CERTIFICATION_COMPLETED",
                    "actor_id": "U-005",
                    "target_id": "C-020",
                    "details": "Certification C-020 for RES-027 was completed",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#certifications",
                    "message": "C-020 for RES-027 completed by U-005",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_016",
        instruction=(
            "You're finance lead Olivia Lee. Aria Hill is PENDING_ACCESS but has been cleared for activation. "
            "She has a pending request access request that is valid."
            "You must activate Aria's account. "
            "You must approve the request and add the requested roles to Aria's account."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Anderson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Aria", "last_name": "Hill"}
            ),
            Action(
                name="UpdateUser",
                kwargs={
                    "user_id": "U-030",
                    "status": "ACTIVE",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-006",
                    "target_id": "U-030",
                    "details": "U-006 changed user U-030 status to ACTIVE",
                },
            ),
            Action(
                name="GetAccessRequest",
                kwargs={"user_id": "U-030", "status": "PENDING"},
            ),
            Action(name="GetResource", kwargs={"resource_id": "RES-032"}),
            Action(name="GetRole", kwargs={"role_id": "ROL-032"}),
            Action(
                name="DecideAccessRequest",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-006",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-030",
                    "role_id": "ROL-032",
                    "action": "ADD",
                    "assigned_by": "U-006",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-006",
                    "target_id": "U-030",
                    "details": "Role ROL-032 added to U-030",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ACCESS_GRANTED",
                    "actor_id": "U-006",
                    "target_id": "AR-008",
                    "details": "Access request AR-008 was approved by U-006",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "olivia.Lee@sigmatech.com",
                    "receiver": "aria.hill@sigmatech.com",
                    "subject": "Access Request APPROVED",
                    "text_content": "Your access request AR-008 has been APPROVED.",
                },
            ),
            Action(name="GetAccessRequest", kwargs={"request_id": "AR-008"}),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-030",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_017",
        instruction=(
            "You're marketing lead Sophia Thompson."
            "Sophie Turner has two pending access requests, "
            "you must approve or reject both requests according to policy "
            "then you must modify her roles accordingly."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Thompson"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-002"}),
            Action(
                name="GetUser",
                kwargs={"first_name": "Sophie", "last_name": "Turner"},
            ),
            Action(
                name="GetUserRoles", kwargs={"user_id": "U-026", "only_active": True}
            ),
            Action(
                name="GetAccessRequest",
                kwargs={"user_id": "U-026", "status": "PENDING"},
            ),
            Action(name="GetResource", kwargs={"resource_id": "RES-008"}),
            Action(
                name="CheckSodConflicts",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-008",
                },
            ),
            Action(
                name="DecideAccessRequest",
                kwargs={
                    "request_id": "AR-009",
                    "reviewer_id": "U-002",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ACCESS_GRANTED",
                    "actor_id": "U-002",
                    "target_id": "AR-009",
                    "details": "Access request AR-009 was approved by U-002",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-008",
                    "action": "ADD",
                    "assigned_by": "U-002",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-002",
                    "target_id": "U-026",
                    "details": "Role ROL-008 added to U-026",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "Sophia.Thompson@sigmatech.com",
                    "receiver": "sophie.turner@sigmatech.com",
                    "subject": "Access Request APPROVED",
                    "text_content": "Your access request AR-009 has been APPROVED.",
                },
            ),
            Action(
                name="DecideAccessRequest",
                kwargs={
                    "request_id": "AR-021",
                    "reviewer_id": "U-002",
                    "decision": "REJECTED",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ACCESS_REJECTED",
                    "actor_id": "U-002",
                    "target_id": "AR-021",
                    "details": "Access request AR-021 was rejected by U-002",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "Sophia.Thompson@sigmatech.com",
                    "receiver": "sophie.turner@sigmatech.com",
                    "subject": "Access Request REJECTED",
                    "text_content": "Your access request AR-021 has been REJECTED.",
                },
            ),
            Action(name="GetAccessRequest", kwargs={"request_id": "AR-009"}),
            Action(name="GetAccessRequest", kwargs={"request_id": "AR-021"}),
            Action(
                name="GetUserRoles", kwargs={"user_id": "U-026", "only_active": True}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_018",
        instruction=(
            "You are RBAC_BOT. Finance analyst Victoria Lee needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 10th, 2025). "
            "Victoria claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Mason Martinez as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Victoria", "last_name": "Lee"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Mason", "last_name": "Martinez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-012",
                    "permission_id": "P-084",
                    "reviewed_by": "U-001",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-10",
                    "expires_on": "2025-10-10T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_019",
        instruction=(
            "You are RBAC_BOT. Finance analyst Chloe Scott needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD September 30th, 2025). "
            "Chloe claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Sophia Thompson as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Chloe", "last_name": "Scott"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Thompson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-002", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-024",
                    "permission_id": "P-084",
                    "reviewed_by": "U-002",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-09-30",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_020",
        instruction=(
            "You are RBAC_BOT. Engineer Mason Martinez needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD September 25th, 2025). "
            "Mason claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Noah Thompson as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Mason", "last_name": "Martinez"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-001",
                    "permission_id": "P-084",
                    "reviewed_by": "U-005",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-09-25",
                    "expires_on": "2025-09-25T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_021",
        instruction=(
            "You are RBAC_BOT. Finance lead Olivia Lee has approved the pending policy exception for Chloe Scott. "
            "You must inspect the details of the request and approve the exception and proceed according to policy."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(name="IsAdmin", kwargs={"user_id": "U-031"}),
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Lee"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Chloe", "last_name": "Scott"}
            ),
            Action(
                name="GetPolicyException",
                kwargs={"user_id": "U-024", "status": "PENDING_REVIEW"},
            ),
            Action(name="GetPermission", kwargs={"permission_id": "P-088"}),
            Action(name="GetResource", kwargs={"resource_id": "RES-035"}),
            Action(
                name="DecidePolicyException",
                kwargs={
                    "exception_id": "PE-019",
                    "reviewer_id": "U-006",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_APPROVED",
                    "actor_id": "U-006",
                    "target_id": "PE-019",
                    "details": "U-006 approved exception PE-019",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-019 approved by U-006",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "rbac@sigmatech.com",
                    "receiver": "chloe.scott@sigmatech.com",
                    "subject": "Policy Exception Approved",
                    "text_content": "Your policy exception request PE-019 has been approved.",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-019"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_022",
        instruction=(
            "You are RBAC_BOT. You must promote HR specialist Emma Martinez to HR Lead by adding the hr-lead role, there is no need to remove any roles. "
            "Update her role assignments accordingly and follow promotion policy for notifications."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Emma", "last_name": "Martinez"}
            ),
            Action(name="GetRole", kwargs={"role_name": "hr-lead"}),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-010",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-010",
                    "role_id": "ROL-037",
                    "action": "ADD",
                    "assigned_by": "U-031",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-010",
                    "details": "Role ROL-037 added to U-010",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#human-resources",
                    "message": "ejohnson promoted to hr-lead by RBAC_BOT.",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "rbac@sigmatech.com",
                    "receiver": "emma.Martinez@sigmatech.com",
                    "subject": "Promotion: hr-lead",
                    "text_content": "Your role has been updated to include hr-lead. Congratulations.",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-010",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_023",
        instruction=(
            "You are RBAC_BOT. You must swap leadership within Human Resources: demote Emma Martinez from HR Recruitment Manager to base HR employee "
            "and promote Ava Martinez to HR Recruitment Manager with all of the same roles as Emma. Record audit entries, notify the HR channel, email the promoted user, and return "
            "both users' updated roles."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031"},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Emma", "last_name": "Johnson"}
            ),
            Action(
                name="GetUserRoles", kwargs={"user_id": "U-010", "only_active": True}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-010",
                    "role_id": "ROL-019",
                    "action": "REMOVE",
                    "assigned_by": "U-031",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-010",
                    "details": "Role ROL-019 removed from U-010",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Ava", "last_name": "Johnson"}
            ),
            Action(name="GetUserRoles", kwargs={"user_id": "U-016"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-016",
                    "role_id": "ROL-019",
                    "action": "ADD",
                    "assigned_by": "U-031",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-016",
                    "details": "Role ROL-019 added to U-016",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#human-resources",
                    "message": "ejohnson promoted to hr-recruitment-manager by RBAC_BOT.",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "rbac@sigmatech.com",
                    "receiver": "ava.Johnson@sigmatech.com",
                    "subject": "Promotion: hr-recruitment-manager",
                    "text_content": "Your role has been updated to include hr-recruitment-manager. Congratulations.",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-010",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-016",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_024",
        instruction=(
            "You are HR_ONBOARD_BOT. A new employee named Olivia Perez has just been hired to the Sales department to replace Ethan Wilson, who has been promoted to sales-lead-manager."
            "You must onboard Olivia following the standard procedures, add all of Ethan's active roles to hers, and return Olivia's active roles."
            "You must carry out Ethan's promotion by adding the sales-lead-manager role to his account."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Ethan", "last_name": "Johnson"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-015",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "operez",
                    "email": "olivia.perez@sigmatech.com",
                    "department": "Sales",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-011",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-011 added to U-034",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "receiver": "olivia.perez@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Olivia, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@sigmatech.com",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-032",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "sales-lead-manager"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-015",
                    "role_id": "ROL-013",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-015",
                    "details": "Role ROL-013 added to U-015",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#sales",
                    "message": "ebrown promoted to sales-lead-manager by RBAC_BOT.",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "rbac@sigmatech.com",
                    "receiver": "ethan.Johnson@sigmatech.com",
                    "subject": "Promotion: sales-lead-manager",
                    "text_content": "Your role has been updated to include sales-lead-manager. Congratulations.",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-015",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_025",
        instruction=(
            "You are RBAC_BOT. Benjamin Johnson (Operations) has left the company. "
            "You must offboard Benjamin immediately, his account is already disabled. Ensure your actions are auditable."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Benjamin", "last_name": "Wilson"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-011",
                    "only_active": False,
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-011", "role_id": "ROL-021", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-011",
                    "details": "Role ROL-021 removed from U-011",
                },
            ),
            Action(
                name="CreateHubspotTicket",
                kwargs={
                    "subject": "Offboard employee Benjamin Johnson (bharris)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "requester_id": "U-031",
                    "category": "OFFBOARDING",
                    "assignee_id": "U-005",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-011",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_026",
        instruction=(
            "You are HR_ONBOARD_BOT. A new employee named Olivia Allen has joined the Finance department. "
            "You must onboard her based on company policy, also give her the 'finance-read' role."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "ogreen",
                    "email": "olivia.Allen@sigmatech.com",
                    "department": "Finance",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-032",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment", kwargs={"department": "Finance"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-029",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-029 added to U-034",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "finance-read"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-030",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-030 added to U-034",
                },
            ),
            Action(name="CheckSodConflicts", kwargs={"user_id": "U-034"}),
            Action(
                name="SendEmail",
                kwargs={
                    "receiver": "olivia.Allen@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Olivia, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@sigmatech.com",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Allen"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_027",
        instruction=(
            "You are Operations Lead Noah Thompson. During an IT audit, you found Jacob Allen's 'operations-deployment-admin' role is redundant. "
            "You must remove it and open a remediation ticket."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Rodriguez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Jacob", "last_name": "Allen"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-023",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-023", "role_id": "ROL-025", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-005",
                    "target_id": "U-023",
                    "details": "Role ROL-025 removed from U-023",
                },
            ),
            Action(
                name="CreateHubspotTicket",
                kwargs={
                    "subject": "Audit Remediation",
                    "description": "Revoked redundant role 'operations-deployment-admin' from user 'jallen' as per audit finding.",
                    "requester_id": "U-005",
                    "category": "COMPLIANCE",
                    "assignee_id": "U-005",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-023",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_028",
        instruction=(
            "You are RBAC_BOT. Marketing analyst Sophia Rodriguez needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD September 20th, 2025). "
            "Sophia claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Olivia Lee as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Rodriguez"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Anderson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-002",
                    "permission_id": "P-084",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-09-20",
                    "expires_on": "2025-09-20T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_029",
        instruction=(
            "You're operations manager Noah Thompson. You must review Oliver Lewis's pending access request for operations-system-admin and approve it per policy. "
            "Then, add the requested role to his account and return Oliver's updated roles."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Oliver", "last_name": "Lewis"}
            ),
            Action(
                name="GetUserRoles", kwargs={"user_id": "U-029", "only_active": True}
            ),
            Action(
                name="GetAccessRequest",
                kwargs={"user_id": "U-029", "status": "PENDING"},
            ),
            Action(name="GetResource", kwargs={"resource_id": "RES-025"}),
            Action(name="GetRole", kwargs={"role_id": "ROL-026"}),
            Action(
                name="DecideAccessRequest",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "decision": "APPROVED",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-026",
                    "action": "ADD",
                    "assigned_by": "U-005",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-005",
                    "target_id": "U-029",
                    "details": "Role ROL-026 added to U-029",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ACCESS_GRANTED",
                    "actor_id": "U-005",
                    "target_id": "AR-007",
                    "details": "Access request AR-007 was approved by U-005",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "Noah.Thompson@sigmatech.com",
                    "receiver": "oliver.lewis@sigmatech.com",
                    "subject": "Access Request APPROVED",
                    "text_content": "Your access request AR-007 has been APPROVED.",
                },
            ),
            Action(name="GetAccessRequest", kwargs={"request_id": "AR-007"}),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-029",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_030",
        instruction=(
            "You are RBAC_BOT. Engineer William Thompson needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 1st, 2025). "
            "William claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Noah Thompson as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "William", "last_name": "Thompson"},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-007",
                    "permission_id": "P-084",
                    "reviewed_by": "U-005",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-01",
                    "expires_on": "2025-10-01T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_031",
        instruction=(
            "You are operations manager Noah Thompson. SIEM Alert ALRT-012 has been resolved. "
            "You must find and close the open security incident ticket regarding ALRT-012. "
            "You must ensure the correct communication channels are updated."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="GetHubspotTicket", kwargs={"alert_id": "ALRT-012"}),
            Action(
                name="UpdateHubspotTicket",
                kwargs={"ticket_id": "TI-053", "status": "CLOSED"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "TICKET_CLOSED",
                    "actor_id": "U-005",
                    "target_id": "TI-053",
                    "details": "Closed security incident ticket TI-053",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#security-incidents",
                    "message": "Ticket TI-053 closed by U-005.",
                    "username": "RBAC_BOT",
                    "timestamp": "2025-08-08T12:00:00.000000Z",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_032",
        instruction=(
            "You are RBAC_BOT. Create a new certification for the IAM / RBAC portal to prepare for audit by reviewer Noah Thompson, due EOD October 12th, 2025."
            "You must ensure Noah is in fact the owner of the IAM / RBAC portal, has authority to review it."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(name="IsAdmin", kwargs={"user_id": "U-031"}),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="GetResource", kwargs={"name": "IAM / RBAC portal"}),
            Action(
                name="CreateCertification",
                kwargs={
                    "reviewer_id": "U-005",
                    "resource_id": "RES-042",
                    "status": "PENDING",
                    "due_date": "2025-10-12T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "CERTIFICATION_CREATED",
                    "actor_id": "U-031",
                    "target_id": "C-024",
                    "details": "Certification C-024 for RES-042 was created.",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#certifications",
                    "message": "C-024 created for RES-042 assigned to U-005.",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_033",
        instruction=(
            "You are engineering lead Mason Martinez. You must create a new permission 'approve-merge' on the 'main-application-repo' resource with "
            "description 'Allows approving merges on the main repository'. "
            "Then assign this permission to the existing 'engineering-lead' role."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Mason", "last_name": "Martinez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(name="GetResource", kwargs={"name": "main-application-repo"}),
            Action(
                name="CreatePermission",
                kwargs={
                    "action": "approve-merge",
                    "resource_id": "RES-002",
                    "description": "Allows approving merges on the main repository",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-001",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-001.",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "engineering-lead"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-034", "permission_id": "P-113"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-001",
                    "target_id": "ROL-034",
                    "details": "Permission P-113 assigned to role ROL-034.",
                },
            ),
            Action(name="GetUser", kwargs={"role_id": "ROL-034", "status": "ACTIVE"}),
            Action(name="CheckSodConflicts", kwargs={"user_id": "U-001"}),
            Action(
                name="GetRolePermissions",
                kwargs={
                    "role_id": "ROL-034",
                    "permission_id": "P-113",
                    "include_role": True,
                    "include_permission": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_034",
        instruction=(
            "You are operations lead Noah Thompson. You must create a new permission 'close-siem-incident' on the 'SIEM' resource with description 'Allows closing incidents in the SIEM'. "
            "Then assign this permission to the existing 'operations-lead' role."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="GetResource", kwargs={"name": "SIEM"}),
            Action(
                name="CreatePermission",
                kwargs={
                    "action": "close-siem-incident",
                    "resource_id": "RES-040",
                    "description": "Allows closing incidents in the SIEM",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-005",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-005.",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "operations-lead"}),
            Action(name="GetUser", kwargs={"role_id": "ROL-038", "status": "ACTIVE"}),
            Action(name="CheckSodConflicts", kwargs={"user_id": "U-005"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-038", "permission_id": "P-113"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-005",
                    "target_id": "ROL-038",
                    "details": "Permission P-113 assigned to role ROL-038.",
                },
            ),
            Action(
                name="GetRolePermissions",
                kwargs={
                    "role_id": "ROL-038",
                    "permission_id": "P-113",
                    "include_role": True,
                    "include_permission": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_035",
        instruction=(
            "You are marketing lead Sophia Thompson. You must create a new permission 'approve-social-post' on the 'social-media-platform' resource with description 'Allows approving scheduled social posts'. "
            "Then assign this permission to the existing 'marketing-lead' role."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Thompson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-002", "include_role_details": True},
            ),
            Action(name="GetResource", kwargs={"name": "social-media-platform"}),
            Action(
                name="CreatePermission",
                kwargs={
                    "action": "approve-social-post",
                    "resource_id": "RES-008",
                    "description": "Allows approving scheduled social posts",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-002",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-002.",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "marketing-lead"}),
            Action(name="GetUser", kwargs={"role_id": "ROL-035", "status": "ACTIVE"}),
            Action(name="CheckSodConflicts", kwargs={"user_id": "U-002"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-035", "permission_id": "P-113"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-002",
                    "target_id": "ROL-035",
                    "details": "Permission P-113 assigned to role ROL-035.",
                },
            ),

            Action(
                name="GetRolePermissions",
                kwargs={
                    "role_id": "ROL-035",
                    "permission_id": "P-113",
                    "include_role": True,
                    "include_permission": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_036",
        instruction=(
            "You are HR_ONBOARD_BOT. HR coordinator Ava Martinez is changing her last name to Jacobs and taking leave until EOD September 30th, 2025. "
            "Update her profile and set her account to inactive during leave. "
            "While Ava is on leave, create a policy exception to be reviewed by Sophia Thompson so that Lily Martin can temporarily 'Process payroll in the system' until EOD September 30th, 2025."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="IsAdmin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="GetUser", kwargs={"first_name": "Ava", "last_name": "Martinez"}),
            Action(name="GetUser", kwargs={"username": "ljacobs", "allow_missing": True}),
            Action(name="UpdateUser", kwargs={"user_id": "U-016", "last_name": "Jacobs"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-016",
                    "details": "U-032 updated user U-016 name to Ava Jacobs; username set to ljacobs; email set to Ava.jacobs@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#human-resources",
                    "message": "User U-016 updated by U-032: username ejohnson -> ljacobs; email set to Ava.jacobs@sigmatech.com; name set to Ava Jacobs.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="UpdateUser", kwargs={"user_id": "U-016", "status": "INACTIVE"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-016",
                    "details": "HR_ONBOARD_BOT changed user U-016 status to INACTIVE",
                },
            ),
            Action(name="GetUser", kwargs={"first_name": "Lily", "last_name": "Martin"}),
            Action(name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Thompson"}),
            Action(name="IsAdmin", kwargs={"user_id": "U-004", "include_role_details": True}),
            Action(name="GetPermission", kwargs={"description": "Process payroll in the system"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-028",
                    "permission_id": "P-051",
                    "reviewed_by": "U-004",
                    "reason": "Temporary access to perform process-payroll until 2025-09-30",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-032",
                    "target_id": "PE-021",
                    "details": "HR_ONBOARD_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-032",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="GetUser", kwargs={"username": "ljacobs"}),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_037",
        instruction=(
            "You are finance lead Olivia Lee. You must create a new permission 'lock-ledger-period' on the 'general-ledger-db' resource with description 'Allows locking accounting periods in the ledger'. "
            "Then assign this permission to the existing 'finance-lead' role."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Lee"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="GetResource", kwargs={"name": "general-ledger-db"}),
            Action(name="GetRole", kwargs={"role_name": "finance-lead"}),
            Action(
                name="CreatePermission",
                kwargs={
                    "action": "lock-ledger-period",
                    "resource_id": "RES-031",
                    "description": "Allows locking accounting periods in the ledger",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-006",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-006.",
                },
            ),
            Action(name="GetUser", kwargs={"role_id": "ROL-039", "status": "ACTIVE"}),
            Action(name="CheckSodConflicts", kwargs={"user_id": "U-006"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-039", "permission_id": "P-113"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-006",
                    "target_id": "ROL-039",
                    "details": "Permission P-113 assigned to role ROL-039.",
                },
            ),
            Action(
                name="GetRolePermissions",
                kwargs={
                    "role_id": "ROL-039",
                    "permission_id": "P-113",
                    "include_role": True,
                    "include_permission": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_038",
        instruction=(
            "You are HR_ONBOARD_BOT. Finance analyst Victoria Lee is changing her last name to Andrews and taking leave until EOD December 1st, 2025. "
            "Update her profile and set her account to inactive during the leave. "
            "Create a time-bound policy exception so that teammate Chloe Scott can 'restart-prod-service' until EOD December 1st, 2025, to be reviewed by Finance lead Olivia Lee."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="IsAdmin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="GetUser", kwargs={"first_name": "Victoria", "last_name": "Lee"}),
            Action(name="GetUser", kwargs={"username": "landrews", "allow_missing": True}),
            Action(name="UpdateUser", kwargs={"user_id": "U-012", "last_name": "Andrews"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "U-032 updated user U-012 name to Victoria Andrews; username set to landrews; email set to Victoria.andrews@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#finance",
                    "message": "User U-012 updated by U-032: username vlee -> landrews; email set to Victoria.andrews@sigmatech.com; name set to Victoria Andrews.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="UpdateUser", kwargs={"user_id": "U-012", "status": "INACTIVE"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "HR_ONBOARD_BOT changed user U-012 status to INACTIVE",
                },
            ),
            Action(name="GetUser", kwargs={"first_name": "Chloe", "last_name": "Scott"}),
            Action(name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Lee"}),
            Action(name="IsAdmin", kwargs={"user_id": "U-006", "include_role_details": True}),
            Action(name="GetPermission", kwargs={"action": "restart-prod-service"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-024",
                    "permission_id": "P-061",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform restart-prod-service until 2025-12-01",
                    "expires_on": "2025-12-01T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-032",
                    "target_id": "PE-021",
                    "details": "HR_ONBOARD_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-032",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="GetUser", kwargs={"username": "landrews"}),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_039",
        instruction=(
            "You are HR_ONBOARD_BOT. Operations engineer Oliver Lewis is changing his last name to Carver and will be on leave until EOD October 31st, 2025. "
            "Update his profile and set his account to inactive during leave. "
            "While Oliver is on leave, assign a temporary 'operations-incident-response' role to Noah Thompson for coverage."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="IsAdmin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="GetUser", kwargs={"first_name": "Oliver", "last_name": "Lewis"}),
            Action(name="GetUser", kwargs={"username": "pcarver", "allow_missing": True}),
            Action(name="UpdateUser", kwargs={"user_id": "U-029", "last_name": "Carver"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "U-032 updated user U-029 name to Oliver Carver; username set to pcarver; email set to Oliver.carver@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#operations",
                    "message": "User U-029 updated by U-032: username olewis -> pcarver; email set to Oliver.carver@sigmatech.com; name set to Oliver Carver.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="UpdateUser", kwargs={"user_id": "U-029", "status": "INACTIVE"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "HR_ONBOARD_BOT changed user U-029 status to INACTIVE",
                },
            ),
            Action(name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}),
            Action(name="GetUserRoles", kwargs={"user_id": "U-005", "only_active": True}),
            Action(name="GetRole", kwargs={"role_name": "operations-incident-response"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-005",
                    "role_id": "ROL-023",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-10-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-005",
                    "details": "Role ROL-023 added to U-005",
                },
            ),
            Action(name="GetUser", kwargs={"username": "pcarver"}),
            Action(name="GetUserRoles", kwargs={"user_id": "U-005", "only_active": True}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_040",
        instruction=(
            "You're Operations lead Noah Thompson. You must review Emma Martinez's pending access request for recruitment manager access. "
            "Decide the access request according to policy, then return the updated request and Emma's roles."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Rodriguez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005"},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Emma", "last_name": "Johnson"}
            ),
            Action(
                name="GetAccessRequest",
                kwargs={"user_id": "U-010", "status": "PENDING"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-010",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="DecideAccessRequest",
                kwargs={
                    "request_id": "AR-037",
                    "reviewer_id": "U-005",
                    "decision": "REJECTED",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ACCESS_REJECTED",
                    "actor_id": "U-005",
                    "target_id": "AR-037",
                    "details": "Access request AR-037 was rejected by U-005",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "Noah.Thompson@sigmatech.com",
                    "receiver": "emma.Martinez@sigmatech.com",
                    "subject": "Access Request REJECTED",
                    "text_content": "Your access request AR-037 has been REJECTED.",
                },
            ),
            Action(name="GetAccessRequest", kwargs={"request_id": "AR-037"}),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-010",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
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
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetHubspotTicket",
                kwargs={"alert_id": "ALRT-012", "status": "OPEN"},
            ),
            Action(name="GetSiemAlert", kwargs={"alert_id": "ALRT-012"}),
            Action(
                name="CanAccessResource",
                kwargs={"user_id": "U-004", "resource_id": "RES-014"},
            ),
            Action(
                name="UpdateUser",
                kwargs={
                    "user_id": "U-004",
                    "status": "SUSPENDED",
                    "updated_by": "U-031",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-031",
                    "target_id": "U-004",
                    "details": "RBAC_BOT changed user U-004 status to SUSPENDED",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-004",
                    "only_active": False,
                    "include_role_details": False,
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-004",
                    "role_id": "ROL-016",
                    "action": "REMOVE",
                    "assigned_by": "U-031",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-004",
                    "details": "Role ROL-016 removed from U-004",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-004",
                    "role_id": "ROL-037",
                    "action": "REMOVE",
                    "assigned_by": "U-031",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-004",
                    "details": "Role ROL-037 removed from U-004",
                },
            ),
            Action(
                name="UpdateHubspotTicket",
                kwargs={"ticket_id": "TI-053", "status": "CLOSED"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "TICKET_CLOSED",
                    "actor_id": "U-031",
                    "target_id": "TI-053",
                    "details": "Closed security incident ticket TI-053",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#security-incidents",
                    "message": "ALRT-012 processed: U-004 suspended and security incident ticket closed.",
                    "username": "RBAC_BOT",
                    "timestamp": "2025-08-08T12:00:00.000000Z",
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-004"}),
            Action(
                name="GetUserRoles", kwargs={"user_id": "U-004", "only_active": True}
            ),
            Action(
                name="GetSession", kwargs={"user_id": "U-004", "only_active": True}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_042",
        instruction=(
            "You are RBAC_BOT. Sales analyst Alexander Clark needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 5th, 2025). "
            "Alexander claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Olivia Lee as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Alexander", "last_name": "Clark"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Anderson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-009",
                    "permission_id": "P-084",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-05",
                    "expires_on": "2025-10-05T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
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
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={
                    "department": "Operations",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-005", "mfa_enabled": True, "status": "INACTIVE"},
            ),
            Action(
                name="GetSession", kwargs={"user_id": "U-005", "only_active": True}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_MFA_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-005",
                    "details": "RBAC_BOT changed user U-005 mfa_enabled to True",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "rbac@sigmatech.com",
                    "receiver": "Noah.Thompson@sigmatech.com",
                    "subject": "MFA Updated",
                    "text_content": "Your MFA setting has been updated to True. Please review your account settings.",
                },
            ),
            Action(
                name="GetUserRoles", kwargs={"user_id": "U-005", "only_active": True}
            ),
            Action(
                name="GetBaseRoleByDepartment",
                kwargs={"department": "Operations"},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-005", "role_id": "ROL-038", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-031",
                    "target_id": "U-005",
                    "details": "Role ROL-038 removed from U-005",
                },
            ),
            Action(
                name="GetUserRoles", kwargs={"user_id": "U-005", "only_active": True}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_044",
        instruction=(
            "You are RBAC_BOT. HR partner Emma Martinez needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 12th, 2025). "
            "Emma claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Noah Thompson as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Emma", "last_name": "Johnson"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Rodriguez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-010",
                    "permission_id": "P-084",
                    "reviewed_by": "U-005",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-12",
                    "expires_on": "2025-10-12T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_045",
        instruction=(
            "You are RBAC_BOT. Engineer Noah Martinez needs a time-bound policy exception to 'Configure CI/CD pipeline'. "
            "You must create the exception for the appropriate engineering permission, set to expire EOD a week from today August 8th, 2025 with Mason Martinez as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Mason", "last_name": "Martinez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="GetPermission",
                kwargs={"description": "Configure CI/CD pipeline"},
            ),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-019",
                    "permission_id": "P-005",
                    "reviewed_by": "U-001",
                    "reason": "Temporary access to perform configure-pipeline until 2025-08-15",
                    "expires_on": "2025-08-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                    "username": "RBAC_BOT",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_046",
        instruction=(
            "You are RBAC_BOT. Operations engineer Jacob Allen needs a time-bound policy exception to 'Modify network firewall rules'. "
            "You must create the exception for the appropriate operations permission set to expire EOD September 15th 2025 with Noah Thompson as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Jacob", "last_name": "Allen"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Rodriguez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="GetPermission",
                kwargs={"description": "Modify network firewall rules"},
            ),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-023",
                    "permission_id": "P-067",
                    "reviewed_by": "U-005",
                    "reason": "Temporary access to perform modify-firewall-rules until 2025-09-15",
                    "expires_on": "2025-09-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_047",
        instruction=(
            "You are RBAC_BOT. HR specialist Grace Young needs a time-bound policy exception to 'Modify employee benefits in system'. "
            "You must create the exception for the appropriate HR permission set to expire EOD October 31st, 2025 with Noah Thompson as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Grace", "last_name": "Young"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Rodriguez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(
                name="GetPermission",
                kwargs={"description": "Modify employee benefits in system"},
            ),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-022",
                    "permission_id": "P-057",
                    "reviewed_by": "U-005",
                    "reason": "Temporary access to perform modify-benefits until 2025-10-31",
                    "expires_on": "2025-10-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_048",
        instruction=(
            "You are RBAC_BOT. Engineer Nathan Thompson needs a time-bound policy exception to 'Deploy updates to customer-facing API'. "
            "You must create the exception for the appropriate engineering permission with Mason Martinez as the reviewer. "
            "The exception should expire at EOD August 31st, 2025."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Nathan", "last_name": "Thompson"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Mason", "last_name": "Martinez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="GetPermission",
                kwargs={"description": "Deploy updates to customer-facing API"},
            ),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-013",
                    "permission_id": "P-012",
                    "reviewed_by": "U-001",
                    "reason": "Temporary access to perform deploy-api until 2025-08-31",
                    "expires_on": "2025-08-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                    "username": "RBAC_BOT",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_049",
        instruction=(
            "You are RBAC_BOT. Marketing specialist Sophie Turner needs a time-bound policy exception to 'Send email marketing campaigns'. "
            "You must create the exception for the appropriate marketing permission with Sophia Rodriguez as the reviewer. "
            "The exception should expire at EOD September 30th, 2025."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Sophie", "last_name": "Turner"},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Rodriguez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-002", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "send-email-campaign"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-026",
                    "permission_id": "P-022",
                    "reviewed_by": "U-002",
                    "reason": "Temporary access to perform send-email-campaign until 2025-09-30",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                    "username": "RBAC_BOT",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_050",
        instruction=(
            "You are RBAC_BOT. Finance analyst Victoria Lee needs a time-bound policy exception to 'Approve invoices in invoicing system'. "
            "You must create the exception for the appropriate finance permission with Olivia Lee as the reviewer. "
            "The exception should expire at EOD September 15th, 2025."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Victoria", "last_name": "Lee"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Anderson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "approve-invoice"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-012",
                    "permission_id": "P-078",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform approve-invoice until 2025-09-15",
                    "expires_on": "2025-09-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                    "username": "RBAC_BOT",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_051",
        instruction=(
            "You are HR_ONBOARD_BOT. Mia Robinson has just gotten married and changed her last name to Thompson. "
            "You must update her user profile to accurately represent her new name. Because of her marriage, she is also taking time off until EOD August 31st, 2025."
            "You must ensure her account is inactive during her leave. During her leave, Chloe Scott will be taking over her auditing duties."
            "Chloe needs the 'finance-audit-access' role."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Mia", "last_name": "Robinson"},
            ),
            Action(
                name="GetUser",
                kwargs={"username": "srodriguez", "allow_missing": True},
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-018", "last_name": "Thompson"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-018",
                    "details": "U-032 updated user U-018 name to Mia Thompson; username set to srodriguez; email set to Mia.Thompson@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#finance",
                    "message": "User U-018 updated by U-032: username mrobinson -> srodriguez; email set to Mia.Thompson@sigmatech.com; name set to Mia Thompson.",
                    "username": "RBAC_BOT",
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-018", "status": "INACTIVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-018",
                    "details": "HR_ONBOARD_BOT changed user U-018 status to INACTIVE",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Chloe", "last_name": "Scott"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-024",
                    "only_active": True,
                },
            ),
            Action(
                name="GetRole",
                kwargs={"role_name": "finance-audit-access"},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-024",
                    "role_id": "ROL-033",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-08-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-024",
                    "details": "Role ROL-033 added to U-024",
                },
            ),
            Action(name="GetUser", kwargs={"username": "srodriguez"}),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-024",
                    "only_active": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_052",
        instruction=(
            "You are HR_ONBOARD_BOT. Emma Martinez has transitioned and updated their first name to Noah. "
            "You must update the user profile to reflect the new first name. Because they are taking leave, set her account to inactive during the leave. "
            "While they are on leave, Ava Johnson needs a time-bound policy exception until EOD September 30th, 2025 to be reviewed by Sophia Thompson so that she can temporarily "
            "'Process payroll in the system' to cover duties."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Emma", "last_name": "Johnson"}
            ),
            Action(
                name="GetUser", kwargs={"username": "nwilson", "allow_missing": True}
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-010", "first_name": "Noah"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-010",
                    "details": "U-032 updated user U-010 name to Noah Johnson; username set to nwilson; email set to noah.Johnson@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#human-resources",
                    "message": "User U-010 updated by U-032: username ejohnson -> nwilson; email set to noah.Johnson@sigmatech.com; name set to Noah Johnson.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-010", "status": "INACTIVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-010",
                    "details": "HR_ONBOARD_BOT changed user U-010 status to INACTIVE",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Ava", "last_name": "Johnson"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Taylor"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-004", "include_role_details": True},
            ),
            Action(
                name="GetPermission",
                kwargs={"description": "Process payroll in the system"},
            ),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-016",
                    "permission_id": "P-051",
                    "reviewed_by": "U-004",
                    "reason": "Temporary access to perform process-payroll until 2025-09-30",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-032",
                    "target_id": "PE-021",
                    "details": "HR_ONBOARD_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-032",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="GetUser", kwargs={"username": "nwilson"}),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_053",
        instruction=(
            "You are HR_ONBOARD_BOT. Sales rep Ethan Wilson is changing his last name to Nguyen and taking a leave of absence. "
            "You must update his profile accordingly and set his account to inactive while he is on leave. "
            "While Ethan is on leave, you must create a policy exception until EOD October 15th, 2025 to be reviewed by Noah Johnson "
            "so Sales teammate Logan Scott can temporarily 'Calculate commissions with the tool' to cover duties."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Ethan", "last_name": "Wilson"}
            ),
            Action(
                name="GetUser", kwargs={"username": "knguyen", "allow_missing": True}
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-015", "last_name": "Nguyen"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-015",
                    "details": "U-032 updated user U-015 name to Ethan Nguyen; username set to knguyen; email set to Ethan.nguyen@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#sales",
                    "message": "User U-015 updated by U-032: username ebrown -> knguyen; email set to Ethan.nguyen@sigmatech.com; name set to Ethan Nguyen.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-015", "status": "INACTIVE"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-015",
                    "details": "HR_ONBOARD_BOT changed user U-015 status to INACTIVE",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Logan", "last_name": "Scott"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Michael", "last_name": "Wilson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-003", "include_role_details": True},
            ),
            Action(
                name="GetPermission",
                kwargs={"description": "Calculate commissions with the tool"},
            ),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-021",
                    "permission_id": "P-043",
                    "reviewed_by": "U-003",
                    "reason": "Temporary access to perform calculate-commission until 2025-10-15",
                    "expires_on": "2025-10-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-032",
                    "target_id": "PE-021",
                    "details": "HR_ONBOARD_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-032",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="GetUser", kwargs={"username": "knguyen"}),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_054",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineer Noah Martinez is changing his first name to Nathan and taking a leave of absense until September 30th, 2025. "
            "You must update his profile and set his account to inactive during leave. "
            "While Noah is on leave, grant a temporary 'engineering-db-schema' role to Mason Wright until EOD September 30th, 2025 to cover production debugging."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="GetUser", kwargs={"username": "ntaylor", "allow_missing": True}
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-019", "first_name": "Nathan"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "U-032 updated user U-019 name to Nathan Thompson; username set to ntaylor; email set to nathan.Thompson@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#engineering",
                    "message": "User U-019 updated by U-032: username nmartinez -> ntaylor; email set to nathan.Thompson@sigmatech.com; name set to Nathan Thompson.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-019", "status": "INACTIVE"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "HR_ONBOARD_BOT changed user U-019 status to INACTIVE",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Mason", "last_name": "Wright"}
            ),
            Action(
                name="GetUserRoles", kwargs={"user_id": "U-025", "only_active": True}
            ),
            Action(name="GetRole", kwargs={"role_name": "engineering-db-schema"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-025",
                    "role_id": "ROL-004",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-025",
                    "details": "Role ROL-004 added to U-025",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-025",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"username": "ntaylor"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_055",
        instruction=(
            "You are HR_ONBOARD_BOT. Operations engineer Jacob Allen is changing his first name to Geoffrey and taking leave. "
            "You must update his profile accordingly and set his account to inactive during leave. "
            "While Jacob is on leave, grant a temporary 'operations-incident-response' coverage role to Operations teammate Oliver Lewis until EOD October 31st, 2025."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Jacob", "last_name": "Allen"}
            ),
            Action(
                name="GetUser", kwargs={"username": "ggreen", "allow_missing": True}
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-023", "first_name": "Geoffrey"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-023",
                    "details": "U-032 updated user U-023 name to Geoffrey Allen; username set to ggreen; email set to geoffrey.Allen@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#operations",
                    "message": "User U-023 updated by U-032: username jallen -> ggreen; email set to geoffrey.Allen@sigmatech.com; name set to Geoffrey Allen.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-023", "status": "INACTIVE"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-023",
                    "details": "HR_ONBOARD_BOT changed user U-023 status to INACTIVE",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Oliver", "last_name": "Lewis"}
            ),
            Action(
                name="GetRole", kwargs={"role_name": "operations-incident-response"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-023",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-10-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "Role ROL-023 added to U-029",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-029",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"username": "ggreen"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_056",
        instruction=(
            "You are HR_ONBOARD_BOT. Marketing analyst Madison Johnson is changing her last name to Thompson and going on leave. "
            "You must update her profile and set her account to inactive during leave. "
            "While Madison is on leave, you must create a policy exception to be reviewed by Sophia Rodriguez so Marketing teammate Sophie Turner can temporarily 'export-marketing-data' until EOD October 10th, 2025."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Madison", "last_name": "Jackson"}
            ),
            Action(
                name="GetUser", kwargs={"username": "nthompson", "allow_missing": True}
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-014", "last_name": "Thompson"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "U-032 updated user U-014 name to Madison Thompson; username set to nthompson; email set to Madison.thompson@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#marketing",
                    "message": "User U-014 updated by U-032: username mjackson -> nthompson; email set to Madison.thompson@sigmatech.com; name set to Madison Thompson.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-014", "status": "INACTIVE"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-014",
                    "details": "HR_ONBOARD_BOT changed user U-014 status to INACTIVE",
                },
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Sophie", "last_name": "Turner"},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Rodriguez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-002", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "export-marketing-data"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-026",
                    "permission_id": "P-026",
                    "reviewed_by": "U-002",
                    "reason": "Temporary access to perform export-marketing-data until 2025-10-10",
                    "expires_on": "2025-10-10T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-032",
                    "target_id": "PE-021",
                    "details": "HR_ONBOARD_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-032",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="GetUser", kwargs={"username": "nthompson"}),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_057",
        instruction=(
            "You are HR_ONBOARD_BOT. Finance analyst Victoria Lee is changing her first name to Elisabeth and taking leave until November 15th, 2025. "
            "You must update her profile and set her account to inactive during leave. "
            "While Victoria is on leave, you must grant a temporary 'finance-invoice-processor' role to teammate Chloe Scott to cover responsibilities."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Victoria", "last_name": "Lee"}
            ),
            Action(
                name="GetUser", kwargs={"username": "eanderson", "allow_missing": True}
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-012", "first_name": "Elisabeth"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "U-032 updated user U-012 name to Elisabeth Lee; username set to eanderson; email set to elisabeth.Lee@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#finance",
                    "message": "User U-012 updated by U-032: username vlee -> eanderson; email set to elisabeth.Lee@sigmatech.com; name set to Elisabeth Lee.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-012", "status": "INACTIVE"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "HR_ONBOARD_BOT changed user U-012 status to INACTIVE",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Chloe", "last_name": "Scott"}
            ),
            Action(
                name="GetUserRoles", kwargs={"user_id": "U-024", "only_active": True}
            ),
            Action(name="GetRole", kwargs={"role_name": "finance-invoice-processor"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-024",
                    "role_id": "ROL-031",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-11-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-024",
                    "details": "Role ROL-031 added to U-024",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-024",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"username": "eanderson"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_058",
        instruction=(
            "You are HR_ONBOARD_BOT. Senior Marketing Lead Sophia Rodriguez (Marketing department) is beginning a 12-month pregnancy leave effective today 2025-08-08. "
            "You must set her account to inactive, remove only her marketing-lead role."
            "We're onboarding a temporary contractor replacement named Julia Perez, "
            "she needs a temporary marketing-lead role that expires EOD 2026-08-08. "
            "Return the replacement's active roles and Sophia's updated inactive user record."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Thompson"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-002",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-002", "status": "INACTIVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-002",
                    "details": "HR_ONBOARD_BOT changed user U-002 status to INACTIVE",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-002",
                    "role_id": "ROL-035",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-002",
                    "details": "Role ROL-035 removed from U-002",
                },
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "jperez",
                    "email": "julia.perez@sigmatech.com",
                    "department": "Marketing",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment",
                kwargs={"department": "Marketing"},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-006",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-006 added to U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-035",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2026-08-08T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-035 added to U-034",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "onboarding@sigmatech.com",
                    "receiver": "julia.perez@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Julia, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-002"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_059",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineering Lead Mason Martinez (Engineering department) is beginning a 12-month pregnancy leave effective today 2025-08-08. "
            "You must set his account to inactive and remove his engineering-lead role. "
            "We're onboarding a temporary contractor replacement for Mason named Olivia Martin. "
            "You must assign Olivia a temporary engineering-lead role that expires when Mason returns EOD 2026-08-08. "
            "Return the replacement's active roles and Mason's updated inactive user record."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Mason", "last_name": "Martinez"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-001",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-001", "status": "INACTIVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-001",
                    "details": "HR_ONBOARD_BOT changed user U-001 status to INACTIVE",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-001",
                    "role_id": "ROL-034",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-001",
                    "details": "Role ROL-034 removed from U-001",
                },
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "omartin",
                    "email": "olivia.martin@sigmatech.com",
                    "department": "Engineering",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment", kwargs={"department": "Engineering"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-001",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-001 added to U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-034",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2026-08-08T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-034 added to U-034",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "onboarding@sigmatech.com",
                    "receiver": "olivia.martin@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Olivia, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-001"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_060",
        instruction=(
            "You are HR_ONBOARD_BOT. Operations Lead Noah Thompson (Operations department) is beginning a 12-month pregnancy leave effective today 2025-08-08. "
            "You must set his account to inactive and remove his operations-lead role. "
            "We're onboarding a temporary contractor replacement named Hannah Scott for Operations. "
            "You must assign Hannah a temporary operations-lead role that expires EOD 2026-08-08. "
            "Return the replacement's active roles and Noah's updated inactive user record."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032"},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-005",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-005", "status": "INACTIVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-005",
                    "details": "HR_ONBOARD_BOT changed user U-005 status to INACTIVE",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-005",
                    "role_id": "ROL-038",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-005",
                    "details": "Role ROL-038 removed from U-005",
                },
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "hscott",
                    "email": "hannah.scott@sigmatech.com",
                    "department": "Operations",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment", kwargs={"department": "Operations"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-021",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-021 added to U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-038",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2026-08-08T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-038 added to U-034",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "onboarding@sigmatech.com",
                    "receiver": "hannah.scott@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Hannah, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-005"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_061",
        instruction=(
            "You are HR_ONBOARD_BOT. Finance Lead Olivia Lee (Finance department) is beginning a 12-month pregnancy leave effective today 2025-08-08. "
            "You must set her account to inactive and remove her finance-lead role."
            "We're onboarding a temporary contractor replacement named Megan Foster, "
            "she needs a temporary finance-lead role that expires EOD 2026-08-08. "
            "Return the replacement's active roles and Olivia's updated inactive user record."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Anderson"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-006",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-006", "status": "INACTIVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-006",
                    "details": "HR_ONBOARD_BOT changed user U-006 status to INACTIVE",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-006",
                    "role_id": "ROL-039",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-006",
                    "details": "Role ROL-039 removed from U-006",
                },
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "mfoster",
                    "email": "megan.foster@sigmatech.com",
                    "department": "Finance",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment", kwargs={"department": "Finance"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-029",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-029 added to U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-039",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2026-08-08T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-039 added to U-034",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "sender": "onboarding@sigmatech.com",
                    "receiver": "megan.foster@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Megan, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-006"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_062",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineer Noah Martinez is transferring from Engineering to Operations. "
            "You must remove Noah's prior engineering roles, he now needs the base role for Operations and operations-server-monitor role. "
            "Return his updated active roles and updated user record."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-019",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-019", "department": "Operations"},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-019", "role_id": "ROL-004", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "Role ROL-004 removed from U-019",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-019", "role_id": "ROL-005", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "Role ROL-005 removed from U-019",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-019", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "Role ROL-001 removed from U-019",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment", kwargs={"department": "Operations"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-019",
                    "role_id": "ROL-021",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "Role ROL-021 added to U-019",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "operations-server-monitor"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-019",
                    "role_id": "ROL-022",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-019",
                    "details": "Role ROL-022 added to U-019",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-019",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-019"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_063",
        instruction=(
            "You are HR_ONBOARD_BOT. Finance specialist Victoria Lee is transferring from Finance to Human Resources. "
            "You must remove Victoria's finance roles, then assign hr-base and hr-benefits-admin. "
            "Return her updated active roles and updated user record."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Victoria", "last_name": "Lee"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-012",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-012", "department": "Human Resources"},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-012", "role_id": "ROL-032", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "Role ROL-032 removed from U-012",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-012", "role_id": "ROL-031", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "Role ROL-031 removed from U-012",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-012", "role_id": "ROL-029", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "Role ROL-029 removed from U-012",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment",
                kwargs={"department": "Human Resources"},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-012",
                    "role_id": "ROL-016",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "Role ROL-016 added to U-012",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "hr-benefits-admin"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-012",
                    "role_id": "ROL-020",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-012",
                    "details": "Role ROL-020 added to U-012",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-012",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-012"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_064",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineer Nathan Thompson is transferring from Engineering to Sales. "
            "You must remove Nathan's engineering roles, he now needs the base role for Sales and the sales-reporting role. "
            "Return his updated active roles and updated user record."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Nathan", "last_name": "Thompson"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-013",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-013", "department": "Sales"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-013", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-013",
                    "details": "Role ROL-001 removed from U-013",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment",
                kwargs={"department": "Sales"},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-013",
                    "role_id": "ROL-011",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-013",
                    "details": "Role ROL-011 added to U-013",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "sales-reporting"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-013",
                    "role_id": "ROL-014",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-013",
                    "details": "Role ROL-014 added to U-013",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-013",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-013"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_065",
        instruction=(
            "You are HR_ONBOARD_BOT. Marketing specialist Sophie Turner is transferring from Marketing to Engineering. "
            "You must update her department and remove all of her previous roles, then add engineering-base, engineering-code-commit, and engineering-qa-test. "
            "Return her updated active roles and updated user record."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Sophie", "last_name": "Turner"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-026",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="UpdateUser",
                kwargs={"user_id": "U-026", "department": "Engineering"},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-026", "role_id": "ROL-010", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-010 removed from U-026",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-026", "role_id": "ROL-007", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-007 removed from U-026",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-026", "role_id": "ROL-006", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-006 removed from U-026",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment", kwargs={"department": "Engineering"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-001",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-001 added to U-026",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "engineering-code-commit"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-002",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-002 added to U-026",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "engineering-qa-test"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-005",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-005 added to U-026",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-026",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-026"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_066",
        instruction=(
            "You are HR_ONBOARD_BOT. Operations engineer Oliver Lewis is transferring from Operations to Finance. "
            "You must remove his currently held roles, he now needs the base role for finance and finance-read. "
            "Return his updated active roles and updated user record."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Oliver", "last_name": "Lewis"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-029",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-029", "department": "Finance"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-029", "role_id": "ROL-021", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "Role ROL-021 removed from U-029",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment", kwargs={"department": "Finance"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-029",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "Role ROL-029 added to U-029",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "finance-read"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-030",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "Role ROL-030 added to U-029",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-029",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-029"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_067",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineer Mason Wright is transferring from Engineering to Finance. "
            "You must update his department on his user account, remove his engineering roles, "
            "for the transfer he needs the base finance role and the finance-invoice-processor role. "
            "Return his updated active roles and updated user record."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Mason", "last_name": "Wright"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={"user_id": "U-025", "only_active": False},
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-025", "department": "Finance"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-025", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-025",
                    "details": "Role ROL-001 removed from U-025",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-025", "role_id": "ROL-003", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-025",
                    "details": "Role ROL-003 removed from U-025",
                },
            ),
            Action(
                name="GetBaseRoleByDepartment", kwargs={"department": "Finance"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-025",
                    "role_id": "ROL-029",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-025",
                    "details": "Role ROL-029 added to U-025",
                },
            ),
            Action(
                name="GetRole",
                kwargs={"role_name": "finance-invoice-processor"},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-025",
                    "role_id": "ROL-031",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-025",
                    "details": "Role ROL-031 added to U-025",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-025",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_068",
        instruction=(
            "You are HR_ONBOARD_BOT. Sales rep Alexander Clark is leaving the company effective today 2025-08-08. "
            "You must offboard Alexander and immediately onboard his replacement Sophia Turner (Sales). "
            "You must replicate Alexander's roles to Sophia. "
            "Return Sophia's active roles and Alexander's now-empty assignments."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Alexander", "last_name": "Clark"}
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-009",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-009", "status": "DISABLED"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-009",
                    "details": "HR_ONBOARD_BOT changed user U-009 status to DISABLED",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-009", "role_id": "ROL-011", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-009",
                    "details": "Role ROL-011 removed from U-009",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-009", "role_id": "ROL-012", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-009",
                    "details": "Role ROL-012 removed from U-009",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-009", "role_id": "ROL-013", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-009",
                    "details": "Role ROL-013 removed from U-009",
                },
            ),
            Action(
                name="CreateHubspotTicket",
                kwargs={
                    "subject": "Offboard employee Alexander Clark (aclark)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "sturner",
                    "email": "sophia.turner@sigmatech.com",
                    "department": "Sales",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-011",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-011 added to U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-012",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-012 added to U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-013",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-013 added to U-034",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "receiver": "sophia.turner@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Sophia, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@sigmatech.com",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-009",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_069",
        instruction=(
            "You are HR_ONBOARD_BOT. Engineer William Thompson is leaving the company (effective 2025-08-08). "
            "You must offboard him and onboard replacement engineer Ethan Clark, replicating his roles (engineering-base, engineering-code-commit, engineering-prod-access). "
            "Return Ethan's roles and William's empty assignments."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "William", "last_name": "Thompson"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={"user_id": "U-007", "only_active": False},
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-007", "status": "DISABLED"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-007",
                    "details": "HR_ONBOARD_BOT changed user U-007 status to DISABLED",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-007", "role_id": "ROL-001", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-007",
                    "details": "Role ROL-001 removed from U-007",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-007", "role_id": "ROL-002", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-007",
                    "details": "Role ROL-002 removed from U-007",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-007", "role_id": "ROL-003", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-007",
                    "details": "Role ROL-003 removed from U-007",
                },
            ),
            Action(
                name="CreateHubspotTicket",
                kwargs={
                    "subject": "Offboard employee William Thompson (wthompson)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "eclark",
                    "email": "ethan.clark@sigmatech.com",
                    "department": "Engineering",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-001",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-001 added to U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-002",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-002 added to U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-003",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-003 added to U-034",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "receiver": "ethan.clark@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Ethan, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@sigmatech.com",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-007",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_070",
        instruction=(
            "You are HR_ONBOARD_BOT. HR specialist Grace Young is leaving the company. "
            "You must offboard Grace and onboard her replacement Hannah Lee (HR) replicating Grace's hr-base role. "
            "Return Hannah's roles and Grace's empty assignments."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Grace", "last_name": "Young"}
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-022", "status": "DISABLED"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-022",
                    "details": "HR_ONBOARD_BOT changed user U-022 status to DISABLED",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={"user_id": "U-022", "only_active": False},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-022", "role_id": "ROL-016", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-022",
                    "details": "Role ROL-016 removed from U-022",
                },
            ),
            Action(
                name="CreateHubspotTicket",
                kwargs={
                    "subject": "Offboard employee Grace Young (gyoung)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "hlee",
                    "email": "hannah.lee@sigmatech.com",
                    "department": "Human Resources",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-016",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-016 added to U-034",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "receiver": "hannah.lee@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Hannah, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@sigmatech.com",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-022",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_071",
        instruction=(
            "You are HR_ONBOARD_BOT. Operations engineer Oliver Lewis is leaving the company. "
            "You must offboard him and onboard replacement Liam Brooks replicating operations-base and operations-system-admin. "
            "Return Liam's roles and Oliver's empty assignments."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Oliver", "last_name": "Lewis"}
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-029", "status": "DISABLED"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "HR_ONBOARD_BOT changed user U-029 status to DISABLED",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={"user_id": "U-029", "only_active": False},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-029", "role_id": "ROL-021", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "Role ROL-021 removed from U-029",
                },
            ),
            Action(
                name="CreateHubspotTicket",
                kwargs={
                    "subject": "Offboard employee Oliver Lewis (olewis)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "lbrooks",
                    "email": "liam.brooks@sigmatech.com",
                    "department": "Operations",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-021",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-021 added to U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-026",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-026 added to U-034",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "receiver": "liam.brooks@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Liam, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@sigmatech.com",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-029",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_072",
        instruction=(
            "You are HR_ONBOARD_BOT. Finance analyst Aria Hill is leaving the company. "
            "You must offboard her and onboard replacement Noah Walker (Finance) replicating Aria's roles for Noah. "
            "Return Noah's roles and Aria's empty assignments."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Aria", "last_name": "Hill"}
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-030", "status": "DISABLED"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-030",
                    "details": "HR_ONBOARD_BOT changed user U-030 status to DISABLED",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={"user_id": "U-030", "only_active": False},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-030", "role_id": "ROL-029", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-030",
                    "details": "Role ROL-029 removed from U-030",
                },
            ),
            Action(
                name="CreateHubspotTicket",
                kwargs={
                    "subject": "Offboard employee Aria Hill (ahill)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "devans",
                    "email": "Noah.Walker@sigmatech.com",
                    "department": "Finance",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-029",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-029 added to U-034",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "receiver": "Noah.Walker@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Noah, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@sigmatech.com",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-030",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_073",
        instruction=(
            "You are HR_ONBOARD_BOT. Marketing specialist Sophie Turner is leaving the company. "
            "You must offboard Sophie and onboard Carla Ramirez (Marketing) replicating all her active marketing roles. "
            "Return Carla's roles and Sophie's empty assignments."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Sophie", "last_name": "Turner"},
            ),
            Action(
                name="UpdateUser", kwargs={"user_id": "U-026", "status": "DISABLED"}
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "HR_ONBOARD_BOT changed user U-026 status to DISABLED",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={"user_id": "U-026", "only_active": False},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-026", "role_id": "ROL-006", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-006 removed from U-026",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-026", "role_id": "ROL-007", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-007 removed from U-026",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={"user_id": "U-026", "role_id": "ROL-010", "action": "REMOVE"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "Role ROL-010 removed from U-026",
                },
            ),
            Action(
                name="CreateHubspotTicket",
                kwargs={
                    "subject": "Offboard employee Sophie Turner (sturner)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "category": "OFFBOARDING",
                    "priority": "MEDIUM",
                    "status": "OPEN",
                    "requester_id": "U-032",
                    "assignee_id": "U-005",
                },
            ),
            Action(
                name="CreateUser",
                kwargs={
                    "actor_id": "U-032",
                    "username": "cramirez",
                    "email": "carla.ramirez@sigmatech.com",
                    "department": "Marketing",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_CREATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "HR_ONBOARD_BOT created new user account U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-006",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-006 added to U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-007",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-007 added to U-034",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-010",
                    "action": "ADD",
                    "assigned_by": "U-032",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-034",
                    "details": "Role ROL-010 added to U-034",
                },
            ),
            Action(
                name="SendEmail",
                kwargs={
                    "receiver": "carla.ramirez@sigmatech.com",
                    "subject": "Welcome to SigmaTech!",
                    "text_content": "Hi Carla, welcome to SigmaTech! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                    "sender": "onboarding@sigmatech.com",
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-034",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-026",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_074",
        instruction=(
            "You are engineering lead Mason Martinez. The engineering team needs a new API gateway resource for microservices management. "
            "You must create a new resource called 'api-gateway-microservices' with HIGH criticality and ISO-27001 compliance, owned by Noah Martinez. "
            "The resource needs: an associated role 'engineering-api-gateway-admin' with the description 'Manages API gateway configuration and routing for microservices'. "
            "and the permission 'configure-api-gateway' with the description: 'Configure routing and load balancing in API gateway' for the new role; give the role to Noah Martinez. "
            "Return the new resource, role, permission, and Noah's updated roles."
        ),
        actions=[
            Action(
                name="GetUser",
                kwargs={"first_name": "Mason", "last_name": "Martinez"},
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Noah", "last_name": "Thompson"},
            ),
            Action(
                name="CreateResource",
                kwargs={
                    "name": "api-gateway-microservices",
                    "owner_id": "U-019",
                    "criticality": "HIGH",
                    "compliance_scope": "ISO-27001",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "RESOURCE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "RES-043",
                    "details": "Resource RES-043 created by U-001",
                },
            ),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "engineering-api-gateway-admin",
                    "description": "Manages API gateway configuration and routing for microservices",
                    "is_temporary": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ROLE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-001",
                },
            ),
            Action(
                name="CreatePermission",
                kwargs={
                    "action": "configure-api-gateway",
                    "resource_id": "RES-043",
                    "description": "Configure routing and load balancing in API gateway",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-001",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-001",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={
                    "role_id": "ROL-043",
                    "permission_id": "P-113",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Permission P-113 assigned to role ROL-043.",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-019",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-001",
                    "target_id": "U-019",
                    "details": "Role ROL-043 added to U-019",
                },
            ),
            Action(
                name="GetResource",
                kwargs={"resource_id": "RES-043"},
            ),
            Action(
                name="GetRole",
                kwargs={"role_id": "ROL-043"},
            ),
            Action(
                name="GetPermission",
                kwargs={"permission_id": "P-113"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-019",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_075",
        instruction=(
            "You are engineering lead Mason Martinez. The sales team needs a new customer support ticketing system for better customer service management. "
            "You must create a new resource called 'customer-support-portal' with MEDIUM criticality and GDPR compliance, owned by Alexander Clark from Sales. "
            "This resource needs: an associated role 'support-ticket-manager' for managing customer support tickets with the description 'Manages customer support tickets and escalations' "
            "and a permission 'manage-support-tickets' with the description: 'Create, update, and resolve customer support tickets' for the new role; give the role to Alexander Clark. "
            "Return the new resource, role, permission, and Alexander's updated roles."
        ),
        actions=[
            Action(
                name="GetUser",
                kwargs={"first_name": "Mason", "last_name": "Martinez"},
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Alexander", "last_name": "Clark"},
            ),
            Action(
                name="CreateResource",
                kwargs={
                    "name": "customer-support-portal",
                    "owner_id": "U-009",
                    "criticality": "MEDIUM",
                    "compliance_scope": "GDPR",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "RESOURCE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "RES-043",
                    "details": "Resource RES-043 created by U-001",
                },
            ),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "support-ticket-manager",
                    "description": "Manages customer support tickets and escalations",
                    "is_temporary": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ROLE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-001",
                },
            ),
            Action(
                name="CreatePermission",
                kwargs={
                    "action": "manage-support-tickets",
                    "resource_id": "RES-043",
                    "description": "Create, update, and resolve customer support tickets",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-001",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-001",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={
                    "role_id": "ROL-043",
                    "permission_id": "P-113",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Permission P-113 assigned to role ROL-043.",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-009",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-001",
                    "target_id": "U-009",
                    "details": "Role ROL-043 added to U-009",
                },
            ),
            Action(
                name="CheckSodConflicts",
                kwargs={
                    "user_id": "U-009",
                },
            ),
            Action(
                name="GetResource",
                kwargs={"resource_id": "RES-043"},
            ),
            Action(
                name="GetRole",
                kwargs={"role_id": "ROL-043"},
            ),
            Action(
                name="GetPermission",
                kwargs={"permission_id": "P-113"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-009",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_076",
        instruction=(
            "You are engineering lead Mason Martinez. The engineering team needs a new code quality assurance tool for better code review processes. "
            "You must create a new resource called 'code-review-platform' with HIGH criticality and ISO-27001 compliance, owned by William Thompson from Engineering. "
            "This resource needs: an associated role 'engineering-code-reviewer' for reviewing code submissions with the description 'Reviews code submissions and enforces quality standards' "
            "and a permission 'approve-code-reviews' for the new role with the description: 'Approve or reject code review submissions'; give the role to William Thompson. "
            "Return the new resource, role, permission, and William's updated roles."
        ),
        actions=[
            Action(
                name="GetUser",
                kwargs={"first_name": "Mason", "last_name": "Martinez"},
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "William", "last_name": "Thompson"},
            ),
            Action(
                name="CreateResource",
                kwargs={
                    "name": "code-review-platform",
                    "owner_id": "U-007",
                    "criticality": "HIGH",
                    "compliance_scope": "ISO-27001",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "RESOURCE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "RES-043",
                    "details": "Resource RES-043 created by U-001",
                },
            ),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "engineering-code-reviewer",
                    "description": "Reviews code submissions and enforces quality standards",
                    "is_temporary": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ROLE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-001",
                },
            ),
            Action(
                name="CreatePermission",
                kwargs={
                    "action": "approve-code-reviews",
                    "resource_id": "RES-043",
                    "description": "Approve or reject code review submissions",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-001",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-001",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={
                    "role_id": "ROL-043",
                    "permission_id": "P-113",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Permission P-113 assigned to role ROL-043.",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-007",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-001",
                    "target_id": "U-007",
                    "details": "Role ROL-043 added to U-007",
                },
            ),
            Action(name="CheckSodConflicts", kwargs={"user_id": "U-007"}),
            Action(
                name="GetResource",
                kwargs={"resource_id": "RES-043"},
            ),
            Action(
                name="GetRole",
                kwargs={"role_id": "ROL-043"},
            ),
            Action(
                name="GetPermission",
                kwargs={"permission_id": "P-113"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-007",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_077",
        instruction=(
            "You are engineering lead Mason Martinez. The marketing team needs a new marketing automation platform for managing campaigns and workflows. "
            "You must create a new resource called 'marketing-automation-platform' with HIGH criticality and GDPR compliance, owned by Madison Martinez from Marketing. "
            "For that resource, you must create: an associated role 'marketing-automation-manager' for managing automated marketing with the description 'Manages automated marketing workflows and campaigns' "
            "and a permission 'configure-marketing-workflows' for the new role with the description: 'Create and modify automated marketing campaign workflows'; give the role to Madison Martinez. "
            "Return the new resource, role, permission, and Madison's updated roles."
        ),
        actions=[
            Action(
                name="GetUser",
                kwargs={"first_name": "Mason", "last_name": "Martinez"},
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Madison", "last_name": "Jackson"},
            ),
            Action(
                name="CreateResource",
                kwargs={
                    "name": "marketing-automation-platform",
                    "owner_id": "U-014",
                    "criticality": "HIGH",
                    "compliance_scope": "GDPR",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "RESOURCE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "RES-043",
                    "details": "Resource RES-043 created by U-001",
                },
            ),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "marketing-automation-manager",
                    "description": "Manages automated marketing workflows and campaigns",
                    "is_temporary": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ROLE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-001",
                },
            ),
            Action(
                name="CreatePermission",
                kwargs={
                    "action": "configure-marketing-workflows",
                    "resource_id": "RES-043",
                    "description": "Create and modify automated marketing campaign workflows",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-001",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-001",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={
                    "role_id": "ROL-043",
                    "permission_id": "P-113",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Permission P-113 assigned to role ROL-043.",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-001",
                    "target_id": "U-014",
                    "details": "Role ROL-043 added to U-014",
                },
            ),
            Action(name="CheckSodConflicts", kwargs={"user_id": "U-014"}),
            Action(
                name="GetResource",
                kwargs={"resource_id": "RES-043"},
            ),
            Action(
                name="GetRole",
                kwargs={"role_id": "ROL-043"},
            ),
            Action(
                name="GetPermission",
                kwargs={"permission_id": "P-113"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-014",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_078",
        instruction=(
            "You are engineering lead Mason Martinez. The finance team needs a new executive financial dashboard for sensitive financial reporting. "
            "You must create a new resource called 'executive-financial-dashboard' with CRITICAL criticality and SOX compliance, owned by Olivia Lee from Finance. "
            "The resource needs: an associated role 'finance-executive-reporting' with the description 'Access to executive-level financial reports and dashboards'. "
            "and a permission 'view-executive-financials' for the new role with the description: 'View executive financial dashboards and sensitive reports'; give the role to Olivia Lee. "
            "Return the new resource, role, permission, and Olivia's updated roles."
        ),
        actions=[
            Action(
                name="GetUser",
                kwargs={"first_name": "Mason", "last_name": "Martinez"},
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Olivia", "last_name": "Lee"},
            ),
            Action(
                name="CreateResource",
                kwargs={
                    "name": "executive-financial-dashboard",
                    "owner_id": "U-006",
                    "criticality": "CRITICAL",
                    "compliance_scope": "SOX",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "RESOURCE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "RES-043",
                    "details": "Resource RES-043 created by U-001",
                },
            ),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "finance-executive-reporting",
                    "description": "Access to executive-level financial reports and dashboards",
                    "is_temporary": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "ROLE_CREATED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-001",
                },
            ),
            Action(
                name="CreatePermission",
                kwargs={
                    "action": "view-executive-financials",
                    "resource_id": "RES-043",
                    "description": "View executive financial dashboards and sensitive reports",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_CREATED",
                    "actor_id": "U-001",
                    "target_id": "P-113",
                    "details": "Permission P-113 created by U-001",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={
                    "role_id": "ROL-043",
                    "permission_id": "P-113",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "PERMISSION_ASSIGNED",
                    "actor_id": "U-001",
                    "target_id": "ROL-043",
                    "details": "Permission P-113 assigned to role ROL-043.",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-006",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-001",
                    "target_id": "U-006",
                    "details": "Role ROL-043 added to U-006",
                },
            ),
            Action(name="CheckSodConflicts", kwargs={"user_id": "U-006"}),
            Action(
                name="GetResource",
                kwargs={"resource_id": "RES-043"},
            ),
            Action(
                name="GetRole",
                kwargs={"role_id": "ROL-043"},
            ),
            Action(
                name="GetPermission",
                kwargs={"permission_id": "P-113"},
            ),
            Action(
                name="GetUserRoles",
                kwargs={
                    "user_id": "U-006",
                    "only_active": True,
                    "include_role_details": True,
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_079",
        instruction=(
            "You are RBAC_BOT. Operations engineer Oliver Lewis needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD September 18th, 2025). "
            "Oliver claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Mason Martinez as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Oliver", "last_name": "Lewis"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Mason", "last_name": "Martinez"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-001", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-029",
                    "permission_id": "P-084",
                    "reviewed_by": "U-001",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-09-18",
                    "expires_on": "2025-09-18T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_080",  # Too simple??
        instruction=(
            "You are Noah Thompson, Operations Lead. "
            "A new third-party vendor integration requires creating a service account 'VENDOR_INTEGRATION_BOT' in the Operations department with the email 'vendor-integration@sigmatech.com'. "
            "You must create this account, it should have a new 'vendor-api-access' role with 'Limited access for third-party vendor integration to API gateway' role with the permission with the action 'read-api'."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-005"}),
            Action(
                name="CreateUser",
                kwargs={
                    "username": "VENDOR_INTEGRATION_BOT",
                    "email": "vendor-integration@sigmatech.com",
                    "department": "Operations",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "User VENDOR_INTEGRATION_BOT created by U-005.",
                },
            ),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "vendor-api-access",
                    "description": "Limited access for third-party vendor integration to API gateway",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-005.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "read-api"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-010"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-010 assigned to role ROL-043.",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-005",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-034",
                    "details": "Role ROL-043 added to U-034",
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-034"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_081",
        instruction=(
            "You are Operations Lead Noah Thompson. "
            "A new marketing automation vendor requires creating a service account 'MARKETING_AUTOMATION_BOT' in the Marketing department with the email 'marketing-automation@sigmatech.com', you must create this account. "
            "The account should have a new 'vendor-marketing-automation' role with 'Limited access for marketing automation vendor to manage campaigns' description with the permission with the action 'send-email-campaign'."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-005"}),
            Action(
                name="CreateUser",
                kwargs={
                    "username": "MARKETING_AUTOMATION_BOT",
                    "email": "marketing-automation@sigmatech.com",
                    "department": "Marketing",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "User MARKETING_AUTOMATION_BOT created by U-005.",
                },
            ),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "vendor-marketing-automation",
                    "description": "Limited access for marketing automation vendor to manage campaigns",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-005.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "send-email-campaign"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-022"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-022 assigned to role ROL-043.",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-005",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-034",
                    "details": "Role ROL-043 added to U-034",
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-034"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_082",
        instruction=(
            "You are Finance Lead Olivia Lee. "
            "A new payment processing vendor requires creating a service account 'PAYMENT_PROCESSOR_BOT' in the Finance department with the email 'payment-processor@sigmatech.com', you must create this account. "
            "The account should have a new 'vendor-payment-processing' role with 'Limited access for payment processing vendor to handle invoices' description with the permission with the action 'view-payments'."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Lee"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-006"}),
            Action(
                name="CreateUser",
                kwargs={
                    "username": "PAYMENT_PROCESSOR_BOT",
                    "email": "payment-processor@sigmatech.com",
                    "department": "Finance",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "User PAYMENT_PROCESSOR_BOT created by U-006.",
                },
            ),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "vendor-payment-processing",
                    "description": "Limited access for payment processing vendor to handle invoices",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-006.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "view-payments"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-079"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-079 assigned to role ROL-043.",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-006",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-034",
                    "details": "Role ROL-043 added to U-034",
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-034"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_083",
        instruction=(
            "You are Sales Lead Noah Martinez. "
            "A new CRM analytics vendor requires creating a service account 'CRM_ANALYTICS_BOT' in the Sales department with the email 'crm-analytics@sigmatech.com', you must create this account. "
            "The account should have a new 'vendor-crm-analytics' role with 'Limited access for CRM analytics vendor to read customer data' description with the permission with the action 'read-crm-customer'."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Johnson"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-003"}),
            Action(
                name="CreateUser",
                kwargs={
                    "username": "CRM_ANALYTICS_BOT",
                    "email": "crm-analytics@sigmatech.com",
                    "department": "Sales",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-003",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "User CRM_ANALYTICS_BOT created by U-003.",
                },
            ),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "vendor-crm-analytics",
                    "description": "Limited access for CRM analytics vendor to read customer data",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-003",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-003.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "read-crm-customer"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-035"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-003",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-035 assigned to role ROL-043.",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-003",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-003",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-034",
                    "details": "Role ROL-043 added to U-034",
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-034"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_084",
        instruction=(
            "You are Operations manager Noah Thompson. "
            "A new recruitment automation vendor requires creating a service account 'RECRUITMENT_AUTOMATION_BOT' in the Human Resources department with the email 'recruitment-automation@sigmatech.com'. "
            "You must create this account, it should have a new 'vendor-recruitment-automation' role with 'Limited access for recruitment vendor to manage job postings' description with the permission with the action 'create-job-posting'."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-005"}),
            Action(
                name="CreateUser",
                kwargs={
                    "username": "RECRUITMENT_AUTOMATION_BOT",
                    "email": "recruitment-automation@sigmatech.com",
                    "department": "Human Resources",
                    "status": "ACTIVE",
                    "mfa_enabled": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "details": "User RECRUITMENT_AUTOMATION_BOT created by U-005.",
                },
            ),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "vendor-recruitment-automation",
                    "description": "Limited access for recruitment vendor to manage job postings",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-005.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "create-job-posting"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-053"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-053 assigned to role ROL-043.",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-034",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-005",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-034",
                    "details": "Role ROL-043 added to U-034",
                },
            ),
            Action(name="GetUser", kwargs={"user_id": "U-034"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_085",
        instruction=(
            "You are Olivia Lee, Finance Lead. "
            "The annual budget planning project requires temporary collaboration between Finance and Sales teams. "
            "You need to create a temporary role 'budget-planning-reviewer' with description 'Temporary cross-department role for budget planning collaboration' "
            "with the permissions view-financial-report and generate-sales-report. "
            "Noah Martinez and Madison Martinez need the role expiring EOD September 7th, 2025."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Lee"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-006"}),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "budget-planning-reviewer",
                    "description": "Temporary cross-department role for budget planning collaboration",
                    "is_temporary": True,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-006.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "view-financial-report"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-085"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-085 assigned to role ROL-043.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "generate-sales-report"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-039"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-039 assigned to role ROL-043.",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Johnson"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-003",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-006",
                    "expires_on": "2025-09-07T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-003",
                    "details": "Role ROL-043 added to U-003",
                },
            ),
            Action(
                name="GetUserRoles", kwargs={"user_id": "U-003"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Madison", "last_name": "Johnson"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-006",
                    "expires_on": "2025-09-07T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-014",
                    "details": "Role ROL-043 added to U-014",
                },
            ),
            Action(
                name="GetUserRoles", kwargs={"user_id": "U-014"}
            ),
            Action(name="GetRole", kwargs={"role_id": "ROL-043"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_086",
        instruction=(
            "You are Mason Martinez, Engineering Lead. "
            "A new microservices deployment requires temporary collaboration between Engineering and Operations. "
            "Create a temporary role 'microservices-deployment-reviewer' with description 'Temporary cross-department role for microservices deployment' "
            "with permissions configure-pipeline and modify-firewall-rules. "
            "Noah Martinez and Jacob Allen need the role, expiring EOD September 15th, 2025."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Mason", "last_name": "Martinez"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-001"}),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "microservices-deployment-reviewer",
                    "description": "Temporary cross-department role for microservices deployment",
                    "is_temporary": True,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-001.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "configure-pipeline"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-005"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-005 assigned to role ROL-043.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "modify-firewall-rules"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-067"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-067 assigned to role ROL-043.",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-019",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                    "expires_on": "2025-09-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-019",
                    "details": "Role ROL-043 added to U-019",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Jacob", "last_name": "Allen"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-023",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-001",
                    "expires_on": "2025-09-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-023",
                    "details": "Role ROL-043 added to U-023",
                },
            ),
            Action(name="GetRole", kwargs={"role_id": "ROL-043"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_087",
        instruction=(
            "You are Noah Thompson, Operations Lead. "
            "A quarterly audit requires temporary access for Finance and Operations to review backup storage. "
            "Create a temporary role 'backup-audit-reviewer' with description 'Temporary role for quarterly backup audit' "
            "with permissions restore-backup and upload-backup. "
            "Olivia Lee and Oliver Lewis need the role, expiring EOD September 30th, 2025."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-005"}),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "backup-audit-reviewer",
                    "description": "Temporary role for quarterly backup audit",
                    "is_temporary": True,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-005.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "restore-backup"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-069"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-069 assigned to role ROL-043.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "upload-backup"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-068"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-068 assigned to role ROL-043.",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Lee"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-006",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-005",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-006",
                    "details": "Role ROL-043 added to U-006",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Oliver", "last_name": "Lewis"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-005",
                    "expires_on": "2025-09-30T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-029",
                    "details": "Role ROL-043 added to U-029",
                },
            ),
            Action(name="GetRole", kwargs={"role_id": "ROL-043"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_088",  # Too simple?
        instruction=(
            "You are Sophia Thompson, Marketing Lead. "
            "A cross-department campaign launch requires temporary collaboration between Marketing and Sales. "
            "Create a temporary role 'campaign-launch-reviewer' with description 'Temporary role for campaign launch collaboration' "
            "with permissions post-social-media and generate-sales-report. "
            "Sophie Turner and Logan Scott need the role, expiring EOD October 1st, 2025."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Thompson"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-002"}),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "campaign-launch-reviewer",
                    "description": "Temporary role for campaign launch collaboration",
                    "is_temporary": True,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-002.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "post-social-media"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-019"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-019 assigned to role ROL-043.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "generate-sales-report"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-039"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-039 assigned to role ROL-043.",
                },
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "Sophie", "last_name": "Turner"},
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-002",
                    "expires_on": "2025-10-01T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-026",
                    "details": "Role ROL-043 added to U-026",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Logan", "last_name": "Scott"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-021",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-002",
                    "expires_on": "2025-10-01T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-021",
                    "details": "Role ROL-043 added to U-021",
                },
            ),
            Action(name="GetRole", kwargs={"role_id": "ROL-043"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_089",
        instruction=(
            "You are Sophia Thompson, HR Lead. "
            "A compliance review requires temporary access for HR and Finance to the benefits administration system. "
            "Create a temporary role 'benefits-compliance-reviewer' with description 'Temporary role for benefits compliance review' "
            "with permissions enroll-in-benefits and view-onboarding-docs. "
            "Grace Young (HR) and Victoria Lee (Finance) need the role, expiring EOD October 15th, 2025."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Thompson"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-004"}),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "benefits-compliance-reviewer",
                    "description": "Temporary role for benefits compliance review",
                    "is_temporary": True,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-004",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-004.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "enroll-in-benefits"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-056"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-004",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-056 assigned to role ROL-043.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "view-onboarding-docs"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-058"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-004",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-058 assigned to role ROL-043.",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Grace", "last_name": "Young"}
            ),
            Action(
                name="CheckSodConflicts",
                kwargs={"user_id": "U-022", "role_id": "ROL-043"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-022",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-004",
                    "expires_on": "2025-10-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-004",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-022",
                    "details": "Role ROL-043 added to U-022",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Victoria", "last_name": "Lee"}
            ),
            Action(
                name="CheckSodConflicts",
                kwargs={"user_id": "U-012", "role_id": "ROL-043"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-012",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-004",
                    "expires_on": "2025-10-15T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-004",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-012",
                    "details": "Role ROL-043 added to U-012",
                },
            ),
            Action(name="GetRole", kwargs={"role_id": "ROL-043"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_090",
        instruction=(
            "You are Olivia Lee, Finance Lead. "
            "A special project requires temporary collaboration between Finance and Marketing to analyze quarterly financial reports and marketing analytics. "
            "Create a temporary role 'finance-marketing-analyst' with description 'Temporary cross-department role for financial and marketing analysis' "
            "with permissions view-financial-report and view-marketing-dashboard. "
            "Chloe Scott and Madison Martinez need the role until EOD October 31st, 2025."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Lee"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-006"}),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "finance-marketing-analyst",
                    "description": "Temporary cross-department role for financial and marketing analysis",
                    "is_temporary": True,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-006.",
                },
            ),
            Action(name="GetPermission", kwargs={"action": "view-financial-report"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-085"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-085 assigned to role ROL-043.",
                },
            ),
            Action(
                name="GetPermission", kwargs={"action": "view-marketing-dashboard"}
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-025"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-025 assigned to role ROL-043.",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Chloe", "last_name": "Scott"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-024",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-006",
                    "expires_on": "2025-10-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-024",
                    "details": "Role ROL-043 added to U-024",
                },
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Madison", "last_name": "Johnson"}
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-006",
                    "expires_on": "2025-10-31T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-014",
                    "details": "Role ROL-043 added to U-014",
                },
            ),
            Action(name="GetRole", kwargs={"role_id": "ROL-043"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_091",
        instruction=(
            "You are Sophia Thompson, Marketing Lead. Due to organizational changes, the 'marketing-analytics-read' and 'marketing-content-editor' roles "
            "are being consolidated into a single 'marketing-content-analyst' role with the description 'Consolidated role for marketing analytics and content editing'. "
            "Migrate all active users and permissions from both old roles to the new one. "
            "Then mark the old roles as 'Deprecated' in their description."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Thompson"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-002"}),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "marketing-content-analyst",
                    "description": "Consolidated role for marketing analytics and content editing",
                    "is_temporary": False,
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "details": "Role ROL-043 created by U-002.",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "marketing-analytics-read"}),
            Action(name="GetRole", kwargs={"role_name": "marketing-content-editor"}),
            Action(
                name="GetRolePermissions",
                kwargs={"role_id": "ROL-009", "include_permission": True},
            ),
            Action(
                name="GetRolePermissions",
                kwargs={"role_id": "ROL-010", "include_permission": True},
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-025"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-025 assigned to role ROL-043.",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-026"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-026 assigned to role ROL-043.",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-030"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-030 assigned to role ROL-043.",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-031"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-031 assigned to role ROL-043.",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-032"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-032 assigned to role ROL-043.",
                },
            ),
            Action(name="GetUser", kwargs={"role_id": "ROL-009", "status": "ACTIVE"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-009",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-014",
                    "details": "Role ROL-009 removed from U-014",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-014",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-002",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-014",
                    "details": "Role ROL-043 added to U-014",
                },
            ),
            Action(name="GetUser", kwargs={"role_id": "ROL-010", "status": "ACTIVE"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-010",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-026",
                    "details": "Role ROL-010 removed from U-026",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-002",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-026",
                    "details": "Role ROL-043 added to U-026",
                },
            ),
            Action(
                name="UpdateRole",
                kwargs={"role_id": "ROL-009", "description": "Deprecated"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_DEPRECATED",
                    "target_id": "ROL-009",
                    "details": "Role ROL-009 marked as deprecated by U-002.",
                },
            ),
            Action(
                name="UpdateRole",
                kwargs={"role_id": "ROL-010", "description": "Deprecated"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_DEPRECATED",
                    "target_id": "ROL-010",
                    "details": "Role ROL-010 marked as deprecated by U-002.",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_092",
        instruction=(
            "You are Olivia Lee, Finance Lead. The 'finance-read' and 'finance-invoice-processor' roles are being consolidated into a single 'finance-data-analyst' role with the description 'Consolidated role for finance data analysis and invoice processing'. "
            "Migrate all active users and permissions from both old roles to the new one. Then mark the old roles as 'Deprecated' in their description."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Lee"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-006"}),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "finance-data-analyst",
                    "description": "Consolidated role for finance data analysis and invoice processing",
                    "is_temporary": False,
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "finance-read"}),
            Action(name="GetRole", kwargs={"role_name": "finance-invoice-processor"}),
            Action(name="GetRolePermissions", kwargs={"role_id": "ROL-030"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-075"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-075 assigned to role ROL-043.",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-083"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-083 assigned to role ROL-043.",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-085"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-085 assigned to role ROL-043.",
                },
            ),
            Action(name="GetRolePermissions", kwargs={"role_id": "ROL-031"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-077"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-077 assigned to role ROL-043.",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-078"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-078 assigned to role ROL-043.",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-079"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-079 assigned to role ROL-043.",
                },
            ),
            Action(name="GetUser", kwargs={"role_id": "ROL-030", "status": "ACTIVE"}),
            Action(name="GetUser", kwargs={"role_id": "ROL-031", "status": "ACTIVE"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-012",
                    "role_id": "ROL-031",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-012",
                    "details": "Role ROL-031 removed from U-012",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-012",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-006",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-012",
                    "details": "Role ROL-043 added to U-012",
                },
            ),
            Action(
                name="UpdateRole",
                kwargs={
                    "role_id": "ROL-030",
                    "description": "Deprecated",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ROLE_DEPRECATED",
                    "target_id": "ROL-030",
                    "details": "Role ROL-030 marked as deprecated by U-006.",
                },
            ),
            Action(
                name="UpdateRole",
                kwargs={
                    "role_id": "ROL-031",
                    "description": "Deprecated",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ROLE_DEPRECATED",
                    "target_id": "ROL-031",
                    "details": "Role ROL-031 marked as deprecated by U-006.",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_093",
        instruction=(
            "You are Sophia Thompson, Marketing Lead. The 'marketing-campaign-manager' and 'marketing-social-media' roles are being consolidated into a single 'marketing-campaign-analyst' role "
            "with the description 'Consolidated role for campaign management and social media oversight'. "
            "Migrate all active users and permissions from both old roles to the new one. Then mark the old roles as 'Deprecated' in their description."
        ),
        actions=[
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Thompson"}
            ),
            Action(name="IsAdmin", kwargs={"user_id": "U-002"}),
            Action(
                name="CreateRole",
                kwargs={
                    "role_name": "marketing-campaign-analyst",
                    "description": "Consolidated role for campaign management and social media oversight",
                    "is_temporary": False,
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "marketing-campaign-manager"}),
            Action(name="GetRolePermissions", kwargs={"role_id": "ROL-007"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-022"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-022 assigned to role ROL-043.",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-024"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-024 assigned to role ROL-043.",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-029"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-029 assigned to role ROL-043.",
                },
            ),
            Action(name="GetRole", kwargs={"role_name": "marketing-social-media"}),
            Action(name="GetRolePermissions", kwargs={"role_id": "ROL-008"}),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-019"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-019 assigned to role ROL-043.",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-020"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-020 assigned to role ROL-043.",
                },
            ),
            Action(
                name="AssignPermissionToRole",
                kwargs={"role_id": "ROL-043", "permission_id": "P-021"},
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "details": "Permission P-021 assigned to role ROL-043.",
                },
            ),
            Action(name="GetUser", kwargs={"role_id": "ROL-007", "status": "ACTIVE"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-007",
                    "action": "REMOVE",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-026",
                    "details": "Role ROL-007 removed from U-026",
                },
            ),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-043",
                    "action": "ADD",
                    "assigned_by": "U-002",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_ROLES_UPDATED",
                    "target_id": "U-026",
                    "details": "Role ROL-043 added to U-026",
                },
            ),
            Action(name="GetUser", kwargs={"role_id": "ROL-008", "status": "ACTIVE"}),
            Action(
                name="UpdateRole",
                kwargs={
                    "role_id": "ROL-007",
                    "description": "Deprecated",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_DEPRECATED",
                    "target_id": "ROL-007",
                    "details": "Role ROL-007 marked as deprecated by U-002.",
                },
            ),
            Action(
                name="UpdateRole",
                kwargs={
                    "role_id": "ROL-008",
                    "description": "Deprecated",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_DEPRECATED",
                    "target_id": "ROL-008",
                    "details": "Role ROL-008 marked as deprecated by U-002.",
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_094",
        instruction=(
            "You are RBAC_BOT. Engineer Nathan Thompson needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD September 22nd, 2025). "
            "Nathan claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Sophia Thompson as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Nathan", "last_name": "Thompson"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Thompson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-002", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-013",
                    "permission_id": "P-084",
                    "reviewed_by": "U-002",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-09-22",
                    "expires_on": "2025-09-22T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_095",
        instruction=(
            "You are RBAC_BOT. Engineer William Thompson needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 3rd, 2025). "
            "William claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Noah Thompson as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser",
                kwargs={"first_name": "William", "last_name": "Thompson"},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Noah", "last_name": "Thompson"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-005", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-007",
                    "permission_id": "P-084",
                    "reviewed_by": "U-005",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-03",
                    "expires_on": "2025-10-03T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_096",
        instruction=(
            "You are RBAC_BOT. Sales analyst Logan Scott needs a time-bound policy exception to submit a tax filing in the tax compliance software for quarter close (EOD October 12th, 2025). "
            "Logan claims the reason for the request is 'quarter-close filing requires elevated permission' and needs the 'submit-tax-filing' permission. "
            "You must create the exception and assign Olivia Lee as the reviewer."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "RBAC_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-031", "include_role_details": True},
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Logan", "last_name": "Scott"}
            ),
            Action(
                name="GetUser", kwargs={"first_name": "Olivia", "last_name": "Lee"}
            ),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-006", "include_role_details": True},
            ),
            Action(name="GetPermission", kwargs={"action": "submit-tax-filing"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-021",
                    "permission_id": "P-084",
                    "reviewed_by": "U-006",
                    "reason": "Temporary access to perform submit-tax-filing until 2025-10-12",
                    "expires_on": "2025-10-12T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-031",
                    "target_id": "PE-021",
                    "details": "RBAC_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-031",
                },
            ),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_097",
        instruction=(
            "You are HR_ONBOARD_BOT. Sales rep Alexander Clark is changing his last name to Lucero and will be on paternity leave until EOD November 1st, 2025. "
            "You must update his profile to reflect the new last name and set his account to inactive during the leave. "
            "While Alexander is on leave, Ethan Johnson will handle quote approvals. "
            "Ethan needs the 'sales-commission-view' role."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(
                name="IsAdmin",
                kwargs={"user_id": "U-032", "include_role_details": True},
            ),
            Action(name="GetUser", kwargs={"first_name": "Alexander", "last_name": "Clark"}),
            Action(name="GetUser", kwargs={"username": "mlucero", "allow_missing": True}),
            Action(name="UpdateUser", kwargs={"user_id": "U-009", "last_name": "Lucero"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-009",
                    "details": "U-032 updated user U-009 name to Alexander Lucero; username set to mlucero; email set to Alexander.lucero@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#sales",
                    "message": "User U-009 updated by U-032: username aclark -> mlucero; email set to Alexander.lucero@sigmatech.com; name set to Alexander Lucero.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="UpdateUser", kwargs={"user_id": "U-009", "status": "INACTIVE"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-009",
                    "details": "HR_ONBOARD_BOT changed user U-009 status to INACTIVE",
                },
            ),
            Action(name="GetUser", kwargs={"first_name": "Ethan", "last_name": "Johnson"}),
            Action(name="GetUserRoles", kwargs={"user_id": "U-015", "only_active": True}),
            Action(name="GetRole", kwargs={"role_name": "sales-commission-view"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-015",
                    "role_id": "ROL-015",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-11-01T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-015",
                    "details": "Role ROL-015 added to U-015",
                },
            ),
            Action(name="GetUser", kwargs={"username": "mlucero"}),
            Action(name="GetUserRoles", kwargs={"user_id": "U-015", "only_active": True}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_098",
        instruction=(
            "You are HR_ONBOARD_BOT. HR specialist Grace Young is changing her first name to Riley and is taking leave until EOD September 5th, 2025. "
            "Update her profile and set her account to inactive during leave. "
            "While Riley is on leave, assign teammate Ava Martinez the temporary 'hr-employee-data-read' role."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="IsAdmin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="GetUser", kwargs={"first_name": "Grace", "last_name": "Young"}),
            Action(name="GetUser", kwargs={"username": "rking", "allow_missing": True}),
            Action(name="UpdateUser", kwargs={"user_id": "U-022", "first_name": "Riley"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-022",
                    "details": "U-032 updated user U-022 name to Riley Young; username set to rking; email set to riley.Young@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#human-resources",
                    "message": "User U-022 updated by U-032: username gyoung -> rking; email set to riley.Young@sigmatech.com; name set to Riley Young.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="UpdateUser", kwargs={"user_id": "U-022", "status": "INACTIVE"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-022",
                    "details": "HR_ONBOARD_BOT changed user U-022 status to INACTIVE",
                },
            ),
            Action(name="GetUser", kwargs={"first_name": "Ava", "last_name": "Martinez"}),
            Action(name="GetUserRoles", kwargs={"user_id": "U-016", "only_active": True}),
            Action(name="GetRole", kwargs={"role_name": "hr-employee-data-read"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-016",
                    "role_id": "ROL-017",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-09-05T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-016",
                    "details": "Role ROL-017 added to U-016",
                },
            ),
            Action(name="GetUser", kwargs={"username": "rking"}),
            Action(name="GetUserRoles", kwargs={"user_id": "U-016", "only_active": True}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_099",
        instruction=(
            "You are HR_ONBOARD_BOT. Operations analyst Lucas Thompson is changing his last name to Wyatt and is taking leave until EOD October 10th, 2025. "
            "Update his profile and set his account to inactive during the leave. "
            "During Lucas's absence, assign a temporary 'operations-incident-response' role to Oliver Lewis."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="IsAdmin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="GetUser", kwargs={"first_name": "Lucas", "last_name": "Thompson"}),
            Action(name="GetUser", kwargs={"username": "rwyatt", "allow_missing": True}),
            Action(name="UpdateUser", kwargs={"user_id": "U-017", "last_name": "Wyatt"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-017",
                    "details": "U-032 updated user U-017 name to Lucas Wyatt; username set to rwyatt; email set to Lucas.wyatt@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#operations",
                    "message": "User U-017 updated by U-032: username lthompson -> rwyatt; email set to Lucas.wyatt@sigmatech.com; name set to Lucas Wyatt.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="UpdateUser", kwargs={"user_id": "U-017", "status": "INACTIVE"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-017",
                    "details": "HR_ONBOARD_BOT changed user U-017 status to INACTIVE",
                },
            ),
            Action(name="GetUser", kwargs={"first_name": "Oliver", "last_name": "Lewis"}),
            Action(name="GetUserRoles", kwargs={"user_id": "U-029", "only_active": True}),
            Action(name="GetRole", kwargs={"role_name": "operations-incident-response"}),
            Action(
                name="UpdateUserRole",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-023",
                    "action": "ADD",
                    "assigned_by": "U-032",
                    "expires_on": "2025-10-10T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_ROLES_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-029",
                    "details": "Role ROL-023 added to U-029",
                },
            ),
            Action(name="GetUser", kwargs={"username": "rwyatt"}),
            Action(name="GetUserRoles", kwargs={"user_id": "U-029", "only_active": True, "include_role_details": True}),
        ],
        outputs=[]
    ),
    Task(
        annotator="liam",
        user_id="liam_100",
        instruction=(
            "You are HR_ONBOARD_BOT. Marketing specialist Sophie Turner is changing her last name to Phelps and is taking leave until EOD October 20th, 2025. "
            "Update her profile and set her account to inactive during leave. "
            "While Sophie is on leave, create a time-bound policy exception for Sales teammate Alexander Clark to temporarily 'search-logs' "
            "until EOD October 20th, 2025, to be reviewed by Marketing lead Sophia Rodriguez."
        ),
        actions=[
            Action(name="GetUser", kwargs={"username": "HR_ONBOARD_BOT"}),
            Action(name="IsAdmin", kwargs={"user_id": "U-032", "include_role_details": True}),
            Action(name="GetUser", kwargs={"first_name": "Sophie", "last_name": "Turner"}),
            Action(name="GetUser", kwargs={"username": "aphelps", "allow_missing": True}),
            Action(name="UpdateUser", kwargs={"user_id": "U-026", "last_name": "Phelps"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_UPDATED",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "U-032 updated user U-026 name to Sophie Phelps; username set to aphelps; email set to Sophie.phelps@sigmatech.com",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#marketing",
                    "message": "User U-026 updated by U-032: username sturner -> aphelps; email set to Sophie.phelps@sigmatech.com; name set to Sophie Phelps.",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="UpdateUser", kwargs={"user_id": "U-026", "status": "INACTIVE"}),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "USER_STATUS_CHANGE",
                    "actor_id": "U-032",
                    "target_id": "U-026",
                    "details": "HR_ONBOARD_BOT changed user U-026 status to INACTIVE",
                },
            ),
            Action(name="GetUser", kwargs={"first_name": "Alexander", "last_name": "Clark"}),
            Action(name="GetUser", kwargs={"first_name": "Sophia", "last_name": "Rodriguez"}),
            Action(name="IsAdmin", kwargs={"user_id": "U-002", "include_role_details": True}),
            Action(name="GetPermission", kwargs={"action": "search-logs"}),
            Action(
                name="CreatePolicyException",
                kwargs={
                    "user_id": "U-009",
                    "permission_id": "P-071",
                    "reviewed_by": "U-002",
                    "reason": "Temporary access to perform search-logs until 2025-10-20",
                    "expires_on": "2025-10-20T23:59:59.000000Z",
                },
            ),
            Action(
                name="CreateAuditLogEntry",
                kwargs={
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "actor_id": "U-032",
                    "target_id": "PE-021",
                    "details": "HR_ONBOARD_BOT created exception request PE-021",
                },
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#policy-exceptions",
                    "message": "Exception PE-021 created by U-032",
                    "username": "HR_ONBOARD_BOT",
                },
            ),
            Action(name="GetUser", kwargs={"username": "aphelps"}),
            Action(name="GetPolicyException", kwargs={"exception_id": "PE-021"}),
        ],
        outputs=[]
    ),
]
