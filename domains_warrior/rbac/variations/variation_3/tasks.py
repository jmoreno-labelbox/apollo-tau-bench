from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="faris",
        user_id="faris_021_review_ops_blog_editor_assign",
        instruction=(
            "You are U-002 (marketing-lead). You need to review AR-021 for U-026 and make a decision to approve or reject under least-privilege principles "
            "while maintaining audit compliance. Confirm AR-021's pending status, and verify ROL-010's permissions against the target "
            "resource. Provide AR-021 decision status and decision notes."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-002"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-021"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-010"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(name="list_policy_exceptions", kwargs={"user_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-021",
                    "reviewer_id": "U-002",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-021",
                    "reviewer_id": "U-002",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-021"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-021"},
            ),
        ],
        outputs=[{"AR-021": "REJECTED", "NOTES": "Already assigned."}],
    ),
    Task(
        annotator="faris",
        user_id="faris_001_process_revoke",
        instruction=(
            "You are U-005 (operations-lead). You need to decide AR-008 in line with policy, make a decision to approve or reject, and ensure the outcome is auditable. "
            "Reflect the granted access and confirm U-030's roles and active sessions. Check if ROL-002 needs to be revoked from U-007, and revoke it if it does. "
            "Provide AR-008 decision and decision notes."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-032"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-008",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": "Met prerequisite finance-base (ROL-029).",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-008", "assigned_by": "U-005"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-030"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-007"}),
            Action(
                name="check_user_status",
                kwargs={"mode": "revoke", "user_id": "U-007", "role_id": "ROL-002"},
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-008"},
            ),
        ],
        outputs=[
            {"AR-008": "APPROVED", "NOTES": "Met prerequisite finance-base (ROL-029)."}
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_002_process_multiple",
        instruction=(
            "You are U-005 (operations-lead). You need to apply policy to decide AR-021 and AR-022, make a decision to approve or reject for each, and ensure each outcome is auditable. "
            "Summarize roles for U-009 & U-026 and active sessions for U-009. Reduce excess access by removing ROL-004 from U-019 and confirm. "
            "Focus only on the named records. Confirm both requests and the revocation processed."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-021"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-021",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-021",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-021"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-021"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-022"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-009"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-022",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-022",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-022"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-009"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-019"}),
            Action(
                name="check_user_status",
                kwargs={"mode": "revoke", "user_id": "U-019", "role_id": "ROL-004"},
            ),
            Action(
                name="revoke_role",
                kwargs={
                    "user_id": "U-019",
                    "role_id": "ROL-004",
                    "actor_id": "U-005",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-019"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "revoke_role", "target_id": "U-019:ROL-004"},
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-022"},
            ),
            Action(name="get_user_sessions", kwargs={"user_id": "U-009"}),
        ],
        outputs=[
            {
                "AR-021": "REJECTED",
                "AR-022": "REJECTED",
                "U-019_ROL-004": "REVOKED",
                "U-019_ROLES": ["ROL-001", "ROL-005"],
                "U-009_SESSIONS": [],
                "U-009_ROLES": ["ROL-011", "ROL-012", "ROL-013"],
                "U-026_ROLES": ["ROL-006", "ROL-007", "ROL-010"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_003_mixed_reviews",
        instruction=(
            "You are U-005 (operations-lead). You need to use policy to decide AR-040 and AR-034 with auditable outcomes; assign on approval and verify roles. "
            "Right-size U-013 by removing ROL-001, then confirm. Provide both decisions and decision notes."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-040"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-014"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-040",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-040",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-034",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(
                name="grant_role",
                kwargs={
                    "request_id": "AR-034",
                    "assigned_by": "U-005",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-014"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-013"}),
            Action(
                name="check_user_status",
                kwargs={"mode": "revoke", "user_id": "U-013", "role_id": "ROL-001"},
            ),
            Action(
                name="revoke_role",
                kwargs={
                    "user_id": "U-013",
                    "role_id": "ROL-001",
                    "actor_id": "U-005",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-013"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-034"},
            ),
        ],
        outputs=[
            {
                "AR-040": "REJECTED",
                "AR-034": "APPROVED",
                "NOTES": (
                    "Certification verified; within clearance and least-privilege."
                ),
                "U-013_ROL-001": "REVOKED",
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_004_review_only",
        instruction=(
            "You are U-005 (operations-lead). You need to review AR-037 and decide it under least-privilege principles while maintaining audit compliance. "
            "Return the decision, notes and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-037"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-037",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-037",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-037"},
            ),
        ],
        outputs=[
            {
                "AR-037": "REJECTED",
                "NOTES": "Already assigned.",
                "AUDIT_LOG_ID": ["LOG-AR-037-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_005_admin",
        instruction=(
            "You are U-005 (operations-lead). Decide AR-007 under policy with an auditable outcome. "
            "Return the decision, notes and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-007"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-007"},
            ),
        ],
        outputs=[
            {
                "AR-007": "REJECTED",
                "NOTES": "Requested role does not cover target resource",
                "AUDIT_LOG_ID": ["LOG-AR-007-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_006_process_hr",
        instruction=(
            "You are U-005 (operations-lead). You need to decide AR-030 according to policy. "
            "Reflect any granted access for U-022 and confirm roles and session status. Provide AR-030 decision."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-030"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-022"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-022"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-030", "assigned_by": "U-005"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-022"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-022"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-030"},
            ),
        ],
        outputs=[{"AR-030": "APPROVED"}],
    ),
    Task(
        annotator="faris",
        user_id="faris_007_process_marketing",
        instruction=(
            "You are U-005 (operations-lead). Decide AR-009 under least-privilege principles and make a decision to approve or reject while maintaining audit compliance. "
            "Return the decision, notes, the requester's roles and active sessions and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-009"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-009",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-009",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-026"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-009"},
            ),
        ],
        outputs=[
            {
                "AR-009": "REJECTED",
                "NOTES": "Requested role does not cover target resource.",
                "U-026_SESSIONS": [],
                "U-026_ROLES": ["ROL-006", "ROL-007", "ROL-010"],
                "AUDIT_LOG_ID": ["LOG-AR-009-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_008_process_verify_AR_009",
        instruction=(
            "You are U-005. Decide AR-009 per policy and make a decision to approve or reject. Ensure the decision is auditable. "
            "Verify the requester's roles and active sessions after the decision. Return status + roles + sessions and audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-009"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-008"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-009",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-009",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-026"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-009"},
            ),
        ],
        outputs=[
            {
                "AR-009": "REJECTED",
                "NOTES": "Requested role does not cover target resource.",
                "U-026_SESSIONS": [],
                "U-026_ROLES": ["ROL-006", "ROL-007", "ROL-010"],
                "AUDIT_LOG_ID": ["LOG-AR-009-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_009_review_AR_007_admin_audit",
        instruction=(
            "You are U-005 (operations-lead), and there are no incidents at the moment. You need to review AR-007 under policy and make a decision to approve or reject. "
            "Return the decision, notes and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-007"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-007"},
            ),
        ],
        outputs=[
            {
                "AR-007": "REJECTED",
                "NOTES": "Requested role does not cover target resource.",
                "AUDIT_LOG_ID": ["LOG-AR-007-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_010_process_AR_030_verify_U_022",
        instruction=(
            "You are U-005 (operations-lead). You need to review AR-030 according to policy, make a decision to approve or reject, while ensuring audit compliance and user notification. "
            "If approved, U-022 must receive the granted role and an email notification. Return the decision, notes, and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-030"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-022"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-030", "assigned_by": "U-005"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-022"}),
            Action(name="get_user_email", kwargs={"user_id": "U-022"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "brittany.king@taucorp.com",
                    "subject": "AR-030 APPROVED",
                    "text_content": "U-005 2024-06-26 16:05:00+00:00",
                },
            ),
        ],
        outputs=[
            {
                "AR-030": "APPROVED",
                "NOTES": (
                    "Certification verified; within clearance and least-privilege."
                ),
                "AUDIT_LOG_ID": ["LOG-AR-030-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_011_review_duplicate_AR_021",
        instruction=(
            "You are U-005 (operations-lead). You need to review AR-021 against policy and make a decision to approve or reject (including duplication checks if applicable). "
            "The final state must show the decided request and related audit entries. Provide AR-021 decision and decision notes."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-021"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-021",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="review_access_request",
                kwargs={
                    "request_id": "AR-021",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-021"},
            ),
        ],
        outputs=[{"AR-021": "REJECTED", "NOTES": "Already assigned."}],
    ),
    Task(
        annotator="faris",
        user_id="faris_012_review_duplicate_ar_022",
        instruction=(
            "You are U-005 (operations-lead). You need to review AR-022 against policy and make a decision to approve or reject (including duplication checks if applicable). "
            "The final state must show the decided request and audit log id for AR-022. Provide AR-022 decision and decision notes."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-022"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-009"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-022",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="review_access_request",
                kwargs={
                    "request_id": "AR-022",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-022"},
            ),
        ],
        outputs=[
            {
                "AR-022": "REJECTED",
                "NOTES": "Already assigned.",
                "AUDIT_LOG_ID": ["LOG-AR-022-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_013_process_ar_034_verify_u_018",
        instruction=(
            "You are U-005 (operations-lead). You need to review AR-034 under least-privilege principles while maintaining complete audit compliance. "
            "Return the decision, notes, the requester's roles, active sessions and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-034",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-034", "assigned_by": "U-005"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-018"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-034"},
            ),
        ],
        outputs=[
            {
                "AR-034": "APPROVED",
                "NOTES": (
                    "Certification verified; within clearance and least-privilege."
                ),
                "U-018_ROLES": ["ROL-029", "ROL-030"],
                "U-018_SESSIONS": [],
                "AUDIT_LOG_ID": ["LOG-AR-034-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_014_rightsize_u_019_remove_rol_004",
        instruction=(
            "You are U-005 (operations-lead). You need to review ROL-004 from U-019 as part of access right-sizing operations. "
            "The revocation must be completed with audit trail evidence and confirmation of U-019's resulting role state. "
            "Confirm role revoked and U-019's roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-019"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-004"}),
            Action(
                name="check_user_status",
                kwargs={"mode": "revoke", "user_id": "U-019", "role_id": "ROL-004"},
            ),
            Action(
                name="revoke_role",
                kwargs={
                    "user_id": "U-019",
                    "role_id": "ROL-004",
                    "actor_id": "U-005",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-019"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "revoke_role", "target_id": "U-019:ROL-004"},
            ),
            Action(name="get_user_sessions", kwargs={"user_id": "U-019"}),
        ],
        outputs=[{"ROL-004": "REMOVED", "U-019_ROLES": ["ROL-001", "ROL-005"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_015_process_ar_008_with_prereq_check",
        instruction=(
            "You are U-005 (operations-lead). You need to review AR-008 only if policy requirements are satisfied, with complete audit compliance. "
            "Upon approval, U-030 must receive the granted role. The final state must include U-030's updated roles and active sessions with complete audit documentation. "
            "Also, provide AR-008 decision, the requester's roles, active sessions and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-008",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": "Met prerequisite finance-base (ROL-029).",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-008", "assigned_by": "U-005"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-030"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-008"},
            ),
        ],
        outputs=[
            {
                "AR-008": "APPROVED",
                "U-030_ROLES": ["ROL-029", "ROL-032"],
                "U-030_SESSIONS": [],
                "AUDIT_LOG_ID": ["LOG-AR-008-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_016_suspend_excess_remove_rol_001_u_013",
        instruction=(
            "You are U-005 (operations-lead). You need to review U-013's roles and revoke ROL-001 to eliminate excess access privileges. "
            "The operation must be completed with auditable evidence confirming the role revocation and U-013's resulting access state. "
            "Confirm role revoked and U-013's roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-013"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "revoke",
                    "user_id": "U-013",
                    "role_id": "ROL-001",
                },
            ),
            Action(
                name="revoke_role",
                kwargs={
                    "user_id": "U-013",
                    "role_id": "ROL-001",
                    "actor_id": "U-005",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-013"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "revoke_role", "target_id": "U-013:ROL-001"},
            ),
        ],
        outputs=[{"ROL-001": "REMOVED", "U-013_ROLES": []}],
    ),
    Task(
        annotator="faris",
        user_id="faris_017_review_admin_request_audit",
        instruction=(
            "You are U-005 (operations-lead). You need to review AR-007 according to policy. There are no incidents at the moment. "
            "Check the access request after the decision. Return the decision, notes, the requester's roles, active sessions and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-007"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-026"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-007"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-029"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-007"},
            ),
        ],
        outputs=[
            {
                "AR-007": "REJECTED",
                "NOTES": "Requested role does not cover target resource.",
                "U-029_ROLES": ["ROL-021"],
                "U-029_SESSIONS": [],
                "AUDIT_LOG_ID": ["LOG-AR-007-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_018_process_finance_read_assign_verify",
        instruction=(
            "You are U-006 (finance-lead). You need to review AR-034 according to policy, and make a decision to approve or reject. "
            "Upon approval, U-018's roles must reflect the granted access. "
            "Return AR-034 decision, decision notes, U-018's updated roles, and audit log evidence."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-030"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-034", "assigned_by": "U-006"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-034"},
            ),
        ],
        outputs=[
            {
                "AR-034": "APPROVED",
                "NOTES": (
                    "Certification verified; within clearance and least-privilege."
                ),
                "U-018_ROLES": ["ROL-029", "ROL-030"],
                "AUDIT_LOG_ID": ["LOG-AR-034-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_019_review_duplicate_marketing_editor",
        instruction=(
            "You are U-005 (operations-lead). You need to review AR-021 if it represents duplicative access (requester already holds the target role). "
            "The outcome must focus exclusively on AR-021 and U-026 with auditable evidence. "
            "Confirm AR-021 status and the reason for rejection. Provide AR-021 decision and decision notes."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-021"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-021",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-021",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-021"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-021"},
            ),
        ],
        outputs=[{"AR-021": "REJECTED", "NOTES": "Already assigned."}],
    ),
    Task(
        annotator="faris",
        user_id="faris_020_review_duplicate_sales_lead_manager",
        instruction=(
            "You are U-003 (sales-lead). You need to review AR-022 if it represents duplicative access (requester already holds the target role). "
            "The outcome must focus exclusively on AR-022 and U-009 with auditable evidence. "
            "Confirm AR-022 status and the reason for rejection. Provide AR-022 decision and decision notes."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-003"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-022"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-009"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-022",
                    "reviewer_id": "U-003",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-022",
                    "reviewer_id": "U-003",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-022"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-022"},
            ),
        ],
        outputs=[{"AR-022": "REJECTED", "NOTES": "Already assigned."}],
    ),
    Task(
        annotator="faris",
        user_id="faris_022_rightsize_remove_eng_schema_from_u_019",
        instruction=(
            "You are U-005 (operations-lead). You need to review U-019's roles and revoke ROL-004 to eliminate excess access privileges. "
            "The operation must be completed with auditable evidence confirming the role revocation and U-019's resulting access state. "
            "Confirm role revoked and U-019's roles and active sessions."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-019"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-004"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "revoke",
                    "user_id": "U-019",
                    "role_id": "ROL-004",
                },
            ),
            Action(
                name="revoke_role",
                kwargs={
                    "user_id": "U-019",
                    "role_id": "ROL-004",
                    "actor_id": "U-005",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-019"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-019"}),
        ],
        outputs=[
            {
                "ROL-004": "REMOVED",
                "U-019_ROLES": ["ROL-001", "ROL-005"],
                "U-019_SESSIONS": [],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_023_review_only_list_pending_prove_status",
        instruction=(
            "You are U-005 (operations-lead). You need to review AR-027 from the pending request queue with auditable results. "
            "Return the decision, notes, U-007's roles and active sessions and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-027"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-002"}),
            Action(name="list_audit_logs", kwargs={"target_id": "RES-002"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-027",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-027",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-007"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-007"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-027"},
            ),
        ],
        outputs=[
            {
                "U-007_ROLES": ["ROL-001", "ROL-002"],
                "U-007_SESSIONS": [],
                "AR-027": "REJECTED",
                "NOTES": "Already assigned.",
                "AUDIT_LOG_ID": ["LOG-AR-027-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_024_create_review_process_new_request_AR_101",
        instruction=(
            "You are U-005 (operations-lead). You need to create AR-101 for U-015 requesting ROL-015 on RES-015 with the justification 'Commission-view access on RES-015.' and then decide it according to policy. "
            "Confirm AR-101 status, decision notes and audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(
                name="create_access_request",
                kwargs={
                    "request_id": "AR-101",
                    "user_id": "U-015",
                    "resource_id": "RES-015",
                    "requested_role_id": "ROL-015",
                    "justification": "Commission-view access on RES-015.",
                    "submitted_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-101"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-015"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-015"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-101",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-101",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-101"}),
        ],
        outputs=[
            {
                "AR-101": "REJECTED",
                "NOTES": "Requested role does not cover target resource.",
                "AUDIT_LOG_ID": ["LOG-AR-101-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_025_create_review_admin_like_AR_102",
        instruction=(
            "You are U-005 (operations-lead). You need to create AR-102 for U-029 requesting ROL-026 on RES-025 with the justification 'Operations system admin access.' and then review it based on least-privilege policy restrictions. Ensure full audit compliance throughout the process. "
            "Provide AR-102 status, decision notes and audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(
                name="create_access_request",
                kwargs={
                    "request_id": "AR-102",
                    "user_id": "U-029",
                    "resource_id": "RES-025",
                    "requested_role_id": "ROL-026",
                    "justification": "Operations system admin access.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-102"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-102",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-102",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-102"},
            ),
        ],
        outputs=[
            {
                "AR-102": "REJECTED",
                "NOTES": "Requested role does not cover target resource.",
                "AUDIT_LOG_ID": ["LOG-AR-102-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_026_prereq_gate_finance_admin_AR_103",
        instruction=(
            "You are U-006 (finance-lead). You need to create AR-103 for U-030 requesting ROL-032 on RES-032 with "
            "the justification 'Budget administration for Q3.' and then review it under least-privilege principles and make a decision to approve or reject. "
            "Return the decision, updated roles, notes, and the audit log id, include the sessions for U-030 if "
            "there are any."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(
                name="create_access_request",
                kwargs={
                    "request_id": "AR-103",
                    "user_id": "U-030",
                    "resource_id": "RES-032",
                    "requested_role_id": "ROL-032",
                    "justification": "Budget administration for Q3.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-103"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-032"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="list_policy_exceptions",
                kwargs={"user_id": "U-030", "active_only": True},
            ),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-103",
                    "reviewer_id": "U-006",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-103",
                    "reviewer_id": "U-006",
                    "approve": True,
                    "notes": "Met prerequisite finance-base (ROL-029).",
                },
            ),
            Action(name="get_user_sessions", kwargs={"user_id": "U-030"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-103"}),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-103", "assigned_by": "U-006"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-103"},
            ),
        ],
        outputs=[
            {
                "AR-103": "APPROVED",
                "NOTES": "Met prerequisite finance-base (ROL-029).",
                "U-030_ROLES": ["ROL-029", "ROL-032"],
                "AUDIT_LOG_ID": ["LOG-AR-103-decision"],
                "U-030_SESSIONS": [],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_027_review_missing_prereq_finance_admin",
        instruction=(
            "You are U-006 (finance-lead). You need to create AR-104 for U-031 requesting ROL-032 on RES-032 with "
            "the justification 'Value Departmental budget administration.' and then review it for "
            "least-privilege compliance and make a decision to approve or reject. Provide AR-104 decision, decision notes and audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(
                name="create_access_request",
                kwargs={
                    "request_id": "AR-104",
                    "user_id": "U-031",
                    "resource_id": "RES-032",
                    "requested_role_id": "ROL-032",
                    "justification": "Value Departmental budget administration.",
                    "submitted_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-104"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-032"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-031"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-104",
                    "reviewer_id": "U-006",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-104",
                    "reviewer_id": "U-006",
                    "approve": False,
                    "notes": "Missing prerequisite finance-base (ROL-029).",
                },
            ),
        ],
        outputs=[
            {
                "AR-104": "REJECTED",
                "NOTES": "Missing prerequisite finance-base (ROL-029).",
                "AUDIT_LOG_ID": ["LOG-AR-104-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_028_review_marketing_social_AR_009_evidence",
        instruction=(
            "You are U-005 (operations-lead). You need to review AR-009 for U-026 and make a decision to approve or reject under "
            "least-privilege principles while maintaining audit compliance. Return the decision, notes, U-026's "
            "roles and active sessions and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-009"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-008"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-009",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-009",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-009"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-026"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-009"},
            ),
        ],
        outputs=[
            {
                "U-026_ROLES": ["ROL-006", "ROL-007", "ROL-010"],
                "AR-009": "REJECTED",
                "U-026_SESSIONS": [],
                "NOTES": "Requested role does not cover target resource.",
                "AUDIT_LOG_ID": ["LOG-AR-009-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_029_engineering_rightsize_u_013_remove_base",
        instruction=(
            "You are U-005 (operations-lead). You need to revoke ROL-001 from U-013 to eliminate excess access "
            "privileges while maintaining complete audit compliance. Check U-013's roles to confirm the change "
            "and check their active sessions. Return U-013's updated roles, active sessions and audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-013"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-001"}),
            Action(
                name="check_user_status",
                kwargs={"mode": "revoke", "user_id": "U-013", "role_id": "ROL-001"},
            ),
            Action(
                name="revoke_role",
                kwargs={
                    "user_id": "U-013",
                    "role_id": "ROL-001",
                    "actor_id": "U-005",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-013"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-013"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "revoke_role", "target_id": "U-013:ROL-001"},
            ),
        ],
        outputs=[
            {
                "U-013_ROLES": [],
                "U-013_SESSIONS": [],
                "AUDIT_LOG_ID": ["LOG-U-013-ROL-001-revoke"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_030_ops_verify_sessions_and_pending_for_sales",
        instruction=(
            "You are U-005 (operations-lead). You need to resolve AR-022 for U-009 while ensuring operational "
            "integrity and policy compliance. The request must be reviewed against policy and make a decision to approve or reject. "
            "A check should be done for U-009's current session status. Return the decision, U-009's current "
            "session status and audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request", kwargs={"request_id": "AR-022"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-009"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-022"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-022",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-022",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-022"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-009"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-022"},
            ),
        ],
        outputs=[
            {
                "U-009_SESSIONS": [],
                "AR-022": "REJECTED",
                "AUDIT_LOG_ID": ["LOG-AR-022-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_031_reconcile_hr_payroll_AR_010_corrective_request",
        instruction=(
            "You are U-004 (hr-lead). Identify and correct the role/resource mismatch in AR-010. Create "
            "corrective request AR-110 for the user, requesting access to RES-020 with requested user role id "
            "ROL-018 and justification 'Align to correct resource.' Review it against policy and make a decision to approve or reject. Return the "
            "corrective request decision and its notes, the requester's roles, the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-004"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-010"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-010"}),
            Action(
                name="create_access_request",
                kwargs={
                    "request_id": "AR-110",
                    "user_id": "U-010",
                    "resource_id": "RES-020",
                    "requested_role_id": "ROL-018",
                    "justification": "Align to correct resource.",
                    "submitted_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-110",
                    "reviewer_id": "U-004",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-110",
                    "reviewer_id": "U-004",
                    "approve": False,
                    "notes": "Admin-like role blocked by policy.",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-010"}),

        ],
        outputs=[
            {
                "U-010_ROLES": ["ROL-016", "ROL-019"],
                "AR-110": "REJECTED",
                "NOTES": "Admin-like role blocked by policy.",
                "AUDIT_LOG_ID": ["LOG-AR-110-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_032_review_duplicate_marketing_analytics_AR_040",
        instruction=(
            "You are U-005 (operations-lead). You need to review AR-040 for U-014 against policy (including duplication checks if applicable) and make a decision to approve or reject. Return the decision, notes, U-014's "
            "roles and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-040"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-014"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-009"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-040",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-040",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-014"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-040"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-040"},
            ),
        ],
        outputs=[
            {
                "U-014_ROLES": ["ROL-006", "ROL-009"],
                "AR-040": "REJECTED",
                "NOTES": "Already assigned.",
                "AUDIT_LOG_ID": ["LOG-AR-040-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_033_process_hr_readonly_AR_030_assign_verify",
        instruction=(
            "You are U-005 (operations-lead). You need to review AR-030 under least-privilege principles, make a decision to approve or reject. "
            "Return the decision, notes and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-030"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-022"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-017"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-030", "assigned_by": "U-005"},
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-030"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-030"},
            ),
        ],
        outputs=[
            {
                "AR-030": "APPROVED",
                "NOTES": (
                    "Certification verified; within clearance and least-privilege."
                ),
                "AUDIT_LOG_ID": ["LOG-AR-030-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_034_create_and_validate_dev_db_read_AR_105_fix",
        instruction=(
            "You are U-001 (engineering-lead). You need to create AR-105 for U-007 (RES-006, ROL-005) with "
            "justification 'Developer DB read access.' and review it against policy and make a decision to approve or reject. Return the decision, notes, "
            "the requester's roles and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-001"}),
            Action(
                name="create_access_request",
                kwargs={
                    "request_id": "AR-105",
                    "user_id": "U-007",
                    "resource_id": "RES-006",
                    "requested_role_id": "ROL-005",
                    "justification": "Developer DB read access.",
                    "submitted_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-105"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-005"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-007"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-105",
                    "reviewer_id": "U-001",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-105",
                    "reviewer_id": "U-001",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
        ],
        outputs=[
            {
                "U-007_ROLES": ["ROL-001", "ROL-002"],
                "AR-105": "REJECTED",
                "NOTES": "Requested role does not cover target resource.",
                "AUDIT_LOG_ID": ["LOG-AR-105-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_035_review_ops_jira_admin_like_AR_106",
        instruction=(
            "You are U-005 (operations-lead). You need to create AR-106 for U-025 requesting ROL-025 on "
            "RES-002 with the justification 'Operations tooling admin access.' and then review it against policy and make a decision to approve or reject. "
            "policy. Return the decision, notes, the requester's roles, active sessions and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(
                name="create_access_request",
                kwargs={
                    "request_id": "AR-106",
                    "user_id": "U-025",
                    "resource_id": "RES-002",
                    "requested_role_id": "ROL-025",
                    "justification": "Operations tooling admin access.",
                    "submitted_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-106"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-025"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-025"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-106",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-106",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Admin-like role blocked by policy.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-106"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-025"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-025"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-106"},
            ),
        ],
        outputs=[
            {
                "U-025_ROLES": ["ROL-001"],
                "AR-106": "REJECTED",
                "NOTES": "Admin-like role blocked by policy.",
                "U-025_SESSIONS": [],
                "AUDIT_LOG_ID": ["LOG-AR-106-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_036_cross_check_permissions_for_user_snapshot",
        instruction=(
            "You are U-005 (operations-lead). You need to validate U-026's current access state and right-size "
            "by removing ROL-010 if present. Return a confirmation of ROL-010's removal, the requester's roles "
            "final state, active sessions and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(name="check_user_status", kwargs={"mode": "revoke", "user_id": "U-026", "role_id": "ROL-010"}),
            Action(
                name="revoke_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-010",
                    "actor_id": "U-005",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "revoke_role", "target_id": "U-026:ROL-010"},
            ),
            Action(name="get_user_sessions", kwargs={"user_id": "U-026"}),
        ],
        outputs=[
            {
                "ROL-010": "REMOVED",
                "U-026_ROLES": ["ROL-006", "ROL-007"],
                "U-026_SESSIONS": [],
                "AUDIT_LOG_ID": ["LOG-U-026-ROL-010-revoke"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_037_revoke_marketing_content_editor_from_u_026",
        instruction=(
            "You are U-002 (marketing-lead). Evaluate U-026's ROL-010 against policy and, if indicated, revoke it. "
            "Return U-026's roles, active sessions, and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-002"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-010"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "revoke",
                    "user_id": "U-026",
                    "role_id": "ROL-010",
                },
            ),
            Action(
                name="revoke_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-010",
                    "actor_id": "U-002",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "revoke_role", "target_id": "U-026:ROL-010"},
            ),
            Action(name="get_user_sessions", kwargs={"user_id": "U-026"}),
        ],
        outputs=[
            {
                "U-026_ROLES": ["ROL-006", "ROL-007"],
                "U-026_SESSIONS": [],
                "AUDIT_LOG_ID": ["LOG-U-026-ROL-010-revoke"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_038_create_review_process_duplicate_AR_107",
        instruction=(
            "You are U-005 with authority to create and review access requests. Create AR-107 for U-009 "
            "requesting resource_id: RES-016 and requested_role_id: ROL-013 with justification "
            "'Duplicate role request.' then evaluate it against policy and make a decision to approve or reject."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="list_access_requests_by_user", kwargs={"user_id": "U-009"}),
            Action(
                name="create_access_request",
                kwargs={
                    "request_id": "AR-107",
                    "user_id": "U-009",
                    "resource_id": "RES-016",
                    "requested_role_id": "ROL-013",
                    "justification": "Duplicate role request.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-107"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-009"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-107",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-107",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-107"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-107"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_039_create_review_process_sales_reporting_AR_108",
        instruction=(
            "You are U-003 with sales-lead authority. You want to create AR-108 for U-015 requesting ROL-014 "
            "with justification 'Sales reporting access.' on RES-014. Make a decision to approve or reject and grant the role if approved. Return U-015's end state roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-003"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-014"}),
            Action(
                name="create_access_request",
                kwargs={
                    "request_id": "AR-108",
                    "user_id": "U-015",
                    "resource_id": "RES-014",
                    "requested_role_id": "ROL-014",
                    "justification": "Sales reporting access.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-108"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-015"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-108",
                    "reviewer_id": "U-003",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-108",
                    "reviewer_id": "U-003",
                    "approve": False,
                    "notes": "Required certification not completed.",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-015"}),
        ],
        outputs=[
            {"user_id": "U-015", "roles": ["ROL-011"]},
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_040_ops_list_audit_window_for_requester",
        instruction=(
            "You are U-005 with review authority. You want to retrieve your review decisions within a 30d "
            "window from the submitted-at timestamp. Review AR-030 and make a decision to approve or reject, if still pending. Return the audit log id and "
            "U-022's updated roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-030"}),
            Action(
                name="get_time_window",
                kwargs={
                    "timestamp": "2024-05-29 14:00:00+00:00",
                    "days": "30d",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={
                    "user_id": "U-005",
                    "date_from": "2024-05-29T14:00:00+00:00",
                    "date_to": "2024-06-28T14:00:00+00:00",
                },
            ),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-030", "assigned_by": "U-005"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-022"}),
        ],
        outputs=[
            {
                "U-022_ROLES": ["ROL-016", "ROL-017"],
                "AUDIT_LOG_ID": ["LOG-AR-030-decision"],
            },
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_041_end_to_end_create_process_blog_cms_AR_109",
        instruction=(
            "You are U-002 with marketing-lead authority. You want to create AR-109 for U-026 requesting "
            "ROL-010 with justification 'Blog CMS editor access.' by resolving the correct resource from role "
            "mapping, then make a decision to approve or reject and grant the role if approved. Return U-026's updated roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-002"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-010"}),
            Action(
                name="create_access_request",
                kwargs={
                    "request_id": "AR-109",
                    "user_id": "U-026",
                    "resource_id": "RES-011",
                    "requested_role_id": "ROL-010",
                    "justification": "Blog CMS editor access.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-109"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-109",
                    "reviewer_id": "U-002",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-109",
                    "reviewer_id": "U-002",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
        ],
        outputs=[
            {"user_id": "U-026", "roles": ["ROL-006", "ROL-007", "ROL-010"]},
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_042_cert_and_hr_closeout_for_u_022",
        instruction=(
            "You are U-005 with certification and access review authority. You want to process outstanding "
            "certifications C-011 and C-005 and evaluate AR-030 for U-022 with decision note 'Within "
            "clearance and least-privilege.' Use the deterministic timestamp for all time fields."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="list_certifications_by_status", kwargs={"status": "PENDING"}),
            Action(
                name="list_certifications_by_status", kwargs={"status": "IN_PROGRESS"}
            ),
            Action(
                name="start_certification",
                kwargs={"certification_id": "C-011", "reviewer_id": "U-005"},
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-011",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-005",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="list_certifications_by_status", kwargs={"status": "IN_PROGRESS"}
            ),
            Action(name="list_access_requests_by_status", kwargs={"status": "PENDING"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": "Within clearance and least-privilege.",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-030", "assigned_by": "U-005"},
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-030"}),
            Action(
                name="list_certifications_by_status", kwargs={"status": "COMPLETED"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_043_recert_and_rightsize_from_inventory",
        instruction=(
            "You are U-005 with certification and access management authority. You want to process "
            "certification C-020 and right-size U-026's access while checking AR-021 status. Use the "
            "deterministic timestamp for all time fields. Return U-026's updated roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-020"},
            ),
            Action(name="start_certification", kwargs={"certification_id": "C-020"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-020"},
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-020",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-020"},
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-021"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "revoke",
                    "user_id": "U-026",
                    "role_id": "ROL-010",
                },
            ),
            Action(
                name="revoke_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-010",
                    "actor_id": "U-005",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
        ],
        outputs=[
            {"user_id": "U-026", "roles": ["ROL-006", "ROL-007"]},
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_044_cert_throughput_plus_single_grant",
        instruction=(
            "You are U-006 with finance-lead and certification authority. You want to process certification "
            "C-020 and evaluate AR-034 for U-018 against policy and make a decision to approve or reject with decision note 'Within clearance and least-privilege.' "
            "Use the deterministic timestamp for completion times."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-020"},
            ),
            Action(
                name="start_certification",
                kwargs={"certification_id": "C-020", "reviewer_id": "U-006"},
            ),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-020"},
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-020",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                    "reviewer_id": "U-006",
                },
            ),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-020"},
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(
                name="check_user_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                    "mode": "access_request",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                    "approve": True,
                    "notes": "Within clearance and least-privilege.",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-034", "assigned_by": "U-006"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_045_recert_and_duplicate_hygiene_v2",
        instruction=(
            "You are U-005 with certification and access review authority. You want to process certification "
            "C-021 and evaluate AR-022 against policy and make a decision to approve or reject. Scope "
            "limited to C-021, AR-022, and requester assignment evidence."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="list_certifications_by_status", kwargs={"status": "PENDING"}),
            Action(
                name="start_certification",
                kwargs={"certification_id": "C-021", "reviewer_id": "U-005"},
            ),
            Action(
                name="list_certifications_by_status", kwargs={"status": "IN_PROGRESS"}
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-021",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="list_certifications_by_status", kwargs={"status": "COMPLETED"}
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-022"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-013"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-009"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-022",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-022",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-022"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-022"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_046_cert_then_remediate_missing_baseline",
        instruction=(
            "You are U-005 with certification and role assignment authority. You want to process "
            "certification C-005 and assign baseline role ROL-007 to U-014 (remediating missing baseline) "
            "with user_role_id UR-999 using the deterministic timestamp. "
            "Return the requester's active sessions."
        ),
        actions=[
            Action(
                name="list_certifications_by_status",
                kwargs={
                    "certification_id": "C-005",
                },
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-005",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="list_certifications_by_status",
                kwargs={
                    "certification_id": "C-005",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-014"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-007"}),
            Action(
                name="assign_user_role",
                kwargs={
                    "user_role_id": "UR-999",
                    "user_id": "U-014",
                    "role_id": "ROL-007",
                    "assigned_by": "U-005",
                    "assigned_on": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-014"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-014"}),
        ],
        outputs=[
            {"U-014_SESSIONS": []}
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_047_block_escalation_and_finish_certs_v2",
        instruction=(
            "You are U-005 with certification and access review authority. You want to complete certification "
            "C-011 using the deterministic timestamp and evaluate AR-007 against policy and make a decision to approve or reject. "
        ),
        actions=[
            Action(name="list_certifications_by_status", kwargs={"status": "PENDING"}),
            Action(
                name="start_certification",
                kwargs={"certification_id": "C-011", "reviewer_id": "U-005"},
            ),
            Action(
                name="list_certifications_by_status", kwargs={"status": "IN_PROGRESS"}
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-011",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="list_certifications_by_status", kwargs={"status": "COMPLETED"}
            ),
            Action(name="list_access_requests_by_status", kwargs={"status": "PENDING"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-007"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-026"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-007"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-007"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_048_cert_sweep_and_permissions_check_v2",
        instruction=(
            "You are U-005 with certification and access review authority. You want to process certification "
            "C-013 with the deterministic timestamp and evaluate AR-034 for U-018 and make a decision to approve or reject. Return requester's roles "
            "and audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(
                name="list_certifications_by_status", kwargs={"status": "IN_PROGRESS"}
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-013",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_certifications_by_status", kwargs={"status": "COMPLETED"}
            ),
            Action(name="list_access_requests_by_status", kwargs={"status": "PENDING"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-030"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-034",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-034", "assigned_by": "U-005"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(name="get_permissions_for_user", kwargs={"user_id": "U-018"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-034"},
            ),
        ],
        outputs=[
            {
                "U-018_PERMISSIONS": [
                    {
                        "permission_id": "P-075",
                        "action": "read-ledger",
                        "resource_id": "RES-030",
                    },
                    {
                        "permission_id": "P-083",
                        "action": "run-tax-report",
                        "resource_id": "RES-033",
                    },
                    {
                        "permission_id": "P-085",
                        "action": "view-financial-report",
                        "resource_id": "RES-034",
                    },
                ]
            },
            {"U-018_ROLES": ["ROL-029", "ROL-030"]},
            {"AUDIT_LOG_ID": ["LOG-AR-034-decision"]},
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_049_finance_recert_and_budget_admin_path_v2",
        instruction=(
            "You are U-005 with certification and access review authority. Process certification C-020 using "
            "the deterministic timestamp 2024-06-26 16:05:00+00:00 and review AR-008 for U-030 against policy and make a decision to approve or reject. "
            "If approved, assign the role and record the decision with an audit log. Return U-030's roles, "
            "audit log id and the permissions for U-030."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-020"},
            ),
            Action(name="start_certification", kwargs={"certification_id": "C-020"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-020"},
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-020",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-020"},
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-032"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-008",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": "Met prerequisite finance-base (ROL-029).",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-008", "assigned_by": "U-005"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-008"},
            ),
        ],
        outputs=[
            {
                "U-030_PERMISSIONS": [
                    {
                        "permission_id": "P-080",
                        "action": "create-budget",
                        "resource_id": "RES-032",
                    },
                    {
                        "permission_id": "P-081",
                        "action": "approve-budget",
                        "resource_id": "RES-032",
                    },
                    {
                        "permission_id": "P-082",
                        "action": "view-budget",
                        "resource_id": "RES-032",
                    },
                ]
            },
            {"user_id": "U-030", "roles": ["ROL-029", "ROL-032"]},
            {"AUDIT_LOG_ID": "LOG-AR-008-decision"},
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_050_quarter_close_zero_wip_with_minimal_note",
        instruction=(
            "You are U-005 with certification management authority. You want to clear all IN_PROGRESS "
            "certifications and log audit entry LOG-CERT-QCLOSE with action_type 'certification_close', "
            "target_id CERT:Q2, and details 'Queue cleared.'"
        ),
        actions=[
            Action(
                name="list_certifications_by_status", kwargs={"status": "IN_PROGRESS"}
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-005",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-013",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-016",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="list_certifications_by_status", kwargs={"status": "COMPLETED"}
            ),
            Action(
                name="append_audit_log",
                kwargs={
                    "log_id": "LOG-CERT-QCLOSE",
                    "actor_id": "U-005",
                    "action_type": "certification_close",
                    "target_id": "CERT:Q2",
                    "timestamp": "2024-06-26 16:05:00+00:00",
                    "details": "Queue cleared.",
                },
            ),
            Action(
                name="list_certifications_by_status", kwargs={"status": "IN_PROGRESS"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_051_cert_recert_and_process_AR_030",
        instruction=(
            "You are U-005 with certification and access review authority. You want to start & process certification C-021 using the deterministic timestamp and evaluate AR-030 with policy-based determination."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(
                name="start_certification",
                kwargs={"certification_id": "C-021", "reviewer_id": "U-005"},
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-021",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-021"},
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-030"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-017"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-030", "assigned_by": "U-005"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_052_process_marketing_AR034",
        instruction=(
            "You are U-005 (operations-lead). Decide AR-034 under least-privilege principles while maintaining audit compliance. "
            "Return the decision, notes, and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-034",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-034", "assigned_by": "U-005"},
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-034"},
            ),
        ],
        outputs=[
            {
                "AR-034": "APPROVED",
                "NOTES": (
                    "Certification verified; within clearance and least-privilege."
                ),
                "AUDIT_LOG_ID": ["LOG-AR-034-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_053_approve_AR008_with_email_notification",
        instruction=(
            "You are U-005 with access review authority. You want to review AR-008 for user U-030 requesting ROL-032 on RES-032, make a decision to approve or reject, and notify them via email. "
            "Return the email receipt."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-008",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": "Met prerequisite finance-base (ROL-029).",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-008", "assigned_by": "U-005"},
            ),
            Action(name="get_user_email", kwargs={"user_id": "U-030"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "marisa.cole@taucorp.com",
                    "subject": "AR-008 APPROVED",
                    "text_content": "U-005 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="list_emails", kwargs={"email_id": "EM-9601"}),
        ],
        outputs=[
            [
                {
                    "email_id": "EM-9601",
                    "timestamp": "2024-06-26 16:05:00+00:00",
                    "sender": "rbac-bot@taucorp.com",
                    "receiver": "marisa.cole@taucorp.com",
                    "subject": "AR-008 APPROVED",
                    "text_content": "U-005 2024-06-26 16:05:00+00:00",
                }
            ]
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_054_deny_AR040_insufficient_permissions",
        instruction=(
            "You are U-004 with access review authority. You want to review AR-040 for user U-014 requesting ROL-009 on RES-010, make a decision to approve or reject, and notify them via email. "
            "Return a record of the sent email."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-004"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-040"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-014"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-009"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-040",
                    "reviewer_id": "U-004",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-040",
                    "reviewer_id": "U-004",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_user_email", kwargs={"user_id": "U-014"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "nicole.thomas@taucorp.com",
                    "subject": "AR-040 REJECTED",
                    "text_content": "U-004 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="list_emails", kwargs={"email_id": "EM-9601"}),
        ],
        outputs=[
            {
                "email_id": "EM-9601",
                "timestamp": "2024-06-26 16:05:00+00:00",
                "sender": "rbac-bot@taucorp.com",
                "receiver": "nicole.thomas@taucorp.com",
                "subject": "AR-040 REJECTED",
                "text_content": "U-004 2024-06-26 16:05:00+00:00",
            },
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_055_approve_AR034_with_compliance_verification",
        instruction=(
            "You are U-005 with access review authority. You want to evaluate AR-034 for user U-018 requesting ROL-030 on RES-034 with least-privilege principles, make a decision to approve or reject, and return the audit log entry for the decision."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-030"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-034",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-034", "assigned_by": "U-005"},
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-034"},
            ),
        ],
        outputs=[
            [
                {
                    "log_id": "LOG-AR-034-decision",
                    "actor_id": "U-005",
                    "action_type": "review_access_request",
                    "target_id": "AR-034",
                    "timestamp": "2024-06-26 16:05:00+00:00",
                    "details": "APPROVED",
                }
            ]
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_056_complete_C013_and_process_assign_AR_034_with_verify",
        instruction=(
            "You are U-005 with certification and access review authority. Complete certification C-013, then review AR-034 for user U-018 requesting ROL-030, make a decision to approve or reject, and finally return U-018's updated role assignments."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-013"},
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-013",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-030"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-034",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-034", "assigned_by": "U-005"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
        ],
        outputs=[{"user_id": "U-018", "roles": ["ROL-029", "ROL-030"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_057_create_AR_111_then_review_for_coverage_mismatch",
        instruction=(
            "You are U-006 with authority to review access requests. Evaluate if U-027 should have ROL-011, make a decision to revoke or not, and return the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-027"}),
            Action(name="check_user_status", kwargs={"mode": "revoke", "user_id": "U-027", "role_id": "ROL-011"}),
            Action(
                name="revoke_role",
                kwargs={"user_id": "U-027", "role_id": "ROL-011", "actor_id": "U-006"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-027"}),
            Action(name="get_user_email", kwargs={"user_id": "U-027"}),
            Action(name="send_email", kwargs={"email_id": "EM-9601", "receiver": "U-027", "subject": "ROL-011 APPROVED", "text_content": "U-006 2024-06-26 16:05:00+00:00"}),
        ],
        outputs=[
            {"AUDIT_LOG_ID": ["LOG-U-027-ROL-011-revoke"]}
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_058_rightsize_revoke_one_role_after_inventory",
        instruction=(
            "You are U-005 with authority to right-size user access. Evaluate U-026's access against policy and make a decision. Apply the decision and return ROL-010's role permissions."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "revoke",
                    "user_id": "U-026",
                    "role_id": "ROL-010",
                },
            ),
            Action(
                name="revoke_role",
                kwargs={
                    "user_id": "U-026",
                    "role_id": "ROL-010",
                    "actor_id": "U-005",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-010"}),
        ],
        outputs=[
            [
                {
                    "permission_id": "P-030",
                    "action": "create-blog-post",
                    "resource_id": "RES-011",
                },
                {
                    "permission_id": "P-031",
                    "action": "publish-blog-post",
                    "resource_id": "RES-011",
                },
                {
                    "permission_id": "P-032",
                    "action": "edit-blog-post",
                    "resource_id": "RES-011",
                },
            ],
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_059_process_AR008_email_receipt",
        instruction=(
            "You are U-005 with access review authority. Review AR-008 for U-030 against policy rules, make a decision to approve or reject, notify them via email, and close the related HubSpot ticket TI-010 (CLOSED)."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(name="list_hubspot_tickets", kwargs={"requester_id": "U-030"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-008",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": "Met prerequisite finance-base (ROL-029).",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-008", "assigned_by": "U-005"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "user_id": "U-030",
                    "subject": "AR-008 APPROVED",
                    "text_content": "U-005 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="update_hubspot_ticket_status",
                kwargs={
                    "ticket_id": "TI-010",
                    "status": "CLOSED",
                    "actor_id": "U-005",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_060_process_AR007_ops_checklist",
        instruction=(
            "You are U-005 with access review authority. Review AR-007 for U-029 requesting ROL-026 against policy, notify them via email, and close the related HubSpot ticket TI-009."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-007"}),
            Action(name="list_hubspot_tickets", kwargs={"requester_id": "U-029"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "user_id": "U-029",
                    "subject": "AR-007 REJECTED",
                    "text_content": "U-005 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="update_hubspot_ticket_status",
                kwargs={
                    "ticket_id": "TI-009",
                    "status": "CLOSED",
                    "actor_id": "U-005",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_061_review_AR040_training_email",
        instruction=(
            "You are U-005 with access review authority. You want to evaluate AR-040 against policy, make a decision to approve or reject, and notify the requester via email. Set the related HubSpot ticket to CLOSED status with MEDIUM priority."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-040"}),
            Action(name="list_hubspot_tickets", kwargs={"requester_id": "U-014"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-040",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-040",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_user_email", kwargs={"user_id": "U-014"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "nicole.thomas@taucorp.com",
                    "subject": "AR-040 REJECTED",
                    "text_content": "U-005 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="update_hubspot_ticket_status",
                kwargs={
                    "ticket_id": "TI-042",
                    "status": "CLOSED",
                    "actor_id": "U-005",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_062_assign_rol_037",
        instruction=(
            "You are U-005 (operations-lead). Make a decision to approve or reject AR-008, and notify the requester via email."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-008",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-005",
                    "approve": True,
                    "notes": "Met prerequisite finance-base (ROL-029).",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-008", "assigned_by": "U-005"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(name="get_user_email", kwargs={"user_id": "U-030"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "marisa.cole@taucorp.com",
                    "subject": "AR-008 APPROVED",
                    "text_content": "U-005 2024-06-26 16:05:00+00:00",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_063_process_AR034_tax_policy",
        instruction=(
            "You are U-006 with finance-lead authority. Review AR-034 for U-018 against policy, make a decision to approve or reject, assign HubSpot ticket TI-036 to yourself, notify them via email, and close the ticket."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(name="list_hubspot_tickets", kwargs={"requester_id": "U-018"}),
            Action(
                name="update_hubspot_ticket_assignee",
                kwargs={
                    "ticket_id": "TI-036",
                    "assignee_id": "U-006",
                    "actor_id": "U-006",
                },
            ),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-034", "assigned_by": "U-006"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(name="get_user_email", kwargs={"user_id": "U-018"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "stephanie.adams@taucorp.com",
                    "subject": "AR-034 APPROVED",
                    "text_content": "U-006 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="update_hubspot_ticket_status",
                kwargs={
                    "ticket_id": "TI-036",
                    "status": "CLOSED",
                    "actor_id": "U-006",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_064_process_AR021_CMS_policy",
        instruction=(
            "You are U-005 with access review authority. You want to process AR-021, make a decision to approve or reject, and notify via email. Return the requester's (U-026) roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-021"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-021",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-021",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_user_email", kwargs={"user_id": "U-026"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "angela.phillips@taucorp.com",
                    "subject": "AR-021 REJECTED",
                    "text_content": "U-005 2024-06-26 16:05:00+00:00",
                },
            ),
        ],
        outputs=[{"U-026_ROLES": ["ROL-006", "ROL-007", "ROL-010"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_065_review_AR022_remediation_email",
        instruction=(
            "You are U-004 with access review authority. You want to evaluate AR-022 for user U-009 against policy, make a decision to approve or reject, and notify the requester via email. Mark HubSpot ticket TI-024 CLOSED with MEDIUM priority."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-004"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-022"}),
            Action(name="list_hubspot_tickets", kwargs={"requester_id": "U-009"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-022",
                    "reviewer_id": "U-004",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-022",
                    "reviewer_id": "U-004",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_user_email", kwargs={"user_id": "U-009"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "matthew.lopez@taucorp.com",
                    "subject": "AR-022 REJECTED",
                    "text_content": "U-004 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="update_hubspot_ticket_status",
                kwargs={
                    "ticket_id": "TI-024",
                    "status": "CLOSED",
                    "actor_id": "U-004",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_066_process_AR030_policy_email",
        instruction=(
            "You are U-003 with sales-lead authority. Review AR-030 for U-022 requesting ROL-017, make a decision to approve or reject, notify them via email. Close HubSpot ticket TI-032."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-003"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-030"}),
            Action(name="list_hubspot_tickets", kwargs={"requester_id": "U-022"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-030",
                    "reviewer_id": "U-003",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-003",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-030", "assigned_by": "U-003"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-022"}),
            Action(name="get_user_email", kwargs={"user_id": "U-022"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "brittany.king@taucorp.com",
                    "subject": "AR-030 APPROVED",
                    "text_content": "U-003 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="update_hubspot_ticket_status",
                kwargs={
                    "ticket_id": "TI-032",
                    "status": "CLOSED",
                    "actor_id": "U-003",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_067_process_AR009_social_policy",
        instruction=(
            "You are U-002 with marketing-lead authority. Review AR-009 for U-026 against policy, make a decision to approve or reject, notify the requester via email. Set HubSpot ticket TI-011 to CLOSED."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-002"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-009"}),
            Action(name="list_hubspot_tickets", kwargs={"requester_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-009",
                    "reviewer_id": "U-002",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-009",
                    "reviewer_id": "U-002",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(name="get_user_email", kwargs={"user_id": "U-026"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "angela.phillips@taucorp.com",
                    "subject": "AR-009 REJECTED",
                    "text_content": "U-002 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="update_hubspot_ticket_status",
                kwargs={
                    "ticket_id": "TI-011",
                    "status": "CLOSED",
                    "actor_id": "U-002",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_068_ack_alert_and_review_AR_053_policy_block",
        instruction=(
            "You are U-005 with security alert and access review authority. You want to respond to SIEM alert ALRT-001 ('UNAUTHORIZED_ACCESS_ATTEMPT') with status ACKNOWLEDGED and note 'Investigating'. Evaluate AR-009 against policy and make a decision to approve or reject. Return audit evidence filtered by review_access_request for target_id AR-009."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(
                name="list_siem_alerts",
                kwargs={"alert_type": "UNAUTHORIZED_ACCESS_ATTEMPT"},
            ),
            Action(
                name="acknowledge_siem_alert",
                kwargs={
                    "alert_id": "ALRT-001",
                    "ack_by": "U-005",
                    "status": "ACKNOWLEDGED",
                    "note": "Investigating",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-009"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-009",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-009",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-009"},
            ),
        ],
        outputs=[
            [
                {
                    "log_id": "LOG-AR-009-decision",
                    "actor_id": "U-005",
                    "action_type": "review_access_request",
                    "target_id": "AR-009",
                    "timestamp": "2024-06-26 16:05:00+00:00",
                    "details": "REJECTED",
                }
            ],
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_069_",
        instruction=(
            "You are U-002 with marketing-lead authority. Evaluate AR-009 against policy, make a decision to approve or reject the request, and return the requester's current roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-002"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-009"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-008"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-009",
                    "reviewer_id": "U-002",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-009",
                    "reviewer_id": "U-002",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
        ],
        outputs=[
            {"user_id": "U-026", "roles": ["ROL-006", "ROL-007", "ROL-010"]},
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_070_",
        instruction=(
            "You are U-005 with marketing-lead authority. Evaluate AR-007 against policy and made a decision to approve or reject. Enable MFA for the requester. Return the audit log id, and requester's role."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-007"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
            Action(name="set_user_mfa", kwargs={"user_id": "U-029", "enabled": True}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-007"},
            ),
        ],
        outputs=[{"AUDIT_LOG_ID": ["LOG-AR-007-decision"], "U-029_ROLES": ["ROL-021"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_071_finance_compliance_eval",
        instruction=(
            "You are U-006 with finance-lead authority. Evaluate AR-008 against policy, make a decision to approve or reject, and return the requester's roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-008",
                    "reviewer_id": "U-006",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-006",
                    "approve": True,
                    "notes": "Met prerequisite finance-base (ROL-029).",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-008", "assigned_by": "U-006"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
        ],
        outputs=[{"U-030_ROLES": ["ROL-029", "ROL-032"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_072_engineering_least_privilege",
        instruction=(
            "You are U-001 with engineering-lead authority. Evaluate AR-020 against policy, make a decision to approve or reject, and return the requester's roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-001"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-020"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-004"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-020",
                    "reviewer_id": "U-001",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-013"}),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-020",
                    "reviewer_id": "U-001",
                    "approve": False,
                    "notes": "Required certification not completed.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-013"}),
        ],
        outputs=[{"U-013_ROLES": ["ROL-001"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_073_marketing_duplicate_check_email",
        instruction=(
            "You are U-002 with marketing-lead authority. You want to evaluate AR-021 against policy, make a decision to approve or reject, and notify RBAC (U-031) via email."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-002"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-021"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-021",
                    "reviewer_id": "U-002",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-021",
                    "reviewer_id": "U-002",
                    "approve": False,
                    "notes": "Already assigned.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_user_email", kwargs={"user_id": "U-031"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "rbac@taucorp.com",
                    "subject": "AR-021 REJECTED",
                    "text_content": "U-002 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-021"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_074_process_hr_mfa",
        instruction=(
            "You are U-004 (hr-lead) with access review and security management authority. You want to evaluate AR-030 against HR policy, make a decision to approve or reject, and ensure the requester's account has MFA protection."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-004"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-030"}),
            Action(name="set_user_mfa", kwargs={"user_id": "U-022", "enabled": True}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-030",
                    "reviewer_id": "U-004",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-004",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-030", "assigned_by": "U-004"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-022"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-030"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_075_dual_triage_ops_finance",
        instruction=(
            "You are U-005 (ops-lead) coordinating with U-006 (finance-lead). You want to process the two earliest pending access requests by applying policy. Return decisions verifiable in audit records."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="list_access_requests_by_status", kwargs={"status": "PENDING"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-007"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-026"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-007"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-008",
                    "reviewer_id": "U-006",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-006",
                    "approve": True,
                    "notes": "Met prerequisite finance-base (ROL-029).",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-008", "assigned_by": "U-006"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-008"},
            ),
        ],
        outputs=[
            {
                "AR-007": "REJECTED",
                "AR-008": "APPROVED",
                "AUDIT_LOG_ID": ["LOG-AR-007-decision", "LOG-AR-008-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_076_process_sales_mfa",
        instruction=(
            "You are U-003 (sales-lead) with access review and security management authority. You want to evaluate AR-022 against policy, make a decision to approve or reject, and notify matthew.lopez@taucorp.com via email. Set MFA status to True and return the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-003"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-022"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-009"}),
            Action(name="set_user_mfa", kwargs={"user_id": "U-009", "enabled": True}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-022",
                    "reviewer_id": "U-003",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-022",
                    "reviewer_id": "U-003",
                    "approve": False,
                    "notes": "Already assigned.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "matthew.lopez@taucorp.com",
                    "subject": "AR-022 REJECTED",
                    "text_content": "U-003 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-022"},
            ),
        ],
        outputs=[{"AUDIT_LOG_ID": ["LOG-AR-022-decision"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_077_review_email_marketing",
        instruction=(
            "You are U-002 (marketing-lead) with access review authority. You want to evaluate AR-040 against policy, make a decision to approve or reject, and notify U-031 via email. Return the email in the output."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-002"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-040"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-014"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-040",
                    "reviewer_id": "U-002",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-040",
                    "reviewer_id": "U-002",
                    "approve": False,
                    "notes": "Already assigned.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_user_email", kwargs={"user_id": "U-031"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "rbac@taucorp.com",
                    "subject": "AR-040 REJECTED",
                    "text_content": "U-002 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-040"},
            ),
        ],
        outputs=[
            {
                "EMAIL_SENT": {
                    "subject": "AR-040 REJECTED",
                    "receiver": "rbac@taucorp.com",
                    "content": "U-002 2024-06-26 16:05:00+00:00",
                }
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_078_rightsize_engineering",
        instruction=(
            "You are U-001 (engineering-lead) with access management authority. You want to check if ROL-037 can be revoked from U-013 and review U-019's current access and optimize it according to least-privilege principles by removing ROL-004. Return whether ROL-037 is revokable and the audit log id for U-019's revoke."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-001"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-019"}),
            Action(
                name="check_user_status",
                kwargs={"mode": "revoke", "user_id": "U-019", "role_id": "ROL-004"},
            ),
            Action(
                name="revoke_role",
                kwargs={"user_id": "U-019", "role_id": "ROL-004", "actor_id": "U-001"},
            ),
            Action(
                name="check_user_status",
                kwargs={"mode": "revoke", "user_id": "U-013", "role_id": "ROL-037"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-019"}),
            Action(
                name="list_audit_logs",
                kwargs={"action_type": "revoke_role", "target_id": "U-019:ROL-004"},
            ),
        ],
        outputs=[
            {
                "U-013_ROL-037_REVOCABLE": False,
                "AUDIT_LOG_ID": "LOG-U-019-ROL-004-revoke",
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_079_seq_cleanup_ops",
        instruction=(
            "You are U-005 (operations-lead) with access management authority. Check the MFA status of U-011 and U-029, then evaluate them for right-sizing ROL-021 and apply the policy recommendation (revoke only if indicated). If no revocation is needed, append audit logs for each user and return the audit log ids."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-011"}),
            Action(name="list_users_by_mfa", kwargs={"user_id": "U-011"}),
            Action(name="list_users_by_mfa", kwargs={"user_id": "U-029"}),
            Action(
                name="check_user_status",
                kwargs={"mode": "revoke", "user_id": "U-011", "role_id": "ROL-021"},
            ),
            Action(
                name="check_user_status",
                kwargs={"mode": "revoke", "user_id": "U-029", "role_id": "ROL-021"},
            ),
            Action(
                name="log_revoke_decision",
                kwargs={
                    "user_id": "U-011",
                    "role_id": "ROL-021",
                    "actor_id": "U-005",
                    "details": "NOOP",
                },
            ),
            Action(
                name="log_revoke_decision",
                kwargs={
                    "user_id": "U-029",
                    "role_id": "ROL-021",
                    "actor_id": "U-005",
                    "details": "NOOP",
                },
            ),
        ],
        outputs=[
            {
                "AUDIT_LOG_ID": [
                    "LOG-U-011-ROL-021-decision",
                    "LOG-U-029-ROL-021-decision",
                ]
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_080_process_finance_prereq",
        instruction=(
            "You are U-006 (finance-lead) with access review authority. You want to evaluate AR-034 under least‑privilege principles, ensuring the requester holds both basic finance permissions: read-ledger and view-payments before approval."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(name="get_permissions_for_user", kwargs={"user_id": "U-018"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-034", "assigned_by": "U-006"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(name="get_permissions_for_user", kwargs={"user_id": "U-018"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-034"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_081_finance_manual_assign_with_cert",
        instruction=(
            "You are U-006 (finance-lead) with certification and access management authority. Make a decision to approve or reject AR-034, but ensure you complete finance certification C-019. Return permissions for requester."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-019"},
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-019",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-034", "assigned_by": "U-006"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(name="get_permissions_for_user", kwargs={"user_id": "U-018"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-034"},
            ),
        ],
        outputs=[{"U-018_PERMISSIONS": ["P-075", "P-079", "P-082", "P-083", "P-085"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_082_sales_check_gate_sessions_with_cert",
        instruction=(
            "You are U-003 (sales-lead) with certification, security, and access management authority. Evaluate AR-022 by ensuring sales certification C-009 is completed and enabling MFA, then assign if approved. Return roles, sessions, and audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-003"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-022"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-009"},
            ),
            Action(name="set_user_mfa", kwargs={"user_id": "U-009", "enabled": True}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-022",
                    "reviewer_id": "U-003",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-022",
                    "reviewer_id": "U-003",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-009"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-009"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-022"},
            ),
        ],
        outputs=[
            {
                "U-009_ROLES": ["ROL-011", "ROL-012", "ROL-013"],
                "U-009_SESSIONS": [],
                "AUDIT_LOG_ID": ["LOG-AR-022-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_083_marketing_review_duplicate_with_cert_notice",
        instruction=(
            "You are U-002 (marketing-lead) with certification and access review authority. Confirm the marketing certification (C-015) state and make a decision to approve or reject AR-040, and notify rbac@taucorp.com via email. Return both email record and audit entry."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-002"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-040"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-015"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-014"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-040",
                    "reviewer_id": "U-002",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-040",
                    "reviewer_id": "U-002",
                    "approve": False,
                    "notes": "Already assigned.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "rbac@taucorp.com",
                    "subject": "AR-040 REJECTED",
                    "text_content": "U-002 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-040"},
            ),
        ],
        outputs=[
            {
                "EMAIL_SENT": {
                    "subject": "AR-040 REJECTED",
                    "receiver": "rbac@taucorp.com",
                    "content": "U-002 2024-06-26 16:05:00+00:00",
                },
                "AUDIT_LOG_ID": ["LOG-AR-040-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_084_engineering_noop_revoke_with_cert_context",
        instruction=(
            "You are U-001 (engineering-lead) with access management and certification authority. Attempt to revoke ROL-012 and ROL-011 from U-015 (expecting NOOP result & success). Return audit log ids if any."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-001"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-015"}),
            Action(
                name="check_user_status",
                kwargs={"mode": "revoke", "user_id": "U-015", "role_id": "ROL-012"},
            ),
            Action(
                name="check_user_status",
                kwargs={"mode": "revoke", "user_id": "U-015", "role_id": "ROL-011"},
            ),
            Action(
                name="revoke_role",
                kwargs={"user_id": "U-015", "role_id": "ROL-011", "actor_id": "U-001"},
            ),
            Action(name="list_audit_logs", kwargs={"action_type": "revoke_role"}),
        ],
        outputs=[{"AUDIT_LOG_ID": ["LOG-U-015-ROL-011-revoke"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_085_finance_mixed_ar007_review_ar034_process_with_certs",
        instruction=(
            "You are U-006 (finance-lead) with certification and access review authority. You want to validate ops certification C-008 and evaluate AR-007, while processing pending finance certification C-019 and evaluating AR-034. Return both decisions confirmed in audit records."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-007"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-026"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-008"},
            ),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-007",
                    "reviewer_id": "U-006",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-007",
                    "reviewer_id": "U-006",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-007"},
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-034"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-019"},
            ),
            Action(name="start_certification", kwargs={"certification_id": "C-019"}),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-019",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-034",
                    "reviewer_id": "U-006",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-034", "assigned_by": "U-006"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
            Action(name="get_permissions_for_user", kwargs={"user_id": "U-018"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-034"},
            ),
        ],
        outputs=[
            {
                "AR-007": "REJECTED",
                "AR-034": "APPROVED",
                "AUDIT_LOG_ID": ["LOG-AR-007-decision", "LOG-AR-034-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_086_mfa_then_cert_then_assign",
        instruction=(
            "You are U-001 (engineering-lead) with security, certification, and access management authority. You want to secure the AR-009 requester with MFA and ensure security certification C-023 is complete before making a decision to approve or deny the access request.. "
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-001"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-009"}),
            Action(name="set_user_mfa", kwargs={"user_id": "U-026", "enabled": True}),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-023"},
            ),
            Action(name="start_certification", kwargs={"certification_id": "C-023"}),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-023",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-009",
                    "reviewer_id": "U-001",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-009",
                    "reviewer_id": "U-001",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-009"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_087_cert_revoke_notify",
        instruction=(
            "You are U-005 (operations-lead). You want to decide whether to revoke ROL-004 from U-007 based on policy; notify the user by email. Return the user's active sessions, and their assigned roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-007"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "revoke",
                    "user_id": "U-007",
                    "role_id": "ROL-004",
                },
            ),
            Action(
                name="revoke_role",
                kwargs={
                    "user_id": "U-007",
                    "role_id": "ROL-004",
                    "actor_id": "U-005",
                },
            ),
            Action(name="get_user_email", kwargs={"user_id": "U-007"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-007"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "christopher.rodriguez@taucorp.com",
                    "subject": "ROL-004 APPROVED",
                    "text_content": "U-005 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-007"}),
        ],
        outputs=[{"U-007_SESSIONS": [], "U-007_ROLES": ["ROL-001", "ROL-002"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_088_policy_exception_check",
        instruction=(
            "You are U-001 (engineering-lead) with certification and access management authority. Make a decision to approve or reject AR-008. Return the audit log for AR-008."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-001"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-008",
                    "reviewer_id": "U-001",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-001",
                    "approve": True,
                    "notes": "Met prerequisite finance-base (ROL-029).",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-008", "assigned_by": "U-001"},
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-008"},
            ),
        ],
        outputs=[{"AUDIT_LOG_ID": ["LOG-AR-008-decision"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_089_mfa_cert_and_dual_assign",
        instruction=(
            "You are U-001 (engineering-lead). You want to secure U-026 with MFA, verify engineering certification C-022 is complete, "
            "then make a decision on AR-009 for U-026. Return the user's permissions and the audit log for AR-009."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-001"}),
            Action(name="set_user_mfa", kwargs={"user_id": "U-026", "enabled": True}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-022"},
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-022",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-009"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-009",
                    "reviewer_id": "U-001",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-009",
                    "reviewer_id": "U-001",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-009"},
            ),
        ],
        outputs=[
            {
                "U-026_PERMISSIONS": ["ROL-006", "ROL-007", "ROL-010"],
                "AUDIT_LOG_ID": ["LOG-AR-009-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_090_cert_expiry_trigger_revoke_request",
        instruction=(
            "You are U-002 (marketing-lead) with certification and access management authority. You want to address expired certification C-021 for U-020 by creating AR-062 for a lower-privilege replacement role (ROL-009) w/ justification 'Lower-privilege role after cert expiry.' Evaluate it and appprove or reject it. Return sessions and audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-002"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-021"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-020"}),
            Action(
                name="create_access_request",
                kwargs={
                    "request_id": "AR-062",
                    "user_id": "U-020",
                    "resource_id": "RES-018",
                    "requested_role_id": "ROL-009",
                    "justification": "Lower-privilege role after cert expiry.",
                    "submitted_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-062",
                    "reviewer_id": "U-002",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-062",
                    "reviewer_id": "U-002",
                    "approve": False,
                    "notes": "Requested role does not cover target resource.",
                    "decision_at": "2024-06-26 16:05:00+00:00",
                },
            ),
            Action(name="get_user_sessions", kwargs={"user_id": "U-020"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-062"},
            ),
        ],
        outputs=[{"U-020_SESSIONS": [], "AUDIT_LOG_ID": ["LOG-AR-062-decision"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_091_certification_finance_approval",
        instruction=(
            "You are U-006 (finance-lead) with certification and access review authority. You want to process the overdue certification C-019 for quarterly financial reports and evaluate pending access request AR-008 from U-030 for finance-budget-admin role, since the certification validates the prerequisite finance-base requirement."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"status": "PENDING", "certification_id": "C-019"},
            ),
            Action(
                name="complete_certification",
                kwargs={"certification_id": "C-019", "reviewer_id": "U-006"},
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-008",
                    "reviewer_id": "U-006",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-006",
                    "approve": True,
                    "notes": "Met prerequisite finance-base (ROL-029).",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-008", "assigned_by": "U-006"},
            ),
            Action(name="get_user_email", kwargs={"user_id": "U-030"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "marisa.cole@taucorp.com",
                    "subject": "AR-008 APPROVED",
                    "text_content": "U-006 2024-06-26 16:05:00+00:00",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_092_siem_investigation_policy_exception",
        instruction=(
            "You are U-005 (operations-lead) with SIEM and security incident authority. You want to investigate and respond to critical SIEM alert ALRT-012, review any related policy exceptions for user U-004, update HubSpot ticket TI-053 with your findings and note 'SIEM alert acknowleged', and send a security briefing email to emily.jones@taucorp.com. The email body should be 'Security briefing: ALRT-012 investigated - U-005 at 2024-06-26 16:05:00+00:00.' and subject should be 'Security Incident - ALRT-012.'"
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="list_siem_alerts", kwargs={"alert_id": "ALRT-012"}),
            Action(
                name="acknowledge_siem_alert",
                kwargs={
                    "alert_id": "ALRT-012",
                    "ack_by": "U-005",
                    "status": "ACKNOWLEDGED",
                    "note": "Triage started.",
                },
            ),
            Action(
                name="list_policy_exceptions",
                kwargs={"user_id": "U-004", "active_only": True},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-004"}),
            Action(
                name="update_hubspot_ticket_status",
                kwargs={
                    "ticket_id": "TI-053",
                    "status": "IN_PROGRESS",
                    "actor_id": "U-005",
                    "note": "SIEM alert acknowleged",
                },
            ),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "emily.jones@taucorp.com",
                    "subject": "Security Incident - ALRT-012.",
                    "text_content": (
                        "Security briefing: ALRT-012 investigated - U-005 at 2024-06-26 16:05:00+00:00."
                    ),
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"action_type": "HUBSPOT_TICKET_UPDATED", "target_id": "TI-053"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_093_cross_department_role_cleanup",
        instruction=(
            "You are U-004 (hr-lead) with role management authority. You want to clean up excessive permissions for user U-027 (disabled sales user) by removing inappropriate sales-base role ROL-011 and notify them via email. Return the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-004"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-027"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-011"}),
            Action(
                name="check_user_status",
                kwargs={"mode": "revoke", "user_id": "U-027", "role_id": "ROL-011"},
            ),
            Action(
                name="revoke_role",
                kwargs={"user_id": "U-027", "role_id": "ROL-011", "actor_id": "U-004"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-027"}),
            Action(name="get_user_email", kwargs={"user_id": "U-027"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "gary.campbell@taucorp.com",
                    "subject": "ROL-011 APPROVED",
                    "text_content": "U-004 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={
                    "action_type": "revoke_role",
                    "actor_id": "U-004",
                    "target_id": "U-027:ROL-011",
                },
            ),
        ],
        outputs=[{"AUDIT_LOG_ID": ["LOG-U-027-ROL-011-revoke"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_094_mfa_access_approval",
        instruction=(
            "You are U-001 (engineering-lead) with access management authority. You want to evaluate access request AR-020 and make a decision to approve or reject the request. Enable MFA for the requester before evaluating the request. Notify the user by email of the decision."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-001"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-020"}),
            Action(name="set_user_mfa", kwargs={"user_id": "U-013", "enabled": True}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-020",
                    "reviewer_id": "U-001",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-020",
                    "reviewer_id": "U-001",
                    "approve": False,
                    "notes": "Required certification not completed.",
                },
            ),
            Action(name="get_user_email", kwargs={"user_id": "U-013"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "brian.taylor@taucorp.com",
                    "subject": "AR-020 REJECTED",
                    "text_content": "U-001 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"action_type": "review_access_request", "target_id": "AR-020"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_095_process_U_022",
        instruction=(
            "You are U-002 (marketing-lead). You need to review AR-030 according to policy, make a decision to approve or reject the request, and follow up with an email notification to the requester. "
            "Return the decision, notes, the requester's roles, active sessions and the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-002"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-030"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-022"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-030",
                    "reviewer_id": "U-002",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-002",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-030"}),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-030", "assigned_by": "U-002"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-022"}),
            Action(name="get_user_email", kwargs={"user_id": "U-022"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "brittany.king@taucorp.com",
                    "subject": "AR-030 APPROVED",
                    "text_content": "U-002 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-030"},
            ),
            Action(name="get_user_sessions", kwargs={"user_id": "U-022"}),
        ],
        outputs=[
            {
                "AR-030": "APPROVED",
                "NOTES": (
                    "Certification verified; within clearance and least-privilege."
                ),
                "U-022_SESSIONS": [],
                "U-022_ROLES": ["ROL-016", "ROL-017"],
                "AUDIT_LOG_ID": ["LOG-AR-030-decision"],
            }
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_096_cert_recert_and_process_AR_030",
        instruction=(
            "You are U-003 with certification and access review authority. You want to start & process certification C-021. Then, evaluate AR-030 and make a decision to approve or reject the request. If approved, grant the role and return the audit log id."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-003"}),
            Action(
                name="start_certification",
                kwargs={"certification_id": "C-021", "reviewer_id": "U-003"},
            ),
            Action(
                name="complete_certification",
                kwargs={
                    "certification_id": "C-021",
                    "completed_on": "2024-06-26 16:05:00+00:00",
                    "reviewer_id": "U-003",
                },
            ),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-021"},
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-030"}),
            Action(name="get_role_permissions", kwargs={"role_id": "ROL-017"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-030",
                    "reviewer_id": "U-003",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-030",
                    "reviewer_id": "U-003",
                    "approve": True,
                    "notes": (
                        "Certification verified; within clearance and least-privilege."
                    ),
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-030", "assigned_by": "U-003"},
            ),
        ],
        outputs=[{"AUDIT_LOG_ID": ["LOG-AR-030-decision"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_097_hubspot_emergency_provisioning",
        instruction=(
            "You are U-005 (operations-lead). You want to process certification C-013 to status COMPLETED, evaluate access request AR-037 against policy, make a decision to approve or reject, and notify U-010 via email."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-037"}),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-013"},
            ),
            Action(
                name="complete_certification",
                kwargs={"certification_id": "C-013", "reviewer_id": "U-005"},
            ),
            Action(
                name="list_certifications_by_status",
                kwargs={"certification_id": "C-013"},
            ),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-037",
                    "reviewer_id": "U-005",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-037",
                    "reviewer_id": "U-005",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_user_email", kwargs={"user_id": "U-010"}),
            Action(
                name="send_email",
                kwargs={
                    "email_id": "EM-9601",
                    "receiver": "ashley.wilson@taucorp.com",
                    "subject": "AR-037 REJECTED",
                    "text_content": "U-005 2024-06-26 16:05:00+00:00",
                },
            ),
            Action(
                name="list_audit_logs",
                kwargs={"action_type": "review_access_request", "target_id": "AR-037"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="faris",
        user_id="faris_098_finance_budget_admin_approval",
        instruction=(
            "You are U-006 (finance-lead) with decision authority over access requests. Review AR-008, make a decision to approve or reject the request, and return the requester's roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-008"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-030"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-008",
                    "reviewer_id": "U-006",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-008",
                    "reviewer_id": "U-006",
                    "approve": True,
                    "notes": "Met prerequisite finance-base (ROL-029).",
                },
            ),
            Action(
                name="grant_role",
                kwargs={"request_id": "AR-008", "assigned_by": "U-006"},
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
            Action(name="list_access_requests_by_user", kwargs={"user_id": "U-030"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "user_id": "U-006"},
            ),
        ],
        outputs=[{"U-030_ROLES": ["ROL-029", "ROL-032"]}],
    ),
    Task(
        annotator="faris",
        user_id="faris_099_marketing_analytics_duplicate_request",
        instruction=(
            "You are U-002 with marketing authority over access requests. You want to review AR-040 for U-014 and make a decision to approve or reject the request. Return U-014's current active sessions, roles, and AR-040 decision and notes. Also, return the audit log for AR-040."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-002"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-040"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-040",
                    "reviewer_id": "U-002",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-040",
                    "reviewer_id": "U-002",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_user_roles", kwargs={"user_id": "U-014"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-040"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-014"}),
            Action(
                name="list_audit_logs",
                kwargs={"filter_by": "review_access_request", "target_id": "AR-040"},
            ),
        ],
        outputs=[
            {
                "U-014_ROLES": ["ROL-006", "ROL-009"],
                "AR-040": "REJECTED",
                "NOTES": "Already assigned.",
                "U-014_SESSIONS": [],
                "AUDIT_LOG_ID": ["LOG-AR-040-decision"],
            },
            [
                {
                    "log_id": "LOG-AR-040-decision",
                    "actor_id": "U-002",
                    "action_type": "review_access_request",
                    "target_id": "AR-040",
                    "timestamp": "2024-06-26 16:05:00+00:00",
                    "details": "REJECTED",
                }
            ],
        ],
    ),
    Task(
        annotator="faris",
        user_id="faris_100_engineering_code_commit_duplicate",
        instruction=(
            "You are U-001 with engineering authority over access requests. You want to review AR-027 for U-007 and make a decision to approve or reject the request. Return U-007's current session status and roles."
        ),
        actions=[
            Action(name="get_user_roles", kwargs={"user_id": "U-001"}),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-027"}),
            Action(name="get_user_roles", kwargs={"user_id": "U-007"}),
            Action(
                name="check_user_status",
                kwargs={
                    "mode": "access_request",
                    "request_id": "AR-027",
                    "reviewer_id": "U-001",
                },
            ),
            Action(
                name="update_access_request_status",
                kwargs={
                    "request_id": "AR-027",
                    "reviewer_id": "U-001",
                    "approve": False,
                    "notes": "Already assigned.",
                },
            ),
            Action(name="get_access_request_details", kwargs={"request_id": "AR-027"}),
            Action(name="get_user_sessions", kwargs={"user_id": "U-007"}),
        ],
        outputs=[{"U-007_ROLES": ["ROL-001", "ROL-002"], "U-007_SESSIONS": []}],
    ),
]
