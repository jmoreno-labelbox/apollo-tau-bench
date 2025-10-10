from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="res_001",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T10:00:00Z; "
            "kick off an email-based design review for Figma artifact art_001 using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread for the day labeled 'Design/Needs-Review', "
            "and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:00:00Z",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
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
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_002",
        instruction=(
            "You are the release publisher and the time is 2024-08-23T11:00:00Z. "
            "Product wants stakeholders aligned—share a release handoff for artifact art_001, summarizing changes since release_001. "
            "Use export profile 'PNG 2x' for the attachment and send from sarah.designer@company.com to ['stakeholders@company.com','product-managers@company.com']; "
            "after sending, tag the artifact 'released/2024-08-23' and record the run."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),
            Action(name="create_release_record", kwargs={
                "artifact_id": "art_001",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "labels": ["released/2024-08-23"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/2024-08-23"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-23T11:00:00Z",
                "ended_at": "2024-08-23T11:00:00Z",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            {
                "previous_release_id":"release_001",
                "release_id":"rel-art_001-20240823-001",
                "asset_id":"asset_en-002",
                "export_id":"exp-art_001-20240823-png-001",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["released/2024-08-23"],
                "run_id":"run_rl-001",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_003",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-23T12:00:00Z; "
            "kick off an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'a11y/needs-audit'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T12:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Accessibility Audit: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "labels": ["Design/Accessibility"],
                "timestamp": "2024-08-23T12:00:00Z",
                "request_id": "ax-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ax-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T12:00:00Z",
                "request_id": "ax-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ax-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["a11y/needs-audit"],
                "remove_tags": [],
                "timestamp": "2024-08-23T12:00:00Z",
                "request_id": "ax-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "accessibility_audit_kickoff",
                "status": "completed",
                "started_at": "2024-08-23T12:00:00Z",
                "ended_at": "2024-08-23T12:00:00Z",
                "timestamp": "2024-08-23T12:00:00Z",
                "request_id": "ax-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ax-001",
                "message_id":"msg_ax-002",
                "asset_id":"asset_en-002",
                "tags":["a11y/needs-audit"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_004",
        instruction=(
            "You are the design systems triage lead and the time is 2024-08-23T13:00:00Z; "
            "coordinate a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-systems@company.com','frontend-guild@company.com'] on a single thread labeled 'Design/Design-System'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'ds/triage-open'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design System Triage: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "labels": ["Design/Design-System"],
                "timestamp": "2024-08-23T13:00:00Z",
                "request_id": "ds-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ds-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_ds-002"],
                "timestamp": "2024-08-23T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ds-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["ds/triage-open"],
                "remove_tags": [],
                "timestamp": "2024-08-23T13:00:00Z",
                "request_id": "ds-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "design_systems_triage",
                "status": "completed",
                "started_at": "2024-08-23T13:00:00Z",
                "ended_at": "2024-08-23T13:00:00Z",
                "timestamp": "2024-08-23T13:00:00Z",
                "request_id": "ds-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ds-001",
                "message_id":"msg_ds-002",
                "asset_id":"asset_ds-002",
                "tags":["ds/triage-open"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_005",
        instruction=(
            "You are the review program manager and the time is 2024-08-23T14:00:00Z; "
            "continue the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on the single thread labeled 'Design/Needs-Review' by sending a reminder. "
            "After sending, mirror replies as Figma comments, apply quorum, and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_006",
        instruction=(
            "You are the change request lead and the time is 2024-08-23T14:30:00Z; "
            "communicate requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Changes-Requested' by sending a request; "
            "after sending, mirror replies as Figma comments, move the cycle to CHANGES_REQUESTED, and add tag 'needs-changes'."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Changes Requested: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Changes-Requested"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_cr-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_cr-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_cr-001",
                "artifact_id": "art_001",
            }),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-23T14:30:00Z",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-changes"],
                "remove_tags": [],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "change_request",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"CHANGES_REQUESTED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_cr-001",
                "message_id":"msg_cr-002",
                "tags":["needs-changes"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_007",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-23T10:05:00Z; "
            "continue the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Needs-Review', "
            "keep identifiers deterministic and reusable, and finalize the cycle by applying quorum."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:05:00Z",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_008",
        instruction=(
            "You are the fix item status updater and the time is 2024-08-23T14:00:00Z. "
            "Your goal is to update fix items from plan_012 for audit_012: mark item_017 and item_018 as APPLIED, "
            "leave item_019 and item_020 as PENDING, and record the run."
        ),
        actions=[
            Action(name="update_fix_item_status", kwargs={
                "item_id": "item_017",
                "status": "APPLIED",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="update_fix_item_status", kwargs={
                "item_id": "item_018",
                "status": "APPLIED",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "up-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fix_item_status_update",
                "status": "completed",
                "started_at": "2024-08-23T14:00:00Z",
                "ended_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "up-003",
            }),
        ],
        outputs=[
            '"item_id":"item_017","status":"APPLIED"',
            '"item_id":"item_018","status":"APPLIED"',
            '"run_id":"run_up-003"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_009",
        instruction=(
            "You are the audit report generator and the time is 2024-08-23T14:30:00Z. "
            "Your goal is to generate a combined audit report for audit_012 (artifact art_001) including both accessibility and design system findings; "
            "after generating the report, export it as a PDF report asset, and record the run."
        ),
        actions=[
            Action(name="generate_combined_audit_report", kwargs={
                "audit_id": "audit_012",
                "artifact_id": "art_001",
                "output_format": "PDF",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "combined_audit_report",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_012"',
            '"artifact_id":"art_001"',
            '"report_asset_id":"asset_au-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_010",
        instruction=(
            "You are the design review coordinator and the time is 2024-08-24T09:00:00Z; "
            "run a same-day email-based design review for Figma artifact art_002 ('Pricing Page – Plans Grid') according to policy, using the 'PNG 2x' export, "
            "notifying ['design-review@company.com','growth-team@company.com'], keeping identifiers deterministic, and reusing the day's thread."

        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "artifact_id": "art_002",
                "started_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-002",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_002",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "en-004",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 2 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-004",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "thread_id": "thr_em-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-004"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_002",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "up-004",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-24T09:00:00Z",
                "ended_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_002-20240824-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-004",
                "thread_id":"thr_em-004",
                "message_id":"msg_em-005",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_011",
        instruction=(
            "You are the fix plan delivery owner and the time is 2024-08-23T13:50:00Z. "
            "Your goal is to coordinate a hybrid delivery for plan_011 on artifact art_001 according to policy by mirroring pending items as Figma comments and "
            "creating one ticket per pending item; after done, notify stakeholders using the canonical digest, add the fixplan delivery tag, "
            "and record the run while keeping identifiers deterministic."
        ),
        actions=[
            Action(name="compute_fix_plan_summary", kwargs={
                "plan_id": "plan_011",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-001",
            }),
            Action(name="deliver_fix_plan", kwargs={
                "plan_id": "plan_011",
                "delivery_method": "COMMENTS",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-002",
            }),
            Action(name="create_tickets_for_pending", kwargs={
                "plan_id": "plan_011",
                "tracker_project": "WEBUX",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-003",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Fix Plan Delivery: plan_011 — pending items",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "labels": ["FixPlan/Owners"],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_fp-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["fixplan/delivered"],
                "remove_tags": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-006",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fixplan_create_and_deliver",
                "status": "completed",
                "started_at": "2024-08-23T13:50:00Z",
                "ended_at": "2024-08-23T13:50:00Z",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-007",
            }),
        ],
        outputs=[
            {
                "plan_id":"plan_011",
                "delivery_method":"COMMENTS",
                "pending_count":6,
                "ticket_ids":["tix-item_011","tix-item_012","tix-item_013","tix-item_014","tix-item_015","tix-item_016"],
                "thread_id":"thr_fp-004",
                "message_id":"msg_fp-005",
                "tags":["fixplan/delivered"],
                "run_id":"run_fp-007",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_012",
        instruction=(
            "You are the audit report generator for the Web UX team and the time is 2024-08-23T14:30:00Z. "
            "Your goal is to generate a combined audit report for audit_012 (artifact art_001) including both accessibility and design system findings; "
            "after generating the report, export it as a PDF report asset, and record the run."
        ),
        actions=[
            Action(name="generate_combined_audit_report", kwargs={
                "audit_id": "audit_012",
                "artifact_id": "art_001",
                "output_format": "PDF",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "combined_audit_report",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_012"',
            '"artifact_id":"art_001"',
            '"report_asset_id":"asset_au-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_013",
        instruction=(
            "You are the design systems triage lead and the time is 2024-08-14T13:00:00Z; "
            "coordinate a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-systems@company.com','frontend-guild@company.com'] on a single thread labeled 'Design/Design-System'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'ds/triage-open'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-14T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design System Triage: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "labels": ["Design/Design-System"],
                "timestamp": "2024-08-14T13:00:00Z",
                "request_id": "ds-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ds-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_ds-002"],
                "timestamp": "2024-08-14T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ds-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["ds/triage-open"],
                "remove_tags": [],
                "timestamp": "2024-08-14T13:00:00Z",
                "request_id": "ds-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "design_systems_triage",
                "status": "completed",
                "started_at": "2024-08-14T13:00:00Z",
                "ended_at": "2024-08-14T13:00:00Z",
                "timestamp": "2024-08-14T13:00:00Z",
                "request_id": "ds-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ds-001",
                "message_id":"msg_ds-002",
                "asset_id":"asset_ds-002",
                "tags":["ds/triage-open"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_014",
        instruction=(
            "You are the design review coordinator for the Web UX H team and the time is 2024-08-23T10:05:00Z; "
            "continue the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Needs-Review', "
            "keep identifiers deterministic and reusable, and finalize the cycle by applying quorum."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:05:00Z",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_015",
        instruction=(
            "You are the design review coordinator for the Web UX A team and the time is 2024-08-23T10:00:00Z; "
            "kick off an email-based design review for Figma artifact art_001 using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread for the day labeled 'Design/Needs-Review', "
            "and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:00:00Z",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
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
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_016",
        instruction=(
            "You are the release publisher for the Web UX team and the time is 2024-08-23T11:00:00Z. "
            "Product wants stakeholders aligned—share a release handoff for artifact art_001, summarizing changes since release_001. "
            "Use export profile 'PNG 2x' for the attachment and send from sarah.designer@company.com to ['stakeholders@company.com','product-managers@company.com']; "
            "after sending, tag the artifact 'released/2024-08-23' and record the run."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),
            Action(name="create_release_record", kwargs={
                "artifact_id": "art_001",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "labels": ["released/2024-08-23"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/2024-08-23"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-23T11:00:00Z",
                "ended_at": "2024-08-23T11:00:00Z",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            {
                "previous_release_id":"release_001",
                "release_id":"rel-art_001-20240823-001",
                "asset_id":"asset_en-002",
                "export_id":"exp-art_001-20240823-png-001",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["released/2024-08-23"],
                "run_id":"run_rl-001",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_017",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-24T09:00:00Z; "
            "run a same-day email-based design review for Figma artifact art_002 ('Pricing Page – Plans Grid') according to policy, using the 'PNG 2x' export, "
            "notifying ['design-review@company.com','growth-team@company.com'], keeping identifiers deterministic, and reusing the day's thread."

        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "artifact_id": "art_002",
                "started_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-002",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_002",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "en-004",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 2 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-004",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "thread_id": "thr_em-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-004"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_002",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "up-004",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-24T09:00:00Z",
                "ended_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_002-20240824-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-004",
                "thread_id":"thr_em-004",
                "message_id":"msg_em-005",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_018",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-22T12:00:00Z; "
            "kick off an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'a11y/needs-audit'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-22T12:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Accessibility Audit: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "labels": ["Design/Accessibility"],
                "timestamp": "2024-08-22T12:00:00Z",
                "request_id": "ax-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ax-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-22T12:00:00Z",
                "request_id": "ax-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ax-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["a11y/needs-audit"],
                "remove_tags": [],
                "timestamp": "2024-08-22T12:00:00Z",
                "request_id": "ax-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "accessibility_audit_kickoff",
                "status": "completed",
                "started_at": "2024-08-22T12:00:00Z",
                "ended_at": "2024-08-22T12:00:00Z",
                "timestamp": "2024-08-22T12:00:00Z",
                "request_id": "ax-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ax-001",
                "message_id":"msg_ax-002",
                "asset_id":"asset_en-002",
                "tags":["a11y/needs-audit"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_019",
        instruction=(
            "You are the review program manager for the Web UX team and the time is 2024-08-23T14:00:00Z; "
            "continue the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on the single thread labeled 'Design/Needs-Review' by sending a reminder. "
            "After sending, mirror replies as Figma comments, apply quorum, and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_020",
        instruction=(
            "You are the change request lead for the Web UX H team and the time is 2024-08-23T14:30:00Z; "
            "communicate requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Changes-Requested' by sending a request; "
            "after sending, mirror replies as Figma comments, move the cycle to CHANGES_REQUESTED, and add tag 'needs-changes'."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Changes Requested: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Changes-Requested"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_cr-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_cr-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_cr-001",
                "artifact_id": "art_001",
            }),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-23T14:30:00Z",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-changes"],
                "remove_tags": [],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "change_request",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"CHANGES_REQUESTED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_cr-001",
                "message_id":"msg_cr-002",
                "tags":["needs-changes"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_021",
        instruction=(
            "You are the design review coordinator for the Web UX G team and the time is 2024-08-23T10:05:00Z; "
            "continue the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Needs-Review', "
            "keep identifiers deterministic and reusable, and finalize the cycle by applying quorum."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:05:00Z",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_022",
        instruction=(
            "You are the fix item status updater and the time is 2024-08-24T14:00:00Z. "
            "Your goal is to update fix items from plan_012 for audit_012: mark item_017 and item_019 as APPLIED, "
            "leave item_018 and item_020 as PENDING, and record the run."
        ),
        actions=[
            Action(name="update_fix_item_status", kwargs={
                "item_id": "item_017",
                "status": "APPLIED",
                "timestamp": "2024-08-24T14:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="update_fix_item_status", kwargs={
                "item_id": "item_019",
                "status": "APPLIED",
                "timestamp": "2024-08-24T14:00:00Z",
                "request_id": "up-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fix_item_status_update",
                "status": "completed",
                "started_at": "2024-08-24T14:00:00Z",
                "ended_at": "2024-08-24T14:00:00Z",
                "timestamp": "2024-08-24T14:00:00Z",
                "request_id": "up-003",
            }),
        ],
        outputs=[
            '"item_id":"item_017","status":"APPLIED"',
            '"item_id":"item_019","status":"APPLIED"',
            '"run_id":"run_up-003"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_023",
        instruction=(
            "You are the design review coordinator for the Web UX B team and the time is 2024-08-23T10:00:00Z; "
            "kick off an email-based design review for Figma artifact art_001 using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread for the day labeled 'Design/Needs-Review', "
            "and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:00:00Z",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
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
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_024",
        instruction=(
            "You are the release publisher for the Web UX A team and the time is 2024-08-23T11:00:00Z. "
            "Product wants stakeholders aligned—share a release handoff for artifact art_001, summarizing changes since release_001. "
            "Use export profile 'PNG 2x' for the attachment and send from sarah.designer@company.com to ['stakeholders@company.com','product-managers@company.com']; "
            "after sending, tag the artifact 'released/2024-08-23' and record the run."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),
            Action(name="create_release_record", kwargs={
                "artifact_id": "art_001",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "labels": ["released/2024-08-23"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/2024-08-23"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-23T11:00:00Z",
                "ended_at": "2024-08-23T11:00:00Z",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            {
                "previous_release_id":"release_001",
                "release_id":"rel-art_001-20240823-001",
                "asset_id":"asset_en-002",
                "export_id":"exp-art_001-20240823-png-001",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["released/2024-08-23"],
                "run_id":"run_rl-001",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_025",
        instruction=(
            "You are the audit report generator for the Web UX A team and the time is 2024-08-23T14:30:00Z. "
            "Your goal is to generate a combined audit report for audit_012 (artifact art_001) including both accessibility and design system findings; "
            "after generating the report, export it as a PDF report asset, and record the run."
        ),
        actions=[
            Action(name="generate_combined_audit_report", kwargs={
                "audit_id": "audit_012",
                "artifact_id": "art_001",
                "output_format": "PDF",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "combined_audit_report",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_012"',
            '"artifact_id":"art_001"',
            '"report_asset_id":"asset_au-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_026",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-21T12:00:00Z; "
            "kick off an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'a11y/needs-audit'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-21T12:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Accessibility Audit: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "labels": ["Design/Accessibility"],
                "timestamp": "2024-08-21T12:00:00Z",
                "request_id": "ax-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ax-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-21T12:00:00Z",
                "request_id": "ax-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ax-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["a11y/needs-audit"],
                "remove_tags": [],
                "timestamp": "2024-08-21T12:00:00Z",
                "request_id": "ax-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "accessibility_audit_kickoff",
                "status": "completed",
                "started_at": "2024-08-21T12:00:00Z",
                "ended_at": "2024-08-21T12:00:00Z",
                "timestamp": "2024-08-21T12:00:00Z",
                "request_id": "ax-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ax-001",
                "message_id":"msg_ax-002",
                "asset_id":"asset_en-002",
                "tags":["a11y/needs-audit"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_027",
        instruction=(
            "You are the change request lead for the Web UX G team and the time is 2024-08-23T14:30:00Z; "
            "communicate requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Changes-Requested' by sending a request; "
            "after sending, mirror replies as Figma comments, move the cycle to CHANGES_REQUESTED, and add tag 'needs-changes'."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Changes Requested: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Changes-Requested"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_cr-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_cr-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_cr-001",
                "artifact_id": "art_001",
            }),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-23T14:30:00Z",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-changes"],
                "remove_tags": [],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "change_request",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"CHANGES_REQUESTED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_cr-001",
                "message_id":"msg_cr-002",
                "tags":["needs-changes"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_028",
        instruction=(
            "You are the design systems triage lead and the time is 2024-08-15T13:00:00Z; "
            "coordinate a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-systems@company.com','frontend-guild@company.com'] on a single thread labeled 'Design/Design-System'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'ds/triage-open'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-15T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design System Triage: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "labels": ["Design/Design-System"],
                "timestamp": "2024-08-15T13:00:00Z",
                "request_id": "ds-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ds-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_ds-002"],
                "timestamp": "2024-08-15T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ds-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["ds/triage-open"],
                "remove_tags": [],
                "timestamp": "2024-08-15T13:00:00Z",
                "request_id": "ds-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "design_systems_triage",
                "status": "completed",
                "started_at": "2024-08-15T13:00:00Z",
                "ended_at": "2024-08-15T13:00:00Z",
                "timestamp": "2024-08-15T13:00:00Z",
                "request_id": "ds-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ds-001",
                "message_id":"msg_ds-002",
                "asset_id":"asset_ds-002",
                "tags":["ds/triage-open"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_029",
        instruction=(
            "You are the design review coordinator for the Web UX A team and the time is 2024-08-24T09:00:00Z; "
            "run a same-day email-based design review for Figma artifact art_002 ('Pricing Page – Plans Grid') according to policy, using the 'PNG 2x' export, "
            "notifying ['design-review@company.com','growth-team@company.com'], keeping identifiers deterministic, and reusing the day's thread."

        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "artifact_id": "art_002",
                "started_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-002",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_002",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "en-004",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 2 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-004",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "thread_id": "thr_em-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-004"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_002",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "up-004",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-24T09:00:00Z",
                "ended_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_002-20240824-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-004",
                "thread_id":"thr_em-004",
                "message_id":"msg_em-005",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_030",
        instruction=(
            "You are the review program manager for the Web UX A team and the time is 2024-08-23T14:00:00Z; "
            "continue the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on the single thread labeled 'Design/Needs-Review' by sending a reminder. "
            "After sending, mirror replies as Figma comments, apply quorum, and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_031",
        instruction=(
            "You are the release publisher for the Web UX B team and the time is 2024-08-23T11:00:00Z. "
            "Product wants stakeholders aligned—share a release handoff for artifact art_001, summarizing changes since release_001. "
            "Use export profile 'PNG 2x' for the attachment and send from sarah.designer@company.com to ['stakeholders@company.com','product-managers@company.com']; "
            "after sending, tag the artifact 'released/2024-08-23' and record the run."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),
            Action(name="create_release_record", kwargs={
                "artifact_id": "art_001",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "labels": ["released/2024-08-23"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/2024-08-23"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-23T11:00:00Z",
                "ended_at": "2024-08-23T11:00:00Z",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            {
                "previous_release_id":"release_001",
                "release_id":"rel-art_001-20240823-001",
                "asset_id":"asset_en-002",
                "export_id":"exp-art_001-20240823-png-001",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["released/2024-08-23"],
                "run_id":"run_rl-001",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_032",
        instruction=(
            "You are the change request lead for the Web UX F team and the time is 2024-08-23T14:30:00Z; "
            "communicate requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Changes-Requested' by sending a request; "
            "after sending, mirror replies as Figma comments, move the cycle to CHANGES_REQUESTED, and add tag 'needs-changes'."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Changes Requested: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Changes-Requested"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_cr-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_cr-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_cr-001",
                "artifact_id": "art_001",
            }),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-23T14:30:00Z",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-changes"],
                "remove_tags": [],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "change_request",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"CHANGES_REQUESTED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_cr-001",
                "message_id":"msg_cr-002",
                "tags":["needs-changes"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_033",
        instruction=(
            "You are the audit report generator for the Web UX B team and the time is 2024-08-23T14:30:00Z. "
            "Your goal is to generate a combined audit report for audit_012 (artifact art_001) including both accessibility and design system findings; "
            "after generating the report, export it as a PDF report asset, and record the run."
        ),
        actions=[
            Action(name="generate_combined_audit_report", kwargs={
                "audit_id": "audit_012",
                "artifact_id": "art_001",
                "output_format": "PDF",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "combined_audit_report",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_012"',
            '"artifact_id":"art_001"',
            '"report_asset_id":"asset_au-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_034",
        instruction=(
            "You are the fix plan delivery owner for the Web UX team and the time is 2024-08-23T13:50:00Z. "
            "Your goal is to coordinate a hybrid delivery for plan_011 on artifact art_001 according to policy by mirroring pending items as Figma comments and "
            "creating one ticket per pending item; after done, notify stakeholders using the canonical digest, add the fixplan delivery tag, "
            "and record the run while keeping identifiers deterministic."
        ),
        actions=[
            Action(name="compute_fix_plan_summary", kwargs={
                "plan_id": "plan_011",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-001",
            }),
            Action(name="deliver_fix_plan", kwargs={
                "plan_id": "plan_011",
                "delivery_method": "COMMENTS",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-002",
            }),
            Action(name="create_tickets_for_pending", kwargs={
                "plan_id": "plan_011",
                "tracker_project": "WEBUX",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-003",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Fix Plan Delivery: plan_011 — pending items",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "labels": ["FixPlan/Owners"],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_fp-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["fixplan/delivered"],
                "remove_tags": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-006",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fixplan_create_and_deliver",
                "status": "completed",
                "started_at": "2024-08-23T13:50:00Z",
                "ended_at": "2024-08-23T13:50:00Z",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-007",
            }),
        ],
        outputs=[
            {
                "plan_id":"plan_011",
                "delivery_method":"COMMENTS",
                "pending_count":6,
                "ticket_ids":["tix-item_011","tix-item_012","tix-item_013","tix-item_014","tix-item_015","tix-item_016"],
                "thread_id":"thr_fp-004",
                "message_id":"msg_fp-005",
                "tags":["fixplan/delivered"],
                "run_id":"run_fp-007",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_035",
        instruction=(
            "You are the design review coordinator for the Web UX F team and the time is 2024-08-23T10:05:00Z; "
            "continue the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Needs-Review', "
            "keep identifiers deterministic and reusable, and finalize the cycle by applying quorum."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:05:00Z",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_036",
        instruction=(
            "You are the design systems triage lead and the time is 2024-08-16T13:00:00Z; "
            "coordinate a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-systems@company.com','frontend-guild@company.com'] on a single thread labeled 'Design/Design-System'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'ds/triage-open'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-16T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design System Triage: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "labels": ["Design/Design-System"],
                "timestamp": "2024-08-16T13:00:00Z",
                "request_id": "ds-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ds-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_ds-002"],
                "timestamp": "2024-08-16T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ds-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["ds/triage-open"],
                "remove_tags": [],
                "timestamp": "2024-08-16T13:00:00Z",
                "request_id": "ds-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "design_systems_triage",
                "status": "completed",
                "started_at": "2024-08-16T13:00:00Z",
                "ended_at": "2024-08-16T13:00:00Z",
                "timestamp": "2024-08-16T13:00:00Z",
                "request_id": "ds-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ds-001",
                "message_id":"msg_ds-002",
                "asset_id":"asset_ds-002",
                "tags":["ds/triage-open"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_037",
        instruction=(
            "You are the fix item status updater and the time is 2024-08-25T14:00:00Z. "
            "Your goal is to update fix items from plan_012 for audit_012: mark item_017 and item_020 as APPLIED, "
            "leave item_018 and item_019 as PENDING, and record the run."
        ),
        actions=[
            Action(name="update_fix_item_status", kwargs={
                "item_id": "item_017",
                "status": "APPLIED",
                "timestamp": "2024-08-25T14:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="update_fix_item_status", kwargs={
                "item_id": "item_020",
                "status": "APPLIED",
                "timestamp": "2024-08-25T14:00:00Z",
                "request_id": "up-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fix_item_status_update",
                "status": "completed",
                "started_at": "2024-08-25T14:00:00Z",
                "ended_at": "2024-08-25T14:00:00Z",
                "timestamp": "2024-08-25T14:00:00Z",
                "request_id": "up-003",
            }),
        ],
        outputs=[
            '"item_id":"item_017","status":"APPLIED"',
            '"item_id":"item_020","status":"APPLIED"',
            '"run_id":"run_up-003"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_038",
        instruction=(
            "You are the review program manager for the Web UX B team and the time is 2024-08-23T14:00:00Z; "
            "continue the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on the single thread labeled 'Design/Needs-Review' by sending a reminder. "
            "After sending, mirror replies as Figma comments, apply quorum, and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_039",
        instruction=(
            "You are the design review coordinator for the Web UX C team and the time is 2024-08-23T10:00:00Z; "
            "kick off an email-based design review for Figma artifact art_001 using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread for the day labeled 'Design/Needs-Review', "
            "and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:00:00Z",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
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
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_040",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-20T12:00:00Z; "
            "kick off an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'a11y/needs-audit'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-20T12:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Accessibility Audit: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "labels": ["Design/Accessibility"],
                "timestamp": "2024-08-20T12:00:00Z",
                "request_id": "ax-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ax-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-20T12:00:00Z",
                "request_id": "ax-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ax-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["a11y/needs-audit"],
                "remove_tags": [],
                "timestamp": "2024-08-20T12:00:00Z",
                "request_id": "ax-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "accessibility_audit_kickoff",
                "status": "completed",
                "started_at": "2024-08-20T12:00:00Z",
                "ended_at": "2024-08-20T12:00:00Z",
                "timestamp": "2024-08-20T12:00:00Z",
                "request_id": "ax-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ax-001",
                "message_id":"msg_ax-002",
                "asset_id":"asset_en-002",
                "tags":["a11y/needs-audit"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_041",
        instruction=(
            "You are the change request lead for the Web UX E team and the time is 2024-08-23T14:30:00Z; "
            "communicate requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Changes-Requested' by sending a request; "
            "after sending, mirror replies as Figma comments, move the cycle to CHANGES_REQUESTED, and add tag 'needs-changes'."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Changes Requested: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Changes-Requested"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_cr-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_cr-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_cr-001",
                "artifact_id": "art_001",
            }),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-23T14:30:00Z",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-changes"],
                "remove_tags": [],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "change_request",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"CHANGES_REQUESTED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_cr-001",
                "message_id":"msg_cr-002",
                "tags":["needs-changes"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_042",
        instruction=(
            "You are the design systems triage lead and the time is 2024-08-17T13:00:00Z; "
            "coordinate a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-systems@company.com','frontend-guild@company.com'] on a single thread labeled 'Design/Design-System'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'ds/triage-open'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-17T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design System Triage: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "labels": ["Design/Design-System"],
                "timestamp": "2024-08-17T13:00:00Z",
                "request_id": "ds-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ds-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_ds-002"],
                "timestamp": "2024-08-17T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ds-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["ds/triage-open"],
                "remove_tags": [],
                "timestamp": "2024-08-17T13:00:00Z",
                "request_id": "ds-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "design_systems_triage",
                "status": "completed",
                "started_at": "2024-08-17T13:00:00Z",
                "ended_at": "2024-08-17T13:00:00Z",
                "timestamp": "2024-08-17T13:00:00Z",
                "request_id": "ds-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ds-001",
                "message_id":"msg_ds-002",
                "asset_id":"asset_ds-002",
                "tags":["ds/triage-open"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_043",
        instruction=(
            "You are the design review coordinator for the Web UX E team and the time is 2024-08-23T10:05:00Z; "
            "continue the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Needs-Review', "
            "keep identifiers deterministic and reusable, and finalize the cycle by applying quorum."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:05:00Z",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_044",
        instruction=(
            "You are the review program manager for the Web UX C team and the time is 2024-08-23T14:00:00Z; "
            "continue the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on the single thread labeled 'Design/Needs-Review' by sending a reminder. "
            "After sending, mirror replies as Figma comments, apply quorum, and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_045",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-19T12:00:00Z; "
            "kick off an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'a11y/needs-audit'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-19T12:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Accessibility Audit: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "labels": ["Design/Accessibility"],
                "timestamp": "2024-08-19T12:00:00Z",
                "request_id": "ax-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ax-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-19T12:00:00Z",
                "request_id": "ax-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ax-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["a11y/needs-audit"],
                "remove_tags": [],
                "timestamp": "2024-08-19T12:00:00Z",
                "request_id": "ax-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "accessibility_audit_kickoff",
                "status": "completed",
                "started_at": "2024-08-19T12:00:00Z",
                "ended_at": "2024-08-19T12:00:00Z",
                "timestamp": "2024-08-19T12:00:00Z",
                "request_id": "ax-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ax-001",
                "message_id":"msg_ax-002",
                "asset_id":"asset_en-002",
                "tags":["a11y/needs-audit"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_046",
        instruction=(
            "You are the fix plan delivery owner for the Web UX A team and the time is 2024-08-23T13:50:00Z. "
            "Your goal is to coordinate a hybrid delivery for plan_011 on artifact art_001 according to policy by mirroring pending items as Figma comments and "
            "creating one ticket per pending item; after done, notify stakeholders using the canonical digest, add the fixplan delivery tag, "
            "and record the run while keeping identifiers deterministic."
        ),
        actions=[
            Action(name="compute_fix_plan_summary", kwargs={
                "plan_id": "plan_011",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-001",
            }),
            Action(name="deliver_fix_plan", kwargs={
                "plan_id": "plan_011",
                "delivery_method": "COMMENTS",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-002",
            }),
            Action(name="create_tickets_for_pending", kwargs={
                "plan_id": "plan_011",
                "tracker_project": "WEBUX",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-003",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Fix Plan Delivery: plan_011 — pending items",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "labels": ["FixPlan/Owners"],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_fp-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["fixplan/delivered"],
                "remove_tags": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-006",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fixplan_create_and_deliver",
                "status": "completed",
                "started_at": "2024-08-23T13:50:00Z",
                "ended_at": "2024-08-23T13:50:00Z",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-007",
            }),
        ],
        outputs=[
            {
                "plan_id":"plan_011",
                "delivery_method":"COMMENTS",
                "pending_count":6,
                "ticket_ids":["tix-item_011","tix-item_012","tix-item_013","tix-item_014","tix-item_015","tix-item_016"],
                "thread_id":"thr_fp-004",
                "message_id":"msg_fp-005",
                "tags":["fixplan/delivered"],
                "run_id":"run_fp-007",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_047",
        instruction=(
            "You are the design review coordinator for the Web UX D team and the time is 2024-08-23T10:00:00Z; "
            "kick off an email-based design review for Figma artifact art_001 using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread for the day labeled 'Design/Needs-Review', "
            "and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:00:00Z",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
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
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_048",
        instruction=(
            "You are the release publisher for the Web UX C team and the time is 2024-08-23T11:00:00Z. "
            "Product wants stakeholders aligned—share a release handoff for artifact art_001, summarizing changes since release_001. "
            "Use export profile 'PNG 2x' for the attachment and send from sarah.designer@company.com to ['stakeholders@company.com','product-managers@company.com']; "
            "after sending, tag the artifact 'released/2024-08-23' and record the run."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),
            Action(name="create_release_record", kwargs={
                "artifact_id": "art_001",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "labels": ["released/2024-08-23"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/2024-08-23"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-23T11:00:00Z",
                "ended_at": "2024-08-23T11:00:00Z",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            {
                "previous_release_id":"release_001",
                "release_id":"rel-art_001-20240823-001",
                "asset_id":"asset_en-002",
                "export_id":"exp-art_001-20240823-png-001",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["released/2024-08-23"],
                "run_id":"run_rl-001",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_049",
        instruction=(
            "You are the audit report generator for the Web UX C team and the time is 2024-08-23T14:30:00Z. "
            "Your goal is to generate a combined audit report for audit_012 (artifact art_001) including both accessibility and design system findings; "
            "after generating the report, export it as a PDF report asset, and record the run."
        ),
        actions=[
            Action(name="generate_combined_audit_report", kwargs={
                "audit_id": "audit_012",
                "artifact_id": "art_001",
                "output_format": "PDF",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "combined_audit_report",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_012"',
            '"artifact_id":"art_001"',
            '"report_asset_id":"asset_au-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_050",
        instruction=(
            "You are the fix plan delivery owner for the Web UX B team and the time is 2024-08-23T13:50:00Z. "
            "Your goal is to coordinate a hybrid delivery for plan_011 on artifact art_001 according to policy by mirroring pending items as Figma comments and "
            "creating one ticket per pending item; after done, notify stakeholders using the canonical digest, add the fixplan delivery tag, "
            "and record the run while keeping identifiers deterministic."
        ),
        actions=[
            Action(name="compute_fix_plan_summary", kwargs={
                "plan_id": "plan_011",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-001",
            }),
            Action(name="deliver_fix_plan", kwargs={
                "plan_id": "plan_011",
                "delivery_method": "COMMENTS",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-002",
            }),
            Action(name="create_tickets_for_pending", kwargs={
                "plan_id": "plan_011",
                "tracker_project": "WEBUX",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-003",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Fix Plan Delivery: plan_011 — pending items",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "labels": ["FixPlan/Owners"],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_fp-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["fixplan/delivered"],
                "remove_tags": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-006",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fixplan_create_and_deliver",
                "status": "completed",
                "started_at": "2024-08-23T13:50:00Z",
                "ended_at": "2024-08-23T13:50:00Z",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-007",
            }),
        ],
        outputs=[
            {
                "plan_id":"plan_011",
                "delivery_method":"COMMENTS",
                "pending_count":6,
                "ticket_ids":["tix-item_011","tix-item_012","tix-item_013","tix-item_014","tix-item_015","tix-item_016"],
                "thread_id":"thr_fp-004",
                "message_id":"msg_fp-005",
                "tags":["fixplan/delivered"],
                "run_id":"run_fp-007",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_051",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-18T12:00:00Z; "
            "kick off an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'a11y/needs-audit'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-18T12:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Accessibility Audit: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "labels": ["Design/Accessibility"],
                "timestamp": "2024-08-18T12:00:00Z",
                "request_id": "ax-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ax-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-18T12:00:00Z",
                "request_id": "ax-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ax-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["a11y/needs-audit"],
                "remove_tags": [],
                "timestamp": "2024-08-18T12:00:00Z",
                "request_id": "ax-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "accessibility_audit_kickoff",
                "status": "completed",
                "started_at": "2024-08-18T12:00:00Z",
                "ended_at": "2024-08-18T12:00:00Z",
                "timestamp": "2024-08-18T12:00:00Z",
                "request_id": "ax-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ax-001",
                "message_id":"msg_ax-002",
                "asset_id":"asset_en-002",
                "tags":["a11y/needs-audit"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_052",
        instruction=(
            "You are the design review coordinator for the Web UX E team and the time is 2024-08-23T10:00:00Z; "
            "kick off an email-based design review for Figma artifact art_001 using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread for the day labeled 'Design/Needs-Review', "
            "and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:00:00Z",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
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
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_053",
        instruction=(
            "You are the release publisher for the Web UX D team and the time is 2024-08-23T11:00:00Z. "
            "Product wants stakeholders aligned—share a release handoff for artifact art_001, summarizing changes since release_001. "
            "Use export profile 'PNG 2x' for the attachment and send from sarah.designer@company.com to ['stakeholders@company.com','product-managers@company.com']; "
            "after sending, tag the artifact 'released/2024-08-23' and record the run."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),
            Action(name="create_release_record", kwargs={
                "artifact_id": "art_001",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "labels": ["released/2024-08-23"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/2024-08-23"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-23T11:00:00Z",
                "ended_at": "2024-08-23T11:00:00Z",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            {
                "previous_release_id":"release_001",
                "release_id":"rel-art_001-20240823-001",
                "asset_id":"asset_en-002",
                "export_id":"exp-art_001-20240823-png-001",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["released/2024-08-23"],
                "run_id":"run_rl-001",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_054",
        instruction=(
            "You are the design review coordinator for the Web UX B team and the time is 2024-08-24T09:00:00Z; "
            "run a same-day email-based design review for Figma artifact art_002 ('Pricing Page – Plans Grid') according to policy, using the 'PNG 2x' export, "
            "notifying ['design-review@company.com','growth-team@company.com'], keeping identifiers deterministic, and reusing the day's thread."

        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "artifact_id": "art_002",
                "started_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-002",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_002",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "en-004",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 2 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-004",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "thread_id": "thr_em-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-004"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_002",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "up-004",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-24T09:00:00Z",
                "ended_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_002-20240824-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-004",
                "thread_id":"thr_em-004",
                "message_id":"msg_em-005",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_055",
        instruction=(
            "You are the fix item status updater and the time is 2024-08-26T14:00:00Z. "
            "Your goal is to update fix items from plan_012 for audit_012: mark item_018 and item_019 as APPLIED, "
            "leave item_017 and item_020 as PENDING, and record the run."
        ),
        actions=[
            Action(name="update_fix_item_status", kwargs={
                "item_id": "item_018",
                "status": "APPLIED",
                "timestamp": "2024-08-26T14:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="update_fix_item_status", kwargs={
                "item_id": "item_019",
                "status": "APPLIED",
                "timestamp": "2024-08-26T14:00:00Z",
                "request_id": "up-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fix_item_status_update",
                "status": "completed",
                "started_at": "2024-08-26T14:00:00Z",
                "ended_at": "2024-08-26T14:00:00Z",
                "timestamp": "2024-08-26T14:00:00Z",
                "request_id": "up-003",
            }),
        ],
        outputs=[
            '"item_id":"item_018","status":"APPLIED"',
            '"item_id":"item_019","status":"APPLIED"',
            '"run_id":"run_up-003"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_056",
        instruction=(
            "You are the review program manager for the Web UX D team and the time is 2024-08-23T14:00:00Z; "
            "continue the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on the single thread labeled 'Design/Needs-Review' by sending a reminder. "
            "After sending, mirror replies as Figma comments, apply quorum, and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_057",
        instruction=(
            "You are the design systems triage lead and the time is 2024-08-18T13:00:00Z; "
            "coordinate a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-systems@company.com','frontend-guild@company.com'] on a single thread labeled 'Design/Design-System'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'ds/triage-open'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-18T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design System Triage: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "labels": ["Design/Design-System"],
                "timestamp": "2024-08-18T13:00:00Z",
                "request_id": "ds-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ds-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_ds-002"],
                "timestamp": "2024-08-18T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ds-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["ds/triage-open"],
                "remove_tags": [],
                "timestamp": "2024-08-18T13:00:00Z",
                "request_id": "ds-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "design_systems_triage",
                "status": "completed",
                "started_at": "2024-08-18T13:00:00Z",
                "ended_at": "2024-08-18T13:00:00Z",
                "timestamp": "2024-08-18T13:00:00Z",
                "request_id": "ds-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ds-001",
                "message_id":"msg_ds-002",
                "asset_id":"asset_ds-002",
                "tags":["ds/triage-open"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_058",
        instruction=(
            "You are the design review coordinator for the Web UX D team and the time is 2024-08-23T10:05:00Z; "
            "continue the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Needs-Review', "
            "keep identifiers deterministic and reusable, and finalize the cycle by applying quorum."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:05:00Z",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_059",
        instruction=(
            "You are the change request lead for the Web UX D team and the time is 2024-08-23T14:30:00Z; "
            "communicate requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Changes-Requested' by sending a request; "
            "after sending, mirror replies as Figma comments, move the cycle to CHANGES_REQUESTED, and add tag 'needs-changes'."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Changes Requested: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Changes-Requested"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_cr-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_cr-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_cr-001",
                "artifact_id": "art_001",
            }),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-23T14:30:00Z",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-changes"],
                "remove_tags": [],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "change_request",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"CHANGES_REQUESTED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_cr-001",
                "message_id":"msg_cr-002",
                "tags":["needs-changes"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_060",
        instruction=(
            "You are the audit report generator for the Web UX D team and the time is 2024-08-23T14:30:00Z. "
            "Your goal is to generate a combined audit report for audit_012 (artifact art_001) including both accessibility and design system findings; "
            "after generating the report, export it as a PDF report asset, and record the run."
        ),
        actions=[
            Action(name="generate_combined_audit_report", kwargs={
                "audit_id": "audit_012",
                "artifact_id": "art_001",
                "output_format": "PDF",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "combined_audit_report",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_012"',
            '"artifact_id":"art_001"',
            '"report_asset_id":"asset_au-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_061",
        instruction=(
            "You are the design review coordinator for the Web UX C team and the time is 2024-08-24T09:00:00Z; "
            "run a same-day email-based design review for Figma artifact art_002 ('Pricing Page – Plans Grid') according to policy, using the 'PNG 2x' export, "
            "notifying ['design-review@company.com','growth-team@company.com'], keeping identifiers deterministic, and reusing the day's thread."

        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "artifact_id": "art_002",
                "started_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-002",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_002",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "en-004",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 2 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-004",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "thread_id": "thr_em-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-004"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_002",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "up-004",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-24T09:00:00Z",
                "ended_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_002-20240824-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-004",
                "thread_id":"thr_em-004",
                "message_id":"msg_em-005",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_062",
        instruction=(
            "You are the review program manager for the Web UX E team and the time is 2024-08-23T14:00:00Z; "
            "continue the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on the single thread labeled 'Design/Needs-Review' by sending a reminder. "
            "After sending, mirror replies as Figma comments, apply quorum, and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_063",
        instruction=(
            "You are the fix plan delivery owner for the Web UX C team and the time is 2024-08-23T13:50:00Z. "
            "Your goal is to coordinate a hybrid delivery for plan_011 on artifact art_001 according to policy by mirroring pending items as Figma comments and "
            "creating one ticket per pending item; after done, notify stakeholders using the canonical digest, add the fixplan delivery tag, "
            "and record the run while keeping identifiers deterministic."
        ),
        actions=[
            Action(name="compute_fix_plan_summary", kwargs={
                "plan_id": "plan_011",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-001",
            }),
            Action(name="deliver_fix_plan", kwargs={
                "plan_id": "plan_011",
                "delivery_method": "COMMENTS",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-002",
            }),
            Action(name="create_tickets_for_pending", kwargs={
                "plan_id": "plan_011",
                "tracker_project": "WEBUX",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-003",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Fix Plan Delivery: plan_011 — pending items",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "labels": ["FixPlan/Owners"],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_fp-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["fixplan/delivered"],
                "remove_tags": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-006",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fixplan_create_and_deliver",
                "status": "completed",
                "started_at": "2024-08-23T13:50:00Z",
                "ended_at": "2024-08-23T13:50:00Z",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-007",
            }),
        ],
        outputs=[
            {
                "plan_id":"plan_011",
                "delivery_method":"COMMENTS",
                "pending_count":6,
                "ticket_ids":["tix-item_011","tix-item_012","tix-item_013","tix-item_014","tix-item_015","tix-item_016"],
                "thread_id":"thr_fp-004",
                "message_id":"msg_fp-005",
                "tags":["fixplan/delivered"],
                "run_id":"run_fp-007",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_064",
        instruction=(
            "You are the design review coordinator for the Web UX F team and the time is 2024-08-23T10:00:00Z; "
            "kick off an email-based design review for Figma artifact art_001 using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread for the day labeled 'Design/Needs-Review', "
            "and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:00:00Z",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
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
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_065",
        instruction=(
            "You are the release publisher for the Web UX E team and the time is 2024-08-23T11:00:00Z. "
            "Product wants stakeholders aligned—share a release handoff for artifact art_001, summarizing changes since release_001. "
            "Use export profile 'PNG 2x' for the attachment and send from sarah.designer@company.com to ['stakeholders@company.com','product-managers@company.com']; "
            "after sending, tag the artifact 'released/2024-08-23' and record the run."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),
            Action(name="create_release_record", kwargs={
                "artifact_id": "art_001",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "labels": ["released/2024-08-23"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/2024-08-23"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-23T11:00:00Z",
                "ended_at": "2024-08-23T11:00:00Z",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            {
                "previous_release_id":"release_001",
                "release_id":"rel-art_001-20240823-001",
                "asset_id":"asset_en-002",
                "export_id":"exp-art_001-20240823-png-001",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["released/2024-08-23"],
                "run_id":"run_rl-001",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_066",
        instruction=(
            "You are the design review coordinator for the Web UX C team and the time is 2024-08-23T10:05:00Z; "
            "continue the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Needs-Review', "
            "keep identifiers deterministic and reusable, and finalize the cycle by applying quorum."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:05:00Z",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_067",
        instruction=(
            "You are the audit report generator for the Web UX E team and the time is 2024-08-23T14:30:00Z. "
            "Your goal is to generate a combined audit report for audit_012 (artifact art_001) including both accessibility and design system findings; "
            "after generating the report, export it as a PDF report asset, and record the run."
        ),
        actions=[
            Action(name="generate_combined_audit_report", kwargs={
                "audit_id": "audit_012",
                "artifact_id": "art_001",
                "output_format": "PDF",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "combined_audit_report",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_012"',
            '"artifact_id":"art_001"',
            '"report_asset_id":"asset_au-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_068",
        instruction=(
            "You are the change request lead for the Web UX C team and the time is 2024-08-23T14:30:00Z; "
            "communicate requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Changes-Requested' by sending a request; "
            "after sending, mirror replies as Figma comments, move the cycle to CHANGES_REQUESTED, and add tag 'needs-changes'."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Changes Requested: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Changes-Requested"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_cr-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_cr-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_cr-001",
                "artifact_id": "art_001",
            }),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-23T14:30:00Z",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-changes"],
                "remove_tags": [],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "change_request",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"CHANGES_REQUESTED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_cr-001",
                "message_id":"msg_cr-002",
                "tags":["needs-changes"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_069",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-17T12:00:00Z; "
            "kick off an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'a11y/needs-audit'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-17T12:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Accessibility Audit: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "labels": ["Design/Accessibility"],
                "timestamp": "2024-08-17T12:00:00Z",
                "request_id": "ax-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ax-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-17T12:00:00Z",
                "request_id": "ax-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ax-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["a11y/needs-audit"],
                "remove_tags": [],
                "timestamp": "2024-08-17T12:00:00Z",
                "request_id": "ax-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "accessibility_audit_kickoff",
                "status": "completed",
                "started_at": "2024-08-17T12:00:00Z",
                "ended_at": "2024-08-17T12:00:00Z",
                "timestamp": "2024-08-17T12:00:00Z",
                "request_id": "ax-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ax-001",
                "message_id":"msg_ax-002",
                "asset_id":"asset_en-002",
                "tags":["a11y/needs-audit"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_070",
        instruction=(
            "You are the design systems triage lead and the time is 2024-08-19T13:00:00Z; "
            "coordinate a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-systems@company.com','frontend-guild@company.com'] on a single thread labeled 'Design/Design-System'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'ds/triage-open'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-19T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design System Triage: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "labels": ["Design/Design-System"],
                "timestamp": "2024-08-19T13:00:00Z",
                "request_id": "ds-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ds-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_ds-002"],
                "timestamp": "2024-08-19T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ds-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["ds/triage-open"],
                "remove_tags": [],
                "timestamp": "2024-08-19T13:00:00Z",
                "request_id": "ds-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "design_systems_triage",
                "status": "completed",
                "started_at": "2024-08-19T13:00:00Z",
                "ended_at": "2024-08-19T13:00:00Z",
                "timestamp": "2024-08-19T13:00:00Z",
                "request_id": "ds-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ds-001",
                "message_id":"msg_ds-002",
                "asset_id":"asset_ds-002",
                "tags":["ds/triage-open"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_071",
        instruction=(
            "You are the fix plan delivery owner for the Web UX D team and the time is 2024-08-23T13:50:00Z. "
            "Your goal is to coordinate a hybrid delivery for plan_011 on artifact art_001 according to policy by mirroring pending items as Figma comments and "
            "creating one ticket per pending item; after done, notify stakeholders using the canonical digest, add the fixplan delivery tag, "
            "and record the run while keeping identifiers deterministic."
        ),
        actions=[
            Action(name="compute_fix_plan_summary", kwargs={
                "plan_id": "plan_011",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-001",
            }),
            Action(name="deliver_fix_plan", kwargs={
                "plan_id": "plan_011",
                "delivery_method": "COMMENTS",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-002",
            }),
            Action(name="create_tickets_for_pending", kwargs={
                "plan_id": "plan_011",
                "tracker_project": "WEBUX",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-003",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Fix Plan Delivery: plan_011 — pending items",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "labels": ["FixPlan/Owners"],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_fp-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["fixplan/delivered"],
                "remove_tags": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-006",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fixplan_create_and_deliver",
                "status": "completed",
                "started_at": "2024-08-23T13:50:00Z",
                "ended_at": "2024-08-23T13:50:00Z",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-007",
            }),
        ],
        outputs=[
            {
                "plan_id":"plan_011",
                "delivery_method":"COMMENTS",
                "pending_count":6,
                "ticket_ids":["tix-item_011","tix-item_012","tix-item_013","tix-item_014","tix-item_015","tix-item_016"],
                "thread_id":"thr_fp-004",
                "message_id":"msg_fp-005",
                "tags":["fixplan/delivered"],
                "run_id":"run_fp-007",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_072",
        instruction=(
            "You are the design review coordinator for the Web UX B team and the time is 2024-08-23T10:05:00Z; "
            "continue the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Needs-Review', "
            "keep identifiers deterministic and reusable, and finalize the cycle by applying quorum."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:05:00Z",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_073",
        instruction=(
            "You are the fix item status updater and the time is 2024-08-27T14:00:00Z. "
            "Your goal is to update fix items from plan_012 for audit_012: mark item_018 and item_020 as APPLIED, "
            "leave item_017 and item_019 as PENDING, and record the run."
        ),
        actions=[
            Action(name="update_fix_item_status", kwargs={
                "item_id": "item_018",
                "status": "APPLIED",
                "timestamp": "2024-08-27T14:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="update_fix_item_status", kwargs={
                "item_id": "item_020",
                "status": "APPLIED",
                "timestamp": "2024-08-27T14:00:00Z",
                "request_id": "up-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fix_item_status_update",
                "status": "completed",
                "started_at": "2024-08-27T14:00:00Z",
                "ended_at": "2024-08-27T14:00:00Z",
                "timestamp": "2024-08-27T14:00:00Z",
                "request_id": "up-003",
            }),
        ],
        outputs=[
            '"item_id":"item_018","status":"APPLIED"',
            '"item_id":"item_020","status":"APPLIED"',
            '"run_id":"run_up-003"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_074",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-16T12:00:00Z; "
            "kick off an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'a11y/needs-audit'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-16T12:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Accessibility Audit: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "labels": ["Design/Accessibility"],
                "timestamp": "2024-08-16T12:00:00Z",
                "request_id": "ax-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ax-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-16T12:00:00Z",
                "request_id": "ax-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ax-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["a11y/needs-audit"],
                "remove_tags": [],
                "timestamp": "2024-08-16T12:00:00Z",
                "request_id": "ax-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "accessibility_audit_kickoff",
                "status": "completed",
                "started_at": "2024-08-16T12:00:00Z",
                "ended_at": "2024-08-16T12:00:00Z",
                "timestamp": "2024-08-16T12:00:00Z",
                "request_id": "ax-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ax-001",
                "message_id":"msg_ax-002",
                "asset_id":"asset_en-002",
                "tags":["a11y/needs-audit"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_075",
        instruction=(
            "You are the change request lead for the Web UX B team and the time is 2024-08-23T14:30:00Z; "
            "communicate requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Changes-Requested' by sending a request; "
            "after sending, mirror replies as Figma comments, move the cycle to CHANGES_REQUESTED, and add tag 'needs-changes'."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Changes Requested: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Changes-Requested"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_cr-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_cr-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_cr-001",
                "artifact_id": "art_001",
            }),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-23T14:30:00Z",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-changes"],
                "remove_tags": [],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "change_request",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"CHANGES_REQUESTED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_cr-001",
                "message_id":"msg_cr-002",
                "tags":["needs-changes"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_076",
        instruction=(
            "You are the audit report generator for the Web UX F team and the time is 2024-08-23T14:30:00Z. "
            "Your goal is to generate a combined audit report for audit_012 (artifact art_001) including both accessibility and design system findings; "
            "after generating the report, export it as a PDF report asset, and record the run."
        ),
        actions=[
            Action(name="generate_combined_audit_report", kwargs={
                "audit_id": "audit_012",
                "artifact_id": "art_001",
                "output_format": "PDF",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "combined_audit_report",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_012"',
            '"artifact_id":"art_001"',
            '"report_asset_id":"asset_au-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_077",
        instruction=(
            "You are the review program manager for the Web UX F team and the time is 2024-08-23T14:00:00Z; "
            "continue the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on the single thread labeled 'Design/Needs-Review' by sending a reminder. "
            "After sending, mirror replies as Figma comments, apply quorum, and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_078",
        instruction=(
            "You are the design review coordinator for the Web UX G team and the time is 2024-08-23T10:00:00Z; "
            "kick off an email-based design review for Figma artifact art_001 using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread for the day labeled 'Design/Needs-Review', "
            "and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:00:00Z",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
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
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_079",
        instruction=(
            "You are the design systems triage lead and the time is 2024-08-20T13:00:00Z; "
            "coordinate a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-systems@company.com','frontend-guild@company.com'] on a single thread labeled 'Design/Design-System'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'ds/triage-open'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-20T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design System Triage: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "labels": ["Design/Design-System"],
                "timestamp": "2024-08-20T13:00:00Z",
                "request_id": "ds-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ds-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_ds-002"],
                "timestamp": "2024-08-20T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ds-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["ds/triage-open"],
                "remove_tags": [],
                "timestamp": "2024-08-20T13:00:00Z",
                "request_id": "ds-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "design_systems_triage",
                "status": "completed",
                "started_at": "2024-08-20T13:00:00Z",
                "ended_at": "2024-08-20T13:00:00Z",
                "timestamp": "2024-08-20T13:00:00Z",
                "request_id": "ds-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ds-001",
                "message_id":"msg_ds-002",
                "asset_id":"asset_ds-002",
                "tags":["ds/triage-open"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_080",
        instruction=(
            "You are the release publisher for the Web UX F team and the time is 2024-08-23T11:00:00Z. "
            "Product wants stakeholders aligned—share a release handoff for artifact art_001, summarizing changes since release_001. "
            "Use export profile 'PNG 2x' for the attachment and send from sarah.designer@company.com to ['stakeholders@company.com','product-managers@company.com']; "
            "after sending, tag the artifact 'released/2024-08-23' and record the run."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),
            Action(name="create_release_record", kwargs={
                "artifact_id": "art_001",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "labels": ["released/2024-08-23"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/2024-08-23"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-23T11:00:00Z",
                "ended_at": "2024-08-23T11:00:00Z",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            {
                "previous_release_id":"release_001",
                "release_id":"rel-art_001-20240823-001",
                "asset_id":"asset_en-002",
                "export_id":"exp-art_001-20240823-png-001",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["released/2024-08-23"],
                "run_id":"run_rl-001",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_081",
        instruction=(
            "You are the review program manager for the Web UX G team and the time is 2024-08-23T14:00:00Z; "
            "continue the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on the single thread labeled 'Design/Needs-Review' by sending a reminder. "
            "After sending, mirror replies as Figma comments, apply quorum, and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_082",
        instruction=(
            "You are the audit report generator for the Web UX G team and the time is 2024-08-23T14:30:00Z. "
            "Your goal is to generate a combined audit report for audit_012 (artifact art_001) including both accessibility and design system findings; "
            "after generating the report, export it as a PDF report asset, and record the run."
        ),
        actions=[
            Action(name="generate_combined_audit_report", kwargs={
                "audit_id": "audit_012",
                "artifact_id": "art_001",
                "output_format": "PDF",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "combined_audit_report",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_012"',
            '"artifact_id":"art_001"',
            '"report_asset_id":"asset_au-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_083",
        instruction=(
            "You are the change request lead for the Web UX A team and the time is 2024-08-23T14:30:00Z; "
            "communicate requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Changes-Requested' by sending a request; "
            "after sending, mirror replies as Figma comments, move the cycle to CHANGES_REQUESTED, and add tag 'needs-changes'."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Changes Requested: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Changes-Requested"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_cr-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_cr-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_cr-001",
                "artifact_id": "art_001",
            }),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-23T14:30:00Z",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-changes"],
                "remove_tags": [],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "change_request",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"CHANGES_REQUESTED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_cr-001",
                "message_id":"msg_cr-002",
                "tags":["needs-changes"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_084",
        instruction=(
            "You are the fix plan delivery owner for the Web UX E team and the time is 2024-08-23T13:50:00Z. "
            "Your goal is to coordinate a hybrid delivery for plan_011 on artifact art_001 according to policy by mirroring pending items as Figma comments and "
            "creating one ticket per pending item; after done, notify stakeholders using the canonical digest, add the fixplan delivery tag, "
            "and record the run while keeping identifiers deterministic."
        ),
        actions=[
            Action(name="compute_fix_plan_summary", kwargs={
                "plan_id": "plan_011",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-001",
            }),
            Action(name="deliver_fix_plan", kwargs={
                "plan_id": "plan_011",
                "delivery_method": "COMMENTS",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-002",
            }),
            Action(name="create_tickets_for_pending", kwargs={
                "plan_id": "plan_011",
                "tracker_project": "WEBUX",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-003",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Fix Plan Delivery: plan_011 — pending items",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "labels": ["FixPlan/Owners"],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_fp-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["fix-owners@company.com", "design-review@company.com"],
                "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["fixplan/delivered"],
                "remove_tags": [],
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-006",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fixplan_create_and_deliver",
                "status": "completed",
                "started_at": "2024-08-23T13:50:00Z",
                "ended_at": "2024-08-23T13:50:00Z",
                "timestamp": "2024-08-23T13:50:00Z",
                "request_id": "fp-007",
            }),
        ],
        outputs=[
            {
                "plan_id":"plan_011",
                "delivery_method":"COMMENTS",
                "pending_count":6,
                "ticket_ids":["tix-item_011","tix-item_012","tix-item_013","tix-item_014","tix-item_015","tix-item_016"],
                "thread_id":"thr_fp-004",
                "message_id":"msg_fp-005",
                "tags":["fixplan/delivered"],
                "run_id":"run_fp-007",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_085",
        instruction=(
            "You are the design systems triage lead and the time is 2024-08-21T13:00:00Z; "
            "coordinate a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-systems@company.com','frontend-guild@company.com'] on a single thread labeled 'Design/Design-System'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'ds/triage-open'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-21T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design System Triage: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "labels": ["Design/Design-System"],
                "timestamp": "2024-08-21T13:00:00Z",
                "request_id": "ds-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ds-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_ds-002"],
                "timestamp": "2024-08-21T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ds-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["ds/triage-open"],
                "remove_tags": [],
                "timestamp": "2024-08-21T13:00:00Z",
                "request_id": "ds-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "design_systems_triage",
                "status": "completed",
                "started_at": "2024-08-21T13:00:00Z",
                "ended_at": "2024-08-21T13:00:00Z",
                "timestamp": "2024-08-21T13:00:00Z",
                "request_id": "ds-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ds-001",
                "message_id":"msg_ds-002",
                "asset_id":"asset_ds-002",
                "tags":["ds/triage-open"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_086",
        instruction=(
            "You are the design review coordinator for the Web UX H team and the time is 2024-08-23T10:00:00Z; "
            "kick off an email-based design review for Figma artifact art_001 using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread for the day labeled 'Design/Needs-Review', "
            "and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:00:00Z",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
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
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_087",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-15T12:00:00Z; "
            "kick off an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'a11y/needs-audit'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-15T12:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Accessibility Audit: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "labels": ["Design/Accessibility"],
                "timestamp": "2024-08-15T12:00:00Z",
                "request_id": "ax-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ax-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-15T12:00:00Z",
                "request_id": "ax-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ax-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["a11y/needs-audit"],
                "remove_tags": [],
                "timestamp": "2024-08-15T12:00:00Z",
                "request_id": "ax-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "accessibility_audit_kickoff",
                "status": "completed",
                "started_at": "2024-08-15T12:00:00Z",
                "ended_at": "2024-08-15T12:00:00Z",
                "timestamp": "2024-08-15T12:00:00Z",
                "request_id": "ax-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ax-001",
                "message_id":"msg_ax-002",
                "asset_id":"asset_en-002",
                "tags":["a11y/needs-audit"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_088",
        instruction=(
            "You are the design review coordinator for the Web UX D team and the time is 2024-08-24T09:00:00Z; "
            "run a same-day email-based design review for Figma artifact art_002 ('Pricing Page – Plans Grid') according to policy, using the 'PNG 2x' export, "
            "notifying ['design-review@company.com','growth-team@company.com'], keeping identifiers deterministic, and reusing the day's thread."

        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "artifact_id": "art_002",
                "started_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-002",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_002",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "en-004",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 2 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-004",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "thread_id": "thr_em-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-004"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_002",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "up-004",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-24T09:00:00Z",
                "ended_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_002-20240824-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-004",
                "thread_id":"thr_em-004",
                "message_id":"msg_em-005",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_089",
        instruction=(
            "You are the release publisher for the Web UX G team and the time is 2024-08-23T11:00:00Z. "
            "Product wants stakeholders aligned—share a release handoff for artifact art_001, summarizing changes since release_001. "
            "Use export profile 'PNG 2x' for the attachment and send from sarah.designer@company.com to ['stakeholders@company.com','product-managers@company.com']; "
            "after sending, tag the artifact 'released/2024-08-23' and record the run."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),
            Action(name="create_release_record", kwargs={
                "artifact_id": "art_001",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "labels": ["released/2024-08-23"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/2024-08-23"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-23T11:00:00Z",
                "ended_at": "2024-08-23T11:00:00Z",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            {
                "previous_release_id":"release_001",
                "release_id":"rel-art_001-20240823-001",
                "asset_id":"asset_en-002",
                "export_id":"exp-art_001-20240823-png-001",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["released/2024-08-23"],
                "run_id":"run_rl-001",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_090",
        instruction=(
            "You are the design review coordinator for the Web UX A team and the time is 2024-08-23T10:05:00Z; "
            "continue the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Needs-Review', "
            "keep identifiers deterministic and reusable, and finalize the cycle by applying quorum."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:05:00Z",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_091",
        instruction=(
            "You are the design systems triage lead and the time is 2024-08-22T13:00:00Z; "
            "coordinate a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-systems@company.com','frontend-guild@company.com'] on a single thread labeled 'Design/Design-System'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'ds/triage-open'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-22T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design System Triage: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "labels": ["Design/Design-System"],
                "timestamp": "2024-08-22T13:00:00Z",
                "request_id": "ds-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ds-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-systems@company.com", "frontend-guild@company.com"],
                "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_ds-002"],
                "timestamp": "2024-08-22T13:00:00Z",
                "request_id": "ds-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ds-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["ds/triage-open"],
                "remove_tags": [],
                "timestamp": "2024-08-22T13:00:00Z",
                "request_id": "ds-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "design_systems_triage",
                "status": "completed",
                "started_at": "2024-08-22T13:00:00Z",
                "ended_at": "2024-08-22T13:00:00Z",
                "timestamp": "2024-08-22T13:00:00Z",
                "request_id": "ds-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ds-001",
                "message_id":"msg_ds-002",
                "asset_id":"asset_ds-002",
                "tags":["ds/triage-open"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_092",
        instruction=(
            "You are the accessibility audit lead and the time is 2024-08-14T12:00:00Z; "
            "kick off an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'; "
            "after sending the request, mirror relevant replies as Figma comments, and tag the artifact 'a11y/needs-audit'. "
        ),
        actions=[
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-14T12:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Accessibility Audit: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "labels": ["Design/Accessibility"],
                "timestamp": "2024-08-14T12:00:00Z",
                "request_id": "ax-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_ax-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["accessibility@company.com", "design-review@company.com"],
                "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-14T12:00:00Z",
                "request_id": "ax-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_ax-001",
                "artifact_id": "art_001",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["a11y/needs-audit"],
                "remove_tags": [],
                "timestamp": "2024-08-14T12:00:00Z",
                "request_id": "ax-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "accessibility_audit_kickoff",
                "status": "completed",
                "started_at": "2024-08-14T12:00:00Z",
                "ended_at": "2024-08-14T12:00:00Z",
                "timestamp": "2024-08-14T12:00:00Z",
                "request_id": "ax-004",
            }),
        ],
        outputs=[
            {
                "thread_id":"thr_ax-001",
                "message_id":"msg_ax-002",
                "asset_id":"asset_en-002",
                "tags":["a11y/needs-audit"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_093",
        instruction=(
            "You are the review program manager for the Web UX H team and the time is 2024-08-23T14:00:00Z; "
            "continue the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on the single thread labeled 'Design/Needs-Review' by sending a reminder. "
            "After sending, mirror replies as Figma comments, apply quorum, and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:00:00Z",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_094",
        instruction=(
            "You are the change request lead for the Web UX team and the time is 2024-08-23T14:30:00Z; "
            "communicate requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Changes-Requested' by sending a request; "
            "after sending, mirror replies as Figma comments, move the cycle to CHANGES_REQUESTED, and add tag 'needs-changes'."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Changes Requested: Homepage Hero Section",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Changes-Requested"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_cr-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_cr-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_cr-001",
                "artifact_id": "art_001",
            }),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "status": "CHANGES_REQUESTED",
                "updated_at": "2024-08-23T14:30:00Z",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-changes"],
                "remove_tags": [],
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-003",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "change_request",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "cr-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"CHANGES_REQUESTED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_cr-001",
                "message_id":"msg_cr-002",
                "tags":["needs-changes"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_095",
        instruction=(
            "You are the design review coordinator for the Web UX E team and the time is 2024-08-24T09:00:00Z; "
            "run a same-day email-based design review for Figma artifact art_002 ('Pricing Page – Plans Grid') according to policy, using the 'PNG 2x' export, "
            "notifying ['design-review@company.com','growth-team@company.com'], keeping identifiers deterministic, and reusing the day's thread."

        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "artifact_id": "art_002",
                "started_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-002",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_002",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "en-004",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 2 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-004",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_002-20240824-001",
                "thread_id": "thr_em-004",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-004",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "growth-team@company.com"],
                "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                "attachments_asset_ids": ["asset_en-004"],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "em-005",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_002",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "up-004",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "review_kickoff",
                "status": "completed",
                "started_at": "2024-08-24T09:00:00Z",
                "ended_at": "2024-08-24T09:00:00Z",
                "timestamp": "2024-08-24T09:00:00Z",
                "request_id": "rv-004",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_002-20240824-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-004",
                "thread_id":"thr_em-004",
                "message_id":"msg_em-005",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_096",
        instruction=(
            "You are the fix item status updater and the time is 2024-08-28T14:00:00Z. "
            "Your goal is to update fix items from plan_012 for audit_012: mark item_019 and item_020 as APPLIED, "
            "leave item_017 and item_018 as PENDING, and record the run."
        ),
        actions=[
            Action(name="update_fix_item_status", kwargs={
                "item_id": "item_019",
                "status": "APPLIED",
                "timestamp": "2024-08-28T14:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="update_fix_item_status", kwargs={
                "item_id": "item_020",
                "status": "APPLIED",
                "timestamp": "2024-08-28T14:00:00Z",
                "request_id": "up-002",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "fix_item_status_update",
                "status": "completed",
                "started_at": "2024-08-28T14:00:00Z",
                "ended_at": "2024-08-28T14:00:00Z",
                "timestamp": "2024-08-28T14:00:00Z",
                "request_id": "up-003",
            }),
        ],
        outputs=[
            '"item_id":"item_019","status":"APPLIED"',
            '"item_id":"item_020","status":"APPLIED"',
            '"run_id":"run_up-003"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_097",
        instruction=(
            "You are the release publisher for the Web UX H team and the time is 2024-08-23T11:00:00Z. "
            "Product wants stakeholders aligned—share a release handoff for artifact art_001, summarizing changes since release_001. "
            "Use export profile 'PNG 2x' for the attachment and send from sarah.designer@company.com to ['stakeholders@company.com','product-managers@company.com']; "
            "after sending, tag the artifact 'released/2024-08-23' and record the run."
        ),
        actions=[
            Action(name="get_release_diff", kwargs={"release_id": "release_001"}),
            Action(name="create_release_record", kwargs={
                "artifact_id": "art_001",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "labels": ["released/2024-08-23"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["stakeholders@company.com","product-managers@company.com"],
                "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["released/2024-08-23"],
                "remove_tags": [],
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "release_handoff",
                "status": "completed",
                "started_at": "2024-08-23T11:00:00Z",
                "ended_at": "2024-08-23T11:00:00Z",
                "timestamp": "2024-08-23T11:00:00Z",
                "request_id": "rl-001",
            }),
        ],
        outputs=[
            {
                "previous_release_id":"release_001",
                "release_id":"rel-art_001-20240823-001",
                "asset_id":"asset_en-002",
                "export_id":"exp-art_001-20240823-png-001",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["released/2024-08-23"],
                "run_id":"run_rl-001",
                "status":"completed",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_098",
        instruction=(
            "You are the audit report generator for the Web UX H team and the time is 2024-08-23T14:30:00Z. "
            "Your goal is to generate a combined audit report for audit_012 (artifact art_001) including both accessibility and design system findings; "
            "after generating the report, export it as a PDF report asset, and record the run."
        ),
        actions=[
            Action(name="generate_combined_audit_report", kwargs={
                "audit_id": "audit_012",
                "artifact_id": "art_001",
                "output_format": "PDF",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-001",
            }),
            Action(name="record_automation_run", kwargs={
                "task_name": "combined_audit_report",
                "status": "completed",
                "started_at": "2024-08-23T14:30:00Z",
                "ended_at": "2024-08-23T14:30:00Z",
                "timestamp": "2024-08-23T14:30:00Z",
                "request_id": "au-002",
            }),
        ],
        outputs=[
            '"audit_id":"audit_012"',
            '"artifact_id":"art_001"',
            '"report_asset_id":"asset_au-001"',
            '"run_id":"run_au-002"',
            '"status":"completed"',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_099",
        instruction=(
            "You are the design review coordinator for the Web UX team and the time is 2024-08-23T10:05:00Z; "
            "continue the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Needs-Review', "
            "keep identifiers deterministic and reusable, and finalize the cycle by applying quorum."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:05:00Z",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:05:00Z",
                "request_id": "em-002",
            }),
            Action(name="sync_replies_to_figma_comments", kwargs={
                "thread_id": "thr_em-001",
                "artifact_id": "art_001",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "design-review@company.com",
                "intent": "APPROVE",
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "approver_email": "ux-team@company.com",
                "intent": "APPROVE",
            }),
            Action(name="update_review_status_by_quorum", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
            }),
        ],
        outputs=[
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"APPROVED",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
            }
        ],
    ),
    Task(
        annotator="0",
        user_id="res_100",
        instruction=(
            "You are the design review coordinator for the Web UX I team and the time is 2024-08-23T10:00:00Z; "
            "kick off an email-based design review for Figma artifact art_001 using the 'PNG 2x' export, "
            "notify recipients ['design-review@company.com','ux-team@company.com'] on a single thread for the day labeled 'Design/Needs-Review', "
            "and keep identifiers deterministic and reusable."
        ),
        actions=[
            Action(name="create_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "artifact_id": "art_001",
                "started_at": "2024-08-23T10:00:00Z",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "rv-001",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
            }),
            Action(name="export_assets", kwargs={
                "artifact_id": "art_001",
                "export_profile": "PNG 2x",
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "en-002",
            }),
            Action(name="create_gmail_thread", kwargs={
                "subject": "Design Review Request: 1 frames ready for review",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "labels": ["Design/Needs-Review"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-001",
            }),
            Action(name="link_cycle_to_thread", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
                "thread_id": "thr_em-001",
            }),
            Action(name="append_gmail_message", kwargs={
                "thread_id": "thr_em-001",
                "sender_email": "sarah.designer@company.com",
                "recipients": ["design-review@company.com", "ux-team@company.com"],
                "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                "attachments_asset_ids": ["asset_en-002"],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "em-002",
            }),
            Action(name="governance_update", kwargs={
                "artifact_id": "art_001",
                "add_tags": ["needs-review"],
                "remove_tags": [],
                "timestamp": "2024-08-23T10:00:00Z",
                "request_id": "up-001",
            }),
            Action(name="get_review_cycle", kwargs={
                "cycle_id": "rev-art_001-20240823-001",
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
            {
                "cycle_id":"rev-art_001-20240823-001",
                "cycle_status":"NEEDS_REVIEW",
                "asset_id":"asset_en-002",
                "thread_id":"thr_em-001",
                "message_id":"msg_em-002",
                "tags":["needs-review"],
                "status":"completed",
            }
        ],
    ),
]
