# Copyright Sierra

tasks = [
    {
        "annotator": 1,
        "user_id": "task_001",
        "instruction": "As Emma Martinez from Human Resources, your task is to onboard Olivia Martin as a contractor in the Finance department. They need the 'finance-read' and 'finance-invoice-processor' roles, with access set to expire in 90 days. Approval for the new user will come from the finance lead.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Emma",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateUser",
                "arguments": {
                    "username": "jmitchell",
                    "email": "Olivia.Martin@sigmatech.com",
                    "department": "Finance",
                    "status": "PENDING_ACCESS"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "jmitchell"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-base"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-read"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-invoice-processor"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-034",
                    "role_id": "ROL-029",
                    "assigned_by": "U-010",
                    "expires_on": "2025-11-06T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-029 added to user U-034."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-034",
                    "role_id": "ROL-030",
                    "assigned_by": "U-010",
                    "expires_on": "2025-11-06T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-030 added to user U-034."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-034",
                    "role_id": "ROL-031",
                    "assigned_by": "U-010",
                    "expires_on": "2025-11-06T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-031 added to user U-034."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-034"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-034 created by user U-010."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "finance-lead"
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-034",
                    "status": "ACTIVE"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-006",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-034 status changed to 'ACTIVE' by user U-006."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-034\", \"status\": \"ACTIVE\"",
                "\"roles\": [\"finance-base\", \"finance-read\", \"finance-invoice-processor\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_002",
        "instruction": "Being Noah Thompson, the Operations Lead, you have been informed about the termination of Sophia Rodriguez. It is essential to conduct their offboarding immediately to protect company assets.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Rodriguez"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Rodriguez"
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-002",
                    "status": "DISABLED"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-002"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-base"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-lead"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-002",
                    "role_id": "ROL-006"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-006 removed from user U-002."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-002",
                    "role_id": "ROL-035"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-035 removed from user U-002."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-002"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-002 status changed to 'DISABLED' by user U-005."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "marketing-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Offboard employee Sophia Rodriguez (edavis)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "requester_id": "U-005",
                    "category": "Offboarding",
                    "assignee_id": "U-005"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-002\", \"status\": \"DISABLED\"",
                "\"roles\": []",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_003",
        "instruction": "From your position in the Operations team, as Oliver Lewis, assist employee Charlotte Walker who is locked out of their account due to too many unsuccessful login attempts. Address this issue on their behalf.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Lewis"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "cwalker"
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-020",
                    "status": "ACTIVE"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "cwalker"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "charlotte.walker@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Account Reactivated",
                    "text_content": "Your account has been reactivated and your access has been restored."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "charlotte.walker@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Account reactivated",
                    "text_content": "Please reset your password using the following link..."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-020",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-020 status changed to 'ACTIVE' by user U-029."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-020\", \"status\": \"ACTIVE\"",
                "\"email_id\": \"EM-016\"",
                "\"email_id\": \"EM-017\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_004",
        "instruction": "As the Operations Lead, Noah Thompson, you received notification of William Thompson's promotion to Engineering Lead. It is necessary to assign him the corresponding 'engineering-lead' role.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "wthompson"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-lead"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-007"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-034",
                    "assigned_by": "U-005"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-034 added to user U-007."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-007",
                    "role_name": "engineering-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-001 removed from user U-007."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-007",
                    "role_name": "engineering-code-commit"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-002"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-002 removed from user U-007."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-007",
                    "role_name": "engineering-prod-access"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-003 removed from user U-007."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-007"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-007\"",
                "\"roles\": [\"engineering-lead\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_005",
        "instruction": "In your dual role as the Operations Lead and compliance officer, Noah Thompson, you are tasked with initiating the quarterly access review for the 'production-web-server-1' resource. Proceed with this certification process.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "production-web-server-1"
                },
            },
            {
                "name": "CreateCertification",
                "arguments": {
                    "reviewer_id": "U-005",
                    "resource_id": "RES-025",
                    "due_date": "2025-09-08T09:56:15Z"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "username": "CERTIFICATION_BOT",
                    "channel": "#certifications",
                    "message": "A new certification C-024 for resources RES-025 has been requested. Due date 2025-09-08T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "CERTIFICATION_CREATED",
                    "target_id": "C-024",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Certification C-024 requested by user U-005"
                }
            }
        ],
        "outputs": [
                "\"certification_id\": \"C-024\", \"status\": \"PENDING\"",
                "\"message_id\": \"SL-042\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_006",
        "instruction": "Acting as Noah Thompson, a SOC analyst addressing a crucial incident, grant Oliver Lewis, an operations team member, emergency administrative access to the 'database-cluster-primary' for the next 4 hours to address the issue. You have to set up a temporary policy exception for him and authorize it, citing 'Emergency incident response' as the justification.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "olewis"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "database-cluster-primary"
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "admin-database-cluster-primary",
                    "resource_id": "RES-026"
                },
            },
            {
                "name": "CreatePolicyException",
                "arguments": {
                    "user_id": "U-029",
                    "permission_id": "P-113",
                    "reviewed_by": "U-005",
                    "reason": "Emergency incident response",
                    "expires_on": "2025-08-08T13:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "target_id": "PE-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Policy exception PE-021 requested by user U-005"
                },
            },
            {
                "name": "GetPolicyExceptionDetails",
                "arguments": {
                    "exception_id": "PE-021"
                },
            },
            {
                "name": "ApprovePolicyException",
                "arguments": {
                    "exception_id": "PE-021",
                    "reviewed_by": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "POLICY_EXCEPTION_APPROVED",
                    "target_id": "PE-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Policy exception PE-021 approved by user U-005."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "oliver.lewis@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Policy Exception Granted",
                    "text_content": "Policy exception for permission 'admin-database-cluster-primary' granted. Expiration: 2025-08-08T13:56:15Z."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-029\"",
                "\"exception_id\": \"PE-021\", \"status\": \"ACTIVE\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_007",
        "instruction": "As Mason Martinez, the Engineering Lead for 'Project Alpha' and currently its sole participant, you must establish a 'project-alpha-dev' (description: 'Developer role for Project Alpha') role granting developers read/write permissions to the 'main-application-repo' ('read-main-repo', 'write-main-repo') and read rights to the 'dev-database-server' ('read-dev-database'). Ensure that all existing project members are provided this role.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "project-alpha-dev",
                    "description": "Developer role for Project Alpha"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-001."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "project-alpha-dev"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "main-application-repo"
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "read-main-repo",
                    "resource_id": "RES-002"
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "write-main-repo",
                    "resource_id": "RES-002"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "dev-database-server"
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "read-dev-database",
                    "resource_id": "RES-007"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-113"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-114"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-115"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-043"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-001",
                    "role_id": "ROL-043",
                    "assigned_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-001",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-001."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-001"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-001\", \"roles\": [\"engineering-base\", \"engineering-lead\", \"project-alpha-dev\"",
                "\"role_id\": \"ROL-043\"",
                "\"permissions\": [\"P-113\", \"P-114\", \"P-115\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_008",
        "instruction": "Being Alexander Clark from the sales team, you are to request read access to examine the marketing analytics data for a new report. The rationale for this request is noted as 'Required for Q3 sales-marketing alignment report.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Clark"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "marketing-analytics-dashboard"
                },
            },
            {
                "name": "ListRoles",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-analytics-read"
                },
            },
            {
                "name": "CreateAccessRequest",
                "arguments": {
                    "user_id": "U-009",
                    "resource_id": "RES-010",
                    "requested_role_id": "ROL-009",
                    "justification": "Required for Q3 sales-marketing alignment report."
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-009",
                    "action_type": "ACCESS_REQUEST_CREATED",
                    "target_id": "AR-042",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-042 created by user U-009."
                },
            },
            {
                "name": "GetAccessRequestDetails",
                "arguments": {
                    "request_id": "AR-042"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "marketing-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Access Request",
                    "description": "Access request AR-042: Role ROL-009 for aclark (U-009).",
                    "requester_id": "U-009",
                    "category": "Access Management",
                    "assignee_id": "U-002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "username": "aclark",
                    "channel": "#access-requests",
                    "message": "Access request AR-042 for resource RES-010 has been created by user U-009. Please review."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-042\", \"status\": \"PENDING\"",
                "\"message_id\": \"SL-042\"",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_009",
        "instruction": "As Noah Thompson, an IT auditor, you have detected a possible Separation of Duties violation regarding employee Emma Martinez, who possesses both the 'hr-recruitment-manager' and 'hr-payroll-admin' roles. It is necessary to investigate and rectify this issue by rescinding the temporary payroll access and logging a ticket stating 'Conflicting roles 'hr-recruitment-manager' and 'hr-payroll-admin' found for employee Emma Martinez. Revoked temporary 'hr-payroll-admin' role.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "ejohnson"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-010"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "hr-payroll-admin"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-010",
                    "role_id": "ROL-018"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-010",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-018 removed from user U-010."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-010"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "SoD Violation",
                    "description": "Conflicting roles 'hr-recruitment-manager' and 'hr-payroll-admin' found for employee Emma Martinez. Revoked temporary 'hr-payroll-admin' role.",
                    "requester_id": "U-005",
                    "category": "Compliance",
                    "assignee_id": "U-005"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-010\"",
                "\"roles\": [\"hr-base\", \"hr-recruitment-manager\"]",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_010",
        "instruction": "In your role as Emma Martinez, an HR compliance manager, assign the 'security-awareness-training-q3' role to all active users within the Sales and Marketing departments to oversee the new Q3 security training. The role description is 'Tracks completion of Q3 security training.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Emma",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "security-awareness-training-q3",
                    "description": "Tracks completion of Q3 security training"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-010."
                },
            },
            {
                "name": "GetActiveUsersByDepartment",
                "arguments": {
                    "department": "Sales"
                },
            },
            {
                "name": "GetActiveUsersByDepartment",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-009",
                    "role_id": "ROL-043",
                    "assigned_by": "U-010"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-009."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-015",
                    "role_id": "ROL-043",
                    "assigned_by": "U-010"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-015",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-015."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-021",
                    "role_id": "ROL-043",
                    "assigned_by": "U-010"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-021."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-002",
                    "role_id": "ROL-043",
                    "assigned_by": "U-010"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-002."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-014",
                    "role_id": "ROL-043",
                    "assigned_by": "U-010"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-014."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-026",
                    "role_id": "ROL-043",
                    "assigned_by": "U-010"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-026."
                }
            }
        ],
        "outputs": [
                "\"role_id\": \"ROL-043\"",
                "\"user_id\": \"U-009\", \"role_id\": \"ROL-043\", \"assigned_by\": \"U-010\"",
                "\"user_id\": \"U-015\", \"role_id\": \"ROL-043\", \"assigned_by\": \"U-010\"",
                "\"user_id\": \"U-021\", \"role_id\": \"ROL-043\", \"assigned_by\": \"U-010\"",
                "\"user_id\": \"U-002\", \"role_id\": \"ROL-043\", \"assigned_by\": \"U-010\"",
                "\"user_id\": \"U-014\", \"role_id\": \"ROL-043\", \"assigned_by\": \"U-010\"",
                "\"user_id\": \"U-026\", \"role_id\": \"ROL-043\", \"assigned_by\": \"U-010\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_011",
        "instruction": "Identify as Noah Thompson, an IT auditor. For a regular audit of temporary roles, you've found that employee William Thompson no longer requires temporary access to the 'engineering-prod-access' role as his project is complete. You need to revoke this role. The audit log must indicate 'Role ROL-003 removed from user U-007.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Rodriguez"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "wthompson"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-prod-access"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-003 removed from user U-007."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-007"
                }
            }
        ],
        "outputs": [
                "\"revoked_role\": \"ROL-003\", \"user_id\": \"U-007\"",
                "\"roles\": [\"engineering-base\", \"engineering-code-commit\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_012",
        "instruction": "Act as Mason Martinez, the Engineering Lead. The system 'salesforce-crm-prod' will be phased out. Initially, remove all associated permissions from every role and deprecate those roles that are left with no permissions following the policy. The updated description for these deprecated roles should be: 'Deprecated due to Salesforce CRM being decommissioned'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "salesforce-crm-prod"
                },
            },
            {
                "name": "GetPermissionsByResource",
                "arguments": {
                    "resource_id": "RES-014"
                },
            },
            {
                "name": "GetRolesByPermission",
                "arguments": {
                    "permission_id": "P-038"
                },
            },
            {
                "name": "GetRolesByPermission",
                "arguments": {
                    "permission_id": "P-039"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-014"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-036"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-011",
                    "permission_id": "P-038"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-014",
                    "permission_id": "P-038"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-014",
                    "permission_id": "P-039"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-036",
                    "permission_id": "P-039"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-014"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-036"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_id": "ROL-014"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "user_id": "U-021"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-021",
                    "role_id": "ROL-014"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-014 removed from user U-021."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-021"
                },
            },
            {
                "name": "UpdateRoleDetails",
                "arguments": {
                    "role_id": "ROL-014",
                    "new_name": "[DEPRECATED]sales-reporting",
                    "new_description": "Deprecated due to Salesforce CRM being decommissioned"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_UPDATED",
                    "target_id": "ROL-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-014 has been updated. name=[[DEPRECATED]sales-reporting] | description=[Deprecated due to Salesforce CRM being decommissioned]"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_id": "ROL-014"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-021\"",
                "\"roles\": [\"sales-base\", \"sales-lead-manager\"]",
                "\"users\": []",
                "\"role_id\": \"ROL-014\", \"permissions\": []"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_013",
        "instruction": "You assume the role of Alexander Clark within the Sales team. You must engage in a cross-departmental initiative and require access to the email-marketing-service to review marketing campaigns. Submit a request for the 'marketing-campaign-manager' role. The reason provided should be 'Access needed for Project Nightingale sales and marketing alignment.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Clark"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "email-marketing-service"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-campaign-manager"
                },
            },
            {
                "name": "CreateAccessRequest",
                "arguments": {
                    "user_id": "U-009",
                    "resource_id": "RES-009",
                    "requested_role_id": "ROL-007",
                    "justification": "Access needed for Project Nightingale sales and marketing alignment."
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-009",
                    "action_type": "ACCESS_REQUEST_CREATED",
                    "target_id": "AR-042",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-042 created by user U-009."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "marketing-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Access Request",
                    "description": "Access request AR-042: Role ROL-007 for aclark (U-009).",
                    "requester_id": "U-009",
                    "category": "Access Management",
                    "assignee_id": "U-002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "username": "aclark",
                    "channel": "#access-requests",
                    "message": "Access request AR-042 for resource RES-009 has been created by user U-009. Please review."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-042\", \"status\": \"PENDING\"",
                "\"message_id\": \"SL-042\"",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_014",
        "instruction": "Identify yourself as Noah Thompson from operations. Conduct a review to ensure no HR department employees possess the 'sales-crm-access' role. You discovered employee Ava Johnson holds this role contrary to policy, and revocation is necessary. Document with 'Found and revoked 'sales-crm-access' role from HR employee Ava Martinez (ejohnson).' for the ticket.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Rodriguez"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "sales-crm-access"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-016",
                    "role_id": "ROL-012"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-016",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-012 removed from user U-016."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-016"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "SoD Violation",
                    "description": "Found and revoked 'sales-crm-access' role from HR employee Ava Johnson (ejohnson).",
                    "requester_id": "U-005",
                    "assignee_id": "U-005",
                    "category": "Compliance"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-016\"",
                "\"roles\": [\"hr-base\"]",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_015",
        "instruction": "Function as Mason Martinez, the Engineering Lead. Employee Nathan Thompson requires short-term access to the production environment for deploying a critical hotfix. Assign him the 'engineering-prod-access' role for a duration of the next 8 hours.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "nwhite"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-prod-access"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-013",
                    "role_id": "ROL-003",
                    "assigned_by": "U-001",
                    "expires_on": "2025-08-08T17:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-013",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-003 added to user U-013."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-013"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-013\"",
                "\"roles\": [\"engineering-base\", \"engineering-prod-access\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_016",
        "instruction": "You are Noah Thompson, the Operations Lead. Handle the creation of a new resource for the company's new 'customer-pii-database'. Set its criticality as 'CRITICAL' and designate yourself as the owner. Additionally, coordinate the creation of a new role 'pi-database-manager' (description: 'Role for managing customer PII data') with two new permissions: 'read-customer-pii-database' and 'write-customer-pii-database', with the respective descriptions 'Allows read access to customer pii database' and 'Allows write access to customer pii database'. Assign the new role to the heads of the Operations and HR departments.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "CreateResource",
                "arguments": {
                    "name": "customer-pii-database",
                    "owner_id": "U-005",
                    "criticality": "CRITICAL"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "RESOURCE_CREATED",
                    "target_id": "RES-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Resource RES-043 created by user U-005."
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "read-customer-pii-database",
                    "resource_id": "RES-043",
                    "description": "Allows read access to customer pii database"
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "write-customer-pii-database",
                    "resource_id": "RES-043",
                    "description": "Allows write access to customer pii database"
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "pi-database-manager",
                    "description": "Role for managing customer pii data"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-005."
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-113"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-114"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-043"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "hr-lead"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-004",
                    "role_id": "ROL-043",
                    "assigned_by": "U-005"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-005",
                    "role_id": "ROL-043",
                    "assigned_by": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-004",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-004."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-005",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-005."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-004"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-005"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-004\", \"roles\": [\"hr-base\", \"hr-lead\", \"pi-database-manager\"",
                "\"user_id\": \"U-005\", \"roles\": [\"operations-base\", \"operations-lead\", \"pi-database-manager\"",
                "\"resource_id\": \"RES-043\"",
                "\"permission_id\": \"P-113\"",
                "\"permission_id\": \"P-114\"",
                "\"role_id\": \"ROL-043\", \"permissions\": [\"P-113\", \"P-114\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_017",
        "instruction": "You are Noah Thompson, the Operations Lead. Approve the pending access request from employee Oliver Lewis. The request ID is 'AR-007'.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetAccessRequestDetails",
                "arguments": {
                    "request_id": "AR-007"
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-007",
                    "status": "APPROVED",
                    "reviewed_by": "U-005"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-007 granted by user U-005."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-029",
                    "role_id": "ROL-026",
                    "assigned_by": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-029",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-026 added to user U-029."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-029"
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-011",
                    "status": "CLOSED",
                    "note": "Access request AR-007 has been approved."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-007\", \"status\": \"APPROVED\"",
                "\"ticket_id\": \"TI-011\", \"status\": \"CLOSED\"",
                "\"roles\": [\"operations-base\", \"operations-system-admin\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_018",
        "instruction": "You are the RBAC system. The temporary access for employee William Thompson granted through the 'engineering-prod-access' role has expired. Revoke this role.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "wthompson"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-prod-access"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-003"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-003 removed from user U-007."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "william.thompson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Temporary Access Revoked",
                    "text_content": "Your temporary access role 'engineering-prod-access' has expired and has been revoked."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-007"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-007\"",
                "\"roles\": [\"engineering-base\", \"engineering-code-commit\"]",
                "\"email_id\": \"EM-016\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_019",
        "instruction": "You are Mason Martinez, the Engineering Lead. Handle the creation of a new 'jira-editor' (description: 'Ticket management access') role for the 'jira-project-management' resource. Include the 'create-jira-issue', 'view-jira-issue', and 'edit-jira-issue' permissions. Also incorporate a new 'delete-jira-issue' permission (description: 'Allows deleting issues in Jira'). Assign this new role to anyone currently serving as an engineering lead.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "jira-project-management"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "jira-editor",
                    "description": "Ticket management access"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-001."
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "delete-jira-issue",
                    "resource_id": "RES-004",
                    "description": "Allows deleting issues in Jira"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "PERMISSION_CREATED",
                    "target_id": "P-113",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-113 created by user U-001."
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-113"
                },
            },
            {
                "name": "GetPermissionDetails",
                "arguments": {
                    "permission_name": "create-jira-issue"
                },
            },
            {
                "name": "GetPermissionDetails",
                "arguments": {
                    "permission_name": "view-jira-issue"
                },
            },
            {
                "name": "GetPermissionDetails",
                "arguments": {
                    "permission_name": "edit-jira-issue"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-007"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-008"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-009"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-043"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "jira-editor"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "engineering-lead"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-001",
                    "role_id": "ROL-043",
                    "assigned_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-001",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-001."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-001"
                }
            }
        ],
        "outputs": [
                "\"permission_id\": \"P-113\"",
                "\"role_id\": \"ROL-043\"",
                "\"permissions\": [\"P-007\", \"P-008\", \"P-009\", \"P-113\"]",
                "\"user_id\": \"U-001\", \"roles\": [\"engineering-base\", \"engineering-lead\", \"jira-editor\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_020",
        "instruction": "You are an automated RBAC bot. A high-severity SIEM alert has been activated for employee William Thompson due to an 'unauthorised_ACCESS_ATTEMPT' on the 'employee-data-portal'. Suspend the user's account and initiate a ticket for the operations team to conduct an investigation.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "William",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetSiemAlerts",
                "arguments": {
                    "user_id": "U-007"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "SIEM_ALERT_CREATED",
                    "target_id": "ALRT-011",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "SIEM alert ALRT-011 created by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-007",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-007 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-007"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-001 removed from user U-007."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-code-commit"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-002"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-002 removed from user U-007."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-prod-access"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-003 removed from user U-007."
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "employee-data-portal"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_id": "ROL-038"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Security Incident",
                    "description": "User William Thompson (wthompson) account suspended due to unauthorised access attempt on employee-data-portal.",
                    "requester_id": "U-031",
                    "category": "Security Incident",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-007"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-007\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-007\", \"roles\": []",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_021",
        "instruction": "Assume the role of Noah Thompson, the Operations Lead. Isabella Martinez's employment has been terminated, and it falls upon you to manage her system offboarding. This requires disabling her account, retracting all assigned roles, and initiating a ticket for Sophia Thompson, the Marketing Lead, to address asset reallocation.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Isabella",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-008",
                    "status": "DISABLED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-008",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-008 status changed to 'DISABLED' by user U-005."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-008"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-008",
                    "role_id": "ROL-006"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-008",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-006 removed from user U-008."
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Offboard employee Isabella Martinez (imartinez)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "requester_id": "U-005",
                    "category": "Offboarding",
                    "assignee_id": "U-002"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-008\", \"status\": \"DISABLED\"",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_022",
        "instruction": "Act as Sophia Thompson, the Marketing Lead. Sophie Turner has submitted a pending request (AR-009) seeking temporary access to the 'marketing-social-media' role for an imminent campaign. Having reviewed the request, you are tasked with approving it, ensuring the access concludes in 30 days.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetAccessRequestDetails",
                "arguments": {
                    "request_id": "AR-009"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-009",
                    "status": "APPROVED",
                    "reviewed_by": "U-002"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-009",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-009 granted by user U-002."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-026",
                    "role_id": "ROL-008",
                    "assigned_by": "U-002",
                    "expires_on": "2025-09-07T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-008 added to user U-026."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-026"
                },
            },
            {
                "name": "GetHubspotTicketsByRequester",
                "arguments": {
                    "requester_id": "U-026"
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-011",
                    "status": "CLOSED",
                    "note": "Access request AR-009 has been approved."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-009\", \"status\": \"APPROVED\"",
                "\"user_id\": \"U-026\"",
                "\"roles\": [\"marketing-base\", \"marketing-campaign-manager\", \"marketing-content-editor\", \"marketing-social-media\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_023",
        "instruction": "Take on the role of Mason Martinez, the Engineering Lead. The decision has been made by the company to integrate infrastructure in the cloud, leading to a subscription to AWS. You are required to establish a new 'aws-cloud-services' resource (criticality: 'CRITICAL') with Nathan Thompson designated as the owner to mirror this update. Additionally, you must create a new 'cloud-infrastructure-manager' role (description: 'Manages all cloud infrastructure resources.') and allocate it to Nathan Thompson and all current holders of the 'engineering-prod-access' role. This role must possess new permissions for the added resource: 'create-cloud-resources' (description: 'Allows creation of new cloud resources'), 'view-cloud-resources' (description: 'Allows read-only access to configuration of cloud resources'), 'modify-cloud-resources' (description: 'Allows modification of existing cloud resources'), and 'remove-cloud-resources' (description: 'Allows removing existing cloud resources')",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Nathan",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateResource",
                "arguments": {
                    "name": "aws-cloud-services",
                    "owner_id": "U-013",
                    "criticality": "CRITICAL"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "RESOURCE_CREATED",
                    "target_id": "RES-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Resource RES-043 created by user U-001."
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "cloud-infrastructure-manager",
                    "description": "Manages all cloud infrastructure resources."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-001."
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "create-cloud-resources",
                    "resource_id": "RES-043",
                    "description": "Allows creation of new cloud resources"
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "view-cloud-resources",
                    "resource_id": "RES-043",
                    "description": "Allows read-only access to configuration of cloud resources"
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "modify-cloud-resources",
                    "resource_id": "RES-043",
                    "description": "Allows modification of existing cloud resources"
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "remove-cloud-resources",
                    "resource_id": "RES-043",
                    "description": "Allows removing existing cloud resources"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-113"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-114"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-115"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-116"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "engineering-prod-access"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-043",
                    "assigned_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-007."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-025",
                    "role_id": "ROL-043",
                    "assigned_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-025",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-025."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-013",
                    "role_id": "ROL-043",
                    "assigned_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-013",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-013."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-007"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-025"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-013"
                }
            }
        ],
        "outputs": [
                "\"resource_id\": \"RES-043\", \"name\": \"aws-cloud-services\", \"owner_id\": \"U-013\"",
                "\"role_id\": \"ROL-043\"",
                "\"user_id\": \"U-007\", \"roles\": [\"engineering-base\", \"engineering-code-commit\", \"engineering-prod-access\", \"cloud-infrastructure-manager\"",
                "\"user_id\": \"U-025\", \"roles\": [\"engineering-base\", \"engineering-prod-access\", \"cloud-infrastructure-manager\"",
                "\"user_id\": \"U-013\", \"roles\": [\"engineering-base\", \"cloud-infrastructure-manager\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_024",
        "instruction": "Fulfill the duties of Noah Martinez, the Sales Lead. You have received an access request (AR-022) from Alexander Clark that requires rejection due to a breach in inter-departmental access policies. Communicate to him via email that the rejection is due to: 'Access to this resource is restricted to the marketing department.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetAccessRequestDetails",
                "arguments": {
                    "request_id": "AR-022"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "aclark"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-022",
                    "status": "REJECTED",
                    "reviewed_by": "U-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ACCESS_REJECTED",
                    "target_id": "AR-022",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-022 rejected by user U-003."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "alexander.clark@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Access Request Rejected",
                    "text_content": "Your access request (AR-022) has been rejected for the following reason: Access to this resource is restricted to the marketing department."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-022\", \"status\": \"REJECTED\"",
                "\"email_id\": \"EM-016\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_025",
        "instruction": "Operate as the automated RBAC system. The present date and time is 2025-09-06T06:00:00+00:00; ignore all other date and time data. You have identified that policy exception PE-010 for Isabella Martinez is overdue. You must address the issue as per policy requirements.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetPolicyExceptionDetails",
                "arguments": {
                    "exception_id": "PE-010"
                },
            },
            {
                "name": "UpdatePolicyExceptionStatus",
                "arguments": {
                    "exception_id": "PE-010",
                    "status": "EXPIRED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "POLICY_EXCEPTION_EXPIRED",
                    "target_id": "PE-010",
                    "timestamp": "2025-09-06T06:00:00+00:00",
                    "details": "Policy exception PE-010 has expired."
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "imartinez"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "isabella.martinez@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-09-06T06:00:00+00:00",
                    "subject": "Policy Exception Expired",
                    "text_content": "Your temporary policy exception (PE-010) has expired."
                }
            }
        ],
        "outputs": [
                "\"exception_id\": \"PE-010\", \"status\": \"EXPIRED\"",
                "\"email_id\": \"EM-016\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_026",
        "instruction": "As Sophia Thompson, the HR Lead, William Thompson is transitioning from Engineering to the Operations department. Handle updating his profile to mirror this shift by removing all his earlier engineering roles ('engineering-base', 'engineering-code-commit', 'engineering-prod-access') and assigning the standard 'operations-base' role.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "wthompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserDepartment",
                "arguments": {
                    "user_id": "U-007",
                    "department": "Operations"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "USER_DEPARTMENT_CHANGED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-007 department changed to Operations by user U-004."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-001 removed from user U-007."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-code-commit"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-002"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-002 removed from user U-007."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-prod-access"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-003 removed from user U-007."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "operations-base"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-021",
                    "assigned_by": "U-004"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-021 added to user U-007."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "william.thompson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Welcome to the Operations Team",
                    "text_content": "Welcome, William! Your system access has been updated for your new role in the Operations department."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-007\", \"department\": \"Operations\"",
                "\"roles\": [\"operations-base\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_027",
        "instruction": "As Noah Thompson, an IT auditor, your task is to start the quarterly access reviews. Proceed to launch the certification campaign for the 'invoicing-system' resource, ensuring it is assigned to its owner, Victoria Lee, with a deadline of 30 days.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "invoicing-system"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "vlee"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateCertification",
                "arguments": {
                    "reviewer_id": "U-012",
                    "resource_id": "RES-032",
                    "due_date": "2025-09-07T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "CERTIFICATION_CREATED",
                    "target_id": "C-024",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Certification C-024 requested by user U-005."
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "username": "CERTIFICATION_BOT",
                    "channel": "#certifications",
                    "message": "A new certification C-024 for resource RES-032 has been requested. Due date 2025-09-07T09:56:15Z"
                }
            }
        ],
        "outputs": [
                "\"certification_id\": \"C-024\", \"status\": \"PENDING\", \"resource_id\": \"RES-032\"",
                "\"message_id\": \"SL-042\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_028",
        "instruction": "Being Noah Thompson, Operations Lead, following the resolution of the recent security incident, the temporary 'operations-incident-response' role is redundant, so coordinate its removal from all assigned users.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "operations-incident-response"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_id": "ROL-023"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "user_id": "U-023"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-023"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-023",
                    "role_id": "ROL-023"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-023",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-023 removed from user U-023."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "jacob.allen@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Temporary Access Revoked",
                    "text_content": "Your temporary access role 'operations-incident-response' has expired and has been revoked."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-023"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-023\"",
                "\"roles\": [\"operations-base\", \"operations-deployment-admin\"]",
                "\"email_id\": \"EM-016\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_029",
        "instruction": "As Sophia Thompson, Marketing Lead, manage the registration of the newly acquired tool in the system as the 'marketing-analytics-platform' resource. Designate it as 'HIGH' criticality with a 'GDPR' compliance scope, with you as the owner. Additionally, create a new role 'marketing-analytics-admin' (description: 'Admin role for marketing analytics platform') featuring a new permission 'admin-marketing-analytics-platform' (description: 'Admin permission for marketing analytics platform') for the platform. Assign this role to yourself.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateResource",
                "arguments": {
                    "name": "marketing-analytics-platform",
                    "owner_id": "U-002",
                    "criticality": "HIGH",
                    "compliance_scope": "GDPR"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "RESOURCE_CREATED",
                    "target_id": "RES-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Resource RES-043 created by user U-002."
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "marketing-analytics-platform"
                },
            },
            {
                "name": "CreateRoleWithPermission",
                "arguments": {
                    "role_name": "marketing-analytics-admin",
                    "resource_id": "RES-043",
                    "permission_name": "admin-marketing-analytics-platform",
                    "role_description": "Admin role for marketing analytics platform",
                    "permission_description": "Admin permission for marketing analytics platform"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-002",
                    "role_id": "ROL-043",
                    "assigned_by": "U-002"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-002."
                }
            }
        ],
        "outputs": [
                "\"resource_id\": \"RES-043\", \"name\": \"marketing-analytics-platform\", \"owner_id\": \"U-002\"",
                "\"role_id\": \"ROL-043\"",
                "\"permission_id\": \"P-113\"",
                "\"user_id\": \"U-002\", \"roles\": [\"marketing-base\", \"marketing-lead\", \"marketing-analytics-admin\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_030",
        "instruction": "As Oliver Lewis from the Operations team, you have concluded that the security alert investigation involving Isabella Martinez was a false positive. Proceed to change her account status from 'SUSPENDED' to 'ACTIVE'.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Lewis"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "imartinez"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-008",
                    "status": "ACTIVE"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-008",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-008 status changed to 'ACTIVE' by user U-029."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "isabella.martinez@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Account Reactivated",
                    "text_content": "Your account has been reactivated and your access has been restored."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-008\", \"status\": \"ACTIVE\"",
                "\"email_id\": \"EM-016\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_031",
        "instruction": "You are Emma Martinez from Human Resources. A new Engineering Manager named Charles Johnson has been hired. Handle the onboarding of his account, providing him temporary 'engineering-prod-access' for 180 days. The engineering lead will need to approve the new user.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Emma",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateUser",
                "arguments": {
                    "username": "cbrown",
                    "email": "charles.Johnson@sigmatech.com",
                    "department": "Engineering",
                    "status": "PENDING_ACCESS"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-034 created by user U-010."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-base"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-034",
                    "role_id": "ROL-001",
                    "assigned_by": "U-010"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-001 added to user U-034."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-prod-access"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-034",
                    "role_id": "ROL-003",
                    "assigned_by": "U-010",
                    "expires_on": "2026-02-04T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-003 added to user U-034."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-034"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "engineering-lead"
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-034",
                    "status": "ACTIVE"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-034 status changed to 'ACTIVE' by user U-001."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-034\", \"status\": \"ACTIVE\"",
                "\"roles\": [\"engineering-base\", \"engineering-prod-access\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_032",
        "instruction": "You are Ethan Johnson from Sales. Seek access to the 'finance-budget-admin' role for the 'budgeting-tool' from the finance department resource, providing the justification 'Access needed for Q4 budget planning collaboration'.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Ethan",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "budgeting-tool"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-budget-admin"
                },
            },
            {
                "name": "CreateAccessRequest",
                "arguments": {
                    "user_id": "U-015",
                    "resource_id": "RES-033",
                    "requested_role_id": "ROL-032",
                    "justification": "Access needed for Q4 budget planning collaboration"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-015",
                    "action_type": "ACCESS_REQUEST_CREATED",
                    "target_id": "AR-042",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-042 created by user U-015."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "finance-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Access Request",
                    "description": "Access request AR-042: Role ROL-032 for ebrown (U-015).",
                    "requester_id": "U-015",
                    "category": "Access Management",
                    "assignee_id": "U-006"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "username": "ebrown",
                    "channel": "#access-requests",
                    "message": "Access request AR-042 for resource RES-033 has been created by user U-015. Please review."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-042\", \"status\": \"PENDING\"",
                "\"user_id\": \"U-015\"",
                "\"ticket_id\": \"TI-054\"",
                "\"message_id\": \"SL-042\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_033",
        "instruction": "You are Noah Thompson, Operations Lead. A SIEM alert has flagged a potential account compromise affecting Madison Martinez. Carry out the necessary actions.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "mjackson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-014",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-014 status changed to 'SUSPENDED' by user U-005."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-014"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-base"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-analytics-read"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-014",
                    "role_id": "ROL-006"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-014",
                    "role_id": "ROL-009"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-006 removed from user U-014."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-009 removed from user U-014."
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-014",
                    "mfa_enabled": true
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "madison.Martinez@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "MFA Enabled on Your Account",
                    "text_content": "Multi-factor authentication (MFA) has been enabled on your account."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-014 by user U-005."
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Security Incident",
                    "description": "User Madison Martinez (mjackson) account suspended due to potentially being compromised.",
                    "requester_id": "U-005",
                    "category": "Security",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-014"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-014\", \"status\": \"SUSPENDED\", \"mfa_enabled\": true",
                "\"user_id\": \"U-014\", \"roles\": []",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_034",
        "instruction": "You are Mason Martinez, Engineering Lead. To accommodate a new internal NuGet package system, establish a 'HIGH' criticality resource named 'internal-nuget-repository' which you will be responsible for. Develop a 'publish-package' permission (description: 'Allows publishing packages to the repository') and a 'nuget-publisher' role (description 'Allows publishing to internal NuGet') which includes the new permission. Assign the new role to William Thompson.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateResource",
                "arguments": {
                    "name": "internal-nuget-repository",
                    "owner_id": "U-001",
                    "criticality": "HIGH"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "RESOURCE_CREATED",
                    "target_id": "RES-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Resource RES-043 created by user U-001."
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "publish-package",
                    "resource_id": "RES-043",
                    "description": "Allows publishing packages to the repository"
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "nuget-publisher",
                    "description": "Allows publishing to internal NuGet"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-113"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "wthompson"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-043",
                    "assigned_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-007."
                }
            }
        ],
        "outputs": [
                "\"resource_id\": \"RES-043\"",
                "\"permission_id\": \"P-113\"",
                "\"role_id\": \"ROL-043\"",
                "\"assigned_user\": \"U-007\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_035",
        "instruction": "You are Noah Thompson, an IT auditor. A compliance scan has detected a Separation of Duties (SoD) violation for Mia Robinson, who holds both a standard finance role and a temporary audit access role. Rectify this by withdrawing her temporary 'finance-audit-access' role and create a ticket to document the finding and resolution. The ticket should carry the subject 'SoD Violation' and the description 'Revoked conflicting role finance-audit-access from user mrobinson.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "mrobinson"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-audit-access"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-018",
                    "role_id": "ROL-033"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-018",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-033 removed from user U-018."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "SoD Violation",
                    "description": "Revoked conflicting role finance-audit-access from user mrobinson.",
                    "requester_id": "U-005",
                    "category": "Compliance",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-018"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-018\"",
                "\"roles\": [\"finance-base\"]",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_036",
        "instruction": "You are Mason Martinez, Engineering Lead. The role 'engineering-db-schema' is being phased out due to departmental restructuring. Handle the necessary procedures and apply the new description 'Deprecated due to department restructuring' for the deprecated role.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-db-schema"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_id": "ROL-004"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "user_id": "U-019"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-019",
                    "role_id": "ROL-004"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-004 removed from user U-019."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-019"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_id": "ROL-004"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-004"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-004",
                    "permission_id": "P-018"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-004"
                },
            },
            {
                "name": "UpdateRoleDetails",
                "arguments": {
                    "role_id": "ROL-004",
                    "new_name": "[DEPRECATED]engineering-db-schema",
                    "new_description": "Deprecated due to department restructuring"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_UPDATED",
                    "target_id": "ROL-004",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-004 has been updated. name=[[DEPRECATED]engineering-db-schema] | description=[Deprecated due to department restructuring]"
                }
            }
        ],
        "outputs": [
                "\"role_revoked\": \"ROL-004\"",
                "\"user_id\": \"U-019\", \"roles\": [\"engineering-base\", \"engineering-qa-test\"]",
                "\"users\": []",
                "\"role_id\": \"ROL-004\", \"permissions\": []"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_037",
        "instruction": "You are Mason Martinez, Engineering Lead. Your team member, Nathan Thompson, urgently needs temporary access to adjust firewall rules on the 'network-firewall-main' resource. Coordinate the creation of a new permission called 'modify-firewall-rules-temp' (description: 'Allows temporary modification of firewall rules.'), and provide him with a 24-hour policy exception citing 'Urgent network reconfiguration required' as the reason.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "network-firewall-main"
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "modify-firewall-rules-temp",
                    "resource_id": "RES-027",
                    "description": "Allows temporary modification of firewall rules."
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "PERMISSION_CREATED",
                    "target_id": "P-113",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-113 created by user U-001."
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Nathan",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "CreatePolicyException",
                "arguments": {
                    "user_id": "U-013",
                    "permission_id": "P-113",
                    "reason": "Urgent network reconfiguration required",
                    "expires_on": "2025-08-09T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "target_id": "PE-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Policy exception PE-021 requested by user U-001"
                },
            },
            {
                "name": "ApprovePolicyException",
                "arguments": {
                    "exception_id": "PE-021",
                    "reviewed_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "POLICY_EXCEPTION_APPROVED",
                    "target_id": "PE-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Policy exception PE-021 approved by user U-001."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "nathan.Thompson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Policy Exception Granted",
                    "text_content": "Policy exception for permission 'modify-firewall-rules-temp' granted. Expiration: 2025-08-09T09:56:15Z."
                }
            }
        ],
        "outputs": [
                "\"permission_id\": \"P-113\"",
                "\"exception_id\": \"PE-021\", \"status\": \"ACTIVE\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_038",
        "instruction": "You are the RBAC system. A password reset request has been started for user Victoria Lee. Address the necessary action.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "vlee"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-012",
                    "status": "PENDING_ACCESS"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-012",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-012 status changed to 'PENDING_ACCESS' by user U-031."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "victoria.lee@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Password Reset",
                    "text_content": "A password reset was initiated for your account. Please follow the link to create a new password."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-012\", \"status\": \"PENDING_ACCESS\"",
                "\"email_id\": \"EM-016\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_039",
        "instruction": "You are Sophia Thompson, Marketing Lead. Since the 'social-media-platform' resource is now under the management of the Operations team, you need to officially hand over its ownership to the Operations Lead. Notify him via email about the change (subject: 'Ownership Transfer 'social-media-platform'') with the content 'Ownership of the social media platform has successfully been transferred to you.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "social-media-platform"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "user_id": "U-005"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-008",
                    "new_owner_id": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-008",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-008 transferred from user U-002 to U-005."
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "social-media-platform"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "Noah.Thompson@sigmatech.com",
                    "sender": "Sophia.Thompson@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Ownership Transfer 'social-media-platform'",
                    "text_content": "Ownership of the social media platform has successfully been transferred to you."
                }
            }
        ],
        "outputs": [
                "\"resource_id\": \"RES-008\", \"owner_id\": \"U-005\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_040",
        "instruction": "You are Noah Thompson, Operations Lead. An urgent situation calls for the creation of a temporary 'emergency-patching-team' role for 24 hours to permit key personnel to deploy a critical patch. Use the description 'Provides temporary access for emergency server patching' for this new role. Assign this role to Jacob Allen and Lucas Thompson.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "emergency-patching-team",
                    "description": "Provides temporary access for emergency server patching",
                    "is_temporary": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-005."
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "jallen"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "lthompson"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-023",
                    "role_id": "ROL-043",
                    "assigned_by": "U-005",
                    "expires_on": "2025-08-09T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-023",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-023."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-017",
                    "role_id": "ROL-043",
                    "assigned_by": "U-005",
                    "expires_on": "2025-08-09T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-017."
                }
            }
        ],
        "outputs": [
                "\"role_id\": \"ROL-043\"",
                "\"assigned_users\": [\"U-023\", \"U-017\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_041",
        "instruction": "As Emma Martinez, HR Lead, your task is to onboard Olivia Allen, a new employee in the Finance department. Approval for the new user will be provided by the finance lead.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Emma",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateUser",
                "arguments": {
                    "username": "ogreen",
                    "email": "olivia.Allen@sigmatech.com",
                    "department": "Finance",
                    "status": "PENDING_ACCESS"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-034 created by user U-010."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-base"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-034",
                    "role_id": "ROL-029",
                    "assigned_by": "U-010"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-029 added to user U-034."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-034"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "finance-lead"
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-034",
                    "status": "ACTIVE"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-006",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-034 status changed to 'ACTIVE' by user U-006."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-034\", \"status\": \"ACTIVE\"",
                "\"roles\": [\"finance-base\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_042",
        "instruction": "Serving as Noah Thompson, IT Auditor, you have found that Jacob Allen's 'operations-deployment-admin' role is superfluous. Resolve this issue by withdrawing the role and opening a ticket with the subject 'Audit Remediation' and description 'Revoked redundant role operations-deployment-admin from user jallen as per audit finding.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Rodriguez"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "jallen"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "operations-deployment-admin"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-023",
                    "role_id": "ROL-025"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-023",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-025 removed from user U-023."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Audit Remediation",
                    "description": "Revoked redundant role 'operations-deployment-admin' from user 'jallen' as per audit finding.",
                    "requester_id": "U-005",
                    "category": "Compliance",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-023"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-023\"",
                "\"roles\": [\"operations-base\", \"operations-incident-response\"]",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_043",
        "instruction": "Functioning as Mason Martinez, Engineering Lead, it is necessary to approve the pending access request AR-020 for Nathan Thompson, which assigns him the 'engineering-db-schema' role required for his responsibilities.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetAccessRequestDetails",
                "arguments": {
                    "request_id": "AR-020"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-020",
                    "status": "APPROVED",
                    "reviewed_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-020",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-020 granted by user U-001."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-013",
                    "role_id": "ROL-004",
                    "assigned_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-013",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-004 added to user U-013."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-013"
                },
            },
            {
                "name": "GetHubspotTicketsByRequester",
                "arguments": {
                    "requester_id": "U-013"
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-022",
                    "status": "CLOSED",
                    "note": "Access request AR-020 has been approved."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-020\", \"status\": \"APPROVED\"",
                "\"user_id\": \"U-013\"",
                "\"roles\": [\"engineering-base\", \"engineering-db-schema\"]",
                "\"ticket_id\": \"TI-022\", \"status\": \"CLOSED\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_044",
        "instruction": "As the automated RBAC system, you have observed a CRITICAL SIEM alert regarding an unauthorized access attempt by Sophia Thompson on the 'salesforce-crm-prod'. It is essential to take the necessary actions to manage this situation.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "staylor"
                },
            },
            {
                "name": "GetSiemAlerts",
                "arguments": {
                    "user_id": "U-004"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "SIEM_ALERT_CREATED",
                    "target_id": "ALRT-012",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "SIEM alert ALRT-012 created by user U-031."
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-004",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-004",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-004 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-004"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "hr-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-004",
                    "role_id": "ROL-016"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-004",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-016 removed from user U-004."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "hr-lead"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-004",
                    "role_id": "ROL-037"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-004",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-037 removed from user U-004."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Security Incident",
                    "description": "User Sophia Thompson (staylor) account suspended due to unauthorised access attempt on 'salesforce-crm-prod'.",
                    "requester_id": "U-031",
                    "category": "Security incident",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-004"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-004\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-004\", \"roles\": []",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_045",
        "instruction": "In the role of Noah Johnson, Sales Lead, you must ensure compliance by confirming that all department users have MFA activated. Activate MFA on any accounts where it is not yet enabled.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Michael",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "GetUsersByDepartment",
                "arguments": {
                    "department": "Sales"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-021",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-021 by user U-003."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "logan.Scott@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "MFA Enabled on Your Account",
                    "text_content": "Multi-factor authentication (MFA) has been enabled on your account."
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-027",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-027",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-027 by user U-003."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "aiden.Harris@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "MFA Enabled on Your Account",
                    "text_content": "Multi-factor authentication (MFA) has been enabled on your account."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-021\", \"mfa_enabled\": true",
                "\"user_id\": \"U-027\", \"mfa_enabled\": true",
                "\"email_id\": \"EM-016\", \"receiver\": \"logan.Scott@sigmatech.com\", \"subject\": \"MFA Enabled on Your Account\"",
                "\"email_id\": \"EM-017\", \"receiver\": \"aiden.Wilson@sigmatech.com\", \"subject\": \"MFA Enabled on Your Account\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_046",
        "instruction": "As Mason Martinez, Engineering Lead, your task is to establish a temporary role, 'hotfix-deployment-override', for an urgent production deployment. Use the role description 'Temporary override for hotfix deployment'. It should be assigned to William Thompson with a valid period of 8 hours.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "wthompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "hotfix-deployment-override",
                    "description": "Temporary override for hotfix deployment.",
                    "is_temporary": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-001."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-043",
                    "assigned_by": "U-001",
                    "expires_on": "2025-08-08T17:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-007."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-007"
                }
            }
        ],
        "outputs": [
                "\"role_id\": \"ROL-043\", \"role_name\": \"hotfix-deployment-override\"",
                "\"user_id\": \"U-007\", \"roles\": [\"engineering-base\",\"engineering-code-commit\",\"engineering-prod-access\",\"hotfix-deployment-override\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_047",
        "instruction": "In the capacity of Noah Thompson, Operations Lead, the investigation of Sophia Thompson's account has been determined to be a false positive. You are required to restore her account and close the investigation ticket associated with the SIEM alert, including the note: 'Investigation complete. Account reactivated.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetHubspotTicketsByAssignee",
                "arguments": {
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "staylor"
                },
            },
            {
                "name": "GetSiemAlerts",
                "arguments": {
                    "user_id": "U-004"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-004"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-004",
                    "status": "ACTIVE"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-004",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-004 status changed to 'ACTIVE' by user U-005."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "sophia.Thompson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Account Reactivated",
                    "text_content": "Your account has been reactivated and your access has been restored."
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-053",
                    "status": "CLOSED",
                    "note": "Investigation complete. Account reactivated."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-004\", \"status\": \"ACTIVE\"",
                "\"ticket_id\": \"TI-053\", \"status\": \"CLOSED\"",
                "\"email_id\": \"EM-016\", \"subject\": \"Account Reactivated\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_048",
        "instruction": "Acting as Oliver Lewis, an IT Auditor, a compliance review has identified that Noah Martinez no longer needs the high-privilege 'engineering-db-schema' role. You need to remove this role from him. Furthermore, transfer ownership of the 'dev-database-server' from him to the Engineering Lead, Mason Martinez. Record this audit finding by creating a ticket with the description 'Remediated audit finding: Revoked unnecessary 'engineering-db-schema' role from user nmartinez and reassigned resource ownership.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Lewis"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "nmartinez"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-db-schema"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-019",
                    "role_id": "ROL-004"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-004 removed from user U-019."
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "dev-database-server"
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-007",
                    "new_owner_id": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-007 transferred from user U-019 to U-001."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Audit Remediation",
                    "description": "Remediated audit finding: Revoked unnecessary 'engineering-db-schema' role from user nmartinez and reassigned resource ownership.",
                    "requester_id": "U-029",
                    "category": "Compliance",
                    "assignee_id": "U-005"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-019\", \"revoked_role\": \"ROL-004\"",
                "\"resource_id\": \"RES-007\", \"owner_id\": \"U-001\"",
                "\"ticket_id\": \"TI-054\", \"status\": \"OPEN\"",
                "\"user_id\": \"U-019\", \"roles\": [\"engineering-base\", \"engineering-qa-test\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_049",
        "instruction": "As Sophia Thompson, Marketing Lead, you have to decline access request AR-021 made by Sophie Turner for the 'marketing-content-editor' role. The reason for this refusal is 'Role requires additional training, which has not been completed.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetAccessRequestDetails",
                "arguments": {
                    "request_id": "AR-021"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "sturner"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-026"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-021",
                    "status": "REJECTED",
                    "reviewed_by": "U-002"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ACCESS_REJECTED",
                    "target_id": "AR-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-021 rejected by user U-002."
                },
            },
            {
                "name": "GetHubspotTicketsByRequester",
                "arguments": {
                    "requester_id": "U-026"
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-023",
                    "status": "CLOSED",
                    "note": "Access request AR-021 has been denied. Reason: Role requires additional training, which has not been completed."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "sophie.turner@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Access Request Rejected",
                    "text_content": "Your access request (AR-021) has been rejected for the following reason: Role requires additional training, which has not been completed."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-021\", \"status\": \"REJECTED\"",
                "\"email_id\": \"EM-016\", \"subject\": \"Access Request Rejected\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_050",
        "instruction": "Serving as Noah Thompson, Operations Lead, since Benjamin Johnson has departed the company, you are to carry out his offboarding process.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "bharris"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-011",
                    "status": "DISABLED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-011",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-011 status changed to 'DISABLED' by user U-005."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-011"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "operations-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-011",
                    "role_id": "ROL-021"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-011",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-021 removed from user U-011."
                },
            },
            {
                "name": "GetResourcesByOwner",
                "arguments": {
                    "owner_id": "U-011"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "database-cluster-primary"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "log-management-system"
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-026",
                    "new_owner_id": "U-005"
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-029",
                    "new_owner_id": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-026 transferred from user U-011 to U-005."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-029",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-029 transferred from user U-011 to U-005."
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Offboard employee Benjamin Johnson (bharris)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "requester_id": "U-005",
                    "category": "Offboarding",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-011"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-011\", \"status\": \"DISABLED\"",
                "\"user_id\": \"U-011\", \"roles\": []",
                "\"ticket_id\": \"TI-054\"",
                "\"resource_id\": \"RES-026\", \"owner_id\": \"U-005\"",
                "\"resource_id\": \"RES-029\", \"owner_id\": \"U-005\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_051",
        "instruction": "Assume the role of Oliver Lewis, an IT Auditor. During Noah Martinez's extended leave, you need to establish a temporary 'sales-crm-approver' role (description: 'Temporary role to approve CRM access requests during owner's absence.') and allocate it to Alexander Clark for approval duties. This role should possess the 'read-crm-customer' and 'update-crm-opportunity' permissions.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Lewis"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Clark"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "salesforce-crm-prod"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "sales-crm-approver",
                    "description": "Temporary role to approve CRM access requests during owner's absence.",
                    "is_temporary": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-029."
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "read-crm-customer",
                    "resource_id": "RES-014"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "PERMISSION_CREATED",
                    "target_id": "P-113",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-113 created by user U-029."
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-113"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-113 assigned to role ROL-043."
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "update-crm-opportunity",
                    "resource_id": "RES-014"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "PERMISSION_CREATED",
                    "target_id": "P-114",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-114 created by user U-029."
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-114"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-114 assigned to role ROL-043."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-009",
                    "role_id": "ROL-043",
                    "assigned_by": "U-029"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-009."
                }
            }
        ],
        "outputs": [
                "\"role_id\": \"ROL-043\"",
                "\"permission_id\": \"P-113\"",
                "\"permission_id\": \"P-114\"",
                "\"assigned_user\": \"U-009\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_052",
        "instruction": "Function as the automated RBAC system. The temporary 'engineering-prod-access' role assigned to Mason Wright has reached its expiration. Accordingly, you should withdraw the role and inform him.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "mwright"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-prod-access"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-025",
                    "role_id": "ROL-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-025",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-003 removed from user U-025."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "mason.wright@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Temporary Access Revoked",
                    "text_content": "Your temporary access role 'engineering-prod-access' has expired and has been revoked."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-025"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-025\", \"roles\": [\"engineering-base\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_053",
        "instruction": "Take on the role of Sophia Rodriguez, marketing lead. Your task is to examine and sanction the pending access request AR-021 for provisional access to the 'marketing-content-editor' role, essential for a cross-departmental initiative. The access should conclude in 60 days.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Rodriguez"
                },
            },
            {
                "name": "GetAccessRequestDetails",
                "arguments": {
                    "request_id": "AR-021"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-021",
                    "status": "APPROVED",
                    "reviewed_by": "U-002"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-021 granted by user U-002."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-026",
                    "role_id": "ROL-010",
                    "assigned_by": "U-002",
                    "expires_on": "2025-10-07T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-010 added to user U-026."
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "user_id": "U-026"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "sophie.turner@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Access Request Approved",
                    "text_content": "Your access request (AR-021) has been approved."
                },
            },
            {
                "name": "GetHubspotTicketsByRequester",
                "arguments": {
                    "requester_id": "U-026"
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-023",
                    "status": "CLOSED",
                    "note": "Access request AR-021 has been approved."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-021\", \"status\": \"APPROVED\"",
                "\"user_id\": \"U-026\", \"roles\": [\"marketing-base\", \"marketing-campaign-manager\", \"marketing-content-editor\"]",
                "\"ticket_id\": \"TI-023\", \"status\": \"CLOSED\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_054",
        "instruction": "Execute the functions of the automated RBAC system. A HIGH severity SIEM alert (ALRT-005) has been identified due to an unauthorized access attempt by Sophia Rodriguez on the 'production-web-server-1'. You are required to carry out the appropriate responses.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "edavis"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-002",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-002 status changed to SUSPENDED by user U-031."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-002"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-002",
                    "role_id": "ROL-006"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-006 removed from user U-002."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-lead"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-002",
                    "role_id": "ROL-035"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-035 removed from user U-002."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Security Incident",
                    "description": "User Sophia Rodriguez (edavis) account suspended due to unauthorised access attempt on production-web-server-1.",
                    "requester_id": "U-031",
                    "category": "Security incident",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-002"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-002\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-002\", \"roles\": []",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_055",
        "instruction": "Occupy the position of Olivia Lee. In compliance with the new policies, ensure that all users within your department are equipped with MFA.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Olivia",
                    "last_name": "Anderson"
                },
            },
            {
                "name": "GetUsersByDepartment",
                "arguments": {
                    "department": "Finance"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-024",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-006",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-024",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-024 by user U-006."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "chloe.scott@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "MFA Enabled on Your Account",
                    "text_content": "Multi-factor authentication (MFA) has been enabled on your account."
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-030",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-006",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-030",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-030 by user U-006."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "aria.hill@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "MFA Enabled on Your Account",
                    "text_content": "Multi-factor authentication (MFA) has been enabled on your account."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-024\", \"mfa_enabled\": true",
                "\"user_id\": \"U-030\", \"mfa_enabled\": true"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_056",
        "instruction": "You are Mason Martinez, Engineering Lead. William Thompson requires the temporary role 'hotfix-deployment-override' for an urgent deployment on the 'customer-facing-api' for the next 8h. The role is described as 'Temporary override for hotfix deployment'. Handle the necessary permissions setup. Establish a permission 'admin-access-customer-facing-api' (description: 'Allows admin access to customer API') for the new role.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "wthompson"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "customer-facing-api"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "admin-access-customer-facing-api",
                    "resource_id": "RES-005",
                    "description": "Allows admin access to customer API"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "PERMISSION_CREATED",
                    "target_id": "P-113",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-113 created by user U-001."
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "hotfix-deployment-override",
                    "description": "Temporary override for hotfix deployment.",
                    "is_temporary": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-001."
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-113"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-113 assigned to role ROL-043."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-043",
                    "assigned_by": "U-001",
                    "expires_on": "2025-08-08T17:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-007."
                }
            }
        ],
        "outputs": [
                "\"role_id\": \"ROL-043\"",
                "\"assigned_user\": \"U-007\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_057",
        "instruction": "You are Noah Thompson, the Operations Lead. Results from the investigation into SIEM alert TI-053 involving Sophia Thompson have determined it was a false positive. You must reactivate her account and finalize the investigation ticket TI-053 with the note: 'Investigation complete. Account reactivated.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Rodriguez"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "staylor"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-004",
                    "status": "ACTIVE"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-004",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-004 status changed to 'ACTIVE' by user U-005."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "sophia.Thompson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Account Reactivated",
                    "text_content": "Your account has been reactivated and your access has been restored."
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-053",
                    "status": "CLOSED",
                    "note": "Investigation complete. Account reactivated."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-004\", \"status\": \"ACTIVE\"",
                "\"ticket_id\": \"TI-053\", \"status\": \"CLOSED\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_058",
        "instruction": "You are Olivia Lee, Finance Lead. Due to a recent audit, you are required to create two new permissions, 'view-expense-reports' (description: 'Allows viewing of all expense reports') and 'approve-expense-report' (description: 'Allows approving submitted expense reports'), for the 'expense-reporting-tool' resource. Assign both permissions to the current 'finance-read' role.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Olivia",
                    "last_name": "Anderson"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "expense-reporting-tool"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "view-expense-reports",
                    "resource_id": "RES-036",
                    "description": "Allows viewing of all expense reports"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_CREATED",
                    "target_id": "P-113",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-113 created by user U-006."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-read"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-030",
                    "permission_id": "P-113"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-030",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-113 assigned to role ROL-030."
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "approve-expense-report",
                    "resource_id": "RES-036",
                    "description": "Allows approving submitted expense reports"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_CREATED",
                    "target_id": "P-114",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-114 created by user U-006."
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-030",
                    "permission_id": "P-114"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-006",
                    "action_type": "PERMISSION_ASSIGNED",
                    "target_id": "ROL-030",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-114 assigned to role ROL-030."
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-030"
                }
            }
        ],
        "outputs": [
                "\"role_id\": \"ROL-030\", \"permissions\": [\"P-075\", \"P-083\", \"P-085\", \"P-113\", \"P-114\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_059",
        "instruction": "You are Olivia Lee, Finance Lead. Transfer ownership of the 'general-ledger-db' to your colleague Mia Robinson (access request justification: 'Assuming ownership of general-ledger-db'). She will also need the 'finance-budget-admin' role to oversee the resource. Obtain approval for this lead role assignment from the Operations Lead.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Olivia",
                    "last_name": "Anderson"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mia",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "general-ledger-db"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-031",
                    "new_owner_id": "U-018"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-006",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-031",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-031 transferred from user U-006 to U-018."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-budget-admin"
                },
            },
            {
                "name": "CreateAccessRequest",
                "arguments": {
                    "user_id": "U-018",
                    "requested_role_id": "ROL-032",
                    "justification": "Assuming ownership of general-ledger-db"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-018",
                    "action_type": "ACCESS_REQUEST_CREATED",
                    "target_id": "AR-042",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-042 created by user U-018."
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "username": "mrobinson",
                    "channel": "#access-requests",
                    "message": "Access request AR-042 for resource RES-031 has been created by user U-018. Please review."
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Access Request",
                    "description": "Access request AR-042: Role ROL-032 for mrobinson (U-018).",
                    "requester_id": "U-018",
                    "category": "Access Management",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-042",
                    "status": "APPROVED",
                    "reviewed_by": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-042",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-042 granted by user U-005."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-018",
                    "role_id": "ROL-032",
                    "assigned_by": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-018",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-032 added to user U-018."
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-054",
                    "status": "CLOSED",
                    "note": "Access request AR-042 has been approved."
                }
            }
        ],
        "outputs": [
                "\"resource_id\": \"RES-031\", \"owner_id\": \"U-018\"",
                "\"user_id\": \"U-018\", \"roles\": [\"finance-base\", \"finance-audit-access\", \"finance-budget-admin\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_060",
        "instruction": "You are Emma Martinez, HR Lead. User Alexander Clark has departed the company. You are required to handle his offboarding process.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Emma",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "aclark"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-009",
                    "status": "DISABLED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-009",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-009 status changed to 'DISABLED' by user U-010."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-009"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "sales-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-009",
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-011 removed from user U-009."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "sales-crm-access"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-009",
                    "role_id": "ROL-012"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-012 removed from user U-009."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "sales-lead-manager"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-009",
                    "role_id": "ROL-013"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-013 removed from user U-009."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "sales-lead"
                },
            },
            {
                "name": "GetResourcesByOwner",
                "arguments": {
                    "owner_id": "U-009"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Offboard employee Alexander Clark (aclark)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "requester_id": "U-010",
                    "category": "Offboarding",
                    "assignee_id": "U-003"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-009\", \"status\": \"DISABLED\"",
                "\"user_id\": \"U-009\", \"roles\": []"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_061",
        "instruction": "You are Emma Martinez, HR Lead. Employee Aiden Harris has been terminated. It's necessary to handle his offboarding, which includes account deactivation, revocation of his 'sales-base' role, and creation of a ticket addressed to his manager, Noah Martinez, for tracking the recovery of company assets. The subject of the ticket should be 'Offboarding for Aiden Harris (amoore)' and the description 'Complete asset recovery for terminated employee.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Emma",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "amoore"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-027",
                    "status": "DISABLED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-027",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-027 status changed to DISABLED by user U-010."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "sales-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-027",
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-027",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-011 removed from user U-027."
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Offboarding for Aiden Wilson (amoore)",
                    "description": "Complete asset recovery for terminated employee.",
                    "requester_id": "U-010",
                    "category": "Offboarding",
                    "assignee_id": "U-003"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-027\", \"status\": \"DISABLED\"",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_062",
        "instruction": "You are Mason Martinez, Engineering Lead. You are required to decline the pending access request AR-027 from William Thompson for the 'engineering-code-commit' role. The reason for the rejection is 'This level of access is no longer required for your current project.' Make sure to notify the user via email.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetAccessRequestDetails",
                "arguments": {
                    "request_id": "AR-027"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "wthompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-027",
                    "status": "REJECTED",
                    "reviewed_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ACCESS_REJECTED",
                    "target_id": "AR-027",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-027 rejected by user U-001."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "william.thompson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Access Request Rejected",
                    "text_content": "Your access request (AR-027) has been rejected for the following reason: This level of access is no longer required for your current project."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-027\", \"status\": \"REJECTED\"",
                "\"email_id\": \"EM-016\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_063",
        "instruction": "You are Noah Thompson, Operations Lead. You need to coordinate the creation of a new resource, 'disaster-recovery-plan', with 'CRITICAL' criticality, assigning ownership to yourself. At the same time, establish a new role 'disaster-recovery-viewer' (description: 'Disaster recovery plan viewer') with the permission 'read-dr-plan' (description: 'Read-only access disaster recovery') to facilitate read-only access to this new resource. Assign Jeffrey Allen the new role.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateResource",
                "arguments": {
                    "name": "disaster-recovery-plan",
                    "owner_id": "U-005",
                    "criticality": "CRITICAL"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "RESOURCE_CREATED",
                    "target_id": "RES-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Resource RES-043 created by user U-005."
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "read-dr-plan",
                    "resource_id": "RES-043",
                    "description": "Read-only access disaster recovery"
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "disaster-recovery-viewer",
                    "description": "Disaster recovery plan viewer"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-005."
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-113"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Jeffrey",
                    "last_name": "Allen"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-023",
                    "role_id": "ROL-043",
                    "assigned_by": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-023",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-023."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-023"
                }
            }
        ],
        "outputs": [
                "\"resource_id\": \"RES-043\"",
                "\"role_id\": \"ROL-043\"",
                "\"permission_id\": \"P-113\"",
                "\"user_id\": \"U-023\", \"roles\": [\"operations-base\",\"operations-incident-response\",\"operations-deployment-admin\",\"disaster-recovery-viewer\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_064",
        "instruction": "You are Noah Thompson, IT Auditor. During a review, it's been identified that William Thompson's temporary 'operations-network-admin' role is redundant. You must initiate the necessary procedures.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "wthompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "engineering-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Early Role Revocation",
                    "description": "User William Thompson (wthompson) has a temporary role (operations-network-admin) that is no longer required and should be revoked.",
                    "requester_id": "U-005",
                    "category": "Access Management",
                    "assignee_id": "U-001"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "operations-network-admin"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-028"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-028 removed from user U-007."
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-054",
                    "status": "CLOSED",
                    "note": "Revocation complete."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "william.thompson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Temporary Access Revoked",
                    "text_content": "Your temporary access role 'operations-network-admin' is no longer required and has been revoked."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-007"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-007\"",
                "\"roles\": [\"engineering-base\",\"engineering-code-commit\",\"engineering-prod-access\"]",
                "\"ticket_id\": \"TI-054\", \"status\": \"CLOSED\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_065",
        "instruction": "You are Mason Martinez, Engineering Lead. For a role cleanup initiative, you must consolidate the 'engineering-qa-test' and 'engineering-db-schema' roles. Merge all permissions and user assignments from these roles into a new, unified role called 'engineering-specialist', with the description 'Consolidated role for QA and DB schema specialists.' Use description '[DEPRECATED] Merged into ROL-043.' for the previous roles.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "engineering-specialist",
                    "description": "Consolidated role for QA and DB schema specialists."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-qa-test"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-db-schema"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-005"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-004"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-018"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-006"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-007"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-009"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "engineering-db-schema"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "engineering-qa-test"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-019",
                    "role_id": "ROL-043",
                    "assigned_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-019."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-019",
                    "role_id": "ROL-004"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-004 removed from user U-019."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-019",
                    "role_id": "ROL-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-005 removed from user U-019."
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-004"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-005"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-004",
                    "permission_id": "P-018"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-005",
                    "permission_id": "P-006"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-005",
                    "permission_id": "P-007"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-005",
                    "permission_id": "P-009"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-004"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-005"
                },
            },
            {
                "name": "UpdateRoleDetails",
                "arguments": {
                    "role_id": "ROL-004",
                    "new_name": "[DEPRECATED]engineering-db-schema",
                    "new_description": "[DEPRECATED] Merged into ROL-043."
                },
            },
            {
                "name": "UpdateRoleDetails",
                "arguments": {
                    "role_id": "ROL-005",
                    "new_name": "[DEPRECATED]engineering-qa-test",
                    "new_description": "[DEPRECATED] Merged into ROL-043."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_UPDATED",
                    "target_id": "ROL-004",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-004 has been updated. name=[[DEPRECATED]engineering-db-schema] | description=[[DEPRECATED] Merged into ROL-043.]"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_UPDATED",
                    "target_id": "ROL-005",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-005 has been updated. name=[[DEPRECATED]engineering-qa-test] | description=[[DEPRECATED] Merged into ROL-043.]"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-019"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-019\"",
                "\"roles\": [\"engineering-base\", \"engineering-specialist\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_066",
        "instruction": "You are Noah Thompson, IT Auditor. A compliance review has identified that Victoria Lee in Finance holds the 'finance-invoice-processor' role, creating a Separation of Duties (SoD) conflict with her primary responsibilities. Manage the situation according to policy and utilize 'Revoked conflicting role finance-invoice-processor from user vlee.' for the ticket.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "vlee"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-invoice-processor"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-012",
                    "role_id": "ROL-031"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-012",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-031 removed from user U-012."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "SoD Violation",
                    "description": "Revoked conflicting role finance-invoice-processor from user vlee.",
                    "requester_id": "U-005",
                    "category": "Compliance",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-012"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-012\"",
                "\"roles\": [\"finance-base\", \"finance-budget-admin\"]",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_067",
        "instruction": "You are Sophia Thompson, HR Lead. Logan Scott is transitioning from Sales to Marketing. Update his user profile accordingly. He requires the 'marketing-base' role for his new assignment.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "lhall"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-021"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserDepartment",
                "arguments": {
                    "user_id": "U-021",
                    "department": "Marketing"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "USER_DEPARTMENT_CHANGE",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-021 department changed to Marketing by user U-004."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "sales-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-021",
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-011 removed from user U-021."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "sales-lead-manager"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-021",
                    "role_id": "ROL-013"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-013 removed from user U-021."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "sales-reporting"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-021",
                    "role_id": "ROL-014"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-014 removed from user U-021."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-base"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-021",
                    "role_id": "ROL-006",
                    "assigned_by": "U-004"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-006 added to user U-021."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-021"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "logan.Scott@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Welcome to the Marketing Team!",
                    "text_content": "Welcome, Logan! Your system access has been updated for your new role in the Marketing department."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-021\", \"department\": \"Marketing\"",
                "\"roles\": [\"marketing-base\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_068",
        "instruction": "You are Noah Thompson, Operations Lead. A critical incident necessitates prompt, high-level intervention. Set up a new temporary role 'critical-incident-commander' with description 'Full administrative access for critical incident response', and assign it to yourself for the next 4 hours.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "critical-incident-commander",
                    "description": "Full administrative access for critical incident response",
                    "is_temporary": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-005."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-005",
                    "role_id": "ROL-043",
                    "assigned_by": "U-005",
                    "expires_on": "2025-08-08T13:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-005",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-005."
                }
            }
        ],
        "outputs": [
                "\"role_id\": \"ROL-043\"",
                "\"assigned_user\": \"U-005\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_069",
        "instruction": "You are Mia Robinson from the Finance department. For completing a one-time vendor payment, you require a policy exception for the 'approve-invoice' permission (P-078) on the 'invoicing-system' resource for 48 hours. The justification is 'One-time vendor payment approval required'. Send our Manager, Olivia Lee, an e-mail with subject 'Policy Exception Review Request' and content 'Please review approve my policy exception request (PE-021).' so that she will approve it.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mia",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePolicyException",
                "arguments": {
                    "user_id": "U-018",
                    "permission_id": "P-078",
                    "reason": "One-time vendor payment approval required",
                    "expires_on": "2025-08-10T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-018",
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "target_id": "PE-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Policy exception PE-021 requested by user U-018."
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Olivia",
                    "last_name": "Lee"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "olivia.Lee@sigmatech.com",
                    "sender": "mia.robinson@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Policy Exception Review Request",
                    "text_content": "Please review approve my policy exception request (PE-021)."
                },
            },
            {
                "name": "ApprovePolicyException",
                "arguments": {
                    "exception_id": "PE-021",
                    "reviewed_by": "U-006"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-006",
                    "action_type": "POLICY_EXCEPTION_APPROVED",
                    "target_id": "PE-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Policy exception PE-021 approved by user U-006."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "mia.robinson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Policy Exception Granted",
                    "text_content": "Policy exception for permission 'approve-invoice' granted. Expiration: 2025-08-10T09:56:15Z."
                }
            }
        ],
        "outputs": [
                "\"exception_id\": \"PE-021\", \"status\": \"ACTIVE\"",
                "\"email_id\": \"EM-016\"",
                "\"email_id\": \"EM-017\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_070",
        "instruction": "You are the automated certification bot. Initiate the quarterly access certification for the 'production-web-server-1' resource. Assign the task to the operations lead.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "CERTIFICATION_BOT"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "production-web-server-1"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateCertification",
                "arguments": {
                    "reviewer_id": "U-005",
                    "resource_id": "RES-025",
                    "due_date": "2025-09-08T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-033",
                    "action_type": "CERTIFICATION_CREATED",
                    "target_id": "C-024",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Certification C-024 requested by user U-033."
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "username": "CERTIFICATION_BOT",
                    "channel": "#certifications",
                    "message": "A new certification C-024 for resource RES-025 has been requested. Due date 2025-09-08T09:56:15Z"
                }
            }
        ],
        "outputs": [
                "\"certification_id\": \"C-024\", \"status\": \"PENDING\"",
                "\"message_id\": \"SL-042\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_071",
        "instruction": "You are Noah Thompson, Operations Lead. Under a new security directive, it is necessary for you to enforce MFA across the entire Sales department.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetUsersByDepartment",
                "arguments": {
                    "department": "Sales"
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-021",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-021 by user U-005."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "logan.Scott@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "MFA Enabled on Your Account",
                    "text_content": "Multi-factor authentication (MFA) has been enabled on your account."
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-027",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-027",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-027 by user U-005."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "aiden.Wilson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "MFA Enabled on Your Account",
                    "text_content": "Multi-factor authentication (MFA) has been enabled on your account."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-003\", \"mfa_enabled\": true",
                "\"user_id\": \"U-009\", \"mfa_enabled\": true",
                "\"user_id\": \"U-015\", \"mfa_enabled\": true",
                "\"user_id\": \"U-021\", \"mfa_enabled\": true",
                "\"user_id\": \"U-027\", \"mfa_enabled\": true"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_072",
        "instruction": "You are the automated RBAC system. As part of the regular quarterly cleanup, identify and deactivate all user accounts that have shown inactivity since May 1st, 2025.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListInactiveUsers",
                "arguments": {
                    "inactive_since": "2025-05-01T00:00:00Z"
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-028",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-028",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-028 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-030",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-030",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-030 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-018",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-018",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-018 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-025",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-025",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-025 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-003",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-003",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-003 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-010",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-010",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-010 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-015",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-015",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-015 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-014",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-014 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-023",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-023",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-023 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-007",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-007 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-020",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-020",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-020 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-001",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-001",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-001 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-011",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-011",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-011 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-031",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-031",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-031 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-029",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-029",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-029 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-013",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-013",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-013 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-026",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-026 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-008",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-008",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-008 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-006",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-006",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-006 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-033",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-033",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-033 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-032",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-032",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-032 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-027",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-027",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-027 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-016",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-016",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-016 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-022",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-022",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-022 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-012",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-012",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-012 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-021",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-021 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-004",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-004",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-004 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-002",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-002 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-009",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-009",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-009 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-017",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-017",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-017 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-024",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-024",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-024 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-005",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-005",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-005 status changed to 'SUSPENDED' by user U-031."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-019",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-019 status changed to 'SUSPENDED' by user U-031."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-028\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-030\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-018\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-025\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-003\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-010\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-015\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-014\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-023\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-007\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-020\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-001\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-011\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-031\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-029\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-013\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-026\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-008\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-006\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-033\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-032\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-027\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-016\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-022\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-012\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-021\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-004\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-002\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-009\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-017\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-024\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-005\", \"status\": \"SUSPENDED\"",
                "\"user_id\": \"U-019\", \"status\": \"SUSPENDED\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_073",
        "instruction": "You are Mason Martinez, Engineering Lead. Due to an urgent database migration, you must provide Nathan Thompson with the 'admin-db-cluster' permission (description: 'Temporary permission for emergency migration') for the 'database-cluster-primary' for a duration of 24 hours. This is a special measure with the reason 'Emergency database migration'.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "nwhite"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "database-cluster-primary"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "admin-db-cluster",
                    "resource_id": "RES-026",
                    "description": "Temporary permission for emergency migration"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "PERMISSION_CREATED",
                    "target_id": "P-113",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Permission P-113 created by user U-001."
                },
            },
            {
                "name": "CreatePolicyException",
                "arguments": {
                    "user_id": "U-013",
                    "permission_id": "P-113",
                    "reason": "Emergency database migration",
                    "expires_on": "2025-08-09T09:56:15Z"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "POLICY_EXCEPTION_REQUESTED",
                    "target_id": "PE-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Policy exception PE-021 requested by user U-001"
                },
            },
            {
                "name": "ApprovePolicyException",
                "arguments": {
                    "exception_id": "PE-021",
                    "reviewed_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "POLICY_EXCEPTION_APPROVED",
                    "target_id": "PE-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Policy exception PE-021 approved by user U-001."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "nathan.Thompson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Policy Exception Granted",
                    "text_content": "Policy exception for permission 'admin-db-cluster' granted. Expiration: 2025-08-09T09:56:15Z."
                }
            }
        ],
        "outputs": [
                "\"exception_id\": \"PE-021\", \"status\": \"ACTIVE\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_074",
        "instruction": "You are Emma Martinez, HR Lead. Following the resignation of Olivia Lee, the Finance Lead, you need to start her offboarding process.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Emma",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Olivia",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-006",
                    "status": "DISABLED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-006",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-006 status changed to DISABLED by user U-010."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-006",
                    "role_id": "ROL-029"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-006",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-029 removed from user U-006."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-lead"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-006",
                    "role_id": "ROL-039"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-006",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-039 removed from user U-006."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Offboard employee Olivia Lee (oanderson)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "requester_id": "U-010",
                    "category": "Offboarding",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-006"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-006\", \"status\": \"DISABLED\"",
                "\"user_id\": \"U-006\", \"roles\": []",
                "\"ticket_id\": \"TI-054\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_075",
        "instruction": "You are Ethan Johnson from the Sales team. To work on a joint project, you need the 'marketing-campaign-manager' role for the 'social-media-platform' using the justification 'Requires campaign manager access for joint sales-marketing project.'. Your request must be approved by your manager, Alexander Clark, (status: 'MANAGER_APPROVED') and subsequently by the Marketing Lead, Sophia Thompson. (status: 'APPROVED')",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Ethan",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Clark"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "social-media-platform"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-campaign-manager"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateAccessRequest",
                "arguments": {
                    "user_id": "U-015",
                    "requested_role_id": "ROL-007",
                    "resource_id": "RES-008",
                    "justification": "Requires campaign manager access for joint sales-marketing project."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-015",
                    "action_type": "ACCESS_REQUEST_CREATED",
                    "target_id": "AR-042",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-042 created by user U-015."
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "username": "ebrown",
                    "channel": "#access-requests",
                    "message": "Access request AR-042 for resource RES-008 has been created by user U-015. Please review."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "marketing-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Access Request",
                    "description": "Access request AR-042: Role ROL-007 for ebrown (U-015).",
                    "requester_id": "U-015",
                    "category": "Access Management",
                    "assignee_id": "U-009"
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-042",
                    "status": "MANAGER_APPROVED",
                    "reviewed_by": "U-009"
                },
            },
            {
                "name": "UpdateHubspotTicketAssignee",
                "arguments": {
                    "ticket_id": "TI-054",
                    "new_assignee_id": "U-002"
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-042",
                    "status": "APPROVED",
                    "reviewed_by": "U-002"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-042",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-042 granted by user U-002."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-015",
                    "role_id": "ROL-007",
                    "assigned_by": "U-002"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-015",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-007 added to user U-015."
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-054",
                    "status": "CLOSED",
                    "note": "Access request AR-042 has been approved"
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-042\", \"status\": \"APPROVED\"",
                "\"ticket_id\": \"TI-054\", \"status\": \"CLOSED\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_076",
        "instruction": "As Sophia Thompson, HR Lead, handle the offboarding process for Marketing employee Sophie Turner, who has resigned.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophie",
                    "last_name": "Turner"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-026",
                    "status": "DISABLED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-026 status changed to DISABLED by user U-004."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-026"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-026",
                    "role_id": "ROL-006"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-006 removed from user U-026."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-campaign-manager"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-026",
                    "role_id": "ROL-007"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-007 removed from user U-026."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-content-editor"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-026",
                    "role_id": "ROL-010"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-010 removed from user U-026."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "marketing-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Offboard employee Sophie Turner (sturner)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked.",
                    "requester_id": "U-004",
                    "category": "Offboarding",
                    "assignee_id": "U-002"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-026\", \"status\": \"DISABLED\"",
                "\"user_id\": \"U-026\", \"roles\": []"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_077",
        "instruction": "Being Emma Martinez from Human Resources, you need to update Ava Martinez's profile after her marriage, changing her last name to 'Smith', and ensure her new username and email address are correctly adjusted.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Emma",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserDetails",
                "arguments": {
                    "user_id": "U-016",
                    "new_username": "lsmith",
                    "new_email": "Ava.smith@sigmatech.com"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "USERNAME_CHANGED",
                    "target_id": "U-016",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Username for user U-016 changed to 'lsmith' by user U-010."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "USER_EMAIL_CHANGED",
                    "target_id": "U-016",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Email address for user U-016 changed to 'Ava.smith@sigmatech.com' by user U-010."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "Ava.smith@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Your User Profile Has Been Updated",
                    "text_content": "This is a notification that your accounts details have been updated. Please review the changed information and report any inconsistencies to Human Ressources."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-016\", \"username\": \"lsmith\", \"email\": \"Ava.smith@sigmatech.com\"",
                "\"email_id\": \"EM-016\", \"status\": \"sent\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_078",
        "instruction": "You, Mia Robinson, a resource owner in the Finance department, must reassign ownership of the 'budgeting-tool' resource to your colleague, Victoria Lee, as you transition to a new role.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mia",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Victoria",
                    "last_name": "Lee"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "budgeting-tool"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-033",
                    "new_owner_id": "U-012"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-018",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-033",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-033 transferred from user U-018 to U-012."
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "budgeting-tool"
                }
            }
        ],
        "outputs": [
                "\"resource_id\": \"RES-033\", \"owner_id\": \"U-012\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_079",
        "instruction": "As the automated RBAC system, you need to address a compliance issue after a scan identified that Victoria Lee's dual roles as 'finance-invoice-processor' and 'finance-budget-admin' violate SoD. Resolve this by revoking the 'finance-invoice-processor'. Use 'Revoked conflicting role 'finance-invoice-processor' from user 'vlee' as per audit finding.' for the ticket content.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "vlee"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-invoice-processor"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-012",
                    "role_id": "ROL-031"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-012",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-031 removed from user U-012."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-012"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "SoD Violation",
                    "description": "Revoked conflicting role 'finance-invoice-processor' from user 'vlee' as per audit finding.",
                    "requester_id": "U-031",
                    "category": "Compliance",
                    "assignee_id": "U-005"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-012\", \"roles\": [\"finance-base\", \"finance-budget-admin\"]",
                "\"ticket_id\": \"TI-054\", \"status\": \"OPEN\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_080",
        "instruction": "As Sophia Thompson, HR Lead, coordinate the update of Noah Martinez's profile as he transfers from Engineering to Operations to become a Network Admin, ensuring he is granted the 'operations-base' and 'operations-network-admin' roles.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Taylor"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "nmartinez"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserDepartment",
                "arguments": {
                    "user_id": "U-019",
                    "department": "Operations"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "USER_DEPARTMENT_CHANGED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-019 department changed to Operations by user U-004."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-019"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-019",
                    "role_id": "ROL-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-001 removed from user U-019."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-db-schema"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-019",
                    "role_id": "ROL-004"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-004 removed from user U-019."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-qa-test"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-019",
                    "role_id": "ROL-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-005 removed from user U-019."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "operations-base"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-019",
                    "role_id": "ROL-021",
                    "assigned_by": "U-004"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-021 added to user U-019."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "operations-network-admin"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-019",
                    "role_id": "ROL-028",
                    "assigned_by": "U-004"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-004",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-028 added to user U-019."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "noah.martinez@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Welcome to the Operations Team!",
                    "text_content": "Welcome, Noah! Your system access has been updated for your new role in the Operations department."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-019\", \"department\": \"Operations\"",
                "\"user_roles\": [\"operations-base\", \"operations-network-admin\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_081",
        "instruction": "You are Oliver Lewis. It is imperative that all active users in the Marketing department without MFA must have it enabled without delay.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Lewis"
                },
            },
            {
                "name": "GetUsersByDepartment",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-002",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-002 by user U-029."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "Sophia.Rodriguez@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "MFA Enabled on Your Account",
                    "text_content": "Multi-factor authentication (MFA) has been enabled on your account."
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-014",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-014 by user U-029."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "madison.Johnson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "MFA Enabled on Your Account",
                    "text_content": "Multi-factor authentication (MFA) has been enabled on your account."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-002\", \"mfa_enabled\": true",
                "\"user_id\": \"U-014\", \"mfa_enabled\": true"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_082",
        "instruction": "You are Oliver Lewis, an IT Auditor. A compliance review has uncovered that Benjamin Wilson, whose account status is 'DISABLED', still retains ownership of certain resources. Coordinate the transfer of these resources' ownership to the current operations lead and eliminate any roles Benjamin may still occupy. Initiate an audit remediation ticket if any are identified.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Lewis"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "bharris"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetResourcesByOwner",
                "arguments": {
                    "owner_id": "U-011"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "database-cluster-primary"
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-026",
                    "new_owner_id": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-026 transferred from user U-011 to U-005."
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "log-management-system"
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-029",
                    "new_owner_id": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-029",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-029 transferred from user U-011 to U-005."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-011"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "operations-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-011",
                    "role_id": "ROL-021"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-011",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-021 removed from user U-011."
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Audit Remediation",
                    "description": "Revoked redundant role 'operations-base' from user 'bharris' as per audit finding.",
                    "requester_id": "U-029",
                    "category": "Compliance",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-011"
                }
            }
        ],
        "outputs": [
                "\"resource_id\": \"RES-026\", \"owner_id\": \"U-005\"",
                "\"resource_id\": \"RES-029\", \"owner_id\": \"U-005\"",
                "\"user_id\": \"U-011\", \"roles\": []",
                "\"ticket_id\": \"TI-054\", \"status\": \"OPEN\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_083",
        "instruction": "You are Mason Martinez, Engineering Lead. Your task is to merge the 'engineering-qa-test' and 'engineering-code-commit' roles into a new 'engineering-developer-advanced' role. The new role's description is 'Advanced developer role with QA and code commit privileges.'. Ensure that all users and permissions from the existing roles are transferred to the new one.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "engineering-developer-advanced",
                    "description": "Advanced developer role with QA and code commit privileges."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-001."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-qa-test"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-code-commit"
                },
            },
            {
                "name": "MergeAndDeprecateRole",
                "arguments": {
                    "source_role_id": "ROL-005",
                    "target_role_id": "ROL-043",
                    "actor_id": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_MERGED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-005 merged into ROL-043."
                },
            },
            {
                "name": "MergeAndDeprecateRole",
                "arguments": {
                    "source_role_id": "ROL-002",
                    "target_role_id": "ROL-043",
                    "actor_id": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ROLE_MERGED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-002 merged into ROL-043."
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-043"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "engineering-developer-advanced"
                }
            }
        ],
        "outputs": [
                "\"role_id\": \"ROL-043\"",
                "\"permissions_migrated\": 4",
                "\"users_reassigned\": 2"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_084",
        "instruction": "You are Oliver Lewis, an IT Auditor. A quarterly review has shown that the 'sales-commission-view' role is obsolete and must be phased out. Follow the prescribed steps in policy and alter the deprecated role's description to '[DEPRECATED] Role is no longer in use and is scheduled for deletion.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Lewis"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "sales-commission-view"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "sales-commission-view"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-015"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-015",
                    "permission_id": "P-044"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-015"
                },
            },
            {
                "name": "UpdateRoleDetails",
                "arguments": {
                    "role_id": "ROL-015",
                    "new_name": "[DEPRECATED]sales-commission-view",
                    "new_description": "[DEPRECATED] Role is no longer in use and is scheduled for deletion."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "ROLE_UPDATED",
                    "target_id": "ROL-015",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-015 has been updated. name=[[DEPRECATED]sales-commission-view] | description=[[DEPRECATED] Role is no longer in use and is scheduled for deletion.]"
                }
            }
        ],
        "outputs": [
                "\"role_id\": \"ROL-015\", \"status\": \"updated\"",
                "\"role_id\": \"ROL-015\", \"permissions\": []"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_085",
        "instruction": "You are the automated RBAC system. Detection shows that the temporary role 'finance-audit-access' assigned to user Mia Robinson has lapsed. Manage this as outlined in the policy.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "mrobinson"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-audit-access"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-018",
                    "role_id": "ROL-033"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-018",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-033 removed from user U-018."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "mia.robinson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Temporary Access Revoked",
                    "text_content": "Your temporary access role 'finance-audit-access' has expired and has been revoked."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-018"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-018\", \"roles\": [\"finance-base\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_086",
        "instruction": "You are Mason Martinez, Engineering Lead. It is essential to decline the access request AR-024 that you submitted because it was mistakenly created.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Martinez"
                },
            },
            {
                "name": "GetAccessRequestDetails",
                "arguments": {
                    "request_id": "AR-024"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-024",
                    "status": "REJECTED",
                    "reviewed_by": "U-001"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-001",
                    "action_type": "ACCESS_REJECTED",
                    "target_id": "AR-024",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-024 rejected by user U-001."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "Mason.martinez@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Access Request Rejected",
                    "text_content": "Your access request (AR-024) has been rejected for the following reason: Created in error."
                },
            },
            {
                "name": "GetHubspotTicketsByRequester",
                "arguments": {
                    "requester_id": "U-001"
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-026",
                    "status": "CLOSED",
                    "note": "Access request AR-024 has been denied. Reason: Created in error."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-024\", \"status\": \"REJECTED\"",
                "\"ticket_id\": \"TI-026\", \"status\": \"CLOSED\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_087",
        "instruction": "You are Noah Martinez, Sales Lead. A 'sales-forecasting-tool' resource with 'HIGH' criticality needs to be established under your ownership. Additionally, create a new role 'sales-forecaster' with the permission 'read-forecast-data' for this resource, allowing it to be assigned to your team members, Ethan Johnson and Logan Scott.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Ethan",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Scott"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateResource",
                "arguments": {
                    "name": "sales-forecasting-tool",
                    "owner_id": "U-003",
                    "criticality": "HIGH"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "RESOURCE_CREATED",
                    "target_id": "RES-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Resource RES-043 created by user U-003."
                },
            },
            {
                "name": "CreateRoleWithPermission",
                "arguments": {
                    "role_name": "sales-forecaster",
                    "resource_id": "RES-043",
                    "permission_name": "read-forecast-data"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-003."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-015",
                    "role_id": "ROL-043",
                    "assigned_by": "U-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-015",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-015."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-021",
                    "role_id": "ROL-043",
                    "assigned_by": "U-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-021."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-015"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-021"
                }
            }
        ],
        "outputs": [
                "\"resource_id\": \"RES-043\"",
                "\"role_id\": \"ROL-043\"",
                "\"user_id\": \"U-015\", \"roles\": [\"sales-base\", \"sales-forecaster\"]",
                "\"user_id\": \"U-021\", \"roles\": [\"sales-base\", \"sales-lead-manager\", \"sales-reporting\", \"sales-forecaster\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_088",
        "instruction": "You are Noah Martinez, Sales Lead. You must decline access request AR-040 from Madison Martinez as she lacks authorization for accessing analytics data (reason: 'Not authorised').",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetAccessRequestDetails",
                "arguments": {
                    "request_id": "AR-040"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "mjackson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-040",
                    "status": "REJECTED",
                    "reviewed_by": "U-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ACCESS_REJECTED",
                    "target_id": "AR-040",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-040 rejected by user U-003."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "madison.Martinez@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Access Request Rejected",
                    "text_content": "Your access request (AR-040) has been rejected for the following reason: Not authorised."
                },
            },
            {
                "name": "GetHubspotTicketsByRequester",
                "arguments": {
                    "requester_id": "U-014"
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-042",
                    "status": "CLOSED",
                    "note": "Access request AR-040 has been denied. Reason: Not authorised."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-040\", \"status\": \"REJECTED\"",
                "\"ticket_id\": \"TI-042\", \"status\": \"CLOSED\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_089",
        "instruction": "You are Emma Martinez, HR Lead. With Charlotte Walker returning from suspension, you need to reactivate her account and assign her the 'marketing-social-media' role to enable her to handle the company's social media activities.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Emma",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "cwalker"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-020",
                    "status": "ACTIVE"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-020",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-020 status changed to 'ACTIVE' by user U-010."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-social-media"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-020",
                    "role_id": "ROL-008",
                    "assigned_by": "U-010"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-020",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-008 added to user U-020."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-020"
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "charlotte.walker@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Account Reactivated",
                    "text_content": "Your account has been reactivated and your access has been restored."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-020\", \"status\": \"ACTIVE\"",
                "\"roles\": [\"marketing-base\", \"marketing-social-media\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_090",
        "instruction": "You are operating as the automated RBAC system. You need to carry out the termination process for employee Lucas Thompson from the Operations department.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "lthompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-017",
                    "status": "DISABLED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-017",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-017 status changed to 'DISABLED' by user U-031."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-017"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "operations-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-017",
                    "role_id": "ROL-021"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-021 removed from user U-017."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "operations-server-monitor"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-017",
                    "role_id": "ROL-022"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-022 removed from user U-017."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "operations-log-viewer"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-017",
                    "role_id": "ROL-024"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-024 removed from user U-017."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Offboard employee Lucas Thompson (lthompson)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "requester_id": "U-031",
                    "category": "Offboarding",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetResourcesByOwner",
                "arguments": {
                    "owner_id": "U-017"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "network-firewall-main"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "monitoring-dashboard-main"
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-027",
                    "new_owner_id": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-027",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-027 transferred from user U-017 to U-005."
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-030",
                    "new_owner_id": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-030",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-030 transferred from user U-017 to U-005."
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "network-firewall-main"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "monitoring-dashboard-main"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-017\", \"status\": \"DISABLED\"",
                "\"user_id\": \"U-017\", \"roles\": []",
                "\"ticket_id\": \"TI-054\", \"status\": \"OPEN\"",
                "\"resource_id\": \"RES-027\", \"owner_id\": \"U-005\"",
                "\"resource_id\": \"RES-030\", \"owner_id\": \"U-005\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_091",
        "instruction": "Your name is Noah Johnson, Sales Lead. The 'sales-base' role will be phased out and substituted with a new, more inclusive 'sales-standard-access' role. The description for the newly introduced role is 'Standard access for all non-lead sales personnel.'. You are responsible for migrating all users from the existing role to the new one and subsequently marking the old role as deprecated with the notation '[DEPRECATED] Merged into ROL-043.'.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Michael",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "sales-standard-access",
                    "description": "Standard access for all non-lead sales personnel."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-003."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "sales-base"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "sales-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-003",
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-003",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-011 removed from user U-003."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-003",
                    "role_id": "ROL-043",
                    "assigned_by": "U-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-003",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-003."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-009",
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-011 removed from user U-009."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-009",
                    "role_id": "ROL-043",
                    "assigned_by": "U-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-009."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-015",
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-015",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-011 removed from user U-015."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-015",
                    "role_id": "ROL-043",
                    "assigned_by": "U-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-015",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-015."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-021",
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-011 removed from user U-021."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-021",
                    "role_id": "ROL-043",
                    "assigned_by": "U-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-021."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-027",
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-027",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-011 removed from user U-027."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-027",
                    "role_id": "ROL-043",
                    "assigned_by": "U-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-027",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-027."
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-011",
                    "permission_id": "P-035"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-011",
                    "permission_id": "P-038"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-011",
                    "permission_id": "P-047"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "UpdateRoleDetails",
                "arguments": {
                    "role_id": "ROL-011",
                    "new_name": "[DEPRECATED]sales-base",
                    "new_description": "[DEPRECATED] Merged into ROL-043."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-003",
                    "action_type": "ROLE_UPDATED",
                    "target_id": "ROL-011",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-011 has been updated. name=[[DEPRECATED]sales-base] | description=[[DEPRECATED] Merged into ROL-043.]"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "sales-standard-access"
                }
            }
        ],
        "outputs": [
                "\"role_id\": \"ROL-043\"",
                "\"permission_id\": \"P-113\"",
                "\"assigned_user\": \"U-010\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_092",
        "instruction": "Your name is Noah Thompson, Operations Lead. You are required to execute a new security policy throughout the company, necessitating that every account in the Engineering and Operations departments must have MFA enabled. Bot accounts associated with these departments are not required to comply with this policy.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Rodriguez"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetUsersByDepartment",
                "arguments": {
                    "department": "Engineering"
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-019",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-019 by user U-005."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "noah.martinez@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "MFA Enabled on Your Account",
                    "text_content": "Multi-factor authentication (MFA) has been enabled on your account."
                },
            },
            {
                "name": "GetUsersByDepartment",
                "arguments": {
                    "department": "Operations"
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-005",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-005",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-005 by user U-005."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "Noah.Thompson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "MFA Enabled on Your Account",
                    "text_content": "Multi-factor authentication (MFA) has been enabled on your account."
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-011",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-011",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-011 by user U-005."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "benjamin.Wilson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "MFA Enabled on Your Account",
                    "text_content": "Multi-factor authentication (MFA) has been enabled on your account."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-019\", \"mfa_enabled\": true",
                "\"user_id\": \"U-005\", \"mfa_enabled\": true",
                "\"user_id\": \"U-011\", \"mfa_enabled\": true"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_093",
        "instruction": "Your name is Emma Martinez, HR Lead. The Sales Lead, Noah Johnson, has been terminated. You are required to handle his offboarding process, which includes disabling his account, revoking all his roles, transferring ownership of all his resources to the Operations Lead, Noah Thompson, and allocating his open tickets to Noah Thompson as well.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Emma",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Michael",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Rodriguez"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-003",
                    "status": "DISABLED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-003",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-003 status changed to 'DISABLED' by user U-010."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-003"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "sales-lead"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "sales-base"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-003",
                    "role_id": "ROL-011"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-003",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-011 removed from user U-003."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-003",
                    "role_id": "ROL-036"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-003",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-036 removed from user U-003."
                },
            },
            {
                "name": "GetResourcesByOwner",
                "arguments": {
                    "owner_id": "U-003"
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-014",
                    "new_owner_id": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-014 transferred from user U-003 to U-005."
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-017",
                    "new_owner_id": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-017",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-017 transferred from user U-003 to U-005."
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-037",
                    "new_owner_id": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-010",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-037",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Ownership for resource RES-037 transferred from user U-003 to U-005."
                },
            },
            {
                "name": "GetHubspotTicketsByAssignee",
                "arguments": {
                    "assignee_id": "U-003"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Offboard employee Noah Johnson (mwilson)",
                    "description": "Complete employee offboarding. User account has been disabled, and roles have been revoked",
                    "requester_id": "U-010",
                    "category": "Offboarding",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-003"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-003\", \"status\": \"DISABLED\"",
                "\"user_id\": \"U-003\", \"roles\": []",
                "\"resource_id\": \"RES-014\", \"owner_id\": \"U-005\"",
                "\"resource_id\": \"RES-017\", \"owner_id\": \"U-005\"",
                "\"resource_id\": \"RES-037\", \"owner_id\": \"U-005\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_094",
        "instruction": "Your name is Noah Thompson, SOC Analyst. A data breach simulation is being executed for the Marketing department. As per the incident response protocol, you are to promptly suspend all active user accounts within that department, withdraw all their roles, and confirm that MFA is enabled on their accounts for future reactivation. The activity of the exercise is being recorded in a new ticket (category: 'Security'), assigned to operations lead, with the subject 'Security Drill: Marketing Department Lockdown' and content 'All user accounts in the Marketing department have been suspended and roles revoked as part of a planned data breach drill.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Noah",
                    "last_name": "Rodriguez"
                },
            },
            {
                "name": "GetUsersByDepartment",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-002"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-014"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-026"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-base"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-lead"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-analytics-read"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-campaign-manager"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-content-editor"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-002",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-002 status changed to 'SUSPENDED' by user U-005."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-002",
                    "role_id": "ROL-006"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-006 removed from user U-002."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-002",
                    "role_id": "ROL-035"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-035 removed from user U-002."
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-002",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-002 by user U-005."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-014",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-014 status changed to 'SUSPENDED' by user U-005."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-014",
                    "role_id": "ROL-006"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-006 removed from user U-014."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-014",
                    "role_id": "ROL-009"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-009 removed from user U-014."
                },
            },
            {
                "name": "UpdateUserMfaStatus",
                "arguments": {
                    "user_id": "U-014",
                    "mfa_enabled": true
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_MFA_ENABLED",
                    "target_id": "U-014",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "MFA enabled for user U-014 by user U-005."
                },
            },
            {
                "name": "UpdateUserStatus",
                "arguments": {
                    "user_id": "U-026",
                    "status": "SUSPENDED"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "User U-026 status changed to 'SUSPENDED' by user U-005."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-026",
                    "role_id": "ROL-006"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-006 removed from user U-026."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-026",
                    "role_id": "ROL-007"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-007 removed from user U-026."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-026",
                    "role_id": "ROL-010"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-010 removed from user U-026."
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Security Drill: Marketing Department Lockdown",
                    "description": "All user accounts in the Marketing department have been suspended and roles revoked as part of a planned data breach drill.",
                    "requester_id": "U-005",
                    "category": "Security",
                    "assignee_id": "U-005"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-002"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-014"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-026"
                }
            }
        ],
        "outputs": [
                "\"ticket_id\": \"TI-054\", \"subject\": \"Security Drill: Marketing Department Lockdown\"",
                "\"user_id\": \"U-002\", \"status\": \"SUSPENDED\", \"mfa_enabled\": true, \"roles\": []",
                "\"user_id\": \"U-014\", \"status\": \"SUSPENDED\", \"mfa_enabled\": true, \"roles\": []",
                "\"user_id\": \"U-026\", \"status\": \"SUSPENDED\", \"mfa_enabled\": true, \"roles\": []"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_095",
        "instruction": "You operate as the automated RBAC system. A compliance audit has detected that Victoria Lee possesses both the 'finance-invoice-processor' and 'finance-budget-admin' roles, constituting an SoD infraction. You need to address this by revoking the 'finance-invoice-processor'.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "vlee"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-invoice-processor"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-012",
                    "role_id": "ROL-031"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-012",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-031 removed from user U-012."
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-012"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-012\", \"roles\": [\"finance-base\", \"finance-budget-admin\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_096",
        "instruction": "As the automated RBAC system, conduct a daily review to identify temporary user role assignments that have outlived their expiration date but weren't de-provisioned automatically. Ensure to handle the revocation for each expired role.",
        "actions": [
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "RBAC_BOT"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "wthompson"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-prod-access"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-007",
                    "role_id": "ROL-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-003 removed from user U-007."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "william.thompson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Temporary Access Revoked",
                    "text_content": "Your temporary access role 'engineering-prod-access' has expired and has been revoked."
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "mrobinson"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "finance-audit-access"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-018",
                    "role_id": "ROL-033"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-018",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-033 removed from user U-018."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "mia.robinson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Temporary Access Revoked",
                    "text_content": "Your temporary access role 'finance-audit-access' has expired and has been revoked."
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "mwright"
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "engineering-prod-access"
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-025",
                    "role_id": "ROL-003"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-025",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-003 removed from user U-025."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "mason.wright@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Temporary Access Revoked",
                    "text_content": "Your temporary access role 'engineering-prod-access' has expired and has been revoked."
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"U-007\", \"role_id\": \"ROL-003\", \"status\": \"revoked\"",
                "\"user_id\": \"U-018\", \"role_id\": \"ROL-033\", \"status\": \"revoked\"",
                "\"user_id\": \"U-025\", \"role_id\": \"ROL-003\", \"status\": \"revoked\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_097",
        "instruction": "In your role as Sophia Thompson, Marketing Lead, address the issue of the 'marketing-campaign-manager' role being too generic by dividing it into two more specific roles. The first is 'marketing-campaign-strategist' (description: 'Develops and oversees marketing campaign strategies.') and the second is 'marketing-campaign-executor' (description: 'Executes and reports on marketing campaigns.'). Efficiently migrate all permissions and users from the original role to the new roles. Assign 'manage-email-lists' to the 'marketing-campaign-executor' role, while allocating everything else to the other role. Adjust the description of the old role to: '[DEPRECATED] Split into ROL-043 and ROL-044.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Sophia",
                    "last_name": "Thompson"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "marketing-campaign-strategist",
                    "description": "Develops and oversees marketing campaign strategies."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-002."
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "marketing-campaign-executor",
                    "description": "Executes and reports on marketing campaigns."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-044",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-044 created by user U-002."
                },
            },
            {
                "name": "GetRoleByName",
                "arguments": {
                    "role_name": "marketing-campaign-manager"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-007"
                },
            },
            {
                "name": "GetPermissionDetails",
                "arguments": {
                    "permission_id": "P-022"
                },
            },
            {
                "name": "GetPermissionDetails",
                "arguments": {
                    "permission_id": "P-024"
                },
            },
            {
                "name": "GetPermissionDetails",
                "arguments": {
                    "permission_id": "P-029"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-022"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-029"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-044",
                    "permission_id": "P-024"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "marketing-campaign-manager"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-026",
                    "role_id": "ROL-043",
                    "assigned_by": "U-002"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-026."
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-026",
                    "role_id": "ROL-044",
                    "assigned_by": "U-002"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-044 added to user U-026."
                },
            },
            {
                "name": "RevokeRole",
                "arguments": {
                    "user_id": "U-026",
                    "role_id": "ROL-007"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-007 removed from user U-026."
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-007"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-007",
                    "permission_id": "P-022"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-007",
                    "permission_id": "P-024"
                },
            },
            {
                "name": "RemovePermissionFromRole",
                "arguments": {
                    "role_id": "ROL-007",
                    "permission_id": "P-029"
                },
            },
            {
                "name": "GetRolePermissions",
                "arguments": {
                    "role_id": "ROL-007"
                },
            },
            {
                "name": "UpdateRoleDetails",
                "arguments": {
                    "role_id": "ROL-007",
                    "new_name": "[DEPRECATED]marketing-campaign-manager",
                    "new_description": "[DEPRECATED] Split into ROL-043 and ROL-044."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-002",
                    "action_type": "ROLE_UPDATED",
                    "target_id": "ROL-007",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-007 has been updated. name=[[DEPRECATED]marketing-campaign-manager] | description=[[DEPRECATED] Split into ROL-043 and ROL-044.]"
                }
            }
        ],
        "outputs": [
                "\"role_id\": \"ROL-043\", \"role_name\": \"marketing-campaign-strategist\"",
                "\"role_id\": \"ROL-044\", \"role_name\": \"marketing-campaign-executor\"",
                "\"user_id\": \"U-026\", \"roles\": [\"marketing-base\", \"marketing-content-editor\", \"marketing-campaign-strategist\", \"marketing-campaign-executor\"]"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_098",
        "instruction": "In your capacity as Olivia Lee, Finance Lead, you have a pending access request (AR-034) from Mia Robinson for the 'finance-read' role. This request must be declined since her current roles suffice in providing the required permissions. Document the rejection rationale as: 'User's existing roles already grant the required permissions.'",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Olivia",
                    "last_name": "Anderson"
                },
            },
            {
                "name": "GetAccessRequestDetails",
                "arguments": {
                    "request_id": "AR-034"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "mrobinson"
                },
            },
            {
                "name": "GetUserRoles",
                "arguments": {
                    "user_id": "U-018"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateAccessRequestStatus",
                "arguments": {
                    "request_id": "AR-034",
                    "status": "REJECTED",
                    "reviewed_by": "U-006"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-006",
                    "action_type": "ACCESS_REJECTED",
                    "target_id": "AR-034",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Access request AR-034 rejected by user U-006."
                },
            },
            {
                "name": "SendEmail",
                "arguments": {
                    "receiver": "mia.robinson@sigmatech.com",
                    "sender": "rbac@sigmatech.com",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "subject": "Access Request Rejected",
                    "text_content": "Your access request (AR-034) has been rejected for the following reason: User's existing roles already grant the required permissions."
                },
            },
            {
                "name": "GetHubspotTicketsByRequester",
                "arguments": {
                    "requester_id": "U-018"
                },
            },
            {
                "name": "UpdateHubspotTicketStatus",
                "arguments": {
                    "ticket_id": "TI-036",
                    "status": "CLOSED",
                    "note": "Access request AR-034 has been denied. Reason: User's existing roles already grant the required permissions."
                }
            }
        ],
        "outputs": [
                "\"request_id\": \"AR-034\", \"status\": \"REJECTED\"",
                "\"ticket_id\": \"TI-036\", \"status\": \"CLOSED\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_099",
        "instruction": "While auditing as Oliver Lewis, you discovered that former staff member Benjamin Wilson, who has been terminated, remains listed as the owner of several resources requiring reassignment per policy. Generate a ticket with the content 'Reassigned ownership of resources from terminated user Benjamin Johnson (bharris) to user drodriguez (U-005)', (subject: 'Audit Remediation', category: 'Compliance') and ensure it is allocated to the new resource owner.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Oliver",
                    "last_name": "Lewis"
                },
            },
            {
                "name": "GetUserByUsername",
                "arguments": {
                    "username": "bharris"
                },
            },
            {
                "name": "GetUsersByRole",
                "arguments": {
                    "role_name": "operations-lead"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "user_id": "U-005"
                },
            },
            {
                "name": "GetResourcesByOwner",
                "arguments": {
                    "owner_id": "U-011"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-026",
                    "new_owner_id": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-026",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Resource RES-026 ownership transferred from U-011 to U-005."
                },
            },
            {
                "name": "UpdateResourceOwner",
                "arguments": {
                    "resource_id": "RES-029",
                    "new_owner_id": "U-005"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-029",
                    "action_type": "RESOURCE_OWNER_CHANGE",
                    "target_id": "RES-029",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Resource RES-029 ownership transferred from U-011 to U-005."
                },
            },
            {
                "name": "CreateHubspotTicket",
                "arguments": {
                    "subject": "Audit Remediation",
                    "description": "Reassigned ownership of resources from terminated user Benjamin Wilson (bharris) to user drodriguez (U-005)",
                    "requester_id": "U-029",
                    "category": "Compliance",
                    "assignee_id": "U-005"
                }
            }
        ],
        "outputs": [
                "\"resource_id\": \"RES-026\", \"owner_id\": \"U-005\"",
                "\"resource_id\": \"RES-029\", \"owner_id\": \"U-005\"",
                "\"ticket_id\": \"TI-054\", \"status\": \"OPEN\""
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "task_100",
        "instruction": "In your position as Lily Martin from Human Resources, manage the provisioning of necessary access for a new cross-functional initiative, 'Project Calypso'. The project team includes Ava Johnson (Human Resources), Logan Scott (Sales), and Mason Wright (Engineering). Establish a new role named 'project-calypso-team' described as 'Provides access for the Project Calypso team.', which should enable access to view the internal wiki, read the dev database, and view the sales reporting dashboard.",
        "actions": [
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Lily",
                    "last_name": "Martin"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Johnson"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Scott"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Wright"
                },
            },
            {
                "name": "GetCurrentTime",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateRole",
                "arguments": {
                    "role_name": "project-calypso-team",
                    "description": "Provides access for the Project Calypso team."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-028",
                    "action_type": "ROLE_CREATED",
                    "target_id": "ROL-043",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 created by user U-028."
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "internal-documentation-wiki"
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "read-wiki",
                    "resource_id": "RES-006",
                    "description": "Read access to internal documentation wiki"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-113"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "dev-database-server"
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "read-dev-db",
                    "resource_id": "RES-007",
                    "description": "Read access to dev database server"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-114"
                },
            },
            {
                "name": "GetResourceByName",
                "arguments": {
                    "name": "sales-reporting-dashboard"
                },
            },
            {
                "name": "CreatePermission",
                "arguments": {
                    "action": "view-sales-report",
                    "resource_id": "RES-015",
                    "description": "View access to sales reporting dashboard"
                },
            },
            {
                "name": "AssignPermissionToRole",
                "arguments": {
                    "role_id": "ROL-043",
                    "permission_id": "P-115"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-016",
                    "role_id": "ROL-043",
                    "assigned_by": "U-028"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-021",
                    "role_id": "ROL-043",
                    "assigned_by": "U-028"
                },
            },
            {
                "name": "GrantRole",
                "arguments": {
                    "user_id": "U-025",
                    "role_id": "ROL-043",
                    "assigned_by": "U-028"
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-028",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-016",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-016."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-028",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-021."
                },
            },
            {
                "name": "WriteAuditLog",
                "arguments": {
                    "actor_id": "U-028",
                    "action_type": "ROLE_GRANTED",
                    "target_id": "U-025",
                    "timestamp": "2025-08-08T09:56:15Z",
                    "details": "Role ROL-043 added to user U-025."
                }
            }
        ],
        "outputs": [
                "\"role_id\": \"ROL-043\"",
                "\"permission_id\": \"P-113\"",
                "\"permission_id\": \"P-114\"",
                "\"permission_id\": \"P-115\""
        ]
    }
]
