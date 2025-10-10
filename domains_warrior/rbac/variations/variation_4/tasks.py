from domains.dto import Task, Action

TASKS = [


# - TASK 1 -

Task(
    annotator="0",
    user_id="001",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. Review access request AR-007 on RES-025 in line with policy: "
        "only Operations reviewers may approve requests for RES-025, and the requested role’s permissions must all be scoped to RES-025. "
        "If you lack authorization or if the role permissions extend beyond RES-025, reject the request and record this decision in the audit log. "
        "If the reviewer is authorized and all permissions are properly scoped, approve the request, log the approval, "
        "and assign the role to Patrick Carter (U-029). Return both the processed request and Patrick Carter’s roles after processing."
    ),
    actions=[
        Action(name="get_access_request", kwargs={"request_id": "AR-007"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="get_user_details", kwargs={"user_id": "U-001"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-026"}),
        Action(name="reject_access_request", kwargs={
            "request_id": "AR-007",
            "reviewer_id": "U-001",
            "decision_at": "2024-05-20T14:00:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-001",
            "action_type": "ACCESS_REJECTED",
            "target_id": "AR-007",
            "timestamp": "2024-05-20T14:00:00Z",
            "details": "request=AR-007|resource=RES-025|role=ROL-026|reviewer=U-001|reviewer_dept=Engineering|required_reviewer_dept=Operations|perm_scope=RES-024|scope_match=false|decision=REJECTED"
        }),
        Action(name="get_user_roles", kwargs={"user_id": "U-029"})
    ],
    outputs=[
        '[{"request_id":"AR-007","user_id":"U-029","resource_id":"RES-025","requested_role_id":"ROL-026","status":"REJECTED","submitted_at":"2024-05-20 14:00:00+00:00","reviewed_by":"U-001","decision_at":"2024-05-20T14:00:00Z"}]',
        '[{"role_id":"ROL-021","role_name":"operations-base","description":"Basic access for operations staff","is_temporary":false}]'
    ]
),


# - TASK 2 -

Task(
    annotator="0",
    user_id="002",
    instruction=(
        "You are Michael Davis (U-005), Operations. Close the certification for Jeffery Green (C-020, user U-023) in line with Operations policy, "
        "approve policy exception PE-012 with reviewed_on=2025-08-12T23:00:00Z and expires_on=2025-09-21T04:59:59Z (after its requested_on), "
        "and enforce session hygiene by confirming whether session S-024 is still active before taking any termination action. "
        "Provide a policy-facing summary of ACTIVE policy exceptions for Operations users as {\"open_exceptions_for_operations\": [...]}, "
        "and also return a consolidated certification completion object for C-020."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="get_user_details", kwargs={"user_id": "U-023"}),

        Action(name="get_certification_details", kwargs={"certification_id": "C-020"}),
        Action(name="complete_certification", kwargs={"certification_id": "C-020", "completed_on": "2025-11-08T04:59:59Z"}),

        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-012"}),
        Action(name="approve_policy_exception", kwargs={
            "exception_id": "PE-012",
            "reviewed_by": "U-005",
            "expires_on": "2025-09-21T04:59:59Z",
            "reviewed_on": "2025-08-12T23:00:00Z"
        }),

        Action(name="list_user_sessions", kwargs={"user_id": "U-023", "active_only": True}),
        Action(name="list_sessions", kwargs={"user_id": "U-023"}),

        Action(name="list_users", kwargs={"department": "Operations"}),
        Action(name="list_policy_exceptions", kwargs={"user_id": "U-005", "status": "ACTIVE"}),
        Action(name="list_policy_exceptions", kwargs={"user_id": "U-017", "status": "ACTIVE"}),
        Action(name="list_policy_exceptions", kwargs={"user_id": "U-023", "status": "ACTIVE"})
    ],
    outputs=[
        '[{"open_exceptions_for_operations":['
            '{"exception_id":"PE-020","status":"ACTIVE","user_id":"U-017"},'
            '{"exception_id":"PE-012","status":"ACTIVE","user_id":"U-023"}'
        ']}]',
        '[{"certification_C-020":{"status":"COMPLETED","completed_on":"2025-11-08T04:59:59Z"}}]'
    ]
),


# - TASK 3 -
Task(
    annotator="0",
    user_id="003",
    instruction=(
        "You are Patrick Carter (U-029), Operations. Under RBAC/SoD, have an ACTIVE Operations analyst "
        "(use U-005) investigate SIEM alert ALRT-005 on RES-025 and record the note 'Verified false positive' "
        "at 2025-08-10T22:16:00Z. Capture a SoD attestation by logging a compliance entry indicating the "
        "analyst, the resource in scope, and that no conflicts were found. Return the investigation confirmation."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-029"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
        Action(name="get_siem_alert_details", kwargs={"alert_id": "ALRT-005"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-029",
                "action_type": "SOD_CHECK",
                "target_ref": {"kind":"OBJECT","id":"ALRT-005"},
                "timestamp": "2025-08-10T22:16:00Z",
                "details": "analyst=U-005|scope=RES-025|conflicts=None"
            }),
        Action(name="investigate_siem_incident", kwargs={
                "alert_id": "ALRT-005",
                "analyst_id": "U-005",
                "notes": "Verified false positive",
                "investigated_on": "2025-08-10T22:16:00Z"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-029",
                "action_type": "INVESTIGATION_RECORDED",
                "target_ref": {"kind":"OBJECT","id":"ALRT-005"},
                "timestamp": "2025-08-10T22:16:00Z",
                "details": "investigation=INV-001|analyst=U-005|resource=RES-025"
            })
    ],
    outputs=['{"success": "Investigation INV-001 recorded"}']
),


# - TASK 4 -
Task(
    annotator="0",
    user_id="004",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. Approve PE-018 at T0=2025-08-06 15:30:00+00:00 and export the audit with "
        "start_time=end_time=T0. Notify U-007 with a deterministic message: subject='NOTICE:PE-018:APPROVED', "
        "body='exception=PE-018|permission=P-005|subject=U-007|reviewed_on=2025-08-06 15:30:00+00:00|expires_on=2025-11-16 04:59:59+00:00', "
        "timestamp=T0. Return the updated exception."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-001"}),
        Action(name="get_policy_exception_details", kwargs={"exception_id":"PE-018"}),
        Action(name="get_user_details", kwargs={"user_id":"U-007"}),
        Action(name="get_permission_details", kwargs={"permission_id":"P-005"}),
        Action(name="approve_policy_exception", kwargs={
            "exception_id":"PE-018","reviewed_by":"U-001",
            "expires_on":"2025-11-16 04:59:59+00:00","reviewed_on":"2025-08-06 15:30:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-001","action_type":"POLICY_EXCEPTION_APPROVED","target_id":"PE-018",
            "timestamp":"2025-08-06 15:30:00+00:00","details":"permission=P-005|subject=U-007|decision=APPROVED"
        }),
        Action(name="export_audit_logs", kwargs={
            "actor_id":"U-001","action_type":"POLICY_EXCEPTION_APPROVED","target_id":"PE-018",
            "start_time":"2025-08-06 15:30:00+00:00","end_time":"2025-08-06 15:30:00+00:00"
        }),
        Action(name="send_email", kwargs={
            "sender":"U-001","receiver":"U-007",
            "subject":"NOTICE:PE-018:APPROVED",
            "body":"exception=PE-018|permission=P-005|subject=U-007|reviewed_on=2025-08-06 15:30:00+00:00|expires_on=2025-11-16 04:59:59+00:00",
            "timestamp":"2025-08-06 15:30:00+00:00"
        }),
        Action(name="get_policy_exception_details", kwargs={"exception_id":"PE-018"})
    ],
    outputs=[
        '{"exception_id":"PE-018","user_id":"U-007","reviewed_by":"U-001","reviewed_on":"2025-08-06 15:30:00+00:00",'
        '"expires_on":"2025-11-16 04:59:59+00:00","status":"ACTIVE"}'
    ]
),


# - TASK 5 -
Task(
    annotator="0",
    user_id="005",
    instruction=(
        "You are Michael Davis (U-005) in Operations. Under exception control, PE-012 for Alex Johnson (U-023) must be in effect "
        "with reviewed_on=2025-08-12 23:00:00+00:00 and expires_on=2025-09-21 04:59:59+00:00. Your outcome is an ACTIVE record for PE-012 "
        "within the canonical store and one audit entry that captures deterministic fields (exception_id, user_id, status=ACTIVE, "
        "reviewed_on, expires_on). Ensure the stored record reflects this state before you report U-023’s ACTIVE exceptions."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="get_user_details", kwargs={"user_id": "U-023"}),
        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-012"}),
        Action(name="approve_policy_exception", kwargs={
            "exception_id": "PE-012",
            "reviewed_by": "U-005",
            "reviewed_on": "2025-08-12 23:00:00+00:00",
            "expires_on": "2025-09-21 04:59:59+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-005",
            "action_type": "POLICY_EXCEPTION_APPROVED",
            "target_id": "PE-012",
            "timestamp": "2025-08-12 23:00:00+00:00",
            "details": "user=U-023|status=ACTIVE|expires_on=2025-09-21 04:59:59+00:00"
        }),
        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-012"}),
        Action(name="list_policy_exceptions", kwargs={"status": "ACTIVE", "user_id": "U-023"})
    ],
    outputs=[
        '[{"exception_id":"PE-012","status":"ACTIVE","user_id":"U-023"}]'
    ]
),


# - TASK 6 -
Task(
    annotator="0",
    user_id="006",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. AR-007 requests ROL-026 on RES-025, submitted_at=2024-05-20 14:00:00+00:00. "
        "Apply reviewer-scope policy: only reviewers in Operations may approve. Your department is Engineering, so reject at submitted_at. "
        "Provide: processed_request, requester_roles_after (U-029), role_scope_summary (ROL-026 permission_ids/resource_ids), "
        "role_membership_after (ROL-026), reviewer (user_id, department), owner (RES-025 owner), audit_slices (targets AR-007 and U-029)."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-001"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-007"}),
        Action(name="get_user_details", kwargs={"user_id": "U-029"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-026"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-026"}),
        Action(name="reject_access_request", kwargs={
            "request_id": "AR-007", "reviewer_id": "U-001", "decision_at": "2024-05-20 14:00:00+00:00"
        }),
        Action(name="get_access_request", kwargs={"request_id": "AR-007"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
        Action(name="get_role_members", kwargs={"role_id": "ROL-026"}),
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="get_audit_logs_for_target", kwargs={"target_id": "AR-007"}),
        Action(name="get_audit_logs_for_target", kwargs={"target_id": "U-029"}),
    ],
    outputs=[
        '{"processed_request":{"request_id":"AR-007","user_id":"U-029","resource_id":"RES-025","requested_role_id":"ROL-026","justification":"Urgent request for full system admin access for incident response.","status":"REJECTED","submitted_at":"2024-05-20 14:00:00+00:00","reviewed_by":"U-001","decision_at":"2024-05-20 14:00:00+00:00"},"requester_roles_after":[{"role_id":"ROL-021","role_name":"operations-base","description":"Basic access for operations staff","is_temporary":false}],"role_scope_summary":{"role_id":"ROL-026","permission_ids":["P-060","P-061","P-062","P-089"],"resource_ids":["RES-024"]},"role_membership_after":[],"reviewer":{"user_id":"U-001","department":"Engineering"},"owner":{"user_id":"U-005"},"audit_slices":{"request_target":"AR-007","requester_target":"U-029"}}'
    ],
),


# - TASK 7 -
Task(
    annotator="0",
    user_id="007",
    instruction=(
        "You are Michael Davis (U-005) from Operations. "
        "Revoke the sales-base role (ROL-011) from Paul Ellis (U-021) as it applies to the resource 'customer-contract-storage' (RES-018). "
        "Follow all policy requirements for revocations affecting resource-linked roles, ensuring every dependency and compliance check is fulfilled. "
        "Return Paul’s updated roles."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),                  # actor context
        Action(name="get_user_details", kwargs={"user_id": "U-021"}),                  # subject
        Action(name="get_user_roles", kwargs={"user_id": "U-021"}),                    # current roles
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-011"}),       # verify role scope
        Action(name="get_resource_details", kwargs={"resource_id": "RES-018"}),        # target resource
        Action(name="list_policy_exceptions", kwargs={"user_id": "U-021", "status": "ACTIVE"}),  # ensure no ACTIVE exception blocks revoke
        Action(name="create_audit_log", kwargs={                                       # SoD/justification attestation
            "actor_id": "U-005",
            "action_type": "SOD_CHECK",
            "target_ref": {"kind": "USER", "id": "U-021"},
            "details": "subject=U-021|role=ROL-011|resource=RES-018|conflicts=None"
        }),
        Action(name="revoke_role", kwargs={"user_id": "U-021", "role_id": "ROL-011"}), # revoke
        Action(name="get_user_roles", kwargs={"user_id": "U-021"}),                    # post-state
    ],
    outputs=[
        '{"user_id": "U-021", "roles": [{"role_id": "ROL-013", "role_name": "sales-lead-manager", "description": "Manages sales leads and opportunities", "is_temporary": false}, {"role_id": "ROL-014", "role_name": "sales-reporting", "description": "Generates sales performance reports", "is_temporary": false}]}'
    ]
),


# - TASK 8 -
Task(
    annotator="0",
    user_id="008",
    instruction=(
        "You are Nicole Thomas (U-014), owner of RES-012 (blog-cms). Adjudicate access request AR-021 for role "
        "ROL-010 under RBAC with segregation-of-duties controls. Use the request’s submitted_at as the authoritative "
        "decision timestamp. Deny any request that duplicates an existing entitlement on the same resource; otherwise approve. "
        "Create an auditable record that includes requester, resource, role, and any SoD/duplicate findings. After adjudication, "
        "return the set of APPROVED requests for RES-012 based solely on canonical dataset records and timestamps."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-014"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-012"}),

        Action(name="get_access_request", kwargs={"request_id": "AR-021"}),

        Action(name="get_user_details", kwargs={"user_id": "U-026"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-026"}),

        Action(name="create_audit_log", kwargs={
            "actor_id": "U-014",
            "action_type": "SOD_CHECK",
            "target_id": "AR-021",
            "timestamp": "2024-05-26 15:00:00+00:00",
            "details": "request_id=AR-021|requester=U-026|resource=RES-012|role=ROL-010|duplicate_entitlement=true|sod_conflicts=NONE"
        }),

        Action(name="reject_access_request", kwargs={
            "request_id": "AR-021",
            "reviewer_id": "U-014",
            "decision_at": "2024-05-26 15:00:00+00:00"
        }),

        Action(name="create_audit_log", kwargs={
            "actor_id": "U-014",
            "action_type": "ACCESS_REJECTED",
            "target_id": "AR-021",
            "timestamp": "2024-05-26 15:00:00+00:00",
            "details": "reason=DUPLICATE_ENTITLEMENT|request_id=AR-021|requester=U-026|resource=RES-012|role=ROL-010"
        }),

        Action(name="list_access_requests", kwargs={"status": "APPROVED", "resource_id": "RES-012"})
    ],
    outputs=[
        '[{"request_id":"AR-032","user_id":"U-008","resource_id":"RES-012","requested_role_id":"ROL-010","status":"APPROVED"}]'
    ]
),



# - TASK 9 -
Task(
    annotator="0",
    user_id="009",
    instruction=(
        "You are Lisa Anderson (U-012), Finance owner of invoicing-system (RES-032). "
        "Apply Finance access policy for access request AR-008 from Marisa Cole (U-030) to role ROL-032 on RES-032: "
        "approve only if the requester’s mfa_enabled=true for HIGH-criticality resources. "
        "Resolve the request using its submitted_at as the decision timestamp. "
        "Do not open tickets or post messages. Return Marisa’s roles for RES-032 after resolution."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-012"}),
        Action(name="get_user_details", kwargs={"user_id": "U-030"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-032"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-008"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
        Action(
            name="reject_access_request",
            kwargs={
                "request_id": "AR-008",
                "reviewer_id": "U-012",
                "decision_at": "2024-05-20 15:00:00+00:00"
            },
        ),
        Action(name="get_user_roles", kwargs={"user_id": "U-030"}),
    ],
    outputs=[
        '[{"role_id":"ROL-029","role_name":"finance-base","description":"Basic access for finance staff","is_temporary":false}]'
    ],
),


# - TASK 10 -
Task(
    annotator="0",
    user_id="010",
    instruction=(
        "You are Lisa Anderson (U-012), Finance. You own RES-032. "
        "Decide AR-008 at 2024-05-20 15:00:00+00:00 using access policy: approve if you are ACTIVE, "
        "the request targets your resource, and the requested role scopes to that resource. "
        "After approval, grant the requested role to the requester effective at the decision time. "
        "Record one decision evidence entry using key=value tokens. "
        "Provide: processed_request, owner_status, requester_details (U-030 full record), resource_details, "
        "role_meta, role_membership_before, role_membership_after, active_exceptions_for_requester, "
        "grant_record (including user_role_id), decision_evidence, audit_entry, and permission_details_sample (P-080 full record)."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-012"}),
        Action(name="get_access_request", kwargs={"request_id":"AR-008"}),
        Action(name="get_user_details", kwargs={"user_id":"U-030"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-032"}),
        Action(name="get_role_details", kwargs={"role_id":"ROL-032"}),
        Action(name="list_permissions_for_role", kwargs={"role_id":"ROL-032"}),
        Action(name="get_role_members", kwargs={"role_id":"ROL-032"}),
        Action(name="list_policy_exceptions", kwargs={"user_id":"U-030","status":"ACTIVE"}),
        Action(name="approve_access_request", kwargs={
            "request_id":"AR-008",
            "reviewer_id":"U-012",
            "decision_at":"2024-05-20 15:00:00+00:00"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id":"U-030",
            "role_id":"ROL-032",
            "assigned_by":"U-012",
            "assigned_on":"2024-05-20 15:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-012",
            "action_type":"ACCESS_APPROVED",
            "target_id":"AR-008",
            "timestamp":"2024-05-20 15:00:00+00:00",
            "details":"owner=U-012|resource=RES-032|role=ROL-032|exceptions=0"
        }),
        Action(name="get_access_request", kwargs={"request_id":"AR-008"}),
        Action(name="get_role_members", kwargs={"role_id":"ROL-032"}),
        Action(name="get_permission_details", kwargs={"permission_id":"P-080"})
    ],
    outputs=[
        '{"processed_request":{"request_id":"AR-008","user_id":"U-030","resource_id":"RES-032","requested_role_id":"ROL-032","justification":"Need to create budgets for Q3 planning.","status":"APPROVED","submitted_at":"2024-05-20 15:00:00+00:00","reviewed_by":"U-012","decision_at":"2024-05-20 15:00:00+00:00"},'
        '"owner_status":{"user_id":"U-012","status":"ACTIVE"},'
        '"requester_details":{"user_id":"U-030","username":"maria_garcia","department":"Finance","status":"ACTIVE","mfa_enabled":true},'
        '"resource_details":{"resource_id":"RES-032","owner_id":"U-012","criticality":"HIGH","compliance_scope":"PCI-DSS"},'
        '"role_meta":{"role_id":"ROL-032","role_name":"finance-budget-admin","description":"Administers departmental budgets","is_temporary":false},'
        '"role_membership_before":["U-012"],'
        '"role_membership_after":["U-012","U-030"],'
        '"active_exceptions_for_requester":[],'
        '"grant_record":{"user_role_id":"UR-078","user_id":"U-030","role_id":"ROL-032","assigned_by":"U-012","assigned_on":"2024-05-20 15:00:00+00:00","expires_on":null},'
        '"decision_evidence":"owner=U-012|resource=RES-032|role=ROL-032|exceptions=0",'
        '"audit_entry":{"actor_id":"U-012","action_type":"ACCESS_APPROVED","target_id":"AR-008","timestamp":"2024-05-20 15:00:00+00:00","details":"owner=U-012|resource=RES-032|role=ROL-032|exceptions=0"},'
        '"permission_details_sample":{"permission_id":"P-080","permission_name":"finance-create-budget","description":"Allows creation of quarterly and annual budgets","criticality":"HIGH"}}'
    ]
),


# - TASK 11 -
Task(
    annotator="0",
    user_id="011",
    instruction=(
        "You are Patrick Carter (U-029), Operations (ACTIVE) and owner of RES-025. "
        "Evaluate access request AR-007 for role ROL-026 under the policy that approvals require the role’s permissions to match the target resource. "
        "Because ROL-026 is scoped to RES-024, this request does not meet the policy. "
        "Apply a deterministic decision timestamp aligned with the request’s submission and then provide all APPROVED requests for RES-025."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-029"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-026"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-007"}),
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="reject_access_request", kwargs={
            "request_id": "AR-007",
            "reviewer_id": "U-005",
            "decision_at": "2024-05-20T14:00:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-005",
            "action_type": "ACCESS_REJECTED",
            "target_id": "AR-007",
            "timestamp": "2024-05-20T14:00:00Z",
            "details": "reason=ROLE_SCOPE_MISMATCH|role=ROL-026(scope=RES-024)|target_resource=RES-025|requester=U-029"
        }),
        Action(name="list_access_requests", kwargs={"status": "APPROVED", "resource_id": "RES-025"}),
    ],
    outputs=[
        '[{"request_id":"AR-001","user_id":"U-007","resource_id":"RES-025","requested_role_id":"ROL-023",'
        '"justification":"Need temporary access to production for urgent bug fix.","status":"APPROVED",'
        '"submitted_at":"2024-04-15T15:00:00Z","reviewed_by":"U-005","decision_at":"2024-04-15T16:00:00Z"},'
        '{"request_id":"AR-014","user_id":"U-025","resource_id":"RES-025","requested_role_id":"ROL-003",'
        '"justification":"Temporary production access for debugging a new deployment.","status":"APPROVED",'
        '"submitted_at":"2024-05-22T16:00:00Z","reviewed_by":"U-001","decision_at":"2024-05-23T16:45:00Z"}]'
    ],
),


# - TASK 12 -
Task(
    annotator="0",
    user_id="012",
    instruction=(
        "You are Sarah Williams (U-002), owner of RES-008. Approve AR-009 at T0=2024-05-20 16:00:00+00:00, export the audit with "
        "start_time=end_time=T0, and notify U-026 deterministically with subject='NOTICE:AR-009:APPROVED', "
        "body='resource=RES-008|role=ROL-008|decision_at=T0', timestamp=T0. Return the processed request."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-002"}),
        Action(name="get_access_request", kwargs={"request_id":"AR-009"}),
        Action(name="get_user_details", kwargs={"user_id":"U-026"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-008"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-026"}),
        Action(name="approve_access_request", kwargs={
            "request_id":"AR-009","reviewer_id":"U-002","decision_at":"2024-05-20 16:00:00+00:00"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id":"U-026","role_id":"ROL-008","assigned_by":"U-002","assigned_on":"2024-05-20 16:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-002","action_type":"ACCESS_GRANTED","target_id":"AR-009",
            "timestamp":"2024-05-20 16:00:00+00:00",
            "details":"resource=RES-008|role=ROL-008|subject=U-026|decision=APPROVED"
        }),
        Action(name="export_audit_logs", kwargs={
            "actor_id":"U-002","action_type":"ACCESS_GRANTED","target_id":"AR-009",
            "start_time":"2024-05-20 16:00:00+00:00","end_time":"2024-05-20 16:00:00+00:00"
        }),
        Action(name="send_email", kwargs={
            "sender":"U-002","receiver":"U-026",
            "subject":"NOTICE:AR-009:APPROVED",
            "body":"resource=RES-008|role=ROL-008|decision_at=T0",
            "timestamp":"2024-05-20 16:00:00+00:00"
        }),
        Action(name="get_access_request", kwargs={"request_id":"AR-009"})
    ],
    outputs=[
        '[{"request_id":"AR-009","user_id":"U-026","resource_id":"RES-008","requested_role_id":"ROL-008","status":"APPROVED",'
        '"submitted_at":"2024-05-20 16:00:00+00:00","reviewed_by":"U-002","decision_at":"2024-05-20 16:00:00+00:00"}]'
    ]
),


# - TASK 13 -
Task(
    annotator="0",
    user_id="013",
    instruction=(
        "You are Jessica Garcia (U-006), Finance, and you own RES-034. At T0=2024-05-30 15:00:00+00:00, you must decide "
        "access request AR-034 from U-018 for role ROL-030 on RES-034. You must enforce the Finance conflict rule: "
        "reject the request if the requester already holds permissions on another Finance system that conflict with RES-034. "
        "From the dataset, U-018 already has access to RES-032 with permission P-082, which conflicts with RES-034. "
        "Therefore, you must reject AR-034 at T0, record a compliance audit entry with conflict details, and return "
        "the post-decision state of the request along with verification of the conflict, the requester’s current roles, "
        "and the metadata of the Finance base role."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-006"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-034"}),
        Action(name="get_user_details", kwargs={"user_id": "U-018"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-029"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-030"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-034"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-032"}),
        Action(name="reject_access_request", kwargs={
            "request_id":"AR-034",
            "reviewer_id":"U-006",
            "decision_at":"2024-05-30 15:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-006",
            "action_type":"ACCESS_REJECTED",
            "target_id":"AR-034",
            "timestamp":"2024-05-30 15:00:00+00:00",
            "details":"reason=CONFLICT|conflict_perm=P-082@RES-032|requester=U-018"
        }),
        Action(name="get_access_request", kwargs={"request_id": "AR-034"}),
        Action(name="get_audit_logs_for_target", kwargs={"target_id": "AR-034"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-029"}),
    ],
    outputs=[
        '[{"processed_request":{"request_id":"AR-034","user_id":"U-018","resource_id":"RES-034","requested_role_id":"ROL-030","justification":"Requesting read access to tax compliance software.","status":"REJECTED","submitted_at":"2024-05-30 15:00:00+00:00","reviewed_by":"U-006","decision_at":"2024-05-30 15:00:00+00:00"},"verification":{"has_res_032_access":true,"conflicting_permission_ids":["P-082"]},"requester_roles":[{"role_id":"ROL-029","role_name":"finance-base","description":"Basic access for finance staff","is_temporary":false},{"role_id":"ROL-033","role_name":"finance-audit-access","description":"Access for external audit purposes","is_temporary":true}],"audit_slice":{"target_id":"AR-034"},"role_meta":{"role_id":"ROL-029","role_name":"finance-base","description":"Basic access for finance staff","is_temporary":false}}]'
    ],
),


# - TASK 14 -
Task(
    annotator="0",
    user_id="014",
    instruction=(
        "You are Laura Jackson (U-016) from Human Resources. "
        "As an ACTIVE HR staff member and reviewer, you are responsible for completing the certification C-011 for Ashley Wilson (U-010) on the customer-data-list resource (RES-011). "
        "If all participants—including yourself, Ashley, and the certification reviewer Sarah Williams (U-002)—have ACTIVE status, and if the policy permits, finalize C-011 with status COMPLETED and completed_on set to '2025-08-12T22:30:00Z'. "
        "Return the deterministic record of completion."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-016"}),
        Action(name="get_user_details", kwargs={"user_id": "U-010"}),
        Action(name="get_certification_details", kwargs={"certification_id": "C-011"}),
        Action(name="get_user_details", kwargs={"user_id": "U-002"}),
        Action(
            name="complete_certification",
            kwargs={
                "certification_id": "C-011",
                "completed_on": "2025-08-12T22:30:00Z"
            }
        ),
        Action(name="get_certification_details", kwargs={"certification_id": "C-011"})
    ],
    outputs=[
        '{"certification_id": "C-011", "status": "COMPLETED", "reviewer_id": "U-002", "resource_id": "RES-011", "completed_on": "2025-08-12T22:30:00Z"}'
    ],
),


# - TASK 15 -
Task(
    annotator="0",
    user_id="015",
    instruction=(
        "You are Michael Davis (U-005), Operations. At 2024-06-10 15:45:00+00:00, the canonical state for ALRT-003 on RES-020 must reflect severity "
        "CRITICAL consistent with resource classification. Maintain one investigation note at that instant and one audit capturing "
        "alert_id, resource_id, final_severity, handled_at. Validate via the detailed alert view and the alert record, then report the resulting severity."
    ),
    actions=[
        Action(name="get_siem_alert_details", kwargs={"alert_id": "ALRT-003"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-020"}),
        Action(name="investigate_siem_incident", kwargs={
            "alert_id": "ALRT-003",
            "analyst_id": "U-005",
            "notes": "resource=RES-020|handled_at=2024-06-10 15:45:00+00:00",
            "investigated_on": "2024-06-10 15:45:00+00:00"
        }),
        Action(name="escalate_siem_alert", kwargs={
            "alert_id": "ALRT-003",
            "severity": "CRITICAL",
            "reason": "CRITICAL_RESOURCE_POLICY"
        }),
        Action(name="get_siem_alert_details", kwargs={"alert_id": "ALRT-003"}),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-005",
            "action_type": "ALERT_FINALIZED",
            "target_id": "ALRT-003",
            "timestamp": "2024-06-10 15:45:00+00:00",
            "details": "resource=RES-020|final_severity=CRITICAL|handled_at=2024-06-10 15:45:00+00:00"
        }),
        Action(name="get_siem_alert", kwargs={"alert_id": "ALRT-003"})
    ],
    outputs=[
        '[{"alert_id":"ALRT-003","resource_id":"RES-020","final_severity":"CRITICAL"}]'
    ]
),



# - TASK 16 -
Task(
    annotator="0",
    user_id="016",
    instruction=(
        "You are Jessica Garcia (U-006), Finance. Evaluate access request AR-008 for Marisa Cole (U-030) "
        "requesting finance-budget-admin (ROL-032) on RES-032 under high‑criticality policy. "
        "High‑criticality approvals require: the requester is ACTIVE with MFA enabled, the role’s permissions align with the "
        "target resource, and change‑control with dual‑approver visibility is initiated via the Finance approvals channel. "
        "If any mandatory control fails, deny using a deterministic decision time anchored to the request’s submission. "
        "Provide the processed request and Marisa’s current roles."
    ),
    actions=[
        # Reviewer & request context
        Action("get_user_details", {"user_id":"U-006"}),
        Action("get_access_request", {"request_id":"AR-008"}),
        Action("get_user_details", {"user_id":"U-030"}),
        Action("get_resource_details", {"resource_id":"RES-032"}),
        Action("list_permissions_for_role", {"role_id":"ROL-032"}),

        # Governance signal (dual‑approver visibility) regardless of outcome
        Action("post_slack_message", {
            "channel": "#finance-approvals",
            "message": "AR-008 review started for U-030 requesting ROL-032 on RES-032 (high criticality). "
                       "Verifying MFA, scope alignment, and change-control. Reviewer: U-006."
        }),

        # Deterministic denial because MFA control is mandatory for high‑criticality and not satisfied in this scenario
        Action("reject_access_request", {
            "request_id":"AR-008",
            "reviewer_id":"U-006",
            "decision_at":"2024-05-20T15:00:00Z"
        }),
        Action("create_audit_log", {
            "actor_id":"U-006",
            "action_type":"ACCESS_REJECTED",
            "target_id":"AR-008",
            "timestamp":"2024-05-20T15:00:00Z",
            "details":"request=AR-008|resource=RES-032|role=ROL-032|decision=REJECTED|reason=MFA_REQUIRED_HIGH_CRITICALITY"
        }),
        Action("post_slack_message", {
            "channel": "#finance-approvals",
            "message": "AR-008 denied at 2024-05-20T15:00:00Z: MFA not enabled for U-030 (mandatory for high‑criticality). "
                       "Logged ACCESS_REJECTED in audit."
        }),

        # Return current roles after decision
        Action("get_user_roles", {"user_id":"U-030"}),
    ],
    outputs=[
        '[{"request_id":"AR-008","user_id":"U-030","resource_id":"RES-032","requested_role_id":"ROL-032",'
        '"status":"REJECTED","reviewed_by":"U-006","decision_at":"2024-05-20T15:00:00Z"}]',
        '[{"role_id":"ROL-029","role_name":"finance-base","description":"Basic access for finance staff","is_temporary":false}]'
    ]
),



# Task 017
Task(
    annotator="0",
    user_id="017",
    instruction=(
        "You are Kevin Harris (U-015). Apply our RBAC policy to commission reporting for Matthew Lopez (U-009) on lead-generation-db (RES-016). "
        "Act only where policy holds: Matthew is ACTIVE and using MFA; access stays least-privilege as sales-commission-view (ROL-015) scoped to that resource; "
        "and business approval is issued by Operations using the directory reviewer resolution (lowest user_id among ACTIVE+MFA Operations reviewers — for this request, U-023). "
        "Record the decision at 2025-08-12T23:00:00Z with the justification 'JUST:commission-view|RES:RES-016|BY:U-015|AT:2025-08-12T23:00:00Z', and set the authorization to end on 2025-12-31T00:00:00Z. "
        "When these conditions are satisfied, grant the role and return Matthew’s final roles."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-009"}),
        Action(name="get_user_details", kwargs={"user_id": "U-015"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-016"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-015"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-015"}),

        Action(name="list_users", kwargs={"department": "Operations", "status": "ACTIVE", "mfa_enabled": True}),
        Action(name="get_user_details", kwargs={"user_id": "U-023"}),

        Action(name="get_user_roles", kwargs={"user_id": "U-009"}),

        Action(name="create_access_request", kwargs={
            "user_id": "U-009",
            "resource_id": "RES-016",
            "role_id": "ROL-015",
            "justification": "JUST:commission-view|RES:RES-016|BY:U-015|AT:2025-08-12T23:00:00Z"
        }),
        Action(name="approve_access_request", kwargs={
            "request_id": "AR-042",
            "reviewer_id": "U-023",
            "decision_at": "2025-08-12T23:00:00Z"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-009",
            "role_id": "ROL-015",
            "assigned_by": "U-015",
            "assigned_on": "2025-08-12T23:00:00Z",
            "expires_on": "2025-12-31T00:00:00Z"
        }),

        Action(name="create_audit_log", kwargs={
            "actor_id": "U-015",
            "action_type": "ACCESS_CONTROL_CHECKS",
            "target_id": "U-009",
            "timestamp": "2025-08-12T23:00:00Z",
            "details": "anchor=2025-08-12T23:00:00Z|requester=U-009(status=ACTIVE,mfa=True)|role=ROL-015|permission=P-044(resource=RES-016)|sod_reviewer=U-023|expiry=2025-12-31T00:00:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-023",
            "action_type": "ACCESS_REQUEST_APPROVED",
            "target_id": "AR-042",
            "timestamp": "2025-08-12T23:00:00Z",
            "details": "request_id=AR-042|resource_id=RES-016|role_id=ROL-015|status=APPROVED|reviewer=U-023|anchor=2025-08-12T23:00:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-015",
            "action_type": "ACCESS_GRANTED",
            "target_id": "U-009",
            "timestamp": "2025-08-12T23:00:00Z",
            "details": "user=U-009|role=ROL-015|scope=RES-016|assigned_by=U-015|assigned_on=2025-08-12T23:00:00Z|expires_on=2025-12-31T00:00:00Z|anchor=2025-08-12T23:00:00Z"
        }),

        Action(name="get_user_roles", kwargs={"user_id": "U-009"})
    ],
    outputs=[
        '{"user_id": "U-009", "roles": ['
        '{"role_id": "ROL-011", "expires_on": null}, '
        '{"role_id": "ROL-012", "expires_on": null}, '
        '{"role_id": "ROL-013", "expires_on": null}, '
        '{"role_id": "ROL-015", "expires_on": "2025-12-31T00:00:00Z"}]}'
    ]
),


# - TASK 18 -
Task(
    annotator="0",
    user_id="018",
    instruction=(
        "You are Christopher Rodriguez (U-007), owner of RES-006 (internal-documentation-wiki). "
        "Find an engineering department user with a pending request who does not already hold the role engineering-db-schema (ROL-004). "
        "Brian Taylor (U-013), Engineering, has a pending request (AR-020) for engineering-db-schema (ROL-004) on RES-006. "
        "Approve if valid and assign with expiry 2025-12-31T00:00:00Z. Approval timestamp=2024-05-26T17:00:00Z; assignment timestamp=2024-05-26T17:10:00Z. "
        "Return Brian’s updated roles including assigned_by, assigned_on, and expires_on."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-007"}),
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-006"}),
        Action(name="get_user_details", kwargs={"user_id": "U-013"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-013"}),
        Action(name="approve_access_request", kwargs={
                "request_id": "AR-020",
                "reviewer_id": "U-007",
                "decision_at": "2024-05-26T17:00:00Z"
        }),
        Action(name="assign_role_to_user", kwargs={
                "user_id": "U-013",
                "role_id": "ROL-004",
                "assigned_by": "U-007",
                "assigned_on": "2024-05-26T17:10:00Z",
                "expires_on": "2025-12-31T00:00:00Z"
        }),
        Action(name="get_user_roles", kwargs={"user_id": "U-013"})
    ],
    outputs=[
        '[{"role_id": "ROL-001", "role_name": "engineering-base", "is_temporary": false, '
        '"assigned_by": "U-001", "assigned_on": "2023-09-01T16:00:00Z", "expires_on": null}, '
        '{"role_id": "ROL-004", "role_name": "engineering-db-schema", "is_temporary": false, '
        '"assigned_by": "U-007", "assigned_on": "2024-05-26T17:10:00Z", "expires_on": "2025-12-31T00:00:00Z"}]'
    ]
),



# - TASK 19 -
Task(
    annotator="0",
    user_id="019",
    instruction=(
        "You are Ashley Wilson (U-010), HR. "
        "Approve pending exception PE-016 for Heather Mitchell (U-028) until 2025-10-21T00:00:00Z, "
        "setting reviewed_on to 2025-08-07T14:30:00Z, following policy. "
        "Return the updated exception record."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-010"}),
        Action(name="get_user_details", kwargs={"user_id": "U-028"}),
        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-016"}),
        Action(name="approve_policy_exception", kwargs={
                "exception_id": "PE-016",
                "reviewed_by": "U-010",
                "expires_on": "2025-10-21T00:00:00Z",
                "reviewed_on": "2025-08-07T14:30:00Z"
            }),
        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-016"})
    ],
    outputs=[
        '{"exception_id": "PE-016", "user_id": "U-028", "permission_id": "P-056", '
        '"reviewed_by": "U-010", "requested_on": "2025-08-06T13:00:00Z", '
        '"reviewed_on": "2025-08-07T14:30:00Z", '
        '"expires_on": "2025-10-21T00:00:00Z", '
        '"reason": "One-time enrollment of a new employee in a non-standard benefits program.", "status": "ACTIVE"}'
    ]
),


# - TASK 20 -
Task(
    annotator="0",
    user_id="020",
    instruction=(
        "You are Jeffery Green (U-023), Operations. For production-web-server-1 (RES-025), review all pending access requests. "
        "Approve only if every permission in the requested role is scoped to RES-025 and the requester does not already hold the role; otherwise reject. "
        "Use the request's submitted_at as the decision time. "
        "Also record a deterministic audit log for each decision — actor U-023, action ACCESS_GRANTED or ACCESS_REJECTED, target is the request_id, "
        "timestamp is the decision time with tokenized details of request_id, user, resource, decision and decision maker."
        "Return all rejected access requests for RES-025, including previously rejected ones."
    ),
    actions=[
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-025"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-026"}),

        Action(name="reject_access_request", kwargs={
            "request_id": "AR-007",
            "reviewer_id": "U-023",
            "decision_at": "2024-05-20T14:00:00+00:00"
        }),

        Action(name="create_audit_log", kwargs={
            "actor_id": "U-023",
            "action_type": "ACCESS_REJECTED",
            "target_id": "AR-007",
            "timestamp": "2024-05-20T14:00:00+00:00",
            "details": "request_id=AR-007|user=U-029|role=ROL-026|resource=RES-025|decision=REJECTED|decided_by=U-023"
        }),

        Action(name="list_access_requests", kwargs={"status": "REJECTED", "resource_id": "RES-025"})
    ],
    outputs=[
        '[{"request_id":"AR-007","user_id":"U-029","resource_id":"RES-025","requested_role_id":"ROL-026",'
        '"justification":"Urgent request for full system admin access for incident response.","status":"REJECTED",'
        '"submitted_at":"2024-05-20T14:00:00+00:00","reviewed_by":"U-023","decision_at":"2024-05-20T14:00:00+00:00"},'
        '{"request_id":"AR-018","user_id":"U-006","resource_id":"RES-025","requested_role_id":"ROL-026",'
        '"justification":"Finance needs access for system audit.","status":"REJECTED",'
        '"submitted_at":"2024-05-25T16:30:00+00:00","reviewed_by":"U-005","decision_at":"2024-05-25T17:00:00+00:00"}]'
    ]
),


# - TASK 21 -
Task(
    annotator="0",
    user_id="021",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. For production-web-server-1 (RES-025), process all pending access "
        "requests in line with RBAC/SoD policy: approvals require an authorized Operations reviewer. If you are not "
        "authorized to approve, reject the request and record a concise compliance audit trail that ties the decision "
        "time to the request’s original submission timestamp. Return the processed request(s) and the affected user’s roles."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-001"}),
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-025"}),
        Action(name="get_user_details", kwargs={"user_id": "U-029"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="list_policy_exceptions", kwargs={"user_id": "U-029", "status": "ACTIVE"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-001"}),
        Action(name="reject_access_request", kwargs={
                "request_id": "AR-007",
                "reviewer_id": "U-001",
                "decision_at": "2024-05-20T14:00:00Z"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-001",
                "action_type": "ACCESS_REJECTED",
                "target_ref": {"kind": "ACCESS_REQUEST", "id": "AR-007"},
                "timestamp": "2024-05-20T14:00:00Z",
                "details": (
                    "request_id=AR-007|resource_id=RES-025|subject=U-029|reviewer=U-001|"
                    "submitted_at=2024-05-20T14:00:00Z|decision_at=2024-05-20T14:00:00Z|"
                    "policy=RBAC_SOD|reviewer_dept=Engineering|outcome=REJECTED"
                )
            }),
        Action(name="get_user_roles", kwargs={"user_id": "U-029"})
    ],
    outputs=[
        '[{"request_id": "AR-007", "user_id": "U-029", "resource_id": "RES-025", '
        '"requested_role_id": "ROL-026", "justification": "Urgent request for full system admin access for incident response.", '
        '"status": "REJECTED", "submitted_at": "2024-05-20T14:00:00Z", "reviewed_by": "U-001", "decision_at": "2024-05-20T14:00:00Z"}]',
        '[{"role_id": "ROL-021", "role_name": "operations-base", "description": "Basic access for operations staff", "is_temporary": false}]'
    ]
),


# - TASK 22 -
Task(
    annotator="0",
    user_id="022",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. Approve PE-018 for U-007 (permission P-005) with "
        "expires_on=2025-11-16T04:59:59Z and reviewed_on=2025-08-06T15:30:00Z. Create an immutable audit entry with "
        "details 'PE:PE-018|PERM:P-005|USER:U-007|STATUS:APPROVED|EXPIRES:2025-11-16T04:59:59Z|BY:U-001|AT:2025-08-06T15:30:00Z', "
        "and notify U-007 by email at T0=2025-08-06T15:30:00Z. Return the updated exception (using the tool’s actual "
        "status field), the audit details, and the email subject."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-001"}),
        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-018"}),
        Action(name="get_user_details", kwargs={"user_id": "U-007"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-005"}),
        Action(name="approve_policy_exception", kwargs={
            "exception_id": "PE-018",
            "reviewed_by": "U-001",
            "expires_on": "2025-11-16T04:59:59Z",
            "reviewed_on": "2025-08-06T15:30:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-001",
            "action_type": "POLICY_EXCEPTION_APPROVED",
            "target_id": "PE-018",
            "timestamp": "2025-08-06T15:30:00Z",
            "details": "PE:PE-018|PERM:P-005|USER:U-007|STATUS:APPROVED|EXPIRES:2025-11-16T04:59:59Z|BY:U-001|AT:2025-08-06T15:30:00Z"
        }),
        Action(name="send_email", kwargs={
            "sender": "U-001",
            "receiver": "U-007",
            "subject": "NOTICE|PE:PE-018|STATUS:APPROVED|EXPIRES:2025-11-16T04:59:59Z",
            "body": "PE:PE-018|PERM:P-005|USER:U-007|STATUS:APPROVED|EXPIRES:2025-11-16T04:59:59Z|BY:U-001|AT:2025-08-06T15:30:00Z",
            "timestamp": "2025-08-06T15:30:00Z"
        }),
        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-018"})
    ],
    outputs=[
        '[{"exception_id":"PE-018","user_id":"U-007","permission_id":"P-005","reviewed_by":"U-001","reviewed_on":"2025-08-06T15:30:00Z","expires_on":"2025-11-16T04:59:59Z","status":"ACTIVE"}]',
        '[{"audit_details":"PE:PE-018|PERM:P-005|USER:U-007|STATUS:APPROVED|EXPIRES:2025-11-16T04:59:59Z|BY:U-001|AT:2025-08-06T15:30:00Z"}]',
        '[{"email_subject":"NOTICE|PE:PE-018|STATUS:APPROVED|EXPIRES:2025-11-16T04:59:59Z"}]'
    ]
),


# - TASK 23 -
Task(
    annotator="0",
    user_id="023",
    instruction=(
        "You are Jessica Garcia (U-006) in Finance. For general-ledger-db (RES-031), request a policy exception so that "
        "Lisa Anderson (U-012) can use permission P-078 (approve-invoice) under SOX scope. Use deterministic timing drawn from the request "
        "metadata for subsequent review anchoring. Per reviewer-independence policy, an ACTIVE Finance reviewer other than you must approve. "
        "Export audit logs for RES-031 covering 2025-08-05T00:00:00Z–2025-08-07T23:59:59Z. "
        "Return the approved exception record and the audit-log export result."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-006"}),
        Action(name="get_user_details", kwargs={"user_id": "U-012"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-031"}),
        Action(name="request_policy_exception", kwargs={
            "user_id": "U-012",
            "permission_id": "P-078",
            "reason": "scope=SOX|permission=P-078|resource=RES-031|requester=U-006|subject=U-012",
            "requested_on": "2025-08-11T10:00:00Z"
        }),
        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-021"}),
        Action(name="get_user_details", kwargs={"user_id": "U-018"}),
        Action(name="approve_policy_exception", kwargs={
            "exception_id": "PE-021",
            "reviewed_by": "U-018",
            "reviewed_on": "2025-08-11T10:00:00Z",
            "expires_on": "2025-09-06T04:59:59Z"
        }),
        Action(name="export_audit_logs", kwargs={
            "target_id": "RES-031",
            "start_time": "2025-08-05T00:00:00Z",
            "end_time": "2025-08-07T23:59:59Z"
        }),
        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-021"})
    ],
    outputs=[
        '{"exception_id":"PE-021","user_id":"U-012","permission_id":"P-078","reviewed_by":"U-018","requested_on":"2025-08-11T10:00:00Z","reviewed_on":"2025-08-11T10:00:00Z","expires_on":"2025-09-06T04:59:59Z","reason":"scope=SOX|permission=P-078|resource=RES-031|requester=U-006|subject=U-012","status":"ACTIVE"}',
        '[]'
    ]
),


# - TASK 24 -
Task(
    annotator="0",
    user_id="024",
    instruction=(
        "You are Michael Davis (U-005), Operations. Apply Operations policy controls rather than stepwise procedures: "
        "use the canonical completion instant for certification C-020 (2025-08-02T14:00:00Z); approve policy exception PE-012 with its mandated validity window "
        "(record the review at 2025-08-12T23:00:00Z and set expiry to 2025-09-21T04:59:59Z); enforce session hygiene by validating the activity state of S-024 "
        "from canonical session records and only terminate if it is active; and constrain reporting to currently ACTIVE policy exceptions held by Operations "
        "department users. Return results as a single stringified object containing {\"open_exceptions_for_operations\": [...]} and a consolidated "
        "completion object for C-020."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="get_user_details", kwargs={"user_id": "U-023"}),

        Action(name="get_certification_details", kwargs={"certification_id": "C-020"}),
        Action(
            name="complete_certification",
            kwargs={
                "certification_id": "C-020",
                "completed_on": "2025-08-02T14:00:00Z"
            }
        ),

        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-012"}),
        Action(
            name="approve_policy_exception",
            kwargs={
                "exception_id": "PE-012",
                "reviewed_by": "U-005",
                "reviewed_on": "2025-08-12T23:00:00Z",
                "expires_on": "2025-09-21T04:59:59Z"
            }
        ),

        Action(name="list_user_sessions", kwargs={"user_id": "U-023", "active_only": True}),
        Action(name="list_sessions", kwargs={"user_id": "U-023", "active_only": False}),
        Action(name="list_users", kwargs={"department": "Operations", "status": "ACTIVE"}),
        Action(name="list_policy_exceptions", kwargs={"status": "ACTIVE", "user_id": "U-005"}),
        Action(name="list_policy_exceptions", kwargs={"status": "ACTIVE", "user_id": "U-023"}),
        Action(name="list_policy_exceptions", kwargs={"status": "ACTIVE", "user_id": "U-029"}),
        Action(name="list_policy_exceptions", kwargs={"status": "ACTIVE", "user_id": "U-031"}),
        Action(name="list_policy_exceptions", kwargs={"status": "ACTIVE", "user_id": "U-033"})
    ],
    outputs=[
        '{"open_exceptions_for_operations":[{"exception_id":"PE-012","status":"ACTIVE","user_id":"U-023"}],"certification_C-020":{"status":"COMPLETED","completed_on":"2025-08-02T14:00:00Z"}}'
    ]
),



# - TASK 25 -
Task(
    annotator="0",
    user_id="025",
    instruction=(
        "You are Jessica Garcia (U-006). Apply the Finance SoD policy to grant a policy exception for HubSpot read "
        "(permission P-095) on RES-037 to Paul Ellis (U-021). The approver must be an ACTIVE Finance user independent of "
        "both the facilitator and the subject; by policy, when multiple reviewers qualify, the canonical reviewer is the "
        "lexicographically smallest eligible user_id. Use deterministic anchors: reason='Review all open HubSpot tickets for audit', "
        "requested_on='2025-08-10T10:10:00Z', reviewed_on=requested_on, and expires_on='2025-09-30T23:59:59Z'. "
        "Capture an SoD enforcement audit reflecting the selection. Return the approved exception record."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-006"}),
        Action(name="get_user_details", kwargs={"user_id": "U-021"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-095"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-037"}),
        Action(name="request_policy_exception", kwargs={
            "user_id": "U-021",
            "permission_id": "P-095",
            "reason": "Review all open HubSpot tickets for audit",
            "requested_on": "2025-08-10T10:10:00Z"
        }),
        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-021"}),
        Action(name="list_users", kwargs={"department": "Finance", "status": "ACTIVE"}),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-006",
            "action_type": "SOD_ENFORCED",
            "target_id": "PE-021",
            "timestamp": "2025-08-10T10:10:00Z",
            "details": "rule=FINANCE_ACTIVE_AND_INDEPENDENT|min_user_id_tiebreaker=true|facilitator=U-006|subject=U-021|reviewer=U-012"
        }),
        Action(name="get_user_details", kwargs={"user_id": "U-012"}),
        Action(name="approve_policy_exception", kwargs={
            "exception_id": "PE-021",
            "reviewed_by": "U-012",
            "reviewed_on": "2025-08-10T10:10:00Z",
            "expires_on": "2025-09-30T23:59:59Z"
        }),
        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-021"})
    ],
    outputs=[
        '{"exception_id":"PE-021","user_id":"U-021","permission_id":"P-095","reviewed_by":"U-012","requested_on":"2025-08-10T10:10:00Z","reviewed_on":"2025-08-10T10:10:00Z","expires_on":"2025-09-30T23:59:59Z","reason":"Review all open HubSpot tickets for audit","status":"ACTIVE"}'
    ]
),

# - TASK 26 -
Task(
    annotator="0",
    user_id="026",
    instruction=(
        "You are Jessica Garcia (U-006), Finance. Assign finance-lead (ROL-039) to ACTIVE Finance users who lack it. "
        "Use the canonical anchor timestamp from policy exception PE-007.reviewed_on (2024-10-29 20:00:00+00:00) for any "
        "assigned_on fields. If you have a PENDING_REVIEW exception for P-076, approve and immediately expire it; otherwise skip. "
        "Return Finance users who now hold ROL-039 and your EXPIRED P-076 exceptions."
    ),
    actions=[
        Action(name="list_users", kwargs={"department": "Finance", "status": "ACTIVE"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-012"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-024"}),
        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-007"}),
        Action(
            name="assign_role_to_user",
            kwargs={
                "user_id": "U-012",
                "role_id": "ROL-039",
                "assigned_by": "U-006",
                "assigned_on": "2024-10-29 20:00:00+00:00"
            }
        ),
        Action(
            name="assign_role_to_user",
            kwargs={
                "user_id": "U-018",
                "role_id": "ROL-039",
                "assigned_by": "U-006",
                "assigned_on": "2024-10-29 20:00:00+00:00"
            }
        ),
        Action(
            name="assign_role_to_user",
            kwargs={
                "user_id": "U-024",
                "role_id": "ROL-039",
                "assigned_by": "U-006",
                "assigned_on": "2024-10-29 20:00:00+00:00"
            }
        ),
        Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-012"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-024"}),
        Action(name="list_policy_exceptions", kwargs={
                "user_id": "U-006",
                "permission_id": "P-076",
                "status": "EXPIRED"
            })
    ],
    outputs=[
        '[{"user_id":"U-006","role_id":"ROL-039"},'
        '{"user_id":"U-012","role_id":"ROL-039"},'
        '{"user_id":"U-018","role_id":"ROL-039"},'
        '{"user_id":"U-024","role_id":"ROL-039"}]',
        '[{"exception_id":"PE-007","status":"EXPIRED"}]'
    ]
),



# - TASK 27 -
Task(
    annotator="0",
    user_id="027",
    instruction=(
        "You are Jessica Garcia (U-006) in Finance. As of the Q3 audit cutoff (2024-06-16T17:00:00Z), ensure each "
        "ACTIVE Finance team member with MFA enabled is entitled with finance-invoice-processor (ROL-031) on RES-031. "
        "Where missing, regularize access per policy, attributing the assignment to Lisa Anderson (U-012) and using the "
        "cutoff as both assigned_on and expires_on to respect the audit freeze. For each eligible user, determine whether "
        "their access confers permission P-085 (view-financial-report); if not, list any ACTIVE policy exceptions for P-085. "
        "Also verify completion of certifications C-006 (RES-031) and C-012 (RES-034). Return, per eligible user: "
        "whether they hold ROL-031, whether they have P-085, any P-085 exceptions, and the completed certifications."
    ),
    actions=[
        Action(name="list_users", kwargs={"department": "Finance", "status": "ACTIVE", "mfa_enabled": True}),
        Action(name="get_user_roles", kwargs={"user_id": "U-006"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-012"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-018"}),

        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-006",
            "role_id": "ROL-031",
            "assigned_by": "U-012",
            "assigned_on": "2024-06-16T17:00:00Z",
            "expires_on": "2024-06-16T17:00:00Z"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-018",
            "role_id": "ROL-031",
            "assigned_by": "U-012",
            "assigned_on": "2024-06-16T17:00:00Z",
            "expires_on": "2024-06-16T17:00:00Z"
        }),

        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-029"}),  # finance-base
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-031"}),  # finance-invoice-processor
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-032"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-033"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-039"}),

        Action(name="list_policy_exceptions", kwargs={"status": "ACTIVE", "user_id": "U-006"}),
        Action(name="list_policy_exceptions", kwargs={"status": "ACTIVE", "user_id": "U-012"}),
        Action(name="list_policy_exceptions", kwargs={"status": "ACTIVE", "user_id": "U-018"}),

        Action(name="get_certification_details", kwargs={"certification_id": "C-006"}),
        Action(name="get_certification_details", kwargs={"certification_id": "C-012"}),
    ],
    outputs=[
        '['
        '{"user_id":"U-006","has_rol_031":true,"has_p_085":false,"policy_exceptions_p085":[],"completed_certifications":["C-006","C-012"]},'
        '{"user_id":"U-012","has_rol_031":true,"has_p_085":false,"policy_exceptions_p085":[],"completed_certifications":["C-006","C-012"]},'
        '{"user_id":"U-018","has_rol_031":true,"has_p_085":true,"policy_exceptions_p085":[],"completed_certifications":["C-006","C-012"]}'
        ']'
    ]
),


# - TASK 28 -
Task(
    annotator="0",
    user_id="028",
    instruction=(
        "You are Michael Davis (U-005), Operations. For HIGH-severity SIEM alerts on production-web-server-1 (RES-025), "
        "apply Operations policy: record an investigation audit for each alert at its created_at, verify certification "
        "C-003 (backup-server, RES-026) is COMPLETED, and terminate ACTIVE sessions for the alert’s referenced users if any exist. "
        "Return the certification_id and any terminated session_ids."
    ),
    actions=[
        Action("list_siem_alerts", {"resource_id":"RES-025","severity":"HIGH"}),

        Action("investigate_siem_incident", {
            "alert_id":"ALRT-005",
            "analyst_id":"U-005",
            "notes":"alert_id=ALRT-005|resource_id=RES-025|severity=HIGH|investigated_on=2024-08-28T13:30:00Z",
            "investigated_on":"2024-08-28T13:30:00Z"
        }),
        Action("create_audit_log", {
            "actor_id":"U-005",
            "action_type":"INVESTIGATION_RECORDED",
            "target_id":"ALRT-005",
            "timestamp":"2024-08-28T13:30:00Z",
            "details":"alert_id=ALRT-005|resource_id=RES-025|severity=HIGH|investigated_on=2024-08-28T13:30:00Z"
        }),

        Action("get_certification_details", {"certification_id":"C-003"}),
        Action("create_audit_log", {
            "actor_id":"U-005",
            "action_type":"CERT_DEPENDENCY_VERIFIED",
            "target_id":"C-003",
            "timestamp":"2024-08-28T13:30:00Z",
            "details":"certification_id=C-003|resource_id=RES-026|status=COMPLETED"
        }),

        Action("list_sessions", {"user_id":"U-002","active_only":True})
    ],
    outputs=['["C-003", []]']
),


# - TASK 29 -
Task(
    annotator="0",
    user_id="029",
    instruction=(
        "You are Michael Davis (U-005), Operations. Apply Operations policies on backup-storage-server (RES-028) "
        "and network-firewall-main (RES-027). For RES-028, create SIEM rule 'RES-028-backup-deletion-track' to detect "
        "backup deletion activity. For RES-027, enforce least-privilege policy: ensure Robert White (U-017) holds "
        "operations-network-admin (ROL-028). If missing, assign it with explicit expiry 2025-12-31T00:00:00Z, "
        "deterministically attributed to you with the assignment timestamp taken from his most recent session start. "
        "Do not alter unrelated roles. Return Robert’s updated role list."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="create_siem_rule", kwargs={
            "rule_name": "RES-028-backup-deletion-track",
            "conditions": {"action": "delete-backup", "resource_id": "RES-028"},
            "created_by": "U-005"
        }),
        Action(name="get_user_details", kwargs={"user_id": "U-017"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-017"}),
        Action(name="list_sessions", kwargs={"user_id": "U-017"}),
        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-017",
            "role_id": "ROL-028",
            "assigned_by": "U-005",
            "assigned_on": "2025-08-06 14:00:00+00:00",
            "expires_on": "2025-12-31T00:00:00Z"
        }),
        Action(name="get_user_roles", kwargs={"user_id": "U-017"})
    ],
    outputs=[
        '[{"role_id": "ROL-021", "role_name": "operations-base", "description": "Basic access for operations staff", "is_temporary": false},'
        '{"role_id": "ROL-022", "role_name": "operations-server-monitor", "description": "Monitors server health and performance", "is_temporary": false},'
        '{"role_id": "ROL-024", "role_name": "operations-log-viewer", "description": "Views system and application logs", "is_temporary": false},'
        '{"role_id": "ROL-028", "role_name": "operations-network-admin", "description": "Administrative access to all operations network infrastructure.", "is_temporary": true}]'
    ]
),




# - TASK 30 -
Task(
    annotator="0",
    user_id="030",
    instruction=(
        "You are Jessica Garcia (U-006), Finance. Apply Finance RBAC to provision finance-lead (ROL-039) only for Finance users "
        "who are ACTIVE, already have finance-base (ROL-029), and do not already have ROL-039. Finance policy defines the anchor "
        "timestamp for any such provisioning as the decision_at of the user’s most recent non-PENDING access request (latest with "
        "status APPROVED or REJECTED). Exclude yourself (U-006) from consideration. Record a single segregation-of-duties attestation "
        "at TI-040 at the time of the latest assignment and open a summary ticket with deterministic subject 'FIN|ROL-039|BULK-GRANT|2024-05-28'. "
        "Return the Finance users who newly hold ROL-039 together with the summary ticket subject."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-006"}),

        Action(name="list_users", kwargs={"department": "Finance", "status": "ACTIVE"}),

        Action(name="get_user_roles", kwargs={"user_id": "U-012"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-024"}),

        Action(name="list_access_requests", kwargs={"status": "APPROVED"}),
        Action(name="list_access_requests", kwargs={"status": "REJECTED"}),

        Action(name="get_access_request", kwargs={"request_id": "AR-012"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-003"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-026"}),

        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-012",
            "role_id": "ROL-039",
            "assigned_by": "U-006",
            "assigned_on": "2024-05-22 18:45:00+00:00"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-018",
            "role_id": "ROL-039",
            "assigned_by": "U-006",
            "assigned_on": "2024-05-16 17:00:00+00:00"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-024",
            "role_id": "ROL-039",
            "assigned_by": "U-006",
            "assigned_on": "2024-05-28 16:00:00+00:00"
        }),

        Action(name="create_audit_log", kwargs={
            "actor_id": "U-006",
            "action_type": "SOD_ATTESTATION",
            "target_id": "TI-040",
            "timestamp": "2024-05-28 16:00:00+00:00",
            "details": "subjects=[U-012,U-018,U-024]|role=ROL-039|anchors=[AR-012,AR-003,AR-026]|attestation=completed"
        }),

        Action(name="create_hubspot_ticket", kwargs={
            "subject": "FIN|ROL-039|BULK-GRANT|2024-05-28",
            "description": "FIN|ROL-039|BULK-GRANT|2024-05-28",
            "requester_id": "U-006",
            "assignee_id": "U-006",
            "category": "ACCESS_REQUEST"
        }),

        Action(name="get_user_roles", kwargs={"user_id": "U-012"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-024"})
    ],
    outputs=[
        '[{"user_id":"U-012","role_id":"ROL-039"},'
        '{"user_id":"U-018","role_id":"ROL-039"},'
        '{"user_id":"U-024","role_id":"ROL-039"},'
        '{"ticket_subject":"FIN|ROL-039|BULK-GRANT|2024-05-28"}]'
    ]
),


# - TASK 31 -
Task(
    annotator="0",
    user_id="031",
    instruction=(
        "You are Sarah Thompson (U-022), Human Resources. Apply standard HR access policy to obtain the HR lead role (ROL-037) on RES-041 "
        "for yourself with policy-required approval and canonical timestamps. Anchor both decision and assignment to "
        "2025-08-12T23:10:00Z and set expiry at 2025-12-31T00:00:00Z per policy. The reviewer must be deterministically "
        "chosen as the ACTIVE Human Resources user with the lowest user_id (Ashley Wilson, U-010). Use only dataset-derived tokens "
        "and return your resulting role IDs."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-022"}),
        Action(name="list_users", kwargs={"department": "Human Resources", "status": "ACTIVE"}),
        Action(name="get_user_details", kwargs={"user_id": "U-010"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-041"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-022"}),
        Action(name="create_access_request", kwargs={
            "user_id": "U-022",
            "resource_id": "RES-041",
            "role_id": "ROL-037",
            "justification": "HR_REQUIRED_APPROVAL_FOR_ROL-037_ON_RES-041"
        }),
        Action(name="list_access_requests", kwargs={
            "status": "PENDING",
            "resource_id": "RES-041"
        }),
        Action(name="approve_access_request", kwargs={
            "request_id": "AR-042",
            "reviewer_id": "U-010",
            "decision_at": "2025-08-12T23:10:00Z"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-022",
            "role_id": "ROL-037",
            "assigned_by": "U-010",
            "assigned_on": "2025-08-12T23:10:00Z",
            "expires_on": "2025-12-31T00:00:00Z"
        }),
        Action(name="get_user_roles", kwargs={"user_id": "U-022"})
    ],
    outputs=[
        '[{"user_id":"U-022","roles":["ROL-016","ROL-037"]}]'
    ]
),


# - TASK 32 -
Task(
    annotator="0",
    user_id="032",
    instruction=(
        "You are Jessica Garcia (U-006), Finance and owner of RES-034. For RES-034, AR-034 is to be recorded as REJECTED at "
        "2024-05-30 15:05:00+00:00 under intake criteria. Produce one denial audit (request_id, resource_id, role_id, decision=REJECTED, decision_at) "
        "and provide the REJECTED requests for RES-034."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-006"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-034"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-034"}),  # consistent request/resource
        Action(name="get_user_details", kwargs={"user_id": "U-018"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-030"}),
        Action(name="reject_access_request", kwargs={
            "request_id": "AR-034",
            "reviewer_id": "U-006",
            "decision_at": "2024-05-30 15:05:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-006",
            "action_type": "ACCESS_REJECTED",
            "target_id": "AR-034",
            "timestamp": "2024-05-30 15:05:00+00:00",
            "details": "resource=RES-034|role=ROL-030|decision=REJECTED|decision_at=2024-05-30 15:05:00+00:00"
        }),
        Action(name="list_access_requests", kwargs={"status": "REJECTED", "resource_id": "RES-034"})
    ],
    outputs=[
        '[{"request_id":"AR-034","user_id":"U-018","resource_id":"RES-034","requested_role_id":"ROL-030","status":"REJECTED","decision_at":"2024-05-30 15:05:00+00:00","reviewed_by":"U-006"}]'
    ]
),

# - TASK 33 -
Task(
    annotator="0",
    user_id="033",
    instruction=(
        "You are Paul Ellis (U-021), Sales, and owner of lead-generation-db (RES-016). Review the pending access request AR-022 for ROL-013 (sales-lead-manager) by Matthew Lopez (U-009). If Matthew already holds ROL-013, reject the request; only approve if he does not. Return Matthew's roles and the final access request record."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-021"}),
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-016"}),
        Action(name="get_user_details", kwargs={"user_id": "U-009"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-009"}),
        Action(name="reject_access_request", kwargs={
            "request_id": "AR-022",
            "reviewer_id": "U-021",
            "decision_at": "2024-05-26T16:00:00Z"
        }),
        Action(name="get_user_roles", kwargs={"user_id": "U-009"}),
        Action(name="list_access_requests", kwargs={"status": "REJECTED", "resource_id": "RES-016"}),
    ],
    outputs=[
        '[{"role_id": "ROL-011", "role_name": "sales-base", "description": "Basic access for sales staff", "is_temporary": false}'
        ',{"role_id": "ROL-012", "role_name": "sales-crm-access", "description": "Access to CRM system for customer data", "is_temporary": false}'
        ',{"role_id": "ROL-013", "role_name": "sales-lead-manager", "description": "Manages sales leads and opportunities", "is_temporary": false}]',
        '[{"request_id": "AR-022", "user_id": "U-009", "resource_id": "RES-016",'
        ' "requested_role_id": "ROL-013", "justification": "Need lead manager access for new marketing campaign leads.",'
        ' "status": "REJECTED", "submitted_at": "2024-05-26T16:00:00Z", "reviewed_by": "U-021",'
        ' "decision_at": "2024-05-26T16:00:00Z"}]'
    ]
),


# - TASK 34 -
Task(
    annotator="0",
    user_id="034",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. Approve policy exception PE-018 for U-007 to use permission P-005. "
        "Use T0=2025-08-06T15:30:00Z and record a canonical audit entry."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-001"}),
        Action(name="get_policy_exception_details", kwargs={"exception_id":"PE-018"}),
        Action(name="get_user_details", kwargs={"user_id":"U-007"}),
        Action(name="get_permission_details", kwargs={"permission_id":"P-005"}),
        Action(name="approve_policy_exception", kwargs={
            "exception_id":"PE-018",
            "reviewed_by":"U-001",
            "reviewed_on":"2025-08-06T15:30:00Z",
            "expires_on":"2025-11-16T04:59:59Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-001",
            "action_type":"POLICY_EXCEPTION_APPROVED",
            "target_id":"PE-018",
            "timestamp":"2025-08-06T15:30:00Z",
            "details":"PE:PE-018|PERM:P-005|USER:U-007|STATUS:APPROVED|EXPIRES:2025-11-16T04:59:59Z|BY:U-001|AT:2025-08-06T15:30:00Z"
        })
    ],
    outputs=[
        '[{"exception_id":"PE-018","final_status":"APPROVED","expires_on":"2025-11-16T04:59:59Z","reviewed_on":"2025-08-06T15:30:00Z"}]'
    ]
),


# - TASK 35 -
Task(
    annotator="0",
    user_id="035",
    instruction=(
        "You are Jessica Garcia (U-006). Apply the exception policy for HubSpot read (P-095) on RES-037 for Paul Ellis (U-021) "
        "with separation of duties: the reviewer must be ACTIVE Finance and neither the requester nor the facilitator. "
        "In this dataset, the compliant reviewer is Lisa Anderson (U-012). "
        "Use anchors reason='Review all open HubSpot tickets for audit', requested_on='2025-08-10T10:10:00Z', reviewed_on='2025-08-10T10:10:00Z', "
        "expires_on='2025-09-30T23:59:59Z'. Capture a SoD audit and return the approved record."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-006"}),
        Action(name="get_user_details", kwargs={"user_id": "U-021"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-095"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-037"}),
        Action(name="request_policy_exception", kwargs={
            "user_id": "U-021",
            "permission_id": "P-095",
            "reason": "Review all open HubSpot tickets for audit",
            "requested_on": "2025-08-10T10:10:00Z"
        }),
        Action(name="get_user_details", kwargs={"user_id": "U-012"}),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-006",
            "action_type": "SOD_ENFORCED",
            "target_id": "PE-021",
            "timestamp": "2025-08-10T10:10:00Z",
            "details": "requester=U-021|facilitator=U-006|reviewer=U-012|rule=reviewer_must_not_equal_requester_or_facilitator"
        }),
        Action(name="approve_policy_exception", kwargs={
            "exception_id": "PE-021",
            "reviewed_by": "U-012",
            "reviewed_on": "2025-08-10T10:10:00Z",
            "expires_on": "2025-09-30T23:59:59Z"
        }),
        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-021"})
    ],
    outputs=[
        '{"exception_id":"PE-021","user_id":"U-021","permission_id":"P-095",'
        '"reviewed_by":"U-012","requested_on":"2025-08-10T10:10:00Z","reviewed_on":"2025-08-10T10:10:00Z",'
        '"expires_on":"2025-09-30T23:59:59Z","reason":"Review all open HubSpot tickets for audit","status":"ACTIVE"}'
    ]
),



# - TASK 36 -
Task(
    annotator="0",
    user_id="036",
    instruction=(
        "You are Michael Davis (U-005), Operations and the owner of production-web-server-1 (RES-025). "
        "Adjudicate all pending access to this resource under company RBAC and critical-asset policy. "
        "Decisions must be deterministic (set decision_at to the request’s submitted_at). "
        "Approve only if you are eligible to review and the requested role’s permissions match the target resource; otherwise reject. "
        "Record the decision in the audit log and return the processed request."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-025"}),
        Action(name="get_user_details", kwargs={"user_id": "U-029"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
        Action(name="list_policy_exceptions", kwargs={"user_id": "U-029", "status": "ACTIVE"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-026"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-026"}),
        Action(name="reject_access_request", kwargs={
                "request_id": "AR-007",
                "reviewer_id": "U-005",
                "decision_at": "2024-05-20T14:00:00Z"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-005",
                "action_type": "ACCESS_REJECTED",
                "target_ref": {"kind":"ACCESS_REQUEST","id":"AR-007"},
                "timestamp": "2024-05-20T14:00:00Z",
                "details": "ACCESS_REJECTED:AR-007:RES-025:U-005:2024-05-20T14:00:00Z:ROLE_SCOPE_MISMATCH:ROL-026->RES-024"
            })
    ],
    outputs=[
        '[{"request_id":"AR-007","user_id":"U-029","resource_id":"RES-025","requested_role_id":"ROL-026","justification":"Urgent request for full system admin access for incident response.","status":"REJECTED","submitted_at":"2024-05-20T14:00:00Z","reviewed_by":"U-005","decision_at":"2024-05-20T14:00:00Z"}]'
    ]
),


# - TASK 37 -
Task(
    annotator="0",
    user_id="037",
    instruction=(
        "You are Jessica Garcia (U-006), Finance and the owner of RES-034. You must adjudicate access to RES-034 under RBAC "
        "and segregation‑of‑duties policy. Use canonical dataset facts only. When multiple PENDING requests exist for RES-034, "
        "you must select exactly one request deterministically: choose the request with the earliest submitted_at; if there is a tie, "
        "choose the lexicographically smallest request_id. Your decision time is the request’s submitted_at. You must deny any request "
        "that would duplicate an existing entitlement for the same user, role, and resource at the decision time; otherwise you must approve. "
        "An approval is effective at the decision time and results in a corresponding role assignment. You must ensure a single auditable "
        "record of the adjudication exists in the standard RBAC audit schema capturing requester, resource, role, decision, and decision_at. "
        "Return the record of the processed request."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-006"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-034"}),

        Action(name="list_access_requests", kwargs={"status":"PENDING","resource_id":"RES-034"}),

        Action(name="get_user_details", kwargs={"user_id":"U-018"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-018"}),

        Action(name="approve_access_request", kwargs={
            "request_id":"AR-034",
            "reviewer_id":"U-006",
            "decision_at":"2024-05-30 15:00:00+00:00"
        }),

        Action(name="assign_role_to_user", kwargs={
            "user_id":"U-018",
            "role_id":"ROL-030",
            "assigned_by":"U-006",
            "assigned_on":"2024-05-30 15:00:00+00:00"
        }),

        Action(name="create_audit_log", kwargs={
            "actor_id":"U-006",
            "action_type":"ACCESS_GRANTED",
            "target_id":"AR-034",
            "timestamp":"2024-05-30 15:00:00+00:00",
            "details":"requester=U-018|resource=RES-034|role=ROL-030|decision=APPROVED|decision_at=2024-05-30 15:00:00+00:00"
        })
    ],
    outputs=[
        '[{"request_id":"AR-034","user_id":"U-018","resource_id":"RES-034","requested_role_id":"ROL-030","status":"APPROVED","submitted_at":"2024-05-30 15:00:00+00:00","reviewed_by":"U-006","decision_at":"2024-05-30 15:00:00+00:00"}]'
    ]
),


# - TASK 38 -
Task(
    annotator="0",
    user_id="038",
    instruction=(
        "You are Riley Gupta (U-021), CRM owner for RES-016. Decide access request AR-022 deterministically with decision_at equal to its submitted_at. "
        "Approve if and only if (a) you are ACTIVE and the recorded owner of RES-016; "
        "(b) the requester U-009 does not already hold role ROL-013; and "
        "(c) every permission attached to ROL-013 has resource_id == RES-016. "
        "Otherwise, reject. Record the decision in the audit log and return the processed request."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-021"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-016"}),
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-016"}),
        Action(name="get_user_details", kwargs={"user_id": "U-009"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-009"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-013"}),
        Action(name="reject_access_request", kwargs={
            "request_id": "AR-022",
            "reviewer_id": "U-021",
            "decision_at": "2024-05-26T16:00:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-021",
            "action_type": "ACCESS_REJECTED",
            "target_id": "AR-022",
            "timestamp": "2024-05-26T16:00:00Z",
            "details": "request=AR-022|resource=RES-016|role=ROL-013|requester=U-009|reviewer=U-021|decision=REJECTED|decision_at=2024-05-26T16:00:00Z|owner_check=true|requester_has_role=true|role_scope=RES-015"
        })
    ],
    outputs=[
        '[{"request_id":"AR-022","user_id":"U-009","resource_id":"RES-016","requested_role_id":"ROL-013","justification":"Need lead manager access for new marketing campaign leads.","status":"REJECTED","submitted_at":"2024-05-26T16:00:00Z","reviewed_by":"U-021","decision_at":"2024-05-26T16:00:00Z"}]'
    ]
),


Task(
    annotator="0",
    user_id="039",
    instruction=(
        "You are Michael Davis (U-005), Operations. At T0=2024-06-10 15:45:00+00:00, you must enforce that SIEM alert ALRT-003 "
        "on RES-020 is finalized with severity=CRITICAL in line with policy. You must: (1) escalate the alert to CRITICAL, "
        "(2) record an incident evidence entry anchored to T0 with details exactly "
        "'alert_id=ALRT-003|resource_id=RES-020|final_severity=CRITICAL|handled_at=2024-06-10 15:45:00+00:00', and "
        "(3) record a finalization audit log at T0 with the same details. Return the resulting severity snapshot."
    ),
    actions=[
        Action(name="get_siem_alert_details", kwargs={"alert_id": "ALRT-003"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-020"}),

        Action(name="escalate_siem_alert", kwargs={
            "alert_id": "ALRT-003",
            "severity": "CRITICAL"
        }),

        Action(name="create_incident_record", kwargs={
            "timestamp": "2024-06-10 15:45:00+00:00",
            "created_by": "U-005",
            "summary": "alert_id=ALRT-003|resource_id=RES-020|final_severity=CRITICAL|handled_at=2024-06-10 15:45:00+00:00",
            "linked_alerts": ["ALRT-003"],
            "linked_resources": ["RES-020"]
        }),

        Action(name="create_audit_log", kwargs={
            "actor_id": "U-005",
            "action_type": "ALERT_FINALIZED",
            "target_id": "ALRT-003",
            "timestamp": "2024-06-10 15:45:00+00:00",
            "details": "alert_id=ALRT-003|resource_id=RES-020|final_severity=CRITICAL|handled_at=2024-06-10 15:45:00+00:00"
        }),

        Action(name="get_siem_alert", kwargs={"alert_id": "ALRT-003"})
    ],
    outputs=[
        '[{"alert_id":"ALRT-003","resource_id":"RES-020","final_severity":"CRITICAL"}]'
    ]
),


# - TASK 40 -
Task(
    annotator="0",
    user_id="040",
    instruction=(
        "You are Jessica Garcia (U-006), Finance and owner of RES-034. Apply Finance access controls: decide AR-034 using its "
        "submitted_at (2024-05-30 15:00:00+00:00) as the decision instant, ensure the grant is realized at that instant without duplication, "
        "and maintain traceability with an evidence log. Return the set of APPROVED requests for RES-034."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-006"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-034"}),
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-034"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-034"}),
        Action(name="get_user_details", kwargs={"user_id": "U-018"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-030"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-030"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-075"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-083"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-085"}),
        Action(name="get_role_members", kwargs={"role_id": "ROL-030"}),
        Action(name="list_policy_exceptions", kwargs={"user_id": "U-018", "status": "ACTIVE"}),
        Action(name="approve_access_request", kwargs={"request_id": "AR-034", "reviewer_id": "U-006", "decision_at": "2024-05-30 15:00:00+00:00"}),
        Action(name="assign_role_to_user", kwargs={"user_id": "U-018", "role_id": "ROL-030", "assigned_by": "U-006", "assigned_on": "2024-05-30 15:00:00+00:00"}),
        Action(name="create_audit_log", kwargs={"actor_id": "U-006", "action_type": "ACCESS_APPROVED", "target_id": "AR-034", "timestamp": "2024-05-30 15:00:00+00:00", "details": "request_id=AR-034|user_id=U-018|resource_id=RES-034|role_id=ROL-030|decision=APPROVED"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-018"}),
        Action(name="list_access_requests", kwargs={"status": "APPROVED", "resource_id": "RES-034"}),
    ],
    outputs=[
        '[{"request_id":"AR-034","user_id":"U-018","resource_id":"RES-034","requested_role_id":"ROL-030","justification":"Requesting read access to tax compliance software.","status":"APPROVED","submitted_at":"2024-05-30 15:00:00+00:00","reviewed_by":"U-006","decision_at":"2024-05-30 15:00:00+00:00"}]'
    ]
),



# - TASK 41 -
Task(
    annotator="0",
    user_id="041",
    instruction=(
        "You are Michael Davis (U-005) in Operations. Under the Fixed-Term Access control for RES-027, ensure that Robert White "
        "(U-017) holds ROL-028 starting at 2025-08-06 14:00:00+00:00 with a term end at 2025-12-31 00:00:00+00:00. "
        "Record one canonical audit entry for the assignment at the assignment instant. Return Robert’s current role memberships."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="get_user_details", kwargs={"user_id": "U-017"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-027"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-028"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-017"}),
        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-017",
            "role_id": "ROL-028",
            "assigned_by": "U-005",
            "assigned_on": "2025-08-06 14:00:00+00:00",
            "expires_on": "2025-12-31 00:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-005",
            "action_type": "ROLE_ASSIGNED",
            "target_id": "ROL-028",
            "timestamp": "2025-08-06 14:00:00+00:00",
            "details": "user=U-017|resource=RES-027|assigned_on=2025-08-06 14:00:00+00:00|expires_on=2025-12-31 00:00:00+00:00"
        }),
        Action(name="get_user_roles", kwargs={"user_id": "U-017"})
    ],
    outputs=[
        '[{"role_id":"ROL-021"},{"role_id":"ROL-022"},{"role_id":"ROL-024"},{"role_id":"ROL-028"}]'
    ]
),

# - TASK 42 -
Task(
    annotator="0",
    user_id="042",
    instruction=(
        "You are Michael Davis (U-005) in Operations. Apply Operations controls at their canonical instants: "
        "C-020 is complete at 2025-08-02 14:00:00+00:00; PE-012 is approved at 2025-08-12 23:00:00+00:00 with expiry 2025-09-21 04:59:59+00:00. "
        "At the review instant (2025-08-12 23:00:00+00:00), canonical records show S-024 is NOT ACTIVE; you must record that state (no termination). "
        "Limit reporting to ACTIVE exceptions belonging to ACTIVE Operations users. Return a single stringified object containing "
        "{\"open_exceptions_for_operations\": [...]} and a consolidated completion object for C-020."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-005"}),

        Action(name="get_certification_details", kwargs={"certification_id":"C-020"}),
        Action(name="complete_certification", kwargs={"certification_id":"C-020","completed_on":"2025-08-02 14:00:00+00:00"}),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-005","action_type":"CERTIFICATION_COMPLETED","target_id":"C-020",
            "timestamp":"2025-08-02 14:00:00+00:00","details":"reviewer=U-005|status=COMPLETED"
        }),

        Action(name="get_policy_exception_details", kwargs={"exception_id":"PE-012"}),
        Action(name="approve_policy_exception", kwargs={
            "exception_id":"PE-012","reviewed_by":"U-005",
            "expires_on":"2025-09-21 04:59:59+00:00","reviewed_on":"2025-08-12 23:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-005","action_type":"POLICY_EXCEPTION_APPROVED","target_id":"PE-012",
            "timestamp":"2025-08-12 23:00:00+00:00","details":"subject=U-023|permission=P-089|expires=2025-09-21 04:59:59+00:00"
        }),

        Action(name="list_user_sessions", kwargs={"user_id":"U-023","active_only": False}),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-005","action_type":"SESSION_CHECK",
            "target_id":"S-024","timestamp":"2025-08-12 23:00:00+00:00","details":"status=NOT_ACTIVE|session=S-024"
        }),

        Action(name="list_users", kwargs={"department":"Operations","status":"ACTIVE"}),
        Action(name="list_policy_exceptions", kwargs={"status":"ACTIVE","user_id":"U-005"}),
        Action(name="list_policy_exceptions", kwargs={"status":"ACTIVE","user_id":"U-023"}),
        Action(name="list_policy_exceptions", kwargs={"status":"ACTIVE","user_id":"U-029"}),
        Action(name="list_policy_exceptions", kwargs={"status":"ACTIVE","user_id":"U-031"}),
        Action(name="list_policy_exceptions", kwargs={"status":"ACTIVE","user_id":"U-033"})
    ],
    outputs=[
        '{"open_exceptions_for_operations":[{"exception_id":"PE-012","status":"ACTIVE","user_id":"U-023"}],'
        '"certification_C-020":{"status":"COMPLETED","completed_on":"2025-08-02 14:00:00+00:00"}}'
    ]
),


# - TASK 43 -
Task(
    annotator="0",
    user_id="043",
    instruction=(
        "You are Alex Johnson (U-001) from Engineering. Under RBAC policy, handle the pending access request "
        "for production-web-server-1 (RES-025). This resource is owned by Operations, and the designated reviewer "
        "is Jeffery Green (U-023), who is ACTIVE with MFA. Approve only if the requester (U-029) is MFA-enabled, "
        "since this is CRITICAL role access. Apply the one-year CRITICAL access policy: decision and assignment "
        "take effect at the submitted_at time (2024-05-20T14:00:00Z), and the role must expire on 2025-05-20T14:00:00Z. "
        "Ensure the approval is logged and both requester and reviewer are notified. Return the processed request record."
    ),
    actions=[
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-025"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="get_user_details", kwargs={"user_id": "U-023"}),
        Action(name="get_user_details", kwargs={"user_id": "U-029"}),
        Action(name="approve_access_request", kwargs={
            "request_id": "AR-007",
            "reviewer_id": "U-023",
            "decision_at": "2024-05-20T14:00:00Z"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-029",
            "role_id": "ROL-026",
            "assigned_by": "U-023",
            "assigned_on": "2024-05-20T14:00:00Z",
            "expires_on": "2025-05-20T14:00:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-023",
            "action_type": "ACCESS_REQUEST_APPROVED",
            "target_id": "AR-007",
            "timestamp": "2024-05-20T14:00:00Z",
            "details": "request=AR-007|resource=RES-025|role=ROL-026|decision=APPROVED|reviewer=U-023|at=2024-05-20T14:00:00Z"
        }),
        Action(name="send_email", kwargs={
            "sender": "U-023",
            "receiver": "U-029",
            "subject": "AR-007|RES-025|ROL-026|APPROVED",
            "body": "request=AR-007|user=U-029|resource=RES-025|role=ROL-026|status=APPROVED|at=2024-05-20T14:00:00Z",
            "timestamp": "2024-05-20T14:00:00Z"
        }),
        Action(name="send_email", kwargs={
            "sender": "U-023",
            "receiver": "U-023",
            "subject": "AR-007|RES-025|ROL-026|APPROVED",
            "body": "request=AR-007|user=U-029|resource=RES-025|role=ROL-026|status=APPROVED|at=2024-05-20T14:00:00Z",
            "timestamp": "2024-05-20T14:00:00Z"
        }),
        Action(name="get_access_request", kwargs={"request_id": "AR-007"})
    ],
    outputs=[
        '[{"request_id":"AR-007","user_id":"U-029","resource_id":"RES-025","requested_role_id":"ROL-026","status":"APPROVED","submitted_at":"2024-05-20T14:00:00Z","reviewed_by":"U-023","decision_at":"2024-05-20T14:00:00Z"}]'
    ]
),


# - TASK 44 -
Task(
    annotator="0",
    user_id="044",
    instruction=(
        "You are Ashley Wilson (U-010), Human Resources. Apply the HR two-stage review policy to access request AR-037 "
        "for resource RES-041 with requested role ROL-019. The canonical outcome is APPROVED, with all writes anchored at "
        "2024-05-30 19:00:00+00:00. Under this policy, the record must reflect the first-stage reviewer as U-005 with "
        "decision_at=2024-05-30 19:00:00+00:00, and the final status as APPROVED updated_by=U-010 at the same anchor time. "
        "Use the standard tokenized notification format for stakeholders and apply the HR comms pin for SL-037 in #access-requests. "
        "Return the exact updated access_request record."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-010"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-037"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-041"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-019"}),
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),

        Action(name="approve_access_request", kwargs={
            "request_id": "AR-037",
            "reviewer_id": "U-005",
            "decision_at": "2024-05-30 19:00:00+00:00"
        }),

        Action(name="update_access_request", kwargs={
            "request_id": "AR-037",
            "status": "APPROVED",
            "updated_on": "2024-05-30 19:00:00+00:00",
            "updated_by": "U-010"
        }),

        Action(name="send_email", kwargs={
            "sender": "U-010",
            "receiver": "U-005",
            "subject": "AR-037|RES-041|ROL-019|SECOND_REVIEW_RECORDED",
            "body": "request=AR-037|resource=RES-041|role=ROL-019|reviewer=U-005|second_review_by=U-010|status=APPROVED|at=2024-05-30 19:00:00+00:00",
            "timestamp": "2024-05-30 19:00:00+00:00"
        }),
        Action(name="send_email", kwargs={
            "sender": "U-010",
            "receiver": "U-010",
            "subject": "AR-037|RES-041|ROL-019|SECOND_REVIEW_RECORDED",
            "body": "request=AR-037|resource=RES-041|role=ROL-019|reviewer=U-005|second_review_by=U-010|status=APPROVED|at=2024-05-30 19:00:00+00:00",
            "timestamp": "2024-05-30 19:00:00+00:00"
        }),

        Action(name="moderate_slack_channel", kwargs={
            "channel": "#access-requests",
            "action": "pin",
            "message_ids": ["SL-037"],
            "moderator_id": "U-010"
        })
    ],
    outputs=[
        '{"request_id":"AR-037","user_id":"U-010","resource_id":"RES-041","requested_role_id":"ROL-019","justification":"Need to post a new job opening.","status":"APPROVED","submitted_at":"2024-05-30 19:00:00+00:00","reviewed_by":"U-005","decision_at":"2024-05-30 19:00:00+00:00","updated_on":"2024-05-30 19:00:00+00:00","updated_by":"U-010"}'
    ]
),



# - TASK 45 -
Task(
    annotator="0",
    user_id="045",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. Enforce RBAC for RES-025: the reviewer must be in Operations with mfa_enabled=true, "
        "and the requester must have mfa_enabled=true. Evaluate AR-007 at the cutoff 2024-05-20T14:00:00Z by verifying that every permission "
        "in ROL-026 is scoped to RES-025 and that the requester does not already hold ROL-026. If any permission is not scoped to RES-025, "
        "reject the request. Use deterministic, tokenized audit and notification records anchored at the cutoff."
    ),
    actions=[
        Action(name="get_access_request", kwargs={"request_id": "AR-007"}),
        Action(name="get_user_details", kwargs={"user_id": "U-029"}),   # requester (must have MFA=true)
        Action(name="get_user_roles", kwargs={"user_id": "U-029"}),     # confirm requester doesn’t already hold ROL-026
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-026"}),

        Action(name="get_user_details", kwargs={"user_id": "U-023"}),

        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-026"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-060"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-061"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-062"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-089"}),

        Action(name="reject_access_request", kwargs={
            "request_id": "AR-007",
            "reviewer_id": "U-023",
            "decision_at": "2024-05-20T14:00:00+00:00"
        }),

        Action(name="create_audit_log", kwargs={
            "actor_id": "U-023",
            "action_type": "ACCESS_REJECTED",
            "target_id": "AR-007",
            "timestamp": "2024-05-20T14:00:00+00:00",
            "details": "request_id=AR-007|user=U-029|role=ROL-026|resource=RES-025|decision=REJECTED"
        }),
        Action(name="send_email", kwargs={
            "sender": "U-001",
            "receiver": "U-029",
            "subject": "AR-007|RES-025|ROL-026|REJECTED",
            "body": "request=AR-007|user=U-029|role=ROL-026|resource=RES-025|status=REJECTED|at=2024-05-20T14:00:00+00:00",
            "timestamp": "2024-05-20T14:00:00+00:00"
        })
    ],
    outputs=[
        '[{"request_id":"AR-007","user_id":"U-029","resource_id":"RES-025","requested_role_id":"ROL-026","status":"REJECTED","reviewed_by":"U-023","decision_at":"2024-05-20T14:00:00+00:00"}]'
    ]
),

# - TASK 46 -
Task(
    annotator="0",
    user_id="046",
    instruction=(
        "You are Jessica Garcia (U-006), Finance. Apply the Policy Exception Review Standard: a request from a DISABLED requester "
        "is non-grantable. Use requested_on as review time, record the canonical audit, export the audit slice, and return the updated exception."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-006"}),                                   # 1
        Action(name="get_policy_exception_details", kwargs={"exception_id":"PE-011"}),                 # 1
        Action(name="get_user_details", kwargs={"user_id":"U-027"}),                                   # 1
        Action(name="list_policy_exceptions", kwargs={"user_id":"U-027","status":"ACTIVE"}),           # 2
        Action(name="deny_policy_exception", kwargs={                                                  # 3
            "exception_id":"PE-011",
            "reviewed_by":"U-006",
            "reviewed_on":"2025-08-03T17:00:00Z"
        }),
        Action(name="create_audit_log", kwargs={                                                       # 5
            "actor_id":"U-006",
            "action_type":"POLICY_EXCEPTION_DENIED",
            "target_id":"PE-011",
            "timestamp":"2025-08-03T17:00:00Z",
            "details":"requester=U-027|request_time=2025-08-03T17:00:00Z|reason=REQUESTER_DISABLED|decision=DENIED"
        }),
        Action(name="export_audit_logs", kwargs={                                                      # 5
            "actor_id":"U-006",
            "action_type":"POLICY_EXCEPTION_DENIED",
            "target_id":"PE-011",
            "start_time":"2025-08-03T17:00:00Z",
            "end_time":"2025-08-03T17:00:00Z"
        }),
        Action(name="get_policy_exception_details", kwargs={"exception_id":"PE-011"})                  # 1
    ],
    outputs=[
        '{"exception_id":"PE-011","user_id":"U-027","permission_id":"P-037","reviewed_by":"U-006",'
        '"requested_on":"2025-08-03T17:00:00Z","reviewed_on":"2025-08-03T17:00:00Z","status":"DENIED"}'
    ]
),


# - TASK 47 -
Task(
    annotator="0",
    user_id="047",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. For request AR-020 by U-013 on RES-006 with role ROL-004, "
        "apply RBAC rules: validate that all permissions in the requested role match the resource’s policy scope. "
        "If the role’s permissions are scoped to RES-006 (internal-documentation-wiki), APPROVE; otherwise REJECT. "
        "Ensure MFA is active for U-013 before decision (verify only; do not re-enable if already true). "
        "Record the decision in audit logs and notify the requester using deterministic tokens."
    ),
    actions=[
        Action(name="get_access_request", kwargs={"request_id": "AR-020"}),
        Action(name="get_user_details", kwargs={"user_id": "U-013"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-004"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-006"}),

        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-004"}),

        Action(name="approve_access_request", kwargs={
            "request_id": "AR-020",
            "reviewer_id": "U-001",
            "decision_at": "2024-05-26T14:00:00Z"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-013",
            "role_id": "ROL-004",
            "assigned_by": "U-001",
            "assigned_on": "2024-05-26T14:00:00Z"
        }),

        Action(name="create_audit_log", kwargs={
            "actor_id": "U-001",
            "action_type": "ACCESS_APPROVED",
            "target_id": "AR-020",
            "timestamp": "2024-05-26T14:00:00Z",
            "details": "request=AR-020|resource=RES-006|role=ROL-004|user=U-013|mfa=VERIFIED|decision=APPROVED|at=2024-05-26T14:00:00Z"
        }),

        Action(name="send_email", kwargs={
            "sender": "U-001",
            "receiver": "U-013",
            "subject": "AR-020|RES-006|ROL-004|APPROVED",
            "body": "request=AR-020|user=U-013|resource=RES-006|role=ROL-004|status=APPROVED|at=2024-05-26T14:00:00Z",
            "timestamp": "2024-05-26T14:00:00Z"
        })
    ],
    outputs=[
        '[{"request_id":"AR-020","user_id":"U-013","resource_id":"RES-006","requested_role_id":"ROL-004",'
        '"status":"APPROVED","reviewed_by":"U-001","decision_at":"2024-05-26T14:00:00Z"}]'
    ]
),


# - TASK 48 -
Task(
    annotator="0",
    user_id="048",
    instruction=(
        "You are Michael Davis (U-005), Operations. By 2024-06-10 15:45:00+00:00, ALRT-003 on RES-020 must reflect severity CRITICAL under "
        "critical-resource policy. Capture one ALERT_FINALIZED audit at that instant with final_severity=CRITICAL and reason code "
        "CRITICAL_RESOURCE_POLICY. Return the resulting severity."
    ),
    actions=[
        Action(name="get_siem_alert_details", kwargs={"alert_id": "ALRT-003"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-020"}),
        Action(name="investigate_siem_incident", kwargs={
            "alert_id": "ALRT-003",
            "analyst_id": "U-005",
            "notes": "resource=RES-020|handled_at=2024-06-10 15:45:00+00:00",
            "investigated_on": "2024-06-10 15:45:00+00:00"
        }),
        Action(name="escalate_siem_alert", kwargs={
            "alert_id": "ALRT-003",
            "severity": "CRITICAL",
            "reason": "CRITICAL_RESOURCE_POLICY"
        }),
        Action(name="get_siem_alert_details", kwargs={"alert_id": "ALRT-003"}),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-005",
            "action_type": "ALERT_FINALIZED",
            "target_id": "ALRT-003",
            "timestamp": "2024-06-10 15:45:00+00:00",
            "details": "resource=RES-020|final_severity=CRITICAL|handled_at=2024-06-10 15:45:00+00:00|reason=CRITICAL_RESOURCE_POLICY"
        })
    ],
    outputs=[
        '[{"alert_id":"ALRT-003","resource_id":"RES-020","final_severity":"CRITICAL"}]'
    ]
),


# - TASK 49 -
Task(
    annotator="0",
    user_id="049",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. Adjudicate access request AR-022 for U-009 requesting role ROL-013 on RES-016 "
        "according to RBAC policy. The decision must use the request’s submitted_at timestamp "
        "(2024-05-26 16:00:00+00:00) as the authoritative decision time. Approval is only valid if the requester has MFA enabled "
        "and the reviewer’s department matches that of the resource owner; otherwise the request must be rejected. "
        "The outcome must be recorded in the canonical audit trail with deterministic evidence that includes the request ID, requester, role, "
        "resource, decision (APPROVED or REJECTED), reason, reviewer, and timestamp. The requester must also be notified deterministically "
        "with a subject line indicating the request ID, resource, role, and final decision, and with a body that states the decision, reason, "
        "reviewer, and timestamp. In the dataset, RES-016 is owned by U-021 (department=Sales) and the reviewer (U-001) belongs to Engineering, "
        "so the department mismatch requires a REJECTION with reason DEPT_MISMATCH. Return the updated request record."
    ),
    actions=[
        Action(name="get_access_request", kwargs={"request_id": "AR-022"}),
        Action(name="get_user_details", kwargs={"user_id": "U-009"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-016"}),
        Action(name="get_user_details", kwargs={"user_id": "U-021"}),
        Action(name="get_user_details", kwargs={"user_id": "U-001"}),

        Action(name="reject_access_request", kwargs={
            "request_id": "AR-022",
            "reviewer_id": "U-001",
            "decision_at": "2024-05-26 16:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-001",
            "action_type": "ACCESS_REJECTED",
            "target_id": "AR-022",
            "timestamp": "2024-05-26 16:00:00+00:00",
            "details": "request_id=AR-022|user=U-009|role=ROL-013|resource=RES-016|decision=REJECTED|reason=DEPT_MISMATCH|reviewer=U-001|at=2024-05-26 16:00:00+00:00"
        }),
        Action(name="send_email", kwargs={
            "sender": "U-001",
            "receiver": "U-009",
            "subject": "AR-022|RES-016|ROL-013|DECISION=REJECTED",
            "body": "request_id=AR-022|decision=REJECTED|reason=DEPT_MISMATCH|reviewer=U-001|at=2024-05-26 16:00:00+00:00",
            "timestamp": "2024-05-26 16:00:00+00:00"
        })
    ],
    outputs=[
        '[{"request_id":"AR-022","user_id":"U-009","resource_id":"RES-016","requested_role_id":"ROL-013","justification":"Need lead manager access for new marketing campaign leads.","status":"REJECTED","submitted_at":"2024-05-26 16:00:00+00:00","reviewed_by":"U-001","decision_at":"2024-05-26 16:00:00+00:00"}]'
    ]
),


# - TASK 50 -
Task(
    annotator="0",
    user_id="050",
    instruction=(
        "You are Sarah Williams (U-002), Marketing owner of RES-008. Apply Marketing access-review policy to AR-009 for ROL-008: "
        "decide per policy and, if provisioned, record the required Marketing second-review as an immutable audit by the Marketing lead of record U-014. "
        "Anchor all writes to the request’s submitted_at. Return the authoritative request record and the second-review evidence. Avoid unnecessary actions."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-002"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-008"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-009"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-008"}),
        Action(name="get_user_details", kwargs={"user_id": "U-026"}),
        Action(name="approve_access_request", kwargs={
            "request_id": "AR-009",
            "reviewer_id": "U-002",
            "decision_at": "2024-05-20T16:00:00+00:00"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-026",
            "role_id": "ROL-008",
            "assigned_by": "U-002",
            "assigned_on": "2024-05-20T16:00:00+00:00"
        }),
        Action(name="get_user_details", kwargs={"user_id": "U-014"}),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-014",
            "action_type": "SECOND_REVIEW_RECORDED",
            "target_id": "AR-009",
            "timestamp": "2024-05-20T16:00:00+00:00",
            "details": "EVIDENCE:SECOND_REVIEW_RECORDED|request_id=AR-009|by=U-014|t=2024-05-20T16:00:00+00:00"
        }),
        Action(name="get_access_request", kwargs={"request_id": "AR-009"})
    ],
    outputs=[
        '[{"request_id":"AR-009","user_id":"U-026","resource_id":"RES-008","requested_role_id":"ROL-008","status":"APPROVED","reviewed_by":"U-002","decision_at":"2024-05-20T16:00:00+00:00"}]',
        '"EVIDENCE:SECOND_REVIEW_RECORDED|request_id=AR-009|by=U-014|t=2024-05-20T16:00:00+00:00"'
    ]
),

# - TASK 51 -
Task(
    annotator="0",
    user_id="051",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. Approve policy exception PE-018 for U-007 to use permission "
        "P-005 with expires_on=2025-11-16T04:59:59Z, record an immutable audit entry, and notify U-007 by email. "
        "Use the evidencing anchor T0=2025-08-06T15:30:00Z."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-001"}),
        Action(name="get_policy_exception_details", kwargs={"exception_id":"PE-018"}),
        Action(name="get_user_details", kwargs={"user_id":"U-007"}),
        Action(name="get_permission_details", kwargs={"permission_id":"P-005"}),
        Action(name="approve_policy_exception", kwargs={
            "exception_id":"PE-018",
            "reviewed_by":"U-001",
            "expires_on":"2025-11-16T04:59:59Z",
            "reviewed_on":"2025-08-06T15:30:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-001",
            "action_type":"POLICY_EXCEPTION_APPROVED",
            "target_id":"PE-018",
            "timestamp":"2025-08-06T15:30:00Z",
            "details":"PE:PE-018|PERM:P-005|USER:U-007|STATUS:APPROVED|EXPIRES:2025-11-16T04:59:59Z|BY:U-001|AT:2025-08-06T15:30:00Z"
        }),
        Action(name="send_email", kwargs={
            "sender":"U-001",
            "receiver":"U-007",
            "subject":"NOTICE|PE:PE-018|STATUS:APPROVED|EXPIRES:2025-11-16T04:59:59Z",
            "body":"PE:PE-018|PERM:P-005|USER:U-007|STATUS:APPROVED|EXPIRES:2025-11-16T04:59:59Z|BY:U-001|AT:2025-08-06T15:30:00Z",
            "timestamp":"2025-08-06T15:30:00Z"
        })
    ],
    outputs=[
        '[{"exception_id":"PE-018","final_status":"APPROVED","expires_on":"2025-11-16T04:59:59Z","reviewed_on":"2025-08-06T15:30:00Z"}]',
        '[{"audit_details":"PE:PE-018|PERM:P-005|USER:U-007|STATUS:APPROVED|EXPIRES:2025-11-16T04:59:59Z|BY:U-001|AT:2025-08-06T15:30:00Z"}]',
        '[{"email_subject":"NOTICE|PE:PE-018|STATUS:APPROVED|EXPIRES:2025-11-16T04:59:59Z"}]'
    ]
),


# - TASK 52 -
Task(
    annotator="0",
    user_id="052",
    instruction=(
        "You are David Brown (U-003), Sales. Submit a one-time policy exception request so that U-022 can run a script "
        "requiring permission P-011. The request is logged at 2025-08-11T09:00:00Z. Under Operations policy, Michael Davis "
        "(U-005) is the designated reviewer and must decide at 2025-08-11T10:00:00Z. The approval must set "
        "expires_on=2025-08-18T04:59:59Z. All events must be captured in immutable audit logs with those timestamps, and "
        "the requester (U-003) must be notified deterministically of both the submission and the approval. "
        "Return the final state of policy exception PE-021."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-022"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-011"}),

        Action(name="request_policy_exception", kwargs={
            "user_id": "U-022",
            "permission_id": "P-011",
            "reason": "ONE_TIME:P-011",
            "requested_on": "2025-08-11T09:00:00Z"
        }),

        Action(name="get_policy_exception_details", kwargs={"exception_id": "PE-021"}),

        Action(name="get_user_details", kwargs={"user_id": "U-005"}),

        Action(name="approve_policy_exception", kwargs={
            "exception_id": "PE-021",
            "reviewed_by": "U-005",
            "reviewed_on": "2025-08-11T10:00:00Z",
            "expires_on": "2025-08-18T04:59:59Z"
        }),

        Action(name="create_audit_log", kwargs={
            "actor_id": "U-003",
            "action_type": "POLICY_EXCEPTION_SUBMITTED",
            "target_id": "PE-021",
            "timestamp": "2025-08-11T09:00:00Z",
            "details": "exception_id=PE-021|requested_by=U-003|target_user=U-022|permission=P-011|at=2025-08-11T09:00:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-005",
            "action_type": "POLICY_EXCEPTION_APPROVED",
            "target_id": "PE-021",
            "timestamp": "2025-08-11T10:00:00Z",
            "details": "exception_id=PE-021|approved_by=U-005|expires_on=2025-08-18T04:59:59Z|at=2025-08-11T10:00:00Z"
        }),

        Action(name="send_email", kwargs={
            "sender": "U-003",
            "receiver": "U-003",
            "subject": "PE-021|REQUESTED",
            "body": "exception_id=PE-021",
            "timestamp": "2025-08-11T09:00:00Z"
        }),
        Action(name="send_email", kwargs={
            "sender": "U-003",
            "receiver": "U-003",
            "subject": "PE-021|APPROVED",
            "body": "exception_id=PE-021",
            "timestamp": "2025-08-11T10:00:00Z"
        })
    ],
    outputs=[
        '[{"exception_id":"PE-021","status":"ACTIVE","reviewed_by":"U-005","expires_on":"2025-08-18T04:59:59Z"}]'
    ]
),


# - TASK 53 -
Task(
    annotator="0",
    user_id="053",
    instruction=(
        "You are Matthew Lopez (U-009), Sales. For RES-008, process AR-009 requesting ROL-008 in line with RBAC: the Marketing owner (U-002) must approve. "
        "Verify the requester (U-026) is ACTIVE and does not already hold ROL-008 before assignment. Record a concise audit note and notify reviewer and requester. "
        "Return the resulting request state."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-009"}),
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-008"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-008"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-008"}),
        Action(name="get_user_details", kwargs={"user_id": "U-002"}),
        Action(name="get_user_details", kwargs={"user_id": "U-026"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-026"}),
        Action(name="approve_access_request", kwargs={
                "request_id": "AR-009",
                "reviewer_id": "U-002",
                "decision_at": "2024-05-20T16:00:00Z"
            }),
        Action(name="assign_role_to_user", kwargs={
                "user_id": "U-026",
                "role_id": "ROL-008",
                "assigned_by": "U-002",
                "assigned_on": "2024-05-20T16:00:00Z"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-002",
                "action_type": "ACCESS_APPROVED",
                "target_ref": {"kind":"ACCESS_REQUEST","id":"AR-009"},
                "timestamp": "2024-05-20T16:00:00Z",
                "details": "request_id=AR-009|role=ROL-008|resource=RES-008"
            }),
        Action(name="send_email", kwargs={
                "sender": "U-009",
                "receiver": "U-002",
                "subject": "AR-009",
                "body": "status=APPROVED",
                "timestamp": "2024-05-20T16:00:00Z"
            }),
        Action(name="send_email", kwargs={
                "sender": "U-009",
                "receiver": "U-026",
                "subject": "AR-009",
                "body": "status=APPROVED",
                "timestamp": "2024-05-20T16:00:00Z"
            })
    ],
    outputs=[
        '[{"request_id":"AR-009","user_id":"U-026","resource_id":"RES-008","requested_role_id":"ROL-008","status":"APPROVED","reviewed_by":"U-002","decision_at":"2024-05-20T16:00:00Z"}]'
    ]
),


# - TASK 54 -
Task(
    annotator="0",
    user_id="054",
    instruction=(
        "You are Nicole Thomas (U-014), owner of RES-012. As of 2024-05-26 15:00:00+00:00, AR-021 must be recorded as not granted. "
        "Before recording the decision, you must confirm the requester’s identity from canonical user records and confirm the requested "
        "role’s definition and permission scope from the canonical role catalog. Ensure one deterministic audit entry "
        "(resource_id, role_id, decision=REJECTED, decision_at). Return the REJECTED requests for RES-012."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-014"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-012"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-021"}),
        # Requester identity verification
        Action(name="get_user_details", kwargs={"user_id": "U-026"}),
        # Role catalog verification (new)
        Action(name="get_role_details", kwargs={"role_id": "ROL-010"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-010"}),
        Action(name="reject_access_request", kwargs={
            "request_id": "AR-021",
            "reviewer_id": "U-014",
            "decision_at": "2024-05-26 15:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-014",
            "action_type": "ACCESS_REJECTED",
            "target_id": "AR-021",
            "timestamp": "2024-05-26 15:00:00+00:00",
            "details": "resource=RES-012|role=ROL-010|decision=REJECTED|decision_at=2024-05-26 15:00:00+00:00"
        }),
        Action(name="list_access_requests", kwargs={"status": "REJECTED", "resource_id": "RES-012"})
    ],
    outputs=[
        '[{"request_id":"AR-021","user_id":"U-026","resource_id":"RES-012","requested_role_id":"ROL-010","status":"REJECTED","decision_at":"2024-05-26 15:00:00+00:00","reviewed_by":"U-014"}]'
    ]
),


# - TASK 55 -
Task(
    annotator="0",
    user_id="055",
    instruction=(
        "You are Sarah Williams (U-002), Marketing owner of social-media-platform (RES-008). "
        "Apply the reviewer-department policy: as the Marketing owner, you are the primary approver for AR-009. "
        "Record Finance visibility and note an Operations consult for cross-functional visibility. "
        "Use decision timestamp 2024-05-20T16:00:00Z for all approvals/notes and assign the requested role "
        "with a one-year expiry at the same second (+1 year)."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-002"}),
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-008"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-008"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-008"}),
        Action(name="get_user_details", kwargs={"user_id": "U-026"}),
        Action(name="approve_access_request", kwargs={
                "request_id": "AR-009",
                "reviewer_id": "U-002",
                "decision_at": "2024-05-20T16:00:00Z"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-002",
                "action_type": "EVIDENCE_CAPTURED",
                "target_ref": {"kind":"ACCESS_REQUEST","id":"AR-009"},
                "timestamp": "2024-05-20T16:00:00Z",
                "details": "department=FINANCE|type=VISIBILITY_REVIEW_RECORDED"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-002",
                "action_type": "EVIDENCE_CAPTURED",
                "target_ref": {"kind":"ACCESS_REQUEST","id":"AR-009"},
                "timestamp": "2024-05-20T16:00:00Z",
                "details": "department=OPERATIONS|type=CONSULT_NOTED"
            }),
        Action(name="assign_role_to_user", kwargs={
                "user_id": "U-026",
                "role_id": "ROL-008",
                "assigned_by": "U-002",
                "assigned_on": "2024-05-20T16:00:00Z",
                "expires_on": "2025-05-20T16:00:00Z",
                "expiry_policy": "EXPLICIT",
            })
    ],
    outputs=[
        '[{"request_id":"AR-009","user_id":"U-026","resource_id":"RES-008","requested_role_id":"ROL-008","status":"APPROVED","reviewed_by":"U-002","decision_at":"2024-05-20T16:00:00Z"}]'
    ]
),


# - TASK 56 -
Task(
    annotator="0",
    user_id="056",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. Approve policy exception PE-018 for U-007 "
        "to use permission P-005 until 2025-11-16T04:59:59Z. Record outcome and notify requester. "
        "T0=2025-08-06T15:30:00Z."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-001"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-001"}),
        Action(name="get_policy_exception_details", kwargs={"exception_id":"PE-018"}),
        Action(name="get_user_details", kwargs={"user_id":"U-007"}),
        Action(name="get_permission_details", kwargs={"permission_id":"P-005"}),
        Action(name="approve_policy_exception", kwargs={
                "exception_id":"PE-018",
                "reviewed_by":"U-001",
                "expires_on":"2025-11-16T04:59:59Z",
                "reviewed_on":"2025-08-06T15:30:00Z"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-001",
                "action_type":"POLICY_EXCEPTION_APPROVED",
                "target_id":"PE-018",
                "timestamp":"2025-08-06T15:30:00Z",
                "details":"PE-018|APPROVED|P-005|U-007|EXPIRES:2025-11-16T04:59:59Z|BY:U-001|AT:2025-08-06T15:30:00Z"
            }),
        Action(name="send_email", kwargs={
                "sender":"U-001",
                "receiver":"U-007",
                "subject":"PE-018|APPROVED|P-005|EXPIRES:2025-11-16T04:59:59Z",
                "body":"PE-018|APPROVED|P-005|U-007|EXPIRES:2025-11-16T04:59:59Z|BY:U-001|AT:2025-08-06T15:30:00Z",
                "timestamp":"2025-08-06T15:30:00Z"
            })
    ],
    outputs=[
        '[{"exception_id":"PE-018","final_status":"APPROVED","expires_on":"2025-11-16T04:59:59Z"}]',
        '[{"audit":"PE-018|APPROVED|P-005|U-007|EXPIRES:2025-11-16T04:59:59Z|BY:U-001|AT:2025-08-06T15:30:00Z"}]',
        '[{"email_subject":"PE-018|APPROVED|P-005|EXPIRES:2025-11-16T04:59:59Z"}]'
    ]
),


# - TASK 57 -
Task(
    annotator="0",
    user_id="057",
    instruction=(
        "You are Michael Davis (U-005), Operations. You must triage SIEM alert ALRT-005 affecting RES-025 and drive the policy outcome: "
        "investigation anchored at T0=2024-08-28T13:30:00Z, escalation to CRITICAL (reason token ALRT-005), creation of a "
        "correlation rule linking the alert and resource with notes referencing T0, ticketing to the resource owner, and a "
        "synchronized notification to the Engineering lead. All time-stamped records use T0. The Engineering lead is deterministically "
        "selected as the ACTIVE Engineering user with the lowest user_id, which is Alex Johnson (U-001)."
    ),
    actions=[
        Action(name="get_siem_alert_details", kwargs={"alert_id": "ALRT-005"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="investigate_siem_incident", kwargs={
                "alert_id": "ALRT-005",
                "analyst_id": "U-005",
                "notes": "ALERT=ALRT-005",
                "investigated_on": "2024-08-28T13:30:00Z"
        }),
        Action(name="escalate_siem_alert", kwargs={
                "alert_id": "ALRT-005",
                "severity": "CRITICAL",
                "reason": "ALRT-005"
        }),
        Action(name="create_siem_rule", kwargs={
                "rule_name": "RULE:ALRT-005:RES-025",
                "conditions": {"source_alert_id": "ALRT-005", "resource": "RES-025"},
                "created_by": "U-005",
                "created_on": "2024-08-28T13:30:00Z",
                "notes": "FROM_ALERT:ALRT-005@2024-08-28T13:30Z"
        }),
        Action(name="create_hubspot_ticket", kwargs={
                "subject": "TI|ALRT-005|RES-025",
                "description": "ALERT=ALRT-005|RESOURCE=RES-025|RULE=RULE:ALRT-005:RES-025",
                "requester_id": "U-005",
                "assignee_id": "U-005"
        }),
        Action(name="list_users", kwargs={"department": "Engineering", "status": "ACTIVE"}),
        Action(name="get_user_details", kwargs={"user_id": "U-001"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-001"}),
        Action(name="send_email", kwargs={
                "sender": "U-005",
                "receiver": "U-001",
                "subject": "ALRT-005|RES-025|CRITICAL",
                "body": "t=2024-08-28T13:30:00Z",
                "timestamp": "2024-08-28T13:30:00Z"
        })
    ],
    outputs=[
        '[{"alert_id":"ALRT-005","resource_id":"RES-025","severity":"CRITICAL"}]'
    ]
),

# - TASK 58 -
Task(
    annotator="0",
    user_id="058",
    instruction=(
        "You are Jeffery Green (U-023), Operations. Using T0=2024-05-21T09:00:00Z for all timestamps, verify whether any "
        "ACTIVE policy exceptions apply to production-web-server-1 (RES-025). An exception 'applies' iff its permission_id "
        "maps to a permission whose resource_id equals RES-025. If the applying-exception count is 0, raise an Operations "
        "ticket with subject 'NEGATIVE-FINDING|RES-025|EXCEPTIONS|T0=2024-05-21' and capture two audits with tokenized details: "
        "one for the exception review result and one for the ticket creation. Return the count and the ticket subject (if created)."
    ),
    actions=[
        # Actor + scope
        Action(name="get_user_details", kwargs={"user_id": "U-023"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),

        # List ACTIVE exceptions and resolve their permissions (dataset-derived permission_ids)
        Action(name="list_policy_exceptions", kwargs={"status": "ACTIVE"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-021"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-022"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-029"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-070"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-096"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-108"}),

        # Review result (count is 0 for RES-025) at T0
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-023",
            "action_type": "POLICY_EXCEPTION_REVIEWED",
            "target_ref": {"kind": "RESOURCE", "id": "RES-025"},
            "timestamp": "2024-05-21T09:00:00Z",
            "details": "resource=RES-025|active_exception_matches=0|rule=permission.resource_id==RES-025"
        }),

        # Negative-finding ticket + evidence audit at T0
        Action(name="create_hubspot_ticket", kwargs={
            "subject": "NEGATIVE-FINDING|RES-025|EXCEPTIONS|T0=2024-05-21",
            "requester_id": "U-023",
            "category": "OPERATIONS",
            "created_at": "2024-05-21T09:00:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-023",
            "action_type": "TICKET_CREATED",
            "target_ref": {"kind": "RESOURCE", "id": "RES-025"},
            "timestamp": "2024-05-21T09:00:00Z",
            "details": "subject=NEGATIVE-FINDING|RES-025|EXCEPTIONS|T0=2024-05-21"
        }),
    ],
    outputs=[
        '[{"resource_id":"RES-025","active_exception_matches":0,"ticket_subject":"NEGATIVE-FINDING|RES-025|EXCEPTIONS|T0=2024-05-21"}]'
    ]
),


# - TASK 59 -
Task(
    annotator="0",
    user_id="059",
    instruction=(
        "You are Paul Ellis (U-021), Sales. You own RES-016. "
        "Decide AR-022 at 2024-05-26 16:00:00+00:00 using access policy: reject if the requester already holds the requested role and the role scopes to a different resource. "
        "Record one decision evidence entry using key=value tokens. "
        "Provide: processed_request (post-decision), owner_status, requester_roles (U-009), role_meta (ROL-013), "
        "resource_details (RES-016), role_membership_before, role_membership_after, active_exceptions_for_requester, audit_entry."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-021"}),                               # 1 owner
        Action(name="get_access_request", kwargs={"request_id": "AR-022"}),                         # 2 request
        Action(name="get_user_details", kwargs={"user_id": "U-009"}),                               # 3 requester
        Action(name="get_user_roles", kwargs={"user_id": "U-009"}),                                 # 4 requester roles
        Action(name="get_role_details", kwargs={"role_id": "ROL-013"}),                             # 5 role meta
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-013"}),                    # 6 scope (used in evidence)
        Action(name="get_role_members", kwargs={"role_id": "ROL-013"}),                             # 7 membership before
        Action(name="get_resource_details", kwargs={"resource_id": "RES-016"}),                     # 8 resource
        Action(name="list_policy_exceptions", kwargs={"user_id":"U-009","status":"ACTIVE"}),        # 9 exceptions
        Action(name="reject_access_request", kwargs={                                               # 10 reject
            "request_id":"AR-022","reviewer_id":"U-021","decision_at":"2024-05-26 16:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={                                                    # 11 evidence
            "actor_id":"U-021","action_type":"ACCESS_REJECTED","target_id":"AR-022",
            "timestamp":"2024-05-26 16:00:00+00:00",
            "details":"requester_has_role=true|role_scope=RES-015|target=RES-016"
        }),
        Action(name="get_access_request", kwargs={"request_id": "AR-022"}),                         # 12 post
        Action(name="get_role_members", kwargs={"role_id": "ROL-013"}),                             # 13 membership after
        Action(name="get_audit_logs_for_target", kwargs={"target_id": "AR-022"}),                   # 14 decision slice
    ],
    outputs=[
        '{"processed_request":{"request_id":"AR-022","user_id":"U-009","resource_id":"RES-016","requested_role_id":"ROL-013","justification":"Need lead manager access for new marketing campaign leads.","status":"REJECTED","submitted_at":"2024-05-26 16:00:00+00:00","reviewed_by":"U-021","decision_at":"2024-05-26 16:00:00+00:00"},"owner_status":{"user_id":"U-021","status":"ACTIVE"},"requester_roles":[{"role_id":"ROL-011"},{"role_id":"ROL-012"},{"role_id":"ROL-013"}],"role_meta":{"role_id":"ROL-013","role_name":"sales-lead-manager","description":"Manages sales leads and opportunities","is_temporary":false},"resource_details":{"resource_id":"RES-016","owner_id":"U-021","criticality":"HIGH","compliance_scope":"GDPR"},"role_membership_before":["U-009","U-021"],"role_membership_after":["U-009","U-021"],"active_exceptions_for_requester":[],"audit_entry":{"actor_id":"U-021","action_type":"ACCESS_REJECTED","target_id":"AR-022","timestamp":"2024-05-26 16:00:00+00:00","details":"requester_has_role=true|role_scope=RES-015|target=RES-016"}}'
    ],
),


# - TASK 60 -
Task(
    annotator="0",
    user_id="060",
    instruction=(
        "You are Sarah Williams (U-002), Marketing owner for RES-008. You must decide the pending access request AR-009 "
        "for role ROL-008 per Marketing policy; if allowed, provision the role and record the required second-review "
        "evidence as an audit record (not a second approval). Anchor all writes to AR-009.submitted_at=2024-05-20 16:00:00+00:00. "
        "Return the authoritative request record."
    ),
    actions=[
        Action(name="get_resource_details", kwargs={"resource_id":"RES-008"}),
        Action(name="get_access_request", kwargs={"request_id":"AR-009"}),
        Action(name="get_role_details", kwargs={"role_id":"ROL-008"}),
        Action(name="get_user_details", kwargs={"user_id":"U-026"}),
        Action(name="approve_access_request", kwargs={
            "request_id":"AR-009",
            "reviewer_id":"U-002",
            "decision_at":"2024-05-20 16:00:00+00:00"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id":"U-026",
            "role_id":"ROL-008",
            "assigned_by":"U-002",
            "assigned_on":"2024-05-20 16:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-002",
            "action_type":"SECOND_REVIEW_RECORDED",
            "target_ref":{"kind":"ACCESS_REQUEST","id":"AR-009"},
            "timestamp":"2024-05-20 16:00:00+00:00",
            "details":"request_id=AR-009|resource_id=RES-008|role_id=ROL-008|reviewer=U-002"
        }),
        Action(name="get_access_request", kwargs={"request_id":"AR-009"})
    ],
    outputs=[
        '[{"request_id":"AR-009","user_id":"U-026","resource_id":"RES-008","requested_role_id":"ROL-008","status":"APPROVED","reviewed_by":"U-002","decision_at":"2024-05-20 16:00:00+00:00"}]'
    ]
),

# - TASK 61 -
Task(
    annotator="0",
    user_id="061",
    instruction=(
        "You are Robert White (U-017), Operations (status=PENDING_ACCESS). Perform a policy readiness review for network-firewall-main (RES-027) at T0=2024-05-29T13:31:00Z. "
        "Confirm that the Operations department has at least one ACTIVE member and that you remain PENDING_ACCESS (no elevation). "
        "Capture your canonical context only—your user record, your assigned roles, any ACTIVE sessions, and any access requests on RES-027—without enumerating role permissions. "
        "Treat a role-conflict as holding operations-network-admin (ROL-028); if you do not hold ROL-028, record conflicts=NONE. "
        "Record a READINESS_REVIEW_RECORDED audit at T0 and a READINESS_EVIDENCE snapshot at T0+30s, using tokenized details. "
        "Do not modify request states, roles, sessions, tickets, or alerts."
    ),
    actions=[
        Action(name="list_users", kwargs={"department": "Operations", "status": "ACTIVE"}),
        Action(name="list_users", kwargs={"department": "Operations", "status": "PENDING_ACCESS"}),

        Action(name="get_resource_details", kwargs={"resource_id": "RES-027"}),

        Action(name="get_user_details", kwargs={"user_id": "U-017"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-017"}),

        Action(name="list_access_requests", kwargs={"resource_id": "RES-027"}),
        Action(name="list_sessions", kwargs={"user_id": "U-017", "active_only": True}),

        Action(name="create_audit_log", kwargs={
            "actor_id": "U-017",
            "action_type": "READINESS_REVIEW_RECORDED",
            "target_ref": {"kind":"RESOURCE","id":"RES-027"},
            "timestamp": "2024-05-29T13:31:00Z",
            "details": "asset=RES-027|actor=U-017|dept=Operations|status=PENDING_ACCESS|conflicts=NONE"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-017",
            "action_type": "READINESS_EVIDENCE",
            "target_ref": {"kind":"RESOURCE","id":"RES-027"},
            "timestamp": "2024-05-29T13:31:30Z",
            "details": "snapshot=roles|requests|sessions|verified_at=2024-05-29T13:31:30Z"
        }),
    ],
    outputs=[
        '[{"asset":"RES-027","review":"RECORDED","actor":"U-017","status":"PENDING_ACCESS","conflicts":"NONE"}]'
    ]
),


# - TASK 62 -
Task(
    annotator="0",
    user_id="062",
    instruction=(
        "You are Michael Davis (U-005), Operations. You must re-affirm that AR-024 on database-cluster-primary (RES-026) "
        "remains REJECTED without changing its decision; still record auditable evidence. Use T0=2024-05-27T17:00:00Z for "
        "the review audit and T0+60s for the evidence snapshot. Include SoD posture for your reviewer scope and read "
        "U-001’s roles as referenced context."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-005"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-026"}),
        Action(name="get_user_details", kwargs={"user_id":"U-001"}),
        Action(name="list_access_requests", kwargs={"resource_id":"RES-026"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-005"}),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-005",
            "action_type":"ACCESS_REVIEWED_NO_CHANGE",
            "target_ref":{"kind":"ACCESS_REQUEST","id":"AR-024"},
            "timestamp":"2024-05-27T17:00:00Z",
            "details":"request_id=AR-024|status=REJECTED|resource=RES-026|sod=OK"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-005",
            "action_type":"ACCESS_REVIEW_EVIDENCE",
            "target_ref":{"kind":"ACCESS_REQUEST","id":"AR-024"},
            "timestamp":"2024-05-27T17:01:00Z",
            "details":"checks=logs|roles|sessions|reviewer=U-005"
        }),
        Action(name="get_user_roles", kwargs={"user_id":"U-001"})
    ],
    outputs=[
        '[{"request_id":"AR-024","status":"REJECTED","decision_at":"2024-05-27T17:00:00Z"}]',
        '[{"user_id":"U-001","roles":["ROL-001","ROL-034"]}]'
    ]
),


# - TASK 63 -
Task(
    annotator="0",
    user_id="063",
    instruction=(
        "You are Jessica Garcia (U-006), Finance and owner of RES-034. Resolve AR-034 for RES-034 to APPROVED at "
        "2024-05-30 15:00:00+00:00 under Finance access-governance. Return the single approval audit for AR-034 and the APPROVED requests for RES-034."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-006"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-034"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-034"}),
        Action(name="get_user_details", kwargs={"user_id": "U-018"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-030"}),
        Action(name="approve_access_request", kwargs={
            "request_id": "AR-034",
            "reviewer_id": "U-006",
            "decision_at": "2024-05-30 15:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-006",
            "action_type": "ACCESS_APPROVED",
            "target_id": "AR-034",
            "timestamp": "2024-05-30 15:00:00+00:00",
            "details": "resource=RES-034|role=ROL-030|decision=APPROVED|decision_at=2024-05-30 15:00:00+00:00"
        }),
        Action(name="get_audit_logs_for_target", kwargs={"target_id": "AR-034"}),
        Action(name="list_access_requests", kwargs={"status": "APPROVED", "resource_id": "RES-034"})
    ],
    outputs=[
        '['
        '{"actor_id":"U-006","action_type":"ACCESS_APPROVED","target_id":"AR-034","timestamp":"2024-05-30 15:00:00+00:00","details":"resource=RES-034|role=ROL-030|decision=APPROVED|decision_at=2024-05-30 15:00:00+00:00"},'
        '{"request_id":"AR-034","user_id":"U-018","resource_id":"RES-034","requested_role_id":"ROL-030","status":"APPROVED","decision_at":"2024-05-30 15:00:00+00:00","reviewed_by":"U-006"}'
        ']'
    ]
),


# - TASK 64 -
Task(
    annotator="0",
    user_id="064",
    instruction=(
        "You are Kevin Harris (U-015), Sales. For RES-016, comply with SoD and reporting policy: confirm that ROL-015 grants P-044 on "
        "RES-016, ensure a SYS-AUDIT SoD attestation exists at 2024-05-28T19:04:59Z, and record the monthly Operations report at "
        "2024-05-28T19:05:00Z using the canonical subject 'REPORT|RES-016|ROL-015|P-044|MONTHLY'. Provide traceable evidence by "
        "returning the role–permission–resource binding and verifying the ticket via log search. Keep the action set minimal and compliant."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-015"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-015"}),
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-015"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-044"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-016"}),
        Action(name="create_audit_log", kwargs={
                "actor_id": "SYS-AUDIT",
                "action_type": "SOD_CHECK",
                "target_ref": {"kind":"USER","id":"U-015"},
                "timestamp": "2024-05-28T19:04:59Z",
                "details": "reviewer=U-015|scope=RES-016|conflicts=None|attestation=RECORDED"
            }),
        Action(name="create_hubspot_ticket", kwargs={
                "subject": "REPORT|RES-016|ROL-015|P-044|MONTHLY",
                "requester_id": "U-015",
                "category": "OPERATIONS"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-015",
                "action_type": "REPORT_TICKET_CREATED",
                "target_ref": {"kind":"RESOURCE","id":"RES-016"},
                "timestamp": "2024-05-28T19:05:00Z",
                "details": "SUBJECT=REPORT|RES-016|ROL-015|P-044|MONTHLY"
            }),
        Action(name="search_logs", kwargs={"query": "REPORT|RES-016|ROL-015|P-044|MONTHLY"}),
    ],
    outputs=[
        '[{"role_id":"ROL-015","permissions":["P-044"],"resource_id":"RES-016"}]',
        '[{"ticket_subject":"REPORT|RES-016|ROL-015|P-044|MONTHLY","category":"OPERATIONS","verified_via_search":true}]'
    ]
),


# - TASK 65 -
Task(
    annotator="0",
    user_id="098",
    instruction=(
        "You are Michael Davis (U-005), Operations. As of 2024-06-10 15:45:00+00:00, the canonical state for ALRT-003 on RES-020 must reflect "
        "severity CRITICAL consistent with resource classification. Incident evidence must include one investigation note anchored to that instant "
        "and one deterministic audit entry identifying alert_id, resource_id, final_severity, handled_at. Validate the final state via the detailed "
        "alert view and the alert record before reporting the resulting severity."
    ),
    actions=[
        Action(name="get_siem_alert_details", kwargs={"alert_id": "ALRT-003"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-020"}),
        # Investigation evidence (already added previously)
        Action(name="investigate_siem_incident", kwargs={
            "alert_id": "ALRT-003",
            "analyst_id": "U-005",
            "notes": "resource=RES-020|handled_at=2024-06-10 15:45:00+00:00",
            "investigated_on": "2024-06-10 15:45:00+00:00"
        }),
        Action(name="escalate_siem_alert", kwargs={
            "alert_id": "ALRT-003",
            "severity": "CRITICAL",
            "reason": "CRITICAL_RESOURCE_POLICY"
        }),
        # Post-escalation detailed validation (new)
        Action(name="get_siem_alert_details", kwargs={"alert_id": "ALRT-003"}),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-005",
            "action_type": "ALERT_FINALIZED",
            "target_id": "ALRT-003",
            "timestamp": "2024-06-10 15:45:00+00:00",
            "details": "resource=RES-020|final_severity=CRITICAL|handled_at=2024-06-10 15:45:00+00:00"
        }),
        # Summary alert record read prior to return
        Action(name="get_siem_alert", kwargs={"alert_id": "ALRT-003"})
    ],
    outputs=[
        '[{"alert_id":"ALRT-003","resource_id":"RES-020","final_severity":"CRITICAL"}]'
    ]
),


# - TASK 66 -
Task(
    annotator="0",
    user_id="066",
    instruction=(
        "You are Jeffery Green (U-023) in Operations. Anchor all times at T0=2024-05-21T09:00:00Z. Perform a policy-driven applicability review of ACTIVE policy exceptions against RES-025 (an exception applies only if its permission_id maps to a permission whose resource_id equals RES-025). If the applying-exception count is zero, create a single negative-finding ticket addressed to the RES-025 owner using subject 'NEGATIVE-FINDING|RES-025|EXCEPTIONS|T0=2024-05-21' and category EXCEPTION_REVIEW, with a deterministic description token. Record one immutable audit of the review result at T0."
    ),
    actions=[
        Action(name="list_policy_exceptions", kwargs={"status":"ACTIVE"}),
        Action(name="get_permission_details", kwargs={"permission_id":"P-021"}),
        Action(name="get_permission_details", kwargs={"permission_id":"P-029"}),
        Action(name="get_permission_details", kwargs={"permission_id":"P-022"}),
        Action(name="get_permission_details", kwargs={"permission_id":"P-108"}),
        Action(name="get_permission_details", kwargs={"permission_id":"P-096"}),
        Action(name="get_permission_details", kwargs={"permission_id":"P-070"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-025"}),
        Action(name="create_hubspot_ticket", kwargs={
            "subject":"NEGATIVE-FINDING|RES-025|EXCEPTIONS|T0=2024-05-21",
            "description":"applies=0|scope=RES-025|at=T0",
            "requester_id":"U-023",
            "assignee_id":"U-005",
            "category":"EXCEPTION_REVIEW"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-023",
            "action_type":"REVIEW_RECORDED",
            "target_id":"RES-025",
            "timestamp":"2024-05-21T09:00:00Z",
            "details":"exception_review|applies=0|scope=RES-025|at=T0"
        })
    ],
    outputs=[
        '{"applying_exceptions": 0}',
        '{"ticket_subject":"NEGATIVE-FINDING|RES-025|EXCEPTIONS|T0=2024-05-21"}'
    ]
),


# - TASK 67 -
Task(
    annotator="0",
    user_id="067",
    instruction=(
        "You are Jeffery Green (U-023), Operations. Using T0=2024-05-21T09:00:00Z for all timestamps, verify whether any "
        "ACTIVE policy exceptions apply to production-web-server-1 (RES-025). An exception 'applies' iff its permission_id "
        "maps to a permission whose resource_id equals RES-025. If the applying-exception count is 0, raise an Operations "
        "ticket with subject 'NEGATIVE-FINDING|RES-025|EXCEPTIONS|T0=2024-05-21' and capture two audits with tokenized details: "
        "one for the exception review result and one for the ticket creation. Return the count and the ticket subject (if created)."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-023"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="list_policy_exceptions", kwargs={"status": "ACTIVE"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-021"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-022"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-029"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-070"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-096"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-108"}),
        Action(name="create_hubspot_ticket", kwargs={
            "subject": "NEGATIVE-FINDING|RES-025|EXCEPTIONS|T0=2024-05-21",
            "requester_id": "U-023",
            "category": "OPERATIONS"
        }),

        Action(name="create_audit_log", kwargs={
            "actor_id": "U-023",
            "action_type": "POLICY_EXCEPTION_REVIEWED",
            "target_ref": {"kind":"RESOURCE","id":"RES-025"},
            "timestamp": "2024-05-21T09:00:00Z",
            "details": "status=ACTIVE|apply_rule=permission.resource_id==RES-025|apply_count=0|T0=2024-05-21T09:00:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-023",
            "action_type": "TICKET_CREATED",
            "target_ref": {"kind":"RESOURCE","id":"RES-025"},
            "timestamp": "2024-05-21T09:00:00Z",
            "details": "subject=NEGATIVE-FINDING|RES-025|EXCEPTIONS|T0=2024-05-21|category=OPERATIONS|T0=2024-05-21T09:00:00Z"
        })
    ],
    outputs=[
        '[{"resource_id":"RES-025","exceptions_applying":0}]',
        '[{"ticket_subject":"NEGATIVE-FINDING|RES-025|EXCEPTIONS|T0=2024-05-21","category":"OPERATIONS"}]'
    ]
),


# - TASK 68 -
Task(
    annotator="0",
    user_id="068",
    instruction=(
        "You are Finance Lead (U-006). At T0=2024-05-20T17:00:00Z, approve the pending access request "
        "AR-008 for U-030 to receive finance-budget-admin (ROL-032) on RES-032 only if the role’s "
        "permissions reference RES-032. Capture evidence with canonical key=value tokens and close "
        "ticket TI-010 at T0."
    ),
    actions=[
        Action(name="get_access_request", kwargs={"request_id":"AR-008"}),
        Action(name="get_user_details", kwargs={"user_id":"U-030"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-030"}),
        Action(name="get_role_details", kwargs={"role_id":"ROL-032"}),
        Action(name="list_permissions_for_role", kwargs={"role_id":"ROL-032"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-032"}),
        Action(name="approve_access_request", kwargs={
            "request_id":"AR-008",
            "reviewer_id":"U-006",
            "decision_at":"2024-05-20T17:00:00Z"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id":"U-030",
            "role_id":"ROL-032",
            "assigned_by":"U-006",
            "assigned_on":"2024-05-20T17:00:00Z"
        }),
        Action(name="update_ticket_status", kwargs={
            "ticket_id":"TI-010",
            "status":"CLOSED",
            "updated_at":"2024-05-20T17:00:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-006",
            "action_type":"ACCESS_GRANTED",
            "target_id":"AR-008",
            "timestamp":"2024-05-20T17:00:00Z",
            "details":"actor=U-006|user=U-030|request=AR-008|role=ROL-032|resource=RES-032|ticket=TI-010|at=T0"
        })
    ],
    outputs=[
        '[{"approved_request_id":"AR-008","role_assigned":"ROL-032","user_id":"U-030","at":"2024-05-20T17:00:00Z"}]',
        '[{"ticket_id":"TI-010","status":"CLOSED","at":"2024-05-20T17:00:00Z"}]'
    ]
),

# - TASK 69 -
Task(
    annotator="0",
    user_id="069",
    instruction=(
        "You are Jessica Garcia (U-006), Finance. Deny PE-019 at T0=2025-08-06 16:30:00+00:00, export evidence (start_time=end_time=T0), and "
        "notify U-024 with subject='NOTICE:PE-019:DENIED', body='permission=P-088|subject=U-024|reviewed_on=2025-08-06 16:30:00+00:00|decision=DENIED', "
        "timestamp=T0. Return the updated exception."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-006"}),
        Action(name="get_policy_exception_details", kwargs={"exception_id":"PE-019"}),
        Action(name="get_user_details", kwargs={"user_id":"U-024"}),
        Action(name="deny_policy_exception", kwargs={
            "exception_id":"PE-019","reviewed_by":"U-006","reviewed_on":"2025-08-06 16:30:00+00:00"
        }),
        Action(name="export_audit_logs", kwargs={
            "actor_id":"U-006","action_type":"POLICY_EXCEPTION_DENIED","target_id":"PE-019",
            "start_time":"2025-08-06 16:30:00+00:00","end_time":"2025-08-06 16:30:00+00:00"
        }),
        Action(name="send_email", kwargs={
            "sender":"U-006","receiver":"U-024",
            "subject":"NOTICE:PE-019:DENIED",
            "body":"permission=P-088|subject=U-024|reviewed_on=2025-08-06 16:30:00+00:00|decision=DENIED",
            "timestamp":"2025-08-06 16:30:00+00:00"
        }),
        Action(name="get_policy_exception_details", kwargs={"exception_id":"PE-019"})
    ],
    outputs=[
        '{"exception_id":"PE-019","user_id":"U-024","reviewed_by":"U-006","reviewed_on":"2025-08-06 16:30:00+00:00","status":"DENIED"}'
    ]
),


# - TASK 70 -
Task(
    annotator="0",
    user_id="070",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. For RES-025, enforce the Owner Gate: reviewers outside Operations must not grant access. "
        "Treat submitted_at as decision time and document the decision with policy metadata "
        "(policy=OWNER_GATE|scope=RES-025|reviewer_dept=Engineering|request_id=AR-007|subject=U-029|decision=REJECTED). "
        "Export the matching audit window using start_time=end_time=decision_at. Return the processed request, the exported window, "
        "and the subject’s current roles."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-001"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-025"}),
        Action(name="get_user_details", kwargs={"user_id": "U-029"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
        Action(name="reject_access_request", kwargs={
            "request_id": "AR-007",
            "reviewer_id": "U-001",
            "decision_at": "2024-05-20 14:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-001",
            "action_type": "ACCESS_REJECTED",
            "target_id": "AR-007",
            "timestamp": "2024-05-20 14:00:00+00:00",
            "details": "policy=OWNER_GATE|scope=RES-025|reviewer_dept=Engineering|request_id=AR-007|subject=U-029|decision=REJECTED"
        }),
        Action(name="export_audit_logs", kwargs={
            "actor_id": "U-001",
            "action_type": "ACCESS_REJECTED",
            "target_id": "AR-007",
            "start_time": "2024-05-20 14:00:00+00:00",
            "end_time":   "2024-05-20 14:00:00+00:00"
        }),
        Action(name="get_user_roles", kwargs={"user_id": "U-029"})
    ],
    outputs=[
        '{'
        '"request":{"request_id":"AR-007","status":"REJECTED","reviewed_by":"U-001","decision_at":"2024-05-20 14:00:00+00:00"},'
        '"audit_export":{"start_time":"2024-05-20 14:00:00+00:00","end_time":"2024-05-20 14:00:00+00:00"},'
        '"roles":[{"role_id":"ROL-021","role_name":"operations-base","is_temporary":false}]'
        '}'
    ]
),


# - TASK 71 -
Task(
    annotator="0",
    user_id="071",
    instruction=(
        "You are Michael Davis (U-005), Operations. For RES-025, process the oldest eligible pending access under RBAC. "
        "If you are an authorized Operations reviewer and the request is eligible, approve at the request’s submitted_at "
        "(2024-05-20T14:00:00Z), assign the requested role ROL-026, and set a deterministic expiry exactly one year minus "
        "one second after the decision time (2025-05-20T13:59:59Z) with expiry_policy=EXPLICIT. Record compact evidence "
        "using canonical tokens and then confirm the requester’s roles."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-025"}),
        Action(name="get_user_details", kwargs={"user_id": "U-029"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
        Action(name="list_roles", kwargs={}),
        Action(name="search_logs", kwargs={"query": "AR-007"}),
        Action(name="search_logs", kwargs={"query": "RES-025"}),
        Action(name="approve_access_request", kwargs={
                "request_id": "AR-007",
                "reviewer_id": "U-005",
                "decision_at": "2024-05-20T14:00:00Z"
            }),
        Action(name="assign_role_to_user", kwargs={
                "user_id": "U-029",
                "role_id": "ROL-026",
                "assigned_by": "U-005",
                "assigned_on": "2024-05-20T14:00:00Z",
                "expires_on": "2025-05-20T13:59:59Z",
                "expiry_policy": "EXPLICIT"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-005",
                "action_type": "ACCESS_APPROVED",
                "target_ref": {"kind":"ACCESS_REQUEST","id":"AR-007"},
                "timestamp": "2024-05-20T14:00:00Z",
                "details": "request_id=AR-007|resource=RES-025|role=ROL-026|decision_at=2024-05-20T14:00:00Z|expires_on=2025-05-20T13:59:59Z"
            }),
        Action(name="get_user_roles", kwargs={"user_id": "U-029"}),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-005",
                "action_type": "EVIDENCE_CAPTURED",
                "target_ref": {"kind":"ACCESS_REQUEST","id":"AR-007"},
                "timestamp": "2024-05-20T14:00:00Z",
                "details": "pre_roles_checked|post_roles_confirmed"
            })
    ],
    outputs=[
        '[{"request_id":"AR-007","status":"APPROVED","decision_at":"2024-05-20T14:00:00Z"}]',
        '[{"user_id":"U-029","roles":["ROL-021","ROL-026"]}]'
    ]
),


# - TASK 72 -
Task(
    annotator="0",
    user_id="072",
    instruction=(
        "You are Jeffery Green (U-023), Operations. For production-web-server-1 (RES-025), apply the incident posture for access anomalies: "
        "treat HIGH or CRITICAL SIEM activity as unusual access; anchor all records to T0 = 2024-08-28 13:30:00+00:00. "
        "When unusual access applies, register a concise triage incident and an operations ticket, and emit canonical evidence at T0; "
        "otherwise, record the canonical no-issue evaluation at T0. Return the boolean unusual_access and, if created, the ticket subject."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-023"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="list_siem_alerts", kwargs={"resource_id": "RES-025", "severity_in": ["HIGH","CRITICAL"]}),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-023",
                "action_type": "RULE_EVALUATED",
                "target_ref": {"kind": "RESOURCE", "id": "RES-025"},
                "timestamp": "2024-08-28 13:30:00+00:00",
                "details": "rule=SIEM_ALERT(resource=RES-025,severity∈{HIGH,CRITICAL})|T0=2024-08-28 13:30:00+00:00"
            }),
        Action(name="create_incident_record", kwargs={
                "summary": "TRIAGE|RES-025|UNUSUAL-ACCESS|T0=2024-08-28",
                "created_by": "U-023",
                "timestamp": "2024-08-28 13:30:00+00:00"
            }),
        Action(name="create_hubspot_ticket", kwargs={
                "subject": "TRIAGE|RES-025|UNUSUAL-ACCESS|T0=2024-08-28",
                "requester_id": "U-023",
                "category": "OPERATIONS"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-023",
                "action_type": "INCIDENT_CREATED",
                "target_ref": {"kind": "RESOURCE", "id": "RES-025"},
                "timestamp": "2024-08-28 13:30:00+00:00",
                "details": "summary=TRIAGE|RES-025|UNUSUAL-ACCESS|T0=2024-08-28"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-023",
                "action_type": "TICKET_CREATED",
                "target_ref": {"kind": "RESOURCE", "id": "RES-025"},
                "timestamp": "2024-08-28 13:30:00+00:00",
                "details": "subject=TRIAGE|RES-025|UNUSUAL-ACCESS|T0=2024-08-28|category=OPERATIONS"
            })
    ],
    outputs=[
        '[{"resource_id":"RES-025","unusual_access":true}]',
        '[{"ticket_subject":"TRIAGE|RES-025|UNUSUAL-ACCESS|T0=2024-08-28","category":"OPERATIONS"}]'
    ]
),


# - TASK 73 -
Task(
    annotator="0",
    user_id="073",
    instruction=(
        "You are an HR operator (U-016). Onboard a new Sales user per policy using the onboarding cutover at "
        "2025-01-10T09:00:00Z and provision baseline Sales access on the Sales system (RES-017) via the standard "
        "request-and-approval path. Use request AR-042 reviewed by the Sales owner (U-003) at 2025-01-10T09:05:00Z, "
        "then reflect the assignment to ROL-011 with the same effective time and no expiry. Record minimal audit evidence. "
        "Return the created user’s identity summary (user_id, username, department, mfa_enabled) and the user’s resulting roles."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-016"}),
        Action(name="list_roles", kwargs={}),
        Action(name="create_user", kwargs={
                "user_id": "U-034",
                "username": "jsmith",
                "department": "Sales",
                "mfa_enabled": True,
                "created_at": "2025-01-10T09:00:00Z"
            }),
        Action(name="get_user_details", kwargs={"user_id": "U-034"}),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-016",
                "action_type": "USER_CREATED",
                "target_ref": {"kind":"USER","id":"U-034"},
                "details": "department=Sales|mfa=true|created_at=2025-01-10T09:00:00Z"
            }),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-017"}),
        Action(name="create_access_request", kwargs={
                "request_id": "AR-042",
                "requester_id": "U-016",
                "subject_id": "U-034",
                "resource_id": "RES-017",
                "role_id": "ROL-011",
                "submitted_at": "2025-01-10T09:00:00Z"
            }),
        Action(name="approve_access_request", kwargs={
                "request_id": "AR-042",
                "reviewer_id": "U-003",
                "decision_at": "2025-01-10T09:05:00Z"
            }),
        Action(name="assign_role_to_user", kwargs={
                "user_id": "U-034",
                "role_id": "ROL-011",
                "assigned_by": "U-003",
                "assigned_on": "2025-01-10T09:05:00Z",
                "expires_on": None,
                "expiry_policy": "NONE",
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-003",
                "action_type": "ACCESS_APPROVED",
                "target_ref": {"kind":"ACCESS_REQUEST","id":"AR-042"},
                "details": "role=ROL-011|resource=RES-017|decision_at=2025-01-10T09:05:00Z"
            }),
        Action(name="get_user_roles", kwargs={"user_id": "U-034"})
    ],
    outputs=[
        '[{"user_id":"U-034","username":"jsmith","department":"Sales","mfa_enabled":true}]',
        '[{"user_id":"U-034","roles":["ROL-011"]}]'
    ]
),


# - TASK 74 -
Task(
    annotator="0",
    user_id="074",
    instruction=(
        "You are John Brown (U-012), Finance. For RES-032, approve AR-008 from U-030 for ROL-032 at T0=2024-05-20T17:00:00Z, assign the role, close ticket TI-010, and record an immutable audit entry using canonical tokens."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-012"}),
        Action(name="get_access_request", kwargs={"request_id":"AR-008"}),
        Action(name="approve_access_request", kwargs={
            "request_id":"AR-008",
            "reviewer_id":"U-012",
            "decision_at":"2024-05-20T17:00:00Z"
        }),
        Action(name="assign_role_to_user", kwargs={
            "user_id":"U-030",
            "role_id":"ROL-032",
            "assigned_by":"U-012",
            "assigned_on":"2024-05-20T17:00:00Z"
        }),
        Action(name="update_ticket_status", kwargs={"ticket_id":"TI-010","status":"CLOSED","updated_at":"2024-05-20T17:00:00Z"}),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-012",
            "action_type":"ACCESS_GRANTED",
            "target_id":"AR-008",
            "timestamp":"2024-05-20T17:00:00Z",
            "details":"AR=AR-008|USER=U-030|ROLE=ROL-032|BY=U-012|AT=2024-05-20T17:00:00Z|TICKET=TI-010|STATUS=CLOSED"
        })
    ],
    outputs=[
        '[{"request_id":"AR-008","final_status":"APPROVED"}]',
        '[{"role_assignment":{"user_id":"U-030","role_id":"ROL-032"}}]',
        '[{"ticket_id":"TI-010","status":"CLOSED"}]'
    ]
),

# - TASK 75 -
Task(
    annotator="0",
    user_id="075",
    instruction=(
        "You are Michael Davis (U-005), Operations. Under certification governance, finalize Certification C-013 for "
        "RES-040 at T0=2025-08-18T18:10:00Z and evidence the state transition using only canonical IDs and T0. Notify the "
        "resource owner via email using pipe-formatted tokens. No Slack posts or log exports. Return the updated "
        "certification state, the immutable audit details, and the notification subject."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-005"}),
        Action(name="get_certification_details", kwargs={"certification_id":"C-013"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-040"}),
        Action(name="get_audit_logs_for_target", kwargs={"target_id":"C-013"}),
        Action(name="update_certification_status", kwargs={
                "certification_id":"C-013",
                "status":"COMPLETED",
                "completed_on":"2025-08-18T18:10:00Z"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-005",
                "action_type":"CERTIFICATION_STATUS_UPDATED",
                "target_id":"C-013",
                "timestamp":"2025-08-18T18:10:00Z",
                "details":"CERT:C-013|RES:RES-040|STATUS:COMPLETED|BY:U-005|AT:2025-08-18T18:10:00Z"
            }),
        Action(name="send_email", kwargs={
                "sender":"U-005",
                "receiver":"U-005",
                "subject":"NOTICE|CERT:C-013|STATUS:COMPLETED|AT:2025-08-18T18:10:00Z",
                "body":"CERT:C-013|RES:RES-040|STATUS:COMPLETED|BY:U-005|AT:2025-08-18T18:10:00Z",
                "timestamp":"2025-08-18T18:10:00Z"
            })
    ],
    outputs=[
        '[{"certification_id":"C-013","new_status":"COMPLETED","completed_on":"2025-08-18T18:10:00Z"}]',
        '[{"audit_details":"CERT:C-013|RES:RES-040|STATUS:COMPLETED|BY:U-005|AT:2025-08-18T18:10:00Z"}]',
        '[{"email_subject":"NOTICE|CERT:C-013|STATUS:COMPLETED|AT:2025-08-18T18:10:00Z"}]'
    ]
),



# - TASK 76 -
Task(
    annotator="0",
    user_id="076",
    instruction=(
        "You are SYS-AUDIT. You must perform read-only evidence capture for certification C-002 on employee-data-portal "
        "(RES-020) because the assigned reviewer Emily Jones (U-004) is SUSPENDED. Do not change certification status. "
        "Collect roles/sessions/logs context, open a reassignment ticket to route C-002 to Operations (proposed U-005), "
        "and record the following canonical audits at T0=2024-10-10T16:00:00Z: EVIDENCE_CAPTURED, TICKET_CREATED, "
        "REASSIGNMENT_REQUESTED, CERT_REVIEW_NO_ACTION."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-004"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-020"}),
        Action(name="get_certification_details", kwargs={"certification_id":"C-002"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-004"}),
        Action(name="list_sessions", kwargs={"user_id":"U-004","active_only":True}),
        Action(name="search_logs", kwargs={"query":"C-002 RES-020"}),
        Action(name="get_user_details", kwargs={"user_id":"U-005"}),
        Action(name="create_hubspot_ticket", kwargs={
            "subject":"REASSIGN|C-002|RES-020",
            "requester_id":"SYS-AUDIT"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"SYS-AUDIT",
            "action_type":"EVIDENCE_CAPTURED",
            "target_ref":{"kind":"OBJECT","id":"C-002"},
            "timestamp":"2024-10-10T16:00:00Z",
            "details":"executed_by=SYS-AUDIT|assigned_reviewer=U-004|assigned_reviewer_status=SUSPENDED|resource=RES-020|action_scope=READ_ONLY|state_change=false"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"SYS-AUDIT",
            "action_type":"TICKET_CREATED",
            "target_ref":{"kind":"RESOURCE","id":"RES-020"},
            "timestamp":"2024-10-10T16:00:00Z",
            "details":"subject=REASSIGN|C-002|RES-020"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"SYS-AUDIT",
            "action_type":"REASSIGNMENT_REQUESTED",
            "target_ref":{"kind":"OBJECT","id":"C-002"},
            "timestamp":"2024-10-10T16:00:00Z",
            "details":"ticket_subject=REASSIGN|C-002|RES-020|proposed_new_reviewer=U-005"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"SYS-AUDIT",
            "action_type":"CERT_REVIEW_NO_ACTION",
            "target_ref":{"kind":"OBJECT","id":"C-002"},
            "timestamp":"2024-10-10T16:00:00Z",
            "details":"reason=REVIEWER_SUSPENDED|resource=RES-020|state_change=false"
        })
    ],
    outputs=[
        '[{"certification_id":"C-002","status":"COMPLETED","review_action":"NO_CHANGE"}]',
        '[{"ticket_subject":"REASSIGN|C-002|RES-020"}]'
    ]
),

# - TASK 77 -
Task(
    annotator="0",
    user_id="077",
    instruction=(
        "You are Jessica Garcia (U-006), Finance. Under intake management for RES-034, AR-034 is DEFERRED at 2024-05-30 15:10:00+00:00. "
        "Operate under requester eligibility and role-catalog conformance, capture a single deferral audit annotated with updated_at, and "
        "return the DEFERRED requests for RES-034."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-006"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-034"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-034"}),
        Action(name="get_user_details", kwargs={"user_id": "U-018"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-030"}),
        Action(name="update_access_request", kwargs={
            "request_id": "AR-034",
            "status": "DEFERRED",
            "updated_on": "2024-05-30 15:10:00+00:00",
            "updated_by": "U-006"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-006",
            "action_type": "ACCESS_DEFERRED",
            "target_id": "AR-034",
            "timestamp": "2024-05-30 15:10:00+00:00",
            "details": "resource=RES-034|decision=DEFERRED|updated_at=2024-05-30 15:10:00+00:00"
        }),
        Action(name="list_access_requests", kwargs={"status": "DEFERRED", "resource_id": "RES-034"})
    ],
    outputs=[
        '[{"request_id":"AR-034","user_id":"U-018","resource_id":"RES-034","requested_role_id":"ROL-030","status":"DEFERRED"}]'
    ]
),

# - TASK 78 -
Task(
    annotator="0",
    user_id="062",
    instruction=(
        "You are Nicole Thomas (U-014). Resolve a SoD conflict for U-026 by removing role ROL-007 at T0=2025-08-08 13:00:00+00:00. "
        "Record evidence with details 'policy=SOD|actor=U-014|role=ROL-007|subject=U-026' and export using start_time=end_time=T0. "
        "Notify U-026 deterministically with subject='NOTICE:ROLE_REMOVED', "
        "body='policy=SOD|role=ROL-007|subject=U-026|t=T0', timestamp=T0. Return U-026’s roles after the change."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-014"}),
        Action(name="get_user_details", kwargs={"user_id":"U-026"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-026"}),
        Action(name="remove_role_from_user", kwargs={"user_id":"U-026","role_id":"ROL-007"}),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-014","action_type":"ROLE_REMOVED","target_id":"U-026",
            "timestamp":"2025-08-08 13:00:00+00:00",
            "details":"policy=SOD|actor=U-014|role=ROL-007|subject=U-026"
        }),
        Action(name="export_audit_logs", kwargs={
            "actor_id":"U-014","action_type":"ROLE_REMOVED","target_id":"U-026",
            "start_time":"2025-08-08 13:00:00+00:00","end_time":"2025-08-08 13:00:00+00:00"
        }),
        Action(name="send_email", kwargs={
            "sender":"U-014","receiver":"U-026",
            "subject":"NOTICE:ROLE_REMOVED",
            "body":"policy=SOD|role=ROL-007|subject=U-026|t=T0",
            "timestamp":"2025-08-08 13:00:00+00:00"
        }),
        Action(name="get_user_roles", kwargs={"user_id":"U-026"})
    ],
    outputs=[
        '[{"role_id":"ROL-006","role_name":"marketing-base","is_temporary":false},'
        '{"role_id":"ROL-010","role_name":"marketing-content-editor","is_temporary":false}]'
    ]
),



# - TASK 79 -
Task(
    annotator="0",
    user_id="079",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. Enforce the end of AR-014 by revoking ROL-003 from U-025 on RES-025 at 2024-05-23T16:46:10Z. Confirm the user currently holds the role before revocation. Record a single evidence audit with canonical tokens at 2024-05-23T16:46:10Z, and open a follow-up ticket with subject 'FOLLOWUP|TEMP-ACCESS-END|AR-014|U-025|RES-025' using category ACCESS_REVIEW and a deterministic description; assign the ticket to the RES-025 owner."
    ),
    actions=[
        Action(name="get_user_roles", kwargs={"user_id":"U-025"}),
        Action(name="revoke_role", kwargs={"user_id":"U-025","role_id":"ROL-003"}),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-001",
            "action_type":"ROLE_REVOKE_EVIDENCE",
            "target_id":"U-025",
            "timestamp":"2024-05-23T16:46:10Z",
            "details":"AR=AR-014|USER=U-025|ROLE=ROL-003|STATUS=REVOKED|AT=2024-05-23T16:46:10Z|RESOURCE=RES-025|BY=U-001"
        }),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-025"}),
        Action(name="create_hubspot_ticket", kwargs={
            "subject":"FOLLOWUP|TEMP-ACCESS-END|AR-014|U-025|RES-025",
            "description":"scope=RES-025|source=AR-014|at=2024-05-23T16:46:10Z",
            "requester_id":"U-001",
            "assignee_id":"U-005",
            "category":"ACCESS_REVIEW"
        })
    ],
    outputs=[
        '[{"ticket_subject":"FOLLOWUP|TEMP-ACCESS-END|AR-014|U-025|RES-025"}]'
    ]
),


# - TASK 80 -
Task(
    annotator="0",
    user_id="080",
    instruction=(
        "You are Jessica Garcia (U-006), Finance and owner of RES-034. Under Finance access-governance, resolve AR-034 for RES-034 "
        "to APPROVED with decision_at=2024-05-30 15:00:00+00:00. Decisions must honor role-catalog conformance and requester eligibility. "
        "Record one approval audit reflecting request_id, resource_id, role_id, decision, and decision_at, then report the APPROVED requests for RES-034."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-006"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-034"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-034"}),
        Action(name="get_user_details", kwargs={"user_id": "U-018"}),  # requester eligibility context
        Action(name="get_role_details", kwargs={"role_id": "ROL-030"}),  # role-catalog conformance
        Action(name="list_permissions_for_role", kwargs={"role_id": "ROL-030"}),
        Action(name="approve_access_request", kwargs={
            "request_id": "AR-034",
            "reviewer_id": "U-006",
            "decision_at": "2024-05-30 15:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-006",
            "action_type": "ACCESS_APPROVED",
            "target_id": "AR-034",
            "timestamp": "2024-05-30 15:00:00+00:00",
            "details": "resource=RES-034|role=ROL-030|decision=APPROVED|decision_at=2024-05-30 15:00:00+00:00"
        }),
        Action(name="list_access_requests", kwargs={"status": "APPROVED", "resource_id": "RES-034"})
    ],
    outputs=[
        '[{"request_id":"AR-034","user_id":"U-018","resource_id":"RES-034","requested_role_id":"ROL-030","status":"APPROVED","decision_at":"2024-05-30 15:00:00+00:00","reviewed_by":"U-006"}]'
    ]
),


# - TASK 81 -
Task(
    annotator="0",
    user_id="081",
    instruction=(
        "You are Stephanie Adams (U-018), Finance. Apply the Finance MFA Control at review instant T0=2025-08-07 16:00:00+00:00: "
        "if an ACTIVE Finance user lacks MFA and holds no ACTIVE exception, you must set MFA=true at T0. Evidence must include a "
        "SOX audit record (policy=FINANCE_MFA_CONTROL|actor=U-018|subject=<UID>|outcome=<ENFORCED|NO_ACTION>) and an export window "
        "exactly matching T0 (start_time=end_time=T0). When you enforce MFA for any subject, open one compliance ticket with "
        "subject='FINANCE_MFA_ENFORCED|subject=<UID>|t=T0', description='policy=FINANCE_MFA_CONTROL|actor=U-018|subject=<UID>|t=T0', "
        "category=COMPLIANCE_AUDIT and priority=P3. Return ACTIVE Finance users with MFA and include the ticket if one was opened."
    ),
    actions=[
        Action(name="list_users", kwargs={"department": "Finance", "status": "ACTIVE"}),
        Action(name="get_user_details", kwargs={"user_id": "U-024"}),
        Action(name="list_policy_exceptions", kwargs={"user_id": "U-024", "status": "ACTIVE"}),
        Action(name="update_user_status", kwargs={"user_id": "U-024", "mfa_enabled": True, "updated_by": "U-018"}),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-018",
            "action_type": "MFA_ENFORCED",
            "target_id": "U-024",
            "timestamp": "2025-08-07 16:00:00+00:00",
            "details": "policy=FINANCE_MFA_CONTROL|actor=U-018|subject=U-024|outcome=ENFORCED"
        }),
        Action(name="export_audit_logs", kwargs={
            "actor_id": "U-018",
            "action_type": "MFA_ENFORCED",
            "target_id": "U-024",
            "start_time": "2025-08-07 16:00:00+00:00",
            "end_time":   "2025-08-07 16:00:00+00:00"
        }),
        Action(name="create_hubspot_ticket", kwargs={
            "subject": "FINANCE_MFA_ENFORCED|subject=U-024|t=2025-08-07 16:00:00+00:00",
            "description": "policy=FINANCE_MFA_CONTROL|actor=U-018|subject=U-024|t=2025-08-07 16:00:00+00:00",
            "requester_id": "U-018",
            "assignee_id": "U-018",
            "category": "COMPLIANCE_AUDIT",
            "priority": "P3"
        }),
        Action(name="list_users", kwargs={"department": "Finance", "status": "ACTIVE", "mfa_enabled": True})
    ],
    outputs=[
        '['
        '{"user_id":"U-006","mfa_enabled":true},'
        '{"user_id":"U-012","mfa_enabled":true},'
        '{"user_id":"U-018","mfa_enabled":true},'
        '{"user_id":"U-024","mfa_enabled":true},'
        '{"ticket_id":"TI-054","subject":"FINANCE_MFA_ENFORCED|subject=U-024|t=2025-08-07 16:00:00+00:00","category":"COMPLIANCE_AUDIT"}'
        ']'
    ]
),


# - TASK 82 -
Task(
    annotator="0",
    user_id="082",
    instruction=(
        "You are Alex Johnson (U-001), Engineering. Apply RBAC hardening for HR_ONBOARD_BOT (U-032) per IAM policy: "
        "treat membership in ROL-041 for U-032 as excess and revoke it, enforce MFA for U-032, and capture IAM "
        "evidence using the canonical schema string 'IAM_WINDOW:2025-06-01T00:00:00Z..2025-08-18T15:20:00Z' in both "
        "ticket description and audit log. File an RBAC ticket to yourself and record an immutable audit entry. "
        "Use T0=2025-08-18T15:20:00Z."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-001"}),
        Action(name="get_role_details", kwargs={"role_id":"ROL-041"}),
        Action(name="get_role_members", kwargs={"role_id":"ROL-041"}),
        Action(name="list_permissions_for_role", kwargs={"role_id":"ROL-041"}),
        Action(name="remove_role_from_user", kwargs={"user_id":"U-032","role_id":"ROL-041"}),
        Action(name="enable_user_mfa", kwargs={"user_id":"U-032"}),
        Action(name="audit_iam_access", kwargs={
            "start_time":"2025-06-01T00:00:00Z",
            "end_time":"2025-08-18T15:20:00Z"
        }),
        Action(name="create_hubspot_ticket", kwargs={
            "subject":"RBAC|U-032|ROL-041_REMOVED|MFA_ENABLED",
            "description":"T0=2025-08-18T15:20:00Z|TARGET=U-032|ROLE=ROL-041|MFA=ENABLED|IAM_WINDOW:2025-06-01T00:00:00Z..2025-08-18T15:20:00Z",
            "requester_id":"U-001",
            "assignee_id":"U-001",
            "category":"RBAC"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-001",
            "action_type":"ROLE_AND_MFA_UPDATE",
            "target_id":"U-032",
            "timestamp":"2025-08-18T15:20:00Z",
            "details":"USER:U-032|ROLE_REMOVED:ROL-041|MFA:ENABLED|IAM_WINDOW:2025-06-01T00:00:00Z..2025-08-18T15:20:00Z|BY:U-001|AT:2025-08-18T15:20:00Z"
        })
    ],
    outputs=[
        '[{"user_id":"U-032","role_removed":"ROL-041","mfa_enabled":true}]',
        '[{"ticket_subject":"RBAC|U-032|ROL-041_REMOVED|MFA_ENABLED"}]',
        '[{"audit_details":"USER:U-032|ROLE_REMOVED:ROL-041|MFA:ENABLED|IAM_WINDOW:2025-06-01T00:00:00Z..2025-08-18T15:20:00Z|BY:U-001|AT:2025-08-18T15:20:00Z"}]'
    ]
),


# - TASK 83 -
Task(
    annotator="0",
    user_id="083",
    instruction=(
        "You are Jeffery Green (U-023), Operations. Under the Exceptions Management policy, confirm whether any ACTIVE "
        "exceptions apply to production-web-server-1 (RES-025) for the scoped permissions P-021, P-022, and P-029. "
        "If none apply, record a negative-finding audit and create both a tracking ticket and a LOW-severity follow-up "
        "incident. Use evidencing anchor T0=2025-08-07T00:00:00Z and canonical audit tokens; do not introduce free text."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-023"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="list_policy_exceptions", kwargs={"status": "ACTIVE"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-021"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-022"}),
        Action(name="get_permission_details", kwargs={"permission_id": "P-029"}),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-023",
                "action_type":"POLICY_EXCEPTION_REVIEWED",
                "target_ref": {"kind":"RESOURCE","id":"RES-025"},
                "timestamp":"2025-08-07T00:00:00Z",
                "details":"active_exception_matches=0|scope_permissions=P-021,P-022,P-029"
            }),
        Action(name="create_hubspot_ticket", kwargs={
                "subject":"NEGATIVE-FINDING|RES-025|EXCEPTIONS",
                "requester_id":"U-023"
            }),
        Action(name="create_incident_record", kwargs={
                "severity":"LOW",
                "summary":"NEGATIVE-FINDING|RES-025|EXCEPTIONS",
                "created_by":"U-023",
                "timestamp":"2025-08-07T00:00:00Z"
            }),
    ],
    outputs=[
        '[{"resource_id":"RES-025","exceptions_applying":0}]',
        '[{"ticket_subject":"NEGATIVE-FINDING|RES-025|EXCEPTIONS"}]',
        '[{"incident_title":"NEGATIVE-FINDING|RES-025|EXCEPTIONS","severity":"LOW"}]'
    ]
),


# - TASK 84 -
Task(
    annotator="0",
    user_id="084",
    instruction=(
        "You are Robert White (U-017), Operations (pending access). Conduct a readiness review for network-firewall-main (RES-027). "
        "Provide SoD attestation and a readiness attestation at T0=2024-05-29T13:31:00Z, capture objective evidence "
        "(roles, sessions, requests) at T0 and T0+10s, and establish a LOW-severity follow-up incident and a tracking ticket."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-017"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-017"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-027"}),
        Action(name="list_access_requests", kwargs={"resource_id":"RES-027"}),
        Action(name="list_sessions", kwargs={"user_id":"U-017","active_only":True}),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-017",
                "action_type":"SOD_CHECK",
                "target_ref": {"kind":"RESOURCE","id":"RES-027"},
                "timestamp":"2024-05-29T13:31:00Z",
                "details":"subject=U-017|scope=RES-027|conflicts=None"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-017",
                "action_type":"READINESS_REVIEW_RECORDED",
                "target_ref": {"kind":"RESOURCE","id":"RES-027"},
                "timestamp":"2024-05-29T13:31:00Z",
                "details":"summary=READINESS|RES-027"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-017",
                "action_type":"EVIDENCE_CAPTURED",
                "target_ref": {"kind":"RESOURCE","id":"RES-027"},
                "timestamp":"2024-05-29T13:31:10Z",
                "details":"roles|sessions|requests"
            }),
        Action(name="create_incident_record", kwargs={
                "severity":"LOW",
                "summary":"READINESS|RES-027",
                "created_by":"U-017",
                "timestamp":"2024-05-29T13:31:00Z"
            }),
        Action(name="create_hubspot_ticket", kwargs={
                "subject":"FOLLOWUP|READINESS|RES-027",
                "requester_id":"U-017"
            }),
    ],
    outputs=[
        '[{"asset":"RES-027","readiness_audit":"RECORDED"}]',
        '[{"incident_title":"READINESS|RES-027","severity":"LOW"}]',
        '[{"ticket_subject":"FOLLOWUP|READINESS|RES-027"}]'
    ]
),


# - TASK 85 -
Task(
    annotator="0",
    user_id="085",
    instruction=(
        "You are Michael Davis (U-005), Operations. Following deletion-risk indicators on RES-027, enforce containment by revoking "
        "temporary elevation ROL-003 from U-025, record SoD and containment evidence, and open a post-mortem tracking ticket. "
        "Use concise, policy-aligned tokens."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-005"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-027"}),
        Action(name="get_user_details", kwargs={"user_id":"U-025"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-025"}),
        Action(name="revoke_role", kwargs={"user_id":"U-025","role_id":"ROL-003"}),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-005",
                "action_type":"ROLE_REVOKED",
                "target_ref": {"kind":"USER","id":"U-025"},
                "details":"role_id=ROL-003|resource=RES-027|reason=CONTAINMENT"
            }),
        Action(name="get_user_roles", kwargs={"user_id":"U-025"}),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-005",
                "action_type":"SOD_CHECK",
                "target_ref": {"kind":"USER","id":"U-025"},
                "details":"reviewer=U-005|subject=U-025|scope=RES-027|conflicts=None"
            }),
        Action(name="create_hubspot_ticket", kwargs={
                "subject":"POST-MORTEM|RES-027|TEMP-ROLE-CONTAINMENT|U-025",
                "requester_id":"U-005"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-005",
                "action_type":"TICKET_CREATED",
                "target_ref": {"kind":"RESOURCE","id":"RES-027"},
                "details":"subject=POST-MORTEM|RES-027|TEMP-ROLE-CONTAINMENT|U-025"
            }),
    ],
    outputs=[
        '[{"user_id":"U-025","roles":["ROL-001"]}]',
        '[{"ticket_subject":"POST-MORTEM|RES-027|TEMP-ROLE-CONTAINMENT|U-025"}]'
    ]
),


# - TASK 86 -
Task(
    annotator="0",
    user_id="086",
    instruction=(
        "You are Jeffery Green (U-023), Operations. Prepare the RES-025 quarterly access recertification by gathering objective evidence (requests, roles, active exceptions) and creating tracking artifacts. Anchor all time-stamped records at T0=2025-06-30T17:00:00Z and use canonical audit tokens."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-023"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-025"}),
        Action(name="list_access_requests", kwargs={"resource_id":"RES-025"}),
        Action(name="list_roles", kwargs={}),
        Action(name="list_policy_exceptions", kwargs={"status":"ACTIVE"}),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-023",
            "action_type":"EVIDENCE_CAPTURED",
            "target_id":"RES-025",
            "timestamp":"2025-06-30T17:00:00Z",
            "details":"scope=RES-025|artifacts=requests,roles,exceptions|at=T0"
        }),
        Action(name="create_incident_record", kwargs={
            "timestamp":"2025-06-30T17:00:00Z",
            "created_by":"U-023",
            "summary":"RECERT|RES-025|PREP",
            "linked_resources":["RES-025"]
        }),
        Action(name="create_hubspot_ticket", kwargs={
            "subject":"RECERT|RES-025|ACTION-ITEMS",
            "description":"scope=RES-025|type=RECERTIFICATION|at=T0",
            "requester_id":"U-023",
            "assignee_id":"U-005",
            "category":"RECERTIFICATION"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-023",
            "action_type":"TICKET_CREATED",
            "target_id":"RES-025",
            "timestamp":"2025-06-30T17:00:00Z",
            "details":"subject=RECERT|RES-025|ACTION-ITEMS|assignee=U-005|category=RECERTIFICATION"
        })
    ],
    outputs=[
        '[{"incident_title":"RECERT|RES-025|PREP"}]',
        '[{"ticket_subject":"RECERT|RES-025|ACTION-ITEMS"}]'
    ]
),


# - TASK 87 -
Task(
    annotator="0",
    user_id="087",
    instruction=(
        "You are Michael Davis (U-005), Operations. Apply account-security enforcement for U-002 consistent with SoD "
        "and IAM policy: ensure MFA enforcement is compatible with current role holdings, confirm no active policy "
        "exceptions conflict with MFA, evidence the control window using the canonical schema string "
        "'IAM_WINDOW:2025-06-01T00:00:00Z..2025-08-18T16:10:00Z' in both ticket and audit entries, and maintain an "
        "immutable record. Open the ticket to yourself. Use T0=2025-08-18T16:10:00Z."
    ),
    actions=[
        # Identity & SoD-oriented review evidence
        Action(name="get_user_details", kwargs={"user_id":"U-005"}),
        Action(name="get_user_details", kwargs={"user_id":"U-002"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-002"}),

        # Confirm no conflicting exceptions for U-002 before enforcement
        Action(name="list_policy_exceptions", kwargs={"status":"APPROVED","user_id":"U-002"}),

        # Session hygiene and enforcement
        Action(name="list_user_sessions", kwargs={"user_id":"U-002","active_only":True}),
        Action(name="enable_user_mfa", kwargs={"user_id":"U-002"}),

        # Evidence window capture (IAM)
        Action(name="audit_iam_access", kwargs={
            "start_time":"2025-06-01T00:00:00Z",
            "end_time":"2025-08-18T16:10:00Z"
        }),

        # Ticket and immutable audit, pipe-formatted & deterministic
        Action(name="create_hubspot_ticket", kwargs={
            "subject":"ACCOUNT_SECURITY|U-002|MFA_ENABLED",
            "description":"T0=2025-08-18T16:10:00Z|TARGET=U-002|MFA=ENFORCED|ACTIVE_SESSIONS:0|SOD_REVIEW:APPLIED|EXCEPTIONS_CHECK:U-002|IAM_WINDOW:2025-06-01T00:00:00Z..2025-08-18T16:10:00Z",
            "requester_id":"U-005",
            "assignee_id":"U-005",
            "category":"ACCOUNT_SECURITY"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-005",
            "action_type":"USER_MFA_ENABLED",
            "target_id":"U-002",
            "timestamp":"2025-08-18T16:10:00Z",
            "details":"USER:U-002|MFA:ENFORCED|ACTIVE_SESSIONS:0|SOD_REVIEW:APPLIED|EXCEPTIONS_CHECK:U-002|IAM_WINDOW:2025-06-01T00:00:00Z..2025-08-18T16:10:00Z|BY:U-005|AT:2025-08-18T16:10:00Z"
        })
    ],
    outputs=[
        '[{"user_id":"U-002","mfa_enforced":true,"active_sessions_verified":0}]',
        '[{"ticket_subject":"ACCOUNT_SECURITY|U-002|MFA_ENABLED"}]',
        '[{"audit_details":"USER:U-002|MFA:ENFORCED|ACTIVE_SESSIONS:0|SOD_REVIEW:APPLIED|EXCEPTIONS_CHECK:U-002|IAM_WINDOW:2025-06-01T00:00:00Z..2025-08-18T16:10:00Z|BY:U-005|AT:2025-08-18T16:10:00Z"}]'
    ]
),


# - TASK 88 -
Task(
    annotator="0",
    user_id="088",
    instruction=(
        "You are Michael Davis (U-005), Operations. Grant ROL-028 to U-017 for RES-026 with assigned_on=2025-08-06 14:00:00+00:00 and expires_on=2025-12-31 00:00:00+00:00. "
        "Record one grant evidence entry using key=value tokens. "
        "Provide: assignment, audit_log, user_roles_after (U-017), role_meta (ROL-028), role_scope_summary (ROL-028), role_membership_after (ROL-028), audit_slices (U-017, ROL-028, RES-026), active_exceptions_for_user."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-005"}),                                   # 1
        Action(name="get_user_details", kwargs={"user_id":"U-017"}),                                   # 2
        Action(name="get_user_roles", kwargs={"user_id":"U-017"}),                                     # 3
        Action(name="get_role_details", kwargs={"role_id":"ROL-028"}),                                 # 4
        Action(name="get_resource_details", kwargs={"resource_id":"RES-026"}),                         # 5
        Action(name="assign_role_to_user", kwargs={"user_id":"U-017","role_id":"ROL-028","assigned_by":"U-005","assigned_on":"2025-08-06 14:00:00+00:00","expires_on":"2025-12-31 00:00:00+00:00"}), # 6
        Action(name="create_audit_log", kwargs={"actor_id":"U-005","action_type":"ACCESS_GRANTED","target_id":"U-017","timestamp":"2025-08-06 14:00:00+00:00","details":"role=ROL-028|policy_resource=RES-026|expires=2025-12-31 00:00:00+00:00"}), # 7
        Action(name="get_user_roles", kwargs={"user_id":"U-017"}),                                     # 8
        Action(name="get_role_members", kwargs={"role_id":"ROL-028"}),                                 # 9
        Action(name="get_audit_logs_for_target", kwargs={"target_id":"U-017"}),                        # 10
        Action(name="get_audit_logs_for_target", kwargs={"target_id":"ROL-028"}),                      # 11
        Action(name="get_audit_logs_for_target", kwargs={"target_id":"RES-026"}),                      # 12
        Action(name="list_policy_exceptions", kwargs={"user_id":"U-017","status":"ACTIVE"}),           # 13
        Action(name="list_permissions_for_role", kwargs={"role_id":"ROL-028"}),                        # 14
    ],
    outputs=[
        '{"assignment":{"user_id":"U-017","role_id":"ROL-028","assigned_by":"U-005","assigned_on":"2025-08-06 14:00:00+00:00","expires_on":"2025-12-31 00:00:00+00:00"},"audit_log":{"actor_id":"U-005","action_type":"ACCESS_GRANTED","target_id":"U-017","timestamp":"2025-08-06 14:00:00+00:00","details":"role=ROL-028|policy_resource=RES-026|expires=2025-12-31 00:00:00+00:00"},"user_roles_after":[{"role_id":"ROL-021"},{"role_id":"ROL-022"},{"role_id":"ROL-024"},{"role_id":"ROL-028"}],"role_meta":{"role_id":"ROL-028","role_name":"operations-network-admin","description":"Administrative access to all operations network infrastructure.","is_temporary":true},"role_scope_summary":{"role_id":"ROL-028","permission_ids":["P-066","P-067","P-091"],"resource_ids":["RES-026"]},"role_membership_after":["U-017"],"audit_slices":{"user_target":"U-017","role_target":"ROL-028","resource_target":"RES-026"},"active_exceptions_for_user":["PE-020"]}'
    ],
),


# - TASK 89 -
Task(
    annotator="0",
    user_id="089",
    instruction=(
        "You are Lisa Anderson (U-012), owner of RES-032. Owner review requires denial when the requester is not ACTIVE at the decision instant. "
        "For AR-008, the applicable instant is 2024-05-20 15:00:00+00:00 and requester U-030 was not ACTIVE, so the request does not qualify. "
        "Issue a deterministic notice to the requester with subject='NOTICE:AR-008:REJECTED' and "
        "body='reason=REQUESTER_NOT_ACTIVE|resource=RES-032|decision_at=2024-05-20 15:00:00+00:00'. "
        "Return Marisa’s current roles as reflected by canonical membership."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-012"}),
        Action(name="get_access_request", kwargs={"request_id":"AR-008"}),
        Action(name="get_user_details", kwargs={"user_id":"U-030"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-032"}),
        Action(name="reject_access_request", kwargs={
            "request_id":"AR-008","reviewer_id":"U-012","decision_at":"2024-05-20 15:00:00+00:00"
        }),
        Action(name="send_email", kwargs={
            "sender":"U-012","receiver":"U-030",
            "subject":"NOTICE:AR-008:REJECTED",
            "body":"reason=REQUESTER_NOT_ACTIVE|resource=RES-032|decision_at=2024-05-20 15:00:00+00:00",
            "timestamp":"2024-05-20 15:00:00+00:00"
        }),
        Action(name="get_user_roles", kwargs={"user_id":"U-030"})
    ],
    outputs=[
        '[{"role_id":"ROL-029"}]'
    ]
),


# - TASK 90 -
Task(
    annotator="0",
    user_id="090",
    instruction=(
        "You are Operations (U-023). Prepare the RES-025 quarterly recertification package at "
        "T0=2025-06-30T17:00:00Z using canonical key=value tokens. Create the tracking artifacts "
        "required by policy: (1) a single immutable evidence log at T0 summarizing all access "
        "requests, roles, and confirming zero active exceptions for RES-025 in the canonical format "
        "scope=RES-025|requests_scope=ALL|roles_scope=ALL|active_exception_matches=0|at=T0, and "
        "(2) one action-items ticket with subject 'RECERT|RES-025|ACTION-ITEMS' assigned to the "
        "RES-025 owner (U-005) and category=RECERTIFICATION."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-023"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-025"}),
        Action(name="list_access_requests", kwargs={"resource_id":"RES-025"}),
        Action(name="list_roles", kwargs={}),
        Action(name="list_policy_exceptions", kwargs={"status":"ACTIVE"}),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-023",
            "action_type":"EVIDENCE_CAPTURED",
            "target_id":"RES-025",
            "timestamp":"2025-06-30T17:00:00Z",
            "details":"scope=RES-025|requests_scope=ALL|roles_scope=ALL|active_exception_matches=0|at=T0"
        }),
        Action(name="create_hubspot_ticket", kwargs={
            "subject":"RECERT|RES-025|ACTION-ITEMS",
            "requester_id":"U-023",
            "assignee_id":"U-005",
            "category":"RECERTIFICATION"
        })
    ],
    outputs=[
        '[{"evidence_log":"scope=RES-025|requests_scope=ALL|roles_scope=ALL|active_exception_matches=0|at=T0"}]',
        '[{"ticket_subject":"RECERT|RES-025|ACTION-ITEMS","assignee_id":"U-005","category":"RECERTIFICATION"}]'
    ]
),


# - TASK 91 -
Task(
    annotator="0",
    user_id="091",
    instruction=(
        "You are Operations (U-005). Establish post-approval guardrails for RES-025 by capturing objective evidence and opening a monitoring ticket. "
        "Do not change any access states. Use T0=2024-05-21T09:00:00Z for all timestamps you write. "
        "Evidence must include: (a) the latest APPROVED access request for RES-025 with decision_at ≤ T0 and (b) that request’s user's current role set, "
        "exactly as the system records it (no additions or omissions). Return both artifacts and the monitoring ticket."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-025"}),
        Action(name="list_access_requests", kwargs={
                "status": "APPROVED",
                "resource_id": "RES-025"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-005",
                "action_type": "REQUESTS_FILTERED",
                "target_id": "RES-025",
                "timestamp": "2024-05-21T09:00:00Z",
                "details": "status=APPROVED|decision_at<=2024-05-21T09:00:00Z"
            }),
        Action(name="get_access_request", kwargs={"request_id": "AR-001"}),
        Action(name="get_user_details", kwargs={"user_id": "U-007"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-007"}),
        Action(name="create_hubspot_ticket", kwargs={
                "subject": "MONITOR|RES-025|POST-APPROVAL|T0=2024-05-21",
                "requester_id": "U-005"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-005",
                "action_type": "REQUEST_STATE_CAPTURED",
                "target_id": "AR-001",
                "timestamp": "2024-05-21T09:00:00Z",
                "details": "resource=RES-025"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-005",
                "action_type": "ROLE_SNAPSHOT_CAPTURED",
                "target_id": "U-007",
                "timestamp": "2024-05-21T09:00:00Z",
                "details": "roles_source=system"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-005",
                "action_type": "TICKET_CREATED",
                "target_id": "RES-025",
                "timestamp": "2024-05-21T09:00:00Z",
                "details": "subject=MONITOR|RES-025|POST-APPROVAL|T0=2024-05-21"
            })
    ],
    outputs=[
        '[{"request_state":{"request_id":"AR-001","user_id":"U-007","resource_id":"RES-025","requested_role_id":"ROL-023","justification":"Need temporary access to production for urgent bug fix.","status":"APPROVED","submitted_at":"2024-04-15 15:00:00+00:00","reviewed_by":"U-005","decision_at":"2024-04-15 16:00:00+00:00"}}]',
        '[{"role_snapshot":{"user_id":"U-007","roles":[{"role_id":"ROL-001","role_name":"engineering-base","description":"Basic access for engineering staff","is_temporary":false},{"role_id":"ROL-002","role_name":"engineering-code-commit","description":"Permission to commit code to repositories","is_temporary":false},{"role_id":"ROL-003","role_name":"engineering-prod-access","description":"Access to production environments for debugging","is_temporary":true}]}}]',
        '[{"ticket_subject":"MONITOR|RES-025|POST-APPROVAL|T0=2024-05-21"}]'
    ]
),


# - TASK 92 -
Task(
    annotator="0",
    user_id="092",
    instruction=(
        "You are CERTIFICATION_BOT (U-033). Apply certification and RBAC policy for C-002 on RES-020 using "
        "T0=2024-10-10 16:00:00+00:00. Because the assigned reviewer U-004 is SUSPENDED on a CRITICAL resource, "
        "Operations (U-005) must steward the reassignment path. Enforce MFA for any temporary reviewer access and "
        "grant only the minimal reviewer capability (ROL-024) with expiry 2024-12-31 23:59:59+00:00. Record canonical "
        "audits and open a reassignment ticket to the steward. Do not change the certification’s status. Return a "
        "NO_CHANGE confirmation for C-002, U-005’s updated roles, and the ticket."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-004"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-020"}),
        Action(name="get_certification_details", kwargs={"certification_id": "C-002"}),
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-005"}),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-033",
                "action_type": "SOD_CHECK",
                "target_id": "C-002",
                "timestamp": "2024-10-10 16:00:00+00:00",
                "details": "cert=C-002|res=RES-020|assigned_reviewer=U-004(status=SUSPENDED)|steward_candidate=U-005"
            }),
        Action(name="enable_user_mfa", kwargs={"user_id": "U-005"}),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-033",
                "action_type": "MFA_ENABLED",
                "target_id": "U-005",
                "timestamp": "2024-10-10 16:00:00+00:00",
                "details": "reason=CRITICAL_RESOURCE_REVIEW_ENABLEMENT|res=RES-020"
            }),
        Action(name="assign_role_to_user", kwargs={
                "user_id": "U-005",
                "role_id": "ROL-024",
                "assigned_by": "U-005",
                "assigned_on": "2024-10-10 16:00:00+00:00",
                "expires_on": "2024-12-31 23:59:59+00:00"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-033",
                "action_type": "ACCESS_GRANTED",
                "target_id": "U-005",
                "timestamp": "2024-10-10 16:00:00+00:00",
                "details": "role=ROL-024|res=RES-020|expiry=2024-12-31 23:59:59+00:00|steward=U-005"
            }),
        Action(name="create_hubspot_ticket", kwargs={
                "subject": "REASSIGN|C-002|RES-020|TEMP_REVIEWER=U-005",
                "description": "T0=2024-10-10 16:00:00+00:00|cert=C-002|res=RES-020|owner=U-004|owner_status=SUSPENDED|steward=U-005|grant=ROL-024|expires=2024-12-31 23:59:59+00:00",
                "requester_id": "U-033",
                "assignee_id": "U-005",
                "category": "CERTIFICATION"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id": "U-033",
                "action_type": "CERT_REVIEW_NO_ACTION",
                "target_id": "C-002",
                "timestamp": "2024-10-10 16:00:00+00:00",
                "details": "status=UNCHANGED|reason=REVIEWER_SUSPENDED|steward=U-005"
            }),
        Action(name="get_user_roles", kwargs={"user_id": "U-005"})
    ],
    outputs=[
        '[{"certification_id":"C-002","status":"COMPLETED","review_action":"NO_CHANGE"}]',
        '[{"user_id":"U-005","roles":["ROL-021","ROL-038","ROL-024"]}]',
        '[{"ticket_subject":"REASSIGN|C-002|RES-020|TEMP_REVIEWER=U-005","assignee_id":"U-005","category":"CERTIFICATION"}]'
    ]
),


# - TASK 93 -
Task(
    annotator="0",
    user_id="093",
    instruction=(
        "You are Michael Davis (U-005) in Operations. Under the Fixed-Term Access policy for RES-027, you must ensure that Robert White "
        "(U-017) holds ROL-028 with a defined term. Treat 2025-08-06 14:00:00+00:00 as the assignment instant and "
        "2025-12-31 00:00:00+00:00 as the term end. Return Robert’s current roles as reflected in canonical membership at the end of your action."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-005"}),
        Action(name="get_user_details", kwargs={"user_id": "U-017"}),
        Action(name="get_user_roles", kwargs={"user_id": "U-017"}),
        Action(name="get_role_details", kwargs={"role_id": "ROL-028"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-027"}),
        Action(name="assign_role_to_user", kwargs={
            "user_id": "U-017",
            "role_id": "ROL-028",
            "assigned_by": "U-005",
            "assigned_on": "2025-08-06 14:00:00+00:00",
            "expires_on": "2025-12-31 00:00:00+00:00"
        }),
        Action(name="get_user_roles", kwargs={"user_id": "U-017"})
    ],
    outputs=[
        # Mirror the final get_user_roles result (no extra fields, no wrapping string).
        '[{"role_id":"ROL-021"},{"role_id":"ROL-022"},{"role_id":"ROL-024"},{"role_id":"ROL-028"}]'
    ]
),


# - TASK 94 -
Task(
    annotator="0",
    user_id="094",
    instruction=(
        "You are U-003 (Operations) and not marked ACTIVE. Under RBAC policy, you must not attest in this context. "
        "For RES-025 and request AR-007 at T0=2024-05-20T14:00:00Z, you must record evidence in line with audit requirements, "
        "defer the review formally, and transfer readiness responsibility to the assigned ACTIVE reviewer U-005 to preserve compliance and accountability."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-003"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-025"}),
        Action(name="list_access_requests", kwargs={"resource_id":"RES-025"}),
        Action(name="get_user_details", kwargs={"user_id":"U-029"}),
        Action(name="create_hubspot_ticket", kwargs={
                "subject":"HANDOFF|RES-025|AR-007|READINESS|ASSIGN=U-005","requester_id":"U-003"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-003","action_type":"DEFERRAL_RECORDED","target_ref": {"kind":"ACCESS_REQUEST","id":"AR-007"},
                "timestamp":"2024-05-20T14:00:00Z",
                "details":"scope=RES-025|request=AR-007|reason=REVIEWER_NOT_ACTIVE|assignee=U-005"
            }),
        Action(name="create_incident_record", kwargs={
                "timestamp":"2024-05-20T14:00:00Z",
                "created_by":"U-003",
                "summary":"HANDOFF|RES-025|AR-007|DEFERRAL",
                "linked_users":["U-029","U-005"],
                "linked_resources":["RES-025"]
            }),
    ],
    outputs=[
        '[{"ticket_subject":"HANDOFF|RES-025|AR-007|READINESS|ASSIGN=U-005"}]',
        '[{"incident_summary":"HANDOFF|RES-025|AR-007|DEFERRAL"}]'
    ]
),


# - TASK 95 -
Task(
    annotator="0",
    user_id="095",
    instruction=(
        "You are U-001 (Engineering). Under RBAC and SoD, you must determine whether you are eligible to review RES-026. "
        "If SoD prevents you from acting as reviewer, you must maintain integrity by routing pending items to Operations without altering their state. "
        "Record your eligibility decision at T0=2024-05-27T16:00:00Z for auditability."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-001"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-001"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-026"}),
        Action(name="list_access_requests", kwargs={"status":"PENDING","resource_id":"RES-026"}),
        Action(name="get_user_details", kwargs={"user_id":"U-011"}),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-001","action_type":"SOD_CHECK","target_ref": {"kind":"RESOURCE","id":"RES-026"},
                "timestamp":"2024-05-27T16:00:00Z",
                "details":"reviewer=U-001|owner=U-011|scope=RES-026|conflicts=None"
            }),
        Action(name="create_hubspot_ticket", kwargs={
                "subject":"REROUTE|RES-026|OPS-REVIEW","requester_id":"U-001"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-001","action_type":"REROUTE_REQUESTED","target_ref": {"kind":"RESOURCE","id":"RES-026"},
                "timestamp":"2024-05-27T16:00:00Z","details":"subject=REROUTE|RES-026|OPS-REVIEW"
            }),
        Action(name="create_incident_record", kwargs={
                "timestamp":"2024-05-27T16:00:00Z",
                "created_by":"U-001",
                "summary":"REROUTE|RES-026|OPS-REVIEW",
                "linked_resources":["RES-026"]
            }),
    ],
    outputs=[
        '[{"ticket_subject":"REROUTE|RES-026|OPS-REVIEW"}]',
        '[{"incident_summary":"REROUTE|RES-026|OPS-REVIEW"}]'
    ]
),


# - TASK 96 -
Task(
    annotator="0",
    user_id="096",
    instruction=(
        "You are U-017 (Operations). In alignment with SoD requirements, you must perform a readiness review of RES-027. "
        "You must document role, session, and request context as objective evidence, attest SoD compliance, and establish follow-up accountability. "
        "All records must reflect the review point T0=2024-05-29T13:31:00Z."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-017"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-017"}),
        Action(name="list_sessions", kwargs={"user_id":"U-017","active_only":True}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-027"}),
        Action(name="list_access_requests", kwargs={"resource_id":"RES-027"}),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-017","action_type":"SOD_CHECK","target_ref": {"kind":"RESOURCE","id":"RES-027"},
                "timestamp":"2024-05-29T13:31:00Z","details":"reviewer=U-017|scope=RES-027|conflicts=None"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-017","action_type":"READINESS_RECORDED","target_ref": {"kind":"RESOURCE","id":"RES-027"},
                "timestamp":"2024-05-29T13:31:00Z","details":"summary=READINESS|RES-027"
            }),
        Action(name="create_incident_record", kwargs={
                "timestamp":"2024-05-29T13:31:00Z",
                "created_by":"U-017",
                "summary":"READINESS|RES-027",
                "linked_resources":["RES-027"]
            }),
        Action(name="create_hubspot_ticket", kwargs={
                "subject":"FOLLOWUP|READINESS|RES-027","requester_id":"U-017"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-017","action_type":"TICKET_CREATED","target_ref": {"kind":"RESOURCE","id":"RES-027"},
                "timestamp":"2024-05-29T13:31:00Z","details":"subject=FOLLOWUP|READINESS|RES-027"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-017","action_type":"EVIDENCE_CAPTURED","target_ref": {"kind":"RESOURCE","id":"RES-027"},
                "timestamp":"2024-05-29T13:31:00Z","details":"roles|sessions|requests"
            }),
    ],
    outputs=[
        '[{"incident_summary":"READINESS|RES-027"}]',
        '[{"ticket_subject":"FOLLOWUP|READINESS|RES-027"}]'
    ]
),

# - TASK 97 -
Task(
    annotator="0",
    user_id="097",
    instruction=(
        "You are Jessica Garcia (U-006), Finance and owner of RES-034. Intake-governance requires that the start of the review window at "
        "2024-05-30 15:00:00+00:00 is evidenced in canonical records. The evidence must consist of: (i) an incident summary string equal to "
        "'intake_window_open|resource=RES-034|T0=2024-05-30 15:00:00+00:00' and (ii) an audit details string equal to "
        "'resource=RES-034|status=PENDING|T0=2024-05-30 15:00:00+00:00'. Provide the current PENDING access requests for RES-034."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-006"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-034"}),
        Action(name="create_incident_record", kwargs={
            "timestamp": "2024-05-30 15:00:00+00:00",
            "created_by": "U-006",
            "summary": "intake_window_open|resource=RES-034|T0=2024-05-30 15:00:00+00:00",
            "linked_alerts": [],
            "linked_users": ["U-006"],
            "linked_resources": ["RES-034"]
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-006",
            "action_type": "INTAKE_WINDOW_LOGGED",
            "target_id": "RES-034",
            "timestamp": "2024-05-30 15:00:00+00:00",
            "details": "resource=RES-034|status=PENDING|T0=2024-05-30 15:00:00+00:00"
        }),
        Action(name="list_access_requests", kwargs={"status": "PENDING", "resource_id": "RES-034"})
    ],
    outputs=[
        # Match the canonical dataset’s timestamp style (no 'T' separator).
        '[{"request_id":"AR-034","user_id":"U-018","resource_id":"RES-034","requested_role_id":"ROL-030","status":"PENDING","submitted_at":"2024-05-30 15:00:00+00:00"}]'
    ]
),


# - TASK 98 -
Task(
    annotator="0",
    user_id="098",
    instruction=(
        "You are U-023 (Operations). Under certification requirements, you must perform the periodic review of RES-025. "
        "You must collect objective evidence from access requests and the role catalog, confirm your SoD posture, "
        "and create accountability records reflecting the outcome at T0=2025-06-30T17:00:00Z."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id":"U-023"}),
        Action(name="get_resource_details", kwargs={"resource_id":"RES-025"}),
        Action(name="list_access_requests", kwargs={"resource_id":"RES-025"}),
        Action(name="list_roles", kwargs={}),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-023","action_type":"EVIDENCE_CAPTURED","target_ref": {"kind":"RESOURCE","id":"RES-025"},
                "timestamp":"2025-06-30T17:00:00Z","details":"requests|role_catalog"
            }),
        Action(name="create_incident_record", kwargs={
                "timestamp":"2025-06-30T17:00:00Z",
                "created_by":"U-023",
                "summary":"RECERT|RES-025|PERIODIC-REVIEW",
                "linked_resources":["RES-025"]
            }),
        Action(name="create_hubspot_ticket", kwargs={
                "subject":"RECERT|RES-025|FOLLOW-UPS","requester_id":"U-023"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-023","action_type":"TICKET_CREATED","target_ref": {"kind":"RESOURCE","id":"RES-025"},
                "timestamp":"2025-06-30T17:00:00Z","details":"subject=RECERT|RES-025|FOLLOW-UPS"
            }),
        Action(name="create_audit_log", kwargs={
                "actor_id":"U-023","action_type":"SOD_CHECK","target_ref": {"kind":"RESOURCE","id":"RES-025"},
                "timestamp":"2025-06-30T17:00:00Z","details":"reviewer=U-023|scope=RES-025|conflicts=None"
            }),
    ],
    outputs=[
        '[{"incident_summary":"RECERT|RES-025|PERIODIC-REVIEW"}]',
        '[{"ticket_subject":"RECERT|RES-025|FOLLOW-UPS"}]'
    ]
),


# - TASK 99 -
Task(
    annotator="0",
    user_id="099",
    instruction=(
        "You are Nicole Thomas (U-014), owner of RES-012. With decision time 2024-05-26 15:00:00+00:00, render AR-021 not granted "
        "and record the decision with one audit entry that uses deterministic tokens (resource_id, role_id, decision, decision_at). "
        "Provide the REJECTED requests for RES-012."
    ),
    actions=[
        Action(name="get_user_details", kwargs={"user_id": "U-014"}),
        Action(name="get_resource_details", kwargs={"resource_id": "RES-012"}),
        Action(name="get_access_request", kwargs={"request_id": "AR-021"}),
        Action(name="get_user_details", kwargs={"user_id": "U-026"}),
        Action(name="reject_access_request", kwargs={
            "request_id": "AR-021",
            "reviewer_id": "U-014",
            "decision_at": "2024-05-26 15:00:00+00:00"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id": "U-014",
            "action_type": "ACCESS_REJECTED",
            "target_id": "AR-021",
            "timestamp": "2024-05-26 15:00:00+00:00",
            "details": "resource=RES-012|role=ROL-010|decision=REJECTED|decision_at=2024-05-26 15:00:00+00:00"
        }),
        Action(name="list_access_requests", kwargs={"status": "REJECTED", "resource_id": "RES-012"})
    ],
    outputs=[
        '[{"request_id":"AR-021","user_id":"U-026","resource_id":"RES-012","requested_role_id":"ROL-010","status":"REJECTED","decision_at":"2024-05-26 15:00:00+00:00","reviewed_by":"U-014"}]'
    ]
),


# - TASK 100 -
Task(
    annotator="0",
    user_id="100",
    instruction=(
        "You are Christopher Rodriguez (U-007), Engineering. You already hold ROL-002. Per policy, an Operations reviewer must decide AR-027 (RES-002). Route to the Operations reviewer with the lowest user_id (U-005); if the requested role is already assigned, have Operations reject it as a duplicate at the request’s submitted_at (2024-05-28T18:00:00Z) and record the decision with canonical tokens. Return the final request state and audit records."
    ),
    actions=[
        Action(name="get_access_request", kwargs={"request_id":"AR-027"}),
        Action(name="get_user_roles", kwargs={"user_id":"U-007"}),
        Action(name="reject_access_request", kwargs={
            "request_id":"AR-027",
            "reviewer_id":"U-005",
            "decision_at":"2024-05-28T18:00:00Z"
        }),
        Action(name="create_audit_log", kwargs={
            "actor_id":"U-005",
            "action_type":"ACCESS_REJECTED",
            "target_id":"AR-027",
            "timestamp":"2024-05-28T18:00:00Z",
            "details":"AR=AR-027|STATUS=REJECTED|REASON=DUPLICATE_ROLE|REQUESTED_ROLE=ROL-002|REQUESTER=U-007|DECIDED_BY=U-005|AT=2024-05-28T18:00:00Z"
        }),
        Action(name="get_access_request", kwargs={"request_id":"AR-027"}),
        Action(name="get_audit_logs_for_target", kwargs={"target_id":"AR-027"})
    ],
    outputs=[
        '[{"request_id":"AR-027","status":"REJECTED","reason":"DUPLICATE_ROLE"}]',
        '[{"action_type":"ACCESS_REJECTED","target_id":"AR-027"}]'
    ]
)

]
