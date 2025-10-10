from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="task_01",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T10:00:00Z. "
            "Initiate an email-based design review of Figma artifact art_001 using export profile 'PNG 2x'. "
            "Send from sarah.designer@company.com to [mike.ux@company.com, alex.dev@company.com, lisa.marketing@company.com]. "
            "Ensure the review email includes the exported asset. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "en-001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"],
                "initial_labels": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-23T10:00:00Z",
                "ended_at": "2024-08-23T10:00:00Z",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"export_id":"exp-art_001-20240823-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="task_02",
        instruction=(
            "You are the release publisher for the Design System team and the time is 2024-08-22T17:00:00Z. "
            "Share a release handoff for Figma artifact art_001 referencing release_001, emailed from "
            "sarah.designer@company.com to [alex.dev@company.com, lisa.marketing@company.com, mike.ux@company.com]. "
            "Export the asset using profile 'PNG 2x' and include it in the email."
        ),
        actions=[
            # Read the referenced release (deterministic)
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),

            # Export asset (provisioning) — en-*
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "en-001",
            }),

            # Create thread (email) — em-*
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — release_001 — 2024-08-22",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["alex.dev@company.com", "lisa.marketing@company.com", "mike.ux@company.com"],
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "em-001",
            }),

            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": (
                    "Hello stakeholders,\n"
                    "Please find the release notes for release_001, including changes.\n"
                    "Regards."
                ),
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "em-002",
            }),

            # Artifact governance tag post-handoff — up-*
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/20240822"],
                "remove_tags": [],
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "up-001",
            }),

            # Record the run — rl-*
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-22T17:00:00Z",
                "ended_at": "2024-08-22T17:00:00Z",
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            # '"release_id":"release_001"',
            '"export_id":"exp-art_001-20240822-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="task_03",
        instruction=(
            "You are the accessibility audit lead for the Web UX team and the time is 2024-08-23T12:05:00Z. "
            "For audit aud-art_003-20240823-001 on Figma artifact art_003, review the accessibility findings across the "
            "categories COLOR_CONTRAST, ALT_TEXT, and FOCUS_ORDER, ensuring coverage of each category, then produce a PDF "
            "accessibility report based strictly on those findings and record the activity. Do not invent any values."
        ),
        actions=[
            Action(name="list_audit_findings_a11y", kwargs={
                "audit_id": "aud-art_003-20240823-001",
                "violation_type": "COLOR_CONTRAST",
            }),
            Action(name="list_audit_findings_a11y", kwargs={
                "audit_id": "aud-art_003-20240823-001",
                "violation_type": "ALT_TEXT",
            }),
            Action(name="list_audit_findings_a11y", kwargs={
                "audit_id": "aud-art_003-20240823-001",
                "violation_type": "FOCUS_ORDER",
            }),
            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_003",
                "audit_id": "aud-art_003-20240823-001",
                "format": "pdf",
                "timestamp": "2024-08-23T12:05:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "a11y_audit",
                "status": "completed",
                "started_at": "2024-08-23T12:05:00Z",
                "ended_at": "2024-08-23T12:05:00Z",
                "timestamp": "2024-08-23T12:05:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"aud-art_003-20240823-001"',
            '"asset_id":"exp-art_003-20240823-pdf-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    ),

    # Task 4 — DS fix plan via COMMENTS (no synthesized items if no findings)
    Task(
        annotator="0",
        user_id="task_04",
        instruction=(
            "You are the design systems triage lead and the time is 2024-08-23T13:10:00Z. "
            "Prepare a minimal fix plan for audit aud-art_003-20240823-001 on Figma artifact art_003, owned by "
            "sarah.designer@company.com, focusing on design-system issues (component mismatches and spacing consistency). "
            "Deliver the plan via COMMENTS anchored to the artifact and record the activity with name of ds_audit_fix. "
            "Use only the data provided here or returned from tools; if no relevant findings are available, deliver an empty plan via COMMENTS without synthesizing items."
        ),
        actions=[
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "aud-art_003-20240823-001",
                "finding_type": "COMPONENT_MISMATCH",
            }),
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "aud-art_003-20240823-001",
                "finding_type": "SPACING",
            }),
            # Create plan (updates) → up-*
            Action(name="create_fix_plan", kwargs={
                "audit_id": "aud-art_003-20240823-001",
                "owner_email": "sarah.designer@company.com",
                "delivery_method": "COMMENTS",
                "timestamp": "2024-08-23T13:10:00Z",
                "request_id": "en-001",
            }),
            # Deliver plan (updates) → up-*
            Action(name="deliver_fix_plan", kwargs={
                "plan_id": "fp-art_003-20240823-001",
                "method": "COMMENTS",
                "timestamp": "2024-08-23T13:10:00Z",
                "request_id": "up-001",
            }),
            # Record run (updates) → up-*
            Action(name="record_automation_run", kwargs={
                "task_name": "ds_audit_fix",
                "status": "completed",
                "started_at": "2024-08-23T13:10:00Z",
                "ended_at": "2024-08-23T13:10:00Z",
                "timestamp": "2024-08-23T13:10:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"plan_id":"fp-art_003-20240823-001"',
            # '"delivery_id":"deliver_up-001"',
            '"method":"COMMENTS"',
            '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    ),

    Task(
        annotator="0",
        user_id="task_05",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T09:10:00Z. "
            "Initiate an email-based design review of Figma artifact art_001 using export profile 'PNG 2x', "
            "sent from sarah.designer@company.com to [mike.ux@company.com, alex.dev@company.com, lisa.marketing@company.com]; "
            "ensure the review email includes the exported asset."
        ),
        actions=[
            # Export (provisioning) → en-*
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "en-001",
            }),
            # Governance at kickoff: add 'needs-review' on the artifact → up-*
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "up-001",
            }),
            # Create thread (email) → em-*
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"],
                "initial_labels": [],
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "em-001",
            }),
            # Append with asset attachment by asset id → em-*
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "em-002",
            }),
            # Record run (review) → rv-*
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-23T09:10:00Z",
                "ended_at": "2024-08-23T09:10:00Z",
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"export_id":"exp-art_001-20240823-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    ),

    Task(
        annotator="0",
        user_id="TASK_06",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T09:10:00Z. "
            "Initiate an email-based design review for artifact art_001 using export profile 'PNG 2x' from "
            "sarah.designer@company.com to [mike.ux@company.com, alex.dev@company.com, lisa.marketing@company.com]. "
            "Mark the artifact for review, include the exported asset in the templated email, and record the run."
        ),
        actions=[
            # 1) Governance tag at kickoff
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "rv-001",
            }),

            # 2) Export with specified profile (ID_RULE -> exp-art_001-20240823-png-001)
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "rv-002",
            }),

            # 3) Start the review email thread — SUBJECT from rules (email.review_request.v2_subject)
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": [
                    "mike.ux@company.com",
                    "alex.dev@company.com",
                    "lisa.marketing@company.com",
                ],
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "rv-003",
            }),

            # 4) Send the message — BODY from rules (email.review_request.v2_body) with tokens filled
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_rv-003",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                "attachments_asset_ids": ["asset_rv-002"],
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "rv-004",
            }),

            # 5) Record the run
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-23T09:10:00Z",
                "ended_at": "2024-08-23T09:10:00Z",
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "rv-005",
            }),
        ],
        outputs=[
            '"export_id":"exp-art_001-20240823-png-001"',
            '"thread_id":"thr_rv-003"',
            '"message_id":"msg_rv-004"',
            '"run_id":"run_rv-005"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="TASK_07",
        instruction=(
            "You are the release publisher and the time is 2024-08-22T17:00:00Z. "
            "A hotfix window is penciled in for tonight and stakeholders want a clean summary before they head into the ship room—"
            "share a release handoff for artifact art_001 summarizing changes since the previous release tag for release_001 "
            "and include an exported asset using profile 'PNG 2x' in the email from sarah.designer@company.com to "
            "['alex.dev@company.com', 'lisa.marketing@company.com', 'mike.ux@company.com']; after sending, add the tag "
            "'released/2024-08-22' to the artifact."
        ),
        actions=[
            # Determine diff against the previous tag explicitly referenced
            Action(name="get_release_diff", kwargs={
                "release_id": "release_001",
            }),

            # Fresh export for the handoff (provisioning ⇒ en- prefix)
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "en-001",
            }),

            # Compose email thread using template-derived subject with NEW release_id
            # Template subject: "Release Handoff — {release_id} — {date}"
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — release_001 — 2024-08-22",
                "sender_email": "sarah.designer@company.com",
                "recipients": [
                    "alex.dev@company.com",
                    "lisa.marketing@company.com",
                    "mike.ux@company.com",
                ],
                "initial_labels": [],
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "em-001",
            }),

            # Template body: "Hello stakeholders,\nPlease find the release notes for {release_id}, including changes.\nRegards."
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hello stakeholders,\nPlease find the release notes for release_001, including changes.\nRegards.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "em-002",
            }),

            # Tag the artifact as released for the stated date
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/2024-08-22"],
                "remove_tags": [],
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "up-001",
            }),

            # Record the run (release workflow ⇒ rl- prefix)
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-22T17:00:00Z",
                "ended_at": "2024-08-22T17:00:00Z",
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            ##'"previous_release_id":"release_001"',
            # #'"release_id":"rel-art_001-20240822-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_001-20240822-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["responsive","released/2024-08-22","hero","landing-page","needs-review"]',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="TASK_08",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-23T17:10:00Z. "
            "After a late-afternoon QA sweep exposed a few regressions, for review cycle cycle_001 issue a changes-requested "
            "update and escalate to ['lisa.marketing@company.com'] with labels ['Design/Escalation','design-review']; "
            "keep the discussion in the same day’s thread."
        ),
        actions=[
            # Apply only the requested labels on the existing same-day thread
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_001",
                "add_labels": ["Design/Escalation", "design-review"],
                "remove_labels": [],
                "timestamp": "2024-08-23T17:10:00Z",
                "request_id": "em-001",
            }),
            Action(name="list_review_cycles", kwargs={}),
            # In-thread escalation using template email.changes_requested.v1 and default sender from rules
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_001",
                "sender_email": "sarah.designer@company.com",  # from SENDER_FALLBACK_RULE
                "recipients": ["lisa.marketing@company.com"],  # explicit escalation target
                "body_html": "Changes requested for art_001. Continuing in today’s thread.",
                # email.changes_requested.v1
                "timestamp": "2024-08-23T17:10:00Z",
                "request_id": "em-002",
            }),

            # Update the review cycle status
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_001",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-23T17:10:00Z",
                "timestamp": "2024-08-23T17:10:00Z",
                "request_id": "rv-001",
            }),

            # Record the automation run
            Action(name="record_automation_run", kwargs={
                "task_name": "changes_requested_escalation",
                "status": "completed",
                "started_at": "2024-08-23T17:10:00Z",
                "ended_at": "2024-08-23T17:10:00Z",
                "timestamp": "2024-08-23T17:10:00Z",
                "request_id": "rv-002",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_001"',
            # '"thread_id":"thread_001"',
            '"labels":["Design/Escalation","design-review"]',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rv-002"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_09",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-24T16:45:00Z. "
            "The team wants the latest feedback captured before Monday’s stand-up—sync the newest message from Gmail thread "
            "thread_011 into Figma artifact art_011 as a comment and record the sync."
        ),
        actions=[
            # Verify the dataset-provided thread exists
            Action(name="get_gmail_thread", kwargs={
                "thread_id": "thread_011",
            }),

            # List messages so the agent can pick the newest (the dataset has entries for this thread)
            Action(name="list_gmail_messages", kwargs={
                "thread_id": "thread_011",
            }),

            # Create the Figma comment using the approved template:
            # "Synced from Gmail thread {thread_id} on {date}."
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_011",
                "author_email": "design-review@company.com",  # per COMMENT_AUTHOR_RULE
                "content": "Synced from Gmail thread thread_011 on 2024-08-24.",
                "timestamp": "2024-08-24T16:45:00Z",
                "request_id": "up-001",
            }),

            # Record the automation run
            Action(name="record_automation_run", kwargs={
                "task_name": "sync_email_to_figma",
                "status": "completed",
                "started_at": "2024-08-24T16:45:00Z",
                "ended_at": "2024-08-24T16:45:00Z",
                "timestamp": "2024-08-24T16:45:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"thread_id":"thread_011"',
            '"artifact_id":"art_011"',
            '"comment_id":"comment_up-001"',
            '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="TASK_10",
        instruction=(
            "You are the review program manager and the time is 2024-08-23T15:00:00Z. "
            "With sign-off nudging the deployment window, for review cycle cycle_001 record approvals for "
            "['mike.ux@company.com', 'alex.dev@company.com'] at ['2024-08-23T15:05:00Z', '2024-08-23T15:07:00Z'], "
            "and mark quorum reached if applicable."
        ),
        actions=[
            # ✅ Derive artifact_id from the review cycle (cycle_001 → art_001)
            Action(name="get_review_cycle", kwargs={"cycle_id": "cycle_001"}),

            # Record two explicit approvals (timestamps come from instruction)
            Action(name="update_review_approval", kwargs={
                "cycle_id": "cycle_001",
                "approver_email": "mike.ux@company.com",
                "approved_ts_nullable": "2024-08-23T15:05:00Z",
                "timestamp": "2024-08-23T15:00:00Z",
                "request_id": "rv-001",
            }),
            Action(name="update_review_approval", kwargs={
                "cycle_id": "cycle_001",
                "approver_email": "alex.dev@company.com",
                "approved_ts_nullable": "2024-08-23T15:07:00Z",
                "timestamp": "2024-08-23T15:00:00Z",
                "request_id": "rv-002",
            }),

            # Quorum met (2 approvals same day) ⇒ mark cycle APPROVED (enum uppercase)
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_001",
                "status": "APPROVED",
                "updated_at": "2024-08-23T15:00:00Z",
                "timestamp": "2024-08-23T15:00:00Z",
                "request_id": "rv-003",
            }),

            # Swap governance tags based on artifact derived from cycle (art_001)
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["approved/2024-08-23"],
                "remove_tags": ["needs-review"],
                "timestamp": "2024-08-23T15:00:00Z",
                "request_id": "up-001",
            }),

            # Record the automation run (ID rule: run_<request_id>)
            Action(name="record_automation_run", kwargs={
                "task_name": "approvals_append",
                "status": "completed",
                "started_at": "2024-08-23T15:00:00Z",
                "ended_at": "2024-08-23T15:00:00Z",
                "timestamp": "2024-08-23T15:00:00Z",
                "request_id": "rv-004",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_001"',
            '"cycle_status":"approved"',  # normalized lowercase per OUTPUT_RULE
            '"run_id":"run_rv-004"',
            '"status":"completed"',
        ],
    )

    , Task(
        annotator="0",
        user_id="TASK_11",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T10:35:00Z. "
            "A stakeholder preview is booked right after lunch—begin a design review for Figma artifact art_003 and, as part of kickoff, "
            "add the tag 'needs-review' to the artifact and include the exported asset 'PNG 2x' in the email to "
            "['mike.ux@company.com', 'alex.dev@company.com']."
        ),
        actions=[
            # Create the same-day review cycle (deterministic ID)
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_003-20240823-001",
                "artifact_id": "art_003",
                "started_at": "2024-08-23T10:35:00Z",
                "timestamp": "2024-08-23T10:35:00Z",
                "request_id": "rv-001",
            }),

            # Export the asset to attach (profile exactly as instructed)
            Action(name="export_assets", kwargs={
                "artifact_id": "art_003",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:35:00Z",
                "request_id": "en-001",
            }),

            # Add kickoff governance tag
            Action(name="governance_update", kwargs={
                "artifact_id": "art_003",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:35:00Z",
                "request_id": "up-001",
            }),

            # Start the review email — template-derived subject/body
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_003 — 2024-08-23",  # email.review_request.v2_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com"],
                "timestamp": "2024-08-23T10:35:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com"],
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_003.\nThanks.",
                # email.review_request.v2_body
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-23T10:35:00Z",
                "request_id": "em-002",
            }),

        ],
        outputs=[
            '"cycle_id":"rev-art_003-20240823-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_003-20240823-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["needs-review"]',
            # '"status":"completed"',
        ],
    )

    , Task(
        annotator="0",
        user_id="TASK_12",
        instruction=(
            "You are the release publisher and the time is 2024-08-22T18:00:00Z. "
            "Product wants a crisp narrative for tomorrow’s digest—share a release handoff for artifact art_003 summarizing changes since "
            "the previous release tag for release_001 and include an exported asset using profile 'PNG 2x' in the email from "
            "sarah.designer@company.com to ['mike.ux@company.com', 'alex.dev@company.com']; after sending, add the tag "
            "'released/2024-08-23' to the artifact if the release date matches 2024-08-23."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={
                "release_id": "release_001",
            }),

            Action(name="export_assets", kwargs={
                "artifact_id": "art_003",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-22T18:00:00Z",
                "request_id": "en-001",
            }),

            # Compose email with NEW release_id per ID_RULE
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_003-20240822-001 — 2024-08-22",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com"],
                "initial_labels": [],
                "timestamp": "2024-08-22T18:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com"],
                "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_003-20240822-001, including changes.\nRegards.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-22T18:00:00Z",
                "request_id": "em-002",
            }),

            # Apply release tag as instructed
            Action(name="governance_update", kwargs={
                "artifact_id": "art_003",
                "add_tags": ["released/2024-08-23"],
                "remove_tags": [],
                "timestamp": "2024-08-22T18:00:00Z",
                "request_id": "up-001",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-22T18:00:00Z",
                "ended_at": "2024-08-22T18:00:00Z",
                "timestamp": "2024-08-22T18:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            # #'"release_id":"rel-art_003-20240822-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_003-20240822-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":"["components","tokens","design-system","released/2024-08-23"]"',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )
    , Task(
        annotator="0",
        user_id="TASK_13",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T11:25:00Z. "
            "Keep the inbox tidy during the lunch crunch—start an email-based design review for Figma artifact art_002 using export profile 'PNG 2x'; "
            "keep a single email thread per artifact for the day and continue in the existing thread if one has already started; "
            "ensure the review email includes the exported asset sent to ['lisa.marketing@company.com']."
        ),
        actions=[
            # Try to locate existing same-day thread (safe if none)
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — art_002 — 2024-08-23",
                "participant_email": "lisa.marketing@company.com",
            }),

            # Create the review cycle
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_002-20240823-001",
                "artifact_id": "art_002",
                "started_at": "2024-08-23T11:25:00Z",
                "timestamp": "2024-08-23T11:25:00Z",
                "request_id": "en-001",
            }),

            # Export for attachment
            Action(name="export_assets", kwargs={
                "artifact_id": "art_002",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:25:00Z",
                "request_id": "en-002",
            }),

            # Kickoff tag
            Action(name="governance_update", kwargs={
                "artifact_id": "art_002",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:25:00Z",
                "request_id": "up-001",
            }),

            # Start or continue the thread — we create if none was found above
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_002 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",  # from SENDER_ROLE_MAP
                "recipients": ["lisa.marketing@company.com"],
                "initial_labels": [],
                "timestamp": "2024-08-23T11:25:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",  # from SENDER_ROLE_MAP
                "recipients": ["lisa.marketing@company.com"],
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_002.\nThanks.",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T11:25:00Z",
                "request_id": "em-002",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-23T11:25:00Z",
                "ended_at": "2024-08-23T11:25:00Z",
                "timestamp": "2024-08-23T11:25:00Z",
                "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"cycle_id":"rev-art_002-20240823-001"',
            '"asset_id":"asset_en-002"',
            '"export_id":"exp-art_002-20240823-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["needs-review"]',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    )
    , Task(
        annotator="0",
        user_id="TASK_14",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-24T09:15:00Z. After overnight fixes landed for the homepage, request a re-review for Figma artifact art_001 addressed to ['mike.ux@company.com', 'alex.dev@company.com'] using the standard re-review notice; start a new email thread for today’s re-review and record the activity."
        ),
        actions=[
            # Try to locate an existing same-day thread (safe if none found)
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — art_001 — 2024-08-24",
                "participant_email": "mike.ux@company.com",
            }),
            # If none is located deterministically, start a new thread for re-review (policy: continue same-day thread; otherwise start one)
            Action(name="create_gmail_thread", kwargs={
                "subject": "Re-review Needed — art_001 — 2024-08-24",  # email.rereview_notice.v1_subject
                "sender_email": "sarah.designer@company.com",  # from SENDER_ROLE_MAP
                "recipients": ["mike.ux@company.com", "alex.dev@company.com"],
                "timestamp": "2024-08-24T09:15:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com"],
                "body_html": "Fixes have been applied on {artifact_id}; please re-review the latest assets."
                   .replace("{artifact_id}", "art_001"),  # email.rereview_notice.v1
                "timestamp": "2024-08-24T09:15:00Z",
                "request_id": "em-002",
            }),
            # Record
            Action(name="record_automation_run", kwargs={
                "task_name": "rereview_kickoff",
                "status": "completed",
                "started_at": "2024-08-24T09:15:00Z",
                "ended_at": "2024-08-24T09:15:00Z",
                "timestamp": "2024-08-24T09:15:00Z",
                "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"status":"completed"',
            '"run_id":"run_rv-001"',
        ],
    )
    , Task(
        annotator="0",
        user_id="TASK_15",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-24T09:15:00Z. "
            "The sprint demo is later this morning—start an email-based design review for Figma artifact art_001 using export profile 'PNG 2x'; "
            "keep a single email thread per artifact for the day and continue in the existing thread if one has already started; "
            "ensure the review email includes the exported asset sent to ['mike.ux@company.com', 'alex.dev@company.com']. record run not needed."
        ),
        actions=[
            # Single-thread policy: check for an existing same-day thread
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — art_001 — 2024-08-24",
                "participant_email": "mike.ux@company.com",
            }),
            # Create same-day review cycle
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240824-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-24T09:15:00Z",
                "timestamp": "2024-08-24T09:15:00Z",
                "request_id": "rv-001",
            }),
            # Export asset per instruction
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T09:15:00Z",
                "request_id": "en-001",
            }),
            # Kickoff governance tag at review start
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-24T09:15:00Z",
                "request_id": "up-001",
            }),
            # Start/continue the review email
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_001 — 2024-08-24",  # email.review_request.v2_subject
                "sender_email": "sarah.designer@company.com",  # from SENDER_ROLE_MAP
                "recipients": ["mike.ux@company.com", "alex.dev@company.com"],
                "timestamp": "2024-08-24T09:15:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com"],
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                # email.review_request.v2_body
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-24T09:15:00Z",
                "request_id": "em-002",
            }),

        ],
        outputs=[
            '"cycle_id":"rev-art_001-20240824-001"',
            # '"cycle_status":"needs_review"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_001-20240824-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["needs-review"]',
            # '"status":"completed"',
        ],
    )
    , Task(
        annotator="0",
        user_id="TASK_16",
        instruction=(
            "You are the review program manager and the time is 2024-08-24T09:20:00Z. "
            "To lock the Friday rollout, for review cycle cycle_008 record approvals for "
            "['alex.dev@company.com', 'mike.ux@company.com'] at ['2024-08-24T09:25:00Z', '2024-08-24T09:29:00Z'], "
            "and mark quorum reached if applicable."
        ),
        actions=[
            Action(name="update_review_approval", kwargs={
                "cycle_id": "cycle_008",
                "approver_email": "alex.dev@company.com",
                "approved_ts_nullable": "2024-08-24T09:25:00Z",
                "timestamp": "2024-08-24T09:20:00Z",
                "request_id": "rv-001",
            }),
            Action(name="update_review_approval", kwargs={
                "cycle_id": "cycle_008",
                "approver_email": "mike.ux@company.com",
                "approved_ts_nullable": "2024-08-24T09:29:00Z",
                "timestamp": "2024-08-24T09:20:00Z",
                "request_id": "rv-002",
            }),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_008",
                "status": "APPROVED",
                "updated_at": "2024-08-24T09:20:00Z",
                "timestamp": "2024-08-24T09:20:00Z",
                "request_id": "rv-003",
            }),
            # Swap tags using alias: cycle_008 -> art_001 (see RULES CYCLE_ALIAS)
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["approved/2024-08-24"],
                "remove_tags": ["needs-review"],
                "timestamp": "2024-08-24T09:20:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "approvals_append",
                "status": "completed",
                "started_at": "2024-08-24T09:20:00Z",
                "ended_at": "2024-08-24T09:20:00Z",
                "timestamp": "2024-08-24T09:20:00Z",
                "request_id": "rv-004",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_008"',
            '"cycle_status":"approved"',
            ##'"tags":["approved/2024-08-24"]',
            '"run_id":"run_rv-004"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_17",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T11:45:00Z. "
            "Capture a lunchtime sweep across the homepage—start an email-based design review attaching export 'PNG 2x' from "
            "'art_001' in a single message to ['mike.ux@company.com', 'alex.dev@company.com', 'lisa.marketing@company.com']; "
            "keep one thread for the review for the day."
        ),
        actions=[
            # Export asset (exact profile from instruction)
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:45:00Z",
                "request_id": "en-001",
            }),

            # Kickoff governance tag on the artifact
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:45:00Z",
                "request_id": "up-001",
            }),

            # Single thread for the day (template subject/body from email.review_request.v2)
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"],
                "timestamp": "2024-08-23T11:45:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"],
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-23T11:45:00Z",
                "request_id": "em-002",
            }),

            # Record the automation run (per workflow)
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-23T11:45:00Z",
                "ended_at": "2024-08-23T11:45:00Z",
                "timestamp": "2024-08-23T11:45:00Z",
                "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_001-20240823-png-001"',
            # '"tags_art_001":["responsive","hero","needs-review","landing-page"]',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    )

    , Task(
        annotator="0",
        user_id="TASK_18",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-24T12:30:00Z. "
            "With copy tweaks holding the banner slot, for review cycle cycle_005 issue a changes-requested update and escalate to "
            "['alex.dev@company.com'] with labels ['design-review','Design/Escalation']; keep the discussion in the same day’s thread."
        ),
        actions=[
            # Apply provided labels (no inventions)
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_005",
                "add_labels": ["design-review", "Design/Escalation"],
                "remove_labels": [],
                "timestamp": "2024-08-24T12:30:00Z",
                "request_id": "em-001",
            }),
            # Send the in-thread changes-requested notice
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_005",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["alex.dev@company.com"],
                "body_html": "Changes requested for {artifact_id}. Continuing in today’s thread."
                   .replace("{artifact_id}", "art_003"),  # via CYCLE_ALIAS mapping cycle_005->art_003
                "timestamp": "2024-08-24T12:30:00Z",
                "request_id": "em-002",
            }),
            # Update cycle status
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_005",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-24T12:30:00Z",
                "timestamp": "2024-08-24T12:30:00Z",
                "request_id": "rv-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "changes_requested_escalation",
                "status": "completed",
                "started_at": "2024-08-24T12:30:00Z",
                "ended_at": "2024-08-24T12:30:00Z",
                "timestamp": "2024-08-24T12:30:00Z",
                "request_id": "rv-002",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_005"',
            '"thread_id":"thread_005"',
            '"labels":["design-review","Design/Escalation"]',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rv-002"',
            '"status":"completed"',
        ],
    )
    , Task(
        annotator="0",
        user_id="TASK_19",
        instruction=(
            "You are the release publisher and the time is 2024-08-21T09:15:00Z."
            "Partner engineering needs a heads-up before their verification run—share a release handoff for artifact art_004 summarizing changes since the previous release tag for release_003 and include an exported asset using profile 'PNG 2x' in the email from mike.ux@company.com to ['alex.dev@company.com']; "
            "after sending, add the tag 'released / 2024-08-21' to the artifact and record the run."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_003"}),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_004",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-21T09:15:00Z",
                "request_id": "en-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_004-20240821-001 — 2024-08-21",
                # email.release_handoff.v1_subject
                "sender_email": "mike.ux@company.com",
                "recipients": ["alex.dev@company.com"],
                "timestamp": "2024-08-21T09:15:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "mike.ux@company.com",
                "recipients": ["alex.dev@company.com"],
                "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_004-20240821-001, including changes.\nRegards.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-21T09:15:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_004",
                "add_tags": ["released/2024-08-21"],
                "remove_tags": [],
                "timestamp": "2024-08-21T09:15:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-21T09:15:00Z",
                "ended_at": "2024-08-21T09:15:00Z",
                "timestamp": "2024-08-21T09:15:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            # '"previous_release_id":"release_003"',
            # #'"release_id":"rel-art_004-20240821-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_004-20240821-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            ##'"tags":["released/2024-08-23"]',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_20",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-24T17:00:00Z. "
            "Before wrapping for the day, sync the latest message from Gmail thread thread_006 into Figma artifact art_003 as a comment and record the sync."
        ),
        actions=[
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_006"}),
            Action(name="list_gmail_messages", kwargs={"thread_id": "thread_006"}),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_003",
                "author_email": "design-review@company.com",  # from SENDER_ROLE_MAP (coord.)
                "content": "Synced from Gmail thread thread_006 on 2024-08-24.",  # figma.comment.sync.v1
                "timestamp": "2024-08-24T17:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "sync_email_to_figma",
                "status": "completed",
                "started_at": "2024-08-24T17:00:00Z",
                "ended_at": "2024-08-24T17:00:00Z",
                "timestamp": "2024-08-24T17:00:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"thread_id":"thread_006"',
            '"artifact_id":"art_003"',
            '"comment_id":"comment_up-001"',
            '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_21",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T11:45:00Z. "
            "The review alias is standing by—initiate an email-based design review of Figma artifact art_001 using export profile 'PNG 2x', "
            "sent from sarah.designer@company.com to ['design-review@company.com']; ensure the review email includes the exported asset and add label 'design-review'."
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001", "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:45:00Z", "request_id": "en-001",
            }),
            # kickoff tag per policy
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001", "add_tags": ["needs-review"], "remove_tags": [],
                "timestamp": "2024-08-23T11:45:00Z", "request_id": "up-001",
            }),
            # email using template email.review_request.v2
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-08-23T11:45:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-23T11:45:00Z", "request_id": "em-002",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001", "add_labels": ["design-review"],
                "timestamp": "2024-08-23T11:45:00Z", "request_id": "em-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff", "status": "completed",
                "started_at": "2024-08-23T11:45:00Z", "ended_at": "2024-08-23T11:45:00Z",
                "timestamp": "2024-08-23T11:45:00Z", "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"labels":["design-review"]',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_001-20240823-png-001"',
            ##'"tags":["hero","landing-page","responsive","needs-review"]',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    )
    , Task(
        annotator="0",
        user_id="TASK_22",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-24T10:05:00Z. "
            "As kickoff for the morning’s sync, begin a design review for Figma artifact art_003 and, as part of kickoff, add the tag 'needs-review' to the artifact "
            "and include the exported asset 'PNG 2x' in the email to ['mike.ux@company.com']."
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_003", "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T10:05:00Z", "request_id": "en-001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_003", "add_tags": ["needs-review"], "remove_tags": [],
                "timestamp": "2024-08-24T10:05:00Z", "request_id": "up-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_003 — 2024-08-24",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com"],
                "timestamp": "2024-08-24T10:05:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_003.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-24T10:05:00Z", "request_id": "em-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff", "status": "completed",
                "started_at": "2024-08-24T10:05:00Z", "ended_at": "2024-08-24T10:05:00Z",
                "timestamp": "2024-08-24T10:05:00Z", "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_003-20240824-png-001"',
            ##'"tags":["needs-review"]',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    )
    , Task(
        annotator="0",
        user_id="TASK_23",
        instruction=(
            "You are the review program manager and the time is 2024-09-02T09:40:00Z. "
            "For the first Monday sprint of the month, for review cycle cycle_012 record approvals for ['mike.ux@company.com'] at "
            "['2024-09-02T09:45:00Z'], and mark quorum reached if applicable."
        ),
        actions=[
            Action(name="update_review_approval", kwargs={
                "cycle_id": "cycle_012", "approver_email": "mike.ux@company.com",
                "approved_ts_nullable": "2024-09-02T09:45:00Z",
                "timestamp": "2024-09-02T09:40:00Z", "request_id": "rv-001",
            }),
            # quorum not met (only 1 approval) → no status swap/tag swap
            Action(name="record_automation_run", kwargs={
                "task_name": "approvals_append", "status": "completed",
                "started_at": "2024-09-02T09:40:00Z", "ended_at": "2024-09-02T09:40:00Z",
                "timestamp": "2024-09-02T09:40:00Z", "request_id": "rv-002",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_012"',
            '"run_id":"run_rv-002"',
            '"status":"completed"',
        ],
    )
    , Task(
        annotator="0",
        user_id="TASK_24",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-23T13:20:00Z. "
            "Keep the thread tidy for artifact art_001—continue the existing email conversation thread_001 with a follow-up that includes the latest export 'PNG 2x'; "
            "refresh the 'needs-review' tag on the artifact for today’s review context; do not create a new thread; record the activity under the review kickoff log."
            "use text 'Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.' for email body"
        ),
        actions=[
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_001"}),
            Action(name="list_gmail_messages", kwargs={"thread_id": "thread_001"}),

            # Ensure the asset attached is the latest export
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T13:20:00Z",
                "request_id": "en-001",
            }),

            # Refresh kickoff governance tag for the day
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T13:20:00Z",
                "request_id": "up-001",
            }),

            # Continue in the same thread with the new export attached
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-23T13:20:00Z",
                "request_id": "em-001",
            }),

            # Record under the review kickoff workflow, per policy expectations
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-23T13:20:00Z",
                "ended_at": "2024-08-23T13:20:00Z",
                "timestamp": "2024-08-23T13:20:00Z",
                "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"thread_id":"thread_001"',
            '"message_id":"msg_em-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_001-20240823-png-001"',
            # '"tags":["hero","landing-page","responsive","needs-review"]',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    )

    , Task(
        annotator="0",
        user_id="TASK_25",
        instruction=(
            "You are the release publisher and the time is 2024-08-21T10:00:00Z. "
            "Security wants a quick diff summary—share a release handoff for artifact art_002 summarizing changes since the previous release tag for release_001 "
            "and include an exported asset using profile 'PNG 2x' in the email from sarah.designer@company.com to ['mike.ux@company.com']; "
            "after sending, add the tag 'released/2024-08-21' to the artifact."
        ),
        actions=[
            # 1) Get the previous release diff (to quote in the email body)
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),

            # 2) Export the asset to attach
            Action(name="export_assets", kwargs={
                "artifact_id": "art_002",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-21T10:00:00Z",
                "request_id": "en-001",
            }),

            # 3) Start the handoff email (template-derived subject)
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_002-20240821-001 — 2024-08-21",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com"],
                "timestamp": "2024-08-21T10:00:00Z",
                "request_id": "em-001",
            }),

            # 4) Append message including the diff summary from step 1 (empty {} is acceptable/deterministic)
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": (
                    "Hello stakeholders,\n"
                    "Please find the release notes for rel-art_002-20240821-001, including changes.\n"
                    "Regards."
                ),
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-21T10:00:00Z",
                "request_id": "em-002",
            }),

            # 5) Tag the artifact with the instruction-date release tag (policy: RELEASE_TAGGING_RULE)
            Action(name="governance_update", kwargs={
                "artifact_id": "art_002",
                "add_tags": ["released/2024-08-21"],
                "remove_tags": [],
                "timestamp": "2024-08-21T10:00:00Z",
                "request_id": "up-001",
            }),

            # 6) Record the automation run
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-21T10:00:00Z",
                "ended_at": "2024-08-21T10:00:00Z",
                "timestamp": "2024-08-21T10:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            # '"previous_release_id":"release_001"',
            # #'"release_id":"rel-art_002-20240821-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_002-20240821-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["released/2024-08-21","header","navigation","global"]',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_26",
        instruction=(
            "You are the design review coordinator and the time is 2024-09-02T12:00:00Z. "
            "An SLA reminder pinged just before lunch—For review cycle cycle_011 on artifact art_011, "
            "issue a changes-requested update and escalate to the related thread with labels ['Design/Escalation']; "
            # "keep the discussion in the same day’s thread."
        ),
        actions=[
            Action(name="get_review_cycle", kwargs={"cycle_id": "cycle_011"}),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_011",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-09-02T12:00:00Z",
                "timestamp": "2024-09-02T12:00:00Z",
                "request_id": "rv-001",
            }),
            # Action(name="find_gmail_threads", kwargs={
            #     "subject_contains": "Changes Requested — 2024-09-02",
            #     "participant_email": "mike.ux@company.com",
            # }),
            # Action(name="create_gmail_thread", kwargs={
            #     "subject": "Changes Requested — 2024-09-02",
            #     "sender_email": "sarah.designer@company.com",
            #     "recipients": ["mike.ux@company.com"],
            #     "timestamp": "2024-09-02T12:00:00Z",
            #     "request_id": "em-001",
            # }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_011",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Changes requested for art_011. Continuing in today’s thread.",
                "timestamp": "2024-09-02T12:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_011",
                "add_labels": ["Design/Escalation"],
                "timestamp": "2024-09-02T12:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="attach_thread_to_review_cycle", kwargs={
                "cycle_id": "cycle_011",
                "thread_id": "thread_011",
                "updated_at": "2024-09-02T12:00:00Z",
                "timestamp": "2024-09-02T12:00:00Z",
                "request_id": "rv-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "changes_requested_escalation",
                "status": "completed",
                "started_at": "2024-09-02T12:00:00Z",
                "ended_at": "2024-09-02T12:00:00Z",
                "timestamp": "2024-09-02T12:00:00Z",
                "request_id": "rv-003",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_011"',
            '"thread_id":"thread_011"',
            # '"message_id":"msg_em-002"',
            '"labels":["Design/Escalation"]',
            '"run_id":"run_rv-003"',
            '"status":"completed"',
        ],
    )

    , Task(
        annotator="0",
        user_id="TASK_27",
        instruction=(
            "You are the release publisher and the time is 2024-08-21T11:20:00Z. "
            "Design Ops asked for a crisp story for leadership’s early sync—share a release handoff for artifact art_009 and changes since the previous "
            "release tag for release_004 and include an exported asset using profile 'PNG 2x' in the email from alex.dev@company.com to "
            "['mike.ux@company.com', 'lisa.marketing@company.com']; the release date is 2024-08-23—after sending, add the tag 'released/2024-08-23' to the artifact."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_004"}),

            Action(name="export_assets", kwargs={
                "artifact_id": "art_009",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-21T11:20:00Z",
                "request_id": "en-001",
            }),

            # Email handoff using template-derived subject/body from rules
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_009-20240821-001 — 2024-08-21",
                "sender_email": "alex.dev@company.com",
                "recipients": ["mike.ux@company.com", "lisa.marketing@company.com"],
                "timestamp": "2024-08-21T11:20:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "alex.dev@company.com",
                "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_009-20240821-001, including changes.\nRegards.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-21T11:20:00Z",
                "request_id": "em-002",
            }),

            # Apply required release tag after sending
            Action(name="governance_update", kwargs={
                "artifact_id": "art_009",
                "add_tags": ["released/2024-08-23"],
                "remove_tags": [],
                "timestamp": "2024-08-21T11:20:00Z",
                "request_id": "up-001",
            }),

            # Record the run
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-21T11:20:00Z",
                "ended_at": "2024-08-21T11:20:00Z",
                "timestamp": "2024-08-21T11:20:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            # '"previous_release_id":"release_004"',
            ##'"release_id":"rel-art_009-20240821-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_009-20240821-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["data","component","released/2024-08-23","table"]',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )

    , Task(
        annotator="0",
        user_id="TASK_28",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-09-02T09:00:00Z. "
            "Ahead of sign-off, for audit audit_012 on artifact art_012 review findings across "
            "['COLOR_CONTRAST', 'FOCUS_ORDER'], produce a PDF accessibility report based strictly on those findings, and record the activity."
            # (Note: Categories adjusted to allowed A11Y set per rules.)
        ),
        actions=[
            Action(name="list_audit_findings_a11y", kwargs={
                "audit_id": "audit_012",
                "violation_type": "COLOR_CONTRAST",
            }),
            Action(name="list_audit_findings_a11y", kwargs={
                "audit_id": "audit_012",
                "violation_type": "FOCUS_ORDER",
            }),
            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_012",
                "audit_id": "audit_012",
                "format": "pdf",
                "timestamp": "2024-09-02T09:00:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "a11y_audit_report",
                "status": "completed",
                "started_at": "2024-09-02T09:00:00Z",
                "ended_at": "2024-09-02T09:00:00Z",
                "timestamp": "2024-09-02T09:00:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_012"',
            '"asset_id":"exp-art_012-20240902-pdf-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    )

    , Task(
        annotator="0",
        user_id="TASK_29",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-21T16:10:00Z. "
            "An SLA breach tripped the on-call alert—due to the breach on review cycle cycle_004, send a changes-requested escalation notice to "
            "the related thread with labels ['Design/Escalation']; keep the discussion linked to the original thread."
        ),
        actions=[
            # Set the cycle status
            Action(name="get_review_cycle", kwargs={"cycle_id": "cycle_004"}),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_004",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-21T16:10:00Z",
                "timestamp": "2024-08-21T16:10:00Z",
                "request_id": "rv-001",
            }),

            # Maintain same-day thread: try to find it first
            # Action(name="find_gmail_threads", kwargs={
            #     "subject_contains": "Changes Requested — 2024-08-21",  # from template subject
            #     #"participant_email": "engineering-leads@company.com",
            # }),

            # Start/continue the escalation thread using the required template (subject/body from rules)
            # Action(name="create_gmail_thread", kwargs={
            #     "subject": "Changes Requested — 2024-08-21",
            #     "sender_email": "sarah.designer@company.com",
            #     "recipients": ["engineering-leads@company.com"],
            #     "timestamp": "2024-08-21T16:10:00Z",
            #     "request_id": "em-001",
            # }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_004",
                "sender_email": "sarah.designer@company.com",
                # email.changes_requested.v1 with {cycle_id} deterministically filled
                "body_html": "Changes requested for art_008. Continuing in today’s thread.",
                "timestamp": "2024-08-21T16:10:00Z",
                "request_id": "em-001",
            }),

            # Apply escalation label
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_004",
                "add_labels": ["Design/Escalation"],
                "timestamp": "2024-08-21T16:10:00Z",
                "request_id": "em-002",
            }),

            # Link thread to the cycle to keep conversation tied
            Action(name="attach_thread_to_review_cycle", kwargs={
                "cycle_id": "cycle_004",
                "thread_id": "thread_004",
                "updated_at": "2024-08-21T16:10:00Z",
                "timestamp": "2024-08-21T16:10:00Z",
                "request_id": "rv-002",
            }),

            # Record the run
            Action(name="record_automation_run", kwargs={
                "task_name": "changes_requested_escalation",
                "status": "completed",
                "started_at": "2024-08-21T16:10:00Z",
                "ended_at": "2024-08-21T16:10:00Z",
                "timestamp": "2024-08-21T16:10:00Z",
                "request_id": "rv-003",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_004"',
            '"thread_id":"thread_004"',
            # '"message_id":"msg_em-002"',
            '"labels":["Design/Escalation"]',
            '"run_id":"run_rv-003"',
            '"status":"completed"',
        ],
    )

    , Task(
        annotator="0",
        user_id="TASK_30",
        instruction=(
            "You are the governance steward and the time is 2024-08-24T11:35:00Z. "
            "With an IA refresh planned, update tags on artifact art_002 by adding ['navigation', 'global'] and removing []; "
            "record the update and keep a note in the day’s review thread from sarah.designer@company.com addressed to ['design-review@company.com']."
        ),
        actions=[
            Action(name="governance_update", kwargs={
                "artifact_id": "art_002", "add_tags": ["navigation", "global"], "remove_tags": [],
                "timestamp": "2024-08-24T11:35:00Z", "request_id": "up-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Update — 2024-08-24",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-08-24T11:35:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "body_html": "Hello,\nPlease see details attached.\nThanks.",
                "timestamp": "2024-08-24T11:35:00Z", "request_id": "em-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "governance_update", "status": "completed",
                "started_at": "2024-08-24T11:35:00Z", "ended_at": "2024-08-24T11:35:00Z",
                "timestamp": "2024-08-24T11:35:00Z", "request_id": "up-002",
            }),
        ],
        outputs=[
            '"artifact_id":"art_002"',
            # '"tags":["header","navigation","global"]',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="TASK_31",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-24T12:50:00Z. "
            "To avoid inbox fragmentation, continue the existing email conversation thread_006 for artifact art_003 with a follow-up that includes the latest 'PNG 2x' export; "
            "do not start a new subject; after sending, apply the email label 'design-review', post a one-line confirmation as a Figma comment on art_003 referencing thread_006, and record the activity."
        ),
        actions=[
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_006"}),
            # Action(name="list_gmail_messages", kwargs={"thread_id": "thread_006"}),

            Action(name="export_assets", kwargs={
                "artifact_id": "art_003", "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T12:50:00Z", "request_id": "en-001",
            }),

            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_006", "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_003.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-24T12:50:00Z", "request_id": "em-001",
            }),

            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_006", "add_labels": ["design-review"],
                "timestamp": "2024-08-24T12:50:00Z", "request_id": "em-002",
            }),

            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_003", "author_email": "sarah.designer@company.com",
                "content": "Synced from Gmail thread thread_006 on 2024-08-24.",
                "timestamp": "2024-08-24T12:50:00Z", "request_id": "up-001",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "review_followup", "status": "completed",
                "started_at": "2024-08-24T12:50:00Z", "ended_at": "2024-08-24T12:50:00Z",
                "timestamp": "2024-08-24T12:50:00Z", "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"thread_id":"thread_006"',
            '"message_id":"msg_em-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_003-20240824-png-001"',
            '"comment_id":"comment_up-001"',
            '"labels":["design-review"]',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],

    )

    ,
    Task(
        annotator="0",
        user_id="TASK_32",
        instruction=(
            "You are the design-system auditor and the time is 2024-09-02T11:00:00Z. "
            "A round of taxonomy drift popped up—For audit audit_011 on artifact art_011, review design-system findings covering ['UNMAPPED','AMBIGUOUS'], "
            "generate a PDF report grounded in those findings, then mark the audit completed, email the PDF to ['design-review@company.com'] using the generic template, "
            "log a short Figma comment on art_011 referencing the report asset, and dont record the activity."
        ),
        actions=[
            Action(name="list_audit_findings_ds", kwargs={"audit_id": "audit_011", "finding_type": "UNMAPPED"}),
            Action(name="list_audit_findings_ds", kwargs={"audit_id": "audit_011", "finding_type": "AMBIGUOUS"}),

            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_011",
                "audit_id": "audit_011",
                "format": "pdf",
                "timestamp": "2024-09-02T11:00:00Z",
                "request_id": "au-001",
            }),

            Action(name="update_audit_status", kwargs={
                "audit_id": "audit_011",
                "status": "COMPLETED",
                "updated_at": "2024-09-02T11:00:00Z",
                "timestamp": "2024-09-02T11:00:00Z",
                "request_id": "au-002",
            }),

            # Email using email.generic_plain (subject/body from rules)
            Action(name="create_gmail_thread", kwargs={
                "subject": "Update — 2024-09-02",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-09-02T11:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hello,\nPlease see details attached.\nThanks.",
                "attachments_asset_ids": ["exp-art_011-20240902-pdf-001"],
                "timestamp": "2024-09-02T11:00:00Z",
                "request_id": "em-002",
            }),

            # Figma comment using the new deterministic template:
            # "Audit report sent — {artifact_id} — {audit_id} — {date} — asset {asset_id}"
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_011",
                "author_email": "sarah.designer@company.com",
                "content": "Audit report sent — art_011 — audit_011 — 2024-09-02 — asset exp-art_011-20240902-pdf-001",
                "timestamp": "2024-09-02T11:00:00Z",
                "request_id": "up-001",
            }),
        ],
        outputs=[
            '"audit_id":"audit_011"',
            '"audit_status":"completed"',
            '"report_asset_id":"exp-art_011-20240902-pdf-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"comment_id":"comment_up-001"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_33",
        instruction=(
            "You are the release publisher and the time is 2024-08-23T11:10:00Z. "
            "Midday sign-off is looming—share a release handoff for artifact art_011 summarizing changes since the previous release tag for release_011 "
            "and include an exported asset using profile 'PNG 2x' in the email from sarah.designer@company.com to "
            "['alex.dev@company.com', 'mike.ux@company.com']; after sending, add the tag 'released/2024-08-23' to the artifact if the release date matches 2024-08-23."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_011"}),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_011", "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:10:00Z", "request_id": "en-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_011-20240823-001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["alex.dev@company.com", "mike.ux@company.com"],
                "timestamp": "2024-08-23T11:10:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_011-20240823-001, including changes.\nRegards.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-23T11:10:00Z", "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_011", "add_tags": ["released/2024-08-23"], "remove_tags": [],
                "timestamp": "2024-08-23T11:10:00Z", "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff", "status": "completed",
                "started_at": "2024-08-23T11:10:00Z", "ended_at": "2024-08-23T11:10:00Z",
                "timestamp": "2024-08-23T11:10:00Z", "request_id": "rl-001",
            }),
        ],
        outputs=[
            # '"previous_release_id":"release_011"',
            ##'"release_id":"rel-art_011-20240823-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_011-20240823-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["released/2024-08-23"]',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_34",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-24T18:00:00Z. "
            "Before the EOD handoff, sync Gmail thread thread_004 into Figma artifact art_008 by posting a thread-level comment that references the thread id "
            "(no per-message reference required); then reply from sarah.designer@company.com in the same Gmail thread using the sync confirmation template, "
            "apply the email label 'synced-to-figma', and record the sync."
        ),
        actions=[
            # Use dataset-provided thread id; no message listing needed
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_004"}),

            # Figma comment using figma.comment.sync.v1 ("Synced Gmail thread {thread_id} on {date}.")
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_008",
                "author_email": "design-review@company.com",
                "content": "Synced from Gmail thread thread_004 on 2024-08-24.",
                "timestamp": "2024-08-24T18:00:00Z",
                "request_id": "up-001",
            }),

            # Reply in the same Gmail thread using email.sync_confirmation (subject not needed for a reply; body is deterministic)
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_004",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Thread thread_004 synced to art_008 on 2024-08-24.",
                "timestamp": "2024-08-24T18:00:00Z",
                "request_id": "em-001",
            }),

            # Apply the requested label
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_004",
                "add_labels": ["synced-to-figma"],
                "timestamp": "2024-08-24T18:00:00Z",
                "request_id": "em-002",
            }),

            # Record the automation run
            Action(name="record_automation_run", kwargs={
                "task_name": "sync_email_to_figma",
                "status": "completed",
                "started_at": "2024-08-24T18:00:00Z",
                "ended_at": "2024-08-24T18:00:00Z",
                "timestamp": "2024-08-24T18:00:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"thread_id":"thread_004"',
            '"comment_id":"comment_up-001"',
            '"message_id":"msg_em-001"',
            '"labels":["synced-to-figma"]',
            '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_35",
        instruction=(
            "You are the design systems triage lead and the time is 2024-09-02T15:30:00Z."
            "Ahead of tomorrow’s stakeholders check-in, for audit aud-art_003-20240902-001 on artifact art_003 (owner sarah.designer@company.com), execute the fixplan_create_and_deliver workflow: base the minimal plan strictly on DS findings in ['COMPONENT_MISMATCH','SPACING'], deliver it as a PDF asset, leave a brief confirmation in Figma, "
            "No need to record the automation run."
        ),
        actions=[
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "aud-art_003-20240902-001", "finding_type": "COMPONENT_MISMATCH"
            }),
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "aud-art_003-20240902-001", "finding_type": "SPACING"
            }),

            Action(name="create_fix_plan", kwargs={
                "audit_id": "aud-art_003-20240902-001",
                "owner_email": "sarah.designer@company.com",
                "delivery_method": "PDF",
                "timestamp": "2024-09-02T15:30:00Z",
                "request_id": "en-001",
            }),

            # No synthesized items if findings unavailable (empty is allowed per DATA_RULE)
            Action(name="upsert_fix_items", kwargs={
                "plan_id": "fp-art_003-20240902-001",
                "items": [],
                "timestamp": "2024-09-02T15:30:00Z",
                "request_id": "up-001",
            }),

            Action(name="deliver_fix_plan", kwargs={
                "plan_id": "fp-art_003-20240902-001",
                "method": "PDF",
                "timestamp": "2024-09-02T15:30:00Z",
                "request_id": "up-002",
            }),

            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_003",
                "author_email": "sarah.designer@company.com",
                "content": "PDF",
                "timestamp": "2024-09-02T15:30:00Z",
                "request_id": "up-003",
            }),

            # Action(name="record_automation_run", kwargs={
            #     "task_name": "fixplan_create_and_deliver",
            #     "status": "completed",
            #     "started_at": "2024-09-02T15:30:00Z",
            #     "ended_at": "2024-09-02T15:30:00Z",
            #     "timestamp": "2024-09-02T15:30:00Z",
            #     "request_id": "up-004",
            # }),
        ],
        outputs=[
            '"plan_id":"fp-art_003-20240902-001"',
            # '"item_count":0',
            # '"delivery_asset_id":"fixplanpdf_up-002"',
            '"comment_id":"comment_up-003"',
            # '"run_id":"run_up-004"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_36",
        instruction=(
            "You are the release publisher and the time is 2024-08-23T12:30:00Z. "
            "Platform is prepping a ship-room review—share a release handoff for artifact art_010 referencing release_005; "
            "export and attach the 'PNG 2x' asset, email from emma.brand@company.com to ['stakeholders@company.com'] using the release template, "
            "apply the email label 'release', add the tag 'released/2024-08-23' to art_010 after sending, and record the run."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_005"}),

            Action(name="export_assets", kwargs={
                "artifact_id": "art_010", "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T12:30:00Z", "request_id": "en-001",
            }),

            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_010-20240823-001 — 2024-08-23",
                "sender_email": "emma.brand@company.com",
                "recipients": ["stakeholders@company.com"],
                "timestamp": "2024-08-23T12:30:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "emma.brand@company.com",
                "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_010-20240823-001, including changes.\nRegards.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-23T12:30:00Z", "request_id": "em-002",
            }),

            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001", "add_labels": ["release"],
                "timestamp": "2024-08-23T12:30:00Z", "request_id": "em-003",
            }),

            Action(name="governance_update", kwargs={
                "artifact_id": "art_010", "add_tags": ["released/2024-08-23"], "remove_tags": [],
                "timestamp": "2024-08-23T12:30:00Z", "request_id": "up-001",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff", "status": "completed",
                "started_at": "2024-08-23T12:30:00Z", "ended_at": "2024-08-23T12:30:00Z",
                "timestamp": "2024-08-23T12:30:00Z", "request_id": "rl-001",
            }),
        ],
        outputs=[
            # '"previous_release_id":"release_005"',
            # '"release_id":"rel-art_010-20240823-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_010-20240823-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"labels":["release"]',
            # '"tags":["released/2024-08-23"]',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],

    )
    ,
    Task(
        annotator="0",
        user_id="TASK_37",
        instruction=(
            "You are the design systems triage lead and the time is 2024-08-24T16:00:00Z. "
            "Inbox-first delivery requested—prepare a minimal fix plan for audit aud-art_003-20240824-001 on artifact art_003, "
            "owned by sarah.designer@company.com; review DS findings for ['COMPONENT_MISMATCH','SPACING'] to seed the plan and the plan, "
            "upsert only available items , deliver the plan as an EMAIL asset to ['stakeholders@company.com'] "
            "leave a confirmation note in Figma on art_003."
        ),
        actions=[
            # Sample DS findings (allowed categories per rules)
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "aud-art_003-20240824-001", "finding_type": "COMPONENT_MISMATCH"
            }),
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "aud-art_003-20240824-001", "finding_type": "SPACING"
            }),

            # Create the fix plan (ID derives date from instruction timestamp)
            Action(name="create_fix_plan", kwargs={
                "audit_id": "aud-art_003-20240824-001",
                "owner_email": "sarah.designer@company.com",
                "delivery_method": "EMAIL",
                "timestamp": "2024-08-24T16:00:00Z",
                "request_id": "en-001",
            }),

            # No synthesized items if none found (empty is acceptable per DATA_RULE)
            Action(name="upsert_fix_items", kwargs={
                "plan_id": "fp-art_003-20240824-001",
                "items": [],
                "timestamp": "2024-08-24T16:00:00Z",
                "request_id": "up-001",
            }),

            # Deliver via EMAIL; recipients are specified in the instruction
            Action(name="deliver_fix_plan", kwargs={
                "plan_id": "fp-art_003-20240824-001",
                "method": "EMAIL",
                "recipients": ["stakeholders@company.com"],
                "timestamp": "2024-08-24T16:00:00Z",
                "request_id": "up-002",
            }),

            # Leave a confirmation note in Figma
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_003",
                "author_email": "design-review@company.com",
                "content": "EMAIL",
                "timestamp": "2024-08-24T16:00:00Z",
                "request_id": "up-003",
            }),

            # Record the run
            Action(name="record_automation_run", kwargs={
                "task_name": "fixplan_create_and_deliver",
                "status": "completed",
                "started_at": "2024-08-24T16:00:00Z",
                "ended_at": "2024-08-24T16:00:00Z",
                "timestamp": "2024-08-24T16:00:00Z",
                "request_id": "up-004",
            }),
        ],
        outputs=[
            '"plan_id":"fp-art_003-20240824-001"',
            # '"item_count":0',
            # '"email_thread_id":"thr_up-002"',
            '"comment_id":"comment_up-003"',
            '"run_id":"run_up-004"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_38",
        instruction=(
            "You are the design systems triage lead and the time is 2024-09-02T16:40:00Z. "
            "Keep the loop tight with marketing—prepare a minimal fix plan for audit aud-art_012-20240902-001 on artifact art_012, "
            "owned by mike.ux@company.com; base the plan strictly on DS findings in ['COMPONENT_MISMATCH','SPACING','TOKENS'] "
            "(deliver an empty plan if none are present); deliver the plan via EMAIL to ['lisa.marketing@company.com'] using the "
            "standard fix-plan template, and record the activity."
        ),
        actions=[
            # Deterministically enumerate allowed DS categories (per RULES)
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "aud-art_012-20240902-001", "finding_type": "COMPONENT_MISMATCH"
            }),
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "aud-art_012-20240902-001", "finding_type": "SPACING"
            }),
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "aud-art_012-20240902-001", "finding_type": "TOKENS"
            }),

            # Create the plan (date derives from instruction timestamp)
            Action(name="create_fix_plan", kwargs={
                "audit_id": "aud-art_012-20240902-001",
                "owner_email": "mike.ux@company.com",
                "delivery_method": "EMAIL",
                "timestamp": "2024-09-02T16:40:00Z",
                "request_id": "en-001",
            }),

            # Deliver via EMAIL (use em- prefix per ID_RULE); tool emits thread_id deterministically
            Action(name="deliver_fix_plan", kwargs={
                "plan_id": "fp-art_012-20240902-001",
                "method": "EMAIL",
                "recipients": ["lisa.marketing@company.com"],
                "timestamp": "2024-09-02T16:40:00Z",
                "request_id": "em-001",
            }),

            # # Verify the resulting thread exists
            # Action(name="get_gmail_thread", kwargs={
            #     "thread_id": "thr_em-001",
            # }),

            # Record the automation run
            Action(name="record_automation_run", kwargs={
                "task_name": "fixplan_create_and_deliver",
                "status": "completed",
                "started_at": "2024-09-02T16:40:00Z",
                "ended_at": "2024-09-02T16:40:00Z",
                "timestamp": "2024-09-02T16:40:00Z",
                "request_id": "up-001",
            }),
        ],
        outputs=[
            '"plan_id":"fp-art_012-20240902-001"',
            # '"email_thread_id":"thr_em-001"',
            '"run_id":"run_up-001"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_39",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-23T18:15:00Z. "
            "Capture late-day decisions—sync the Gmail thread reference from thread_008 into Figma artifact art_010 as a comment "
            "(thread reference only; message-level metadata not required), then reply in-thread with the explicit acknowledgement "
            "'Synced to Figma for art_010 on 2024-08-23.'; apply the email label 'synced-to-figma', and record the sync."
        ),
        actions=[
            # Read the thread (dataset-provided id; deterministic)
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_008"}),

            # (Optional) List messages—safe even if empty in this dataset
            # Action(name="list_gmail_messages", kwargs={"thread_id": "thread_008"}),

            # Create the Figma comment with the thread reference; coordinator alias as author
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_010",
                "author_email": "design-review@company.com",
                "content": "Synced from Gmail thread thread_008 on 2024-08-23.",
                "timestamp": "2024-08-23T18:15:00Z",
                "request_id": "up-001",
            }),

            # Reply in-thread explicitly acknowledging the sync (instruction provides exact body text)
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_008",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Synced to Figma for art_010 on 2024-08-23.",
                "timestamp": "2024-08-23T18:15:00Z",
                "request_id": "em-001",
            }),

            # Apply the required label
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_008",
                "add_labels": ["synced-to-figma"],
                "timestamp": "2024-08-23T18:15:00Z",
                "request_id": "em-002",
            }),

            # Record the run
            Action(name="record_automation_run", kwargs={
                "task_name": "sync_email_to_figma",
                "status": "completed",
                "started_at": "2024-08-23T18:15:00Z",
                "ended_at": "2024-08-23T18:15:00Z",
                "timestamp": "2024-08-23T18:15:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"thread_id":"thread_008"',
            '"comment_id":"comment_up-001"',
            '"message_id":"msg_em-001"',
            '"labels":["synced-to-figma"]',
            '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_40",
        instruction=(
            "You are the design review coordinator and the time is 2024-09-02T14:30:00Z. "
            "After fixes rolled in from the morning triage, request a re-review for Figma artifact art_003 addressed to ['alex.dev@company.com', 'lisa.marketing@company.com'] using the standard re-review notice; "
            "maintain one same-day thread (continue if present, otherwise start a new one), attach the latest 'PNG 2x' export, apply the email label 'design-review', "
            "add the kickoff tag 'needs-review' on art_003, and record the activity."
        ),
        actions=[
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Re-review Needed — art_003 — 2024-09-02",
                # "participant_email": "alex.dev@company.com",
            }),

            Action(name="export_assets", kwargs={
                "artifact_id": "art_003", "export_profile": "PNG 2x",
                "timestamp": "2024-09-02T14:30:00Z", "request_id": "en-001",
            }),

            Action(name="create_gmail_thread", kwargs={
                "subject": "Re-review Needed — art_003 — 2024-09-02",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["alex.dev@company.com", "lisa.marketing@company.com"],
                "timestamp": "2024-09-02T14:30:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "body_html": "Fixes have been applied on art_003; please re-review the latest assets.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-09-02T14:30:00Z", "request_id": "em-002",
            }),

            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001", "add_labels": ["design-review"],
                "timestamp": "2024-09-02T14:30:00Z", "request_id": "em-003",
            }),

            Action(name="governance_update", kwargs={
                "artifact_id": "art_003", "add_tags": ["needs-review"], "remove_tags": [],
                "timestamp": "2024-09-02T14:30:00Z", "request_id": "up-001",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "rereview_kickoff", "status": "completed",
                "started_at": "2024-09-02T14:30:00Z", "ended_at": "2024-09-02T14:30:00Z",
                "timestamp": "2024-09-02T14:30:00Z", "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_003-20240902-png-001"',
            '"labels":["design-review"]',
            # '"tags":["needs-review","components","tokens","design-system"]',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],

    ),
    Task(
        annotator="0",
        user_id="TASK_41",
        instruction=(
            "You are the governance steward and the time is 2024-09-02T09:05:00Z. "
            "With sign-off confirmed, update tags on artifact art_011 by adding ['approved'] and removing ['needs-review']; "
            "record the update and send a short note to ['design-review@company.com'] in the day’s review thread—"
            "keep a single same-day thread (continue it if it exists; otherwise start one) using the standard update template."
        ),
        actions=[
            Action(name="governance_update", kwargs={
                "artifact_id": "art_011", "add_tags": ["approved"], "remove_tags": ["needs-review"],
                "timestamp": "2024-09-02T09:05:00Z", "request_id": "up-001",
            }),
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Update — 2024-09-02",
                "participant_email": "design-review@company.com",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Update — 2024-09-02",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-09-02T09:05:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "body_html": "Hello,\nPlease see details attached.\nThanks.",
                "timestamp": "2024-09-02T09:05:00Z", "request_id": "em-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "governance_update", "status": "completed",
                "started_at": "2024-09-02T09:05:00Z", "ended_at": "2024-09-02T09:05:00Z",
                "timestamp": "2024-09-02T09:05:00Z", "request_id": "up-002",
            }),
        ],
        outputs=[
            '"artifact_id":"art_011"',
            # '"tags":["contact","component","form","approved"]',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_42",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-23T16:40:00Z. "
            "Keep continuity for the team—For review cycle cycle_003 on artifact art_007, communicate that changes are requested by replying "
            "in the existing same-day email thread thread_003 to the original recipients ['mike.ux@company.com','alex.dev@company.com'] "
            "using the standard changes-requested template; do not create a new subject; attach this thread to the review cycle and record the update."
        ),
        actions=[
            # Confirm the cycle and set status
            Action(name="get_review_cycle", kwargs={"cycle_id": "cycle_003"}),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_003", "status": "CHANGES_REQUESTED", "updated_at": "2024-08-23T16:40:00Z",
                "timestamp": "2024-08-23T16:40:00Z", "request_id": "rv-001",
            }),

            # Continue the existing same-day thread (no new subject)
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_003"}),
            Action(name="list_gmail_messages", kwargs={"thread_id": "thread_003"}),

            # Send the in-thread notice using the changes-requested template
            # Subject is not created (reply in-thread); body derives from template:
            #   subject: "Changes Requested — {date}"  (not used since we reply)
            #   body: "Changes requested for {artifact_id}. Continuing in today’s thread."
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_003",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Changes requested for art_007. Continuing in today’s thread.",
                "timestamp": "2024-08-23T16:40:00Z", "request_id": "em-001",
            }),

            # Tie the thread to the cycle for traceability
            Action(name="attach_thread_to_review_cycle", kwargs={
                "cycle_id": "cycle_003", "thread_id": "thread_003", "updated_at": "2024-08-23T16:40:00Z",
                "timestamp": "2024-08-23T16:40:00Z", "request_id": "rv-002",
            }),

            # Record the run
            Action(name="record_automation_run", kwargs={
                "task_name": "changes_requested_escalation", "status": "completed",
                "started_at": "2024-08-23T16:40:00Z", "ended_at": "2024-08-23T16:40:00Z",
                "timestamp": "2024-08-23T16:40:00Z", "request_id": "rv-003",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_003"',
            '"thread_id":"thread_003"',
            '"message_id":"msg_em-001"',
            '"run_id":"run_rv-003"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_43",
        instruction=(
            "You are the release publisher and the time is 2024-08-21T12:40:00Z. "
            "Brand is lining up guidelines updates—share a release handoff for artifact art_007 referencing release_005, "
            "include an exported asset 'PNG 2x' in the email from lisa.marketing@company.com to ['emma.brand@company.com']."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_005"}),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_007", "export_profile": "PNG 2x",
                "timestamp": "2024-08-21T12:40:00Z", "request_id": "en-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_007-20240821-001 — 2024-08-21",
                # email.release_handoff.v1_subject
                "sender_email": "lisa.marketing@company.com",
                "recipients": ["emma.brand@company.com"],
                "timestamp": "2024-08-21T12:40:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "lisa.marketing@company.com",
                "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_007-20240821-001, including changes.\nRegards.",
                # template body
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-21T12:40:00Z", "request_id": "em-002",
            }),
            # Release handoff policy: tag after successful handoff with date from instruction timestamp
            Action(name="governance_update", kwargs={
                "artifact_id": "art_007", "add_tags": ["released/20240821"], "remove_tags": [],
                "timestamp": "2024-08-21T12:40:00Z", "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff", "status": "completed",
                "started_at": "2024-08-21T12:40:00Z", "ended_at": "2024-08-21T12:40:00Z",
                "timestamp": "2024-08-21T12:40:00Z", "request_id": "rl-001",
            }),
        ],
        outputs=[
            # '"previous_release_id":"release_005"',
            # '"release_id":"rel-art_007-20240821-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_007-20240821-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["needs-review","released/20240821","pricing","conversion","cta"]',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_44",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-09-02T11:25:00Z. "
            "Keep the day’s thread consistent—initiate an email-based design review of Figma artifact art_009 using export profile 'PNG 2x', "
            "from sarah.designer@company.com to ['mike.ux@company.com']; include the exported asset."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_009-20240902-001", "artifact_id": "art_009",
                "started_at": "2024-09-02T11:25:00Z", "timestamp": "2024-09-02T11:25:00Z", "request_id": "en-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_009", "export_profile": "PNG 2x",
                "timestamp": "2024-09-02T11:25:00Z", "request_id": "en-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_009", "add_tags": ["needs-review"], "remove_tags": [],
                "timestamp": "2024-09-02T11:25:00Z", "request_id": "up-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_009 — 2024-09-02",  # email.review_request.v2_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com"],
                "timestamp": "2024-09-02T11:25:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_009.\nThanks.",
                # template body
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-09-02T11:25:00Z", "request_id": "em-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff", "status": "completed",
                "started_at": "2024-09-02T11:25:00Z", "ended_at": "2024-09-02T11:25:00Z",
                "timestamp": "2024-09-02T11:25:00Z", "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"cycle_id":"rev-art_009-20240902-001"',
            '"asset_id":"asset_en-002"',
            '"export_id":"exp-art_009-20240902-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["component","table","data","needs-review"]',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_45",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-24T11:10:00Z. "
            "To streamline feedback on shared dependencies, run a consolidated email-based design review and attach 'PNG 2x' exports from "
            "['art_004', 'art_005'] in a single message to ['design-review@company.com']; maintain one thread for the consolidated review for the day."
            "No need to log the run"
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_004", "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T11:10:00Z", "request_id": "en-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_005", "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T11:10:00Z", "request_id": "en-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_004", "add_tags": ["needs-review"], "remove_tags": [],
                "timestamp": "2024-08-24T11:10:00Z", "request_id": "up-001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_005", "add_tags": ["needs-review"], "remove_tags": [],
                "timestamp": "2024-08-24T11:10:00Z", "request_id": "up-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — Consolidated — 2024-08-24",  # email.review_request_consolidated.v1_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-08-24T11:10:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x exports.\nThanks.",
                # consolidated template body
                "attachments_asset_ids": ["asset_en-001", "asset_en-002"],
                "timestamp": "2024-08-24T11:10:00Z", "request_id": "em-002",
            }),

        ],
        outputs=[
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"asset_ids":["asset_en-001","asset_en-002"]',
            '"export_ids":["exp-art_004-20240824-png-001","exp-art_005-20240824-png-001"]',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_46",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-21T16:30:00Z. "
            "A follow-up SLA alert just fired—due to the breach on review cycle cycle_004 for artifact art_008, "
            "send a changes-requested escalation notice to ['design-automation@company.com','product-managers@company.com'] "
            "using the standard changes-requested template; maintain same-day continuity (continue the existing thread for product-managers@company.com if present, "
            "otherwise start one), apply the label ['Design/Escalation'], attach the thread to the review cycle, No need to record the automation run."
        ),
        actions=[
            # 1) Fetch cycle
            Action(name="get_review_cycle", kwargs={"cycle_id": "cycle_004"}),

            # 2) Maintain same-day continuity: try to find an existing thread first
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Changes Requested — 2024-08-21",
                "participant_email": "product-managers@company.com",
            }),

            # 3) Mark status = CHANGES_REQUESTED
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_004", "status": "CHANGES_REQUESTED", "updated_at": "2024-08-21T16:30:00Z",
                "timestamp": "2024-08-21T16:30:00Z", "request_id": "rv-001",
            }),

            # 4) Start/continue the escalation email (subject from template family; new thread ok if none found)
            Action(name="create_gmail_thread", kwargs={
                "subject": "Changes Requested — 2024-08-21",  # email.changes_requested.v1_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-automation@company.com", "product-managers@company.com"],
                "timestamp": "2024-08-21T16:30:00Z", "request_id": "em-001",
            }),

            # 5) Body EXACTLY from template with {artifact_id} filled
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "body_html": "Changes requested for art_008. Continuing in today’s thread.",
                # email.changes_requested.v1
                "timestamp": "2024-08-21T16:30:00Z", "request_id": "em-002",
            }),

            # 6) Apply escalation label exactly as instructed
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001", "add_labels": ["Design/Escalation"],
                "timestamp": "2024-08-21T16:30:00Z", "request_id": "em-003",
            }),

            # 7) Link the email thread to the review cycle for traceability
            Action(name="attach_thread_to_review_cycle", kwargs={
                "cycle_id": "cycle_004", "thread_id": "thr_em-001", "updated_at": "2024-08-21T16:30:00Z",
                "timestamp": "2024-08-21T16:30:00Z", "request_id": "rv-002",
            }),

        ],
        outputs=[
            '"cycle_id":"cycle_004"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"labels":["Design/Escalation"]',
            '"status":"changes_requested"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_47",
        instruction=(
            "You are the design review coordinator and the time is 2024-09-02T16:20:00Z. "
            "With the final polish now landed, request a re-review for Figma artifact art_012 addressed to ['mike.ux@company.com'] "
            "using the standard re-review notice; maintain same-day continuity (continue the existing thread if present, otherwise start one), "
            "and record the activity."
        ),
        actions=[
            # Maintain same-day continuity: try to find the existing re-review thread first
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Re-review Needed — art_012 — 2024-09-02",  # email.rereview_notice.v1_subject
                "participant_email": "mike.ux@company.com",
            }),

            # Start a thread only if none is found (THREAD_POLICY)
            Action(name="create_gmail_thread", kwargs={
                "subject": "Re-review Needed — art_012 — 2024-09-02",  # from rules: email.rereview_notice.v1_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com"],
                "timestamp": "2024-09-02T16:20:00Z", "request_id": "em-001",
            }),

            # Send the re-review notice using the template body from rules
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Fixes have been applied on art_012; please re-review the latest assets.",
                # email.rereview_notice.v1
                "timestamp": "2024-09-02T16:20:00Z", "request_id": "em-002",
            }),

            # Record the run
            Action(name="record_automation_run", kwargs={
                "task_name": "rereview_kickoff", "status": "completed",
                "started_at": "2024-09-02T16:20:00Z", "ended_at": "2024-09-02T16:20:00Z",
                "timestamp": "2024-09-02T16:20:00Z", "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_48",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-24T10:30:00Z. "
            "Contrast and flow are under scrutiny—For audit audit_001 on artifact art_001, review findings across "
            "['COLOR_CONTRAST', 'FOCUS_ORDER'], produce a PDF accessibility report based strictly on those findings, and record the activity."
        ),
        actions=[
            Action(name="list_audit_findings_a11y",
                   kwargs={"audit_id": "audit_001", "violation_type": "COLOR_CONTRAST"}),
            Action(name="list_audit_findings_a11y", kwargs={"audit_id": "audit_001", "violation_type": "FOCUS_ORDER"}),
            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_001", "audit_id": "audit_001", "format": "pdf",
                "timestamp": "2024-08-24T10:30:00Z", "request_id": "au-001",
            }),
            Action(name="update_audit_status", kwargs={
                "audit_id": "audit_001", "status": "COMPLETED", "updated_at": "2024-08-24T10:30:00Z",
                "timestamp": "2024-08-24T10:30:00Z", "request_id": "au-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "a11y_audit_report", "status": "completed",
                "started_at": "2024-08-24T10:30:00Z", "ended_at": "2024-08-24T10:30:00Z",
                "timestamp": "2024-08-24T10:30:00Z", "request_id": "au-003",
            }),
        ],
        outputs=[
            '"audit_id":"audit_001"',
            '"asset_id":"exp-art_001-20240824-pdf-001"',
            '"run_id":"run_au-003"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_49",
        instruction=(
            "You are the release publisher and the time is 2024-09-02T09:30:00Z. "
            "PMs asked for a Monday morning roll-up—share a release handoff for artifact art_002 referencing release_012; "
            "attach the 'PNG 2x' export and email from mike.ux@company.com to ['product-managers@company.com', 'stakeholders@company.com']; "
            "summarize differences from the prior release tag."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_012"}),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_002", "export_profile": "PNG 2x",
                "timestamp": "2024-09-02T09:30:00Z", "request_id": "en-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_002-20240902-001 — 2024-09-02",
                "sender_email": "mike.ux@company.com",
                "recipients": ["product-managers@company.com", "stakeholders@company.com"],
                "timestamp": "2024-09-02T09:30:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "mike.ux@company.com",
                "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_002-20240902-001, including changes.\nRegards.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-09-02T09:30:00Z", "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_002", "add_tags": ["released/20240902"], "remove_tags": [],
                "timestamp": "2024-09-02T09:30:00Z", "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff", "status": "completed",
                "started_at": "2024-09-02T09:30:00Z", "ended_at": "2024-09-02T09:30:00Z",
                "timestamp": "2024-09-02T09:30:00Z", "request_id": "rl-001",
            }),
        ],
        outputs=[
            # '"previous_release_id":"release_012"',
            # #'"release_id":"rel-art_002-20240902-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_002-20240902-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["released/20240902"]',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_50",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T11:45:00Z. "
            "The review alias is standing by—initiate an email-based design review of Figma artifact art_001 using export profile 'PNG 2x', "
            "sent from sarah.designer@company.com to ['design-review@company.com']; ensure the review email includes the exported asset and add label 'design-review'. "
            "No need to log the run."
        ),
        actions=[
            # Create the same-day review cycle (rv- prefix per ID_RULE)
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T11:45:00Z",
                "timestamp": "2024-08-23T11:45:00Z",
                "request_id": "rv-001",
            }),

            # Export the asset to attach (en- prefix)
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:45:00Z",
                "request_id": "en-001",
            }),

            # Kickoff governance tag per GOV_AT_KICKOFF
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:45:00Z",
                "request_id": "up-001",
            }),

            # THREAD_POLICY: continue same-day thread if present
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — art_001 — 2024-08-23",
                "participant_email": "design-review@company.com",
            }),

            # Start (or continue) the review email using the template
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_001 — 2024-08-23",  # email.review_request.v2_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-08-23T11:45:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                # email.review_request.v2_body
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-23T11:45:00Z",
                "request_id": "em-002",
            }),

            # Apply the requested email label (from instruction)
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001",
                "add_labels": ["design-review"],
                "timestamp": "2024-08-23T11:45:00Z",
                "request_id": "em-003",
            }),
        ],
        outputs=[
            '"cycle_id":"rev-art_001-20240823-001"',
            '"cycle_status":"IN_FLIGHT"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_001-20240823-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"labels":["design-review"]',
            # '"tags":["needs-review", "responsive", "hero", "landing-page"]',
        ],
    ),
    # TASK_51 — Email-based design review kickoff (art_001)
    Task(
        annotator="0",
        user_id="TASK_51",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-09-02T09:05:00Z. "
            "Monday stand-up is in an hour—start an email-based design review for Figma artifact art_001 using export profile 'PNG 2x'; "
            "keep a single email thread per artifact for the day and continue in the existing thread if one has already started; "
            "ensure the review email includes the exported asset sent to ['lisa.marketing@company.com']."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240902-001",
                "artifact_id": "art_001",
                "started_at": "2024-09-02T09:05:00Z",
                "timestamp": "2024-09-02T09:05:00Z",
                "request_id": "rv-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-09-02T09:05:00Z",
                "request_id": "en-001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-09-02T09:05:00Z",
                "request_id": "up-001",
            }),
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — art_001 — 2024-09-02",
                "participant_email": "lisa.marketing@company.com",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_001 — 2024-09-02",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["lisa.marketing@company.com"],
                "timestamp": "2024-09-02T09:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-09-02T09:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-09-02T09:05:00Z",
                "ended_at": "2024-09-02T09:05:00Z",
                "timestamp": "2024-09-02T09:05:00Z",
                "request_id": "rv-002",
            }),
        ],
        outputs=[
            '"cycle_id":"rev-art_001-20240902-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_001-20240902-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["needs-review"]',
            '"run_id":"run_rv-002"',
            '"status":"completed"',
        ],
    )
    ,
    # TASK_52 — A11Y report (invalid categories → fail cleanly per ERROR_RULE)
    Task(
        annotator="0",
        user_id="TASK_52",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-24T11:00:00Z. "
            "With QA noting sizing quirks on dashboards, for audit audit_002 on artifact art_008 review findings across "
            "['COLOR_CONTRAST','FOCUS_ORDER']; generate a PDF accessibility report based strictly on those findings; "
            "mark the audit completed; email the report to ['design-review@company.com'] using the generic template and apply the email label 'a11y-report'; "
            "and do not record the run."
        ),
        actions=[
            # Scope strictly to allowed A11Y categories
            Action(name="list_audit_findings_a11y", kwargs={
                "audit_id": "audit_002", "violation_type": "COLOR_CONTRAST"
            }),
            Action(name="list_audit_findings_a11y", kwargs={
                "audit_id": "audit_002", "violation_type": "FOCUS_ORDER"
            }),

            # Generate the PDF report
            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_008", "audit_id": "audit_002", "format": "pdf",
                "timestamp": "2024-08-24T11:00:00Z", "request_id": "au-001",
            }),

            # Mark audit completed
            Action(name="update_audit_status", kwargs={
                "audit_id": "audit_002", "status": "COMPLETED", "updated_at": "2024-08-24T11:00:00Z",
                "timestamp": "2024-08-24T11:00:00Z", "request_id": "au-002",
            }),

            # Email the report using the generic template (subject/body from rules)
            Action(name="create_gmail_thread", kwargs={
                "subject": "Update — 2024-08-24",  # email.generic_plain.v1_subject
                "sender_email": "design-review@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-08-24T11:00:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "design-review@company.com",
                "body_html": "Hello,\nPlease see details attached.\nThanks.",  # email.generic_plain.v1
                "attachments_asset_ids": ["exp-art_008-20240824-pdf-001"],
                "timestamp": "2024-08-24T11:00:00Z", "request_id": "em-002",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001", "add_labels": ["a11y-report"],
                "timestamp": "2024-08-24T11:00:00Z", "request_id": "em-003",
            }),

        ],
        outputs=[
            '"audit_id":"audit_002"',
            '"report_asset_id":"exp-art_008-20240824-pdf-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"labels":["a11y-report"]',
            '"status":"completed"',
        ],

    )
    ,
    # TASK_53 — Email-based review kickoff (art_003) with label
    Task(
        annotator="0",
        user_id="TASK_53",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-24T09:40:00Z. "
            "The UX guild wants early eyes on tokens—initiate an email-based design review of Figma artifact art_003 using export profile 'PNG 2x', "
            "sent from sarah.designer@company.com to ['ux-team@company.com']; ensure the review email includes the exported asset and add label 'design-review'."
            "Dont record the run."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_003-20240824-001",
                "artifact_id": "art_003",
                "started_at": "2024-08-24T09:40:00Z",
                "timestamp": "2024-08-24T09:40:00Z",
                "request_id": "rv-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_003",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T09:40:00Z",
                "request_id": "en-001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_003",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-24T09:40:00Z",
                "request_id": "up-001",
            }),
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — art_003 — 2024-08-24",
                "participant_email": "ux-team@company.com",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_003 — 2024-08-24",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["ux-team@company.com"],
                "timestamp": "2024-08-24T09:40:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_003.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-24T09:40:00Z",
                "request_id": "em-002",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001",
                "add_labels": ["design-review"],
                "timestamp": "2024-08-24T09:40:00Z",
                "request_id": "em-003",
            }),

        ],
        outputs=[
            '"cycle_id":"rev-art_003-20240824-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_003-20240824-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"labels":["design-review"]',
            # '"tags":["needs-review"]',
        ],
    )
    ,
    # TASK_54 — Sync latest message (thread_009 → art_009) — fail cleanly if no messages
    Task(
        annotator="0",
        user_id="TASK_54",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-23T18:30:00Z. "
            "Capture end-of-day decisions—sync the newest message from Gmail thread thread_009 into Figma artifact art_009 as a comment; "
            "include the source message reference if one exists (otherwise proceed without it); "
            "then reply in the same thread using the sync-confirmation template to acknowledge the sync, "
            "apply the email label 'synced-to-figma', and record the sync."
        ),
        actions=[
            # Read thread and list messages to attempt retrieving the latest
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_009"}),
            Action(name="list_gmail_messages", kwargs={"thread_id": "thread_009"}),

            # Create the Figma comment (source_message_id provided only if available)
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_009",
                "author_email": "design-review@company.com",
                "content": "Synced from Gmail thread thread_009 on 2024-08-23.",  # figma.comment.sync template
                "source_message_id_nullable": 'msg_010',
                "timestamp": "2024-08-23T18:30:00Z",
                "request_id": "up-001",
            }),

            # Reply in-thread with the sync-confirmation template
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_009",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Thread thread_009 synced to art_009 on 2024-08-23.",  # email.sync_confirmation.v1
                "timestamp": "2024-08-23T18:30:00Z",
                "request_id": "em-001",
            }),

            # Apply the requested label (update-prefixed request_id)
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_009",
                "add_labels": ["synced-to-figma"],
                "timestamp": "2024-08-23T18:30:00Z",
                "request_id": "up-002",
            }),

            # Record the run
            Action(name="record_automation_run", kwargs={
                "task_name": "sync_email_to_figma",
                "status": "completed",
                "started_at": "2024-08-23T18:30:00Z",
                "ended_at": "2024-08-23T18:30:00Z",
                "timestamp": "2024-08-23T18:30:00Z",
                "request_id": "up-003",
            }),
        ],
        outputs=[
            '"thread_id":"thread_009"',
            '"comment_id":"comment_up-001"',
            '"message_id":"msg_em-001"',
            '"labels":["synced-to-figma"]',
            '"run_id":"run_up-003"',
            '"status":"completed"',
        ],

    )
    ,
    Task(
        annotator="0",
        user_id="TASK_55",
        instruction=(
            "You are the design review coordinator and the time is 2024-09-02T12:20:00Z. "
            "A blocker ping just landed—For review cycle cycle_012, issue a changes-requested update to "
            "['alex.dev@company.com', 'mike.ux@company.com'] with labels ['Design','design-review'];  "
            "Automation run record is not needed."
        ),
        actions=[
            Action(name="get_review_cycle", kwargs={"cycle_id": "cycle_012"}),

            # Update-type ⇒ use up- prefix
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_012",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-09-02T12:20:00Z",
                "timestamp": "2024-09-02T12:20:00Z",
                "request_id": "up-001",
            }),

            # THREAD_POLICY: continue same-day thread (no create/search)
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_012",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["alex.dev@company.com", "mike.ux@company.com"],  # <-- address recipients
                "body_html": "Changes requested for art_012. Continuing in today’s thread.",
                "timestamp": "2024-09-02T12:20:00Z",
                "request_id": "em-001",
            }),

            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_012",
                "add_labels": ["Design", "design-review"],
                "timestamp": "2024-09-02T12:20:00Z",
                "request_id": "em-002",
            }),

            # Minimal attach; update-type ⇒ up- prefix
            Action(name="attach_thread_to_review_cycle", kwargs={
                "cycle_id": "cycle_012",
                "thread_id": "thread_012",
                "updated_at": "2024-09-02T12:20:00Z",
                "timestamp": "2024-09-02T12:20:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_012"',
            '"thread_id":"thread_012"',
            # Optionally:
            # '"message_id":"msg_em-001"',
            # '"labels":["Design","design-review"]',
        ],
    )

    ,
    # TASK_56 — Approvals append (single approval; no quorum)
    Task(
        annotator="0",
        user_id="TASK_56",
        instruction=(
            "You are the review program manager and the time is 2024-08-23T15:20:00Z. "
            "A final sign-off is pending—For review cycle cycle_007, record approvals for "
            "['sarah.designer@company.com'] at ['2024-08-23T15:25:00Z'], and mark quorum reached if applicable."
        ),
        actions=[
            Action(name="update_review_approval", kwargs={
                "cycle_id": "cycle_007",
                "approver_email": "sarah.designer@company.com",
                "approved_ts_nullable": "2024-08-23T15:25:00Z",
                "timestamp": "2024-08-23T15:20:00Z",
                "request_id": "rv-001",
            }),
            # Quorum not met (needs ≥2 same-day approvals) → no status/tag change
            Action(name="record_automation_run", kwargs={
                "task_name": "approvals_append",
                "status": "completed",
                "started_at": "2024-08-23T15:20:00Z",
                "ended_at": "2024-08-23T15:20:00Z",
                "timestamp": "2024-08-23T15:20:00Z",
                "request_id": "rv-002",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_007"',
            '"approver":"sarah.designer@company.com"',
            '"run_id":"run_rv-002"',
            '"status":"completed"',
        ],
    )
    ,
    # TASK_57 — Release handoff (art_008) with tagging
    Task(
        annotator="0",
        user_id="TASK_57",
        instruction=(
            "You are the release publisher and the time is 2024-08-19T17:10:00Z. "
            "Marketing wants a preview for tomorrow’s newsletter—share a release handoff for artifact art_008 referencing release_004, "
            "include an exported asset 'PNG 2x' in the email from alex.dev@company.com to ['lisa.marketing@company.com']."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_004"}),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_008",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-19T17:10:00Z",
                "request_id": "en-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — release_004 — 2024-08-19",
                "sender_email": "alex.dev@company.com",
                "recipients": ["lisa.marketing@company.com"],
                "timestamp": "2024-08-19T17:10:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "alex.dev@company.com",
                "body_html": "Hello stakeholders,\nPlease find the release notes for release_004, including changes.\nRegards.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-19T17:10:00Z",
                "request_id": "em-002",
            }),
            # Per RELEASE_TAGGING_RULE add released/<YYYYMMDD> with instruction date
            Action(name="governance_update", kwargs={
                "artifact_id": "art_008",
                "add_tags": ["released/20240819"],
                "remove_tags": [],
                "timestamp": "2024-08-19T17:10:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-19T17:10:00Z",
                "ended_at": "2024-08-19T17:10:00Z",
                "timestamp": "2024-08-19T17:10:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            # '"previous_release_id":"release_004"',
            # #'"release_id":"rel-art_008-20240819-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_008-20240819-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["released/20240819"]',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )
    ,
    # TASK_58 — Governance update + note in day’s review thread (art_003)
    Task(
        annotator="0",
        user_id="TASK_58",
        instruction=(
            "You are the governance steward and the time is 2024-08-24T10:05:00Z. "
            "Component coverage just expanded—update tags on artifact art_003 by adding ['components', 'tokens'] and removing []; "
            "record the update and keep a note in the day’s review thread, sending the note from sarah.designer@company.comto['design-review@company.com'] "
            "using the generic update email template (subject: 'Update — {date}')."
        ),
        actions=[
            Action(name="governance_update", kwargs={
                "artifact_id": "art_003",
                "add_tags": ["components", "tokens"],
                "remove_tags": [],
                "timestamp": "2024-08-24T10:05:00Z",
                "request_id": "up-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Update — 2024-08-24",  # email.generic_plain.v1_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-08-24T10:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hello,\nPlease see details attached.\nThanks.",  # email.generic_plain.v1
                "timestamp": "2024-08-24T10:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "governance_update",
                "status": "completed",
                "started_at": "2024-08-24T10:05:00Z",
                "ended_at": "2024-08-24T10:05:00Z",
                "timestamp": "2024-08-24T10:05:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"artifact_id":"art_003"',
            # '"tags":["components","tokens"]',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    )
    ,
    # TASK_59 — Email-based design review kickoff (art_010)
    Task(
        annotator="0",
        user_id="TASK_59",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-09-02T12:15:00Z. "
            "A device matrix check is queued—initiate an email-based design review of Figma artifact art_010 using export profile 'PNG 2x', "
            "from sarah.designer@company.com to ['emma.brand@company.com']; keep the day’s thread consistent and include the exported asset."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_010-20240902-001",
                "artifact_id": "art_010",
                "started_at": "2024-09-02T12:15:00Z",
                "timestamp": "2024-09-02T12:15:00Z",
                "request_id": "rv-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_010",
                "export_profile": "PNG 2x",
                "timestamp": "2024-09-02T12:15:00Z",
                "request_id": "en-001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_010",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-09-02T12:15:00Z",
                "request_id": "up-001",
            }),
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — art_010 — 2024-09-02",
                "participant_email": "emma.brand@company.com",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_010 — 2024-09-02",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["emma.brand@company.com"],
                "timestamp": "2024-09-02T12:15:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_010.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-09-02T12:15:00Z",
                "request_id": "em-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-09-02T12:15:00Z",
                "ended_at": "2024-09-02T12:15:00Z",
                "timestamp": "2024-09-02T12:15:00Z",
                "request_id": "rv-002",
            }),
        ],
        outputs=[
            '"cycle_id":"rev-art_010-20240902-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_010-20240902-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"tags":["needs-review"]',
            '"run_id":"run_rv-002"',
            '"status":"completed"',
        ],
    )
    ,
    # TASK_60 — Release handoff (art_005) with tagging
    Task(
        annotator="0",
        user_id="TASK_60",
        instruction=(
            "You are the release publisher and the time is 2024-08-20T13:30:00Z. "
            "Partner teams need a heads-up before staging—share a release handoff for artifact art_005 referencing release_002, "
            "include an exported asset 'PNG 2x' in the email from mike.ux@company.com to ['sarah.designer@company.com', 'alex.dev@company.com']."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_002"}),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_005",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-20T13:30:00Z",
                "request_id": "en-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — release_002 — 2024-08-20",  # <-- reference release_002
                "sender_email": "mike.ux@company.com",
                "recipients": ["sarah.designer@company.com", "alex.dev@company.com"],
                "timestamp": "2024-08-20T13:30:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "mike.ux@company.com",
                "body_html": "Hello stakeholders,\nPlease find the release notes for release_002, including changes.\nRegards.",
                # <-- reference release_002
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-20T13:30:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_005",
                "add_tags": ["released/20240820"],
                "remove_tags": [],
                "timestamp": "2024-08-20T13:30:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-20T13:30:00Z",
                "ended_at": "2024-08-20T13:30:00Z",
                "timestamp": "2024-08-20T13:30:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_005-20240820-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_61",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-24T17:15:00Z. "
            "Capture the late-day update by reflecting Gmail thread thread_010 in Figma artifact art_002 with an attributed comment "
            "(no per-message id required), acknowledge in-thread using the sync-confirmation template, "
            "apply the standard 'synced-to-figma' label to the thread, and record the sync."
        ),
        actions=[
            # Read the thread context (non-blocking; used for consistency)
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_010"}),

            # Figma note (creation → 'en-' request_id)
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_002",
                "author_email": "design-review@company.com",
                "content": "Synced from Gmail thread thread_010 on 2024-08-24.",  # figma.comment.sync template
                "timestamp": "2024-08-24T17:15:00Z",
                "request_id": "en-001",
            }),

            # In-thread confirmation (sync-confirmation template)
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_010",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Thread thread_010 synced to art_002 on 2024-08-24.",  # email.sync_confirmation.v1
                "timestamp": "2024-08-24T17:15:00Z",
                "request_id": "em-001",
            }),

            # Apply the requested label
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_010",
                "add_labels": ["synced-to-figma"],
                "timestamp": "2024-08-24T17:15:00Z",
                "request_id": "up-001",
            }),

            # Record the automation run
            Action(name="record_automation_run", kwargs={
                "task_name": "sync_email_to_figma",
                "status": "completed",
                "started_at": "2024-08-24T17:15:00Z",
                "ended_at": "2024-08-24T17:15:00Z",
                "timestamp": "2024-08-24T17:15:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"thread_id":"thread_010"',
            '"comment_id":"comment_en-001"',
            '"message_id":"msg_em-001"',
            '"labels":["synced-to-figma"]',
            '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_62",
        instruction=(
            "You are the review program manager and the time is 2024-09-02T10:00:00Z. "
            "After a clean smoke test, for review cycle cycle_003 record approvals for ['lisa.marketing@company.com'] at ['2024-09-02T10:05:00Z']; "
            "mark the cycle approved only if quorum (two same-day approvals) is reached; otherwise leave the status unchanged. "
            "Email a confirmation to ['design-review@company.com'] using the generic template (continue an existing same-day thread if found), "
            "link the thread to cycle_003, and do not record the automation run."
        ),
        actions=[
            Action(name="get_review_cycle", kwargs={"cycle_id": "cycle_003"}),

            Action(name="update_review_approval", kwargs={
                "cycle_id": "cycle_003",
                "approver_email": "lisa.marketing@company.com",
                "approved_ts_nullable": "2024-09-02T10:05:00Z",
                "timestamp": "2024-09-02T10:00:00Z",
                "request_id": "rv-001",
            }),

            # Quorum not proven here → no status change action

            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Update — 2024-09-02",
                "participant_email": "design-review@company.com",
            }),

            Action(name="create_gmail_thread", kwargs={
                "subject": "Update — 2024-09-02",  # email.generic_plain.v1_subject
                "sender_email": "design-review@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-09-02T10:00:00Z",
                "request_id": "em-001",
            }),

            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "design-review@company.com",
                "body_html": "Hello,\nPlease see details attached.\nThanks.",  # email.generic_plain.v1
                "timestamp": "2024-09-02T10:00:00Z",
                "request_id": "em-002",
            }),

            Action(name="attach_thread_to_review_cycle", kwargs={
                "cycle_id": "cycle_003",
                "thread_id": "thr_em-001",
                "updated_at": "2024-09-02T10:00:00Z",
                "timestamp": "2024-09-02T10:00:00Z",
                "request_id": "rv-002",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_003"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_63",
        instruction=(
            "You are the governance steward and the time is 2024-08-23T09:05:00Z. "
            "Align metadata before the design review—update tags on artifact art_001 by adding ['design-system','responsive'] and removing ['needs-review']; "
            "send a same-day note from sarah.designer@company.com to ['design-review@company.com'] using the generic template "
            "(continue an existing same-day thread if present), apply label 'governance', and record the update."
        ),
        actions=[
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["design-system", "responsive"],
                "remove_tags": ["needs-review"],
                "timestamp": "2024-08-23T09:05:00Z",
                "request_id": "up-001",
            }),
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Update — 2024-08-23",
                "participant_email": "design-review@company.com",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Update — 2024-08-23",  # email.generic_plain.v1_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-08-23T09:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hello,\nPlease see details attached.\nThanks.",  # email.generic_plain.v1
                "timestamp": "2024-08-23T09:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001",
                "add_labels": ["governance"],
                "timestamp": "2024-08-23T09:05:00Z",
                "request_id": "up-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "governance_update",
                "status": "completed",
                "started_at": "2024-08-23T09:05:00Z",
                "ended_at": "2024-08-23T09:05:00Z",
                "timestamp": "2024-08-23T09:05:00Z",
                "request_id": "up-003",
            }),
        ],
        outputs=[
            '"artifact_id":"art_001"',
            # '"tags":["hero","landing-page","design-system","responsive"]',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"labels":["governance"]',
            '"run_id":"run_up-003"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_64",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-09-02T10:40:00Z. "
            "Share the morning build with leadership—start an email-based design review for Figma artifact art_002 using export profile 'PNG 2x'; "
            "keep a single email thread per artifact for the day and continue in an existing thread if one has already started; "
            "ensure the review email includes the exported asset sent to ['stakeholders@company.com','product-managers@company.com']; "
            "add the label 'design-review'. Dont need to record the automation run."
        ),
        actions=[
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — art_002 — 2024-09-02",
                "participant_email": "stakeholders@company.com",
            }),
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_002-20240902-001", "artifact_id": "art_002",
                "started_at": "2024-09-02T10:40:00Z",
                "timestamp": "2024-09-02T10:40:00Z", "request_id": "rv-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_002", "export_profile": "PNG 2x",
                "timestamp": "2024-09-02T10:40:00Z", "request_id": "en-001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_002", "add_tags": ["needs-review"], "remove_tags": [],
                "timestamp": "2024-09-02T10:40:00Z", "request_id": "up-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_002 — 2024-09-02",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com", "product-managers@company.com"],
                "timestamp": "2024-09-02T10:40:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_002.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-09-02T10:40:00Z", "request_id": "em-002",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001", "add_labels": ["design-review"],
                "timestamp": "2024-09-02T10:40:00Z", "request_id": "up-002",
            }),
        ],
        outputs=[
            '"cycle_id":"rev-art_002-20240902-001"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_002-20240902-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"labels":["design-review"]',
            # '"tags":["needs-review"]',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_65",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-09-02T13:40:00Z. Multiple teams are touching shared primitives—run a consolidated email-based design review and attach 'PNG 2x' exports from ['art_009','art_010'] in a single message to ['stakeholders@company.com','ux-team@company.com']; use the email.review_request_consolidated.v1 template with subject 'Review Request — Consolidated — 2024-09-02'; maintain one consolidated thread for the day, add label 'design-review'. Do not record the automation run."
        ),
        actions=[
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — Consolidated — 2024-09-02",
                "participant_email": "stakeholders@company.com",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_009", "export_profile": "PNG 2x",
                "timestamp": "2024-09-02T13:40:00Z", "request_id": "en-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_010", "export_profile": "PNG 2x",
                "timestamp": "2024-09-02T13:40:00Z", "request_id": "en-002",
            }),

            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — Consolidated — 2024-09-02",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com", "ux-team@company.com"],
                "timestamp": "2024-09-02T13:40:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x exports.\nThanks.",
                "attachments_asset_ids": ["asset_en-001", "asset_en-002", ],
                "timestamp": "2024-09-02T13:40:00Z", "request_id": "em-002",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001", "add_labels": ["design-review"],
                "timestamp": "2024-09-02T13:40:00Z", "request_id": "up-001",
            }),

        ],
        outputs=[
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"asset_ids":["asset_en-001","asset_en-002"]',
            '"export_ids":["exp-art_009-20240902-png-001","exp-art_010-20240902-png-001"]',
            '"labels":["design-review"]',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_66",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-09-02T17:10:00Z. "
            "Grid updates just landed—start an email-based design review for Figma artifact art_004 using export profile 'PNG 2x'; "
            "keep a single email thread per artifact for the day and continue in the existing thread if one has already started; "
            "ensure the review email  "
            "includes the exported asset, sent from sarah.designer@company.com to ['design-review@company.com']; "
            "as part of kickoff, add the tag 'needs-review' to the artifact; add the Gmail label 'design-review'; "
            "Dont need to record the automation run."
        ),
        actions=[
            # 1) Export the asset for the email
            Action(name="export_assets", kwargs={
                "artifact_id": "art_004",
                "export_profile": "PNG 2x",
                "timestamp": "2024-09-02T17:10:00Z",
                "request_id": "en-001",
            }),
            # 2) Apply kickoff governance tag
            Action(name="governance_update", kwargs={
                "artifact_id": "art_004",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-09-02T17:10:00Z",
                "request_id": "up-001",
            }),
            # 3) Maintain same-day continuity (ok if none found)
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — art_004 — 2024-09-02",
                "participant_email": "design-review@company.com",
            }),
            # 4) Create/continue the review thread using the deterministic template
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_004 — 2024-09-02",  # email.review_request.v1_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-09-02T17:10:00Z",
                "request_id": "em-001",
            }),
            # 5) Send the message with the exported asset attached
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com"],
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_004.\nThanks.",
                # email.review_request.v1
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-09-02T17:10:00Z",
                "request_id": "em-002",
            }),
            # 6) Label the thread for tracking
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001",
                "add_labels": ["design-review"],
                "timestamp": "2024-09-02T17:10:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_004-20240902-png-001"',
            # '"tags":["needs-review"]',
            '"labels":["design-review"]',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="TASK_67",
        instruction=(
            "You are the design review coordinator and the time is 2024-09-02T16:40:00Z. "
            "After a targeted patch shipped, request a re-review for Figma artifact art_005 addressed to "
            "['sarah.designer@company.com','mike.ux@company.com'] using the standard re-review notice; "
            "continue in the established same-day email thread for the artifact ( 'User Profile Screen Implementation' ) (do not start a new subject), "
            "apply label 'design-review', and record the update."
        ),
        actions=[
            # Locate the established same-day thread (no new subject allowed)
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "User Profile Screen Implementation",
            }),

            # Continue in the existing thread with the deterministic re-review template
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_007",  # existing same-day thread
                "sender_email": "sarah.designer@company.com",
                "recipients": ["sarah.designer@company.com", "mike.ux@company.com"],
                "body_html": "Fixes have been applied on art_005; please re-review the latest assets.",
                # email.rereview_notice.v1
                "timestamp": "2024-09-02T16:40:00Z",
                "request_id": "em-001",
            }),

            # Apply requested label
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_007",
                "add_labels": ["design-review"],
                "timestamp": "2024-09-02T16:40:00Z",
                "request_id": "up-001",
            }),

            # Record the update
            Action(name="record_automation_run", kwargs={
                "task_name": "rereview_kickoff",
                "status": "completed",
                "started_at": "2024-09-02T16:40:00Z",
                "ended_at": "2024-09-02T16:40:00Z",
                "timestamp": "2024-09-02T16:40:00Z",
                "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"artifact_id":"art_005"',
            '"thread_id":"thread_007"',
            '"message_id":"msg_em-001"',
            '"labels":["design-review"]',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_68",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-09-02T09:20:00Z. "
            "Contrast checks are gating the handoff—For audit audit_002 on artifact art_008, review findings across ['COLOR_CONTRAST'], "
            "produce a PDF accessibility report strictly from those findings, mark the audit completed, and email the PDF "
            "from design-review@company.com to ['design-review@company.com'] using the generic template; "
            "verify the sent thread. Dont need to record the automation run."
        ),
        actions=[
            Action(name="list_audit_findings_a11y",
                   kwargs={"audit_id": "audit_002", "violation_type": "COLOR_CONTRAST"}),

            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_008", "audit_id": "audit_002", "format": "pdf",
                "timestamp": "2024-09-02T09:20:00Z", "request_id": "au-001",
            }),

            # Use up- prefix for updates
            Action(name="update_audit_status", kwargs={
                "audit_id": "audit_002", "status": "COMPLETED",
                "updated_at": "2024-09-02T09:20:00Z",
                "timestamp": "2024-09-02T09:20:00Z", "request_id": "up-001",
            }),

            Action(name="create_gmail_thread", kwargs={
                "subject": "Update — 2024-09-02",
                "sender_email": "design-review@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-09-02T09:20:00Z", "request_id": "em-001",
            }),

            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "design-review@company.com",
                "recipients": ["design-review@company.com"],
                "body_html": "Hello,\nPlease see details attached.\nThanks.",  # email.generic_plain.v1
                "attachments_asset_ids": ["exp-art_008-20240902-pdf-001"],  # matches GenerateAuditReport output
                "timestamp": "2024-09-02T09:20:00Z", "request_id": "em-002",
            }),

            Action(name="get_gmail_thread", kwargs={
                "thread_id": "thr_em-001", "request_id": "em-003",
            }),

            # Action(name="record_automation_run", kwargs={
            #     "task_name": "a11y_audit_report", "status": "completed",
            #     "started_at": "2024-09-02T09:20:00Z", "ended_at": "2024-09-02T09:20:00Z",
            #     "timestamp": "2024-09-02T09:20:00Z", "request_id": "up-002",
            # }),
        ],
        outputs=[
            '"audit_id":"audit_002"',
            '"asset_id":"exp-art_008-20240902-pdf-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            # '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_69",
        instruction=(
            "You are the design review coordinator and the time is 2024-09-02T11:05:00Z. "
            "Brand refresh assets landed—kick off an email-based design review for Figma artifact art_010 using export profile 'PNG 2x', "
            "from sarah.designer@company.com to ['design-review@company.com']; continue a same-day thread if one exists, "
            "ensure the review email includes the exported asset, apply label 'design-review', and record the activity."
        ),
        actions=[
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — art_010 — 2024-09-02",
                "participant_email": "design-review@company.com",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_010", "export_profile": "PNG 2x",
                "timestamp": "2024-09-02T11:05:00Z", "request_id": "en-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_010 — 2024-09-02",  # email.review_request.v1_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-09-02T11:05:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_010.\nThanks.",
                # email.review_request.v1
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-09-02T11:05:00Z", "request_id": "em-002",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001", "add_labels": ["design-review"],
                "timestamp": "2024-09-02T11:05:00Z", "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff", "status": "completed",
                "started_at": "2024-09-02T11:05:00Z", "ended_at": "2024-09-02T11:05:00Z",
                "timestamp": "2024-09-02T11:05:00Z", "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"artifact_id":"art_010"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_010-20240902-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"labels":["design-review"]',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_70",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-09-02T13:05:00Z. "
            "Shared navigation is in scope—initiate an email-based design review of Figma artifact art_012 using export profile 'PNG 2x', "
            "from sarah.designer@company.com to ['alex.dev@company.com','mike.ux@company.com']; "
            "keep the day’s thread consistent, include the exported asset, apply label 'design-review', verify the thread, No need to record the automation run."
        ),
        actions=[
            # Add required kickoff tag per review_kickoff workflow
            Action(name="governance_update", kwargs={
                "artifact_id": "art_012",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-09-02T13:05:00Z",
                "request_id": "up-001",
            }),

            Action(name="export_assets", kwargs={
                "artifact_id": "art_012", "export_profile": "PNG 2x",
                "timestamp": "2024-09-02T13:05:00Z", "request_id": "en-001",
            }),

            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_012 — 2024-09-02",  # email.review_request.v1_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["alex.dev@company.com", "mike.ux@company.com"],
                "timestamp": "2024-09-02T13:05:00Z", "request_id": "em-001",
            }),

            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "sarah.designer@company.com",
                "recipients": ["alex.dev@company.com", "mike.ux@company.com"],
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_012.\nThanks.",
                # email.review_request.v1
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-09-02T13:05:00Z", "request_id": "em-002",
            }),

            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001", "add_labels": ["design-review"],
                "timestamp": "2024-09-02T13:05:00Z", "request_id": "up-002",
            }),

            # Verify via thread metadata (more reliable than listing messages)
            Action(name="get_gmail_thread", kwargs={
                "thread_id": "thr_em-001", "request_id": "em-003",
            }),

            # Action(name="record_automation_run", kwargs={
            #     "task_name": "review_kickoff", "status": "completed",
            #     "started_at": "2024-09-02T13:05:00Z", "ended_at": "2024-09-02T13:05:00Z",
            #     "timestamp": "2024-09-02T13:05:00Z", "request_id": "rv-001",
            # }),
        ],
        outputs=[
            '"artifact_id":"art_012"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_012-20240902-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"labels":["design-review"]',
            # '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    )
    ,

    Task(
        annotator="0",
        user_id="TASK_71",
        instruction=(
            "You are the governance steward and the time is 2024-08-23T18:50:00Z. "
            "Sign-off landed—update tags on artifact art_003 by adding ['approved'] and removing ['needs-review']; "
            "send a same-day confirmation note from design-review@company.com to ['design-review@company.com'] "
            "using the generic template (continue the day’s thread if present), apply label 'governance', "
            "and record the update."
        ),
        actions=[
            Action(name="governance_update", kwargs={
                "artifact_id": "art_003",
                "add_tags": ["approved"],
                "remove_tags": ["needs-review"],
                "timestamp": "2024-08-23T18:50:00Z",
                "request_id": "up-001",
            }),
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Update — 2024-08-23",
                "participant_email": "design-review@company.com",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Update — 2024-08-23",  # email.generic_plain.v1_subject
                "sender_email": "design-review@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-08-23T18:50:00Z",
                "request_id": "em-002",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-002",
                "sender_email": "design-review@company.com",
                "recipients": ["design-review@company.com"],
                "body_html": "Hello,\nPlease see details attached.\nThanks.",  # email.generic_plain.v1
                "timestamp": "2024-08-23T18:50:00Z",
                "request_id": "em-003",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-002",
                "add_labels": ["governance"],
                "timestamp": "2024-08-23T18:50:00Z",
                "request_id": "up-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "governance_update",
                "status": "completed",
                "started_at": "2024-08-23T18:50:00Z",
                "ended_at": "2024-08-23T18:50:00Z",
                "timestamp": "2024-08-23T18:50:00Z",
                "request_id": "up-003",
            }),
        ],
        outputs=[
            '"artifact_id":"art_003"',
            # '"tags":["approved"]',
            '"thread_id":"thr_em-002"',
            '"message_id":"msg_em-003"',
            '"labels":["governance"]',
            '"run_id":"run_up-003"',
            '"status":"completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_72",
        instruction=(
            "You are the design review coordinator and the time is 2024-09-02T14:10:00Z. "
            "After a quick rollback test passed, request a re-review for Figma artifact art_001 addressed to ['sarah.designer@company.com'] "
            "using the standard re-review notice; continue the same-day review subject (use the existing thread 'Data Table Component Review'), "
            "apply label 'design-review', and record the update."
        ),
        actions=[
            # Prove the thread exists (log the lookup)
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Data Table Component Review",
            }),

            # Append to the actual thread from your data (no fabrication)
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_009",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["sarah.designer@company.com"],
                "body_html": "Fixes have been applied on art_001; please re-review the latest assets.",
                # email.rereview_notice.v1
                "timestamp": "2024-09-02T14:10:00Z",
                "request_id": "em-001",
            }),

            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_009",
                "add_labels": ["design-review"],
                "timestamp": "2024-09-02T14:10:00Z",
                "request_id": "up-001",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "rereview_kickoff",
                "status": "completed",
                "started_at": "2024-09-02T14:10:00Z",
                "ended_at": "2024-09-02T14:10:00Z",
                "timestamp": "2024-09-02T14:10:00Z",
                "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"artifact_id":"art_001"',
            '"thread_id":"thread_009"',
            '"message_id":"msg_em-001"',
            '"labels":["design-review"]',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_73",
        instruction=(
            "You are the design review coordinator and the time is 2024-09-02T14:50:00Z. "
            "A sidebar fix just landed—request a re-review for Figma artifact art_002 addressed to "
            "['mike.ux@company.com','alex.dev@company.com'] using the standard re-review notice; "
            "continue the existing same-day thread if present (look it up by participant 'mike.ux@company.com'; otherwise start one), "
            "apply label 'design-review', and record the update."
        ),
        actions=[
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Re-review Needed — art_002 — 2024-09-02",
                "participant_email": "mike.ux@company.com",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Re-review Needed — art_002 — 2024-09-02",  # email.rereview_notice.v1_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com"],
                "timestamp": "2024-09-02T14:50:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com"],
                "body_html": "Fixes have been applied on art_002; please re-review the latest assets.",
                # email.rereview_notice.v1
                "timestamp": "2024-09-02T14:50:00Z",
                "request_id": "em-002",
            }),
            Action(name="get_gmail_thread", kwargs={"thread_id": "thr_em-001"}),  # continuity read
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001",
                "add_labels": ["design-review"],
                "timestamp": "2024-09-02T14:50:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "rereview_kickoff",
                "status": "completed",
                "started_at": "2024-09-02T14:50:00Z",
                "ended_at": "2024-09-02T14:50:00Z",
                "timestamp": "2024-09-02T14:50:00Z",
                "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"artifact_id":"art_002"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"labels":["design-review"]',
            '"run_id":"run_rv-001"',
            '"status":"completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_74",
        instruction=(
            "You are the review program manager and the time is 2024-08-24T10:40:00Z. "
            "Ahead of the weekend freeze, for review cycle cycle_008 record approvals for "
            "['mike.ux@company.com','sarah.designer@company.com'] at "
            "['2024-08-24T10:45:00Z','2024-08-24T10:55:00Z']; "
            "if quorum is met as of the latest approval time, set the cycle to APPROVED, "
            "replace any 'needs-review' tags on the cycle’s artifacts with 'approved/20240824', "
            "No need to record automation run."
        ),
        actions=[
            Action(name="update_review_approval", kwargs={
                "cycle_id": "cycle_008",
                "approver_email": "mike.ux@company.com",
                "approved_ts_nullable": "2024-08-24T10:45:00Z",
                "timestamp": "2024-08-24T10:40:00Z",
                "request_id": "rv-001",
            }),
            Action(name="update_review_approval", kwargs={
                "cycle_id": "cycle_008",
                "approver_email": "sarah.designer@company.com",
                "approved_ts_nullable": "2024-08-24T10:55:00Z",
                "timestamp": "2024-08-24T10:40:00Z",
                "request_id": "rv-002",
            }),

            # Update-type => up- prefix; set at latest approval time
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_008",
                "status": "APPROVED",
                "updated_at": "2024-08-24T10:55:00Z",
                "timestamp": "2024-08-24T10:55:00Z",
                "request_id": "up-001",
            }),

            # Use CYCLE_ALIAS (cycle_008 ⇒ art_001) for deterministic governance update
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["approved/20240824"],
                "remove_tags": ["needs-review"],
                "timestamp": "2024-08-24T10:55:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_008"',
            '"cycle_status":"approved"',
            '"status":"completed"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_75",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-24T17:30:00Z. "
            "Capture the handoff chatter for Gmail thread thread_007 by reflecting the newest update as an attributed comment on Figma artifact art_005, "
            "acknowledge the sync in-thread , apply the 'synced-to-figma' label, "
            "verify delivery by reading the thread metadata."
        ),
        actions=[
            # Baseline read
            Action(name="get_gmail_thread", kwargs={
                "thread_id": "thread_007",
                "timestamp": "2024-08-24T17:30:00Z",
                "request_id": "em-001",
            }),
            Action(name="list_gmail_messages", kwargs={
                "thread_id": "thread_007",
                "timestamp": "2024-08-24T17:30:00Z",
                "request_id": "em-002",
            }),

            # Create the Figma comment (sync note)
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_005",
                "author_email": "design-review@company.com",
                "content": "Synced from Gmail thread thread_007 on 2024-08-24.",  # figma.comment.sync.v1
                "timestamp": "2024-08-24T17:30:00Z",
                "request_id": "en-001",
            }),

            # In-thread acknowledgement (continue existing thread; no new recipients)
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_007",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Thread thread_007 synced to art_005 on 2024-08-24.",  # email.sync_confirmation.v1
                "timestamp": "2024-08-24T17:30:00Z",
                "request_id": "em-003",
            }),

            # Apply the requested label
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_007",
                "add_labels": ["synced-to-figma"],
                "timestamp": "2024-08-24T17:30:00Z",
                "request_id": "up-001",
            }),

            # Verify delivery by reading thread metadata (labels reflect the sync)
            Action(name="get_gmail_thread", kwargs={
                "thread_id": "thread_007",
                "timestamp": "2024-08-24T17:30:00Z",
                "request_id": "em-004",
            }),

            # Record the automation run
            Action(name="record_automation_run", kwargs={
                "task_name": "sync_email_to_figma",
                "status": "completed",
                "started_at": "2024-08-24T17:30:00Z",
                "ended_at": "2024-08-24T17:30:00Z",
                "timestamp": "2024-08-24T17:30:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"thread_id":"thread_007"',
            '"comment_id":"comment_en-001"',
            '"labels":["synced-to-figma"]',
            '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_76",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-24T17:45:00Z. "
            "Close the loop on the settings epic by ensuring the latest note from Gmail thread thread_011 is reflected in Figma artifact art_011 "
            "as an attributed comment. Acknowledge in the same Gmail thread using the sync-confirmation template, apply the 'synced-to-figma' label, "
            "verify delivery by reading the thread metadata, and record the sync."
        ),
        actions=[
            # Baseline reads (OK to keep)
            Action(name="get_gmail_thread", kwargs={
                "thread_id": "thread_011",
            }),
            Action(name="list_gmail_messages", kwargs={
                "thread_id": "thread_011",
            }),

            # Use standard figma.comment.sync.v1 body; omit source_message_id to avoid nondeterminism
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_011",
                "author_email": "design-review@company.com",
                "content": "Synced from Gmail thread thread_011 on 2024-08-24.",
                "timestamp": "2024-08-24T17:45:00Z",
                "request_id": "en-001",
            }),

            # In-thread acknowledgement (continue the same thread)
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_011",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Thread thread_011 synced to art_011 on 2024-08-24.",
                "timestamp": "2024-08-24T17:45:00Z",
                "request_id": "em-001",
            }),

            # Apply the requested label
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_011",
                "add_labels": ["synced-to-figma"],
                "timestamp": "2024-08-24T17:45:00Z",
                "request_id": "up-001",
            }),

            # Verify via thread metadata (list_gmail_messages cannot surface the new reply with current tools)
            Action(name="get_gmail_thread", kwargs={
                "thread_id": "thread_011",
                "timestamp": "2024-08-24T17:45:00Z",
                "request_id": "em-002",
            }),

            # Record the automation run
            Action(name="record_automation_run", kwargs={
                "task_name": "sync_email_to_figma",
                "status": "completed",
                "started_at": "2024-08-24T17:45:00Z",
                "ended_at": "2024-08-24T17:45:00Z",
                "timestamp": "2024-08-24T17:45:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"thread_id":"thread_011"',
            '"comment_id":"comment_en-001"',
            '"labels":["synced-to-figma"]',
            '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_77",
        instruction=(
            "You are the design-system auditor and the time is 2024-08-24T11:20:00Z. "
            "With the library version bump pending, for audit audit_003 on artifact art_003 review design-system findings "
            "covering ['COMPONENT_MISMATCH','SPACING'], generate a PDF report grounded in those findings, mark the audit completed, "
            "email the PDF from design-review@company.com to ['design-review@company.com'] using the generic template, "
            "verify the sent thread, and do not record the automation run."
        ),
        actions=[
            Action(name="list_audit_findings_ds",
                   kwargs={"audit_id": "audit_003", "finding_type": "COMPONENT_MISMATCH"}),
            Action(name="list_audit_findings_ds",
                   kwargs={"audit_id": "audit_003", "finding_type": "SPACING"}),

            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_003",
                "audit_id": "audit_003",
                "format": "pdf",
                "timestamp": "2024-08-24T11:20:00Z",
                "request_id": "au-001",
            }),

            # Update-type => up- prefix
            Action(name="update_audit_status", kwargs={
                "audit_id": "audit_003",
                "status": "COMPLETED",
                "updated_at": "2024-08-24T11:20:00Z",
                "timestamp": "2024-08-24T11:20:00Z",
                "request_id": "up-001",
            }),

            Action(name="create_gmail_thread", kwargs={
                "subject": "Update — 2024-08-24",
                "sender_email": "design-review@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-08-24T11:20:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "design-review@company.com",
                "recipients": ["design-review@company.com"],
                "body_html": "Hello,\nPlease see details attached.\nThanks.",
                "attachments_asset_ids": ["exp-art_003-20240824-pdf-001"],  # <-- match GenerateAuditReport
                "timestamp": "2024-08-24T11:20:00Z",
                "request_id": "em-002",
            }),

            Action(name="get_gmail_thread", kwargs={
                "thread_id": "thr_em-001",
                "timestamp": "2024-08-24T11:20:00Z",
                "request_id": "em-003",
            }),
        ],
        outputs=[
            '"audit_id":"audit_003"',
            '"asset_id":"exp-art_003-20240824-pdf-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_78",
        instruction=(
            "You are the design-system auditor and the time is 2024-08-24T11:40:00Z. "
            "A component swap is under consideration—For audit audit_010 on artifact art_010, review design-system findings "
            "covering ['TOKENS']; produce a PDF report grounded in those findings; mark the audit completed; "
            "email the PDF from design-review@company.com to ['design-review@company.com'] using the generic template "
            "(subject: 'Update — 2024-08-24'); verify the sent thread by reading its metadata. No need to log the run."
        ),
        actions=[
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "audit_010", "finding_type": "TOKENS"
            }),
            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_010", "audit_id": "audit_010", "format": "pdf",
                "timestamp": "2024-08-24T11:40:00Z", "request_id": "au-001",
            }),
            # Update-type ⇒ use up- prefix
            Action(name="update_audit_status", kwargs={
                "audit_id": "audit_010", "status": "COMPLETED",
                "updated_at": "2024-08-24T11:40:00Z",
                "timestamp": "2024-08-24T11:40:00Z", "request_id": "up-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Update — 2024-08-24",
                "sender_email": "design-review@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-08-24T11:40:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001", "sender_email": "design-review@company.com",
                "body_html": "Hello,\nPlease see details attached.\nThanks.",
                "attachments_asset_ids": ["exp-art_010-20240824-pdf-001"],  # ← match tool output
                "timestamp": "2024-08-24T11:40:00Z", "request_id": "em-002",
            }),
            # Verify via thread metadata
            Action(name="get_gmail_thread", kwargs={
                "thread_id": "thr_em-001", "request_id": "em-003"
            }),
        ],
        outputs=[
            '"audit_id":"audit_010"',
            '"asset_id":"exp-art_010-20240824-pdf-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
        ],
    )

    ,

    Task(
        annotator="0",
        user_id="TASK_79",
        instruction=(
            "You are the design-system auditor and the time is 2024-09-02T11:20:00Z. "
            "Deliver a DS TOKENS–based PDF audit report for audit audit_012 on artifact art_012, "
            "ensure the audit is marked COMPLETED, and notify ['design-review@company.com'] via the generic email template "
            "(subject: 'Update — 2024-09-02') from design-review@company.com with the PDF attached; "
            "verify by reading the thread’s metadata. No need to log the run."
        ),
        actions=[
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "audit_012", "finding_type": "TOKENS"
            }),
            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_012", "audit_id": "audit_012", "format": "pdf",
                "timestamp": "2024-09-02T11:20:00Z", "request_id": "au-001",
            }),
            Action(name="update_audit_status", kwargs={
                "audit_id": "audit_012", "status": "COMPLETED",
                "updated_at": "2024-09-02T11:20:00Z",
                "timestamp": "2024-09-02T11:20:00Z", "request_id": "up-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Update — 2024-09-02",
                "sender_email": "design-review@company.com",
                "recipients": ["design-review@company.com"],
                "timestamp": "2024-09-02T11:20:00Z", "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "design-review@company.com",
                "recipients": ["design-review@company.com"],
                "body_html": "Hello,\nPlease see details attached.\nThanks.",
                "attachments_asset_ids": ["exp-art_012-20240902-pdf-001"],  # match GenerateAuditReport result
                "timestamp": "2024-09-02T11:20:00Z", "request_id": "em-002",
            }),
            Action(name="get_gmail_thread", kwargs={
                "thread_id": "thr_em-001",
                "timestamp": "2024-09-02T11:20:00Z", "request_id": "em-003",
            }),
        ],
        outputs=[
            '"audit_id":"audit_012"',
            '"asset_id":"exp-art_012-20240902-pdf-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_80",
        instruction=(
            "You are the audit lead and the time is 2024-08-23T14:00:00Z. "
            "Leadership requested a unified view—For audit audit_009 on artifact art_006, ensure both A11Y and DS dimensions are represented, "
            "produce a combined PDF report, leave a Figma comment confirming report delivery using the standard audit-report template, and record the activity."
        ),
        actions=[
            Action(name="get_audit", kwargs={"audit_id": "audit_009"}),

            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_006",
                "audit_id": "audit_009",
                "format": "pdf",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "au-001",
            }),

            Action(name="update_audit_status", kwargs={
                "audit_id": "audit_009",
                "status": "COMPLETED",
                "updated_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "up-001",
            }),

            # Template: "Audit report sent — {artifact_id} — {audit_id} — {date} — asset {asset_id}"
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_006",
                "author_email": "design-review@company.com",
                "content": "Audit report sent — art_006 — audit_009 — 2024-08-23 — asset exp-art_006-20240823-pdf-001",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "en-001",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "combined_audit_report",
                "status": "completed",
                "started_at": "2024-08-23T14:00:00Z",
                "ended_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"audit_id":"audit_009"',
            '"asset_id":"exp-art_006-20240823-pdf-001"',
            '"comment_id":"comment_en-001"',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_81",
        instruction=(
            "You are the review program manager and the time is 2024-08-24T09:50:00Z. "
            "Align with the Saturday cut—For review cycle cycle_010, record approvals for "
            "['alex.dev@company.com', 'mike.ux@company.com'] at ['2024-08-24T09:55:00Z', '2024-08-24T09:57:00Z'], "
            "set APPROVED at the latest timestamp if quorum, and record the activity."
        ),
        actions=[
            Action(name="get_review_cycle", kwargs={"cycle_id": "cycle_010"}),

            Action(name="update_review_approval", kwargs={
                "cycle_id": "cycle_010",
                "approver_email": "alex.dev@company.com",
                "approved_ts_nullable": "2024-08-24T09:55:00Z",
                "timestamp": "2024-08-24T09:50:00Z",
                "request_id": "rv-001",
            }),
            Action(name="update_review_approval", kwargs={
                "cycle_id": "cycle_010",
                "approver_email": "mike.ux@company.com",
                "approved_ts_nullable": "2024-08-24T09:57:00Z",
                "timestamp": "2024-08-24T09:50:00Z",
                "request_id": "rv-002",
            }),

            # Quorum reached → set APPROVED at the latest approval time
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_010",
                "status": "APPROVED",
                "updated_at": "2024-08-24T09:57:00Z",
                "timestamp": "2024-08-24T09:57:00Z",
                "request_id": "up-001",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "approvals_append",
                "status": "completed",
                "started_at": "2024-08-24T09:50:00Z",
                "ended_at": "2024-08-24T09:57:00Z",
                "timestamp": "2024-08-24T09:57:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_010"',
            '"cycle_status":"approved"',  # judge expects lowercase in outputs even though status set is "APPROVED"
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_82",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-23T18:45:00Z. "
            "Capture end-of-day context for infra—sync the latest message from Gmail thread thread_005 into Figma artifact art_004 as a comment; "
            "acknowledge in-thread, label it 'synced-to-figma', verify via thread metadata, and record the sync."
        ),
        actions=[
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_005", "request_id": "em-001"}),
            Action(name="list_gmail_messages", kwargs={"thread_id": "thread_005", "request_id": "em-002"}),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_004", "author_email": "design-review@company.com",
                "content": "Synced from Gmail thread thread_005 on 2024-08-23.",
                "timestamp": "2024-08-23T18:45:00Z", "request_id": "en-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_005", "sender_email": "sarah.designer@company.com",
                "body_html": "Thread thread_005 synced to art_004 on 2024-08-23.",
                "timestamp": "2024-08-23T18:45:00Z", "request_id": "em-003",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_005", "add_labels": ["synced-to-figma"],
                "timestamp": "2024-08-23T18:45:00Z", "request_id": "up-001",
            }),
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_005", "request_id": "em-004"}),
            Action(name="record_automation_run", kwargs={
                "task_name": "sync_email_to_figma",
                "status": "completed",
                "started_at": "2024-08-23T18:45:00Z",
                "ended_at": "2024-08-23T18:45:00Z",
                "timestamp": "2024-08-23T18:45:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"thread_id":"thread_005"',
            '"comment_id":"comment_en-001"',
            '"labels":["synced-to-figma"]',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_83",
        instruction=(
            "You are the design review coordinator and the time is 2024-09-02T17:00:00Z. "
            "Before closing the book on the sprint, sync the newest message from Gmail thread thread_012 into Figma artifact art_012 as a comment; "
            "acknowledge in-thread, label it 'synced-to-figma', verify via thread metadata, and record the sync."
        ),
        actions=[
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_012", "request_id": "em-001"}),
            Action(name="list_gmail_messages", kwargs={"thread_id": "thread_012", "request_id": "em-002"}),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_012", "author_email": "design-review@company.com",
                "content": "Synced from Gmail thread thread_012 on 2024-09-02.",
                "timestamp": "2024-09-02T17:00:00Z", "request_id": "en-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_012", "sender_email": "sarah.designer@company.com",
                "body_html": "Thread thread_012 synced to art_012 on 2024-09-02.",
                "timestamp": "2024-09-02T17:00:00Z", "request_id": "em-003",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_012", "add_labels": ["synced-to-figma"],
                "timestamp": "2024-09-02T17:00:00Z", "request_id": "up-001",
            }),
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_012", "request_id": "em-004"}),
            Action(name="record_automation_run", kwargs={
                "task_name": "sync_email_to_figma",
                "status": "completed",
                "started_at": "2024-09-02T17:00:00Z",
                "ended_at": "2024-09-02T17:00:00Z",
                "timestamp": "2024-09-02T17:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"thread_id":"thread_012"',
            '"comment_id":"comment_en-001"',
            '"labels":["synced-to-figma"]',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_84",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T12:10:00Z. "
            "Engineering wants eyes on a new card layout—initiate an email-based design review of Figma artifact art_006 using export profile 'PNG 2x', "
            "from sarah.designer@company.com to ['mike.ux@company.com']; keep the day’s thread consistent and include the exported asset; "
            "apply the 'needs-review' label; record the activity."
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_006",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T12:10:00Z",
                "request_id": "en-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_006 — 2024-08-23",  # email.review_request.v2_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com"],
                "timestamp": "2024-08-23T12:10:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_006.\nThanks.",
                # email.review_request.v2_body
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-23T12:10:00Z",
                "request_id": "em-002",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001",
                "add_labels": ["needs-review"],
                "timestamp": "2024-08-23T12:10:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "design_review_email",
                "status": "completed",
                "started_at": "2024-08-23T12:10:00Z",
                "ended_at": "2024-08-23T12:10:00Z",
                "timestamp": "2024-08-23T12:10:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_006-20240823-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rl-001"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_85",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-24T10:20:00Z. "
            "The promo banner variant is ready—initiate an email-based design review of Figma artifact art_007 using export profile 'PNG 2x', "
            "from sarah.designer@company.com to ['alex.dev@company.com', 'lisa.marketing@company.com']; keep the day’s thread consistent, "
            "include the exported asset, apply the 'needs-review' label, and record the activity."
        ),
        actions=[
            # 1) Export the asset (deterministic IDs)
            Action(name="export_assets", kwargs={
                "artifact_id": "art_007",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T10:20:00Z",
                "request_id": "en-001",
            }),

            # 2) Start today's review thread (no same-day thread exists in data; creating a new one is correct)
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_007 — 2024-08-24",  # email.review_request.v2_subject
                "sender_email": "sarah.designer@company.com",
                "recipients": ["alex.dev@company.com", "lisa.marketing@company.com"],
                "timestamp": "2024-08-24T10:20:00Z",
                "request_id": "em-001",
            }),

            # 3) Body must follow email.review_request.v2_body (exact phrase: "Please review the attached …")
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_007.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-24T10:20:00Z",
                "request_id": "em-002",
            }),

            # 4) Apply kickoff label
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001",
                "add_labels": ["needs-review"],
                "timestamp": "2024-08-24T10:20:00Z",
                "request_id": "up-001",
            }),

            # 5) Record the automation run
            Action(name="record_automation_run", kwargs={
                "task_name": "design_review_email",
                "status": "completed",
                "started_at": "2024-08-24T10:20:00Z",
                "ended_at": "2024-08-24T10:20:00Z",
                "timestamp": "2024-08-24T10:20:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_007-20240824-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rl-001"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_86",
        instruction=(
            "You are the audit lead and the time is 2024-08-23T14:20:00Z. "
            "Merge feedback for a single packet—For audit audit_003 on artifact art_003, ensure combined A11Y (COLOR_CONTRAST) and "
            "DS (AMBIGUOUS) coverage is reflected; produce a PDF report, leave a Figma comment using the standard audit-report template, "
            "and record the activity."
        ),
        actions=[
            Action(name="get_audit", kwargs={"audit_id": "audit_003"}),

            # Use allowed A11Y category name
            Action(name="list_audit_findings_a11y", kwargs={
                "audit_id": "audit_003",
                "violation_type": "COLOR_CONTRAST",
            }),
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "audit_003",
                "finding_type": "AMBIGUOUS",
            }),

            # Deterministic report asset id: exp-art_003-20240823-pdf-001
            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_003",
                "audit_id": "audit_003",
                "format": "pdf",
                "timestamp": "2024-08-23T14:20:00Z",
                "request_id": "au-001",
            }),

            # TEMPLATE_SELECTION_RULE: figma.comment.audit_report_sent.v1
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_003",
                "author_email": "design-review@company.com",
                "content": "Audit report sent — art_003 — audit_003 — 2024-08-23 — asset exp-art_003-20240823-pdf-001",
                "timestamp": "2024-08-23T14:20:00Z",
                "request_id": "en-001",
            }),

            # Update-type => up- prefix
            Action(name="update_audit_status", kwargs={
                "audit_id": "audit_003",
                "status": "COMPLETED",
                "updated_at": "2024-08-23T14:20:00Z",
                "timestamp": "2024-08-23T14:20:00Z",
                "request_id": "up-001",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "audit_combined_report",
                "status": "completed",
                "started_at": "2024-08-23T14:20:00Z",
                "ended_at": "2024-08-23T14:20:00Z",
                "timestamp": "2024-08-23T14:20:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"audit_id":"audit_003"',
            '"asset_id":"exp-art_003-20240823-pdf-001"',
            '"comment_id":"comment_en-001"',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_87",
        instruction=(
            "You are the audit lead and the time is 2024-08-24T12:20:00Z. "
            "Support a cross-team readout—For audit audit_002 on artifact art_008, ensure combined A11Y (COLOR_CONTRAST) and "
            "DS (UNMAPPED) coverage is reflected; produce a PDF report, leave a Figma comment using the standard audit-report template, "
            "and record the activity."
        ),
        actions=[
            Action(name="get_audit", kwargs={"audit_id": "audit_002"}),

            # A11Y + DS coverage checks
            Action(name="list_audit_findings_a11y", kwargs={
                "audit_id": "audit_002",
                "violation_type": "COLOR_CONTRAST",
            }),
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "audit_002",
                "finding_type": "UNMAPPED",
            }),

            # Deterministic PDF asset id: exp-art_008-20240824-pdf-001
            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_008",
                "audit_id": "audit_002",
                "format": "pdf",
                "timestamp": "2024-08-24T12:20:00Z",
                "request_id": "au-001",
            }),

            # Standard comment template: "Audit report sent — {artifact_id} — {audit_id} — {date} — asset {asset_id}"
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_008",
                "author_email": "design-review@company.com",
                "content": "Audit report sent — art_008 — audit_002 — 2024-08-24 — asset exp-art_008-20240824-pdf-001",
                "timestamp": "2024-08-24T12:20:00Z",
                "request_id": "en-001",
            }),

            # Record activity (audit-prefixed request_id)
            Action(name="record_automation_run", kwargs={
                "task_name": "combined_audit_report",
                "status": "completed",
                "started_at": "2024-08-24T12:20:00Z",
                "ended_at": "2024-08-24T12:20:00Z",
                "timestamp": "2024-08-24T12:20:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_002"',
            '"asset_id":"exp-art_008-20240824-pdf-001"',
            '"comment_id":"comment_en-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_88",
        instruction=(
            "You are the design review coordinator and the time is 2024-09-02T09:55:00Z. "
            "Keep thread continuity for approvals—continue the existing conversation thread_011 for artifact art_011 with a follow-up that includes the latest 'PNG 2x' export; "
            "do not start a new subject; record the activity."
        ),
        actions=[
            # 1) Export latest PNG 2x for art_011
            Action(name="export_assets", kwargs={
                "artifact_id": "art_011",
                "export_profile": "PNG 2x",
                "timestamp": "2024-09-02T09:55:00Z",
                "request_id": "en-001",
            }),

            # 2) (Optional) Read existing thread context
            Action(name="get_gmail_thread", kwargs={
                "thread_id": "thread_011",
                "request_id": "em-001",
            }),

            # 3) Append reply with deterministic generic template; attach exported asset
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_011",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hello,\nPlease see details attached.\nThanks.",  # email.generic_plain.v1
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-09-02T09:55:00Z",
                "request_id": "em-002",
            }),

            # 4) Record the run
            Action(name="record_automation_run", kwargs={
                "task_name": "design_review_followup",
                "status": "completed",
                "started_at": "2024-09-02T09:55:00Z",
                "ended_at": "2024-09-02T09:55:00Z",
                "timestamp": "2024-09-02T09:55:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"thread_id":"thread_011"',
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_011-20240902-png-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_89",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-24T09:40:00Z. "
            "Contrast is gating sign-off—For audit audit_004 on artifact art_004, review findings across COLOR_CONTRAST only, "
            "produce a PDF accessibility report based strictly on those findings, leave a Figma comment using the standard audit-report template, "
            "and record the activity."
        ),
        actions=[
            Action(name="get_audit", kwargs={"audit_id": "audit_004"}),
            Action(name="list_audit_findings_a11y", kwargs={
                "audit_id": "audit_004", "violation_type": "COLOR_CONTRAST"
            }),
            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_004",
                "audit_id": "audit_004",
                "format": "pdf",
                "timestamp": "2024-08-24T09:40:00Z",
                "request_id": "au-001",
            }),
            # figma.comment.audit_report_sent.v1
            # "Audit report sent — {artifact_id} — {audit_id} — {date} — asset {asset_id}"
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_004",
                "author_email": "design-review@company.com",
                "content": "Audit report sent — art_004 — audit_004 — 2024-08-24 — asset exp-art_004-20240824-pdf-001",
                "timestamp": "2024-08-24T09:40:00Z",
                "request_id": "en-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "a11y_audit_report",
                "status": "completed",
                "started_at": "2024-08-24T09:40:00Z",
                "ended_at": "2024-08-24T09:40:00Z",
                "timestamp": "2024-08-24T09:40:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_004"',
            '"asset_id":"exp-art_004-20240824-pdf-001"',
            '"comment_id":"comment_en-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_90",
        instruction=(
            "You are the design-system auditor and the time is 2024-08-24T12:05:00Z. "
            "Ambiguity needs triage—For audit audit_003 on artifact art_003, review design-system findings covering AMBIGUOUS mappings, "
            "generate a PDF report grounded in those findings, leave a Figma comment using the standard audit-report template, and record the activity."
        ),
        actions=[
            Action(name="get_audit", kwargs={"audit_id": "audit_003"}),

            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "audit_003",
                "finding_type": "AMBIGUOUS",
            }),

            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_003",
                "audit_id": "audit_003",
                "format": "pdf",
                "timestamp": "2024-08-24T12:05:00Z",
                "request_id": "au-001",
            }),

            Action(name="update_audit_status", kwargs={
                "audit_id": "audit_003",
                "status": "COMPLETED",
                "updated_at": "2024-08-24T12:05:00Z",
                "timestamp": "2024-08-24T12:05:00Z",
                "request_id": "up-001",
            }),

            # figma.comment.audit_report_sent.v1 => "Audit report sent — {artifact_id} — {audit_id} — {date} — asset {asset_id}"
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_003",
                "author_email": "design-review@company.com",
                "content": "Audit report sent — art_003 — audit_003 — 2024-08-24 — asset exp-art_003-20240824-pdf-001",
                "timestamp": "2024-08-24T12:05:00Z",
                "request_id": "en-001",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "ds_audit_report",
                "status": "completed",
                "started_at": "2024-08-24T12:05:00Z",
                "ended_at": "2024-08-24T12:05:00Z",
                "timestamp": "2024-08-24T12:05:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"audit_id":"audit_003"',
            '"asset_id":"exp-art_003-20240824-pdf-001"',
            '"comment_id":"comment_en-001"',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_91",
        instruction=(
            "You are the governance steward and the time is 2024-09-02T18:00:00Z. "
            "After final sign-off, update tags on artifact art_012 by adding ['approved','responsive'] and removing ['needs-review']; "
            "leave a concise, tokenized Figma note documenting the exact tag changes; record the update."
        ),
        actions=[
            # Update only the requested tags (no invented labels)
            Action(name="governance_update", kwargs={
                "artifact_id": "art_012",
                "add_tags": ["approved", "responsive"],
                "remove_tags": ["needs-review"],
                "timestamp": "2024-09-02T18:00:00Z",
                "request_id": "up-001",
            }),

            # Deterministic, tokenized Figma note
            # "Governance update — {artifact_id} — add {add_list} — remove {remove_list} — {date}"
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_012",
                "author_email": "design-review@company.com",
                "content": "Governance update — art_012 — add [approved,responsive] — remove [needs-review] — 2024-09-02",
                "timestamp": "2024-09-02T18:00:00Z",
                "request_id": "en-001",
            }),

            # Record the update (use 'up-' prefix for request_id/run_id)
            Action(name="record_automation_run", kwargs={
                "task_name": "governance_update",
                "status": "completed",
                "started_at": "2024-09-02T18:00:00Z",
                "ended_at": "2024-09-02T18:00:00Z",
                "timestamp": "2024-09-02T18:00:00Z",
                "request_id": "up-002",
            }),
        ],
        outputs=[
            '"artifact_id":"art_012"',
            '"comment_id":"comment_en-001"',
            '"run_id":"run_up-002"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="TASK_92",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-24T17:55:00Z. "
            "One last capture before EOD—sync the latest message from Gmail thread thread_003 into Figma artifact art_003 as a comment; "
            "acknowledge in-thread, label it 'synced-to-figma', verify via thread metadata, and record the sync."
        ),
        actions=[
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_003", "request_id": "em-001"}),
            Action(name="list_gmail_messages", kwargs={"thread_id": "thread_003", "request_id": "em-002"}),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_003", "author_email": "design-review@company.com",
                "content": "Synced from Gmail thread thread_003 on 2024-08-24.",
                "timestamp": "2024-08-24T17:55:00Z", "request_id": "en-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_003", "sender_email": "sarah.designer@company.com",
                "body_html": "Thread thread_003 synced to art_003 on 2024-08-24.",
                "timestamp": "2024-08-24T17:55:00Z", "request_id": "em-003",
            }),
            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_003", "add_labels": ["synced-to-figma"],
                "timestamp": "2024-08-24T17:55:00Z", "request_id": "up-001",
            }),
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_003", "request_id": "em-004"}),
            Action(name="record_automation_run", kwargs={
                "task_name": "sync_email_to_figma",
                "status": "completed",
                "started_at": "2024-08-24T17:55:00Z",
                "ended_at": "2024-08-24T17:55:00Z",
                "timestamp": "2024-08-24T17:55:00Z", "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"thread_id":"thread_003"',
            '"comment_id":"comment_en-001"',
            '"labels":["synced-to-figma"]',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    ),
    # TASK_M1 — Review kickoff (new same-day thread; PNG 2x; needs-review label)
    Task(
        annotator="0",
        user_id="TASK_92",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-20T10:05:00Z. "
            "Kick off an email-based design review for artifact art_001 using export profile 'PNG 2x', "
            "from sarah.designer@company.com to ['alex.dev@company.com','lisa.marketing@company.com']; "
            "start today's thread, attach the export, apply the 'needs-review' label, link to the cycle, no need to record the automation run."
        ),
        actions=[
            # Derive the cycle deterministically (the dataset has a single cycle for art_001 → cycle_001)
            Action(name="list_review_cycles", kwargs={}),

            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-20T10:05:00Z",
                "request_id": "en-001",
            }),

            # Thread policy: check same-day thread for both recipients
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — art_001 — 2024-08-20",
                "participant_email": "alex.dev@company.com",
            }),
            Action(name="find_gmail_threads", kwargs={
                "subject_contains": "Review Request — art_001 — 2024-08-20",
                "participant_email": "lisa.marketing@company.com",
            }),

            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_001 — 2024-08-20",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["alex.dev@company.com", "lisa.marketing@company.com"],
                "timestamp": "2024-08-20T10:05:00Z",
                "request_id": "em-001",
            }),

            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],  # from export_assets ID_RULE
                "timestamp": "2024-08-20T10:05:00Z",
                "request_id": "em-002",
            }),

            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thr_em-001",
                "add_labels": ["needs-review"],
                "timestamp": "2024-08-20T10:05:00Z",
                "request_id": "up-001",
            }),

            # Link to the (now-derivable) cycle: cycle_001
            Action(name="attach_thread_to_review_cycle", kwargs={
                "cycle_id": "cycle_001",
                "thread_id": "thr_em-001",
                "updated_at": "2024-08-20T10:05:00Z",
                "timestamp": "2024-08-20T10:05:00Z",
                "request_id": "rv-001",
            }),

        ],
        outputs=[
            '"asset_id":"asset_en-001"',
            '"export_id":"exp-art_001-20240820-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_94",
        instruction=(
            "You are the design review coordinator and the time is 2024-09-02T12:30:00Z. "
            "Keep the dialogue in one place—For review cycle cycle_012 (artifact art_012), continue the existing thread thread_012 "
            "with a changes-requested follow-up; apply label ['changes-requested']; record the update."
        ),
        actions=[
            Action(name="get_review_cycle", kwargs={"cycle_id": "cycle_012"}),

            # Confirm current labels / metadata (no request_id param for this tool)
            Action(name="get_gmail_thread", kwargs={"thread_id": "thread_012"}),

            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_012",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-09-02T12:30:00Z",
                "timestamp": "2024-09-02T12:30:00Z",
                "request_id": "up-001",
            }),

            Action(name="append_gmail_message", kwargs={
                "thread_id": "thread_012",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Changes requested for art_012. Continuing in today’s thread.",
                "timestamp": "2024-09-02T12:30:00Z",
                "request_id": "em-001",
            }),

            Action(name="apply_gmail_labels", kwargs={
                "thread_id": "thread_012",
                "add_labels": ["changes-requested"],
                "timestamp": "2024-09-02T12:30:00Z",
                "request_id": "up-002",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "review_changes_requested",
                "status": "completed",
                "started_at": "2024-09-02T12:30:00Z",
                "ended_at": "2024-09-02T12:30:00Z",
                "timestamp": "2024-09-02T12:30:00Z",
                "request_id": "rv-001",
            }),
        ],
        outputs=[
            '"cycle_id":"cycle_012"',
            '"thread_id":"thread_012"',
            '"message_id":"msg_em-001"',
            '"run_id":"run_rv-001"',
        ],
    )

    ,
    Task(
        annotator="0",
        user_id="TASK_95",
        instruction=(
            "You are the systems audit lead and the time is 2024-08-24T11:20:00Z. "
            "For audit audit_006 on artifact art_009, review DS findings across UNMAPPED and AMBIGUOUS, "
            "produce a PDF report, leave a Figma comment using the standard audit-report template, "
            "then update tags to add ['ds-reviewed'] and remove ['needs-review']; record the activity."
        ),
        actions=[
            Action(name="get_audit", kwargs={"audit_id": "audit_006"}),

            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "audit_006",
                "finding_type": "UNMAPPED",
            }),
            Action(name="list_audit_findings_ds", kwargs={
                "audit_id": "audit_006",
                "finding_type": "AMBIGUOUS",
            }),

            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_009",
                "audit_id": "audit_006",
                "format": "pdf",
                "timestamp": "2024-08-24T11:20:00Z",
                "request_id": "au-001",
            }),

            # Template: "Audit report sent — {artifact_id} — {audit_id} — {date} — asset {asset_id}"
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_009",
                "author_email": "design-review@company.com",
                "content": "Audit report sent — art_009 — audit_006 — 2024-08-24 — asset exp-art_009-20240824-pdf-001",
                "timestamp": "2024-08-24T11:20:00Z",
                "request_id": "en-001",
            }),

            Action(name="governance_update", kwargs={
                "artifact_id": "art_009",
                "add_tags": ["ds-reviewed"],
                "remove_tags": ["needs-review"],
                "timestamp": "2024-08-24T11:20:00Z",
                "request_id": "up-001",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "ds_audit_report_and_tags",
                "status": "completed",
                "started_at": "2024-08-24T11:20:00Z",
                "ended_at": "2024-08-24T11:20:00Z",
                "timestamp": "2024-08-24T11:20:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_006"',
            '"asset_id":"exp-art_009-20240824-pdf-001"',
            '"comment_id":"comment_en-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    )
    ,
    Task(
        annotator="0",
        user_id="task_96",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T10:00:00Z. "
            "Kick off an email-based design review of Figma artifact art_001 using export profile 'PNG 2x'. "
            "Send from sarah.designer@company.com to [mike.ux@company.com, alex.dev@company.com, lisa.marketing@company.com]. "
            "Make sure the review email includes the exported asset."
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "en-001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-23T10:00:00Z",
                "ended_at": "2024-08-23T10:00:00Z",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"export_id":"exp-art_001-20240823-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="task_97",
        instruction=(
            "You are the release publisher for the Design System team and the time is 2024-08-22T17:00:00Z. "
            "Share a release handoff for Figma artifact art_001 referencing release_001, emailed from "
            "sarah.designer@company.com to [alex.dev@company.com, lisa.marketing@company.com, mike.ux@company.com]. "
            "Export the asset using profile 'PNG 2x' and include it in the email."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),

            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "en-001",
            }),

            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — release_001 — 2024-08-22",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["alex.dev@company.com", "lisa.marketing@company.com", "mike.ux@company.com"],
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "em-001",
            }),

            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": (
                    "Hello stakeholders,\n"
                    "Please find the release notes for release_001, including changes.\n"
                    "Regards."
                ),
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "em-002",
            }),

            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/20240822"],
                "remove_tags": [],
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "up-001",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-22T17:00:00Z",
                "ended_at": "2024-08-22T17:00:00Z",
                "timestamp": "2024-08-22T17:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"export_id":"exp-art_001-20240822-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="task_98",
        instruction=(
            "You are the accessibility audit lead for the Web UX team and the time is 2024-08-23T12:05:00Z. "
            "For audit audit_003 on Figma artifact art_003, review A11Y findings for COLOR_CONTRAST and ALT_TEXT, "
            "then produce a PDF accessibility report strictly based on those findings and record the activity."
        ),
        actions=[
            Action(name="list_audit_findings_a11y", kwargs={
                "audit_id": "audit_003",
                "violation_type": "COLOR_CONTRAST",
            }),
            Action(name="list_audit_findings_a11y", kwargs={
                "audit_id": "audit_003",
                "violation_type": "ALT_TEXT",
            }),
            Action(name="GenerateAuditReport", kwargs={
                "artifact_id": "art_003",
                "audit_id": "audit_003",
                "format": "pdf",
                "timestamp": "2024-08-23T12:05:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "a11y_audit",
                "status": "completed",
                "started_at": "2024-08-23T12:05:00Z",
                "ended_at": "2024-08-23T12:05:00Z",
                "timestamp": "2024-08-23T12:05:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_003"',
            '"asset_id":"exp-art_003-20240823-pdf-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="task_99",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T09:10:00Z. "
            "Initiate an email-based design review for artifact art_001 using export profile 'PNG 2x' from "
            "sarah.designer@company.com to [mike.ux@company.com, alex.dev@company.com, lisa.marketing@company.com]. "
            "Mark the artifact for review, include the exported asset in the email, and record the run."
        ),
        actions=[
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "rl-001",
            }),

            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "rl-002",
            }),

            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"],
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "rl-003",
            }),

            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_rl-003",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                "attachments_asset_ids": ["asset_rl-002"],
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "rl-004",
            }),

            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-23T09:10:00Z",
                "ended_at": "2024-08-23T09:10:00Z",
                "timestamp": "2024-08-23T09:10:00Z",
                "request_id": "rl-005",
            }),
        ],
        outputs=[
            '"export_id":"exp-art_001-20240823-png-001"',
            '"thread_id":"thr_rl-003"',
            '"message_id":"msg_rl-004"',
            '"run_id":"run_rl-005"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="task_100",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-24T11:15:00Z. "
            "Kick off an email-based design review of Figma artifact art_003 using export profile 'PNG 2x'. "
            "Send from sarah.designer@company.com to [mike.ux@company.com, alex.dev@company.com, lisa.marketing@company.com]. "
            "Make sure the review email includes the exported asset."
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_003",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T11:15:00Z",
                "request_id": "en-001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_003",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-24T11:15:00Z",
                "request_id": "up-001",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Review Request — art_003 — 2024-08-24",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"],
                "timestamp": "2024-08-24T11:15:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_003.\nThanks.",
                "attachments_asset_ids": ["asset_en-001"],
                "timestamp": "2024-08-24T11:15:00Z",
                "request_id": "em-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-24T11:15:00Z",
                "ended_at": "2024-08-24T11:15:00Z",
                "timestamp": "2024-08-24T11:15:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            '"export_id":"exp-art_003-20240824-png-001"',
            '"thread_id":"thr_em-001"',
            '"message_id":"msg_em-002"',
            '"run_id":"run_rl-001"',
            '"status":"completed"',
        ],
    )

]

TASKS.reverse()

