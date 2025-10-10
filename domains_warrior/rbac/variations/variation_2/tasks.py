from domains.dto import Action, Task
import json

TASKS = [
    Task(
        annotator="2",
        user_id="task_001",
        instruction=(
            "You are Ashley Wilson from Human Resources. You need to onboard a new engineering intern, John Fairchild, into the Engineering department. He will require the 'engineering-base' and 'engineering-code-commit' roles. Ensure no Separation of Duties conflicts are created and notify the new user's manager upon completion."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(
                name="create_user",
                kwargs={
                    "username": "jfairchild",
                    "email": "john.fairchild@taucorp.com",
                    "department": "Engineering",
                    "status": "ACTIVE",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "New user account created via onboarding workflow.",
                },
            ),

            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-base"}),
            Action(
                name="assign_role_to_user",
                kwargs={"user_id": "U-034", "role_id": "ROL-001", "assigned_by": "U-010"},
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_ASSIGNED", "target_id": "U-034", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role engineering-base (ROL-001) assigned to user jfairchild (U-034) as part of onboarding.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-code-commit"}),
            Action(
                name="assign_role_to_user",
                kwargs={"user_id": "U-034", "role_id": "ROL-002", "assigned_by": "U-010"},
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_ASSIGNED", "target_id": "U-034", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role engineering-code-commit (ROL-002) assigned to user jfairchild (U-034) as part of onboarding.",
                },
            ),

            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "onboarding@taucorp.com", "receiver": "john.fairchild@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi John, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-034"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-001"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "hr-operations@taucorp.com", "receiver": "alex.johnson@taucorp.com",
                    "subject": "Notification: New Direct Report - John Fairchild",
                    "text_content": "Hi Alex, this is an automated notification to inform you that a new employee, John Fairchild, has been onboarded into your department (Engineering). They have been assigned their initial roles. Please follow up with them regarding any additional access needs.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-034",
                "username": "jfairchild",
                "email": "john.fairchild@taucorp.com",
                "department": "Engineering",
                "status": "ACTIVE",
                "roles": ["engineering-base", "engineering-code-commit"],
                "manager_notified": "U-001"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_002",
        instruction=(
            "You are Ashley Wilson from Human Resources. Please process the offboarding for Christopher Rodriguez, who is leaving the company from the Engineering department."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "crodriguez"}),
            Action(
                name="update_user_status",
                kwargs={
                    "user_id": "U-007",
                    "new_status": "DISABLED",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account disabled as part of standard employee offboarding process.",
                },
            ),
            Action(
                name="get_user_roles_by_user_id",
                kwargs={
                    "user_id": "U-007",
                },
            ),
            Action(
                name="revoke_role_from_user",
                kwargs={
                    "user_role_id": "UR-003",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-001 revoked from user crodriguez during offboarding.",
                },
            ),
            Action(
                name="revoke_role_from_user",
                kwargs={
                    "user_role_id": "UR-004",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-002 revoked from user crodriguez during offboarding.",
                },
            ),
            Action(
                name="revoke_role_from_user",
                kwargs={
                    "user_role_id": "UR-005",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-003 revoked from user crodriguez during offboarding.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-007",
                "final_status": "DISABLED",
                "roles_revoked_count": 3
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_003",
        instruction="You are Alex Johnson, Engineering Lead. A compliance scan has flagged that access request AR-003 may violate the access duration policy for CRITICAL resources. Please investigate the access that was granted as a result of this request. If you find that its duration is non-compliant, you must revoke the non-compliant grant and re-issue access with the correct 4-hour expiration.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "ajohnson"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-003"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-018"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-031"}),

            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-052"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001", "action_type": "ROLE_REVOKED", "target_id": "U-018", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Non-compliant access grant (UR-052) revoked to enforce temporary access policy for CRITICAL resources.",
                },
            ),

            Action(
                name="create_access_request",
                kwargs={
                    "user_id": "U-018", "role_id": "ROL-033", "resource_id": "RES-031", "timestamp": "2025-08-09 10:00:00+00:00",
                    "justification": "Re-issuing access with a 4-hour temporary grant per compliance policy for CRITICAL resources.",
                },
            ),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-018"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001", "action_type": "ACCESS_REQUEST_CREATED", "target_id": "AR-042", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-042 created for user sadams (U-018).",
                },
            ),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-006"}),
            Action(
                name="approve_access_request",
                kwargs={
                    "request_id": "AR-042",
                    "reviewer_id": "U-006",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "expires_on": "2025-08-09 14:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ACCESS_GRANTED", "target_id": "AR-042", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Temporary access grant approved for request AR-042 with a 4-hour expiration.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "it-operations@taucorp.com", "receiver": "stephanie.adams@taucorp.com",
                    "subject": "Action Required: Your Access Grant has been Updated",
                    "text_content": "This is an automated notification. The access grant associated with your request AR-003 was found to be non-compliant and has been revoked. It has been replaced with a new temporary 4-hour grant in compliance with the policy for CRITICAL resources. The new temporary access will expire at 2025-08-09 14:00:00+00:00.",
                },
            ),
        ],
        outputs=[json.dumps({"original_request_remediated": "AR-003", "non_compliant_grant_revoked": "UR-052", "new_temporary_request_id": "AR-042", "access_expires_on": "2025-08-09 14:00:00+00:00"})],
    ),
    Task(
        annotator="2",
        user_id="task_004",
        instruction=(
            "You are Michael Davis, IT Operations Manager. You have received a CRITICAL SIEM alert (ALRT-005). Perform a full investigation and take all necessary containment actions as per the security incident response policy."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-005"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-002"}),
            Action(name="list_user_sessions", kwargs={"user_id": "U-002"}),
            
            Action(name="update_user_status", kwargs={"user_id": "U-002", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_SUSPENDED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for U-002 suspended by mdavis in response to critical SIEM alert ALRT-005.",
                },
            ),

            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-002"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-010"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-006 revoked from user swilliams (U-002) as a preventative measure following critical SIEM alert ALRT-005.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-011"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-002",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-035 revoked from user swilliams (U-002) as a preventative measure following critical SIEM alert ALRT-005.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "marketing-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-035"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "security-operations@taucorp.com",
                    "receiver": "michael.davis@taucorp.com",
                    "subject": "ESCALATION: Security Alert - Lead Account Suspended (U-002)",
                    "text_content": "Hi Michael, this is an automated notification to inform you that the account for a department lead, swilliams (U-002), has been temporarily suspended due to a critical security alert (ALRT-005). This is an escalation notification per security policy. Please contact Security Operations for more details.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "INVESTIGATION: Suspicious Activity for user U-002 (swilliams)",
                    "description": "Investigation of SIEM alert ALRT-005. Findings: User U-002 (swilliams) is the Marketing department lead. A check of recent sessions and assigned roles revealed no anomalies. Actions Taken: User account was suspended and all assigned roles (ROL-006, ROL-035) were revoked as a precautionary measure due to the HIGH severity of the alert. Further monitoring is recommended.",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "SECURITY_INVESTIGATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_investigated": "U-002",
                "containment_actions": ["user_suspended", "all_roles_revoked"],
                "revoked_roles": ["ROL-006", "ROL-035"],
                "hubspot_ticket_created": True,
                "notification_escalated": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_005",
        instruction="You are Jessica Garcia, Finance Manager. A new access request, 'AR-034', from your direct report Stephanie Adams is pending your review. Please conduct a thorough review of the request, ensuring that approving it would not violate any compliance policies, including the principle of Separation of Duties, before making a final decision.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "jgarcia"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-034"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-018"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-018"}),

            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-030"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-029"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-033"}),

            Action(
                name="reject_access_request",
                kwargs={
                    "request_id": "AR-034", "reviewer_id": "U-006", "timestamp": "2025-08-09 10:00:00+00:00",
                    "rejection_reason": "Approval would violate the Separation of Duties policy. User cannot have both 'finance-audit-access' and 'finance-read' roles.",
                },
            ),

            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-006", "action_type": "POLICY_VIOLATION_IDENTIFIED", "target_id": "U-018", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "SoD violation identified for user U-018: Granting requested role ROL-030 would create a conflict with existing role ROL-033.",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-006", "action_type": "ACCESS_REJECTED", "target_id": "AR-034", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-034 rejected by jgarcia (U-006). Reason: Approval would violate the Separation of Duties policy. User cannot have both 'finance-audit-access' and 'finance-read' roles.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "it-operations@taucorp.com", "receiver": "stephanie.adams@taucorp.com",
                    "subject": "Update on Your Access Request (AR-034)",
                    "text_content": "Hi Stephanie, your access request (AR-034) for the 'finance-read' role was rejected. A compliance review found that granting this role would create a Separation of Duties policy conflict with your existing roles. Please contact your manager if you have any questions.",
                },
            ),
        ],
        outputs=[json.dumps({"request_id": "AR-034", "status": "REJECTED", "reason": "SOD_VIOLATION"})],
    ),
    Task(
        annotator="2",
        user_id="task_006",
        instruction="You are Michael Davis, IT Operations Manager. A critical incident has been declared: the production database is down. You must execute the emergency 'break-glass' procedure to grant the on-call engineer, Brian Taylor, the specific, least-privileged access required to resolve a database outage. Ensure the entire procedure is documented in HubSpot in accordance with the 'EMERGENCY_ACCESS' policy.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_user_details_by_username", kwargs={"username": "btaylor"}),
            Action(name="get_resource_by_name", kwargs={"resource_name": "database-cluster-primary"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-db-admin"}),
            Action(
                name="create_access_request",
                kwargs={
                    "user_id": "U-013",
                    "role_id": "ROL-027",
                    "resource_id": "RES-026",
                    "justification": "Emergency 'break-glass' access to resolve critical production database outage.",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="approve_access_request",
                kwargs={
                    "request_id": "AR-042",
                    "reviewer_id": "U-005",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "expires_on": "2025-08-09 14:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "EMERGENCY_ACCESS_INITIATED",
                    "target_id": "U-013",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Emergency access procedure initiated by Michael Davis (U-005) for user Brian Taylor (U-013) to address a critical incident.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "EMERGENCY_ACCESS", "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-005",
                    "subject": "EMERGENCY ACCESS: Break-Glass Procedure for User U-013",
                    "description": "Emergency access granted to user btaylor (U-013) via temporary role assignment (AR-042). Access to role 'operations-db-admin' (ROL-027) on resource 'database-cluster-primary' (RES-026) expires at 2025-08-09 14:00:00+00:00.",
                },
            ),
        ],
        outputs=[json.dumps({"emergency_role_granted": "ROL-027", "user_id": "U-013", "access_request_id": "AR-042", "hubspot_ticket_created": True})],
    ),
    Task(
        annotator="2",
        user_id="task_007",
        instruction=(
            "You are Michael Davis from Operations. A routine audit has flagged that user mlopez may have inappropriate access. Please investigate and correct this."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_user_details_by_username", kwargs={"username": "mlopez"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-009"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-013"}),

            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-036"}),

            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-023"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-013 revoked from user mlopez (U-009) due to security policy violation: User has manager-level role but is not the department lead.",
                },
            ),
            Action(name="update_user_status", kwargs={"user_id": "U-009", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_SUSPENDED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for mlopez (U-009) suspended due to security policy violation: Inappropriate assignment of manager-level role.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "INVESTIGATION: Suspicious Activity for user U-009 (mlopez)",
                    "description": "Audit-based investigation of user mlopez (U-009) confirmed a policy violation. Finding: User was assigned the 'sales-lead-manager' role (ROL-013) but is not the designated department lead. Actions Taken: The inappropriate role assignment (UR-023) was revoked, and the user's account has been suspended. Further review of user's activity is recommended.",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "SECURITY_INVESTIGATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_investigated": "U-009",
                "remediation_steps": ["role_revoked", "user_suspended"],
                "hubspot_ticket_created": True,
                "revoked_user_role_id": "UR-023"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_008",
        instruction=(
            "You are Alex Johnson, Engineering Lead. A new access request has been posted in the #access-requests Slack channel (message ID: SL-001). Please review it and take the appropriate action."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "ajohnson"}),
            Action(name="get_slack_message_by_id", kwargs={"message_id": "SL-001"}),
            Action(name="find_access_request_by_details",
                kwargs={"user_id": "U-007", "resource_id": "RES-025", "role_id": "ROL-023"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-007"}), 
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-023"}),
            Action(
                name="reject_access_request",
                kwargs={
                    "request_id": "AR-001",
                    "reviewer_id": "U-001",
                    "reason": "Role is not appropriate for user's department. Violation of least privilege.",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "ACCESS_REJECTED",
                    "target_id": "AR-001",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-001 rejected by ajohnson (U-001). Reason: Role is not appropriate for user's department. Violation of least privilege.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-base"}), 
            Action(name="assign_role_to_user", kwargs={"user_id": "U-007", "role_id": "ROL-001"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Proactively assigned standard role ROL-001 to user U-007 after inappropriate request.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "christopher.rodriguez@taucorp.com",
                    "subject": "Update on Your Access Request (AR-001)",
                    "text_content": "Hi Christopher, your access request (AR-001) for role ROL-023 was rejected as it violates the principle of least privilege. To ensure you have the necessary access for your standard duties, we have proactively assigned you the base role for your department. Please contact IT Operations if you have further questions.",
                },
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests",
                    "message": "Update on request AR-001: This request has been reviewed by ajohnson and the final status is REJECTED. cc: @crodriguez",
                    "thread_id": "SL-001",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-001",
                "decision": "REJECTED",
                "proactive_remediation": "ASSIGNED_BASE_ROLE",
                "assigned_role_id": "ROL-001"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_009",
        instruction=(
            "You are Michael Davis, IT Operations Manager. A routine security check has flagged former employee James Moore as suspicious activity regarding 'sales-reporting-dashboard'. Please investigate and create the required alerts and tickets for Legal & HR."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_user_details_by_username", kwargs={"username": "jmoore"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-011"}),
            Action(name="list_user_sessions", kwargs={"user_id": "U-011"}), 
            Action(name="get_resource_by_name", kwargs={"resource_name": "sales-reporting-dashboard"}), 
            Action(
                name="create_siem_alert",
                kwargs={
                    "alert_type": "POTENTIAL_DATA_EXFILTRATION",
                    "user_id": "U-011",
                    "resource_id": "RES-015",
                    "severity": "CRITICAL",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "SIEM_ALERT_CREATED",
                    "target_id": "ALRT-013",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "SIEM alert ALRT-013 created for POTENTIAL_DATA_EXFILTRATION on RES-015.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "URGENT: Forensic Investigation of Data Exfiltration by Former Employee (U-011)",
                    "description": "Forensic investigation opened for former employee James Moore (U-011) regarding suspicious access to sales-reporting-dashboard (RES-015). Anomalous session detected from IP address 2001:db8:cafe::1 at 2025-08-03 15:00:00+00:00. SIEM alert ALRT-013 created. Assigning to Legal & HR for follow-up.",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "LEGAL_HR_INVESTIGATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_investigated": "U-011",
                "user_status_confirmed": "DISABLED",
                "alert_created": True,
                "hubspot_ticket_created": True,
                "ticket_category": "LEGAL_HR_INVESTIGATION"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_010",
        instruction=(
            "You are Alex Johnson, Engineering Lead. A new access request has been posted in the #access-requests Slack channel that requires your review (message_id: SL-018)."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "ajohnson"}),
            Action(name="get_slack_message_by_id", kwargs={"message_id": "SL-018"}),
            Action(name="find_access_request_by_details", kwargs={"user_id": "U-006", "resource_id": "RES-025", "role_id": "ROL-026"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-006"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-026"}),

            Action(
                name="reject_access_request",
                kwargs={
                    "request_id": "AR-018", "reviewer_id": "U-001", "timestamp": "2025-08-09 10:00:00+00:00",
                    "rejection_reason": "Role is not appropriate for user's department. Violation of least privilege.",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001", "action_type": "ACCESS_REJECTED", "target_id": "AR-018", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-018 rejected by ajohnson (U-001). Reason: Role is not appropriate for user's department. Violation of least privilege.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "finance-base"}),
            Action(name="assign_role_to_user", kwargs={"user_id": "U-006", "role_id": "ROL-029", "assigned_by": "U-001"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001", "action_type": "ROLE_ASSIGNED", "target_id": "U-006", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Proactively assigned standard role ROL-029 to user U-006 after inappropriate request.",
                },
            ),

            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "it-operations@taucorp.com", "receiver": "jessica.garcia@taucorp.com",
                    "subject": "Update on Your Access Request (AR-018)",
                    "text_content": "Hi Jessica, your access request (AR-018) for role ROL-026 was rejected as it violates the principle of least privilege. To ensure you have the necessary access for your standard duties, we have proactively assigned you the base role for your department. Please contact IT Operations if you have further questions.",
                },
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests",
                    "message": "Update on request AR-018: This request has been reviewed by ajohnson and the final status is REJECTED. cc: @jgarcia",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "reply_to_message_id": "SL-018"
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-018",
                "final_status": "REJECTED",
                "proactive_solution_provided": True,
                "assigned_role_id": "ROL-029"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_011",
        instruction=(
            "You are the RBAC Bot. As part of your duties to maintain a secure and compliant access control environment, a new access request requires your review (message_id: SL-022). Investigate the request and the user's current access, and take all necessary actions to resolve the request in a way that ensures business continuity while upholding our security policies."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_slack_message_by_id", kwargs={"message_id": "SL-022"}),
            Action(name="find_access_request_by_details", kwargs={"user_id": "U-009", "resource_id": "RES-016", "role_id": "ROL-013"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-009"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-013"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-009"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-016"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-021"}),
            Action(
                name="reject_access_request",
                kwargs={
                    "request_id": "AR-022", "reviewer_id": "U-021", "timestamp": "2025-08-09 10:00:00+00:00",
                    "rejection_reason": "The requested access is redundant. The user's existing roles already provide the necessary permissions.",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-021", "action_type": "ACCESS_REJECTED", "target_id": "AR-022", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-022 rejected by pellis (U-021). Reason: The requested access is redundant. The user's existing roles already provide the necessary permissions.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "it-operations@taucorp.com", "receiver": "matthew.lopez@taucorp.com",
                    "subject": "Update on Your Access Request (AR-022)",
                    "text_content": "Hi Matthew, your access request (AR-022) for the 'sales-lead-manager' role was rejected. The reason is: The requested access is redundant. The user's existing roles already provide the necessary permissions. No further action is needed.",
                },
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests", "message": "Update on request AR-022: This request has been reviewed by pellis and the final status is REJECTED. cc: @mlopez",
                    "timestamp": "2025-08-09 10:00:00+00:00", "thread_id": "SL-022"
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-022",
                "final_status": "REJECTED",
                "rejection_reason": "The requested access is redundant. The user's existing roles already provide the necessary permissions.",
                "notifications_sent": ["email", "slack"]
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_012",
        instruction=(
            "You are Ashley Wilson from HR. Please process the department switching for Amanda Miller, from Marketing to Engineering."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "amiller"}),
    
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-008"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-012"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-008",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-006 revoked from user amiller (U-008) as part of department change to Engineering.",
                },
            ),
            Action(
                name="update_user_department",
                kwargs={
                    "user_id": "U-008",
                    "new_department": "Engineering",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "USER_DEPARTMENT_CHANGE",
                    "target_id": "U-008",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User amiller (U-008) department changed to Engineering.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-base"}),
            Action(
                name="assign_role_to_user",
                kwargs={
                    "user_id": "U-008",
                    "role_id": "ROL-001",
                    "assigned_by": "U-010",
                    "assigned_on": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-008",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role engineering-base (ROL-001) assigned to user amiller (U-008) as part of department change to Engineering.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-034"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-001"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "amanda.miller@taucorp.com",
                    "subject": "Confirmation of Your Department Change",
                    "text_content": "Hi Amanda, this email confirms that your department has been successfully changed to Engineering. Your previous roles have been revoked and you have been granted the standard 'engineering-base' access. Please contact your new manager, Alex Johnson, for any additional access you may require.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "alex.johnson@taucorp.com",
                    "subject": "Notification: Department Change for Amanda Miller",
                    "text_content": "Hi Alex, this is an automated notification to inform you that Amanda Miller has been transferred to your department (Engineering) and has been assigned the standard 'engineering-base' role. Please follow up with them regarding any additional access needs.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-008",
                "previous_department": "Marketing",
                "new_department": "Engineering",
                "roles_revoked": ["ROL-006"],
                "roles_granted": ["ROL-001"]
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_013",
        instruction=(
            "You are Michael Davis, IT Operations Manager. You have received a CRITICAL SIEM alert (ALRT-012) for a user in the Human Resources department. Perform a full investigation and take all necessary containment actions as per the security incident response policy."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-012"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}),
            Action(name="list_user_sessions", kwargs={"user_id": "U-004"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-004"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-016"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-037"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-029"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-004",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-016 revoked from user ejones (U-004) as a preventative measure following critical SIEM alert ALRT-012.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-030"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-004",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-037 revoked from user ejones (U-004) as a preventative measure following critical SIEM alert ALRT-012.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "security-operations@taucorp.com",
                    "receiver": "michael.davis@taucorp.com",
                    "subject": "ESCALATION: Security Alert - User Account Suspended (U-004)",
                    "text_content": "Hi Michael, this is an automated notification to inform you that the account for a department lead, ejones (U-004), has been temporarily suspended due to a critical security alert (ALRT-012). This is an escalation notification per security policy. Please contact Security Operations for more details.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "INVESTIGATION: Suspicious Activity for user U-004 (ejones)",
                    "description": "Investigation of SIEM alert ALRT-012 complete. User ejones (U-004) was confirmed to be already suspended. As a further preventative measure due to the cross-departmental nature of the alert, the user's 'hr-lead' role (ROL-037) was also revoked. No further action required. Closing ticket.",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "SECURITY_INVESTIGATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="update_hubspot_ticket",
                kwargs={"ticket_id": "TI-054", "status": "CLOSED", "timestamp": "2025-08-09 10:00:00+00:00"}
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "INVESTIGATION_CLOSED",
                    "target_id": "ALRT-012",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigation complete. HubSpot ticket TI-054 updated with findings and status changed to CLOSED.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_investigated": "U-004",
                "containment_actions": ["user_already_suspended", "all_roles_revoked"],
                "revoked_roles": ["ROL-016", "ROL-037"],
                "notification_sent_to": "michael.davis@taucorp.com",
                "hubspot_ticket_id": "TI-054",
                "investigation_complete": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_014",
        instruction=(
            "You are Alex Johnson from Engineering. A compliance scan has flagged that the permanent access grant for user Daniel Taylor (dtaylor) to the production CI/CD pipeline (a CRITICAL resource) is non-compliant. Remediate this by revoking the permanent access and replacing it with a temporary 4-hour grant."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "ajohnson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "dtaylor"}),

            Action(name="get_resource_by_name", kwargs={"resource_name": "cicd-pipeline-main"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-019"}),

            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-008"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-019",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Permanent access grant (UR-008) revoked to enforce temporary access policy for CRITICAL resources.",
                },
            ),

            Action(
                name="create_access_request",
                kwargs={
                    "user_id": "U-019",
                    "role_id": "ROL-004",
                    "resource_id": "RES-003",
                    "justification": "Re-issuing access with a 4-hour temporary grant per compliance policy for CRITICAL resources.",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),

            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-003"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-007"}),
            Action(
                name="approve_access_request",
                kwargs={
                    "request_id": "AR-042",
                    "reviewer_id": "U-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "expires_on": "2025-08-09 14:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-007",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-042",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Temporary access grant approved for request AR-042 with a 4-hour expiration.",
                },
            ),

            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "daniel.taylor@taucorp.com",
                    "subject": "Action Required: Your Access Grant has been Updated",
                    "text_content": "This is an automated notification. The permanent access grant associated with request AR-042 has been revoked and replaced with a temporary 4-hour grant in compliance with the policy for CRITICAL resources. The new temporary access will expire at 2025-08-09 14:00:00+00:00.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_remediated": "U-019",
                "revoked_user_role_id": "UR-008",
                "new_temporary_request_id": "AR-042",
                "access_expires_on": "2025-08-09 14:00:00+00:00"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_015",
        instruction=(
            "You are Michael Davis, IT Operations Manager. You have received a HIGH severity SIEM alert (ALRT-003) regarding a user in the Sales department. Perform a full investigation and take all necessary containment actions, including notifying the appropriate manager or escalating if they are unavailable."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-003"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-009"}),
            
            Action(name="check_user_sessions_by_id", kwargs={"user_id": "U-009"}),

            Action(name="update_user_status", kwargs={"user_id": "U-009", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "USER_SUSPENDED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for U-009 suspended by mdavis in response to critical SIEM alert ALRT-003.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-009"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-021"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-011 revoked from user mlopez (U-009) as a containment measure following critical SIEM alert ALRT-003."}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-022"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-012 revoked from user mlopez (U-009) as a containment measure following critical SIEM alert ALRT-003."}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-023"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-013 revoked from user mlopez (U-009) as a containment measure following critical SIEM alert ALRT-003."}),

            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-036"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-003"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}), 
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "security-operations@taucorp.com", "receiver": "michael.davis@taucorp.com",
                    "subject": "ESCALATION: Security Alert - User Account Suspended (U-009)",
                    "text_content": "Hi Michael, this is an automated notification to inform you that the account for user Matthew Lopez (U-009) has been temporarily suspended due to a critical security alert (ALRT-003). This is an escalation notification as their direct manager is not in an active state. Please contact Security Operations for more details.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "INVESTIGATION: Suspicious Activity for user U-009 (mlopez)",
                    "description": "Investigation of SIEM alert ALRT-003. Findings: User U-009 (mlopez) is in the Sales department. A check of recent sessions and assigned roles revealed no anomalies. Actions Taken: User account was suspended and all assigned roles (ROL-011, ROL-012, ROL-013) were revoked as a precautionary measure due to the HIGH severity of the alert.",
                    "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-005", "category": "SECURITY_INVESTIGATION", "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_investigated": "U-009",
                "containment_actions": ["user_suspended", "all_roles_revoked"],
                "notification_escalated": True,
                "hubspot_ticket_id": "TI-054"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_016",
        instruction=(
            "You are Sarah Williams from Marketing. A new access request has been posted in Slack (message_id: SL-013). Please review and take the appropriate action."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "swilliams"}),
            Action(name="get_slack_message_by_id", kwargs={"message_id": "SL-013"}),
            Action(name="find_access_request_by_details", kwargs={"user_id": "U-014", "resource_id": "RES-010", "role_id": "ROL-009"}),
            
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-010"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-026"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-014"}),
            
            Action(
                name="update_access_request",
                kwargs={
                    "request_id": "AR-013",
                    "new_reviewer_id": "U-026",
                    "new_status": "PENDING",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                }
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ACCESS_REQUEST_REVIEWED",
                    "target_id": "AR-013",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-013 reviewed by swilliams (U-002) and rerouted to correct owner aphillips (U-026).",
                },
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests",
                    "message": "Update on request AR-013: This request has been reviewed by @swilliams and rerouted to the correct approver, @aphillips. cc: @nthomas",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "thread_id": "SL-013"
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-013",
                "status": "PENDING",
                "reason": "The reviewer is not the designated approver for the requested resource.",
                "rerouted_to": "U-026"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_017",
        instruction=(
            "You are the Certification Bot. It is time to process the in-progress access certification campaign 'C-005' for the 'sales-lead' role. Review all users with this role and revoke access for any user who is not in the 'Sales' department or does not have an 'ACTIVE' status. Document all findings and send a summary to the campaign reviewer upon completion."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "CERTIFICATION_BOT"}),
            Action(name="get_certification_details_by_id", kwargs={"certification_id": "C-005"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-lead"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-036"}),

            Action(name="find_users_with_role", kwargs={"role_id": "ROL-036"}),
            
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-003"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-003"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-020"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-033", 
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-003",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-036 revoked from user dbrown (U-003) due to failing certification C-005 (user not in an ACTIVE state).",
                },
            ),

            Action(name="update_certification_status", kwargs={"certification_id": "C-005", "new_status": "COMPLETED", "timestamp": "2025-08-09 10:00:00+00:00"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-033", 
                    "action_type": "CERTIFICATION_COMPLETED",
                    "target_id": "C-005",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Certification campaign C-005 status updated to COMPLETED on behalf of reviewer dbrown.",
                },
            ),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-014"}),
            Action(
                name="send_email",
                kwargs={
                    "sender": "certifications@taucorp.com", "receiver": "david.brown@taucorp.com", "subject": "Certification Campaign C-005 Completed",
                    "text_content": "Hi David, this is an automated notification that the certification campaign C-005 for resource salesforce-crm-prod (RES-014) has been completed. A total of 1 users were reviewed. 1 non-compliant user(s) were found, and 1 role assignment(s) were revoked. No further action is required.",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[json.dumps({"certification_id": "C-005", "status": "COMPLETED", "violations_found": 1, "remediated_users": ["U-003"]})],
    ),
    Task(
        annotator="2",
        user_id="task_018",
        instruction=(
            "You are Ashley Wilson from HR. You need to onboard a new Sales Associate, Olivia Green, for the Sales department, managed by David Brown. She will require the 'sales-base' and 'sales-crm-access' roles. Ensure no Separation of Duties conflicts are created and notify the new user's manager upon completion."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(
                name="create_user",
                kwargs={
                    "username": "ogreen",
                    "email": "olivia.green@taucorp.com",
                    "department": "Sales",
                    "status": "ACTIVE",
                },
            ),
            Action(name="get_user_details_by_username", kwargs={"username": "ogreen"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034", 
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "New user account created via onboarding workflow.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-base"}),
            Action(
                name="assign_role_to_user",
                kwargs={"user_id": "U-034", "role_id": "ROL-011", "assigned_by": "U-010"},
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role sales-base (ROL-011) assigned to user ogreen (U-034) as part of onboarding.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-crm-access"}),
            Action(
                name="assign_role_to_user",
                kwargs={"user_id": "U-034", "role_id": "ROL-012", "assigned_by": "U-010"},
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role sales-crm-access (ROL-012) assigned to user ogreen (U-034) as part of onboarding.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "onboarding@taucorp.com",
                    "receiver": "olivia.green@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Olivia, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-036"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-003"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "david.brown@taucorp.com",
                    "subject": "Notification: New Direct Report - Olivia Green",
                    "text_content": "Hi David, this is an automated notification to inform you that a new employee, Olivia Green, has been onboarded into your department (Sales). They have been assigned their initial roles. Please follow up with them regarding any additional access needs.", # Correct template
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-034",
                "username": "ogreen",
                "email": "olivia.green@taucorp.com",
                "department": "Sales",
                "status": "ACTIVE",
                "roles": ["sales-base", "sales-crm-access"],
                "manager_notified": "U-003" # The correct manager is notified
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_019",
        instruction="You are Alex Johnson from Engineering. The main application repository ('main-application-repo') is corrupted and needs immediate administrative intervention. Grant emergency administrative access to the repository to 'crodriguez', the on-call engineer.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "ajohnson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "crodriguez"}),
            Action(name="get_resource_by_name", kwargs={"resource_name": "main-application-repo"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-code-commit"}),
            Action(
                name="create_access_request",
                kwargs={
                    "user_id": "U-007", "role_id": "ROL-002", "resource_id": "RES-002", "timestamp": "2025-08-09 10:00:00+00:00",
                    # This justification is now sourced from a specific, deterministic rule.
                    "justification": "Emergency administrative access to resolve corruption of the main application repository.",
                },
            ),
            Action(
                name="approve_access_request",
                kwargs={
                    "request_id": "AR-042", "reviewer_id": "U-001", "timestamp": "2025-08-09 10:00:00+00:00",
                    "expires_on": "2025-08-09 14:00:00+00:00", 
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001", "action_type": "EMERGENCY_ACCESS_INITIATED", "target_id": "U-007", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Emergency access procedure initiated by Alex Johnson (U-001) for user Christopher Rodriguez (U-007) to address a critical incident.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "EMERGENCY_ACCESS", "priority": "HIGH", "assignee_id": "U-001", "requester_id": "U-001",
                    "subject": "EMERGENCY ACCESS: Break-Glass Procedure for User U-007",
                    "description": "Emergency access granted to user Christopher Rodriguez (U-007) via temporary role assignment (AR-042). Access to role 'engineering-code-commit' (ROL-002) on resource 'main-application-repo' (RES-002) expires at 2025-08-09 14:00:00+00:00.",
                },
            ),
        ],
        outputs=[json.dumps({"emergency_role_granted": "ROL-002", "user_role_id": "UR-063", "access_request_id": "AR-042", "hubspot_ticket_created": True})],
    ),
    Task(
        annotator="2",
        user_id="task_020",
        instruction="You are the RBAC Bot, performing a routine compliance audit. You have detected a potential anomaly: access request 'AR-019' was rejected by user 'dbrown'. However, records indicate that 'dbrown' was not in an 'ACTIVE' state at the time of the rejection. Your task is to investigate this anomaly, confirm the details of all associated users and requests, and create a high-priority HubSpot ticket for the IT Operations team to investigate this process control failure.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-019"}),
            Action(name="get_user_details_by_username", kwargs={"username": "dbrown"}),

            Action(name="get_user_details_by_id", kwargs={"user_id": "U-016"}), 
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-014"}),

            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}), 

            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031", "action_type": "POLICY_VIOLATION_IDENTIFIED", "target_id": "AR-019", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Process control failure detected: Access request AR-019 was actioned by user U-003, who is not in an ACTIVE state.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "COMPLIANCE_AUDIT", "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-031",
                    "subject": "ACTION REQUIRED: Process Control Failure on Access Request AR-019",
                    "description": "Automated compliance audit of access request AR-019 has detected a critical process control failure. The request was rejected by user dbrown (U-003), whose account status was 'PENDING_ACCESS' at the time of the decision. This action should not have been possible. Escalating to IT Operations for manual review of system controls and audit logs to determine how this occurred.",
                },
            ),
        ],
        outputs=[json.dumps({"anomaly_detected": "ACTION_BY_INACTIVE_USER", "request_id": "AR-019", "escalated_to": "U-005", "hubspot_ticket_created": True})],
    ),
    Task(
        annotator="2",
        user_id="task_021",
        instruction=(
            "You are Jessica Garcia, the Finance Lead. A new access request has been posted in the #access-requests Slack channel (message_id: SL-020) that requires your review."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "jgarcia"}),
            Action(name="get_slack_message_by_id", kwargs={"message_id": "SL-020"}),
            Action(name="find_access_request_by_details", kwargs={"user_id": "U-013", "resource_id": "RES-006", "role_id": "ROL-004"}),
            
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-006"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-007"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-013"}),
            
            Action(
                name="update_access_request",
                kwargs={
                    "request_id": "AR-020",
                    "new_reviewer_id": "U-007",
                    "new_status": "PENDING",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                }
            ),
            
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ACCESS_REQUEST_REVIEWED",
                    "target_id": "AR-020",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-020 reviewed by jgarcia (U-006) and rerouted to correct owner crodriguez (U-007).",
                },
            ),
            
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests",
                    "message": "Update on request AR-020: This request has been reviewed by @jgarcia and rerouted to the correct approver, @crodriguez. cc: @btaylor",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "reply_to_message_id": "SL-020"
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-020",
                "status": "PENDING",
                "reason": "The reviewer is not the designated approver for the requested resource.",
                "rerouted_to": "U-007"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_022",
        instruction=(
            "You are Ashley Wilson from HR. Please process the department transfer for Lisa Anderson, who is moving from the Finance department to the Sales department."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "landerson"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-012"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-048"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-029 revoked from user landerson (U-012) as part of department change to Sales.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-049"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-031 revoked from user landerson (U-012) as part of department change to Sales.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-050"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-032 revoked from user landerson (U-012) as part of department change to Sales.",
                },
            ),
            Action(name="update_user_department", kwargs={"user_id": "U-012", "new_department": "Sales"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "USER_DEPARTMENT_CHANGE", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User landerson (U-012) department changed to Sales.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-base"}),
            Action(name="assign_role_to_user", kwargs={"user_id": "U-012", "role_id": "ROL-011", "assigned_by": "U-010"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_ASSIGNED", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role sales-base (ROL-011) assigned to user landerson (U-012) as part of department change to Sales.",
                },
            ),

            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-036"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-003"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "hr-operations@taucorp.com", "receiver": "lisa.anderson@taucorp.com",
                    "subject": "Confirmation of Your Department Change",
                    "text_content": "Hi Lisa, this email confirms that your department has been successfully changed to Sales. Your previous roles have been revoked and you have been granted the standard 'sales-base' access. Please contact your new manager, David Brown, for any additional access you may require.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "hr-operations@taucorp.com", "receiver": "david.brown@taucorp.com",
                    "subject": "Notification: Department Change for Lisa Anderson",
                    "text_content": "Hi David, this is an automated notification to inform you that Lisa Anderson has been transferred to your department (Sales) and has been assigned the standard 'sales-base' role. Please follow up with them regarding any additional access needs.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-012",
                "previous_department": "Finance",
                "new_department": "Sales",
                "roles_revoked": ["ROL-029", "ROL-031", "ROL-032"],
                "roles_granted": ["ROL-011"],
                "manager_notified": "U-003"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_023",
        instruction=(
            "You are Michael Davis, IT Operations Manager. A HIGH severity SIEM alert (ALRT-006) has been triggered for user 'sadams'. Conduct a full investigation and take all necessary containment actions as per the security incident response policy."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-006"}),
            Action(name="get_user_details_by_username", kwargs={"username": "sadams"}),
            Action(name="list_user_sessions", kwargs={"user_id": "U-018"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_SESSION_CHECKED",
                    "target_id": "U-018",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigator reviewed recent sessions for user U-018 as part of security investigation.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-018"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_REVIEWED",
                    "target_id": "U-018",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigator reviewed assigned roles for user U-018 as part of security investigation.",
                },
            ),
            Action(name="update_user_status", kwargs={"user_id": "U-018", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_SUSPENDED",
                    "target_id": "U-018",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for U-018 suspended by mdavis in response to critical SIEM alert ALRT-006.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-051"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-018",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-029 revoked from user sadams (U-018) as a preventative measure following critical SIEM alert ALRT-006.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-052"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-018",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-033 revoked from user sadams (U-018) as a preventative measure following critical SIEM alert ALRT-006.",
                },
            ),

            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "INVESTIGATION: Suspicious Activity for user U-018 (sadams)",
                    "description": "Investigation of SIEM alert ALRT-006. Findings: User U-018 (sadams) is in the Finance department. A check of recent sessions and assigned roles revealed no anomalies. Actions Taken: User account was suspended and all assigned roles were revoked as a precautionary measure due to the HIGH severity of the alert. Further monitoring is recommended.",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "SECURITY_INVESTIGATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_investigated": "U-018",
                "investigation_steps_logged": ["session_check", "role_check"],
                "containment_actions": ["user_suspended", "all_roles_revoked"],
                "revoked_roles": ["ROL-029", "ROL-033"],
                "hubspot_ticket_created": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_024",
        instruction=(
            "You are Michael Davis, IT Operations Manager. A compliance alert has been triggered for user 'pcarter' in the Operations department, indicating a possible role assignment violation. Please investigate, log your findings, and remediate any issues."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_user_details_by_username", kwargs={"username": "pcarter"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-029"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_REVIEWED", 
                    "target_id": "U-029",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigator reviewed assigned roles for user U-029 as part of security investigation.",
                },
            ),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-021"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_VIOLATION_IDENTIFIED",
                    "target_id": "U-029",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Violation found for user U-029: Role ROL-021 is assigned permanently, violating policy that requires it to be temporary.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-045"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-029",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-021 revoked from user pcarter (U-029) due to security policy violation: Permanent assignment of temporary role.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "compliance-system@taucorp.com",
                    "receiver": "patrick.carter@taucorp.com",
                    "subject": "Action Required: Your Access Has Been Updated",
                    "text_content": "Hi Patrick, a compliance review found that your assignment of the 'operations-base' role (ROL-021) was non-compliant with security policy. This role has been revoked. Please submit a new access request if you still require this access.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "COMPLIANCE: Remediated role assignment for user U-029 (pcarter)",
                    "description": "Compliance-driven investigation of user pcarter (U-029). Finding: User had a permanent assignment (UR-045) for a role that must be temporary (ROL-021). Action Taken: The non-compliant role assignment was revoked.",
                    "priority": "MEDIUM",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "COMPLIANCE_REMEDIATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_investigated": "U-029",
                "policy_violation": "Permanent assignment of temporary role",
                "remediation_action": "revoked_user_role_id",
                "revoked_user_role_id": "UR-045",
                "hubspot_ticket_created": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_025",
        instruction=(
            "You are Ashley Wilson from HR. Process the department transfer for Robert White (rwhite), who is moving from Operations to Engineering. He must retain his 'operations-server-monitor' role for one week to train his replacement."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "rwhite"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-017"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-040"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-021 revoked from user rwhite (U-017) as part of department change to Engineering.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-042"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-024 revoked from user rwhite (U-017) as part of department change to Engineering.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-041"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-022 revoked from user rwhite (U-017) as part of department change to Engineering.",
                },
            ),
            Action(
                name="assign_role_to_user",
                kwargs={
                    "user_id": "U-017",
                    "role_id": "ROL-022",
                    "assigned_by": "U-010",
                    "expires_on": "2025-08-16 10:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Temporary role ROL-022 assigned to user rwhite (U-017) with a defined expiration.",
                },
            ),
            Action(name="update_user_department", kwargs={"user_id": "U-017", "new_department": "Engineering"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "USER_DEPARTMENT_CHANGE",
                    "target_id": "U-017",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User rwhite (U-017) department changed to Engineering.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-base"}),
            Action(
                name="assign_role_to_user",
                kwargs={
                    "user_id": "U-017",
                    "role_id": "ROL-001",
                    "assigned_by": "U-010",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role engineering-base (ROL-001) assigned to user rwhite (U-017) as part of department change to Engineering.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-034"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-001"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "robert.white@taucorp.com",
                    "subject": "Confirmation of Your Department Change",
                    "text_content": "Hi Robert, this email confirms that your department has been successfully changed to Engineering. Your previous roles have been revoked and you have been granted the standard 'engineering-base' access. Please contact your new manager, Alex Johnson, for any additional access you may require.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "alex.johnson@taucorp.com",
                    "subject": "Notification: Department Change for Robert White",
                    "text_content": "Hi Alex, this is an automated notification to inform you that Robert White has been transferred to your department (Engineering) and has been assigned the standard 'engineering-base' role. Please follow up with them regarding any additional access needs.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-017",
                "previous_department": "Operations",
                "new_department": "Engineering",
                "roles_revoked": ["ROL-021", "ROL-024", "ROL-022"],
                "roles_granted": ["ROL-001"],
                "retained_role_details": {
                    "role_id": "ROL-022",
                    "access_expires_on": "2025-08-16 10:00:00+00:00"
                }
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_026",
        instruction=(
            "You are the RBAC Bot. A new access request has been posted in the #access-requests Slack channel (message_id: SL-024). Please review it and take the appropriate action based on company policy."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_slack_message_by_id", kwargs={"message_id": "SL-024"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-001"}),
            Action(name="find_access_request_by_details",
                   kwargs={"user_id": "U-001", "resource_id": "RES-026", "role_id": "ROL-027"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-026"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-011"}), 
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}), 
            Action(
                name="reject_access_request",
                kwargs={
                    "request_id": "AR-024",
                    "reviewer_id": "U-031", 
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "rejection_reason": "Resource owner is disabled. Request is being rerouted to the appropriate department lead for review.",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031",
                    "action_type": "ACCESS_REJECTED",
                    "target_id": "AR-024",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-024 rejected by RBAC_BOT (U-031). Reason: Resource owner is disabled. Request is being rerouted to the appropriate department lead for review.",
                },
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests",
                    "message": "Update on request AR-024: This request has been reviewed by RBAC_BOT and the final status is REJECTED. This request has been rerouted to the correct approver, @mdavis. cc: @ajohnson",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "reply_to_message_id": "SL-024"
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-024",
                "final_status": "REJECTED",
                "rejection_reason": "Resource owner disabled.",
                "next_action": "Rerouted to department lead @mdavis."
            })
        ],
    ),
        Task(
        annotator="2",
        user_id="task_027",
        instruction=(
            "You are Michael Davis, the IT Operations Manager. A high-priority access request (AR-007) from your team member, Patrick Carter, has been submitted for the 'operations-system-admin' role on the critical production web server. Please review and take the appropriate action in line with the temporary access policy for critical resources."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-007"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-029"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-025"}),
            Action(
                name="approve_access_request",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "expires_on": "2025-08-09 14:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-007 approved by mdavis (U-005). Role ROL-026 granted to user U-029.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "patrick.carter@taucorp.com",
                    "subject": "Your Access Request AR-007 has been Approved",
                    "text_content": "Hi Patrick, your access request AR-007 for role ROL-026 has been approved by Michael Davis. This access is temporary and will expire on 2025-08-09 14:00:00+00:00.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-007",
                "final_status": "APPROVED",
                "is_temporary": True,
                "access_expires_on": "2025-08-09 14:00:00+00:00"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_028",
        instruction=(
            "You are Michael Davis, the IT Operations Manager. A high-priority access request (AR-007) from your team member, Patrick Carter, has been submitted for the 'operations-system-admin' role on the critical production web server. Please review and take the appropriate action, ensuring each step is logged for audit purposes."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-007"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ACCESS_REQUEST_REVIEWED",
                    "target_id": "AR-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-007 review initiated by mdavis.",
                },
            ),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-025"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_CHECK_PERFORMED",
                    "target_id": "RES-025",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy check for resource RES-025 confirmed CRITICAL status, mandating temporary access.",
                },
            ),
            Action(
                name="approve_access_request",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "expires_on": "2025-08-09 14:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-007 approved by mdavis (U-005). Role ROL-026 granted to user U-029.",
                },
            ),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-029"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "patrick.carter@taucorp.com",
                    "subject": "Your Access Request AR-007 has been Approved",
                    "text_content": "Hi Patrick, your access request AR-007 for role ROL-026 has been approved by Michael Davis. This access is temporary and will expire on 2025-08-09 14:00:00+00:00.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-007",
                "final_status": "APPROVED",
                "is_temporary": True,
                "access_expires_on": "2025-08-09 14:00:00+00:00",
                "audit_trail_complete": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_029",
        instruction="You are Michael Davis, IT Operations Manager. You have been assigned a high-priority, open security ticket in HubSpot (TI-053) regarding a critical SIEM alert. You must conduct a full investigation, take all necessary containment actions as per policy for critical cross-department alerts, and document your findings by updating and closing the ticket.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_hubspot_ticket_by_id", kwargs={"ticket_id": "TI-053"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-012"}),
            
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}),
            Action(name="list_user_sessions", kwargs={"user_id": "U-004"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-005", "action_type": "USER_SESSION_CHECKED", "target_id": "U-004", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Investigator reviewed recent sessions for user U-004 as part of security investigation."}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-004"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-016"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-037"}),

            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-029"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-004", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-016 revoked from user ejones (U-004) as a preventative measure following critical SIEM alert ALRT-012.",
                },
            ),
            
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-030"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-004", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-037 revoked from user ejones (U-004) as a preventative measure following critical SIEM alert ALRT-012.",
                },
            ),

            Action(
                name="update_hubspot_ticket",
                kwargs={
                    "ticket_id": "TI-053", "status": "CLOSED", "closed_at": "2025-08-09 10:00:00+00:00", "timestamp": "2025-08-09 10:00:00+00:00",
                    "description": "Investigation of SIEM alert ALRT-012 complete. User ejones (U-004) was confirmed to be already suspended. As a further preventative measure due to the cross-departmental nature of the alert, the user's 'hr-lead' role (ROL-037) was also revoked. No further action required. Closing ticket.",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "INVESTIGATION_CLOSED", "target_id": "TI-053", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigation complete. HubSpot ticket TI-053 updated with findings and status changed to CLOSED.",
                },
            ),
        ],
        outputs=[json.dumps({"ticket_investigated": "TI-053", "user_investigated": "U-004", "containment_actions": ["user_already_suspended", "all_roles_revoked"], "revoked_roles": ["ROL-016", "ROL-037"], "ticket_final_status": "CLOSED"})],
    ),
    Task(
        annotator="2",
        user_id="task_030",
        instruction=(
            "You are Michael Davis, IT Operations Manager. As part of a routine audit, you need to review the active policy exception PE-010 and ensure it is still compliant with security policies. Take any necessary remediation actions and log the process."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_policy_exception_by_id", kwargs={"exception_id": "PE-010"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-008"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_VIOLATION_IDENTIFIED",
                    "target_id": "PE-010",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Violation found for policy exception PE-010: Exception is active for a user (U-008) who is not in an active state.",
                },
            ),
            Action(name="revoke_policy_exception", kwargs={"exception_id": "PE-010"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_EXCEPTION_REVOKED",
                    "target_id": "PE-010",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy exception PE-010 for user U-008 was revoked due to a policy violation: User is not in an active state.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "COMPLIANCE: Revoked policy exception for user U-008",
                    "description": "Audit of active policy exception PE-010 revealed a policy violation. The exception was active for user Amanda Miller (U-008), whose account status is SUSPENDED. Action Taken: The policy exception was revoked.",
                    "priority": "MEDIUM",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "COMPLIANCE_REMEDIATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "audited_entity_type": "PolicyException",
                "audited_entity_id": "PE-010",
                "policy_violation": "Active exception for suspended user",
                "remediation_action": "Exception revoked",
                "hubspot_ticket_created": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_031",
        instruction=(
            "You are the Certification Bot. It is time to process the in-progress access certification campaign C-016 for the 'lead-generation-db' resource. You must identify all users with access, revoke access for any who are not in the Sales department, and send a summary email to the campaign reviewer upon completion."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "CERTIFICATION_BOT"}),
            Action(name="get_certification_details_by_id", kwargs={"certification_id": "C-016"}),
            Action(name="find_roles_by_resource_id", kwargs={"resource_id": "RES-016"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-015"}),
            Action(
                name="update_certification_status",
                kwargs={
                    "certification_id": "C-016",
                    "new_status": "COMPLETED",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-003"}), 
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-033", 
                    "action_type": "CERTIFICATION_COMPLETED",
                    "target_id": "C-016",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Certification campaign C-016 status updated to COMPLETED by dbrown.",
                },
            ),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-016"}),
            Action(
                name="send_email",
                kwargs={
                    "sender": "certifications@taucorp.com",
                    "receiver": "david.brown@taucorp.com",
                    "subject": "Certification Campaign C-016 Completed",
                    "text_content": "Hi David, this is an automated notification that the certification campaign C-016 for resource lead-generation-db (RES-016) has been completed. A total of 0 users were reviewed. 0 non-compliant role assignments were revoked. No further action is required.",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "certification_id": "C-016",
                "final_status": "COMPLETED",
                "users_reviewed": 0,
                "revocations_made": 0,
                "notification_sent_to": "david.brown@taucorp.com"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_032",
        instruction=(
            "You are Michael Davis, the IT Operations Manager. A new access request (AR-007) for the 'production-web-server-1' requires your review. You must process this request in accordance with all security policies for critical resources."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-007"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-025"}),
            Action(
                name="approve_access_request",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "expires_on": "2025-08-09 14:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-007 approved by mdavis (U-005). Role ROL-026 granted to user U-029.",
                },
            ),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-029"}),
            Action(
                name="send_email",
                kwargs={
                    "sender": "it-operations@taucorp.com",
                    "receiver": "patrick.carter@taucorp.com",
                    "subject": "Your Access Request AR-007 has been Approved",
                    "text_content": "Hi Patrick, your access request AR-007 for role ROL-026 has been approved by Michael Davis. This access is temporary and will expire on 2025-08-09 14:00:00+00:00.",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-007",
                "final_status": "APPROVED",
                "is_temporary": True,
                "access_expires_on": "2025-08-09 14:00:00+00:00",
                "notification_sent_to": "patrick.carter@taucorp.com"
            })
        ],
    ),
     Task(
        annotator="2",
        user_id="task_033",
        instruction=(
            "You are Michael Davis from Operations. A routine audit has flagged that user 'mlopez' in the Sales department may have an inappropriate, manager-level role. Please investigate this potential policy violation. If a violation is confirmed, revoke the inappropriate role, suspend the user's account, and document the incident."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_user_details_by_username", kwargs={"username": "mlopez"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-009"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-013"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-036"}),
            
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "POLICY_VIOLATION_IDENTIFIED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User was assigned the 'sales-lead-manager' role (ROL-013) but is not the designated department lead.",
                },
            ),

            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-023"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-013 revoked from user mlopez (U-009) due to security investigation finding inappropriate access.",
                },
            ),
            
            Action(name="update_user_status", kwargs={"user_id": "U-009", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "USER_SUSPENDED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for mlopez (U-009) suspended due to inappropriate role assignment (UR-023).",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "INVESTIGATION: Suspicious Activity for user U-009 (mlopez)",
                    "description": "Audit-based investigation of user mlopez (U-009) confirmed a policy violation. Finding: User was assigned the 'sales-lead-manager' role (ROL-013) but is not the designated department lead.. Actions Taken: The inappropriate role assignment (UR-023) was revoked, and the user's account has been suspended.. Further review of user's activity is recommended.",
                    "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-005", "category": "SECURITY_INVESTIGATION", "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_investigated": "U-009",
                "investigation_finding": "Inappropriate manager-level role assignment",
                "remediation_actions": ["role_revoked", "user_suspended"],
                "hubspot_ticket_id": "TI-054"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_034",
        instruction=(
            "You are Alex Johnson, the Engineering Lead. A pending access request (AR-020) for the 'engineering-db-schema' role requires your review. Please process this request, ensuring the user meets all policy prerequisites before making a decision."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "ajohnson"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-020"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-013"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-013"}),

            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-004"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-002"}), 
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001", "action_type": "POLICY_VIOLATION_IDENTIFIED", "target_id": "AR-020", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy violation identified for request AR-020: User U-013 does not have prerequisite role ROL-002 for requested role ROL-004.",
                },
            ),
            Action(
                name="reject_access_request",
                kwargs={
                    "request_id": "AR-020", "reviewer_id": "U-001", "timestamp": "2025-08-09 10:00:00+00:00",
                    "rejection_reason": "User does not meet the prerequisites for the requested role.",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001", "action_type": "ACCESS_REJECTED", "target_id": "AR-020", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-020 rejected by ajohnson (U-001). Reason: User does not meet the prerequisites for the requested role.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "it-operations@taucorp.com", "receiver": "brian.taylor@taucorp.com",
                    "subject": "Update on Your Access Request (AR-020)",
                    "text_content": "Hi Brian, your access request (AR-020) for the 'engineering-db-schema' role was rejected. A compliance review found that you do not have the required prerequisite role ('engineering-code-commit'). Please request and receive the prerequisite role before resubmitting this request.",
                },
            ),
        ],
        outputs=[json.dumps({"request_id": "AR-020", "status": "REJECTED", "reason": "PREREQUISITE_NOT_MET"})],
    ),
    Task(
        annotator="2",
        user_id="task_035",
        instruction=(
            "You are Michael Davis, IT Operations Manager. As part of a routine audit, you need to review the active policy exception PE-010 and ensure it is still compliant with security policies. Take any necessary remediation actions and log the process."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_policy_exception_by_id", kwargs={"exception_id": "PE-010"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-008"}),    
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_VIOLATION_IDENTIFIED",
                    "target_id": "PE-010",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Violation found for policy exception PE-010: Exception is active for a user (U-008) who is not in an active state.",
                },
            ),
            Action(name="revoke_policy_exception", kwargs={"exception_id": "PE-010"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_EXCEPTION_REVOKED",
                    "target_id": "PE-010",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy exception PE-010 for user U-008 was revoked due to a policy violation: User is not in an active state.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "COMPLIANCE: Revoked policy exception for user U-008",
                    "description": "Audit of active policy exception PE-010 revealed a policy violation. The exception was active for user amiller (U-008), whose account status is SUSPENDED. Action Taken: The policy exception was revoked.",
                    "priority": "MEDIUM",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "COMPLIANCE_REMEDIATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "audited_entity_type": "PolicyException",
                "audited_entity_id": "PE-010",
                "policy_violation": "Active exception for suspended user",
                "remediation_action": "Exception revoked",
                "hubspot_ticket_created": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_036",
        instruction=(
            "You are Heather Mitchell from HR. Please process the department transfer for Brian Taylor, who is moving from Engineering to Operations. He must retain his 'engineering-db-schema' role for one week to assist with a project handover."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "hmitchell"}),
            Action(name="get_user_details_by_username", kwargs={"username": "btaylor"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-013"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-006"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-028",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-013",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-001 revoked from user btaylor (U-013) as part of department change to Operations.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-db-schema"}),
            Action(
                name="assign_role_to_user",
                kwargs={
                    "user_id": "U-013",
                    "role_id": "ROL-004",
                    "assigned_by": "U-028",
                    "expires_on": "2025-08-16 10:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-028",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-013",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Temporary role ROL-004 assigned to user btaylor (U-013) with a defined expiration.",
                },
            ),
            Action(name="update_user_department", kwargs={"user_id": "U-013", "new_department": "Operations"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-028",
                    "action_type": "USER_DEPARTMENT_CHANGE",
                    "target_id": "U-013",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User btaylor (U-013) department changed to Operations.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-base"}),
            Action(
                name="assign_role_to_user",
                kwargs={
                    "user_id": "U-013",
                    "role_id": "ROL-021",
                    "assigned_by": "U-028",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-028",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-013",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role operations-base (ROL-021) assigned to user btaylor (U-013) as part of department change.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "brian.taylor@taucorp.com",
                    "subject": "Confirmation of Your Department Change",
                    "text_content": "Hi Brian, this email confirms that your department has been successfully changed to Operations. Your previous roles have been revoked and you have been granted the standard 'operations-base' access. Please contact your new manager, Michael Davis, for any additional access you may require.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "michael.davis@taucorp.com",
                    "subject": "Notification: Department Change for Brian Taylor",
                    "text_content": "Hi Michael, this is an automated notification to inform you that Brian Taylor has been transferred to your department (Operations) and has been assigned the standard 'operations-base' role. Please follow up with them regarding any additional access needs.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-013",
                "previous_department": "Engineering",
                "new_department": "Operations",
                "roles_revoked": ["ROL-001"],
                "roles_granted": ["ROL-021"],
                "retained_role_details": {
                    "role_id": "ROL-004",
                    "access_expires_on": "2025-08-16 10:00:00+00:00"
                }
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_037",
        instruction=(
            "You are Michael Davis, the IT Operations Manager. A new high-priority access request (AR-007) for the production web server is pending your review. Please process this request in accordance with all security policies for critical resources."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-007"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-025"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_CHECK_PERFORMED",
                    "target_id": "RES-025",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy check for resource RES-025 confirmed CRITICAL status, mandating temporary access.",
                },
            ),
            Action(
                name="approve_access_request",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "expires_on": "2025-08-09 14:00:00+00:00",
                },
            ),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-029"}), 
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-007 approved by mdavis (U-005). Role ROL-026 granted to user U-029.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "patrick.carter@taucorp.com",
                    "subject": "Your Access Request AR-007 has been Approved",
                    "text_content": "Hi Patrick, your access request AR-007 for role ROL-026 has been approved by Michael Davis. This access is temporary and will expire on 2025-08-09 14:00:00+00:00.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-007",
                "final_status": "APPROVED",
                "is_temporary": True,
                "access_expires_on": "2025-08-09 14:00:00+00:00",
                "notification_sent_to": "patrick.carter@taucorp.com"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_038",
        instruction=(
            "You are Michael Davis, IT Operations Manager. A compliance alert has been triggered for user 'pellis', indicating a possible violation of the temporary access policy for the 'sales-reporting' role. Please investigate, log your findings, and remediate any issues."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_user_details_by_username", kwargs={"username": "pellis"}),
                Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-021"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_VIOLATION_IDENTIFIED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Violation found for user U-021: Role ROL-014 is assigned permanently, violating policy that requires it to be temporary.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-027"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-014 revoked from user pellis (U-021) due to security policy violation: Permanent assignment of a role that must be temporary.",
                },
            ),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-014"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "paul.ellis@taucorp.com",
                    "subject": "Action Required: Your Access Has Been Updated",
                    "text_content": "Hi Paul, a compliance review found that your assignment of the 'sales-reporting' role (ROL-014) was non-compliant with security policy. This role has been revoked. Please submit a new access request if you still require this access.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "COMPLIANCE: Remediated role assignment for user U-021 (pellis)",
                    "description": "Compliance-driven investigation of user pellis (U-021). Finding: User had a permanent assignment (UR-027) for a role that must be temporary (ROL-014). Action Taken: The non-compliant role assignment was revoked.",
                    "priority": "MEDIUM",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "COMPLIANCE_REMEDIATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_investigated": "U-021",
                "policy_violation": "Permanent assignment of a role required to be temporary",
                "remediation_action": "revoked_user_role_id",
                "revoked_user_role_id": "UR-027",
                "hubspot_ticket_created": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_039",
        instruction=(
            "You are Alex Johnson, Engineering Lead. A new access request (AR-020) for the 'engineering-db-schema' role is pending your review. Please process this request, ensuring the user meets all policy prerequisites before making a decision."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "ajohnson"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-020"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-013"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-013"}),

            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-004"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-002"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001", "action_type": "POLICY_VIOLATION_IDENTIFIED", "target_id": "AR-020", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy violation identified for request AR-020: User U-013 does not have prerequisite role ROL-002 for requested role ROL-004.",
                },
            ),
            Action(
                name="reject_access_request",
                kwargs={
                    "request_id": "AR-020", "reviewer_id": "U-001", "timestamp": "2025-08-09 10:00:00+00:00",
                    "rejection_reason": "User does not meet the prerequisites for the requested role.",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001", "action_type": "ACCESS_REJECTED", "target_id": "AR-020", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-020 rejected by ajohnson (U-001). Reason: User does not meet the prerequisites for the requested role.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "it-operations@taucorp.com", "receiver": "brian.taylor@taucorp.com",
                    "subject": "Update on Your Access Request (AR-020)",
                    "text_content": "Hi Brian, your access request (AR-020) for the 'engineering-db-schema' role was rejected. A compliance review found that you do not have the required prerequisite role ('engineering-code-commit'). Please request and receive the prerequisite role before resubmitting this request.",
                },
            ),
        ],
        outputs=[json.dumps({"request_id": "AR-020", "status": "REJECTED", "reason": "PREREQUISITE_NOT_MET"})],
    ),
    Task(
        annotator="2",
        user_id="task_040",
        instruction=(
            "You are the Certification Bot. It is time to process the in-progress access certification campaign C-008 for the 'production-web-server-1' resource, which is owned by the Operations department. You must identify all users with access, revoke access for any who are not in the Operations department, and send a summary email to the campaign reviewer upon completion."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "CERTIFICATION_BOT"}),
            Action(name="get_certification_details_by_id", kwargs={"certification_id": "C-008"}),    
            Action(name="find_roles_by_resource_id", kwargs={"resource_id": "RES-025"}),    
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-021"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-027"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),    
            
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-011"}), 
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-017"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-023"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-029"}),    
            
            Action(
                name="update_certification_status",
                kwargs={
                    "certification_id": "C-008",
                    "new_status": "COMPLETED",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-033",
                    "action_type": "CERTIFICATION_COMPLETED",
                    "target_id": "C-008",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Certification campaign C-008 status updated to COMPLETED on behalf of reviewer mdavis.",
                },
            ),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-025"}),
            Action(
                name="send_email",
                kwargs={
                    "sender": "certifications@taucorp.com",
                    "receiver": "michael.davis@taucorp.com",
                    "subject": "Certification Campaign C-008 Completed",
                    "text_content": "Hi Michael, this is an automated notification that the certification campaign C-008 for resource production-web-server-1 (RES-025) has been completed. A total of 5 users were reviewed. 0 non-compliant role assignments were revoked. No further action is required.",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "certification_id": "C-008",
                "final_status": "COMPLETED",
                "users_reviewed": 5,
                "revocations_made": 0,
                "notification_sent_to": "michael.davis@taucorp.com"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_041",
        instruction=(
            "You are Michael Davis, IT Operations Manager. A compliance audit has flagged a potential ownership conflict for the 'customer-facing-api' (RES-005). Investigate the current owner, 'dtaylor', and their assigned roles. If their roles are inconsistent with owning a critical production resource, reassign ownership to their direct manager and document the remediation."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-005"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-019"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-019"}),
            
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "POLICY_VIOLATION_IDENTIFIED", "target_id": "RES-005", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "POLICY_VIOLATION_IDENTIFIED: User dtaylor (U-019) owns critical resource RES-005 but lacks appropriate permanent roles.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-034"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-001"}),

            Action(name="update_resource_owner", kwargs={"resource_id": "RES-005", "new_owner_id": "U-001"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "RESOURCE_OWNER_CHANGED", "target_id": "RES-005", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Resource RES-005 ownership reassigned from dtaylor (U-019) to ajohnson (U-001) to remediate ownership policy violation.",
                },
            ),

            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "COMPLIANCE_REMEDIATION", "priority": "MEDIUM", "assignee_id": "U-005", "requester_id": "U-005",
                    "subject": "COMPLIANCE: Remediated Ownership for Resource RES-005",
                    "description": "Compliance audit of resource customer-facing-api (RES-005) revealed an ownership violation. The owner, dtaylor (U-019), holds only temporary or non-production roles, which is inconsistent with owning a critical resource. Action Taken: Ownership has been reassigned to their direct manager, ajohnson (U-001).",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "resource_audited": "RES-005",
                "violation_found": "Ownership inconsistent with user roles",
                "remediation_action": "Resource ownership reassigned",
                "old_owner": "U-019",
                "new_owner": "U-001",
                "hubspot_ticket_id": "TI-054"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_042",
        instruction=(
            "You are the RBAC Bot. A routine audit of the access request queue has flagged that request AR-030 for the CRITICAL resource 'employee-data-portal' has been pending for an unusually long time. Investigate the cause of the delay and take all necessary actions to escalate the request to ensure it is reviewed by the appropriate party."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-030"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-022"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-020"}),
            
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}), 
            Action(name="get_role_id_by_name", kwargs={"role_name": "hr-lead"}), 
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-037"}), 
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),

            Action(
                name="update_access_request",
                kwargs={
                    "request_id": "AR-030",
                    "new_reviewer_id": "U-005",
                    "new_status": "PENDING",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031",
                    "action_type": "ACCESS_REQUEST_REVIEWED",
                    "target_id": "AR-030",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-030 reviewed by RBAC_BOT (U-031) and rerouted to correct owner mdavis (U-005).",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "ACTION REQUIRED: Stale Access Request Escalated (AR-030)",
                    "description": "Automated audit identified stale access request AR-030 for user bking (U-022). The designated approver, ejones (U-004), is suspended. The request has been escalated to the Operations Lead for review and manual processing.",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-031",
                    "category": "COMPLIANCE_AUDIT",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_investigated": "AR-030",
                "issue_found": "APPROVER_UNAVAILABLE",
                "unavailable_approver": "U-004",
                "escalation_path_followed": ["U-004", "U-005"],
                "escalation_action_taken": "Rerouted to U-005",
                "hubspot_ticket_created": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_043",
        instruction=(
            "You are the RBAC Bot. A compliance audit has flagged a series of inconsistencies related to access request AR-025. You must conduct a full investigation to determine the root cause of the system failure, document all findings in a HubSpot ticket, and escalate to the Operations Lead."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-025"}),
            
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-020"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-002"}), 

            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-020"}),

            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),

            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "CRITICAL: System Inconsistency in Access Request (AR-025)",
                    "description": "Investigation of access request AR-025 revealed a critical system failure. The request was approved for a SUSPENDED user (sevans, U-020), but the corresponding role (ROL-007) was never granted, leaving the database in an inconsistent state. This indicates a failure in the access provisioning workflow. Escalating for immediate technical review of the approval process and the inconsistent data state.",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-031",
                    "category": "SYSTEM_FAILURE",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),

            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031",
                    "action_type": "SYSTEM_FAILURE_IDENTIFIED",
                    "target_id": "AR-025",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "System failure found for access request AR-025: Request was approved but the role was not granted, resulting in an inconsistent system state.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_investigated": "AR-025",
                "system_failure_found": "PHANTOM_ROLE_GRANT",
                "approved_role_missing": "ROL-007",
                "affected_user": "U-020",
                "escalation_contact": "U-005",
                "hubspot_ticket_created": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_044",
        instruction=(
            "You are Sarah Williams, Marketing Lead. You need to onboard a new Marketing Analyst, Peter Griffin, into the Marketing department. He will require the 'marketing-base' and 'marketing-analytics-read' roles. Ensure no Separation of Duties conflicts are created and notify yourself upon completion."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "swilliams"}),
            Action(
                name="create_user",
                kwargs={
                    "username": "pgriffin",
                    "email": "peter.griffin@taucorp.com",
                    "department": "Marketing",
                    "status": "ACTIVE",
                },
            ),
            Action(name="get_user_details_by_username", kwargs={"username": "pgriffin"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "USER_CREATED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "New user account created via onboarding workflow.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "marketing-base"}),
            Action(
                name="assign_role_to_user",
                kwargs={"user_id": "U-034", "role_id": "ROL-006", "assigned_by": "U-002"},
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role marketing-base (ROL-006) assigned to user pgriffin (U-034) as part of onboarding.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "marketing-analytics-read"}),
            Action(
                name="assign_role_to_user",
                kwargs={"user_id": "U-034", "role_id": "ROL-009", "assigned_by": "U-002"},
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-034",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role marketing-analytics-read (ROL-009) assigned to user pgriffin (U-034) as part of onboarding.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "onboarding@taucorp.com",
                    "receiver": "peter.griffin@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Peter, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "sarah.williams@taucorp.com", # Notifying the manager
                    "subject": "Notification: New Direct Report - Peter Griffin",
                    "text_content": "Hi Sarah, this is an automated notification to inform you that a new employee, Peter Griffin, has been onboarded into your department (Marketing). They have been assigned their initial roles. Please follow up with them regarding any additional access needs.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-034",
                "username": "pgriffin",
                "email": "peter.griffin@taucorp.com",
                "department": "Marketing",
                "status": "ACTIVE",
                "roles": ["marketing-base", "marketing-analytics-read"],
                "manager_notified": "U-002"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_045",
        instruction=(
            "You are Michael Davis, IT Operations Manager. A HIGH severity SIEM alert, ALRT-011, has been triggered for user 'crodriguez' (U-007) attempting to access the 'employee-data-portal' (RES-020). As part of a full forensic investigation, you must review the user's historical access requests and recent sessions to identify any patterns of high-risk behavior before taking all necessary containment and remediation actions."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-011"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-007"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-020"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}),
            Action(name="find_access_requests_by_user_id", kwargs={"user_id": "U-007"}),
            
            Action(name="list_user_sessions", kwargs={"user_id": "U-007"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "USER_SESSION_CHECKED", "target_id": "U-007", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigator reviewed recent sessions for user U-007 as part of security investigation.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-007"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "USER_ROLES_REVIEWED", "target_id": "U-007", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigator reviewed assigned roles for user U-007 as part of security investigation.",
                },
            ),

            Action(name="update_user_status", kwargs={"user_id": "U-007", "new_status": "SUSPENDED"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-005", "action_type": "USER_SUSPENDED", "target_id": "U-007", "timestamp": "2025-08-09 10:00:00+00:00", "details": "User account for U-007 suspended by mdavis in response to critical SIEM alert ALRT-011."}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-003"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-007", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-001 revoked from user crodriguez (U-007) as a preventative measure following critical SIEM alert ALRT-011."}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-004"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-007", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-002 revoked from user crodriguez (U-007) as a preventative measure following critical SIEM alert ALRT-011."}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-005"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-007", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-003 revoked from user crodriguez (U-007) as a preventative measure following critical SIEM alert ALRT-011."}),

            Action(name="get_role_id_by_name", kwargs={"role_name": "hr-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-037"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "security-operations@taucorp.com", "receiver": "michael.davis@taucorp.com",
                    "subject": "ESCALATED: Security Alert on Resource RES-020",
                    "text_content": "Hi Michael, this is an automated notification. A critical security alert (ALRT-011) was triggered on resource employee-data-portal (RES-020). The designated owner is unavailable. As the escalation contact, you are being notified. The user's account has been suspended and an investigation is underway.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "SECURITY_INVESTIGATION", "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-005",
                    "subject": "INVESTIGATION: Cross-Department Access Attempt (ALRT-011)",
                    "description": "Investigation of SIEM alert ALRT-011. Findings: User crodriguez (U-007) from Engineering department attempted to access critical Human Resources resource 'employee-data-portal' (RES-020). A review of historical activity shows a pattern of requests for cross-departmental access (AR-001, AR-033). Actions Taken: User account suspended and all assigned roles (ROL-001, ROL-002, ROL-003) were revoked as a preventative measure.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "alert_investigated": "ALRT-011",
                "violation_found": "Cross-department access attempt with a history of similar requests.",
                "containment_actions": ["user_suspended", "all_roles_revoked"],
                "revoked_roles": ["ROL-001", "ROL-002", "ROL-003"],
                "notification_escalated": True,
                "hubspot_ticket_id": "TI-054"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_046",
        instruction=(
            "You are Jessica Garcia, Finance Lead. A new access request, 'AR-034', from your direct report Stephanie Adams is pending your review. Please conduct a thorough review of the request, ensuring that approving it would not violate any compliance policies, including the principle of Separation of Duties, before making a final decision."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "jgarcia"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-034"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-018"}),
            
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-018"}),
            Action(name="get_user_role_details_by_user_role_id", kwargs={"user_role_id": "UR-051"}),
            Action(name="get_user_role_details_by_user_role_id", kwargs={"user_role_id": "UR-052"}),

            Action(
                name="approve_access_request",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "expires_on": None,
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-034",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-034 approved by jgarcia (U-006). Role ROL-030 granted to user U-018.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "stephanie.adams@taucorp.com",
                    "subject": "Your Access Request AR-034 has been Approved",
                    "text_content": "Hi Stephanie, your access request AR-034 for role ROL-030 has been approved by Jessica Garcia. You have been granted permanent access.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-034",
                "status": "APPROVED",
                "reason": "No active Separation of Duties violation found; conflicting role was expired."
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_047",
        instruction=(
            "You are Ashley Wilson from HR. User rwhite is transferring from Operations to Finance department. Update their department and assign appropriate finance roles while removing operations roles."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "rwhite"}),
            
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-017"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-040"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-021 revoked from user rwhite (U-017) as part of department change to Finance.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-041"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-022 revoked from user rwhite (U-017) as part of department change to Finance.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-042"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-024 revoked from user rwhite (U-017) as part of department change to Finance.",
                },
            ),

            Action(name="update_user_department", kwargs={"user_id": "U-017", "new_department": "Finance"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "USER_DEPARTMENT_CHANGE",
                    "target_id": "U-017",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User rwhite (U-017) department changed to Finance.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "finance-base"}),
            Action(name="assign_role_to_user", kwargs={"user_id": "U-017", "role_id": "ROL-029", "assigned_by": "U-010"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role finance-base (ROL-029) assigned to user rwhite (U-017) as part of department change to Finance.",
                },
            ),

            Action(name="get_role_id_by_name", kwargs={"role_name": "finance-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-039"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-006"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "robert.white@taucorp.com",
                    "subject": "Confirmation of Your Department Change",
                    "text_content": "Hi Robert, this email confirms that your department has been successfully changed to Finance. Your previous roles have been revoked and you have been granted the standard 'finance-base' access. Please contact your new manager, Jessica Garcia, for any additional access you may require.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "jessica.garcia@taucorp.com",
                    "subject": "Notification: Department Change for Robert White",
                    "text_content": "Hi Jessica, this is an automated notification to inform you that Robert White has been transferred to your department (Finance) and has been assigned the standard 'finance-base' role. Please follow up with them regarding any additional access needs.",
                },
            ),

            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "Department Transfer Processed: Robert White (U-017)",
                    "description": "Department transfer completed for user rwhite (U-017) from Operations to Finance. All 3 previous roles were revoked and the standard base role for the new department was assigned. All relevant managers have been notified.",
                    "priority": "MEDIUM",
                    "assignee_id": "U-010",
                    "requester_id": "U-010",
                    "category": "USER_MANAGEMENT",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-017",
                "old_department": "Operations",
                "new_department": "Finance",
                "roles_revoked": ["ROL-021", "ROL-022", "ROL-024"],
                "roles_assigned": ["ROL-029"],
                "transfer_completed": True,
                "hubspot_ticket_id": "TI-054"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_048",
        instruction=(
            "You are the RBAC Bot. A new access request has been posted in the #access-requests Slack channel (message_id: SL-027). Please review it and take the appropriate action."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_slack_message_by_id", kwargs={"message_id": "SL-027"}),
            Action(name="find_access_request_by_details", kwargs={"user_id": "U-007", "resource_id": "RES-002", "role_id": "ROL-002"}),
            
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-007"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-002"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-001"}), 
            Action(
                name="reject_access_request",
                kwargs={
                    "request_id": "AR-027",
                    "reviewer_id": "U-001",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "rejection_reason": "The requested access is redundant. The user's existing roles already provide the necessary permissions.",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "ACCESS_REJECTED",
                    "target_id": "AR-027",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-027 rejected by ajohnson (U-001). Reason: The requested access is redundant. The user's existing roles already provide the necessary permissions.",
                },
            ),

            Action(name="get_user_details_by_id", kwargs={"user_id": "U-007"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-002"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "christopher.rodriguez@taucorp.com",
                    "subject": "Update on Your Access Request (AR-027)",
                    "text_content": "Hi Christopher, your access request (AR-027) for the 'engineering-code-commit' role was rejected as it violates the principle of least privilege. We have confirmed you already have the standard base role for your department, so no further action is needed. Please contact IT Operations if you have further questions.",
                },
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests",
                    "message": "Update on request AR-027: This request has been reviewed by ajohnson and the final status is REJECTED. cc: @crodriguez",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "reply_to_message_id": "SL-027"
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-027",
                "final_status": "REJECTED",
                "rejection_reason": "Redundant access request.",
                "notifications_sent": ["email", "slack"]
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_049",
        instruction=(
            "You are Ashley Wilson from HR. Please process the department transfer for Lisa Anderson, who is moving from the Finance department to the Sales department."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "landerson"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-012"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-048"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-029 revoked from user landerson (U-012) as part of department change to Sales.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-049"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-031 revoked from user landerson (U-012) as part of department change to Sales.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-050"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-032 revoked from user landerson (U-012) as part of department change to Sales.",
                },
            ),
            Action(name="update_user_department", kwargs={"user_id": "U-012", "new_department": "Sales"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "USER_DEPARTMENT_CHANGE", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User landerson (U-012) department changed to Sales.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-base"}),
            Action(name="assign_role_to_user", kwargs={"user_id": "U-012", "role_id": "ROL-011", "assigned_by": "U-010"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_ASSIGNED", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role sales-base (ROL-011) assigned to user landerson (U-012) as part of department change to Sales.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-036"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-003"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "lisa.anderson@taucorp.com",
                    "subject": "Confirmation of Your Department Change",
                    "text_content": "Hi Lisa, this email confirms that your department has been successfully changed to Sales. Your previous roles have been revoked and you have been granted the standard 'sales-base' access. Please contact your new manager, David Brown, for any additional access you may require.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "david.brown@taucorp.com",
                    "subject": "Notification: Department Change for Lisa Anderson",
                    "text_content": "Hi David, this is an automated notification to inform you that Lisa Anderson has been transferred to your department (Sales) and has been assigned the standard 'sales-base' role. Please follow up with them regarding any additional access needs.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-012",
                "previous_department": "Finance",
                "new_department": "Sales",
                "roles_revoked": ["ROL-029", "ROL-031", "ROL-032"],
                "roles_granted": ["ROL-011"],
                "manager_notified": "U-003"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_050",
        instruction=(
            "You are Jessica Garcia, Finance Lead. A new access request, AR-022, from user 'mlopez' is pending your review. Please conduct a thorough review and take the appropriate action based on company policy."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "jgarcia"}),
            
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-022"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-016"}),
            
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-021"}), 
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-009"}),
            
            Action(
                name="update_access_request",
                kwargs={
                    "request_id": "AR-022",
                    "new_reviewer_id": "U-021",
                    "new_status": "PENDING",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                }
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-006",
                    "action_type": "ACCESS_REQUEST_REVIEWED",
                    "target_id": "AR-022",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-022 reviewed by jgarcia (U-006) and rerouted to correct owner pellis (U-021).",
                },
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests",
                    "message": "Update on request AR-022: This request has been reviewed by @jgarcia and rerouted to the correct approver, @pellis. cc: @mlopez",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-022",
                "status": "PENDING",
                "reason": "The reviewer is not the designated approver for the requested resource.",
                "rerouted_to": "U-021"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_051",
        instruction=(
            "You are Ashley Wilson from HR. Please process the offboarding for Paul Ellis, who is leaving the company from the Sales department."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "pellis"}),
            Action(name="update_user_status", kwargs={"user_id": "U-021", "new_status": "DISABLED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-021",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account disabled as part of standard employee offboarding process.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-021"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-025"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-011 revoked from user pellis during offboarding.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-026"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-013 revoked from user pellis during offboarding.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-027"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-021",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-014 revoked from user pellis during offboarding.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-021",
                "final_status": "DISABLED",
                "roles_revoked_count": 3
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_052",
        instruction=(
            "You are the RBAC Bot. A new access request (AR-030) for the 'employee-data-portal' is pending review, but the resource owner is disabled. Process it according to company policy for disabled resource owners by rerouting it to the appropriate escalation contact."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-030"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-020"}),
            
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}), 
            Action(name="get_role_id_by_name", kwargs={"role_name": "hr-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-037"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}), 

            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),

            Action(
                name="update_access_request",
                kwargs={
                    "request_id": "AR-030",
                    "new_reviewer_id": "U-005",
                    "new_status": "PENDING",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),

            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031",
                    "action_type": "ACCESS_REQUEST_REVIEWED",
                    "target_id": "AR-030",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-030 reviewed by RBAC_BOT (U-031) and rerouted to correct owner mdavis (U-005).",
                },
            ),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-022"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-017"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "brittany.king@taucorp.com",
                    "subject": "Update on Your Access Request (AR-030)",
                    "text_content": "Hi Brittany, your access request (AR-030) for the 'hr-employee-data-read' role was reviewed, but the designated resource owner is currently unavailable. The request has been escalated to the Operations Lead for a final decision. No further action is needed from you at this time.",
                },
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "message": "Update on request AR-030: This request has been reviewed by RBAC_BOT. The designated owner is unavailable. This request has been escalated to the Operations Lead, @mdavis, for a final decision. cc: @bking",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-030",
                "final_status": "PENDING",
                "escalation_path_followed": ["U-004", "U-005"],
                "rerouted_to": "U-005",
                "notifications_sent": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_053",
        instruction=(
            "You are the RBAC Bot. A new access request has been posted in the #access-requests Slack channel (message_id: SL-027). Please review it and take the appropriate action."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_slack_message_by_id", kwargs={"message_id": "SL-027"}),
            Action(name="find_access_request_by_details",
                   kwargs={"user_id": "U-007", "resource_id": "RES-002", "role_id": "ROL-002"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-007"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-002"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-001"}),
            Action(
                name="reject_access_request",
                kwargs={
                    "request_id": "AR-027",
                    "reviewer_id": "U-001",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "rejection_reason": "The requested access is redundant. The user's existing roles already provide the necessary permissions.",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001",
                    "action_type": "ACCESS_REJECTED",
                    "target_id": "AR-027",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-027 rejected by ajohnson (U-001). Reason: The requested access is redundant. The user's existing roles already provide the necessary permissions.",
                },
            ),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-007"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-002"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "christopher.rodriguez@taucorp.com",
                    "subject": "Update on Your Access Request (AR-027)",
                    "text_content": "Hi Christopher, your access request (AR-027) for the 'engineering-code-commit' role was rejected as it violates the principle of least privilege. We have confirmed you already have the standard base role for your department, so no further action is needed. Please contact IT Operations if you have further questions.",
                },
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "channel": "#access-requests",
                    "message": "Update on request AR-027: This request has been reviewed by ajohnson and the final status is REJECTED. cc: @crodriguez",
                    "reply_to_message_id": "SL-027"
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-027",
                "final_status": "REJECTED",
                "rejection_reason": "The requested access is redundant. The user's existing roles already provide the necessary permissions."
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_054",
        instruction=(
            "You are Ashley Wilson from HR. Please process the department transfer for Matthew Lopez, who is moving from the Sales department to the Marketing department."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "mlopez"}),

            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-009"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-021"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-011 revoked from user mlopez (U-009) as part of department change to Marketing.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-022"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-012 revoked from user mlopez (U-009) as part of department change to Marketing.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-023"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-013 revoked from user mlopez (U-009) as part of department change to Marketing.",
                },
            ),

            Action(name="update_user_department", kwargs={"user_id": "U-009", "new_department": "Marketing"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "USER_DEPARTMENT_CHANGE",
                    "target_id": "U-009",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User mlopez (U-009) department changed to Marketing.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "marketing-base"}),
            Action(name="assign_role_to_user", kwargs={"user_id": "U-009", "role_id": "ROL-006", "assigned_by": "U-010"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-009",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role marketing-base (ROL-006) assigned to user mlopez (U-009) as part of department change to Marketing.",
                },
            ),

            Action(name="get_role_id_by_name", kwargs={"role_name": "marketing-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-035"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-002"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "matthew.lopez@taucorp.com",
                    "subject": "Confirmation of Your Department Change",
                    "text_content": "Hi Matthew, this email confirms that your department has been successfully changed to Marketing. Your previous roles have been revoked and you have been granted the standard 'marketing-base' access. Please contact your new manager, Sarah Williams, for any additional access you may require.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "sarah.williams@taucorp.com",
                    "subject": "Notification: Department Change for Matthew Lopez",
                    "text_content": "Hi Sarah, this is an automated notification to inform you that Matthew Lopez has been transferred to your department (Marketing) and has been assigned the standard 'marketing-base' role. Please follow up with them regarding any additional access needs.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-009",
                "previous_department": "Sales",
                "new_department": "Marketing",
                "roles_revoked": ["ROL-011", "ROL-012", "ROL-013"],
                "roles_granted": ["ROL-006"]
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_055",
        instruction=(
            "You are David Brown, Sales Lead. A new access request (from Slack message SL-031) for the 'cicd-pipeline-main' resource requires your review. Process this request in accordance with the resource ownership and approval policies."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "dbrown"}),
            Action(name="get_slack_message_by_id", kwargs={"message_id": "SL-031"}),
            Action(name="find_access_request_by_details", kwargs={"user_id": "U-025", "resource_id": "RES-003", "role_id": "ROL-005"}),
            
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-003"}),
            
            Action(
                name="reject_access_request",
                kwargs={
                    "request_id": "AR-031",
                    "reviewer_id": "U-003",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "rejection_reason": "The reviewer is not the designated approver for the requested resource.",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-003",
                    "action_type": "ACCESS_REJECTED",
                    "target_id": "AR-031",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-031 rejected by dbrown (U-003). Reason: The reviewer is not the designated approver for the requested resource.",
                },
            ),
            
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-007"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-025"}),
            
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests",
                    "message": "Update on request AR-031: This request has been reviewed by dbrown and the final status is REJECTED. This request has been rerouted to the correct approver, @crodriguez. cc: @rbaker",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "reply_to_message_id": "SL-031"
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-031",
                "final_status": "REJECTED",
                "rejection_reason": "The reviewer is not the designated approver for the requested resource.",
                "next_action": "Rerouted to correct approver @crodriguez."
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_056",
        instruction=(
            "You are Michael Davis, IT Operations Manager. You need to perform a compliance audit for user 'crodriguez' who has been flagged for having excessive permissions beyond their department requirements. Review and remediate any violations."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_user_details_by_username", kwargs={"username": "crodriguez"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-007"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-003"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-005"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-003 revoked from user crodriguez (U-007) due to security policy violation: Excessive permissions detected during compliance audit.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "COMPLIANCE: Excessive Permissions Remediated for User U-007",
                    "description": "Compliance audit completed for user crodriguez (U-007). Found excessive permissions - revoked role ROL-003 (engineering-prod-access). User now has appropriate base-level access only.",
                    "priority": "MEDIUM",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "COMPLIANCE_REMEDIATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "compliance-system@taucorp.com",
                    "receiver": "christopher.rodriguez@taucorp.com",
                    "subject": "Action Required: Your Access Has Been Updated",
                    "text_content": "Hi Christopher, a compliance review found that your assignment of the 'engineering-prod-access' role (ROL-003) was non-compliant with security policy. This role has been revoked. Please submit a new access request if you still require this access.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_audited": "U-007",
                "compliance_violations_found": 1,
                "roles_revoked": ["ROL-003"],
                "roles_retained": ["ROL-001", "ROL-002"],
                "hubspot_ticket_id": "TI-054"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_057",
        instruction=(
            "You are Jessica Garcia from Finance. You need to onboard a new Finance Analyst, Peter King, into the Finance department. He will require the 'finance-base' and 'finance-read' roles. Ensure no Separation of Duties conflicts are created and notify the new user's manager upon completion."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "jgarcia"}),
            Action(
                name="create_user",
                kwargs={
                    "username": "pking",
                    "email": "peter.king@taucorp.com",
                    "department": "Finance",
                    "status": "ACTIVE",
                },
            ),
            Action(name="get_user_details_by_username", kwargs={"username": "pking"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-006", "action_type": "USER_CREATED", "target_id": "U-034", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "New user account created via onboarding workflow.",
                },
            ),

            Action(name="get_role_id_by_name", kwargs={"role_name": "finance-base"}),
            Action(name="assign_role_to_user", kwargs={"user_id": "U-034", "role_id": "ROL-029", "assigned_by": "U-006"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-006", "action_type": "ROLE_ASSIGNED", "target_id": "U-034", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role finance-base (ROL-029) assigned to user pking (U-034) as part of onboarding.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "finance-read"}),
            Action(name="assign_role_to_user", kwargs={"user_id": "U-034", "role_id": "ROL-030", "assigned_by": "U-006"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-006", "action_type": "ROLE_ASSIGNED", "target_id": "U-034", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role finance-read (ROL-030) assigned to user pking (U-034) as part of onboarding.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "onboarding@taucorp.com", "receiver": "peter.king@taucorp.com",
                    "subject": "Welcome to TauCorp!",
                    "text_content": "Hi Peter, welcome to TauCorp! Your account has been set up and is ready to go. Please log in to complete your profile and get started.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "hr-operations@taucorp.com", "receiver": "jessica.garcia@taucorp.com",
                    "subject": "Notification: New Direct Report - Peter King",
                    "text_content": "Hi Jessica, this is an automated notification to inform you that a new employee, Peter King, has been onboarded into your department (Finance). They have been assigned their initial roles. Please follow up with them regarding any additional access needs.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-034",
                "username": "pking",
                "email": "peter.king@taucorp.com",
                "department": "Finance",
                "status": "ACTIVE",
                "roles": ["finance-base", "finance-read"],
                "manager_notified": "U-006"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_058",
        instruction=(
            "You are Michael Davis, IT Operations Manager. You have received a HIGH severity SIEM alert (ALRT-010) for an unauthorized access attempt. Perform a comprehensive investigation and take all necessary containment actions as per the security incident response policy."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-010"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-029"}),
            Action(name="list_user_sessions", kwargs={"user_id": "U-029"}),
            
            Action(name="update_user_status", kwargs={"user_id": "U-029", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_SUSPENDED",
                    "target_id": "U-029",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for U-029 suspended by mdavis in response to critical SIEM alert ALRT-010.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-029"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-045"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-029",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-021 revoked from user pcarter (U-029) as a preventative measure following critical SIEM alert ALRT-010.",
                },
            ),
            
            Action(name="find_hubspot_ticket_by_description", kwargs={"keyword": "ALRT-010"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "INVESTIGATION_CLOSED",
                    "target_id": "ALRT-010",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigation for SIEM alert ALRT-010 closed. Finding: A previously closed HubSpot ticket (TI-051) already exists for this alert. No further action taken.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "alert_investigated": "ALRT-010",
                "user_suspended": "U-029",
                "investigation_status": "closed",
                "existing_ticket_found": "TI-051",
                "sessions_checked": True,
                "containment_actions": ["user_suspended", "role_revoked"],
                "revoked_roles": ["ROL-021"]
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_059",
        instruction=(
            "You are Michael Davis, IT Operations Manager. You need to perform a compliance audit for user 'landerson' who has been flagged for having excessive permissions beyond their department requirements. Review and remediate any violations."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_user_details_by_username", kwargs={"username": "landerson"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "COMPLIANCE_AUDIT",
                    "target_id": "U-012",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Compliance-driven review of roles initiated for user landerson (U-012) by mdavis.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-012"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-049"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-012",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-031 revoked from user landerson (U-012) due to security policy violation: Excessive permissions detected during compliance audit.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-050"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-012",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-032 revoked from user landerson (U-012) due to security policy violation: Excessive permissions detected during compliance audit.",
                },
            ),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-031"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "compliance-system@taucorp.com",
                    "receiver": "lisa.anderson@taucorp.com",
                    "subject": "Action Required: Your Access Has Been Updated",
                    "text_content": "Hi Lisa, a compliance review found that your assignment of the 'finance-invoice-processor' role (ROL-031) was non-compliant with security policy. This role has been revoked. Please submit a new access request if you still require this access.",
                },
            ),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-032"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "compliance-system@taucorp.com",
                    "receiver": "lisa.anderson@taucorp.com",
                    "subject": "Action Required: Your Access Has Been Updated",
                    "text_content": "Hi Lisa, a compliance review found that your assignment of the 'finance-budget-admin' role (ROL-032) was non-compliant with security policy. This role has been revoked. Please submit a new access request if you still require this access.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "COMPLIANCE: Excessive Permissions Remediated for User U-012",
                    "description": "Compliance audit completed for user landerson (U-012). Found excessive permissions - revoked roles ROL-031 (finance-invoice-processor) and ROL-032 (finance-budget-admin). User now has appropriate base-level access only.",
                    "priority": "MEDIUM",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "COMPLIANCE_REMEDIATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_audited": "U-012",
                "compliance_violations_found": 2,
                "roles_revoked": ["ROL-031", "ROL-032"],
                "roles_retained": ["ROL-029"],
                "notifications_sent": ["lisa.anderson@taucorp.com", "lisa.anderson@taucorp.com"],
                "hubspot_ticket_id": "TI-054"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_060",
        instruction=(
            "You are Ashley Wilson from HR. Please reactivate the account for Robert White, who is returning from leave. As per policy, revoke all his non-base roles and ensure his access is restored to the standard 'operations-base' role for the Operations department."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "rwhite"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-017"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-041"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-017", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-022 revoked from user rwhite (U-017) as part of account reactivation process.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-042"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-017", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-024 revoked from user rwhite (U-017) as part of account reactivation process.",
                },
            ),
            Action(name="update_user_status", kwargs={"user_id": "U-017", "new_status": "ACTIVE"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "USER_STATUS_CHANGE", "target_id": "U-017", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for rwhite (U-017) reactivated upon return from leave.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-021"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "hr-operations@taucorp.com", "receiver": "robert.white@taucorp.com",
                    "subject": "Welcome Back! Your TauCorp Account has been Reactivated",
                    "text_content": "Hi Robert, welcome back to TauCorp! Your account has been reactivated and you have been assigned the standard 'operations-base' role for your department. Please contact your manager, Michael Davis, for any additional access you may require.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "hr-operations@taucorp.com", "receiver": "michael.davis@taucorp.com",
                    "subject": "Notification: User Account Reactivated (Robert White)",
                    "text_content": "Hi Michael, this is an automated notification to inform you that Robert White has returned from leave and their account has been reactivated in your department (Operations). They have been assigned the standard 'operations-base' role. Please follow up with them regarding any additional access needs.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "User Reactivation Processed: Robert White (U-017)",
                    "description": "User reactivation process completed for rwhite (U-017). Account status set to ACTIVE. All 2 non-base roles were revoked and the standard base role for the Operations department was retained. All relevant parties have been notified.",
                    "priority": "MEDIUM",
                    "assignee_id": "U-010",
                    "requester_id": "U-010",
                    "category": "USER_MANAGEMENT",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-017",
                "final_status": "ACTIVE",
                "department": "Operations",
                "roles_revoked": ["ROL-022", "ROL-024"],
                "roles_retained": ["ROL-021"],
                "hubspot_ticket_id": "TI-054"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_061",
        instruction=(
            "You are the RBAC Bot. Michael Davis ('mdavis'), the Operations Lead, has triggered a break-glass procedure for user 'jgreen' to address a critical incident involving the 'production-web-server-1'. Verify Michael's authority as Operations Lead, then grant 'jgreen' temporary emergency write access to 'write-prod-db'."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),            
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-005"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "EMERGENCY_ACCESS_INITIATED",
                    "target_id": "U-023",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Emergency access procedure initiated by mdavis for user jgreen to address a critical incident.",
                },
            ),
            Action(name="get_user_details_by_username", kwargs={"username": "jgreen"}),
            Action(name="get_resource_by_name", kwargs={"resource_name": "production-web-server-1"}),            
            Action(name="get_permission_by_name", kwargs={"permission_name": "write-prod-db", "resource_id": "RES-025"}),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-023",      
                    "permission_id": "P-064", 
                    "justification": "Emergency break-glass access to resolve critical production database outage.",
                    "approved_by": "U-005",   
                    "expires_on": "2025-08-09 14:00:00+00:00",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_EXCEPTION_CREATED",
                    "target_id": "U-023",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Emergency policy exception PE-021 granted to user U-023 for permission P-064. Justification: Emergency break-glass access to resolve critical production database outage.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "EMERGENCY ACCESS: Break-Glass Procedure for User U-023",
                    "description": "Emergency break-glass access granted to user jgreen (U-023) via policy exception PE-021. Requester and approver mdavis (U-005) confirmed as authorized. Access to permission 'write-prod-db' (P-064) on resource 'production-web-server-1' (RES-025) expires at 2025-08-09 14:00:00+00:00.",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "EMERGENCY_ACCESS",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "procedure": "break-glass",
                "approver_verified": True,
                "policy_exception_id": "PE-021",
                "user_id": "U-023",
                "permission_granted": "P-064",
                "ticket_id": "TI-054"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_062",
        instruction=(
            "You are Michael Davis, Operations Lead. As part of a company restructuring, user 'jgarcia' is moving from Finance to the Operations department. Revoke their old roles, update their department, and assign them the standard 'operations-base' role."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_user_details_by_username", kwargs={"username": "jgarcia"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-006"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-046"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-006",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-029 revoked from user jgarcia (U-006) due to department change.",
                },
            ),
            
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-047"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-006",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-039 revoked from user jgarcia (U-006) due to department change.",
                },
            ),

            Action(name="update_user_department", kwargs={"user_id": "U-006", "new_department": "Operations"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_DEPARTMENT_CHANGE",
                    "target_id": "U-006",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User jgarcia (U-006) department changed to Operations.",
                },
            ),

            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-base"}),
            Action(name="assign_role_to_user", kwargs={"user_id": "U-006", "role_id": "ROL-021", "assigned_by": "U-005"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-006",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-021 assigned to user jgarcia (U-006) by mdavis (U-005).",
                },
            ),
            
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "jessica.garcia@taucorp.com",
                    "subject": "Confirmation of Your Department Change",
                    "text_content": "Hi Jessica, this email confirms that your department has been successfully changed to Operations. Your previous roles have been revoked and you have been granted the standard 'operations-base' access. Please contact Michael Davis for any additional access you may require.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_id": "U-006",
                "new_department": "Operations",
                "roles_revoked": ["ROL-029", "ROL-039"],
                "role_assigned": "ROL-021",
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_063",
        instruction=(
            "You are Michael Davis, IT Operations Manager. A routine audit has flagged that an active policy exception, 'PE-010', exists for a suspended user. Investigate this violation, revoke the exception as per policy, and document the remediation."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_policy_exception_by_id", kwargs={"exception_id": "PE-010"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-008"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_VIOLATION_IDENTIFIED",
                    "target_id": "PE-010",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Violation found for policy exception PE-010: Exception is active for a user (U-008) who is not in an active state.",
                },
            ),

            Action(name="revoke_policy_exception", kwargs={"exception_id": "PE-010"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_EXCEPTION_REVOKED",
                    "target_id": "PE-010",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy exception PE-010 for user U-008 was revoked due to a policy violation: User is not in an active state.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "COMPLIANCE: Revoked policy exception for user U-008",
                    "description": "Audit of active policy exception PE-010 revealed a policy violation. The exception was active for user amiller (U-008), whose account status is SUSPENDED. Action Taken: The policy exception was revoked.",
                    "priority": "MEDIUM",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "COMPLIANCE_REMEDIATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "violation_type": "Active exception for suspended user",
                "exception_id": "PE-010",
                "affected_user": "U-008",
                "remediation_taken": "Policy exception revoked",
                "ticket_id": "TI-054"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_064",
        instruction=(
            "You are Michael Davis, Operations Lead. A new Separation of Duties policy prevents any user from holding both the 'operations-base' (ROL-021) and 'operations-server-monitor' (ROL-022) roles simultaneously. Find any users with this toxic combination and remediate the violation by revoking the 'operations-base' role."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-021"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-022"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-017"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-017"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-040"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-017",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-021 revoked from user rwhite (U-017) due to security policy violation: Separation of Duties conflict with role ROL-022.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "compliance-system@taucorp.com",
                    "receiver": "robert.white@taucorp.com",
                    "subject": "Action Required: Your Access Has Been Updated",
                    "text_content": "Hi Robert, a compliance review found that your assignment of the 'operations-base' role (ROL-021) was non-compliant with security policy. This role has been revoked. Please submit a new access request if you still require this access.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "sod_violation_found": True,
                "conflicting_roles": ["ROL-021", "ROL-022"],
                "affected_user": "U-017",
                "remediation_action": "Revoked role ROL-021",
                "notification_sent": "robert.white@taucorp.com"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_065",
        instruction=(
            "You are Michael Davis, Operations Lead. A CRITICAL SIEM alert, 'ALRT-002', has been triggered for user 'nthomas'. Per security policy, you must immediately suspend the user's account and notify their direct manager."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-002"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-014"}),
            
            Action(name="update_user_status", kwargs={"user_id": "U-014", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_SUSPENDED",
                    "target_id": "U-014",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for U-014 suspended by mdavis in response to critical SIEM alert ALRT-002.",
                },
            ),
            
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-014"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-013"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-014",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-006 revoked from user nthomas (U-014) as a preventative measure following critical SIEM alert ALRT-002.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-057"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-014",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-009 revoked from user nthomas (U-014) as a preventative measure following critical SIEM alert ALRT-002.", 
                },
            ),

            Action(name="get_role_id_by_name", kwargs={"role_name": "marketing-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-035"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-002"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "security-operations@taucorp.com",
                    "receiver": "sarah.williams@taucorp.com",
                    "subject": "Security Alert: User Account Suspended (U-014)",
                    "text_content": "Hi Sarah, this is an automated notification to inform you that the account for your direct report, nthomas (U-014), has been temporarily suspended due to a critical security alert (ALRT-002). Please contact Security Operations for more details.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "INVESTIGATION: Suspicious Activity for user U-014 (nthomas)",
                    "description": "Investigation of SIEM alert ALRT-002. Findings: User nthomas (U-014) from Marketing department triggered critical security alert ALRT-002 on resource RES-021. Actions Taken: User account suspended and all assigned roles (ROL-006, ROL-009) were revoked as containment measures per security policy.",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "SECURITY_INVESTIGATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "alert_investigated": "ALRT-002",
                "user_suspended": "U-014",
                "containment_actions": ["user_suspended", "all_roles_revoked"],
                "revoked_roles": ["ROL-006", "ROL-009"],
                "manager_notified": "U-002",
                "hubspot_ticket_created": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_066",
        instruction=(
            "You are Michael Davis, IT Operations Manager. User 'pcarter' has been terminated immediately. Revoke all access, disable the account, and create a 'MEDIUM' severity SIEM alert against the 'global-all-systems' resource to document the event."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_user_details_by_username", kwargs={"username": "pcarter"}),
            
            Action(name="update_user_status", kwargs={"user_id": "U-029", "new_status": "DISABLED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-029",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account disabled as part of standard employee offboarding process.",
                },
            ),
            
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-029"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-045"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-029",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-021 revoked from user pcarter (U-029) during offboarding.",
                },
            ),
            
            Action(name="get_resource_by_name", kwargs={"resource_name": "global-all-systems"}),
            
            Action(
                name="create_siem_alert",
                kwargs={
                    "user_id": "U-029",
                    "resource_id": "RES-001",
                    "alert_type": "USER_TERMINATED",
                    "severity": "MEDIUM",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "SIEM_ALERT_CREATED",
                    "target_id": "ALRT-013",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "SIEM alert ALRT-013 created for USER_TERMINATION on U-029"
                }
            ),
        ],
        outputs=[
            json.dumps({
                "user_terminated": "U-029",
                "account_status": "DISABLED",
                "roles_revoked": ["ROL-021"],
                "security_alert_created": "ALRT-013"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_067",
        instruction=(
            "You are Michael Davis, Operations Lead. You must review and process the pending access request 'AR-007' from user 'pcarter' for the 'operations-system-admin' role, ensuring all security policies are followed."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-007"}),
            
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-029"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-025"}),
            
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_CHECK_PERFORMED",
                    "target_id": "RES-025",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy check for resource RES-025 confirmed CRITICAL status, mandating temporary access.",
                },
            ),
            
            Action(
                name="approve_access_request",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "expires_on": "2025-08-09 14:00:00+00:00", 
                },
            ),
            
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-007",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-007 approved by mdavis (U-005). Role ROL-026 granted to user U-029.",
                },
            ),
            
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "patrick.carter@taucorp.com",
                    "subject": "Your Access Request AR-007 has been Approved",
                    "text_content": "Hi Patrick, your access request AR-007 for role ROL-026 has been approved by Michael Davis. This access is temporary and will expire on 2025-08-09 14:00:00+00:00.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-007",
                "status": "APPROVED",
                "access_type": "temporary",
                "expires_on": "2025-08-09 14:00:00+00:00",
                "notification_sent": "patrick.carter@taucorp.com"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_068",
        instruction=(
            "You are the RBAC Bot. A compliance check has identified that user \'jgarcia\' (U-006), the Finance Lead, inappropriately holds the \'finance-lead\' role (ROL-039) which was assigned by themselves. Remediate this self-assignment violation by revoking the role and notify the user and the appropriate escalation manager as per policy."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_user_details_by_username", kwargs={"username": "jgarcia"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-006"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-039"}),
            
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031",
                    "action_type": "POLICY_VIOLATION_IDENTIFIED",
                    "target_id": "U-006",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy violation identified for user U-006: User self-assigned the finance-lead role (ROL-039).",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-047"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-006",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-039 revoked from user jgarcia (U-006) due to self-assignment violation.",
                },
            ),
            
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "compliance-system@taucorp.com",
                    "receiver": "jessica.garcia@taucorp.com",
                    "subject": "Action Required: Your Access Has Been Updated",
                    "text_content": "Hi Jessica, a compliance review found that your assignment of the \'finance-lead\' role (ROL-039) was non-compliant with security policy. This role has been revoked. Please submit a new access request if you still require this access.",
                },
            ),

            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),            
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),            
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),
            
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "compliance-system@taucorp.com",
                    "receiver": "michael.davis@taucorp.com",
                    "subject": "Compliance Violation Remediated: jgarcia (U-006)",
                    "text_content": "Hi Michael, this is an automated notification. A compliance violation was remediated for user jgarcia (U-006), who had an inappropriate role assignment. The role has been revoked. Full details are available in the compliance dashboard.",
                },
            ),
            
        ],
        outputs=[
            json.dumps({
                "violation_remediated": True,
                "affected_user": "U-006",
                "revoked_role_assignment": "UR-047",
                "notifications_sent": ["jessica.garcia@taucorp.com", "michael.davis@taucorp.com"]
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_069",
        instruction=(
            "You are Alex Johnson, Engineering Lead. A new access request (AR-020) for the 'engineering-db-schema' role is pending your review. Please process this request, ensuring the user meets all policy prerequisites before making a decision."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "ajohnson"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-020"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-013"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-013"}),

            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-004"}), 
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-002"}), 
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001", "action_type": "POLICY_VIOLATION_IDENTIFIED", "target_id": "AR-020", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy violation identified for request AR-020: User U-013 does not have prerequisite role ROL-002 for requested role ROL-004.",
                },
            ),
            Action(
                name="reject_access_request",
                kwargs={
                    "request_id": "AR-020", "reviewer_id": "U-001", "timestamp": "2025-08-09 10:00:00+00:00",
                    "rejection_reason": "User does not meet the prerequisites for the requested role.",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001", "action_type": "ACCESS_REJECTED", "target_id": "AR-020", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-020 rejected by ajohnson (U-001). Reason: User does not meet the prerequisites for the requested role.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "it-operations@taucorp.com", "receiver": "brian.taylor@taucorp.com",
                    "subject": "Update on Your Access Request (AR-020)",
                    "text_content": "Hi Brian, your access request (AR-020) for the 'engineering-db-schema' role was rejected. A compliance review found that you do not have the required prerequisite role ('engineering-code-commit'). Please request and receive the prerequisite role before resubmitting this request.",
                },
            ),
        ],
        outputs=[json.dumps({"request_id": "AR-020", "status": "REJECTED", "reason": "PREREQUISITE_NOT_MET"})],
    ),
    Task(
        annotator="2",
        user_id="task_070",
        instruction=(
            "You are Michael Davis, IT Operations Manager. You must investigate and document the critical SIEM alert \'ALRT-012\', where user ejones attempted to access the Salesforce CRM."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-012"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-014"}),
            Action(name="list_user_sessions", kwargs={"user_id": "U-004"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_SESSION_CHECKED",
                    "target_id": "U-004",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigator reviewed recent sessions for user U-004 as part of security investigation.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-004"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_REVIEWED",
                    "target_id": "U-004",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigator reviewed assigned roles for user U-004 as part of security investigation.",
                },
            ),
            
            Action(name="get_user_role_details_by_user_role_id", kwargs={"user_role_id": "UR-029"}),
            Action(name="get_user_role_details_by_user_role_id", kwargs={"user_role_id": "UR-030"}),

            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-029"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-004",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-016 revoked from user ejones (U-004) as a preventative measure following critical SIEM alert ALRT-012.",
                },
            ),
            
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-030"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-004",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-037 revoked from user ejones (U-004) as a preventative measure following critical SIEM alert ALRT-012.",
                },
            ),
            
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "INVESTIGATION: Suspicious Activity for user U-004 (ejones)",
                    "description": "Investigation of SIEM alert ALRT-012. Findings: User ejones (U-004) from Human Resources department attempted to access resource \'salesforce-crm-prod\' (RES-014). No roles granting this access were found. The attempt was correctly blocked by the system. User was already suspended. Actions Taken: All assigned roles (ROL-016, ROL-037) were revoked as additional containment measures per security policy.",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "SECURITY_INVESTIGATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "alert_investigated": "ALRT-012",
                "investigator": "U-005",
                "finding": "Unauthorized access attempt was successfully blocked. User was already suspended.",
                "containment_actions": ["all_roles_revoked"],
                "revoked_roles": ["ROL-016", "ROL-037"],
                "ticket_created": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_071",
        instruction=(
            "You are the RBAC Bot. A routine audit has flagged user 'landerson' for a potential Segregation of Duties (SoD) violation, as they hold multiple financial roles. Investigate their assigned roles ('finance-invoice-processor' and 'finance-budget-admin') and remediate any toxic combinations by revoking the role tied to the less critical resource."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_user_details_by_username", kwargs={"username": "landerson"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-012"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-031"}), 
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-032"}), 
            Action(name="find_resources_by_role_id", kwargs={"role_id": "ROL-031"}),
            Action(name="find_resources_by_role_id", kwargs={"role_id": "ROL-032"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-031"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-032"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031",
                    "action_type": "POLICY_VIOLATION_IDENTIFIED",
                    "target_id": "U-012",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "SoD violation identified for user U-012: User holds conflicting roles ROL-031 and ROL-032.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-050"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-012",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-032 revoked from user landerson (U-012) due to security policy violation: Separation of Duties conflict with role ROL-031.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "compliance-system@taucorp.com",
                    "receiver": "lisa.anderson@taucorp.com",
                    "subject": "Action Required: Your Access Has Been Updated",
                    "text_content": "Hi Lisa, a compliance review found that your role assignments violated the Segregation of Duties policy. To remediate this, your access to the 'finance-budget-admin' role (ROL-032) has been revoked. No further action is needed from you. Please contact your manager if you have any questions.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "COMPLIANCE: SoD Violation Remediated for User U-012",
                    "description": "Audit identified a Segregation of Duties violation for user landerson (U-012), who held conflicting roles ROL-031 and ROL-032. Action Taken: The less critical role, ROL-032, was revoked to resolve the conflict.",
                    "priority": "MEDIUM",
                    "assignee_id": "U-031",
                    "requester_id": "U-031",
                    "category": "COMPLIANCE_REMEDIATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[json.dumps({"sod_violation_remediated": True, "affected_user": "U-012", "revoked_role": "ROL-032"})],
    ),
    Task(
        annotator="2",
        user_id="task_072",
        instruction=(
            "You are Ashley Wilson, an HR Manager. Process the immediate offboarding for user 'amiller', who has been terminated. Ensure all roles and any active policy exceptions are revoked and that their account is disabled."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "amiller"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-008"}),
            Action(name="get_policy_exception_by_user_id", kwargs={"user_id": "U-008"}),
            Action(name="update_user_status", kwargs={"user_id": "U-008", "new_status": "DISABLED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "USER_STATUS_CHANGE",
                    "target_id": "U-008",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account disabled as part of standard employee offboarding process.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-012"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-008",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-006 revoked from user amiller during offboarding.",
                },
            ),
            Action(name="revoke_policy_exception", kwargs={"exception_id": "PE-010"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "POLICY_EXCEPTION_REVOKED",
                    "target_id": "PE-010",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy exception PE-010 for user U-008 was revoked due to a policy violation: User is not in an active state.",
                },
            ),
        ],
        outputs=[json.dumps({"user_offboarded": "U-008", "account_status": "DISABLED", "roles_revoked": ["ROL-006"], "exceptions_revoked": ["PE-010"]})],
    ),
    Task(
        annotator="2",
        user_id="task_073",
        instruction=(
            "You are Sarah Williams, Marketing Lead. A new access request (AR-021) has been routed to you. Verify if you are the designated approver for the requested resource and take the appropriate action based on policy."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "swilliams"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-021"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-012"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-014"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-026"}),
            Action(
                name="approve_access_request",
                kwargs={
                    "request_id": "AR-021",
                    "reviewer_id": "U-002",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "expires_on": None,
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-002",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-021",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-021 approved by swilliams (U-002). Role ROL-010 granted to user U-026.",
                },
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests",
                    "message": "Update on request AR-021: This request has been reviewed by swilliams and the final status is APPROVED. cc: @aphillips",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "angela.phillips@taucorp.com",
                    "subject": "Your Access Request AR-021 has been Approved",
                    "text_content": "Hi Angela, your access request AR-021 for role ROL-010 has been approved by Sarah Williams. You have been granted permanent access.",
                },
            ),
        ],
        outputs=[json.dumps({"request_id": "AR-021", "status": "APPROVED", "approved_by": "U-002"})],
    ),
    Task(
        annotator="2",
        user_id="task_074",
        instruction=(
            "You are Michael Davis, IT Operations Manager. A forensic audit has flagged a suspicious session ('S-028'). Investigate this session, confirm the associated user's status, notify their direct manager, and escalate by creating a critical SIEM alert and a legal/HR ticket."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_session_details_by_id", kwargs={"session_id": "S-028"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-027"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-036"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-003"}),
            Action(name="get_resource_by_name", kwargs={"resource_name": "global-all-systems"}),
            Action(
                name="create_siem_alert",
                kwargs={
                    "user_id": "U-027",
                    "resource_id": "RES-001",
                    "alert_type": "POTENTIAL_DATA_EXFILTRATION",
                    "severity": "CRITICAL",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "SIEM_ALERT_CREATED",
                    "target_id": "ALRT-013",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "SIEM alert ALRT-013 created for POTENTIAL_DATA_EXFILTRATION on RES-001",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "URGENT: Forensic Investigation of Data Exfiltration by Former Employee (U-027)",
                    "description": "Forensic investigation opened for former employee Gary Campbell (U-027) regarding suspicious access to global-all-systems (RES-001). Anomalous session detected from IP address 172.16.0.23 at 2025-08-03 17:00:00+00:00. SIEM alert ALRT-013 created. Assigning to Legal & HR for follow-up.",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "LEGAL_HR_INVESTIGATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "security-operations@taucorp.com",
                    "receiver": "david.brown@taucorp.com",
                    "subject": "Security Alert: Suspicious Activity on Former Employee Account (U-027)",
                    "text_content": "Hi David, this is an automated notification to inform you that suspicious activity was detected on the account of your former direct report, Gary Campbell (U-027), after their termination. A critical SIEM alert (ALRT-013) has been created and the incident has been escalated to Legal & HR. Please contact Security Operations for more details.",
                },
            ),
        ],
        outputs=[json.dumps({"investigation_subject": "U-027", "suspicious_session": "S-028", "siem_alert_created": "ALRT-013", "ticket_created": "TI-054", "manager_notified": "U-003"})],
    ),
    Task(
        annotator="2",
        user_id="task_075",
        instruction=(
            "You are Michael Davis, IT Operations Manager. A critical SIEM alert (ALRT-001) has been triggered for user 'ajohnson'. As per policy, suspend the user's account, notify their direct manager (escalating if necessary), and document the incident."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-001"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-001"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-002"}),
            
            Action(name="list_user_sessions", kwargs={"user_id": "U-001"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_SESSION_CHECKED",
                    "target_id": "U-001",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigator reviewed recent sessions for user U-001 as part of security investigation.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-001"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_ROLES_REVIEWED",
                    "target_id": "U-001",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigator reviewed assigned roles for user U-001 as part of security investigation.",
                },
            ),
            
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-001"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-034"}),
            
            Action(name="update_user_status", kwargs={"user_id": "U-001", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_SUSPENDED",
                    "target_id": "U-001",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for ajohnson (U-001) suspended by mdavis in response to critical SIEM alert ALRT-001.",
                },
            ),
            
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-001"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-001",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-001 revoked from user ajohnson (U-001) as a preventative measure following critical SIEM alert ALRT-001.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-002"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-001",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-034 revoked from user ajohnson (U-001) as a preventative measure following critical SIEM alert ALRT-001.",
                },
            ),
            
            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-034"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-001"}),
            
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),
            
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "INVESTIGATION: Suspicious Activity for user U-001 (ajohnson)",
                    "description": "Investigation of SIEM alert ALRT-001. Findings: User ajohnson (U-001) from Engineering department triggered UNAUTHORIZED_ACCESS_ATTEMPT alert on resource RES-002. Investigation revealed user held roles ROL-001, ROL-034. Actions Taken: User account suspended and all assigned roles (ROL-001, ROL-034) were revoked as containment measures per security policy.",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "category": "SECURITY_INVESTIGATION",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "security-operations@taucorp.com",
                    "receiver": "michael.davis@taucorp.com",
                    "subject": "ESCALATION: Security Alert - User Account Suspended (U-001)",
                    "text_content": "Hi Michael, this is an automated notification to inform you that the account for user ajohnson (U-001), has been temporarily suspended due to a critical security alert (ALRT-001). This is an escalation notification as their direct manager is not in an active state. Please contact Security Operations for more details.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "alert_investigated": "ALRT-001",
                "user_suspended": "U-001",
                "containment_actions": ["user_suspended", "all_roles_revoked"],
                "revoked_roles": ["ROL-001", "ROL-034"],
                "escalated_to": "U-005",
                "hubspot_ticket_created": True
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_076",
        instruction=(
            "You are Ashley Wilson from HR. As part of a corporate restructuring, user 'jgarcia' is moving from the Finance department to the Operations department. Update their department, revoke their old roles, assign the standard base role for their new department, and send all required notifications."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "jgarcia"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-006"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-046"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-006",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-029 revoked from user jgarcia (U-006) as part of department change to Operations.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-047"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-006",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-039 revoked from user jgarcia (U-006) as part of department change to Operations.",
                },
            ),
            Action(name="update_user_department", kwargs={"user_id": "U-006", "new_department": "Operations"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "USER_DEPARTMENT_CHANGE",
                    "target_id": "U-006",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User jgarcia (U-006) department changed to Operations.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-base"}),
            Action(name="assign_role_to_user", kwargs={"user_id": "U-006", "role_id": "ROL-021", "assigned_by": "U-010"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010",
                    "action_type": "ROLE_ASSIGNED",
                    "target_id": "U-006",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role operations-base (ROL-021) assigned to user jgarcia (U-006) as part of department change to Operations.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "jessica.garcia@taucorp.com",
                    "subject": "Confirmation of Your Department Change",
                    "text_content": "Hi Jessica, this email confirms that your department has been successfully changed to Operations. Your previous roles have been revoked and you have been granted the standard 'operations-base' access. Please contact your new manager, Michael Davis, for any additional access you may require.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "hr-operations@taucorp.com",
                    "receiver": "michael.davis@taucorp.com",
                    "subject": "Notification: Department Change for Jessica Garcia",
                    "text_content": "Hi Michael, this is an automated notification to inform you that Jessica Garcia has been transferred to your department (Operations) and has been assigned the standard 'operations-base' role. Please follow up with them regarding any additional access needs.",
                },
            ),
        ],
        outputs=[json.dumps({"user_id": "U-006", "new_department": "Operations", "notifications_sent": ["jessica.garcia@taucorp.com", "michael.davis@taucorp.com"]})],
    ),
    Task(
        annotator="2",
        user_id="task_077",
        instruction=(
            "You are David Brown, Sales Lead. Complete the access certification campaign 'C-005' for the 'salesforce-crm-prod' resource. Review all users with access and revoke any assignments that are non-compliant with the policy that a user's status must be exactly 'ACTIVE' and their department must be 'Sales'."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "dbrown"}),
            Action(name="get_certification_details_by_id", kwargs={"certification_id": "C-005"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-014"}),
            Action(name="find_roles_by_resource_id", kwargs={"resource_id": "RES-014"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-011"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-014"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-036"}),
            
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-009"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-015"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-021"}),

            Action(name="get_user_details_by_id", kwargs={"user_id": "U-027"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-027"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-028"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-003", "action_type": "ROLE_REVOKED", "target_id": "U-027", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-011 revoked from user gcampbell (U-027) due to failing certification C-005 (user not in an ACTIVE state).",
                },
            ),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-003"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-003"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-019"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-003", "action_type": "ROLE_REVOKED", "target_id": "U-003", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-011 revoked from user dbrown (U-003) due to failing certification C-005 (user not in an ACTIVE state).",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-020"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-003", "action_type": "ROLE_REVOKED", "target_id": "U-003", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-036 revoked from user dbrown (U-003) due to failing certification C-005 (user not in an ACTIVE state).",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-003", "action_type": "CERTIFICATION_COMPLETED", "target_id": "C-005", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Certification campaign C-005 status updated to COMPLETED by dbrown.",
                },
            ),
            Action(name="update_certification_status", kwargs={"certification_id": "C-005", "new_status": "COMPLETED", "timestamp": "2025-08-09 10:00:00+00:00"}),
            Action(
                name="send_email",
                kwargs={
                    "sender": "it-operations@taucorp.com", "receiver": "david.brown@taucorp.com", "subject": "Certification Campaign C-005 Completed",
                    "text_content": "Hi David, this is an automated notification that the certification campaign C-005 for resource salesforce-crm-prod (RES-014) has been completed. A total of 5 users were reviewed. 2 non-compliant users were found, and 3 role assignments were revoked. No further action is required.",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[json.dumps({"certification_id": "C-005", "status": "COMPLETED", "violations_found": 2, "remediated_users": ["U-027", "U-003"]})],
    ),
    Task(
        annotator="2",
        user_id="task_078",
        instruction=(
            "You are Michael Davis, IT Operations Manager. A HIGH severity SIEM alert, 'ALRT-006', has been triggered for user 'sadams'. Per security policy, you must suspend the user's account and notify their direct manager. If the user is a department lead, you must escalate the notification to the Operations Lead."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-006"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-018"}),
            Action(name="update_user_status", kwargs={"user_id": "U-018", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "USER_SUSPENDED",
                    "target_id": "U-018",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for U-018 suspended by mdavis in response to critical SIEM alert ALRT-006.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "finance-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-039"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-006"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "security-operations@taucorp.com",
                    "receiver": "stephanie.adams@taucorp.com",
                    "subject": "Security Alert: Your User Account Has Been Suspended",
                    "text_content": "Hi Stephanie, as a precautionary measure in response to a critical security alert (ALRT-006), your user account has been temporarily suspended. All active sessions have been terminated. Please contact IT Operations to begin the account recovery process.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "security-operations@taucorp.com",
                    "receiver": "jessica.garcia@taucorp.com",
                    "subject": "Security Alert: User Account Suspended (U-018)",
                    "text_content": "Hi Jessica, this is an automated notification to inform you that the account for your direct report, Stephanie Adams (U-018), has been temporarily suspended due to a critical security alert (ALRT-006). Please contact Security Operations for more details.",
                },
            ),
        ],
        outputs=[json.dumps({"alert_investigated": "ALRT-006", "user_suspended": "U-018", "manager_notified": "U-006"})],
    ),
    Task(
        annotator="2",
        user_id="task_079",
        instruction=(
            "You are Michael Davis, IT Operations Manager. An automated audit has flagged a potential security violation for user 'gcampbell'. The user's account is disabled, but may still have active privileges (roles or policy exceptions). Investigate and revoke all associated privileges."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_user_details_by_username", kwargs={"username": "gcampbell"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-027"}),
            Action(name="get_policy_exception_by_user_id", kwargs={"user_id": "U-027"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-028"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-027",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-011 revoked from user gcampbell (U-027) due to policy violation: User is not in an ACTIVE state.",
                },
            ),
            Action(name="revoke_policy_exception", kwargs={"exception_id": "PE-011"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "POLICY_EXCEPTION_REVOKED",
                    "target_id": "U-027",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy exception PE-011 for user U-027 was revoked due to a policy violation: User is not in an active state.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "category": "COMPLIANCE_AUDIT",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "subject": "AUDIT: Inactive User Cleanup for U-027 (gcampbell)",
                    "description": "Audit-based investigation of user gcampbell (U-027) confirmed a policy violation. Finding: User status is DISABLED but they held active privileges. Actions Taken: Role ROL-011 was revoked. Policy Exception PE-011 was revoked. The user now has no active privileges, in compliance with policy.",
                },
            ),
        ],
        outputs=[json.dumps({"user_investigated": "U-027", "violation_found": True, "role_revoked": "ROL-011", "exception_revoked": "PE-011", "hubspot_ticket_created": True})],
    ),
    Task(
        annotator="2",
        user_id="task_080",
        instruction=(
            "You are Michael Davis, IT Operations Manager. A MEDIUM severity SIEM alert 'ALRT-008' has been triggered for an unauthorized access attempt by user 'hmitchell'. Investigate the alert and take appropriate remediation steps according to policy."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-008"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-028"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-009"}),
            Action(name="check_user_sessions_by_id", kwargs={"user_id": "U-028"}), 
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "USER_SESSION_CHECKED", "target_id": "U-028", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigator reviewed recent sessions for user U-028 as part of security investigation.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-028"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-016"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-017"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-020"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-036"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-028", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-020 (hr-benefits-admin) revoked from user hmitchell (U-028) as a preventative measure following investigation of SIEM alert ALRT-008.",
                },
            ),
            Action(name="get_role_id_by_name", kwargs={"role_name": "hr-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-037"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}), 
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}), 
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}), 
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}), 
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "compliance-system@taucorp.com", 
                    "receiver": "michael.davis@taucorp.com",
                    "subject": "Action Required: Your Access Has Been Updated",
                    "text_content": "Hi Michael, this is an automated notification regarding a compliance action for user Heather Mitchell (U-028). Their direct manager is currently unavailable. A preventative action was taken in response to security alert ALRT-008, and their role 'hr-benefits-admin' has been revoked. Full details are in the compliance dashboard.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "category": "SECURITY_INVESTIGATION",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "subject": "INVESTIGATION: Suspicious Activity for user U-028 (hmitchell)",
                    "description": "Investigation of SIEM alert ALRT-008. Findings: User hmitchell (U-028) from Human Resources attempted to access critical resource 'email-marketing-service' (RES-009). The attempt was correctly blocked. A review of recent sessions found no anomalies. As a preventative measure due to the risky behavior, the user's most privileged role, 'hr-benefits-admin' (ROL-020), was revoked. The user's direct manager was found to be unavailable, and the notification was escalated to the Operations Lead.",
                },
            ),
        ],
        outputs=[json.dumps({"alert_investigated": "ALRT-008", "preventative_action_taken": True, "revoked_role": "ROL-020", "notification_escalated": True})],
    ),
    Task(
        annotator="2",
        user_id="task_081",
        instruction="You are Ashley Wilson, HR Specialist. Onboard a new employee, Sarah Lee, into Engineering. As part of her role, she will also require 'engineering-prod-access', so please ensure the standard process is followed by creating a new access request for this privilege.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="create_user", kwargs={"username": "slee", "email": "sarah.lee@taucorp.com", "department": "Engineering", "status": "ACTIVE"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-010", "action_type": "USER_CREATED", "target_id": "U-034", "timestamp": "2025-08-09 10:00:00+00:00", "details": "New user account created via onboarding workflow."}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-base"}),
            Action(name="assign_role_to_user", kwargs={"user_id": "U-034", "role_id": "ROL-001", "assigned_by": "U-010"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-010", "action_type": "ROLE_ASSIGNED", "target_id": "U-034", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role engineering-base (ROL-001) assigned to user slee (U-034) as part of onboarding."}),

            Action(name="get_role_id_by_name", kwargs={"role_name": "engineering-prod-access"}),
            Action(name="find_resources_by_role_id", kwargs={"role_id": "ROL-003"}),
            Action(
                name="create_access_request",
                kwargs={
                    "user_id": "U-034", "role_id": "ROL-003", "resource_id": "RES-002",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "justification": "Additional privileged access required for new employee slee (U-034) as part of standard onboarding for their role.",
                },
            ),
            Action(name="log_audit_event", kwargs={"actor_id": "U-010", "action_type": "ACCESS_REQUEST_CREATED", "target_id": "U-034", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Access request AR-042 created for user slee (U-034)."}),

            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-002"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-001"}),
            Action(
                name="send_email",
                kwargs={
                    "sender": "it-operations@taucorp.com", "receiver": "alex.johnson@taucorp.com",
                    "subject": "Action Required: New Access Request Pending Your Review",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "text_content": "Hi Alex, this is an automated notification that a new access request (AR-042) has been submitted for a resource you own, 'main-application-repo'. The request is for user slee and is pending your review.",
                },
            ),
        ],
        outputs=[json.dumps({"user_created": "U-034", "base_role_assigned": "ROL-001", "access_request_created": "AR-042", "approver_notified": "U-001"})],
    ),
    Task(
        annotator="2",
        user_id="task_082",
        instruction="You are the RBAC Bot. A new access request (AR-030) for the 'employee-data-portal' is pending review. Process it according to company policy for handling requests with unavailable approvers.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),

            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-030"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-020"}),

            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}),

            Action(name="get_role_id_by_name", kwargs={"role_name": "hr-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-037"}),

            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),

            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),

            Action(
                name="update_access_request",
                kwargs={
                    "request_id": "AR-030",
                    "new_reviewer_id": "U-005",
                    "new_status": "PENDING",
                    "timestamp": "2025-08-09 10:00:00+00:00"
                }
            ),

            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031",
                    "action_type": "ACCESS_REQUEST_REVIEWED",
                    "target_id": "AR-030",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-030 reviewed by RBAC_BOT (U-031) and rerouted to correct owner mdavis (U-005)."
                }
            ),

            Action(name="get_user_details_by_id", kwargs={"user_id": "U-022"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "message": "Update on request AR-030: This request has been reviewed by @RBAC_BOT. The designated owner is unavailable. This request has been escalated to the Operations Lead, @mdavis, for a final decision. cc: @bking"
                }
            ),
        ],
        outputs=[json.dumps({
            "request_id": "AR-030",
            "status": "PENDING",
            "reason": "Resource owner is disabled. Request is being rerouted to the appropriate department lead for review.",
            "rerouted_to": "U-005"
        })],
    ),
    Task(
        annotator="2",
        user_id="task_083",
        instruction="You are Lisa Anderson from Financial. Review access request AR-021. Approve it or reject it based on policy while making sure the user has appropriate base-level access.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "landerson"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-021"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-012"}),
            Action(
                name="reject_access_request",
                kwargs={
                    "request_id": "AR-021", "reviewer_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "rejection_reason": "The reviewer is not the designated approver for the requested resource.",
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-012", "action_type": "ACCESS_REJECTED", "target_id": "AR-021", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-021 rejected by landerson (U-012). Reason: The reviewer is not the designated approver for the requested resource.",
                },
            ),

            Action(name="get_user_details_by_id", kwargs={"user_id": "U-026"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-026"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-014"}), # Get correct approver's details (@nthomas)
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests", "timestamp": "2025-08-09 10:00:00+00:00",
                    "message": "Update on request AR-021: This request has been reviewed by landerson and the final status is REJECTED. This request has been rerouted to the correct approver, @nthomas. cc: @aphillips",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "it-operations@taucorp.com", "receiver": "angela.phillips@taucorp.com", "subject": "Update on Your Access Request (AR-021)", "timestamp": "2025-08-09 10:00:00+00:00",
                    "text_content": "Hi Angela, your access request (AR-021) was reviewed, but it was routed to the incorrect approver and has been rerouted. We have confirmed that you already have the standard base role for your department, so no further access changes are needed at this time.",
                },
            ),
        ],
        outputs=[json.dumps({"request_id": "AR-021", "decision": "REJECTED", "rerouted_to": "U-014", "proactive_remediation": "Not required, user already has base role"})],
    ),
    Task(
        annotator="2",
        user_id="task_084",
        instruction="You are Michael Davis, IT Operations Manager. You have been assigned to investigate SIEM alert ALRT-009. Perform a full investigation according to security policy and take all appropriate remediation and notification actions.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-009"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-012"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-041"}),
            Action(name="check_user_sessions_by_id", kwargs={"user_id": "U-012"}),

            Action(name="update_user_status", kwargs={"user_id": "U-012", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "USER_SUSPENDED", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for U-012 suspended by mdavis in response to critical SIEM alert ALRT-009.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-012"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-032"}), 
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-050"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-032 (finance-budget-admin) revoked from user landerson (U-012) as a preventative measure following investigation of SIEM alert ALRT-009.",
                },
            ),

            Action(name="get_role_id_by_name", kwargs={"role_name": "finance-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-039"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-006"}),
            Action(
                name="send_email",
                kwargs={
                    "sender": "security-operations@taucorp.com", "receiver": "jessica.garcia@taucorp.com", "subject": "Security Alert: User Account Suspended (U-012)", "timestamp": "2025-08-09 10:00:00+00:00",
                    "text_content": "Hi Jessica, this is an automated notification to inform you that the account for your direct report, Lisa Anderson (U-012), has been temporarily suspended due to a critical security alert (ALRT-009). Please contact Security Operations for more details.",
                },
            ),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}), 
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}), 
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),
            Action(
                name="send_email",
                kwargs={
                    "sender": "security-operations@taucorp.com", "receiver": "michael.davis@taucorp.com", "subject": "ESCALATED: Security Alert on Resource RES-041", "timestamp": "2025-08-09 10:00:00+00:00",
                    "text_content": "Hi Michael, this is an automated notification. A critical security alert (ALRT-009) was triggered on resource Hiring platform (RES-041). The designated owner is unavailable. As the escalation contact, you are being notified. The user's account has been suspended and an investigation is underway.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "subject": "INVESTIGATION: Suspicious Activity for user U-012 (landerson)",
                    "description": "Investigation of SIEM alert ALRT-009. Findings: User landerson (U-012) from Finance department attempted to access critical resource 'Hiring platform' (RES-041). This cross-department access to a critical resource is a policy violation. Actions Taken: User account suspended and role ROL-032 revoked.",
                    "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-005", "category": "SECURITY_INVESTIGATION", "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
        ],
        outputs=[json.dumps({"alert_investigated": "ALRT-009", "finding": "Cross-department access violation", "containment_actions": ["user_suspended", "role_revoked"], "notifications_sent": True, "escalation_sent": True})],
    ),
    Task(
        annotator="2",
        user_id="task_085",
        instruction="You are Laura Jackson, HR Specialist. Process the department change for user 'aphillips', who is moving from Marketing to Sales.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "ljackson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "aphillips"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-026"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-016"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-016", "action_type": "ROLE_REVOKED", "target_id": "U-026", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-006 revoked from user aphillips (U-026) as part of department change to Sales."}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-017"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-016", "action_type": "ROLE_REVOKED", "target_id": "U-026", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-007 revoked from user aphillips (U-026) as part of department change to Sales."}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-018"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-016", "action_type": "ROLE_REVOKED", "target_id": "U-026", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-010 revoked from user aphillips (U-026) as part of department change to Sales."}),
            Action(name="update_user_department", kwargs={"user_id": "U-026", "new_department": "Sales"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-016", "action_type": "USER_DEPARTMENT_CHANGE", "target_id": "U-026", "timestamp": "2025-08-09 10:00:00+00:00", "details": "User aphillips (U-026) department changed to Sales."}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-base"}),
            Action(name="assign_role_to_user", kwargs={"user_id": "U-026", "role_id": "ROL-011", "assigned_by": "U-016"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-016", "action_type": "ROLE_ASSIGNED", "target_id": "U-026", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role sales-base (ROL-011) assigned to user aphillips (U-026) as part of department change to Sales."}),
            
            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-036"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-003"}),
            Action(
                name="send_email",
                kwargs={
                    "sender": "hr-operations@taucorp.com", "receiver": "angela.phillips@taucorp.com", "subject": "Confirmation of Your Department Change", "timestamp": "2025-08-09 10:00:00+00:00",
                    "text_content": "Hi Angela, this email confirms that your department has been successfully changed to Sales. Your previous roles have been revoked and you have been granted the standard 'sales-base' access. Please contact your new manager, David Brown, for any additional access you may require.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "sender": "hr-operations@taucorp.com", 
                    "receiver": "david.brown@taucorp.com", 
                    "subject": "Notification: Department Change for Angela Phillips", 
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "text_content": "Hi David, this is an automated notification to inform you that Angela Phillips has been transferred to your department (Sales) and has been assigned the standard 'sales-base' role. Please follow up with them regarding any additional access needs.",
                },
            ),
        ],
        outputs=[json.dumps({"user_department_updated": "U-026", "old_roles_revoked": ["ROL-006", "ROL-007", "ROL-010"], "new_role_assigned": "ROL-011", "manager_notified": "U-003"})],
    ),
    Task(
        annotator="2",
        user_id="task_086",
        instruction="You are Michael Davis, Operations Lead. The critical production database system, 'production-web-server-1', is down. Grant emergency database admin access 'admin-db-cluster' to engineer 'rbaker' to resolve the issue.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_user_details_by_username", kwargs={"username": "rbaker"}),
            Action(name="get_resource_by_name", kwargs={"resource_name": "production-web-server-1"}),
            Action(name="get_permission_by_name", kwargs={"permission_name": "admin-db-cluster", "resource_id": "RES-025"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "EMERGENCY_ACCESS_INITIATED",
                    "target_id": "U-025",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Emergency access procedure initiated by mdavis for user rbaker to address a critical incident.",
                },
            ),
            Action(
                name="create_policy_exception",
                kwargs={
                    "user_id": "U-025", "permission_id": "P-090",
                    "justification": "Emergency break-glass access to resolve critical production database outage.",
                    "approved_by": "U-005", "expires_on": "2025-08-09 14:00:00+00:00", "timestamp": "2025-08-09 10:00:00+00:00"
                },
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "POLICY_EXCEPTION_CREATED", "target_id": "U-025", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Emergency policy exception PE-021 granted to user U-025 for permission P-090. Justification: Emergency break-glass access to resolve critical production database outage.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "EMERGENCY_ACCESS", "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-005",
                    "subject": "EMERGENCY ACCESS: Break-Glass Procedure for User U-025",
                    "description": "Emergency break-glass access granted to user rbaker (U-025) via policy exception PE-021. Requester and approver Michael Davis (U-005) confirmed as authorized. Access to permission 'admin-db-cluster' (P-090) on resource 'production-web-server-1' (RES-025) expires at 2025-08-09 14:00:00+00:00.",
                },
            ),
        ],
        outputs=[json.dumps({"exception_created": "PE-021", "user_id": "U-025", "hubspot_ticket_created": True})],
    ),
    Task(
        annotator="2",
        user_id="task_087",
        instruction="You are Ashley Wilson, HR Specialist. Process the offboarding for employee 'aphillips'. Ensure all access is revoked and any owned resources are reassigned to their direct manager.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "aphillips"}),
            Action(name="update_user_status", kwargs={"user_id": "U-026", "new_status": "DISABLED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "USER_STATUS_CHANGE", "target_id": "U-026", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for aphillips (U-026) disabled as part of standard employee offboarding process.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-026"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-016"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-026", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-006 revoked from user aphillips during offboarding."}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-017"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-026", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-007 revoked from user aphillips during offboarding."}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-018"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-026", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-010 revoked from user aphillips during offboarding."}),

            Action(name="find_resources", kwargs={"owner_id": "U-026"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "marketing-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-035"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-002"}),
            Action(name="update_resource_owner", kwargs={"resource_id": "RES-010", "new_owner_id": "U-002"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "RESOURCE_OWNER_CHANGED", "target_id": "RES-010", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Resource RES-010 ownership reassigned from aphillips (U-026) to swilliams (U-002) due to user offboarding.",
                },
            ),
            Action(name="update_resource_owner", kwargs={"resource_id": "RES-013", "new_owner_id": "U-002"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "RESOURCE_OWNER_CHANGED", "target_id": "RES-013", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Resource RES-013 ownership reassigned from aphillips (U-026) to swilliams (U-002) due to user offboarding.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "USER_MANAGEMENT", "priority": "MEDIUM", "assignee_id": "U-010", "requester_id": "U-010",
                    "subject": "Offboarding Complete: Angela Phillips (U-026)",
                    "description": "Offboarding process completed for user aphillips (U-026). Account disabled, all 3 roles revoked. Owned resources RES-010 and RES-013 were reassigned to their manager, swilliams (U-002).",
                },
            ),
        ],
        outputs=[json.dumps({"user_offboarded": "U-026", "roles_revoked": 3, "resources_reassigned": 2, "hubspot_ticket_created": True})],
    ),
    Task(
        annotator="2",
        user_id="task_088",
        instruction="You are Michael Davis, IT Operations Manager. A CRITICAL SIEM alert, 'ALRT-007', has been triggered. Conduct a full investigation and take all necessary containment and remediation actions as per security policy, including notifying the appropriate manager or escalating if they are unavailable.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-007"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-016"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-031"}),
            Action(name="check_user_sessions_by_id", kwargs={"user_id": "U-016"}),
            
            Action(name="update_user_status", kwargs={"user_id": "U-016", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "USER_SUSPENDED", "target_id": "U-016", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for U-016 suspended by mdavis in response to critical SIEM alert ALRT-007.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-016"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-016"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-033"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-016", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-016 (hr-base) revoked from user ljackson (U-016) as a preventative measure following investigation of SIEM alert ALRT-007.",
                },
            ),
            
            Action(name="get_role_id_by_name", kwargs={"role_name": "hr-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-037"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}), 
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}), 
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "security-operations@taucorp.com", "receiver": "michael.davis@taucorp.com",
                    "subject": "ESCALATION: Security Alert - User Account Suspended (U-016)",
                    "text_content": "Hi Michael, this is an automated notification to inform you that the account for user Laura Jackson (U-016) has been temporarily suspended due to a critical security alert (ALRT-007). This is an escalation notification as their direct manager is not in an active state. Please contact Security Operations for more details.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "SECURITY_INVESTIGATION", "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-005",
                    "subject": "INVESTIGATION: Suspicious Activity for user U-016 (ljackson)",
                    "description": "Investigation of SIEM alert ALRT-007. Findings: User ljackson (U-016) from Human Resources department attempted to access general-ledger-db (RES-031), a critical resource. This cross-department access to a critical resource is a policy violation. Actions Taken: User account suspended and role ROL-016 revoked. Notification escalated to Operations Lead due to direct manager's suspended status.",
                },
            ),
        ],
        outputs=[json.dumps({"alert_investigated": "ALRT-007", "violation_found": "Cross-department access attempt", "containment_actions": ["user_suspended", "role_revoked"], "notification_escalated": True, "hubspot_ticket_created": True})],
    ),
    Task(
        annotator="2",
        user_id="task_089",
        instruction="You are Michael Davis, IT Operations Manager. A cross-department access request, AR-030, has been flagged. You must follow the full escalation policy to find the correct approver and, if the escalation path ends with you, make a final decision based on the Principle of Least Privilege.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-030"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-022"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-020"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "hr-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-037"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),

            Action(
                name="approve_access_request",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "expires_on": "2025-08-09 14:00:00+00:00", 
                },
            ),

            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ACCESS_GRANTED",
                    "target_id": "AR-030",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-030 approved by mdavis (U-005). Role ROL-017 granted to user U-022.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "brittany.king@taucorp.com",
                    "subject": "Your Access Request AR-030 has been Approved",
                    "text_content": "Hi Brittany, your access request AR-030 for role ROL-017 has been approved by Michael Davis. This access is temporary and will expire on 2025-08-09 14:00:00+00:00.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "request_id": "AR-030",
                "decision": "APPROVED_TEMPORARY",
                "final_approver": "U-005",
                "access_expires_on": "2025-08-09 14:00:00+00:00"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_090",
        instruction="You are the RBAC Bot. A compliance audit has flagged that access request AR-037 is stale and has been pending for more than 7 days. Investigate why the request is stalled and escalate it according to the multi-step escalation policy.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-037"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-041"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}),
            
            Action(name="get_role_id_by_name", kwargs={"role_name": "hr-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-037"}),
            
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),
            
            Action(
                name="update_access_request",
                kwargs={
                    "request_id": "AR-037",
                    "new_reviewer_id": "U-005",
                    "new_status": "PENDING",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                },
            ),
            
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031",
                    "action_type": "ACCESS_REQUEST_REVIEWED",
                    "target_id": "AR-037",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-037 reviewed by RBAC_BOT (U-031) and rerouted to correct owner mdavis (U-005).",
                },
            ),
            
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-010"}),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "COMPLIANCE_AUDIT", "priority": "MEDIUM", "assignee_id": "U-005", "requester_id": "U-031",
                    "subject": "ACTION REQUIRED: Stale Access Request Escalated (AR-037)",
                    "description": "Automated audit identified stale access request AR-037 for user awilson (U-010). The designated approver, ejones (U-004), is suspended. The request has been escalated to the Operations Lead for review and manual processing.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "it-operations@taucorp.com",
                    "receiver": "ashley.wilson@taucorp.com",
                    "subject": "Update on Your Access Request (AR-037)",
                    "text_content": "Hi Ashley, this is an automated notification. Your access request (AR-037) was identified as stale because the designated approver is unavailable. The request has been escalated and a ticket has been created to ensure it is reviewed. No further action is needed from you at this time.",
                },
            ),
        ],
        outputs=[json.dumps({"stale_request_found": "AR-037", "escalation_required": True, "escalated_to": "U-005", "hubspot_ticket_id": "TI-054"})],
    ),
    Task(
        annotator="2",
        user_id="task_091",
        instruction="You are Michael Davis, IT Operations Manager. A HIGH severity SIEM alert, 'ALRT-003', has been triggered for a cross-department access attempt. Conduct a full investigation and take all necessary containment, remediation, and escalation actions as defined by security policy.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-003"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-009"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-020"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}),
            Action(name="check_user_sessions_by_id", kwargs={"user_id": "U-009"}),
            Action(name="update_user_status", kwargs={"user_id": "U-009", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "USER_SUSPENDED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for U-009 suspended by mdavis in response to critical SIEM alert ALRT-003.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-009"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-021"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-011 revoked from user mlopez (U-009) as a containment measure following critical SIEM alert ALRT-003.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-022"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-012 revoked from user mlopez (U-009) as a containment measure following critical SIEM alert ALRT-003.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-023"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-013 revoked from user mlopez (U-009) as a containment measure following critical SIEM alert ALRT-003.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "SECURITY_INVESTIGATION", "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-005",
                    "subject": "INVESTIGATION: Cross-Department Access Attempt (ALRT-003)",
                    "description": "Investigation of SIEM alert ALRT-003. Findings: User mlopez (U-009) from Sales department attempted to access critical HR resource 'employee-data-portal' (RES-020). This is a policy violation. Actions Taken: User account suspended and all 3 assigned roles revoked. Notification escalated to Operations Lead due to direct manager's non-active status.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "security-operations@taucorp.com", "receiver": "michael.davis@taucorp.com",
                    "subject": "ESCALATION: Security Alert - User Account Suspended (U-009)",
                    "text_content": "Hi Michael, this is an automated notification to inform you that the account for user Matthew Lopez (U-009) has been temporarily suspended due to a critical security alert (ALRT-003). This is an escalation notification as their direct manager is not in an active state. Please contact Security Operations for more details.",
                },
            ),
        ],
        outputs=[json.dumps({"alert_investigated": "ALRT-003", "containment_actions": ["user_suspended", "all_roles_revoked"], "notification_escalated": True, "hubspot_ticket_created": True})],
    ),
    Task(
        annotator="2",
        user_id="task_092",
        instruction="You are the RBAC Bot. A scheduled compliance audit has flagged that user 'sevans' has a 'SUSPENDED' status but still possesses active role assignments. This is a policy violation. You must investigate and remediate this by revoking all of their assigned roles and documenting the action in a compliance ticket.",
        actions=[
            # Phase 1: Investigation
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_user_details_by_username", kwargs={"username": "sevans"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-020"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-014"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031", "action_type": "ROLE_REVOKED", "target_id": "U-020", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-006 revoked from user sevans (U-020) due to policy violation: User is not in an ACTIVE state.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-015"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-031", "action_type": "ROLE_REVOKED", "target_id": "U-020", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-008 revoked from user sevans (U-020) due to policy violation: User is not in an ACTIVE state.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "COMPLIANCE_REMEDIATION", "priority": "MEDIUM", "assignee_id": "U-031", "requester_id": "U-031",
                    "subject": "COMPLIANCE: Remediated active roles for suspended user U-020",
                    "description": "Automated audit of user sevans (U-020) revealed a policy violation. The user's account status is SUSPENDED, but they held 2 active role assignments. Actions Taken: All active roles (UR-014, UR-015) were revoked.",
                },
            ),
        ],
        outputs=[json.dumps({"user_audited": "U-020", "violation": "Active roles on suspended user", "roles_revoked": ["UR-014", "UR-015"], "hubspot_ticket_created": True})],
    ),
    Task(
        annotator="2",
        user_id="task_093",
        instruction="You are Ashley Wilson, HR Specialist. Process the immediate offboarding for employee 'rbaker'. Ensure all roles and any active or expired policy exceptions are revoked and that their account is disabled.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "rbaker"}),
            Action(name="update_user_status", kwargs={"user_id": "U-025", "new_status": "DISABLED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "USER_STATUS_CHANGE", "target_id": "U-025", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account disabled as part of standard employee offboarding process.",
                },
            ),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-025"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-009"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-025", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-001 revoked from user rbaker during offboarding.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-058"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-025", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-003 revoked from user rbaker during offboarding.",
                },
            ),
            Action(name="get_policy_exception_by_user_id", kwargs={"user_id": "U-025", "include_inactive":True}),
            Action(name="revoke_policy_exception", kwargs={"exception_id": "PE-003"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-010", "action_type": "POLICY_EXCEPTION_REVOKED", "target_id": "U-025", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Policy exception PE-003 for user U-025 was revoked during offboarding.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "USER_MANAGEMENT", "priority": "MEDIUM", "assignee_id": "U-010", "requester_id": "U-010",
                    "subject": "Offboarding Complete: rbaker (U-025)",
                    "description": "Offboarding process completed for user rbaker (U-025). Account disabled, 2 roles revoked, and 1 policy exceptions revoked. 0 owned resources found and handled according to policy."
                },
            ),
        ],
        outputs=[json.dumps({"user_offboarded": "U-025", "roles_revoked": 2, "exceptions_revoked": 1, "resources_reassigned": 0})],
    ),
    Task(
        annotator="2",
        user_id="task_094",
        instruction="You are Michael Davis, IT Operations Manager. A CRITICAL SIEM alert, 'ALRT-011', has been triggered. Per security policy, you must perform a full investigation and take all necessary containment actions, including user suspension and revocation of all assigned roles.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-011"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-007"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-020"}),
            Action(name="list_user_sessions", kwargs={"user_id": "U-007"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-007"}),
            
            Action(name="update_user_status", kwargs={"user_id": "U-007", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "USER_SUSPENDED", "target_id": "U-007", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for crodriguez (U-007) suspended due to security policy violation: Critical SIEM alert ALRT-011.",
                },
            ),
            
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-003"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-007", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-001 revoked from user crodriguez (U-007) as a preventative measure following critical SIEM alert ALRT-011.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-004"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-007", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-002 revoked from user crodriguez (U-007) as a preventative measure following critical SIEM alert ALRT-011.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-005"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-007", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-003 revoked from user crodriguez (U-007) as a preventative measure following critical SIEM alert ALRT-011.",
                },
            ),
            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "SECURITY_INVESTIGATION", "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-005",
                    "subject": "INVESTIGATION: Suspicious Activity for user U-007 (crodriguez)",
                    "description": "Investigation of SIEM alert ALRT-011. Findings: User crodriguez (U-007) triggered alert on critical resource RES-020. Investigation revealed user held multiple roles including a temporary role. Actions Taken: User account suspended and all assigned roles (ROL-001, ROL-002, ROL-003) were revoked as containment measures per security policy.",
                },
            ),
        ],
        outputs=[json.dumps({
            "alert_investigated": "ALRT-011", 
            "user_suspended": "U-007", 
            "containment_actions": ["user_suspended", "all_roles_revoked"],
            "revoked_roles": ["ROL-001", "ROL-002", "ROL-003"], 
            "hubspot_ticket_created": True
        })],
    ),
    Task(
        annotator="2",
        user_id="task_095",
        instruction="You are the Certification Bot. It is time to process the quarterly access certification campaign 'C-003'. Review all users with role ROL-003. For any user who is not in the Engineering department or whose status is not 'ACTIVE', revoke their access. For every user found to be compliant, you must add a record to the campaign's audit trail confirming their successful certification.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "CERTIFICATION_BOT"}),
            Action(name="get_certification_details_by_id", kwargs={"certification_id": "C-003"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-003"}),

            Action(name="find_users_with_role", kwargs={"role_id": "ROL-003"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-007"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-033", "action_type": "ACCESS_REVIEW_COMPLETED", "target_id": "U-007", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User crodriguez (U-007) confirmed compliant for role ROL-003 during certification campaign C-003.",
                },
            ),

            Action(name="get_user_details_by_id", kwargs={"user_id": "U-025"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-033", "action_type": "ACCESS_REVIEW_COMPLETED", "target_id": "U-025", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User rbaker (U-025) confirmed compliant for role ROL-003 during certification campaign C-003.",
                },
            ),

            Action(name="update_certification_status", kwargs={"certification_id": "C-003", "new_status": "COMPLETED", "timestamp": "2025-08-09 10:00:00+00:00"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-033", "action_type": "CERTIFICATION_COMPLETED", "target_id": "C-003", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Certification campaign C-003 status updated to COMPLETED by CERTIFICATION_BOT.",
                },
            ),
        ],
        outputs=[json.dumps({"certification_id": "C-003", "status": "COMPLETED", "violations_found": 0, "remediated_users": []})],
    ),
    Task(
        annotator="2",
        user_id="task_096",
        instruction="You are Alex Johnson from Engineering. An access request, 'AR-021', has been assigned to you for review. The request is for the 'blog-cms' resource. Please conduct a thorough review and take all necessary actions in accordance with the principle of least privilege and our standard operating procedures for access approvals.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "ajohnson"}),
            Action(name="get_access_request_by_id", kwargs={"request_id": "AR-021"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-012"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-010"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-026"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-014"}),
            Action(
                name="update_access_request",
                kwargs={"request_id": "AR-021", "new_reviewer_id": "U-014", "new_status": "PENDING"},
            ),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-001", "action_type": "ACCESS_REQUEST_REVIEWED", "target_id": "AR-021", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Access request AR-021 reviewed by ajohnson (U-001) and rerouted to correct owner nthomas (U-014).",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "it-operations@taucorp.com", "receiver": "angela.phillips@taucorp.com",
                    "subject": "Update on Your Access Request (AR-021)",
                    "text_content": "Hi Angela, your access request (AR-021) for the 'marketing-content-editor' role was reviewed, but it was routed to the incorrect approver. The request has been rerouted to the correct resource owner for their review. No further action is needed from you at this time.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "it-operations@taucorp.com", "receiver": "nicole.thomas@taucorp.com",
                    "subject": "Action Required: New Access Request Pending Your Review",
                    "text_content": "Hi Nicole, this is an automated notification that a new access request (AR-021) has been submitted for a resource you own, 'blog-cms'. The request is for user aphillips and is pending your review.",
                },
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel": "#access-requests", "timestamp": "2025-08-09 10:00:00+00:00",
                    "message": "Update on request AR-021: This request has been reviewed by @ajohnson. This request has been rerouted to the correct approver, @nthomas. cc: @aphillips",
                },
            ),
        ],
        outputs=[json.dumps({"request_id": "AR-021", "status": "REROUTED", "new_approver_notified": "U-014"})],
    ),
    Task(
        annotator="2",
        user_id="task_097",
        instruction=(
            "You are Michael Davis, IT Operations Manager. A MEDIUM severity SIEM alert, ALRT-008, has been triggered for user 'hmitchell' attempting to access the 'email-marketing-service'. This represents a risky cross-departmental access attempt. Investigate the incident and, as a preventative measure, revoke the user's most privileged non-base role. Document the incident and actions in a HubSpot ticket and notify the appropriate manager, escalating if necessary."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-008"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-028"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-009"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-014"}),

            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-028"}),
            Action(name="get_role_details_by_id", kwargs={"role_id": "ROL-020"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-036"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005",
                    "action_type": "ROLE_REVOKED",
                    "target_id": "U-028",
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-020 (hr-benefits-admin) revoked from user hmitchell (U-028) as a preventative measure following investigation of SIEM alert ALRT-008.",
                },
            ),

            Action(name="get_role_id_by_name", kwargs={"role_name": "hr-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-037"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-004"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "sender": "compliance-system@taucorp.com",
                    "receiver": "michael.davis@taucorp.com",
                    "subject": "ESCALATED NOTIFICATION: Compliance Action for Heather Mitchell",
                    "text_content": "Hi Michael, this is an automated notification regarding a compliance action for user Heather Mitchell (U-028). Their direct manager is currently unavailable. A preventative action was taken in response to security alert ALRT-008, and their role 'hr-benefits-admin' has been revoked. Full details are in the compliance dashboard.",
                },
            ),

            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00",
                    "category": "SECURITY_INVESTIGATION",
                    "priority": "HIGH",
                    "assignee_id": "U-005",
                    "requester_id": "U-005",
                    "subject": "INVESTIGATION: Cross-Department Access Attempt (ALRT-008)",
                    "description": "Investigation of SIEM alert ALRT-008. Findings: User hmitchell (U-028) from Human Resources department attempted to access critical Marketing resource 'email-marketing-service' (RES-009). The attempt was correctly blocked. As a preventative measure due to the risky behavior, the user's most privileged role, 'hr-benefits-admin' (ROL-020), was revoked. The user's direct manager was found to be unavailable, and the notification was escalated.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "alert_investigated": "ALRT-008",
                "preventative_action_taken": True,
                "revoked_role": "ROL-020",
                "notification_escalated": True,
                "hubspot_ticket_id": "TI-054"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_098",
        instruction="You are Ashley Wilson, HR Specialist. Process the department transfer for user 'pcarter', who is transferring to Sales. Ensure all old roles are revoked, assign the sales-base role, and notify the appropriate management.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "awilson"}),
            Action(name="get_user_details_by_username", kwargs={"username": "pcarter"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-029"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-045"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-010", "action_type": "ROLE_REVOKED", "target_id": "U-029", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-021 revoked from user pcarter (U-029) as part of department change to Sales."}),
            Action(name="update_user_department", kwargs={"user_id": "U-029", "new_department": "Sales"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-010", "action_type": "USER_DEPARTMENT_CHANGE", "target_id": "U-029", "timestamp": "2025-08-09 10:00:00+00:00", "details": "User pcarter (U-029) department changed to Sales."}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-base"}),
            Action(name="assign_role_to_user", kwargs={"user_id": "U-029", "role_id": "ROL-011", "assigned_by": "U-010"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-010", "action_type": "ROLE_ASSIGNED", "target_id": "U-029", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role sales-base (ROL-011) assigned to user pcarter (U-029) as part of department change to Sales."}),

            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-036"}), 
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-003"}),
            
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", 
                    "sender": "hr-operations@taucorp.com", 
                    "receiver": "patrick.carter@taucorp.com", 
                    "subject": "Confirmation of Your Department Change", 
                    "text_content": "Hi Patrick, this email confirms that your department has been successfully changed to Sales. Your previous roles have been revoked and you have been granted the standard 'sales-base' access. Please contact your new manager, David Brown, for any additional access you may require."
                }
            ),

            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", 
                    "sender": "hr-operations@taucorp.com", 
                    "receiver": "david.brown@taucorp.com",
                    "subject": "Notification: Department Change for Patrick Carter",
                    "text_content": "Hi David, this is an automated notification to inform you that Patrick Carter has been transferred to your department (Sales) and has been assigned the standard 'sales-base' role. Please follow up with them regarding any additional access needs.",
                },
            ),
        ],
        outputs=[json.dumps({"user_transferred": "U-029", "new_department": "Sales", "manager_notified": "U-003"})],
    ),
    Task(
        annotator="2",
        user_id="task_099",
        instruction="You are Michael Davis, IT Operations Manager. A high-severity SIEM alert, 'ALRT-003', has been triggered for an unauthorized access attempt by user 'mlopez'. As part of your investigation, you must perform a full forensic review, take all necessary containment actions as defined by the security incident response policy, and notify the appropriate management.",
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "mdavis"}),
            Action(name="get_siem_alert_by_id", kwargs={"alert_id": "ALRT-003"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-009"}),
            Action(name="find_access_requests_by_user_id", kwargs={"user_id": "U-009"}),
            Action(name="get_policy_exception_by_user_id", kwargs={"user_id": "U-009", "include_inactive": True}),
            
            Action(name="list_user_sessions", kwargs={"user_id": "U-009"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "USER_SESSION_CHECKED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigator reviewed recent sessions for user U-009 as part of security investigation.",
                },
            ),

            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-009"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "USER_ROLES_REVIEWED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Investigator reviewed assigned roles for user U-009 as part of security investigation.",
                },
            ),

            Action(name="update_user_status", kwargs={"user_id": "U-009", "new_status": "SUSPENDED"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "USER_SUSPENDED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "User account for mlopez (U-009) suspended due to security policy violation: Pattern of high-risk access attempts.",
                },
            ),
            
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-021"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-011 revoked from user mlopez (U-009) as a preventative measure following critical SIEM alert ALRT-003.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-022"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-012 revoked from user mlopez (U-009) as a preventative measure following critical SIEM alert ALRT-003.",
                },
            ),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-023"}),
            Action(
                name="log_audit_event",
                kwargs={
                    "actor_id": "U-005", "action_type": "ROLE_REVOKED", "target_id": "U-009", "timestamp": "2025-08-09 10:00:00+00:00",
                    "details": "Role ROL-013 revoked from user mlopez (U-009) as a preventative measure following critical SIEM alert ALRT-003.",
                },
            ),

            Action(
                name="create_hubspot_ticket",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "category": "SECURITY_INVESTIGATION", "priority": "HIGH", "assignee_id": "U-005", "requester_id": "U-005",
                    "subject": "INVESTIGATION: Suspicious Activity for user U-009 (mlopez)",
                    "description": "Investigation of SIEM alert ALRT-003. Findings: Unauthorized access attempt detected. A review of the user's history revealed a pattern of high-risk behavior, including a previously rejected access request (AR-005) and a denied policy exception (PE-002). Actions Taken: User account has been SUSPENDED and all assigned roles (ROL-011, ROL-012, ROL-013) were revoked.",
                },
            ),

            Action(name="get_role_id_by_name", kwargs={"role_name": "sales-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-036"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-003"}),
            Action(name="get_role_id_by_name", kwargs={"role_name": "operations-lead"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-038"}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-005"}),
            Action(
                name="send_email",
                kwargs={
                    "timestamp": "2025-08-09 10:00:00+00:00", "sender": "security-operations@taucorp.com", "receiver": "michael.davis@taucorp.com",
                    "subject": "ESCALATION: Security Alert - User Account Suspended (U-009)",
                    "text_content": "Hi Michael, this is an automated notification to inform you that the account for user mlopez (U-009) has been temporarily suspended due to a critical security alert (ALRT-003). This is an escalation notification as their direct manager is not in an active state. Please contact Security Operations for more details.",
                },
            ),
        ],
        outputs=[
            json.dumps({
                "user_investigated": "U-009", "user_suspended": True, "containment_actions": ["user_suspended", "all_roles_revoked"],
                "revoked_roles": ["ROL-011", "ROL-012", "ROL-013"], "hubspot_ticket_id": "TI-054", "escalation_notified": "U-005"
            })
        ],
    ),
    Task(
        annotator="2",
        user_id="task_100",
        instruction=(
            "You are the RBAC Bot, performing a scheduled compliance audit on the 'invoicing-system' (RES-032), a resource critical to the Finance department. You must review all users who have access to this resource. For each user, verify that their department is 'Finance' and their status is 'ACTIVE'. Revoke access for any user who fails this compliance check and document each action."
        ),
        actions=[
            Action(name="get_current_time", kwargs={}),
            Action(name="get_user_details_by_username", kwargs={"username": "RBAC_BOT"}),
            Action(name="get_resource_details_by_id", kwargs={"resource_id": "RES-032"}),
            Action(name="find_roles_by_resource_id", kwargs={"resource_id": "RES-032"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-029"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-032"}),
            Action(name="find_users_with_role", kwargs={"role_id": "ROL-039"}),

            Action(name="get_user_details_by_id", kwargs={"user_id": "U-006"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-031", "action_type": "ACCESS_REVIEW_COMPLETED", "target_id": "U-006", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Resource access review for invoicing-system (RES-032) completed. User jgarcia (U-006) access verified as appropriate for Finance department."}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-012"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-031", "action_type": "ACCESS_REVIEW_COMPLETED", "target_id": "U-012", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Resource access review for invoicing-system (RES-032) completed. User landerson (U-012) access verified as appropriate for Finance department."}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-018"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-031", "action_type": "ACCESS_REVIEW_COMPLETED", "target_id": "U-018", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Resource access review for invoicing-system (RES-032) completed. User sadams (U-018) access verified as appropriate for Finance department."}),
            Action(name="get_user_details_by_id", kwargs={"user_id": "U-024"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-031", "action_type": "ACCESS_REVIEW_COMPLETED", "target_id": "U-024", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Resource access review for invoicing-system (RES-032) completed. User khall (U-024) access verified as appropriate for Finance department."}),

            Action(name="get_user_details_by_id", kwargs={"user_id": "U-030"}),
            Action(name="get_user_roles_by_user_id", kwargs={"user_id": "U-030"}),
            Action(name="revoke_role_from_user", kwargs={"user_role_id": "UR-054"}),
            Action(name="log_audit_event", kwargs={"actor_id": "U-031", "action_type": "ROLE_REVOKED", "target_id": "U-030", "timestamp": "2025-08-09 10:00:00+00:00", "details": "Role ROL-029 revoked from user mcole (U-030) due to policy violation: User is not in an ACTIVE state."}),
            
            Action(name="create_hubspot_ticket", kwargs={"timestamp": "2025-08-09 10:00:00+00:00", "category": "COMPLIANCE_AUDIT", "priority": "MEDIUM", "assignee_id": "U-031", "requester_id": "U-031", "subject": "AUDIT: Resource Access Review - invoicing-system", "description": "Scheduled access review completed for resource invoicing-system (RES-032). Total users reviewed: 5. Users with appropriate access: 4. Found 1 non-compliant user (U-030) whose access was revoked due to non-ACTIVE status."}),
        ],
        outputs=[
            json.dumps({
                "resource_audited": "RES-032",
                "users_reviewed": 5,
                "compliant_users": ["U-006", "U-012", "U-018", "U-024"],
                "violations_found": 1,
                "remediated_users": ["U-030"],
                "hubspot_ticket_id": "TI-054"
            })
        ],
    ),
]    