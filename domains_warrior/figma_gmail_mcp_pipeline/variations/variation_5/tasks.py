from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="MED_1",
        instruction="You are a cross-channel design-review posture coordinator responsible for triage consistency, policy alignment, and audit-ready traceability across Gmail and Figma. Work centers on the Gmail conversation in the design-review label involving alex.dev@company.com with the subject keyword 'Design'; the scope is the active conversation tracked as thread_001 requiring a normalized triage stance and sync eligibility. Policy context should remain aligned with the organization 's DLP configuration and intent keywords so communication remains safe and stakeholder reporting is consistent. The coordination outcome is a stakeholder-ready record in which thread_001 reflects a triaged, figma-sync posture with the 'urgent' designation deprecated effective 2024-08-22T12:00:00Z, and a DLP assessment confirming the conversation is clean, providing timestamped evidence for audit visibility and Figma synchronization. Constants: label design-review; participant alex.dev@company.com; keyword Design; thread_id thread_001; add_labels [triaged, figma-sync]; remove_labels [urgent]; changed_ts 2024-08-22T12:00:00Z.",
        actions=[
            Action(name="search_gmail_threads", kwargs={"label": "design-review", "participant": "alex.dev@company.com", "keyword": "Design"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_001", "add_labels": ["triaged", "figma-sync"], "remove_labels": ["urgent"], "changed_ts": "2024-08-22T12:00:00Z"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_001"})
        ],
        outputs=[
            """{
            "thread_id": "thread_001",
            "blocked_terms_found": []
            }"""
        ]
    ),

    Task(
        annotator="0",
        user_id="MED_2",
        instruction=(
            "You draft a concise release announcement and verify differences for release_001 without over-specifying the process. "
            "Treat the public release catalog under version_prefix release/ (artifact_id None) as the context for change verification and then prepare a message in thread_006 from sarah.designer@company.com at 2024-08-22T17:00:00Z. "
            "The announcement must use subject 'Release 1.2.0 Announcement' and body text 'Highlights and changes included.' so that the resulting draft id can be tracked. "
            "Use constants exactly: version_prefix release/, artifact_id None, release_id release_001, thread_id thread_006, from_email sarah.designer@company.com, created_ts 2024-08-22T17:00:00Z, subject 'Release 1.2.0 Announcement', body 'Highlights and changes included.'."
        ),
        actions=[
            Action(name="list_releases", kwargs={"version_prefix": "release/", "artifact_id": None}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."})
        ],
        outputs=[
            """{
            "success": true,
            "message_id": "relmsg_9cc87e81"
            }"""
        ]
    ),

    Task(
        annotator="0",
        user_id="MED_3",
        instruction=(
            "You are the audit follow-up owner for art_001. Your goal is to ensure that completed findings are understood, a new combined design-system/accessibility review exists, and preparation is logged with the right configuration context. "
            "Anchor your reasoning in these fixed references: artifact_id art_001, status COMPLETED, audit_id audit_001, created_ts 2024-08-23T09:00:00Z, audit_type COMBINED_DS_A11Y, config_key dlp_config, log_ts 2024-08-23T09:05:00Z, message 'Prepared audit session for art_001'. "
            "Avoid prescriptive step lists; the expectation is that the above identifiers and timestamps are reflected in the updated state and the final note."
        ),
        actions=[
            Action(name="list_audits", kwargs={"artifact_id": "art_001", "status": "COMPLETED"}),
            Action(name="summarize_audit", kwargs={"audit_id": "audit_001"}),
            Action(name="create_audit_session", kwargs={"artifact_id": "art_001", "created_ts": "2024-08-23T09:00:00Z", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="read_system_config", kwargs={"config_key": "dlp_config"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-23T09:05:00Z", "message": "Prepared audit session for art_001"})
        ],
        outputs=[
            """{
            "success": true,
            "log_id": "log_7c69622f"
            }"""
        ]
    ),

    Task(
        annotator="0",
        user_id="MED_4",
        instruction=(
            "You are a release announcement coordinator ensuring draft safety and label alignment for the 1.4.0 rollout. "
            "Maintain compliant posture for the existing Release 1.4.0 conversation and reflect a clear draft state without prescribing step order. "
            "Use constants: release_id release_004, thread_id thread_008, message_id relmsg_f9e9c1b6, from_email sarah.designer@company.com, "
            "created_ts 2024-08-23T16:30:00Z, changed_ts 2024-08-23T16:35:00Z, subject 'Release 1.4.0 Announcement', body 'Changelog and new components included.'"
        ),
        actions=[
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_004",
                "thread_id": "thread_008",
                "from_email": "sarah.designer@company.com",
                "created_ts": "2024-08-23T16:30:00Z",
                "subject": "Release 1.4.0 Announcement",
                "body": "Changelog and new components included."
            }),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_f9e9c1b6"}),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_008",
                "add_labels": ["release-draft"],
                "remove_labels": [],
                "changed_ts": "2024-08-23T16:35:00Z"
            }),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_008"})
        ],
        outputs=[
            """{
              "thread_id": "thread_008",
              "blocked_terms_found": []
            }"""
        ]
    ),

    Task(
        annotator="0",
        user_id="MED_5",
        instruction="You are a release communications and DLP posture steward for the Design Tokens update, responsible for stakeholder-safe announcement traceability and audit-grade labeling across Gmail collaboration threads with awareness of Figma library token context. Work is anchored to release release_011 and centers on the discussion thread thread_013 associated with pm.lead@company.com; the announcement content is fixed as “Candidate build ready for stakeholder walkthrough.” with authored time 2024-08-23T19:20:00Z. Policy context should remain aligned with the organization 's DLP configuration and intent keywords so that communication remains safe, consistent, and reportable, and so downstream dashboards and audit logs present deterministic outcomes. The coordination outcome is: the Gmail thread reflects the candidate announcement at the stated timestamp, and the thread 's DLP posture is evaluated once; if sensitive terms are detected the thread is labeled dlp-flag with timestamped traceability at 2024-08-23T19:22:00Z, otherwise no label is applied. Constants: release_id release_011; thread_id thread_013; from_email pm.lead@company.com; created_ts 2024-08-23T19:20:00Z; body “Candidate build ready for stakeholder walkthrough.”; dlp_label_if_found dlp-flag with dlp_changed_ts 2024-08-23T19:22:00Z.",
        actions=[
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_013",
                "from_email": "pm.lead@company.com",
                "body": "Candidate build ready for stakeholder walkthrough.",
                "created_ts": "2024-08-23T19:20:00Z"
            }),
            Action(name="dlp_scan_and_label_thread", kwargs={
                "thread_id": "thread_013",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-23T19:22:00Z"
            })
        ],
        outputs=[
            """{
              "thread_id": "thread_013",
              "blocked_terms_found": [],
              "label_applied": false
            }"""
        ]
    ),

    Task(
        annotator="0",
        user_id="MED_6",
        instruction=(
            "You are a design-system release coordination owner ensuring announcements align with catalog scope and safety posture. "
            "Operate on the design-system navigation update without prescribing tool order and ultimately scan dlp thread. "
            "Use constants: version_prefix release/, release_id release_006, thread_id thread_010, from_email sarah.designer@company.com, "
            "created_ts 2024-08-23T18:20:00Z, subject 'Design System v1.1.0 - Navigation Components', body 'Tokens and components updated.'"
        ),
        actions=[
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_006"}),
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_006",
                "thread_id": "thread_010",
                "from_email": "sarah.designer@company.com",
                "created_ts": "2024-08-23T18:20:00Z",
                "subject": "Design System v1.1.0 - Navigation Components",
                "body": "Tokens and components updated."
            }),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_010"})
        ],
        outputs=[
            """{
              "thread_id": "thread_010",
              "blocked_terms_found": []
            }"""
        ]
    ),

    Task(
        annotator="0",
        user_id="MED_7",
        instruction=(
        "You are a Figma accessibility coordination specialist responsible for dashboard header compliance alignment and audit traceability. "
        "Work centers on the dashboard header frame art_004 owned by mike.ux@company.com within the dashboard working set; the scope is the FRAME type modified since 2024-08-01T00:00:00Z. "
        "Policy context should remain aligned with the organization's dlp configuration and intent keywords to ensure safe, consistent communication and accurate stakeholder reporting. "
        "The coordination outcome is a concise, stakeholder-ready summary of the completed audit audit_004 and an artifact status that reflects a11y-reviewed with timestamped traceability. "
        "Constants: owner_email mike.ux@company.com, tag dashboard, artifact_type FRAME, modified_since 2024-08-01T00:00:00Z, artifact_id art_004, audit_id audit_004, tag a11y-reviewed at 2024-08-23T18:30:00Z."
        ),
        actions=[
            Action(name="read_system_config", kwargs={"config_key": "dlp_config"}),
            Action(name="read_system_config", kwargs={"config_key": "intent_keywords"}),
            Action(name="list_artifacts", kwargs={
                "owner_email": "mike.ux@company.com",
                "tag": "dashboard",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="list_audits", kwargs={"artifact_id": "art_004", "status": "COMPLETED"}),
            Action(name="summarize_audit", kwargs={"audit_id": "audit_004"}),
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_004",
                "tag": "a11y-reviewed",
                "changed_ts": "2024-08-23T18:30:00Z"
            })
        ],
        outputs=[
            """{
              "audit_id": "audit_004",
              "ds_findings": 0,
              "a11y_findings": 2
            }"""
        ]
    ),

    Task(
        annotator="0",
        user_id="MED_8",
        instruction=(
        "You are a review progression and approval traceability owner for pricing components, responsible for stakeholder-ready status alignment and audit-grade documentation. "
        "Work is anchored to the active cycle cycle_008; coordination emphasizes deterministic timing, clear approver attribution, and policy-aligned visibility. "
        "The approval record should attribute pm.lead@company.com with decision APPROVED at 2024-08-23T20:10:00Z using the approval note 'Looks good to ship.', and an operational note 'Approval recorded for pricing review' should be reflected at 2024-08-23T20:12:00Z for traceability. "
        "The review state must present a finalized APPROVED posture by 2024-08-23T20:15:00Z so release readiness and reporting remain consistent. "
        "Constants: cycle_id cycle_008; approver_email pm.lead@company.com; decision APPROVED at 2024-08-23T20:10:00Z; approval_comment 'Looks good to ship.'; op_note 'Approval recorded for pricing review' at 2024-08-23T20:12:00Z; final_status APPROVED at 2024-08-23T20:15:00Z."
        ),
        actions=[
            Action(name="record_review_approval", kwargs={
                "cycle_id": "cycle_008",
                "approver_email": "pm.lead@company.com",
                "decision": "APPROVED",
                "decided_ts": "2024-08-23T20:10:00Z",
                "comment": "Looks good to ship."
            }),
            Action(name="log_terminal_event", kwargs={
                "log_ts": "2024-08-23T20:12:00Z",
                "message": "Approval recorded for pricing review"
            }),
            Action(name="advance_review_status", kwargs={
                "cycle_id": "cycle_008",
                "new_status": "APPROVED",
                "changed_ts": "2024-08-23T20:15:00Z"
            })
        ],
        outputs=[
            """{
              "success": true,
              "cycle_id": "cycle_008",
              "from": "NEEDS_REVIEW",
              "to": "APPROVED"
            }"""
        ]
    ),

    Task(
        annotator="0",
        user_id="MED_9",
        instruction="You are a cross-surface coordination owner for a data-table design discussion, ensuring Gmail thread discoverability, DLP-aligned safety posture, and copy alignment with related Figma artifacts. Work is anchored to thread thread_009; scope centers on label hygiene and a stakeholder-ready PM nudge that avoids sensitive terms. The coordination outcome is a concise PM message recorded in-thread and a label posture reflecting design-review with timestamped traceability, with a clean DLP scan (blocked_terms_found=[]). Constants: thread_id thread_009; add_labels ['design-review'] at 2024-08-23T18:00:00Z; from_email pm.lead@company.com; created_ts 2024-08-23T18:05:00Z; body 'Copy update alignment requested for homepage hero and pricing sections.'",
        actions=[
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_009",
                "add_labels": ["design-review"],
                "remove_labels": [],
                "changed_ts": "2024-08-23T18:00:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_009",
                "from_email": "pm.lead@company.com",
                "body": "Copy update alignment requested for homepage hero and pricing sections.",
                "created_ts": "2024-08-23T18:05:00Z"
            }),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_009"})
        ],
        outputs=[
            """{
              "thread_id": "thread_009",
              "blocked_terms_found": []
            }"""
        ]
    ),

    Task(
        annotator="0",
        user_id="MED_10",
        instruction="You are a handoff coordinator ensuring the pricing page frame is marked ready and assets are enumerated for delivery. Rely on these exact anchors: Gmail owner_email lisa.marketing@company.com, tag needs-review, Figma artifact_type FRAME, modified_since 2024-08-01T00:00:00Z, artifact_id art_007, add_tag handoff-ready, changed_ts 2024-08-23T08:45:00Z. You capture the asset snapshot for art_007 after the tag update.",
        actions=[
            Action(name="list_artifacts", kwargs={ 'owner_email': 'lisa.marketing@company.com', 'tag': 'needs-review', 'artifact_type': 'FRAME', 'modified_since': '2024-08-01T00:00:00Z' }),
            Action(name="add_artifact_tag", kwargs={ 'artifact_id': 'art_007', 'tag': 'handoff-ready', 'changed_ts': '2024-08-23T08:45:00Z' }),
            Action(name="list_assets_for_artifact", kwargs={ 'artifact_id': 'art_007' })
        ],
        outputs=[
            "[\n  {\n    \"asset_id\": \"asset_006\",\n    \"profile\": null,\n    \"file_name\": null,\n    \"mime_type\": null\n  }\n]"
        ],
    ),

    Task(
        annotator="0",
        user_id="MED_11",
        instruction="You are the approval-traceability owner for the Figma Navigation Bar review. Tell a policy-aligned audit story where art_002 opens a review at 2024-08-23T10:00:00Z, transitions to NEEDS_REVIEW at 10:05:00Z, captures a recorded decision APPROVED from Gmail alex.dev@company.com at 10:06:00Z with rationale 'Looks good.', and reaches terminal status APPROVED at 10:07:00Z. Ground this narrative in the system of record by returning the canonical artifact summary for art_002; do not vary the identifiers, statuses, timestamps, approver, or comment.",
        actions=[
            Action(name="start_review_cycle", kwargs={ 'artifact_id': 'art_002', 'created_ts': '2024-08-23T10:00:00Z' }),
            Action(name="advance_review_status", kwargs={ 'cycle_id': 'cycle_2c0e9232', 'new_status': 'NEEDS_REVIEW', 'changed_ts': '2024-08-23T10:05:00Z' }),
            Action(name="record_review_approval", kwargs={ 'cycle_id': 'cycle_2c0e9232', 'approver_email': 'alex.dev@company.com', 'decision': 'APPROVED', 'decided_ts': '2024-08-23T10:06:00Z', 'comment': 'Looks good.' }),
            Action(name="advance_review_status", kwargs={ 'cycle_id': 'cycle_2c0e9232', 'new_status': 'APPROVED', 'changed_ts': '2024-08-23T10:07:00Z' }),
            Action(name="get_artifact_summary", kwargs={ 'artifact_id': 'art_002' })
        ],
        outputs=[
            "{\n  \"artifact_id\": \"art_002\",\n  \"artifact_name\": \"Navigation Bar\",\n  \"artifact_type\": \"FRAME\",\n  \"deep_link\": \"https://www.figma.com/file/abc123def456/Design-System?node-id=1%3A4\",\n  \"owner_email\": \"sarah.designer@company.com\",\n  \"current_tags\": [\n    \"navigation\",\n    \"header\",\n    \"global\"\n  ],\n  \"modified_ts\": \"2024-08-21T09:15:00Z\"\n}"
        ],
    ),

    Task(
        annotator="0",
        user_id="MED_12",
        instruction="You prepare a concise release draft for the mobile app v2.1.0 and confirm attachment policy compliance. Compose in thread_id thread_007 with release_id release_002 from from_email mike.ux@company.com at created_ts 2024-08-23T12:30:00Z with subject 'Mobile App v2.1.0 Release' and body 'Shipping profile & dashboard improvements.' Then run a guard check using the produced message_id.",
        actions=[
            Action(name="compose_release_email_draft", kwargs={ 'release_id': 'release_002', 'thread_id': 'thread_007', 'from_email': 'mike.ux@company.com', 'created_ts': '2024-08-23T12:30:00Z', 'subject': 'Mobile App v2.1.0 Release', 'body': 'Shipping profile & dashboard improvements.' }),
            Action(name="guard_attachment_policy_on_draft", kwargs={ 'message_id': 'relmsg_5b8194ea' })
        ],
        outputs=[
            "{\n  \"message_id\": \"relmsg_5b8194ea\",\n  \"approx_body_bytes\": 42,\n  \"max_total_bytes\": 10000000,\n  \"ok\": true\n}"
        ],
    ),


    # complexity_edges: 8
    Task(
        annotator="0",
        user_id="MED_13",
        instruction=(
            "You draft a concise release announcement and validate attachment policy, then confirm linked assets. "
            "Use constants exactly: release_id release_001, thread_id thread_006, from_email sarah.designer@company.com, "
            "created_ts 2024-08-22T17:00:00Z, subject 'Release 1.2.0 Announcement', body 'Highlights and changes included.', "
            "and finally list assets for artifact_id art_001."
        ),
        actions=[
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[
            """[
                {
                    "asset_id": "asset_001",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                },
                {
                    "asset_id": "asset_002",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                }
            ]"""
        ]
    ),

    Task(
        annotator="0",
        user_id="MED_14",
        instruction="You are a marketing token-policy compliance coordinator responsible for asset enumeration and stakeholder-ready artifact reporting. Work centers on the marketing file set owned by lisa.marketing@company.com within the website tag; the scope is the FILE type modified since 2024-08-01T00:00:00Z, with art_006 as the target artifact. Policy context remains aligned with configuration design_system_mappings, and outcomes should be Figma deep-link aware and suitable for sharing via Gmail. The coordination outcome is a concise, traceable summary of art_006 plus an operational Gmail note capturing “Checked marketing file assets” at 2024-08-23T13:30:00Z. Constants: config_key design_system_mappings; owner_email lisa.marketing@company.com; tag website; artifact_type FILE; modified_since 2024-08-01T00:00:00Z; artifact_id art_006; log_ts 2024-08-23T13:30:00Z; message “Checked marketing file assets”.",
        actions=[
            Action(name="read_system_config", kwargs={"config_key": "design_system_mappings"}),
            Action(name="list_artifacts", kwargs={"owner_email": "lisa.marketing@company.com", "tag": "website", "artifact_type": "FILE", "modified_since": "2024-08-01T00:00:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_006"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-23T13:30:00Z", "message": "Checked marketing file assets"}),
            Action(name="get_artifact_summary", kwargs={"artifact_id": "art_006"})
        ],
        outputs=[
            """{
            "artifact_id": "art_006",
            "artifact_name": "Marketing Website",
            "artifact_type": "FILE",
            "owner_email": "lisa.marketing@company.com",
            "deep_link": "https://www.figma.com/file/def456ghi789/Marketing-Website",
            "current_tags": [
                "marketing",
                "website",
                "landing-pages"
            ],
            "modified_ts": "2024-08-21T15:30:00Z"
            }"""
        ]
    ),

    # complexity_edges: 9
    Task(
        annotator="0",
        user_id="MED_15",
        instruction="You are a cross-channel review coordination owner for Gmail nudges and Figma asset verification, responsible for auditable reminder delivery, label taxonomy alignment, and availability reporting. Work is anchored to conversation thread thread_003 and artifact art_001; communication should be concise, policy-aligned, and traceable for stakeholders. The coordination outcome is a timestamped reviewer nudge attributed to john.pm@company.com, a thread state reflecting the needs-review label for tracking, and a current asset inventory for reporting. Constants: thread_id thread_003; from_email john.pm@company.com; message body “Please review the latest update today.” at 2024-08-23T13:07:00Z; label needs-review at 2024-08-23T13:08:00Z; artifact_id art_001.",
        actions=[
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_003", "from_email": "john.pm@company.com", "body": "Please review the latest update today.", "created_ts": "2024-08-23T13:07:00Z"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_003", "add_labels": ["needs-review"], "remove_labels": [], "changed_ts": "2024-08-23T13:08:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[
            """[
                {
                    "asset_id": "asset_001",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                },
                {
                    "asset_id": "asset_002",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                }
            ]"""
        ]
    ),


    # complexity_edges: 7
    Task(
        annotator="0",
        user_id="MED_16",
        instruction=(
            "You formalize approval tracking on art_004: open the review cycle at 2024-08-23T13:00:00Z, "
            "then record APPROVED by alex.dev@company.com at 2024-08-23T13:25:00Z with comment 'LGTM'. "
            "Finish by listing assets for art_001."
        ),
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="record_review_approval", kwargs={"cycle_id": "cycle_1dc59e3f", "approver_email": "alex.dev@company.com", "decision": "APPROVED", "decided_ts": "2024-08-23T13:25:00Z", "comment": "LGTM"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[
            """[
                {
                    "asset_id": "asset_001",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                },
                {
                    "asset_id": "asset_002",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                }
            ]"""
        ]
    ),


    # complexity_edges: 9
    Task(
        annotator="0",
        user_id="MED_17",
        instruction=(
            "You remove a deprecated tag and ensure the thread is labeled correctly, then confirm exported assets. "
            "For art_005 remove tag deprecated at changed_ts 2024-08-23T10:50:00Z; for thread_005 add label housekeeping "
            "at changed_ts 2024-08-23T10:55:00Z. Conclude by listing assets for art_001."
        ),
        actions=[
            Action(name="remove_artifact_tag", kwargs={"artifact_id": "art_005", "tag": "deprecated", "changed_ts": "2024-08-23T10:50:00Z"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_005", "add_labels": ["housekeeping"], "remove_labels": [], "changed_ts": "2024-08-23T10:55:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[
            """[
                {
                    "asset_id": "asset_001",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                },
                {
                    "asset_id": "asset_002",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                }
            ]"""
        ]
    ),

    # complexity_edges: 8
    Task(
        annotator="0",
        user_id="MED_18",
        instruction=(
            "You prepare a minimal release communication and attach a deterministic asset reference. "
            "Confirm diff context with release_id release_001, then compose a draft in thread_id thread_006 from from_email sarah.designer@company.com at created_ts 2024-08-22T17:00:00Z "
            "using subject 'Release 1.2.0 Summary' and body 'Highlights and changes included.'. "
            "Return the exported assets for artifact_id art_001."
        ),
        actions=[
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Summary", "body": "Highlights and changes included."}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """{
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }"""
    ],
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="MED_19",
        instruction="You are the design-review conversation steward ensuring crisp label posture, one concise reviewer cue, and a stable asset reference. Focus on the conversation that matches label design-review, participant mike.ux@company.com, keyword 'Review'; normalize thread_001 so that needs-attention and Design/Needs-Review are present while old-tag is absent with label state effective 2024-08-24T10:15:00Z. Preserve a short reviewer prompt from sarah.designer@company.com at 10:16:00Z with exact body 'Requesting review for art_002.'. Deliver the exported assets for art_001 as the downstream anchor.",
        actions=[
            Action(name="search_gmail_threads", kwargs={"label": "design-review", "participant": "mike.ux@company.com", "keyword": "Review"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_001", "add_labels": ["needs-attention", "Design/Needs-Review"], "remove_labels": ["old-tag"], "changed_ts": "2024-08-24T10:15:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_001", "from_email": "sarah.designer@company.com", "body": "Requesting review for art_002.", "created_ts": "2024-08-24T10:16:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """{
        "asset_id": "asset_001",
        "profile": null,
        "file_name": null,
        "mime_type": null
        },
        {
        "asset_id": "asset_002",
        "profile": null,
        "file_name": null,
        "mime_type": null
        }"""
        ],
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="MED_20",
        instruction="You are the pricing-page audit-readiness steward responsible for a policy-aligned snapshot and a precise status marker. The canonical record must evidence: completed audits on art_007 with a summary for audit_005; art_007 in posture audit-pending effective 2024-08-25T12:01:00Z; a fresh COMBINED_DS_A11Y session on art_007 with creation time 2024-08-25T12:00:00Z; audit_workflow_config recognized as the scope authority; asset visibility for art_007; and a terminal program log with the exact text 'Initiated combined audit session for art_007' at 2024-08-25T12:02:00Z.",
        actions=[
            Action(name="list_audits", kwargs={"artifact_id": "art_007", "status": "COMPLETED"}),
            Action(name="summarize_audit", kwargs={"audit_id": "audit_005"}),
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_007", "tag": "audit-pending", "changed_ts": "2024-08-25T12:01:00Z"}),
            Action(name="create_audit_session", kwargs={"artifact_id": "art_007", "created_ts": "2024-08-25T12:00:00Z", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="read_system_config", kwargs={"config_key": "audit_workflow_config"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_007"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-25T12:02:00Z", "message": "Initiated combined audit session for art_007"})
        ],
        outputs=[
            """{
    "audit_id": "audit_005",
    "ds_findings": 0,
    "a11y_findings": 0
    }"""
    ]
    ),

    # Auto Task 11
    Task(
        annotator="0",
        user_id="HARD_1",
        instruction=(
            "You synchronize review sentiment from Gmail into a review cycle for art_004 and quantify it. "
            "The cycle you operate is identified as cycle_id cycle_1dc59e3f linked to thread_003, "
            "and you will incorporate two deterministic messages for intent parsing at created_ts 2024-08-23T13:10:00Z and 2024-08-23T13:15:00Z with the exact bodies "
            "'Looks good—LGTM from marketing.' from email lisa.marketing@company.com and 'Please REVISE the grid spacing to 8px multiples.' from alex.dev@company.com, respectively. "
            "Grounding constants: artifact_id art_004, cycle_id cycle_1dc59e3f, thread_id thread_003, created_ts 2024-08-23T13:00:00Z/13:05:00Z/13:10:00Z/13:15:00Z."
        ),
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_003", "from_email": "lisa.marketing@company.com", "body": "Looks good—LGTM from marketing.", "created_ts": "2024-08-23T13:10:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_003", "from_email": "alex.dev@company.com", "body": "Please REVISE the grid spacing to 8px multiples.", "created_ts": "2024-08-23T13:15:00Z"}),
            Action(name="sync_gmail_intents_to_review", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003"})
        ],
        outputs=[
            """{
            "cycle_id": "cycle_1dc59e3f",
            "thread_id": "thread_003",
            "intent_counts": {
                "approve": 1,
                "changes": 1,
                "blocker": 0
            }
            }"""
        ]
    ),

    Task(
        annotator="0",
        user_id="HARD_2",
        instruction="You are the QA readiness provenance steward ensuring signal alignment and database-state hygiene across the Figma↔Gmail workflow. Deliver an audit-ready record (facts, not procedures) anchored to artifact art_009 and thread thread_011—order-agnostic and reflecting only persisted DB mutations—confirming: tag qa-ready present on art_009 effective 2024-08-23T19:00:00Z; a Figma comment by qa.lead@company.com at node-9:3 with exact text 'QA ready. Please create checklist.' at 2024-08-23T19:05:00Z; a Gmail message on thread_011 from qa.lead@company.com at 2024-08-23T19:10:00Z with body 'QA checklist attached. Please review.'; and a DLP evaluation of thread_011 using label dlp-flag at 2024-08-23T19:12:00Z. Return a concise DLP findings summary and whether a label was applied.",
        actions=[
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_009",
                "tag": "qa-ready",
                "changed_ts": "2024-08-23T19:00:00Z"
            }),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_009",
                "author_email": "qa.lead@company.com",
                "body": "QA ready. Please create checklist.",
                "anchor_ref": "node-9:3",
                "created_ts": "2024-08-23T19:05:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_011",
                "from_email": "qa.lead@company.com",
                "body": "QA checklist attached. Please review.",
                "created_ts": "2024-08-23T19:10:00Z"
            }),
            Action(name="dlp_scan_and_label_thread", kwargs={
                "thread_id": "thread_011",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-23T19:12:00Z"
            })
        ],
        outputs=[
            """{
              "thread_id": "thread_011",
              "blocked_terms_found": [],
              "label_applied": false
            }"""
        ]
    ),


    # --- Fixed user_229 ---
    Task(
        annotator="0",
        user_id="HARD_3",
        instruction=(
            "You coordinate a hotfix announcement with deterministic labeling and a single safety evaluation. "
            "Use constants: release_id release_010, thread_id thread_011, "
            "from_email pm.lead@company.com at created_ts 2024-08-24T13:30:00Z subject 'Hotfix 2.0.1 Patch' body 'Fixes urgent bug.', "
            "ack_from qa.lead@company.com at 2024-08-24T13:40:00Z 'LGTM for hotfix.', triage_changed_ts 2024-08-24T13:35:00Z, "
            "dlp_label_if_found dlp-flag with dlp_changed_ts 2024-08-24T13:42:00Z."
        ),
        actions=[
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_011",
                "add_labels": ["triaged"],
                "remove_labels": [],
                "changed_ts": "2024-08-24T13:35:00Z"
            }),
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_010",
                "thread_id": "thread_011",
                "from_email": "pm.lead@company.com",
                "created_ts": "2024-08-24T13:30:00Z",
                "subject": "Hotfix 2.0.1 Patch",
                "body": "Fixes urgent bug."
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_011",
                "from_email": "qa.lead@company.com",
                "body": "LGTM for hotfix.",
                "created_ts": "2024-08-24T13:40:00Z"
            }),
            Action(name="read_system_config", kwargs={"config_key": "dlp_config"}),
            Action(name="dlp_scan_and_label_thread", kwargs={
                "thread_id": "thread_011",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-24T13:42:00Z"
            })
        ],
        outputs=[
            """{
              "thread_id": "thread_011",
              "blocked_terms_found": [],
              "label_applied": false
            }"""
        ]
    ),


    # --- Fixed user_221 ---
    Task(
        annotator="0",
        user_id="HARD_4",
        instruction=(
            "You are a homepage readiness coordinator ensuring artifact priority, clear guidance, and aligned communication without extraneous discovery. "
            "Focus on art_001 homepage hero and its discussion: set a priority signal, capture a guidance note, nudge the team, and validate safety. "
            "Use constants: artifact_id art_001, tag priority at 2024-08-23T16:50:00Z, author_email sarah.designer@company.com, body 'Prioritize above-the-fold tweaks.', "
            "anchor_ref node-1:2, comment_created_ts 2024-08-23T16:52:00Z, thread_id thread_001, nudge_from product.owner@company.com, "
            "nudge_created_ts 2024-08-23T16:55:00Z, nudge 'Homepage priority flagged—tracking in sprint.'"
        ),
        actions=[
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_001",
                "tag": "priority",
                "changed_ts": "2024-08-23T16:50:00Z"
            }),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_001",
                "author_email": "sarah.designer@company.com",
                "body": "Prioritize above-the-fold tweaks.",
                "anchor_ref": "node-1:2",
                "created_ts": "2024-08-23T16:52:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_001",
                "from_email": "product.owner@company.com",
                "body": "Homepage priority flagged—tracking in sprint.",
                "created_ts": "2024-08-23T16:55:00Z"
            }),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_001"})
        ],
        outputs=[
            """{
              "thread_id": "thread_001",
              "blocked_terms_found": []
            }"""
        ]
    ),


    Task(
        annotator="0",
        user_id="HARD_5",
        instruction=(
            "You are a review cycle coordinator translating Gmail intent into trackable review progress for the dashboard without relying on predefined cycle identifiers. "
            "At 2024-08-24T16:25:00Z, capture a deterministic approval intent in thread_002, mark art_007 as review-ready via a tag, verify safety posture, and surface artifact and asset context grounded in design_system_mappings and DLP policy. "
            "Use intent “Approve CTA placement.” by lisa.marketing@company.com at 2024-08-24T16:20:00Z. "
            "Constants: artifact_id art_007, thread_id thread_002, log_ts 2024-08-24T16:26:00Z, message 'Intent captured and posture verified for art_007'"
        ),
        actions=[
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_002",
                "from_email": "lisa.marketing@company.com",
                "body": "Approve CTA placement.",
                "created_ts": "2024-08-24T16:20:00Z"
            }),
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_007", "tag": "review-ready", "changed_ts": "2024-08-24T16:25:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_007"}),
            Action(name="read_system_config", kwargs={"config_key": "design_system_mappings"}),
            Action(name="read_system_config", kwargs={"config_key": "dlp_config"}),
            Action(name="get_artifact_summary", kwargs={"artifact_id": "art_007"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_002"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-24T16:26:00Z", "message": "Intent captured and posture verified for art_007"})
        ],
        outputs=[
            """[
                {
                    "asset_id": "asset_006",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                }
            ]"""
        ]
    ),

    Task(
        annotator="0",
        user_id="HARD_6",
        instruction="You coordinate pricing review intent and safety posture with Figma↔Gmail alignment, emphasizing auditability and deterministic db-modifying state changes without prescribing order. Target outcome: the cycle is linked to its conversation of record, an approval signal exists and is synced as intent, the thread is DLP-clean, and the conversation is discoverable under “Pricing.” Use constants: artifact_id art_007 at created_ts 2024-08-23T12:00:00Z; cycle_id cycle_38980610 linked to thread_id thread_008 at changed_ts 2024-08-23T12:05:00Z; approval from alex.dev@company.com with body 'APPROVED - ship it' at created_ts 2024-08-23T12:06:00Z; DLP confirmation on thread_008; keyword Pricing.",
        actions=[
            Action(name="start_review_cycle", kwargs={ 'artifact_id': 'art_007', 'created_ts': '2024-08-23T12:00:00Z' }),
            Action(name="link_review_to_thread", kwargs={ 'cycle_id': 'cycle_38980610', 'thread_id': 'thread_008', 'changed_ts': '2024-08-23T12:05:00Z' }),
            Action(name="append_message_to_thread", kwargs={ 'thread_id': 'thread_008', 'from_email': 'alex.dev@company.com', 'body': 'APPROVED - ship it', 'created_ts': '2024-08-23T12:06:00Z' }),
            Action(name="sync_gmail_intents_to_review", kwargs={ 'cycle_id': 'cycle_38980610', 'thread_id': 'thread_008' }),
            Action(name="dlp_scan_thread", kwargs={ 'thread_id': 'thread_008' }),
            Action(name="search_gmail_threads", kwargs={ 'keyword': 'Pricing' })
        ],
        outputs=[
            "[\n  {\n    \"thread_id\": \"thread_008\",\n    \"subject\": \"Pricing Page A/B Testing Results\",\n    \"current_labels\": [\n      \"pricing\",\n      \"ab-testing\",\n      \"results\"\n    ],\n    \"updated_ts\": \"2024-08-23T12:06:00Z\"\n  }\n]"
        ],
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_7",
        instruction="You serve as the release communications + brand guidance coordinator. Establish a compliant release announcement draft for release_001 in thread_006 authored by sarah.designer@company.com at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.' Maintain policy alignment by validating the draft with message_id relmsg_9cc87e81. Capture brand direction on art_003 by logging a designer note from emma.brand@company.com anchored at node-2:7 at 2024-08-23T12:00:00Z with text 'Please update the brand color token to Brand/Primary/600.'. For audit visibility, provide the author-scoped comment history on art_003 since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="list_figma_comments", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[
            """[
            {
                "comment_id": "cmt_10b86546",
                "author_email": "emma.brand@company.com",
                "anchor_ref": "node-2:7",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "created_ts": "2024-08-23T12:00:00Z"
            }
            ]"""
        ]
    ),


    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_8",
        instruction="You are the compliance steward aligning Gmail security memos with Figma design directives for an audit-ready snapshot without prescribing sequence. Scope anchors: mail thread_002 and artifact art_003. The verified record must unambiguously reflect: a memo on thread_002 authored by sarah.designer@company.com at 2024-08-23T11:00:00Z with exact body “Please note: temporary password is abcd-1234; rotate after testing.”; a DLP posture where label_if_found dlp-flag is applied to thread_002 when sensitive content is detected, effective 2024-08-23T11:05:00Z; and a brand note on art_003 anchored at node-2:7 authored by emma.brand@company.com at 2024-08-23T12:00:00Z with text “Please update the brand color token to Brand/Primary/600.” Grounding constants: thread_id thread_002, artifact_id art_003, anchor_ref node-2:7, and the timestamps above. Deliverable: the author-filtered Figma comment history for art_003 scoped to emma.brand@company.com since 2024-08-01T00:00:00Z, reflecting the persisted (db) modifications.",
        actions=[
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_002", "from_email": "sarah.designer@company.com", "body": "Please note: temporary password is abcd-1234; rotate after testing.", "created_ts": "2024-08-23T11:00:00Z"}),
            Action(name="dlp_scan_and_label_thread", kwargs={"thread_id": "thread_002", "label_if_found": "dlp-flag", "changed_ts": "2024-08-23T11:05:00Z"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="list_figma_comments", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[
            """[
            {
                "comment_id": "cmt_10b86546",
                "author_email": "emma.brand@company.com",
                "anchor_ref": "node-2:7",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "created_ts": "2024-08-23T12:00:00Z"
            }
            ]"""
        ]
    ),


    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_9",
        instruction="You own release communications readiness and QA traceability for release_001. Target state: a release announcement draft for release_001 in thread_006 from sarah.designer@company.com created at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.' validated for attachment policy using message_id relmsg_9cc87e81; thread_006 carries the label release-ready with changed_ts 2024-08-22T17:10:00Z; a QA confirmation note exists in thread_006 from qa.lead@company.com created at 2024-08-22T17:06:00Z with body 'QA sign-off complete'; and, for handoff, return the exported assets linked to artifact art_001.",
        actions=[
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_006", "add_labels": ["release-ready"], "remove_labels": [], "changed_ts": "2024-08-22T17:10:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_006", "from_email": "qa.lead@company.com", "body": "QA sign-off complete", "created_ts": "2024-08-22T17:06:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[
            """[
                {
                    "asset_id": "asset_001",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                },
                {
                    "asset_id": "asset_002",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                }
            ]"""
        ]
    ),


    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_10",
        instruction="You coordinate a cross-channel review kickoff for the homepage frame, align labels, and surface the asset snapshot for engineering. Within the homepage scope owned by sarah.designer@company.com—limited to FRAME artifacts tagged needs-review and modified on/after 2024-08-01T00:00:00Z—your target is art_001. The review kickoff must be recorded at 2024-08-24T09:30:00Z. Conversation hygiene applies to the active design-review thread that includes alex.dev@company.com and matches keyword “Design”: normalize its labels by adding triaged and figma-sync and removing urgent with change time 2024-08-24T09:40:00Z. Return the exported assets tied to art_001.",
        actions=[
            Action(name="list_artifacts", kwargs={"owner_email": "sarah.designer@company.com", "tag": "needs-review", "artifact_type": "FRAME", "modified_since": "2024-08-01T00:00:00Z"}),
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_001", "created_ts": "2024-08-24T09:30:00Z"}),
            Action(name="search_gmail_threads", kwargs={"label": "design-review", "participant": "alex.dev@company.com", "keyword": "Design"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_001", "add_labels": ["triaged", "figma-sync"], "remove_labels": ["urgent"], "changed_ts": "2024-08-24T09:40:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """{
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }"""
    ],
    ),


    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_11",
        instruction="You own the formal design review confirmation for art_004 and cross-artifact visibility. Ensure a review instance exists at 2024-08-23T13:00:00Z for art_004 and is mapped to the correct Gmail conversation via cycle_1dc59e3f → thread_003 with a linkage timestamp at 2024-08-23T13:05:00Z. Record the final decision as APPROVED by alex.dev@company.com at 2024-08-23T13:25:00Z including the comment 'Ship it'. For awareness reporting, surface the author-filtered comment timeline on art_003 for emma.brand@company.com since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="record_review_approval", kwargs={"cycle_id": "cycle_1dc59e3f", "approver_email": "alex.dev@company.com", "decision": "APPROVED", "decided_ts": "2024-08-23T13:25:00Z", "comment": "Ship it"}),
            Action(name="list_figma_comments", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[
            """[]"""
        ]
    ),


    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_12",
        instruction="You drive handoff readiness for the marketing frame while tightening data-loss posture and leaving a lightweight coordination trace. Within art_003, the artifact state reflects the handoff milestone at 2024-08-24T12:00:00Z; collaboration context is captured as a design note authored by mike.ux@company.com at 2024-08-24T12:05:00Z anchored on node-5:1 with body “Prep handoff”. The related marketing discussion is thread_002 and records a caution from sarah.designer@company.com at 2024-08-23T11:00:00Z: “Please note: temporary password is abcd-1234; rotate after testing.” DLP compliance is mandatory—when violations are detected the thread carries label dlp-flag with change time 2024-08-23T11:05:00Z. Provide the scan-and-label result.",
        actions=[
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_003", "tag": "handoff-ready", "changed_ts": "2024-08-24T12:00:00Z"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_003", "author_email": "mike.ux@company.com", "body": "Prep handoff", "anchor_ref": "node-5:1", "created_ts": "2024-08-24T12:05:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_002", "from_email": "sarah.designer@company.com", "body": "Please note: temporary password is abcd-1234; rotate after testing.", "created_ts": "2024-08-23T11:00:00Z"}),
            Action(name="dlp_scan_and_label_thread", kwargs={"thread_id": "thread_002", "label_if_found": "dlp-flag", "changed_ts": "2024-08-23T11:05:00Z"}),
        ],
        outputs=[
            """{
    "thread_id": "thread_002",
    "blocked_terms_found": [
    "password"
    ],
    "label_applied": true
    }"""
    ],
    ),


    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_13",
        instruction="You finalize a release announcement grounded in the release/ lineage and ensure the conversation reflects a positive release signal. Treat release_001 as the authoritative diff source for this announcement. The announcement exists as a draft in thread_006 from sarah.designer@company.com at 2024-08-22T17:00:00Z with subject “Release 1.2.0 Announcement” and body “Highlights and changes included.” The draft message relmsg_9cc87e81 complies with attachment policy, and the thread carries Design/Release and sentiment/positive with change time 2024-08-22T17:05:00Z. Return the exported assets tied to art_001.",
        actions=[
            Action(name="list_releases", kwargs={"version_prefix": "release/"}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "sentiment/positive"], "remove_labels": [], "changed_ts": "2024-08-22T17:05:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """{
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }"""
    ],
    ),


    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_14",
        instruction="You are the integrated design-system/accessibility audit coordinator producing a clear preparation footprint. Use design_system_mappings as the starting frame, and constrain the scope to FILE artifacts owned by lisa.marketing@company.com tagged website and modified on/after 2024-08-01T00:00:00Z. The target art_006 is documented with an audit of type COMBINED_DS_A11Y at 2024-08-24T13:00:00Z, a preparation log 'Prepared audit for art_006' at 2024-08-24T13:05:00Z, and a working tag audit-in-progress effective 2024-08-24T13:06:00Z. Return the canonical artifact summary for art_006 to anchor this record.",
        actions=[
            Action(name="read_system_config", kwargs={"config_key": "design_system_mappings"}),
            Action(name="list_artifacts", kwargs={"owner_email": "lisa.marketing@company.com", "tag": "website", "artifact_type": "FILE", "modified_since": "2024-08-01T00:00:00Z"}),
            Action(name="create_audit_session", kwargs={"artifact_id": "art_006", "created_ts": "2024-08-24T13:00:00Z", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-24T13:05:00Z", "message": "Prepared audit for art_006"}),
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_006", "tag": "audit-in-progress", "changed_ts": "2024-08-24T13:06:00Z"}),
            Action(name="get_artifact_summary", kwargs={"artifact_id": "art_006"}),
        ],
        outputs=[
            """{
            "artifact_id": "art_006",
            "artifact_name": "Marketing Website",
            "artifact_type": "FILE",
            "owner_email": "lisa.marketing@company.com",
            "deep_link": "https://www.figma.com/file/def456ghi789/Marketing-Website",
            "current_tags": [
            "marketing",
            "website",
            "landing-pages"
            ],
            "modified_ts": "2024-08-24T13:06:00Z"
            }"""
    ],
    ),

    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="HARD_15",
        instruction=(
            "You translate Gmail intent into quantified review sentiment for the dashboard review without prescribing sequence. "
            "Operate on art_004 with cycle_id cycle_1dc59e3f linked to thread_003. "
            "Record two deterministic intents for parsing: "
            "'Looks good—LGTM from marketing.' from lisa.marketing@company.com at 2024-08-23T13:10:00Z and "
            "'Please REVISE the grid spacing to 8px multiples.' from alex.dev@company.com at 2024-08-23T13:15:00Z. "
            "Grounding constants: artifact_id art_004, cycle_id cycle_1dc59e3f, thread_id thread_003, "
            "created_ts 2024-08-23T13:00:00Z and 2024-08-23T13:05:00Z for cycle/link, and the two message timestamps above. "
            "Return the synced intent counts."
        ),
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_003", "from_email": "lisa.marketing@company.com", "body": "Looks good—LGTM from marketing.", "created_ts": "2024-08-23T13:10:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_003", "from_email": "alex.dev@company.com", "body": "Please REVISE the grid spacing to 8px multiples.", "created_ts": "2024-08-23T13:15:00Z"}),
            Action(name="sync_gmail_intents_to_review", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003"})
        ],
        outputs=[
            """{
            "cycle_id": "cycle_1dc59e3f",
            "thread_id": "thread_003",
            "intent_counts": {
                "approve": 1,
                "changes": 1,
                "blocker": 0
            }
            }"""
        ]
    ),

    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="HARD_16",
        instruction=(
            "You coordinate brand-aligned release communications and prove audit-ready traceability without prescribing a tool order. "
            "Compose a concise draft then validate attachment policy, and capture a durable FIGMA brand note with author-scoped history. "
            "Constants: release_id release_001, thread_id thread_006, from_email sarah.designer@company.com, created_ts 2024-08-22T17:00:00Z, "
            "subject 'Release 1.2.0 Announcement', body 'Highlights and changes included.', message_id relmsg_9cc87e81; "
            "artifact_id art_003, author_email emma.brand@company.com, anchor_ref node-2:7, comment_created_ts 2024-08-23T12:00:00Z, since_ts 2024-08-01T00:00:00Z."
        ),
        actions=[
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_006",
                "from_email": "sarah.designer@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_003",
                "author_email": "emma.brand@company.com",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "anchor_ref": "node-2:7",
                "created_ts": "2024-08-23T12:00:00Z"
            }),
            Action(name="list_figma_comments", kwargs={
                "artifact_id": "art_003",
                "author_email": "emma.brand@company.com",
                "since_ts": "2024-08-01T00:00:00Z"
            })
        ],
        outputs=[
            """[
            {
                "comment_id": "cmt_10b86546",
                "author_email": "emma.brand@company.com",
                "anchor_ref": "node-2:7",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "created_ts": "2024-08-23T12:00:00Z"
            }
            ]"""
        ]
    ),

    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="HARD_17",
        instruction="You are a homepage review coordination specialist responsible for audit-grade traceability and policy-aligned status visibility across Figma and Gmail. Work centers on artifact art_001 owned by sarah.designer@company.com within the needs-review FRAME scope modified since 2024-08-01T00:00:00Z. The verified posture must reflect a review cycle created at 2024-08-24T09:30:00Z; Gmail evidence under label design-review involving alex.dev@company.com matching keyword “Design”; and a label state for thread_001 with triaged and figma-sync present and urgent absent effective 2024-08-24T09:40:00Z. The coordination outcome is a concise, stakeholder-ready asset list for art_001 with timestamped traceability. Constants: owner_email sarah.designer@company.com, tag needs-review, artifact_type FRAME, modified_since 2024-08-01T00:00:00Z, artifact_id art_001, review_created 2024-08-24T09:30:00Z, gmail_label design-review, participant alex.dev@company.com, keyword Design, thread_id thread_001, add_labels [triaged, figma-sync], remove_labels [urgent], changed_ts 2024-08-24T09:40:00Z.",
        actions=[
            Action(name="list_artifacts", kwargs={"owner_email": "sarah.designer@company.com", "tag": "needs-review", "artifact_type": "FRAME", "modified_since": "2024-08-01T00:00:00Z"}),
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_001", "created_ts": "2024-08-24T09:30:00Z"}),
            Action(name="search_gmail_threads", kwargs={"label": "design-review", "participant": "alex.dev@company.com", "keyword": "Design"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_001", "add_labels": ["triaged", "figma-sync"], "remove_labels": ["urgent"], "changed_ts": "2024-08-24T09:40:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[
            """[
                {
                    "asset_id": "asset_001",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                },
                {
                    "asset_id": "asset_002",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                }
            ]"""
        ]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_18",
        instruction="You consolidate Gmail feedback signals and Figma release posture into a single audit-ready snapshot without prescribing sequence. Scope anchors: artifact context art_002 and mail context thread_006. Record two deterministic notes for parsing — “Approve pricing grid.” from pm.lead@company.com at 2024-08-24T18:05:00Z and “Revise discount footnote.” from qa.lead@company.com at 2024-08-24T18:10:00Z; assert safety via a single DLP evaluation on thread_006; and reflect release state by applying tag approved-for-release to art_002 effective 2024-08-24T18:16:00Z (db mutation). Deliverable: the exported asset list for art_002. Grounding constants: artifact_id art_002, thread_id thread_006, and the exact timestamps above.",
        actions=[
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_006",
                "from_email": "pm.lead@company.com",
                "body": "Approve pricing grid.",
                "created_ts": "2024-08-24T18:05:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_006",
                "from_email": "qa.lead@company.com",
                "body": "Revise discount footnote.",
                "created_ts": "2024-08-24T18:10:00Z"
            }),
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_002", "tag": "approved-for-release", "changed_ts": "2024-08-24T18:16:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_002"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_006"})
        ],
        outputs=[
            """[
                {
                    "asset_id": "asset_003",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                }
            ]"""
        ]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_19",
        instruction="You are the landing-page kickoff and triage steward responsible for an audit-ready coordination snapshot. Scope anchors: owner sarah.designer@company.com, artifact type FRAME, tag landing-page, modified on/after 2024-08-01T00:00:00Z; artifact context art_001 and mail context thread_001. The verified record must unambiguously reflect a kickoff note authored by sarah.designer@company.com at 2024-08-25T09:00:00Z with exact text 'Handoff kickoff for landing page.'; a label stance on thread_001 where triaged and handoff are present and dlp-flag is absent effective 2024-08-25T09:05:00Z; and the deliverable is the exported asset list tied to art_001.",
        actions=[
            Action(name="list_artifacts", kwargs={
            "owner_email": "sarah.designer@company.com",
            "tag": "landing-page",
            "artifact_type": "FRAME",
            "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
            "thread_id": "thread_001",
            "from_email": "sarah.designer@company.com",
            "body": "Handoff kickoff for landing page.",
            "created_ts": "2024-08-25T09:00:00Z"
            }),
            Action(name="update_thread_labels", kwargs={
            "thread_id": "thread_001",
            "add_labels": ["triaged", "handoff"],
            "remove_labels": ["dlp-flag"],
            "changed_ts": "2024-08-25T09:05:00Z"
            }),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """{
            "asset_id": "asset_001",
            "profile": null,
            "file_name": null,
            "mime_type": null
            },
            {
            "asset_id": "asset_002",
            "profile": null,
            "file_name": null,
            "mime_type": null
            }"""
        ],
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_20",
        instruction="You are the pricing page handoff coordinator ensuring a durable designer note and an explicit readiness posture. Scope: owner lisa.marketing@company.com, tag needs-review, artifact type FRAME, modified on/after 2024-08-01T00:00:00Z; target art_007. The audit-ready state documents a canonical design note on art_007 anchored node-7:2 by lisa.marketing@company.com at 2024-08-25T10:40:00Z with exact body 'Mark CTA “Sign up”.' and shows art_007 carrying tag handoff-ready effective 2024-08-25T10:45:00Z. The deliverable is the exported asset snapshot for art_007.",
        actions=[
            Action(name="list_artifacts", kwargs={
                "owner_email": "lisa.marketing@company.com",
                "tag": "needs-review",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_007",
                "author_email": "lisa.marketing@company.com",
                "body": "Mark CTA “Sign up”.",
                "anchor_ref": "node-7:2",
                "created_ts": "2024-08-25T10:40:00Z"
            }),
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_007",
                "tag": "handoff-ready",
                "changed_ts": "2024-08-25T10:45:00Z"
            }),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_007"}),
        ],
        outputs=[
            """[
            {
            "asset_id": "asset_006",
            "profile": null,
            "file_name": null,
            "mime_type": null
            }
            ]"""
            ],
        ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_21",
        instruction="You are the review-sentiment normalization lead aligning lifecycle signals with conversation intent. Lifecycle anchor: cycle_003 for the pricing/table discussion linked to thread_003 at 2024-08-25T10:05:00Z. The authoritative conversation record shows two discrete notes that must be uploaded to db — lisa.marketing@company.com 'Looks good—LGTM from marketing.' at 2024-08-25T10:10:00Z and alex.dev@company.com 'Please REVISE the grid spacing to 8px multiples.' at 2024-08-25T10:15:00Z — and the cycle reflects synchronized mail intents from thread_003. Provide the intent count roll-up for the cycle_003 ↔ thread_003 pair.",
        actions=[
            Action(name="link_review_to_thread", kwargs={
            "cycle_id": "cycle_003",
            "thread_id": "thread_003",
            "changed_ts": "2024-08-25T10:05:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
            "thread_id": "thread_003",
            "from_email": "lisa.marketing@company.com",
            "body": "Looks good—LGTM from marketing.",
            "created_ts": "2024-08-25T10:10:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
            "thread_id": "thread_003",
            "from_email": "alex.dev@company.com",
            "body": "Please REVISE the grid spacing to 8px multiples.",
            "created_ts": "2024-08-25T10:15:00Z"
            }),
            Action(name="sync_gmail_intents_to_review", kwargs={
            "cycle_id": "cycle_003",
            "thread_id": "thread_003"
            }),
        ],
        outputs=[
        """{
        "cycle_id": "cycle_003",
        "thread_id": "thread_003",
        "intent_counts": {
        "approve": 1,
        "changes": 1,
        "blocker": 0
        }
        }"""
        ],
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_22",
        instruction="You are the admin-navigation coordination lead responsible for durable design notes, synced mail visibility, and a stable reference snapshot. The authoritative record should present: a canonical design observation on art_011 by design.lead@company.com at 2024-08-25T12:30:00Z anchored at node-11:4 with text 'Tighten header spacing to 8px rhythm.'; thread_013 showing a sync touchpoint from design.lead@company.com at 2024-08-25T12:32:00Z with 'Design note logged on art_011.'; a label stance on thread_013 where figma-sync is present effective 2024-08-25T12:33:00Z; and, for downstream consumers, the exported assets for art_001 as the stable reference.",
        actions=[
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_011",
                "author_email": "design.lead@company.com",
                "body": "Tighten header spacing to 8px rhythm.",
                "anchor_ref": "node-11:4",
                "created_ts": "2024-08-25T12:30:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_013",
                "from_email": "design.lead@company.com",
                "body": "Design note logged on art_011.",
                "created_ts": "2024-08-25T12:32:00Z"
            }),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_013",
                "add_labels": ["figma-sync"],
                "remove_labels": [],
                "changed_ts": "2024-08-25T12:33:00Z"
            }),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """{
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }"""
    ],
    ),

    # complexity_edges: 12
    Task(
        annotator="0",
        user_id="HARD_23",
        instruction="You are the pricing audit kickoff coordinator accountable for governance alignment, stakeholder visibility, and a traceable audit snapshot. Treat fix_workflow_config and intent_keywords as the authoritative governance context. The finalized kickoff snapshot should evidence a COMBINED_DS_A11Y kickoff on art_003 (created 2024-08-25T09:00:00Z), a program checkpoint note 'Fix planning kickoff' at 2024-08-25T09:02:00Z, stakeholder visibility on thread_006 from emma.brand@company.com at 2024-08-25T09:03:00Z with 'Kickoff: reviewing audit_c924d63d and preparing plan.', and a mail posture where planning is present as of 2024-08-25T09:04:00Z. Output the summarized counts for audit_c924d63d.",
        actions=[
            Action(name="read_system_config", kwargs={"config_key": "fix_workflow_config"}),
            Action(name="read_system_config", kwargs={"config_key": "intent_keywords"}),
            Action(name="create_audit_session", kwargs={
                "artifact_id": "art_003",
                "created_ts": "2024-08-25T09:00:00Z",
                "audit_type": "COMBINED_DS_A11Y"
            }),
            Action(name="log_terminal_event", kwargs={
                "log_ts": "2024-08-25T09:02:00Z",
                "message": "Fix planning kickoff"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_006",
                "from_email": "emma.brand@company.com",
                "body": "Kickoff: reviewing audit_c924d63d and preparing plan.",
                "created_ts": "2024-08-25T09:03:00Z"
            }),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_006",
                "add_labels": ["planning"],
                "remove_labels": [],
                "changed_ts": "2024-08-25T09:04:00Z"
            }),
            Action(name="summarize_audit", kwargs={"audit_id": "audit_c924d63d"}),
        ],
        outputs=[
            """{"audit_id": "audit_c924d63d",
        "ds_findings": 0,
        "a11y_findings": 0
        }"""
        ],
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_24",
        instruction="You are the thread-hygiene and sync-state steward for the Navigation discussion, producing an audit-ready snapshot without prescribing sequence. Scope anchors: Gmail label responsive, participant alex.dev@company.com, keyword Navigation; thread context thread_010. Vocabulary authority: the canonical label set named gmail_labels from system configuration—normalize/validate any label writes against it (db modification). Compliance target effective 2024-08-25T10:00:00Z: on thread_010 the stance is triaged and figma-sync present and responsive absent; plus a concise status ping authored by sarah.designer@company.com at 2024-08-25T10:02:00Z with exact text 'Design synced to Figma.'; and a single DLP safety confirmation reporting no blocked terms. Preserve all identifiers and literals exactly as provided and return the verified state.",
        actions=[
            Action(name="search_gmail_threads", kwargs={"label": "responsive", "participant": "alex.dev@company.com", "keyword": "Navigation"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_010", "add_labels": ["triaged", "figma-sync"], "remove_labels": ["responsive"], "changed_ts": "2024-08-25T10:00:00Z"}),
            Action(name="read_system_config", kwargs={"config_key": "gmail_labels"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_010", "from_email": "sarah.designer@company.com", "body": "Design synced to Figma.", "created_ts": "2024-08-25T10:02:00Z"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_010"})
        ],
        outputs=[
            """{
    "thread_id": "thread_010",
    "blocked_terms_found": []
    }"""
    ]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_25",
        instruction="You maintain an audit-ready governance snapshot for the Pricing Page across Figma/Gmail context without prescribing order. Scope anchors: FRAME artifacts owned by lisa.marketing@company.com tagged pricing and modified on/after 2024-08-01T00:00:00Z; focal artifact art_007. The verified record must unambiguously show: the latest COMPLETED audits for art_007 with audit_005 summarized; art_007 tagged audit-pending effective 2024-08-25T12:01:00Z; a COMBINED_DS_A11Y session created at 2024-08-25T12:00:00Z; audit_workflow_config as the authoritative scope; and inclusion of the exported asset list for art_007. Return the consolidated evidence bundle.",
        actions=[
            Action(name="list_artifacts", kwargs={
                "owner_email": "lisa.marketing@company.com",
                "tag": "pricing",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="list_audits", kwargs={
                "artifact_id": "art_007",
                "status": "COMPLETED"
            }),
            Action(name="summarize_audit", kwargs={
                "audit_id": "audit_005"
            }),
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_007",
                "tag": "audit-pending",
                "changed_ts": "2024-08-25T12:01:00Z"
            }),
            Action(name="create_audit_session", kwargs={
                "artifact_id": "art_007",
                "created_ts": "2024-08-25T12:00:00Z",
                "audit_type": "COMBINED_DS_A11Y"
            }),
            Action(name="read_system_config", kwargs={
                "config_key": "audit_workflow_config"
            }),
            Action(name="list_assets_for_artifact", kwargs={
                "artifact_id": "art_007"
            })
        ],
        outputs=[
            """[
    {
    "asset_id": "asset_006",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ]
    ),


    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_26",
        instruction="You prepare a concise public note for the marketing website launch and verify communications guardrails under the release governance. Treat the release/ catalog (with artifact_id None) as authoritative and quantify release_003 via its deterministic message context. The audit-ready thread_003 record should demonstrate: an announcement draft by lisa.marketing@company.com at 2024-08-25T13:45:00Z with subject 'Release 1.0.0 Announcement' and body 'Launching marketing website.' validated under message_id relmsg_ddbea77f; label vocabulary aligned to gmail_labels with release-draft present as of 2024-08-25T13:50:00Z; and a DLP safety confirmation showing the thread is clean.",
        actions=[
            Action(name="list_releases", kwargs={
                "version_prefix": "release/",
                "artifact_id": None
            }),
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_003",
                "thread_id": "thread_003",
                "from_email": "lisa.marketing@company.com",
                "created_ts": "2024-08-25T13:45:00Z",
                "subject": "Release 1.0.0 Announcement",
                "body": "Launching marketing website."
            }),
            Action(name="guard_attachment_policy_on_draft", kwargs={
                "message_id": "relmsg_ddbea77f"
            }),
            Action(name="read_system_config", kwargs={
                "config_key": "gmail_labels"
            }),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_003",
                "add_labels": ["release-draft"],
                "remove_labels": [],
                "changed_ts": "2024-08-25T13:50:00Z"
            }),
            Action(name="dlp_scan_thread", kwargs={
                "thread_id": "thread_003"
            })
        ],
        outputs=[
            """{
    "thread_id": "thread_003",
    "blocked_terms_found": []
    }"""
    ]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_27",
        instruction="You finalize landing-page campaign readiness using a goal-based policy—no fixed sequence—that synchronizes Figma brand guidance with Gmail implementation evidence and performs one deterministic DLP evaluation. Use constants: artifact_id art_006; tag handoff-ready with changed_ts 2024-08-24T14:00:00Z; Figma comment by emma.brand@company.com anchored node-6:45 at 2024-08-24T14:02:00Z body 'Use latest brand tokens.'; Gmail thread thread_010 message from alex.dev@company.com at 2024-08-24T14:05:00Z body 'Updated hero copy applied.'; DLP label_if_found dlp-flag with changed_ts 2024-08-24T14:12:00Z. Return the DLP outcome deterministically.",
        actions=[
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_006",
                "tag": "handoff-ready",
                "changed_ts": "2024-08-24T14:00:00Z"
            }),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_006",
                "author_email": "emma.brand@company.com",
                "body": "Use latest brand tokens.",
                "anchor_ref": "node-6:45",
                "created_ts": "2024-08-24T14:02:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_010",
                "from_email": "alex.dev@company.com",
                "body": "Updated hero copy applied.",
                "created_ts": "2024-08-24T14:05:00Z"
            }),
            Action(name="dlp_scan_and_label_thread", kwargs={
                "thread_id": "thread_010",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-24T14:12:00Z"
            })
        ],
        outputs=[
            """{
    "thread_id": "thread_010",
    "blocked_terms_found": [],
    "label_applied": false
    }"""
    ],
    ),


    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_28",
        instruction="You own the hero handoff within the Figma↔Gmail design-to-build pipeline. Within FRAME artifacts modified on/after 2024-08-01T00:00:00Z and tagged landing-page (email sarah.designer@company.com), the homepage frame's authoritative identity is art_001. The finalized record should demonstrate: art_001 carrying status handoff-ready effective 2024-08-25T09:00:00Z; a coordination note by mike.ux@company.com anchored node-1:3 at 2024-08-25T09:05:00Z with body 'Ready for implementation; confirm responsive behavior.'; and the exported assets listing for art_001 as the stable reference snapshot.",
        actions=[
        Action(name="list_artifacts", kwargs={
        "owner_email": "sarah.designer@company.com",
        "tag": "landing-page",
        "artifact_type": "FRAME",
        "modified_since": "2024-08-01T00:00:00Z"
        }),
        Action(name="add_artifact_tag", kwargs={
        "artifact_id": "art_001",
        "tag": "handoff-ready",
        "changed_ts": "2024-08-25T09:00:00Z"
        }),
        Action(name="create_figma_comment", kwargs={
        "artifact_id": "art_001",
        "author_email": "mike.ux@company.com",
        "body": "Ready for implementation; confirm responsive behavior.",
        "anchor_ref": "node-1:3",
        "created_ts": "2024-08-25T09:05:00Z"
        }),
        Action(name="list_assets_for_artifact", kwargs={
        "artifact_id": "art_001"
        })
        ],
        outputs=[
        """[
        {
        "asset_id": "asset_001",
        "profile": null,
        "file_name": null,
        "mime_type": null
        },
        {
        "asset_id": "asset_002",
        "profile": null,
        "file_name": null,
        "mime_type": null
        }
        ]"""
        ]
    ),

    # complexity_edges:  15
    Task(
        annotator="0",
        user_id="HARD_29",
        instruction="You convert Gmail thread sentiment into review intents for a Figma FRAME artifact without prescribing call order. Scope anchors: search within FRAME artifacts owned by mike.ux@company.com tagged revise and modified_since 2024-08-01T00:00:00Z; artifact context art_012; review cycle cycle_19bc41cf; mail thread thread_012. Grounding constants: review created_ts 2024-08-25T11:00:00Z, link changed_ts 2024-08-25T11:02:00Z, and a deterministic approval from mike.ux@company.com at 2024-08-25T11:05:00Z with exact body 'Looks good — LGTM to proceed.'. Deliverable: persist a synced intent summary for {cycle_id: cycle_19bc41cf, thread_id: thread_012} whose counts reflect the full thread history including this approval.",
        actions=[
            Action(name="list_artifacts", kwargs={
                "owner_email": "mike.ux@company.com",
                "tag": "revise",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="start_review_cycle", kwargs={
                "artifact_id": "art_012",
                "created_ts": "2024-08-25T11:00:00Z"
            }),
            Action(name="link_review_to_thread", kwargs={
                "cycle_id": "cycle_19bc41cf",
                "thread_id": "thread_012",
                "changed_ts": "2024-08-25T11:02:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_012",
                "from_email": "mike.ux@company.com",
                "body": "Looks good — LGTM to proceed.",
                "created_ts": "2024-08-25T11:05:00Z"
            }),
            Action(name="sync_gmail_intents_to_review", kwargs={
                "cycle_id": "cycle_19bc41cf",
                "thread_id": "thread_012"
            })
        ],
        outputs=[
            """{
    "cycle_id": "cycle_19bc41cf",
    "thread_id": "thread_012",
    "intent_counts": {
    "approve": 1,
    "changes": 0,
    "blocker": 0
    }
    }"""
    ]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_30",
        instruction="You prepare a concise mobile release summary while keeping thread hygiene aligned to policy. Treat the release/ lineage as authoritative, with quantified differences for release_002. The audit-ready record for thread_007 should demonstrate: a deterministic summary draft authored by sarah.designer@company.com at 2024-08-24T11:00:00Z with subject 'Release 1.3.0 Summary' and body 'Key highlights prepared.'; a label stance where Design/Release and announced are present as of 2024-08-24T11:05:00Z; and a DLP safety confirmation on the same thread. Provide the release_002 diff summary as part of the evidence.",
        actions=[
            Action(name="list_releases", kwargs={"version_prefix": "release/"}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_002"}),
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_002",
                "thread_id": "thread_007",
                "from_email": "sarah.designer@company.com",
                "created_ts": "2024-08-24T11:00:00Z",
                "subject": "Release 1.3.0 Summary",
                "body": "Key highlights prepared."
            }),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_007",
                "add_labels": ["Design/Release", "announced"],
                "remove_labels": [],
                "changed_ts": "2024-08-24T11:05:00Z"
            }),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_007"})
        ],
        outputs=[
            """{
    "release_id": "release_002",
    "added": 0,
    "updated": 0,
    "removed": 0
    }"""
    ],
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_31",
        instruction="You orchestrate a combined DS+A11Y audit kickoff for the Homepage Hero Section with evidence preserved and tool-agnostic policy. Scope: Figma FRAME artifacts owned by sarah.designer@company.com, tag hero, modified since 2024-08-01T00:00:00Z. Grounding constants: artifact_id art_001, audit_id audit_001, tag audit-pending with changed_ts 2024-08-25T18:35:00Z, audit_type COMBINED_DS_A11Y with created_ts 2024-08-25T18:36:00Z, config_key audit_workflow_config. Include the existing exported assets overview for provenance and keep Gmail traceability in mind (no sending required). Policy: identify the latest COMPLETED audit for that artifact and summarize it; ensure pending state and session readiness are reflected in the database without prescribing order. Return only the summarized audit counts.",
        actions=[
            Action(name="list_artifacts", kwargs={
                "owner_email": "sarah.designer@company.com",
                "tag": "hero",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="list_audits", kwargs={
                "artifact_id": "art_001",
                "status": "COMPLETED"
            }),
            Action(name="summarize_audit", kwargs={
                "audit_id": "audit_001"
            }),
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_001",
                "tag": "audit-pending",
                "changed_ts": "2024-08-25T18:35:00Z"
            }),
            Action(name="create_audit_session", kwargs={
                "artifact_id": "art_001",
                "created_ts": "2024-08-25T18:36:00Z",
                "audit_type": "COMBINED_DS_A11Y"
            }),
            Action(name="read_system_config", kwargs={
                "config_key": "audit_workflow_config"
            }),
            Action(name="list_assets_for_artifact", kwargs={
                "artifact_id": "art_001"
            })
        ],
        outputs=[
            """{
            "audit_id": "audit_001",
            "ds_findings": 0,
            "a11y_findings": 2
            }"""
            ]
        ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_32",
        instruction="You translate brand guidance into provenance and review context without prescribing sequence. Use constants: artifact_id art_003, thread_id thread_003; Gmail note from design.system@company.com at 2024-08-23T12:10:00Z body 'Brand tokens aligned with DS v3.'; review annotation on Figma anchored at node-2:7 by emma.brand@company.com at 2024-08-23T12:00:00Z text 'Please update the brand color token to Brand/Primary/600.'. Include a DLP safety check on the Gmail thread. Return the author-scoped comment history for art_003 filtered to author_email emma.brand@company.com since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_003",
                "from_email": "design.system@company.com",
                "body": "Brand tokens aligned with DS v3.",
                "created_ts": "2024-08-23T12:10:00Z"
            }),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_003"}),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_003",
                "author_email": "emma.brand@company.com",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "anchor_ref": "node-2:7",
                "created_ts": "2024-08-23T12:00:00Z"
            }),
            Action(name="list_figma_comments", kwargs={
                "artifact_id": "art_003",
                "author_email": "emma.brand@company.com",
                "since_ts": "2024-08-01T00:00:00Z"
            })
        ],
        outputs=[
            "[\n  {\n    \"comment_id\": \"cmt_10b86546\",\n    \"author_email\": \"emma.brand@company.com\",\n    \"anchor_ref\": \"node-2:7\",\n    \"body\": \"Please update the brand color token to Brand/Primary/600.\",\n    \"created_ts\": \"2024-08-23T12:00:00Z\"\n  }\n]"
        ],
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_33",
        instruction="You are a Figma↔Gmail workflow steward closing out a pricing review in a governed, audit-ready posture. Within FRAME artifacts tagged pricing and owned by lisa.marketing@company.com (modified since 2024-08-01T00:00:00Z), the homepage pricing frame's authoritative identity is art_007. The canonical snapshot must evidence: the stale status removal with needs-review no longer present effective 2024-08-25T18:40:00Z; a provenance note on the artifact by pm.lead@company.com anchored node-3:3 at 2024-08-25T18:41:00Z with the exact body 'Removed 'needs-review' after approval; proceeding to implementation.'; and the final artifact summary for art_007 as the stable reference for downstream discoverability in the MCP pipeline.",
        actions=[
            Action(name="list_artifacts", kwargs={
                "owner_email": "lisa.marketing@company.com",
                "tag": "pricing",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="remove_artifact_tag", kwargs={
                "artifact_id": "art_007",
                "tag": "needs-review",
                "changed_ts": "2024-08-25T18:40:00Z"
            }),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_007",
                "author_email": "pm.lead@company.com",
                "body": "Removed 'needs-review' after approval; proceeding to implementation.",
                "anchor_ref": "node-3:3",
                "created_ts": "2024-08-25T18:41:00Z"
            }),
            Action(name="get_artifact_summary", kwargs={
                "artifact_id": "art_007"
            })
        ],
        outputs=[
            """{
            "artifact_id": "art_007",
            "artifact_name": "Pricing Page",
            "artifact_type": "FRAME",
            "owner_email": "lisa.marketing@company.com",
            "deep_link": "https://www.figma.com/file/def456ghi789/Marketing-Website?node-id=3%3A3",
            "current_tags": [
            "pricing",
            "conversion",
            "cta"
            ],
            "modified_ts": "2024-08-25T18:40:00Z"
            }"""
            ]
        ),

    # complexity_edges:  14
    Task(
        annotator="0",
        user_id="HARD_34",
        instruction="You are the release-comms safety coordinator operating across Gmail and the release catalog to maintain policy-clean discoverability. The audit-ready record must show: source mail thread_003 containing a sensitive note from lisa.marketing@company.com at 2024-08-23T09:00:00Z with body 'Temporary password is abcd-1234. Rotate after testing.' and a single safety evaluation that applies dlp-flag at 2024-08-23T09:05:00Z; plus a deterministic 1.4.0 announcement draft for release_004 in thread_008 by sarah.designer@company.com at 2024-08-23T16:30:00Z with subject 'Release 1.4.0 Announcement' and body 'Changelog and new components included.' The deliverable is the set of threads discoverable under label dlp-flag, consistent with the Release Notes & Asset Handoff workflow.",
        actions=[
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_003",
                "from_email": "lisa.marketing@company.com",
                "body": "Temporary password is abcd-1234. Rotate after testing.",
                "created_ts": "2024-08-23T09:00:00Z"
            }),
            Action(name="dlp_scan_and_label_thread", kwargs={
                "thread_id": "thread_003",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-23T09:05:00Z"
            }),
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_004",
                "thread_id": "thread_008",
                "from_email": "sarah.designer@company.com",
                "created_ts": "2024-08-23T16:30:00Z",
                "subject": "Release 1.4.0 Announcement",
                "body": "Changelog and new components included."
            }),
            Action(name="search_gmail_threads", kwargs={"label": "dlp-flag"})
        ],
        outputs=[
            "[\n  {\n    \"thread_id\": \"thread_003\",\n    \"subject\": \"Marketing Website Launch Approval\",\n    \"current_labels\": [\n      \"marketing\",\n      \"approval\",\n      \"launch\",\n      \"dlp-flag\"\n    ],\n    \"updated_ts\": \"2024-08-23T09:05:00Z\"\n  }\n]"
        ],
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_35",
        instruction="You are finalizing a release-ready conversation with asset lineage preserved for downstream handoff. The authoritative snapshot must reflect: the maintained release_001 draft in thread_006 authored by sarah.designer@company.com at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.'; a QA memo from qa.lead@company.com at 2024-08-22T17:06:00Z with body 'QA sign-off complete'; a conversation posture where release-ready is present effective 2024-08-22T17:10:00Z; and the exported assets listing for artifact_id art_001 as the stable asset reference aligned to the Figma↔Gmail release workflow.",
        actions=[
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_006",
                "from_email": "sarah.designer@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_006",
                "from_email": "qa.lead@company.com",
                "body": "QA sign-off complete",
                "created_ts": "2024-08-22T17:06:00Z"
            }),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_006",
                "add_labels": ["release-ready"],
                "remove_labels": [],
                "changed_ts": "2024-08-22T17:10:00Z"
            }),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[
            "[\n  {\n    \"asset_id\": \"asset_001\",\n    \"profile\": null,\n    \"file_name\": null,\n    \"mime_type\": null\n  },\n  {\n    \"asset_id\": \"asset_002\",\n    \"profile\": null,\n    \"file_name\": null,\n    \"mime_type\": null\n  }\n]"
        ],
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_36",
        instruction="You translate Gmail pricing feedback into governed review progress with one safety evaluation and searchable evidence—without prescribing sequence. Apply the Email-Centric Design Review policy (Figma↔Gmail). Grounding constants: artifact_id art_007, cycle_id cycle_38980610, thread_id thread_008; created_ts 2024-08-23T12:00:00Z and changed_ts 2024-08-23T12:05:00Z; and one deterministic intent “APPROVED - ship it” from alex.dev@company.com at 2024-08-23T12:06:00Z. Return an audit-ready snapshot where review intents for cycle_38980610/thread_008 are reflected, a single safety evaluation is recorded, and evidence is discoverable by the keyword “Pricing”.",
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_007", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={
                "cycle_id": "cycle_38980610",
                "thread_id": "thread_008",
                "changed_ts": "2024-08-23T12:05:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_008",
                "from_email": "alex.dev@company.com",
                "body": "APPROVED - ship it",
                "created_ts": "2024-08-23T12:06:00Z"
            }),
            Action(name="sync_gmail_intents_to_review", kwargs={
                "cycle_id": "cycle_38980610",
                "thread_id": "thread_008"
            }),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_008"}),
            Action(name="search_gmail_threads", kwargs={"keyword": "Pricing"})
        ],
        outputs=[
            "[\n  {\n    \"thread_id\": \"thread_008\",\n    \"subject\": \"Pricing Page A/B Testing Results\",\n    \"current_labels\": [\n      \"pricing\",\n      \"ab-testing\",\n      \"results\"\n    ],\n    \"updated_ts\": \"2024-08-23T12:06:00Z\"\n  }\n]"
        ],
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_37",
        instruction="You are the Figma↔Gmail release communications steward preserving lineage, attachment guardrails, and downstream discoverability. The audit-ready record must evidence: releases discoverable under prefix release/ with the authoritative diff for release_001; a deterministic announcement draft in Google thread_006 by sarah.designer@company.com at 2024-08-22T17:00:00Z with subject “Release 1.2.0 Announcement” and body “Highlights and changes included.”; attachment guardrails recorded under message_id relmsg_9cc87e81; a conversation posture where Design/Release and announced are present effective 2024-08-22T17:06:30Z; and the diff summary for release_001 retained as the stable reference for stakeholders in the Release Notes workflow.",
        actions=[
            Action(name="list_releases", kwargs={"version_prefix": "release/"}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_006",
                "from_email": "sarah.designer@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_006",
                "add_labels": ["Design/Release", "announced"],
                "remove_labels": [],
                "changed_ts": "2024-08-22T17:06:30Z"
            }),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"})
        ],
        outputs=[
            """{
    "release_id": "release_001",
    "added": 0,
    "updated": 0,
    "removed": 0
    }"""
    ],
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_38",
        instruction="You are the Figma↔Gmail review orchestration lead for the pricing module, responsible for governed progress, safety posture, and searchable traceability within the Email-Centric Design Review & Approval workflow. Produce an audit-ready snapshot that records—as immutable facts (a record, not a procedure)—the following: a review for Figma artifact art_007 with creation time 2024-08-23T12:00:00Z recorded under cycle_38980610; association to the source conversation thread_008 effective 2024-08-23T12:05:00Z; a deterministic approval signal in that Google conversation from alex.dev@company.com at 2024-08-23T12:06:00Z with the exact text “APPROVED - ship it”; synchronized intent tallies on the same review cycle; and a safety confirmation for thread_008. For downstream discoverability, also include the set of threads discoverable by keyword “Pricing.” Honor all literals exactly and introduce no substitutes.",
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_007", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={
                "cycle_id": "cycle_38980610",
                "thread_id": "thread_008",
                "changed_ts": "2024-08-23T12:05:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_008",
                "from_email": "alex.dev@company.com",
                "body": "APPROVED - ship it",
                "created_ts": "2024-08-23T12:06:00Z"
            }),
            Action(name="sync_gmail_intents_to_review", kwargs={
                "cycle_id": "cycle_38980610",
                "thread_id": "thread_008"
            }),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_008"}),
            Action(name="search_gmail_threads", kwargs={"keyword": "Pricing"})
        ],
        outputs=[
            "[\n  {\n    \"thread_id\": \"thread_008\",\n    \"subject\": \"Pricing Page A/B Testing Results\",\n    \"current_labels\": [\n      \"pricing\",\n      \"ab-testing\",\n      \"results\"\n    ],\n    \"updated_ts\": \"2024-08-23T12:06:00Z\"\n  }\n]"
        ],
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_39",
        instruction="You are the cross-channel asset-readiness steward for the Release Notes & Asset Handoff workflow, ensuring export lineage, coordinated safety posture, and cross-system discoverability across Figma↔Gmail. Produce an audit-ready snapshot that evidences—as immutable facts (a record, not a procedure)—the following: Figma artifact art_001 in status handoff-ready effective 2024-08-24T10:00:00Z; an outcomes note authored by mike.ux@company.com anchored node-1:12 at 2024-08-24T10:02:00Z with the exact body 'Hero assets exported—keep alt text synced.'; source mail context thread_004 documenting a coordination note from design.system@company.com at 2024-08-24T10:03:00Z with the exact text 'Assets exported for homepage hero.'; and a single safety evaluation represented as of 08-24T10:04:00Z, where dlp-flag is used only upon detection. Include the exported assets listing for artifact_id art_001 as the stable delivery reference. Honor the literals exactly and introduce no substitutes.",
        actions=[
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_001",
                "tag": "handoff-ready",
                "changed_ts": "2024-08-24T10:00:00Z"
            }),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_001",
                "author_email": "mike.ux@company.com",
                "body": "Hero assets exported—keep alt text synced.",
                "anchor_ref": "node-1:12",
                "created_ts": "2024-08-24T10:02:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_004",
                "from_email": "design.system@company.com",
                "body": "Assets exported for homepage hero.",
                "created_ts": "2024-08-24T10:03:00Z"
            }),
            Action(name="dlp_scan_and_label_thread", kwargs={
                "thread_id": "thread_004",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-24T10:04:00Z"
            }),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[
            """[
    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ],
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_40",
        instruction=(
            "You are the guarded release-draft steward ensuring lineage, attachment safety, and a release-ready posture. "
            "Record a non-procedural, audit-ready snapshot that confirms: operation within the release/ lineage with release_001 as the diff authority; "
            "a release Gmail draft in thread_006 from sarah.designer@company.com at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.'; "
            "attachment-policy validation via message_id relmsg_9cc87e81; and a conversation state where Design/Release and release-ready are present effective 2024-08-22T17:06:00Z. "
            "Provide the exported assets tied to art_001 as the stable reference."
        ),
        actions=[
            Action(name="list_releases", kwargs={"version_prefix": "release/"}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "release-ready"], "remove_labels": [], "changed_ts": "2024-08-22T17:06:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """[
    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ],
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_41",
        instruction="You are the handoff-readiness steward aligning Figma↔Gmail posture and tag hygiene. Deliver an audit-ready record (facts, not procedures) showing: configuration baselines design_system_mappings and intent_keywords consulted; art_001 carrying handoff-ready effective 2024-08-25T08:00:00Z; terminal note 'Applied temporary handoff tag for art_001' at 2024-08-25T08:01:00Z; handoff-check present at 2024-08-25T08:05:00Z and absent by 2024-08-25T08:25:00Z; handoff-ready absent by 2024-08-25T08:30:00Z; terminal note 'Removed temporary handoff tag for art_001' at 2024-08-25T08:31:00Z; and the exported asset list for art_001 as the stable reference. Treat tag and log changes as durable DB modifications with immutable timestamps.",
        actions=[
            Action(name="read_system_config", kwargs={"config_key": "design_system_mappings"}),
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_001", "tag": "handoff-ready", "changed_ts": "2024-08-25T08:00:00Z"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-25T08:01:00Z", "message": "Applied temporary handoff tag for art_001"}),
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_001", "tag": "handoff-check", "changed_ts": "2024-08-25T08:05:00Z"}),
            Action(name="remove_artifact_tag", kwargs={"artifact_id": "art_001", "tag": "handoff-check", "changed_ts": "2024-08-25T08:25:00Z"}),
            Action(name="remove_artifact_tag", kwargs={"artifact_id": "art_001", "tag": "handoff-ready", "changed_ts": "2024-08-25T08:30:00Z"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-25T08:31:00Z", "message": "Removed temporary handoff tag for art_001"}),
            Action(name="read_system_config", kwargs={"config_key": "intent_keywords"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """[
        {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ]
    ),


    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_42",
        instruction="You are the release-ready communications steward ensuring compliant posture under attachment guardrails. Provide a non-procedural, audit-ready snapshot confirming: a deterministic Gmail draft for release_001 in thread_006 from sarah.designer@company.com at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.'; attachment-policy validation via Gmail message_id relmsg_9cc87e81; a conversation stance on Figma thread_006 where Design/Release and sentiment/positive are present and draft is absent as of 08-22T17:05:00Z; the QA note 'QA sign-off complete' authored by qa.lead@company.com at 08-22T17:06:00Z; and the exported assets tied to art_001 as the stable evidence.",
        actions=[
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "sentiment/positive"], "remove_labels": ["draft"], "changed_ts": "2024-08-22T17:05:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_006", "from_email": "qa.lead@company.com", "body": "QA sign-off complete", "created_ts": "2024-08-22T17:06:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """[
    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ]
    ),

    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="HARD_43",
        instruction="You are the provenance steward closing the review loop with label normalization under policy. Provide an audit-ready, non-procedural snapshot confirming: a cycle for art_004 created at 2024-08-23T13:00:00Z (cycle_1dc59e3f) and linked to thread_003 at 08-23T13:05:00Z; status NEEDS_REVIEW effective 08-23T13:20:00Z; an APPROVED decision by alex.dev@company.com at 08-23T13:25:00Z with comment 'LGTM'; a normalized label posture on thread_003 where Design/Approved is present and Design/Needs-Review is absent as of 08-23T13:30:00Z; the terminal log 'Review approved and labels aligned' at 08-23T13:31:00Z; and the exported assets for art_001 as the stable reference.",
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="advance_review_status", kwargs={"cycle_id": "cycle_1dc59e3f", "new_status": "NEEDS_REVIEW", "changed_ts": "2024-08-23T13:20:00Z"}),
            Action(name="record_review_approval", kwargs={"cycle_id": "cycle_1dc59e3f", "approver_email": "alex.dev@company.com", "decision": "APPROVED", "decided_ts": "2024-08-23T13:25:00Z", "comment": "LGTM"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_003", "add_labels": ["Design/Approved"], "remove_labels": ["Design/Needs-Review"], "changed_ts": "2024-08-23T13:30:00Z"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-23T13:31:00Z", "message": "Review approved and labels aligned"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """[

    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ]
    ),


    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_44",
        instruction="You are the Gmail→Figma signal-quantification steward ensuring sentiment posture without prescribing steps. Provide an audit-ready, non-procedural record whose evidence demonstrates: a review for Figma art_004 with creation time 2024-08-23T13:00:00Z under deterministic cycle_id cycle_1dc59e3f; association to source conversation thread_003 effective 2024-08-23T13:05:00Z; two Gmail messages recognized as intents—'Looks good—LGTM from marketing.' from lisa.marketing@company.com at 2024-08-23T13:10:00Z and 'Please REVISE the grid spacing to 8px multiples.' from alex.dev@company.com at 2024-08-23T13:15:00Z; a conversation stance on thread_003 where sentiment/mixed is present effective 2024-08-23T13:16:00Z; synchronized Gmail intents on that same cycle; and the exported assets for art_001 as the stable handoff reference.",
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_003", "from_email": "lisa.marketing@company.com", "body": "Looks good—LGTM from marketing.", "created_ts": "2024-08-23T13:10:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_003", "from_email": "alex.dev@company.com", "body": "Please REVISE the grid spacing to 8px multiples.", "created_ts": "2024-08-23T13:15:00Z"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_003", "add_labels": ["sentiment/mixed"], "remove_labels": [], "changed_ts": "2024-08-23T13:16:00Z"}),
            Action(name="sync_gmail_intents_to_review", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """[

    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ]
    ),


    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_45",
        instruction="You translate governance intent into a canonical audit state for marketing navigation without prescribing sequence. Use constants: artifact_id art_006; audit_type COMBINED_DS_A11Y with created_ts 2024-08-28T13:00:00Z; terminal log at 2024-08-28T13:05:00Z message 'Prepared audit for art_006'; tag audit-in-progress added at 2024-08-28T13:06:00Z and removed at 2024-08-28T13:20:00Z; config_key design_system_mappings. Context: Figma FILE with Gmail-linked traceability (no email required). Policy: confirm design-system mapping, persist the audit posture and tag lifecycle in the database, and treat the canonical artifact summary as authoritative. Return only the artifact summary for art_006 reflecting modified_ts 2024-08-28T13:20:00Z.",
        actions=[
            Action(name="read_system_config", kwargs={"config_key": "design_system_mappings"}),
            Action(name="create_audit_session", kwargs={
                "artifact_id": "art_006",
                "created_ts": "2024-08-28T13:00:00Z",
                "audit_type": "COMBINED_DS_A11Y"
            }),
            Action(name="log_terminal_event", kwargs={
                "log_ts": "2024-08-28T13:05:00Z",
                "message": "Prepared audit for art_006"
            }),
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_006",
                "tag": "audit-in-progress",
                "changed_ts": "2024-08-28T13:06:00Z"
            }),
            Action(name="remove_artifact_tag", kwargs={
                "artifact_id": "art_006",
                "tag": "audit-in-progress",
                "changed_ts": "2024-08-28T13:20:00Z"
            }),
            Action(name="get_artifact_summary", kwargs={"artifact_id": "art_006"}),
        ],
        outputs=[
            """{
    "artifact_id": "art_006",
    "artifact_name": "Marketing Website",
    "artifact_type": "FILE",
    "owner_email": "lisa.marketing@company.com",
    "deep_link": "https://www.figma.com/file/def456ghi789/Marketing-Website",
    "current_tags": [
    "marketing",
    "website",
    "landing-pages"
    ],
    "modified_ts": "2024-08-28T13:20:00Z"
    }"""
    ]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_46",
        instruction="You are a budget-disciplined fix-planning steward for marketing website accessibility who reports an audit-ready record of planning signals without stepwise prescription. Governance orientation references fix_workflow_config; planning lifecycle for art_006 shows a11y-queued present at 2024-08-28T15:05:00Z, fix-planned present at 2024-08-28T15:10:00Z, the narrative “Fix plan drafted for art_006” captured at 2024-08-28T15:11:00Z, and fix-planned cleared at 2024-08-28T15:30:00Z; authoritative status is represented by the canonical artifact summary for art_006 reflecting modified_ts 2024-08-28T15:30:00Z.",
        actions=[
            Action(name="read_system_config", kwargs={"config_key": "fix_workflow_config"}),
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_006",
                "tag": "a11y-queued",
                "changed_ts": "2024-08-28T15:05:00Z"
            }),
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_006",
                "tag": "fix-planned",
                "changed_ts": "2024-08-28T15:10:00Z"
            }),
            Action(name="log_terminal_event", kwargs={
                "log_ts": "2024-08-28T15:11:00Z",
                "message": "Fix plan drafted for art_006"
            }),
            Action(name="remove_artifact_tag", kwargs={
                "artifact_id": "art_006",
                "tag": "fix-planned",
                "changed_ts": "2024-08-28T15:30:00Z"
            }),
            Action(name="get_artifact_summary", kwargs={"artifact_id": "art_006"}),
        ],
        outputs=[
            """{
    "artifact_id": "art_006",
    "artifact_name": "Marketing Website",
    "artifact_type": "FILE",
    "owner_email": "lisa.marketing@company.com",
    "deep_link": "https://www.figma.com/file/def456ghi789/Marketing-Website",
    "current_tags": [
    "marketing",
    "website",
    "landing-pages",
    "a11y-queued"
    ],
    "modified_ts": "2024-08-28T15:30:00Z"
    }"""
    ]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_47",
        instruction="You own brand accessibility guidance capture across Figma↔Gmail. Target state: intent_keywords consulted; art_012 includes a brand note by emma.brand@company.com at 2024-08-26T 09:00:00Z anchored node-12:1 with body “Align tokens with brand v3.” and a QA note by brand.qa@company.com at 2024-08- 26T09:05:00Z anchored node-12:2 with body “Verify logo safe-area usage.”; thread_001 carries triaged and figma-sync and excludes urgent with changed_ts 2024- 08-26T09:06:00Z; an audit entry “Brand feedback captured for art_012” at 2024 -08-26T09:07:00Z; and the exported assets for art_001 for discoverability.",
        actions=[
            Action(name="read_system_config", kwargs={"config_key": "intent_keywords"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_012", "author_email": "emma.brand@company.com", "body": "Align tokens with brand v3.", "anchor_ref": "node-12:1", "created_ts": "2024-08-26T09:00:00Z"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_012", "author_email": "brand.qa@company.com", "body": "Verify logo safe-area usage.", "anchor_ref": "node-12:2", "created_ts": "2024-08-26T09:05:00Z"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_001", "add_labels": ["triaged", "figma-sync"], "remove_labels": ["urgent"], "changed_ts": "2024-08-26T09:06:00Z"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-26T09:07:00Z", "message": "Brand feedback captured for art_012"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """[
    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_48",
        instruction="You are the brand-guidance provenance steward ensuring policy-aligned traceability for design-system tokens across the Figma↔Gmail workflow. Produce an audit-ready record (facts, not procedures) confirming: the policy config intent_keywords was referenced; on art_003 a Figma comment anchored to node-2:7 authored by emma.brand@company.com (Gmail identity) at 2024-08-28T09:05:00Z with the exact text “Please update the brand color token to Brand/Primary/600.”; thread_005 exhibits DB label hygiene with triaged present and update absent effective 2024-08-28T09:06:00Z; a terminal log “Brand guidance captured for Design System” at 2024-08-28T09:07:00Z; and the canonical artifact summary for art_003 as the coordination outcome.",
        actions=[
            Action(name="read_system_config", kwargs={"config_key": "intent_keywords"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_005", "add_labels": ["triaged"], "remove_labels": ["update"], "changed_ts": "2024-08-28T09:06:00Z"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-28T09:05:00Z"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-28T09:07:00Z", "message": "Brand guidance captured for Design System"}),
            Action(name="get_artifact_summary", kwargs={"artifact_id": "art_003"}),
        ],
        outputs=[
            """{
    "artifact_id": "art_003",
    "artifact_name": "Design System",
    "artifact_type": "PAGE",
    "owner_email": "sarah.designer@company.com",
    "deep_link": "https://www.figma.com/file/abc123def456/Design-System?node-id=1%3A2",
    "current_tags": [
    "design-system",
    "components",
    "tokens"
    ],
    "modified_ts": "2024-08-22T16:45:00Z"
    }"""
    ]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_49",
        instruction="You are a review-intent intake coordinator responsible for translating Gmail feedback into deterministic evidence without changing review status.  Your primary responsibility involves review provenance for art_004 with cycle_id cycle_b73c0216 linked to thread_010 (created 2024-08-24T09:00:00Z / linked 2024-08-24T09:05:00Z).  The intake workflow centers on two intent messages: from alex.dev@company.com at 2024-08-24T09:10:00Z with body 'Looks good—LGTM from engineering.' and from lisa.marketing@company.com at 2024-08-24T09:12:00Z with body 'Please adjust spacing to 8px grid; otherwise fine.' Return the last append message result.",
        actions=[
            Action(name="start_review_cycle", kwargs={
                "artifact_id": "art_004",
                "created_ts": "2024-08-24T09:00:00Z"
            }),
            Action(name="link_review_to_thread", kwargs={
                "cycle_id": "cycle_b73c0216",
                "thread_id": "thread_010",
                "changed_ts": "2024-08-24T09:05:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_010",
                "from_email": "alex.dev@company.com",
                "body": "Looks good—LGTM from engineering.",
                "created_ts": "2024-08-24T09:10:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_010",
                "from_email": "lisa.marketing@company.com",
                "body": "Please adjust spacing to 8px grid; otherwise fine.",
                "created_ts": "2024-08-24T09:12:00Z"
            }),
        ],
        outputs=[
    """{
    "success": true,
    "message_id": "msg_84dd1303"
    }""",
    ],
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_50",
        instruction="You consolidate release communications into a single Gmail thread with deterministic provenance and database-backed state, without prescribing sequence. Use constants: release_id release_001, thread_id thread_010, from_email sarah.designer@company.com at created_ts 2024-08-22T17:00:00Z subject 'Release 1.2.0 Announcement' body 'Highlights and changes included.', label 'announced' with changed_ts 2024-08-22T17:06:00Z, and an approval note 'APPROVE rollout.' at 2024-08-22T17:07:00Z. Policy: ensure the draft, announced posture, and approval are captured so the DB mirrors Gmail; Figma context may be referenced as metadata. Return only the result of the final append.",
        actions=[
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_010",
                "from_email": "sarah.designer@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_010",
                "add_labels": ["announced"],
                "remove_labels": [],
                "changed_ts": "2024-08-22T17:06:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_010",
                "from_email": "sarah.designer@company.com",
                "body": "APPROVE rollout.",
                "created_ts": "2024-08-22T17:07:00Z"
            }),
        ],
        outputs=[
    """{
    "success": true,
    "message_id": "msg_da121760"
    }""",
    ],
    ),

    Task(
        annotator="0",
        user_id="EXP_1",
        instruction=(
        "You are a structured review coordination owner responsible for translating admin navigation update signals into an auditable trail across artifact_id art_011 and thread_id thread_013. "
        "Stakeholder intent and design guidance must be captured, aligned, and surfaced for decision traceability and accessibility of the review record. "
        "The coordination captures two canonical decision signals—msg1 at 2024-08-23T22:10:00Z by pm.lead@company.com stating 'Approve navigation density.' and msg2 at 2024-08-23T22:15:00Z by qa.lead@company.com noting 'Blocker: overflow on mobile filter.'—and reflects review posture through label alignment where 'triaged' and 'needs-review' are present with changed_ts 2024-08-23T22:25:00Z. "
        "Design oversight is represented by a design note at 2024-08-23T22:30:00Z by design.lead@company.com anchored to node-11:3 with guidance 'Proceed after mobile fix.' "
        "Safety governance relies on data loss prevention policy; if blocked content is detected, the thread carries dlp-flag with dlp_changed_ts 2024-08-23T22:35:00Z. "
        "Your responsibility ensures coherent review coordination, traceable decision signals, accurate DLP posture application, and a fully auditable navigation update trail."
        ),
        actions=[
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_013",
                "from_email": "pm.lead@company.com",
                "body": "Approve navigation density.",
                "created_ts": "2024-08-23T22:10:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_013",
                "from_email": "qa.lead@company.com",
                "body": "Blocker: overflow on mobile filter.",
                "created_ts": "2024-08-23T22:15:00Z"
            }),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_013",
                "add_labels": ["triaged", "needs-review"],
                "remove_labels": [],
                "changed_ts": "2024-08-23T22:25:00Z"
            }),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_011",
                "author_email": "design.lead@company.com",
                "body": "Proceed after mobile fix.",
                "anchor_ref": "node-11:3",
                "created_ts": "2024-08-23T22:30:00Z"
            }),
            Action(name="dlp_scan_and_label_thread", kwargs={
                "thread_id": "thread_013",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-23T22:35:00Z"
            })
        ],
        outputs=[
            """{
              "thread_id": "thread_013",
              "blocked_terms_found": [],
              "label_applied": false
            }"""
        ]
    ),


    Task(
        annotator="0",
        user_id="EXP_2",
        instruction=(
        "You are an admin panel coordination owner aligning comment traceability, asset visibility, release awareness, and safety posture without prescribing a fixed sequence. "
        "Focus on art_008 and its discussion in thread_004: capture a deterministic resolution note by mike.ux@company.com anchored at node-8:13 at 2024-08-24T18:46:00Z with body 'Admin header focus order and ARIA attributes validated; keyboard navigation confirmed.' "
        "Retain a current assets snapshot for art_008 to reflect readiness. "
        "Record a concise coordination update in thread_004 from design.system@company.com at 2024-08-24T18:48:00Z with body 'Admin panel changes synced—moving to validation.' "
        "Preserve safety posture through a single evaluation on thread_004 with label_if_found dlp-flag and changed_ts 2024-08-24T18:50:00Z. "
        "Ground decisions in dlp_config and design_system_mappings, and maintain release_002 awareness via a diff snapshot. "
        "Constants: artifact_id art_008, comment_id comment_006, asset_id asset_007, thread_id thread_004, release_id release_002."
        ),
        actions=[
            Action(name="list_figma_comments", kwargs={"artifact_id": "art_008"}),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_008",
                "author_email": "mike.ux@company.com",
                "body": "Admin header focus order and ARIA attributes validated; keyboard navigation confirmed",
                "anchor_ref": "node-8:13",
                "created_ts": "2024-08-24T18:46:00Z"
            }),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_008"}),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_004",
                "from_email": "design.system@company.com",
                "body": "Admin panel changes synced—moving to validation.",
                "created_ts": "2024-08-24T18:48:00Z"
            }),
            Action(name="dlp_scan_and_label_thread", kwargs={"thread_id": "thread_004", "label_if_found": "dlp-flag", "changed_ts": "2024-08-24T18:50:00Z"}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_002"}),
            Action(name="read_system_config", kwargs={"config_key": "dlp_config"}),
            Action(name="read_system_config", kwargs={"config_key": "design_system_mappings"})
        ],
        outputs=[
            """{
                "release_id": "release_002",
                "added": 0,
                "updated": 0,
                "removed": 0
            }"""
        ]
    ),

    Task(
        annotator="0",
        user_id="EXP_3",
        instruction="You are the review-to-approval provenance steward ensuring Gmail↔Figma signal parity without prescribing steps. Deliver an audit-ready record (facts, not procedures) validating: thread_006 carries two intents—a message from pm.lead@company.com at 2024-08-24T18:05:00Z with body 'Approve pricing grid.' and a message from qa.lead@company.com at 2024-08-24T18:10:00Z with body 'Revise discount footnote.'—with a confirmed DLP status; the design_system_mappings policy was referenced for terminology alignment; art_002 reflects a database state change where tag approved-for-release is present effective 2024-08-24T18:16:00Z; the assets listing for art_002 is surfaced; and the terminal log 'Review intents captured and tag applied for art_002' is recorded at 2024-08-24T 18:17:00Z. Constants: artifact_id art_002; thread_id thread_006.",
        actions=[
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_006",
                "from_email": "pm.lead@company.com",
                "body": "Approve pricing grid.",
                "created_ts": "2024-08-24T18:05:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_006",
                "from_email": "qa.lead@company.com",
                "body": "Revise discount footnote.",
                "created_ts": "2024-08-24T18:10:00Z"
            }),
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_002", "tag": "approved-for-release", "changed_ts": "2024-08-24T18:16:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_002"}),
            Action(name="read_system_config", kwargs={"config_key": "design_system_mappings"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_006"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-24T18:17:00Z", "message": "Review intents captured and tag applied for art_002"})
        ],
        outputs=[
            """[
                {
                    "asset_id": "asset_003",
                    "profile": null,
                    "file_name": null,
                    "mime_type": null
                }
            ]"""
        ]
    ),

    # complexity_edges: 16
    Task(
        annotator="0",
        user_id="EXP_4",
        instruction="You manage visibility tagging, release communications compliance, and brand guidance verification. Maintain a temporary visibility tag cycle on art_001 using tag handoff-ready with start timestamp 2024-08-23T10:10:00Z and removal timestamp 2024-08-23T10:40:00Z. Prepare the release_001 announcement draft in thread_006 from sarah.designer@company.com at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.' and confirm attachment policy compliance under message_id relmsg_9cc87e81. Capture a brand note on art_003 authored by emma.brand@company.com anchored at node-2:7 at 2024-08-23T12:00:00Z with text 'Please update the brand color token to Brand/Primary/600.', then deliver that author's comment history on art_003 since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_001", "tag": "handoff-ready", "changed_ts": "2024-08-23T10:10:00Z"}),
            Action(name="remove_artifact_tag", kwargs={"artifact_id": "art_001", "tag": "handoff-ready", "changed_ts": "2024-08-23T10:40:00Z"}),
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="list_figma_comments", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[
            """[
            {
                "comment_id": "cmt_10b86546",
                "author_email": "emma.brand@company.com",
                "anchor_ref": "node-2:7",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "created_ts": "2024-08-23T12:00:00Z"
            }
            ]"""
        ]
    ),


    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="EXP_5",
        instruction="You coordinate compliance-aware escalation across email and design review with brand guidance tracking. Target, deterministic state: thread_002 contains a memo by sarah.designer@company.com at 2024-08-23T11:00:00Z with body 'Please note: temporary password is abcd-1234; rotate after testing.' and carries DLP posture via label dlp-flag with changed_ts 2024-08-23T11:05:00Z if sensitive content is detected; art_004 has a review identified as cycle_1dc59e3f linked to thread_003 and reflecting interim status NEEDS_REVIEW at 2024-08-23T13:20:00Z after a creation timestamp of 2024-08-23T13:00:00Z and link timestamp 2024-08-23T13:05:00Z; brand direction is captured on art_003 from emma.brand@company.com anchored at node-2:7 at 2024-08-23T12:00:00Z with text 'Please update the brand color token to Brand/Primary/600.'; output is the author-filtered comment history for art_003 scoped to emma.brand@company.com since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_002", "from_email": "sarah.designer@company.com", "body": "Please note: temporary password is abcd-1234; rotate after testing.", "created_ts": "2024-08-23T11:00:00Z"}),
            Action(name="dlp_scan_and_label_thread", kwargs={"thread_id": "thread_002", "label_if_found": "dlp-flag", "changed_ts": "2024-08-23T11:05:00Z"}),
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="advance_review_status", kwargs={"cycle_id": "cycle_1dc59e3f", "new_status": "NEEDS_REVIEW", "changed_ts": "2024-08-23T13:20:00Z"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="list_figma_comments", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[
            """[
            {
                "comment_id": "cmt_10b86546",
                "author_email": "emma.brand@company.com",
                "anchor_ref": "node-2:7",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "created_ts": "2024-08-23T12:00:00Z"
            }
            ]"""
        ]
    ),


    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="EXP_6",
        instruction="You are the review-provenance steward ensuring Figma↔Gmail intent parity for release readiness and brand guidance. Deliver an audit-ready record (facts, not procedures) confirming: a review cycle cycle_1dc59e3f for art_004 created at 2024-08-23T13:00:00Z and associated to thread_003 effective 2024-08-23T13:05:00Z; thread_003 carries two explicit signals—qa.lead@company.com “this needs changes” at 2024-08-23T13:12:00Z and build.bot@company.com “blocker: build failing” at 2024-08-23T13:14:00Z—and these intents are reflected in cycle_1dc59e3f; a release_001 announcement draft in thread_006 from sarah.designer@company.com created at 2024-08-22T17:00:00Z with subject “Release 1.2.0 Announcement” and body “Highlights and changes included.” validated via message_id relmsg_9cc87e81 under attachment policy; and brand guidance on art_003 recorded as a Figma note anchored node-2:7 by emma.brand@company.com at 2024-08-23T12:00:00Z stating “Please update the brand color token to Brand/Primary/600.” Output the author-scoped comment history for art_003 filtered to emma.brand@company.com since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_003", "from_email": "qa.lead@company.com", "body": "this needs changes", "created_ts": "2024-08-23T13:12:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_003", "from_email": "build.bot@company.com", "body": "blocker: build failing", "created_ts": "2024-08-23T13:14:00Z"}),
            Action(name="sync_gmail_intents_to_review", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003"}),
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="list_figma_comments", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[
            """[
            {
                "comment_id": "cmt_10b86546",
                "author_email": "emma.brand@company.com",
                "anchor_ref": "node-2:7",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "created_ts": "2024-08-23T12:00:00Z"
            }
            ]"""
        ]
    ),


    # complexity_edges: 19
    Task(
        annotator="0",
        user_id="EXP_7",
        instruction="You oversee end-to-end closure across review progression, approvals, compliance labeling, release comms, and brand guidance. Target state must uniquely include: art_004 review (cycle_1dc59e3f) associated to thread_003 with creation 2024-08-23T13:00:00Z and linkage 2024-08-23T13:05:00Z, showing interim status NEEDS_REVIEW at 2024-08-23T13:20:00Z and a final decision APPROVED by alex.dev@company.com at 2024-08-23T13:25:00Z with comment 'LGTM'; thread_002 contains 'temporary password abcd-1234 for staging' from devops@company.com at 2024-08-23T11:15:00Z and reflects DLP posture with label dlp-flag at changed_ts 2024-08-23T11:16:00Z when sensitive content is present; a release_001 announcement draft is present in thread_006 from sarah.designer@company.com created at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.' validated via message_id relmsg_9cc87e81; brand direction exists on art_003 from emma.brand@company.com anchored at node-2:7 at 2024-08-23T12:00:00Z with text 'Please update the brand color token to Brand/Primary/600.'; output is the author-filtered comment history for art_003 limited to emma.brand@company.com since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="advance_review_status", kwargs={"cycle_id": "cycle_1dc59e3f", "new_status": "NEEDS_REVIEW", "changed_ts": "2024-08-23T13:20:00Z"}),
            Action(name="record_review_approval", kwargs={"cycle_id": "cycle_1dc59e3f", "approver_email": "alex.dev@company.com", "decision": "APPROVED", "decided_ts": "2024-08-23T13:25:00Z", "comment": "LGTM"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_002", "from_email": "devops@company.com", "body": "temporary password abcd-1234 for staging", "created_ts": "2024-08-23T11:15:00Z"}),
            Action(name="dlp_scan_and_label_thread", kwargs={"thread_id": "thread_002", "label_if_found": "dlp-flag", "changed_ts": "2024-08-23T11:16:00Z"}),
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="list_figma_comments", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[
            """{
                "comment_id": "cmt_10b86546",
                "author_email": "emma.brand@company.com",
                "anchor_ref": "node-2:7",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "created_ts": "2024-08-23T12:00:00Z"
            }"""
        ]
    ),


    # complexity_edges: 19
    Task(
        annotator="0",
        user_id="EXP_8",
        instruction="You run an end-to-end release communication with attachment and DLP guardrails, then provide a stable asset reference. Operate within the release/ lineage using release_001 as the authoritative diff. The announcement exists as a draft in thread_006 from sarah.designer@company.com at 2024-08-22T17:00:00Z with subject “Release 1.2.0 Announcement” and body “Highlights and changes included.” The draft message relmsg_9cc87e81 complies with attachment policy; conversation status reflects Design/Release and announced with draft removed at 2024-08-22T17:06:00Z; a closing note “APPROVE rollout.” from sarah.designer@company.com is recorded at 2024-08-22T17:07:00Z; DLP posture is verified on the same thread. Return the exported assets for art_001.",
        actions=[
            Action(name="list_releases", kwargs={"version_prefix": "release/"}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "announced"], "remove_labels": ["draft"], "changed_ts": "2024-08-22T17:06:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_006", "from_email": "sarah.designer@company.com", "body": "APPROVE rollout.", "created_ts": "2024-08-22T17:07:00Z"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_006"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """{
            "asset_id": "asset_001",
            "profile": null,
            "file_name": null,
            "mime_type": null
            },
            {
            "asset_id": "asset_002",
            "profile": null,
            "file_name": null,
            "mime_type": null
            }"""
        ],
    ),

    Task(
        annotator="0",
        user_id="EXP_9",
        instruction="You are the brand-governance steward maintaining Gmail↔Figma signal parity and audit-ready authorship for art_012. Deliver an audit-ready record (facts, not procedures) confirming: governance references intent_keywords and dlp_config were consulted; a canonical brand note by emma.brand@company.com at 2024-08-24T13:00:00Z anchored node-12:1 with exact body 'Align tokens with brand v3.'; a companion QA note by brand.qa@company.com at 2024-08-24T13:05:00Z anchored node-12:2 with exact body 'Verify logo safe-area usage.'; and a terminal DB-visible modification at 2024-08-24T13:10:00Z recording 'Brand page comments added.' Provide the author-scoped comment view for art_012 filtered to emma.brand@company.com since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="read_system_config", kwargs={"config_key": "intent_keywords"}),
            Action(name="read_system_config", kwargs={"config_key": "dlp_config"}),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_012",
                "author_email": "emma.brand@company.com",
                "body": "Align tokens with brand v3.",
                "anchor_ref": "node-12:1",
                "created_ts": "2024-08-24T13:00:00Z"
            }),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_012",
                "author_email": "brand.qa@company.com",
                "body": "Verify logo safe-area usage.",
                "anchor_ref": "node-12:2",
                "created_ts": "2024-08-24T13:05:00Z"
            }),
            Action(name="log_terminal_event", kwargs={
                "log_ts": "2024-08-24T13:10:00Z",
                "message": "Brand page comments added"
            }),
            Action(name="list_figma_comments", kwargs={
                "artifact_id": "art_012",
                "author_email": "emma.brand@company.com",
                "since_ts": "2024-08-01T00:00:00Z"
            })
        ],
        outputs=[
            """{
              "artifact_id": "art_012",
              "comments_recorded": 2,
              "filtered_list_count": 1
            }"""
        ]
    ),

    # complexity_edges: 21
    Task(
        annotator="0",
        user_id="EXP_10",
        instruction="You are the landing-page review orchestration specialist accountable for posture alignment, DLP-clean communication hygiene, and handoff readiness. Scope is the art_001 landing-page frame owned by sarah.designer@company.com (artifact type FRAME, tag landing-page, modified on/after 2024-08-01T00:00:00Z) with mail context in thread_001. The committed end-state must satisfy all of the following facts: (1) art_001 carries review posture needs-review with effective time 2024-08-24T09:45:00Z; (2) the review ledger shows a single active review instance for art_001 with status IN_FLIGHT created at 2024-08-24T09:46:00Z; (3) thread_001 records a kickoff authored by sarah.designer@company.com at 2024-08-24T09:47:00Z with text “Please REVIEW design; awaiting APPROVE or CHANGES.”; (4) as of 2024-08-24T09:48:00Z the thread's label posture includes Design/Needs-Review and triaged and excludes dlp-flag; (5) a DLP verification exists for thread_001; (6) provide the exported asset list for art_001.",
        actions=[
            Action(name="list_artifacts", kwargs={"owner_email": "sarah.designer@company.com", "tag": "landing-page", "artifact_type": "FRAME", "modified_since": "2024-08-01T00:00:00Z"}),
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_001", "tag": "needs-review", "changed_ts": "2024-08-24T09:45:00Z"}),
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_001", "created_ts": "2024-08-24T09:46:00Z", "status": "IN_FLIGHT"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_001", "from_email": "sarah.designer@company.com", "body": "Please REVIEW design; awaiting APPROVE or CHANGES.", "created_ts": "2024-08-24T09:47:00Z"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_001", "add_labels": ["Design/Needs-Review", "triaged"], "remove_labels": ["dlp-flag"], "changed_ts": "2024-08-24T09:48:00Z"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_001"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """{
            "asset_id": "asset_001",
            "profile": null,
            "file_name": null,
            "mime_type": null
            },
            {
            "asset_id": "asset_002",
            "profile": null,
            "file_name": null,
            "mime_type": null
            }"""
        ],
    ),


    # complexity_edges: 23
    Task(
        annotator="0",
        user_id="EXP_11",
        instruction="You are the active design-review triage owner ensuring mail↔artifact signal parity under DLP policy. Focus on the conversation that matches label design-review, participant alex.dev@company.com, keyword 'Design'. The verified state demonstrates: thread_001 carries labels triaged, figma-sync, Design/Needs-Review with urgent absent (effective 2024-08-24T12:00:00Z); the conversation history includes a reviewer reply by alex.dev@company.com at 2024-08-24T12:05:00Z with the exact body 'CHANGES: Please adjust spacing.' and a confirmed DLP status; and the artifact side mirrors triage with art_001 tagged triaged effective 2024-08-24T12:10:00Z plus a design note anchored node-1:2 authored by alex.dev@company.com at 2024-08-24T12:11:00Z stating 'CHANGES requested noted.' Provide the exported assets for art_001.",
        actions=[
            Action(name="search_gmail_threads", kwargs={"label": "design-review", "participant": "alex.dev@company.com", "keyword": "Design"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_001", "add_labels": ["triaged", "figma-sync", "Design/Needs-Review"], "remove_labels": ["urgent"], "changed_ts": "2024-08-24T12:00:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_001", "from_email": "alex.dev@company.com", "body": "CHANGES: Please adjust spacing.", "created_ts": "2024-08-24T12:05:00Z"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_001"}),
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_001", "tag": "triaged", "changed_ts": "2024-08-24T12:10:00Z"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_001", "author_email": "alex.dev@company.com", "body": "CHANGES requested noted.", "anchor_ref": "node-1:2", "created_ts": "2024-08-24T12:11:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """{
            "asset_id": "asset_001",
            "profile": null,
            "file_name": null,
            "mime_type": null
            },
            {
            "asset_id": "asset_002",
            "profile": null,
            "file_name": null,
            "mime_type": null
            }"""
        ],
    ),

    # complexity_edges: 21
    Task(
        annotator="0",
        user_id="EXP_12",
        instruction="You are the pricing-modification triage steward ensuring signal alignment and discoverability across the Figma↔Gmail workflow. Deliver an audit-ready record (facts, not procedures) validating: art_007 's review created at 2024-08-23T12:00:00Z under cycle_38980610 and associated to thread_008 effective 2024-08-24T19:05:00Z; the Gmail conversation contains a blocker note by qa.lead@company.com at 2024-08-24T19:06:00Z with body 'BLOCKER: consent modal failing on Safari' and a confirmed DLP status; synchronized intents are persisted; the review database state shows changes—status ESCALATED at 2024-08-24T19:07:00Z and decision CHANGES_REQUESTED by alex.dev@company.com at 2024-08-24T19:10:00Z with comment 'Address Safari issue'; and the thread is discoverable via keyword 'Pricing'. Provide the surfaced conversation metadata.",
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_007", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={"cycle_id": "cycle_38980610", "thread_id": "thread_008", "changed_ts": "2024-08-24T19:05:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_008", "from_email": "qa.lead@company.com", "body": "BLOCKER: consent modal failing on Safari", "created_ts": "2024-08-24T19:06:00Z"}),
            Action(name="sync_gmail_intents_to_review", kwargs={"cycle_id": "cycle_38980610", "thread_id": "thread_008"}),
            Action(name="advance_review_status", kwargs={"cycle_id": "cycle_38980610", "new_status": "ESCALATED", "changed_ts": "2024-08-24T19:07:00Z"}),
            Action(name="record_review_approval", kwargs={"cycle_id": "cycle_38980610", "approver_email": "alex.dev@company.com", "decision": "CHANGES_REQUESTED", "decided_ts": "2024-08-24T19:10:00Z", "comment": "Address Safari issue"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_008"}),
            Action(name="search_gmail_threads", kwargs={"keyword": "Pricing"}),
        ],
        outputs=[
            """[
            {
            "thread_id": "thread_008",
            "subject": "Pricing Page A/B Testing Results",
            "current_labels": [
            "pricing",
            "ab-testing",
            "results"
            ],
            "updated_ts": "2024-08-24T19:06:00Z"
            }
            ]"""
        ]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="EXP_13",
        instruction="You are the navigation updates approval-closure steward responsible for a deterministic decision trail and clean mail safety posture. Your audit-ready outcome must unambiguously reflect: on cycle_1dc59e3f an approver decision recorded by design.lead@company.com with decision APPROVED, decided_ts 2024-08-25T18:20:00Z, and comment 'Ship after QA signoff.'; a mail stance on thread_003 where Design/Approved and triaged are present while needs-review and dlp-flag are absent effective 2024-08-25T18:25:00Z; and a short closure note authored by design.lead@company.com at 2024-08-25T 18:26:00Z with exact body 'Approved pending QA.'. Provide the verified DLP safety result for thread_003 (expected no blocked terms).",
        actions=[
            Action(name="record_review_approval", kwargs={
                "cycle_id": "cycle_1dc59e3f",
                "approver_email": "design.lead@company.com",
                "decision": "APPROVED",
                "decided_ts": "2024-08-25T18:20:00Z",
                "comment": "Ship after QA signoff."
            }),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_003",
                "add_labels": ["Design/Approved", "triaged"],
                "remove_labels": ["needs-review", "dlp-flag"],
                "changed_ts": "2024-08-25T18:25:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_003",
                "from_email": "design.lead@company.com",
                "body": "Approved pending QA.",
                "created_ts": "2024-08-25T18:26:00Z"
            }),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_003"}),
        ],
        outputs=[
            """{
    "thread_id": "thread_003",
    "blocked_terms_found": []
    }"""
    ],
    ),

    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="EXP_14",
        instruction="You are the needs-review provenance steward maintaining Figma↔Gmail signal parity and label-hygiene (db modification traceable) under DLP. Deliver an audit-ready snapshot—facts, not procedures—covering: scope filter owner sarah.designer@company.com, tag landing-page, artifact type FRAME, modified_since 2024-08-01T00:00:00Z; art_001 shows tag needs-review effective 2024-08-24T09:45:00Z; a review for art_001 created 2024-08-24T09:46:00Z with status IN_FLIGHT; thread_001 carries a kickoff note by sarah.designer@company.com at 2024-08-24T09:47:00Z with exact body “Please REVIEW design; awaiting APPROVE or CHANGES.”; thread_001 label posture has Design/Needs-Review and triaged present and dlp-flag absent effective 2024-08-24T09:48:00Z with DLP scan confirming mail safety. Output the exported assets for art_001.",
        actions=[
            Action(name="list_artifacts", kwargs={
                "owner_email": "sarah.designer@company.com",
                "tag": "landing-page",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_001",
                "tag": "needs-review",
                "changed_ts": "2024-08-24T09:45:00Z"
            }),
            Action(name="start_review_cycle", kwargs={
                "artifact_id": "art_001",
                "created_ts": "2024-08-24T09:46:00Z",
                "status": "IN_FLIGHT"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_001",
                "from_email": "sarah.designer@company.com",
                "body": "Please REVIEW design; awaiting APPROVE or CHANGES.",
                "created_ts": "2024-08-24T09:47:00Z"
            }),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_001",
                "add_labels": ["Design/Needs-Review", "triaged"],
                "remove_labels": ["dlp-flag"],
                "changed_ts": "2024-08-24T09:48:00Z"
            }),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_001"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """{
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }"""
    ],
    ),

    # complexity_edges: 19
    Task(
        annotator="0",
        user_id="EXP_15",
        instruction="You are the release-communications steward ensuring Figma↔Gmail signal alignment, compliant labeling, and preserved design lineage. Deliver an audit-ready record (facts, not procedures) confirming: releases under version prefix 'release/' with the diff for release_001; a single announcement draft by sarah.designer@company.com captured at 2024-08-22T17:00:00Z in thread_006 with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.' identified as relmsg_9cc87e81 and attachment-compliant; a DB-visible thread_006 posture where Design/Release and announced are present and draft is absent effective 2024-08-22T17:06:00Z; a closing confirmation by sarah.designer@company.com at 2024-08-22T17:07:00Z stating 'APPROVE rollout.'; and DLP safety verification recorded for thread_006. Provide the exported asset list tied to art_001.",
        actions=[
            Action(name="list_releases", kwargs={"version_prefix": "release/"}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_006",
                "from_email": "sarah.designer@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_006",
                "add_labels": ["Design/Release", "announced"],
                "remove_labels": ["draft"],
                "changed_ts": "2024-08-22T17:06:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_006",
                "from_email": "sarah.designer@company.com",
                "body": "APPROVE rollout.",
                "created_ts": "2024-08-22T17:07:00Z"
            }),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_006"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """{
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }"""
    ],
    ),

    # complexity_edges: 20
    Task(
        annotator="0",
        user_id="EXP_16",
        instruction="You are the accessibility-readiness and DLP-assurance steward for the admin header. Operate within the admin dashboard frame scope (owner alex.dev@company.com, tag dashboard, FRAME, modified_since 2024-08-01T00:00:00Z). Produce an audit-ready snapshot that evidences, without prescribing steps: art_008 in posture a11y-reviewed effective 2024-08-25T15:00:00Z; an outcomes note by alex.dev@company.com anchored node-8:11 at 2024-08-25T15:05:00Z with the exact body 'A11y review completed: focus order and ARIA roles verified.'; and source mail thread_004 carrying a verification note from alex.dev@company.com at 2024-08-25T15:10:00Z with the exact text 'Including test ssn 000-12-3456 for DLP verification only.' Safety posture is represented by a single evaluation captured at 2024-08-25T15:12:00Z and governed by dlp_config; the record shows the detection and the policy label dlp-flag applied.",
        actions=[
            Action(name="list_artifacts", kwargs={"owner_email": "alex.dev@company.com", "tag": "dashboard", "artifact_type": "FRAME", "modified_since": "2024-08-01T00:00:00Z"}),
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_008", "tag": "a11y-reviewed", "changed_ts": "2024-08-25T15:00:00Z"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_008", "author_email": "alex.dev@company.com", "body": "A11y review completed: focus order and ARIA roles verified.", "anchor_ref": "node-8:11", "created_ts": "2024-08-25T15:05:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_004", "from_email": "alex.dev@company.com", "body": "Including test ssn 000-12-3456 for DLP verification only.", "created_ts": "2024-08-25T15:10:00Z"}),
            Action(name="read_system_config", kwargs={"config_key": "dlp_config"}),
            Action(name="dlp_scan_and_label_thread", kwargs={"thread_id": "thread_004", "label_if_found": "dlp-flag", "changed_ts": "2024-08-25T15:12:00Z"})
        ],
        outputs=[
            """{
    "thread_id": "thread_004",
    "blocked_terms_found": [
    "ssn"
    ],
    "label_applied": true
    }"""
    ]
    ),

    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="EXP_17",
        instruction="You are the mobile release communications steward aligning Figma artifacts and Gmail posture. Deliver an audit-ready record (facts, not procedures) establishing: the release catalog scoped by version_prefix release/ and artifact_id None as the authoritative index; a quantified diff for release_012; a deterministic draft on thread_014 authored by mike.ux@company.com at 2024-08-25T16:00:00Z with subject 'Mobile App v2.2.0 - Release Notes' and body 'Changelog and enhancements for Settings & Profile.'; attachment-policy compliance for message_id relmsg_b607ec35; a label posture where release-draft and triaged are present as of 2024-08-25T16:05:00Z; an acknowledgment by qa.lead@company.com at 2024-08-25T16:06:00Z with the exact text 'ACK: No blocking issues in QA.'; and a DLP safety confirmation showing no findings on thread_014.",
        actions=[
            Action(name="list_releases", kwargs={"version_prefix": "release/", "artifact_id": None}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_012"}),
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_012", "thread_id": "thread_014", "from_email": "mike.ux@company.com", "created_ts": "2024-08-25T16:00:00Z", "subject": "Mobile App v2.2.0 - Release Notes", "body": "Changelog and enhancements for Settings & Profile."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_b607ec35"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_014", "add_labels": ["release-draft", "triaged"], "remove_labels": [], "changed_ts": "2024-08-25T16:05:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_014", "from_email": "qa.lead@company.com", "body": "ACK: No blocking issues in QA.", "created_ts": "2024-08-25T16:06:00Z"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_014"})
        ],
        outputs=[
            """{
    "thread_id": "thread_014",
    "blocked_terms_found": []
    }"""
    ]
    ),

    # complexity_edges: 20
    Task(
        annotator="0",
        user_id="EXP_18",
        instruction="You are the release-provenance steward for the 1.2.0 web rollout, maintaining Figma↔Gmail hygiene. Deliver an audit-ready record (facts, not procedures) confirming: lineage under release/ with the authoritative diff for release_001; a deterministic announcement draft for release_001 in thread_006 by sarah.designer@company.com at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.' validated via message_id relmsg_9cc87e81 and passing attachment-policy guard; a label posture where Design/Release and final are present and draft is absent effective 2024-08-22T17:06:00Z; a closing note from sarah.designer@company.com at 2024-08-22T17:07:30Z reading 'APPROVED for rollout.'; a DLP safety confirmation for thread_006; and the exported assets listing for art_001 as the stable handoff reference.",
        actions=[
            Action(name="list_releases", kwargs={"version_prefix": "release/"}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_006",
                "from_email": "sarah.designer@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_006",
                "add_labels": ["Design/Release", "final"],
                "remove_labels": ["draft"],
                "changed_ts": "2024-08-22T17:06:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_006",
                "from_email": "sarah.designer@company.com",
                "body": "APPROVED for rollout.",
                "created_ts": "2024-08-22T17:07:30Z"
            }),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_006"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[
            """[
    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ],
    ),

    # complexity_edges: 20
    Task(
        annotator="0",
        user_id="EXP_19",
        instruction="You are the a11y readiness steward enforcing DLP guardrails across the Figma↔Gmail surface. Document—without prescribing steps—an audit-ready snapshot that shows: the scope is FRAME artifacts tagged dashboard owned by alex.dev@company.com and modified on/after 2024-08-01T00:00:00Z; art_008 in posture a11y-reviewed effective 2024-08-25T15:00:00Z; a comment by alex.dev@company.com anchored node-8:11 at 2024-08-25T15:05:00Z with body 'A11y review completed: focus order and ARIA roles verified.'; source mail thread_004 carrying a verification note from alex.dev@company.com at 2024-08-25T15:10:00Z with the exact text 'Including password for DLP verification only.'; and a single DLP evaluation at 2024-08-25T15:12:00Z, per dlp_config, that deterministically records the blocked token 'password' and applies the policy label dlp-flag.",
        actions=[
            Action(name="list_artifacts", kwargs={
                "owner_email": "alex.dev@company.com",
                "tag": "dashboard",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_008",
                "tag": "a11y-reviewed",
                "changed_ts": "2024-08-25T15:00:00Z"
            }),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_008",
                "author_email": "alex.dev@company.com",
                "body": "A11y review completed: focus order and ARIA roles verified.",
                "anchor_ref": "node-8:11",
                "created_ts": "2024-08-25T15:05:00Z"
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_004",
                "from_email": "alex.dev@company.com",
                "body": "Including password for DLP verification only.",
                "created_ts": "2024-08-25T15:10:00Z"
            }),
            Action(name="read_system_config", kwargs={
                "config_key": "dlp_config"
            }),
            Action(name="dlp_scan_and_label_thread", kwargs={
                "thread_id": "thread_004",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-25T15:12:00Z"
            })
        ],
        outputs=[
            """{
    "thread_id": "thread_004",
    "blocked_terms_found": [
    "password"
    ],
    "label_applied": true
    }"""
    ]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="EXP_20",
        instruction="You finalize a compliant release-ready state while preserving asset context within the Figma↔Gmail release workflow. The canonical record should demonstrate: the maintained draft for release_001 in thread_006 by sarah.designer@company.com at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.'; a QA acknowledgment from qa.lead@company.com at 2024-08-22T17:06:00Z with body 'QA sign-off complete'; attachment-policy validation under message_id relmsg_9cc87e81; a conversation posture where release-ready is present effective 2024-08-22T17:10:00Z; and an artifact-side trace where art_001 carries a temporary handoff-ready tag applied 2024-08-23T10:10:00Z and removed 2024-08-23T10:40:00Z. Provide the exported assets listing for art_001 as the stable reference.",
        actions=[
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_006",
                "from_email": "sarah.designer@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_006",
                "from_email": "qa.lead@company.com",
                "body": "QA sign-off complete",
                "created_ts": "2024-08-22T17:06:00Z"
            }),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_006",
                "add_labels": ["release-ready"],
                "remove_labels": [],
                "changed_ts": "2024-08-22T17:10:00Z"
            }),
            Action(name="add_artifact_tag", kwargs={
                "artifact_id": "art_001",
                "tag": "handoff-ready",
                "changed_ts": "2024-08-23T10:10:00Z"
            }),
            Action(name="remove_artifact_tag", kwargs={
                "artifact_id": "art_001",
                "tag": "handoff-ready",
                "changed_ts": "2024-08-23T10:40:00Z"
            }),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[
            "[\n  {\n    \"asset_id\": \"asset_001\",\n    \"profile\": null,\n    \"file_name\": null,\n    \"mime_type\": null\n  },\n  {\n    \"asset_id\": \"asset_002\",\n    \"profile\": null,\n    \"file_name\": null,\n    \"mime_type\": null\n  }\n]"
        ],
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="EXP_21",
        instruction="You close the loop on review provenance and capture brand guidance with deterministic evidence. The audit-ready snapshot should evidence: for art_004, a review created 2024-08-23T13:00:00Z (cycle_1dc59e3f), linked to thread_003 at 2024-08-23T13:05:00Z, advanced to NEEDS_REVIEW at 2024-08-23T13:20:00Z, and finalized with an APPROVED decision by alex.dev@company.com at 2024-08-23T13:25:00Z with comment 'LGTM'; and, separately, a brand note on art_003 by emma.brand@company.com anchored node-2:7 at 2024-08-23T12:00:00Z with body 'Please update the brand color token to Brand/Primary/600.' The deliverable is the author-scoped comment history for artifact_id art_003 filtered to author_email emma.brand@company.com since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={
                "cycle_id": "cycle_1dc59e3f",
                "thread_id": "thread_003",
                "changed_ts": "2024-08-23T13:05:00Z"
            }),
            Action(name="advance_review_status", kwargs={
                "cycle_id": "cycle_1dc59e3f",
                "new_status": "NEEDS_REVIEW",
                "changed_ts": "2024-08-23T13:20:00Z"
            }),
            Action(name="record_review_approval", kwargs={
                "cycle_id": "cycle_1dc59e3f",
                "approver_email": "alex.dev@company.com",
                "decision": "APPROVED",
                "decided_ts": "2024-08-23T13:25:00Z",
                "comment": "LGTM"
            }),
            Action(name="create_figma_comment", kwargs={
                "artifact_id": "art_003",
                "author_email": "emma.brand@company.com",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "anchor_ref": "node-2:7",
                "created_ts": "2024-08-23T12:00:00Z"
            }),
            Action(name="list_figma_comments", kwargs={
                "artifact_id": "art_003",
                "author_email": "emma.brand@company.com",
                "since_ts": "2024-08-01T00:00:00Z"
            })
        ],
        outputs=[
            "[\n  {\n    \"comment_id\": \"cmt_10b86546\",\n    \"author_email\": \"emma.brand@company.com\",\n    \"anchor_ref\": \"node-2:7\",\n    \"body\": \"Please update the brand color token to Brand/Primary/600.\",\n    \"created_ts\": \"2024-08-23T12:00:00Z\"\n  }\n]"
        ],
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="EXP_22",
        instruction="You coordinate compliant marketing approval and release posture across Gmail and Figma and release governance without prescribing steps. The audit-ready snapshot should evidence: source mail thread_003 containing a sensitive note from lisa.marketing@company.com at 2024-08-23T09:00:00Z with body 'Temporary password is abcd-1234. Rotate after testing.' and a single safety evaluation applying dlp-flag at 2024-08-23T09:05:00Z; and, concurrently, a deterministic 1.4.0 announcement draft for Figma release_004 in thread_008 authored by sarah.designer@company.com at 2024-08-23T16:30:00Z with subject 'Release 1.4.0 Announcement' and body 'Changelog and new components included.' validated via Google message_id relmsg_f9e9c1b6, with a label stance where release-draft is present as of 2024-08-23T16:35:00Z. The deliverable includes the set of threads discoverable under label dlp-flag.",
        actions=[
            Action(name="append_message_to_thread", kwargs={
                "thread_id": "thread_003",
                "from_email": "lisa.marketing@company.com",
                "body": "Temporary password is abcd-1234. Rotate after testing.",
                "created_ts": "2024-08-23T09:00:00Z"
            }),
            Action(name="dlp_scan_and_label_thread", kwargs={
                "thread_id": "thread_003",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-23T09:05:00Z"
            }),
            Action(name="compose_release_email_draft", kwargs={
                "release_id": "release_004",
                "thread_id": "thread_008",
                "from_email": "sarah.designer@company.com",
                "created_ts": "2024-08-23T16:30:00Z",
                "subject": "Release 1.4.0 Announcement",
                "body": "Changelog and new components included."
            }),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_f9e9c1b6"}),
            Action(name="update_thread_labels", kwargs={
                "thread_id": "thread_008",
                "add_labels": ["release-draft"],
                "remove_labels": [],
                "changed_ts": "2024-08-23T16:35:00Z"
            }),
            Action(name="search_gmail_threads", kwargs={"label": "dlp-flag"})
        ],
        outputs=[
            "[\n  {\n    \"thread_id\": \"thread_003\",\n    \"subject\": \"Marketing Website Launch Approval\",\n    \"current_labels\": [\n      \"marketing\",\n      \"approval\",\n      \"launch\",\n      \"dlp-flag\"\n    ],\n    \"updated_ts\": \"2024-08-23T09:05:00Z\"\n  }\n]"
        ],
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="EXP_23",
        instruction="You are the review-provenance steward ensuring database state alignment across the Figma↔Gmail workflow. Document—without prescribing steps—an audit-ready snapshot confirming: the review for artifact art_004 created at 2024-08-23T13:00:00Z under cycle_1dc59e3f; its association to thread_003 effective 2024-08-23T13:05:00Z; two verbatim Gmail messages—lisa.marketing@company.com “Looks good—LGTM from marketing.” at 2024-08-23T13:10:00Z and alex.dev@company.com “Please REVISE the grid spacing to 8px multiples.” at 2024-08-23T13:15:00Z—captured with authors/timestamps/bodies; and Gmail intent tallies synchronized to cycle_1dc59e3f. Represent DB modifications only as settled facts. Output only the exported assets for art_001 as the stable handoff reference.",
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_003", "from_email": "lisa.marketing@company.com", "body": "Looks good—LGTM from marketing.", "created_ts": "2024-08-23T13:10:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_003", "from_email": "alex.dev@company.com", "body": "Please REVISE the grid spacing to 8px multiples.", "created_ts": "2024-08-23T13:15:00Z"}),
            Action(name="sync_gmail_intents_to_review", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """[
    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ]
    ),

    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="EXP_24",
        instruction=(
            "You are the review-provenance steward ensuring signal alignment and label hygiene across the Figma↔Gmail workflow. "
            "Deliver an audit-ready record (facts, not procedures) confirming: the art_004 review created at 2024-08-23T13:00:00Z under cycle_1dc59e3f; "
            "its association to thread_003 effective 2024-08-23T13:05:00Z; the NEEDS_REVIEW state recorded at 2024-08-23T13:20:00Z; "
            "an APPROVED decision by alex.dev@company.com at 2024-08-23T13:25:00Z with comment 'LGTM'; "
            "a normalized conversation posture where Design/Approved is present and Design/Needs-Review is absent as of 2024-08-23T13:30:00Z; "
            "and the terminal log 'Review approved and labels aligned' captured at 2024-08-23T13:31:00Z. "
            "Provide the exported assets for art_001 as the stable handoff reference."
        ),
        actions=[
            Action(name="start_review_cycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="link_review_to_thread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="advance_review_status", kwargs={"cycle_id": "cycle_1dc59e3f", "new_status": "NEEDS_REVIEW", "changed_ts": "2024-08-23T13:20:00Z"}),
            Action(name="record_review_approval", kwargs={"cycle_id": "cycle_1dc59e3f", "approver_email": "alex.dev@company.com", "decision": "APPROVED", "decided_ts": "2024-08-23T13:25:00Z", "comment": "LGTM"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_003", "add_labels": ["Design/Approved"], "remove_labels": ["Design/Needs-Review"], "changed_ts": "2024-08-23T13:30:00Z"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-23T13:31:00Z", "message": "Review approved and labels aligned"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """[
    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ]
    ),


    # complexity_edges: 19
    Task(
        annotator="0",
        user_id="EXP_25",
        instruction=(
            "You are the safety-and-workflow posture coordinator for marketing updates, maintaining label hygiene and policy alignment. "
            "The audit-ready snapshot must evidence (without prescribing steps): thread_010 carries marketing and triaged as of 2024-08-24T18:20:00Z; "
            "the source conversation includes the exact memo 'Requires copy tweak on hero headline and UTM link validation' from lisa.marketing@company.com at 2024-08-24T18:22:00Z; "
            "a single safety evaluation occurred at 2024-08-24T18:23:00Z using dlp-flag only upon detection and governed by dlp_config; "
            "awareness of release_009 via its diff summary; the terminal note 'Posture confirmed for marketing updates' recorded at 2024-08-24T18:24:00Z; "
            "and the final label timestamp set at 2024-08-24T18:25:00Z. "
            "Provide the exported assets for art_001 as the stable reference for downstream stakeholders."
        ),
        actions=[
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_010", "add_labels": ["marketing", "triaged"], "remove_labels": [], "changed_ts": "2024-08-24T18:20:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_010", "from_email": "lisa.marketing@company.com", "body": "Requires copy tweak on hero headline and UTM link validation", "created_ts": "2024-08-24T18:22:00Z"}),
            Action(name="dlp_scan_and_label_thread", kwargs={"thread_id": "thread_010", "label_if_found": "dlp-flag", "changed_ts": "2024-08-24T18:23:00Z"}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_009"}),
            Action(name="read_system_config", kwargs={"config_key": "dlp_config"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-24T18:24:00Z", "message": "Posture confirmed for marketing updates"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_010", "add_labels": [], "remove_labels": [], "changed_ts": "2024-08-24T18:25:00Z"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """[
    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ]
    ),

    # complexity_edges: 14
    Task(
    annotator="0",
    user_id="EXP_26",
    instruction=(
        "You are the a11y preflight and workflow-hygiene coordinator for marketing surfaces, aligning Figma artifacts and Gmail posture. "
        "Document—without prescribing steps—an audit-ready snapshot that shows: FILE artifacts owned by lisa.marketing@company.com with tag website and modified on/after 2024-08-01T00:00:00Z as the scope; "
        "art_006 under an audit session of type COMBINED_DS_A11Y at 2024-08-24T14:00:00Z; a terminal note 'Preflight started for art_006' at 2024-08-24T14:02:00Z; "
        "the tag audit-in-progress present on art_006 effective 2024-08-24T14:03:00Z; and thread_010 carrying marketing and triaged as of 2024-08-24T14:05:00Z. "
        "Provide exported assets for art_001 as the stable handoff reference."
    ),
    actions=[
    Action(name="list_artifacts", kwargs={"owner_email": "lisa.marketing@company.com", "tag": "website", "artifact_type": "FILE", "modified_since": "2024-08-01T00:00:00Z"}),
    Action(name="create_audit_session", kwargs={"artifact_id": "art_006", "created_ts": "2024-08-24T14:00:00Z", "audit_type": "COMBINED_DS_A11Y"}),
    Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-24T14:02:00Z", "message": "Preflight started for art_006"}),
    Action(name="add_artifact_tag", kwargs={"artifact_id": "art_006", "tag": "audit-in-progress", "changed_ts": "2024-08-24T14:03:00Z"}),
    Action(name="update_thread_labels", kwargs={"thread_id": "thread_010", "add_labels": ["marketing", "triaged"], "remove_labels": [], "changed_ts": "2024-08-24T14:05:00Z"}),
    Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
    ],
    outputs=[
    """[
    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ],
    ),

    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="EXP_27",
        instruction=(
            "You are the end-to-end release-communications steward, enforcing lineage, attachment guardrails, and deterministic closeout within the release/ catalog. "
            "Record a non-procedural, audit-ready snapshot that confirms: Figma release_001 under the release/ lineage with its authoritative diff; "
            "a draft in thread_006 from sarah.designer@company.com at 2024-08-22T17:00:00Z (subject 'Release 1.2.0 Announcement', body 'Highlights and changes included.'); "
            "attachment validation via Gmail message_id relmsg_9cc87e81; a conversation posture where Design/Release and announced are present and draft is absent as of 2024-08-22T17:06:30Z; "
            "the closeout memo 'Release comms drafted and announced.' at 2024-08-22T17:07:00Z; and a safety evaluation for thread_006 aligned to dlp_config. "
            "Return the exported assets for art_001 as the stable reference."
        ),
        actions=[
            Action(name="list_releases", kwargs={"version_prefix": "release/"}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "announced"], "remove_labels": ["draft"], "changed_ts": "2024-08-22T17:06:30Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_006", "from_email": "sarah.designer@company.com", "body": "Release comms drafted and announced.", "created_ts": "2024-08-22T17:07:00Z"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_006"}),
            Action(name="read_system_config", kwargs={"config_key": "dlp_config"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """[
    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ],
    ),

    # complexity_edges: 16
    Task(
        annotator="0",
        user_id="EXP_28",
        instruction="You are the brand-guidance provenance steward ensuring signal alignment and label hygiene across the Figma↔Gmail workflow (db-modification traceable) with safety alignment. Deliver an audit-ready record—facts, not procedures—confirming: governance inputs intent_keywords and dlp_config acknowledged; a canonical Figma note on art_012 by emma.brand@company.com at 2024-08-24T15:00:00Z anchored node-12:9 with body “Consolidate brand tokens to v3 palette.”; a Gmail coordination memo in thread_010 from lisa.marketing@company.com at 2024-08-24T15:05:00Z with body “Brand token rollout scheduled for next sprint.”; a conversation posture where marketing and figma-sync are present as of 2024-08-24T15:06:00Z; and a recorded DLP safety evaluation for thread_010. Provide exported assets for art_001 as the stable reference for release-comms alignment.",
        actions=[
            Action(name="read_system_config", kwargs={"config_key": "intent_keywords"}),
            Action(name="read_system_config", kwargs={"config_key": "dlp_config"}),
            Action(name="create_figma_comment", kwargs={"artifact_id": "art_012", "author_email": "emma.brand@company.com", "body": "Consolidate brand tokens to v3 palette.", "anchor_ref": "node-12:9", "created_ts": "2024-08-24T15:00:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_010", "from_email": "lisa.marketing@company.com", "body": "Brand token rollout scheduled for next sprint.", "created_ts": "2024-08-24T15:05:00Z"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_010", "add_labels": ["marketing", "figma-sync"], "remove_labels": [], "changed_ts": "2024-08-24T15:06:00Z"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_010"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """[
    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ],
    ),


    # complexity_edges: 19
    Task(
        annotator="0",
        user_id="EXP_29",
        instruction="You are the release-communications steward operating within the Figma↔Gmail workflow under the release/ lineage and attachment guardrails. Provide a non-procedural, audit-ready snapshot whose evidence shows the following facts (without prescribing how they were produced): release_001 is treated as the authoritative diff within the release/ catalog; a deterministic draft exists in thread_006 from sarah.designer@company.com at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.'; attachment-policy compliance is evidenced via message_id relmsg_9cc87e81; the conversation posture reflects db modification Design/Release and announced present and draft absent as of 2024-08-22T17:06:00Z; the closing note 'APPROVE rollout.' is recorded at 2024-08-22T17:07:00Z; and a safety evaluation is on record for thread_006. Include the exported assets tied to art_001 as the stable reference.",
        actions=[
            Action(name="list_releases", kwargs={"version_prefix": "release/"}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="update_thread_labels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "announced"], "remove_labels": ["draft"], "changed_ts": "2024-08-22T17:06:00Z"}),
            Action(name="append_message_to_thread", kwargs={"thread_id": "thread_006", "from_email": "sarah.designer@company.com", "body": "APPROVE rollout.", "created_ts": "2024-08-22T17:07:00Z"}),
            Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_006"}),
            Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[
            """[
    {
    "asset_id": "asset_001",
    "profile": null,
    "file_name": null,
    "mime_type": null
    },
    {
    "asset_id": "asset_002",
    "profile": null,
    "file_name": null,
    "mime_type": null
    }
    ]"""
    ]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="EXP_30",
        instruction="You are the audit preparation and cleanup steward for art_006, documenting posture without prescribing steps. Deliver an audit-ready record whose evidence shows: design_system_mappings consulted; a COMBINED_DS_A11Y audit session for art_006 at 2024-08-24T13:00:00Z; the log 'Prep audit for marketing site' at 2024-08-24T13:02:00Z; tag a11y-queued present at 2024-08-24T13:03:00Z; tag audit-in-progress present at 2024-08-24T13:06:00Z; a11y-queued removed at 2024-08-24T13:19:00Z; audit-in-progress removed at 2024-08-24T13:20:00Z; the log 'Cleanup audit markers' at 2024-08-24T13:21:00Z; and the canonical artifact summary for art_006.",
        actions=[
            Action(name="read_system_config", kwargs={"config_key": "design_system_mappings"}),
            Action(name="create_audit_session", kwargs={"artifact_id": "art_006", "created_ts": "2024-08-24T13:00:00Z", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-24T13:02:00Z", "message": "Prep audit for marketing site"}),
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_006", "tag": "a11y-queued", "changed_ts": "2024-08-24T13:03:00Z"}),
            Action(name="add_artifact_tag", kwargs={"artifact_id": "art_006", "tag": "audit-in-progress", "changed_ts": "2024-08-24T13:06:00Z"}),
            Action(name="remove_artifact_tag", kwargs={"artifact_id": "art_006", "tag": "a11y-queued", "changed_ts": "2024-08-24T13:19:00Z"}),
            Action(name="remove_artifact_tag", kwargs={"artifact_id": "art_006", "tag": "audit-in-progress", "changed_ts": "2024-08-24T13:20:00Z"}),
            Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-24T13:21:00Z", "message": "Cleanup audit markers"}),
            Action(name="get_artifact_summary", kwargs={"artifact_id": "art_006"}),
        ],
        outputs=[
            """{
    "artifact_id": "art_006",
    "artifact_name": "Marketing Website",
    "artifact_type": "FILE",
    "owner_email": "lisa.marketing@company.com",
    "deep_link": "https://www.figma.com/file/def456ghi789/Marketing-Website",
    "current_tags": [
    "marketing",
    "website",
    "landing-pages"
    ],
    "modified_ts": "2024-08-24T13:20:00Z"
    }"""
    ]
    ),

#     ### BACKUP TASKS ####
#     #####################
    # # complexity_edges:  18
    # Task(
    #     annotator="0",
    #     user_id="EXP_43",
    #     instruction="You are the safety-and-workflow posture coordinator for marketing updates on thread_010, operating with DLP and intent awareness. Provide a non-procedural, audit-ready record that shows: labels marketing and triaged present on thread_010 effective 2024-08-24T18:20:00Z; a memo from lisa.marketing@company.com recorded at 2024-08-24T18:22:00Z with exact body 'Requires copy tweak on hero headline and UTM link validation'; a DLP evaluation at 2024-08-24T18:23:00Z that applies label dlp-flag only upon detection; awareness of release_009 via its diff summary; dlp_config and intent_keywords consulted; the terminal log 'DLP posture recorded' at 2024-08-24T18:26:00Z; label safety/checked present at 2024-08-24T18:27:00Z with a no-op confirmation at 2024-08-24T18:28:00Z; and the exported assets for art_001 as the stable reference.",
    #     actions=[
    #         Action(name="update_thread_labels", kwargs={"thread_id": "thread_010", "add_labels": ["marketing", "triaged"], "remove_labels": [], "changed_ts": "2024-08-24T18:20:00Z"}),
    #         Action(name="append_message_to_thread", kwargs={"thread_id": "thread_010", "from_email": "lisa.marketing@company.com", "body": "Requires copy tweak on hero headline and UTM link validation", "created_ts": "2024-08-24T18:22:00Z"}),
    #         Action(name="dlp_scan_and_label_thread", kwargs={"thread_id": "thread_010", "label_if_found": "dlp-flag", "changed_ts": "2024-08-24T18:23:00Z"}),
    #         Action(name="get_release_diff_summary", kwargs={"release_id": "release_009"}),
    #         Action(name="read_system_config", kwargs={"config_key": "dlp_config"}),
    #         Action(name="read_system_config", kwargs={"config_key": "intent_keywords"}),
    #         Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-24T18:26:00Z", "message": "DLP posture recorded"}),
    #         Action(name="update_thread_labels", kwargs={"thread_id": "thread_010", "add_labels": ["safety/checked"], "remove_labels": [], "changed_ts": "2024-08-24T18:27:00Z"}),
    #         Action(name="update_thread_labels", kwargs={"thread_id": "thread_010", "add_labels": [], "remove_labels": [], "changed_ts": "2024-08-24T18:28:00Z"}),
    #         Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
    #     ],
    #     outputs=[
    #         """[
    # {
    # "asset_id": "asset_001",
    # "profile": null,
    # "file_name": null,
    # "mime_type": null
    # },
    # {
    # "asset_id": "asset_002",
    # "profile": null,
    # "file_name": null,
    # "mime_type": null
    # }
    # ]"""
    # ]
    # ),

    # # complexity_edges: 17
    # Task(
    #     annotator="0",
    #     user_id="EXP_44",
    #     instruction="You are the guarded release-communications coordinator operating under the release/ lineage with attachment and DLP guardrails. Provide a non-procedural, audit-ready snapshot confirming: releases discoverable with version_prefix 'release/'; release_001 validated via its diff summary; a draft in thread_006 from sarah.designer@company.com at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.'; attachment policy validation via Gmail relmsg_9cc87e81; a conversation posture where Design/Release and announced are present and draft is absent as of 2024-08-22T17:06:00Z; the closing note 'APPROVE rollout.' at 2024-08-22T17:07:00Z; a DLP scan on thread_006 with the terminal log 'DLP scan complete' at 2024-08-22T17:08:00Z; and the exported Figma assets for art_001 as the stable reference.",
    #     actions=[
    #         Action(name="list_releases", kwargs={"version_prefix": "release/"}),
    #         Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
    #         Action(name="compose_release_email_draft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "sarah.designer@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
    #         Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_9cc87e81"}),
    #         Action(name="update_thread_labels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "announced"], "remove_labels": ["draft"], "changed_ts": "2024-08-22T17:06:00Z"}),
    #         Action(name="append_message_to_thread", kwargs={"thread_id": "thread_006", "from_email": "sarah.designer@company.com", "body": "APPROVE rollout.", "created_ts": "2024-08-22T17:07:00Z"}),
    #         Action(name="dlp_scan_thread", kwargs={"thread_id": "thread_006"}),
    #         Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-22T17:08:00Z", "message": "DLP scan complete"}),
    #         Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
    #     ],
    #     outputs=[
    #         """[
    # {
    # "asset_id": "asset_001",
    # "profile": null,
    # "file_name": null,
    # "mime_type": null
    # },
    # {
    # "asset_id": "asset_002",
    # "profile": null,
    # "file_name": null,
    # "mime_type": null
    # }
    # ]"""
    # ]
    # ),


    # # complexity_edges: 17
    # Task(
    #     annotator="0",
    #     user_id="EXP_45",
    #     instruction="You are the cross-surface provenance steward coordinating a deterministic brand note within review governance. Provide an audit-ready, non-procedural record that demonstrates: a review for art_003 created at 2024-08-23T12:45:00Z (cycle_7a255cf0) and associated with thread_001 at 2024-08-23T12:50:00Z; status NEEDS_REVIEW effective 2024-08-23T12:55:00Z; a stakeholder nudge captured in thread_001 from emma.brand@company.com at 2024-08-23T12:58:00Z with body 'Brand guidance incoming.'; a label stance where Brand/Review is present and urgent absent as of 2024-08-23T12:59:00Z; a brand comment on Figma art_003 by emma.brand@company.com anchored node-2:7 at 2024-08-23T12:00:00Z with body 'Please update the brand color token to Brand/Primary/600.'; and the author-scoped Figma comment list for artifact_id art_003 filtered to author_email emma.brand@company.com since 2024-08-01T00:00:00Z.",
    #     actions=[
    #         Action(name="start_review_cycle", kwargs={"artifact_id": "art_003", "created_ts": "2024-08-23T12:45:00Z"}),
    #         Action(name="link_review_to_thread", kwargs={"cycle_id": "cycle_7a255cf0", "thread_id": "thread_001", "changed_ts": "2024-08-23T12:50:00Z"}),
    #         Action(name="advance_review_status", kwargs={"cycle_id": "cycle_7a255cf0", "new_status": "NEEDS_REVIEW", "changed_ts": "2024-08-23T12:55:00Z"}),
    #         Action(name="append_message_to_thread", kwargs={"thread_id": "thread_001", "from_email": "emma.brand@company.com", "body": "Brand guidance incoming.", "created_ts": "2024-08-23T12:58:00Z"}),
    #         Action(name="update_thread_labels", kwargs={"thread_id": "thread_001", "add_labels": ["Brand/Review"], "remove_labels": ["urgent"], "changed_ts": "2024-08-23T12:59:00Z"}),
    #         Action(name="create_figma_comment", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
    #         Action(name="list_figma_comments", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "since_ts": "2024-08-01T00:00:00Z"}),
    #     ],
    #     outputs=[
    #         """[
    # {
    # "comment_id": "cmt_10b86546",
    # "author_email": "emma.brand@company.com",
    # "anchor_ref": "node-2:7",
    # "body": "Please update the brand color token to Brand/Primary/600.",
    # "created_ts": "2024-08-23T12:00:00Z"
    # }
    # ]"""
    # ]
    # ),

#     # # complexity_edges: 13
#     # Task(
#     #     annotator="0",
#     #     user_id="EXP_46",
#     #     instruction="You own accessibility feedback coordination for the admin panel header. Target state: an active design-review conversation in Gmail (label “design-review”, participant alex.dev@company.com, keyword “Design”); art_003 carries a canonical note by emma.brand@company.com at 2024-08-26T10:00:00Z anchored node-3:header with body “Add ARIA labels and keyboard navigation support.”; thread_001 posture shows a11y and figma-sync present and urgent absent with changed_ts 2024-08-26T10:00:00Z; a kickoff message from alex.dev@company.com at 2024-08-26T10:01:00Z with body “Accessibility improvements in progress - adding ARIA labels and keyboard navigation support”; and exported assets for art_001 as handoff evidence. Use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support or similar.",
#     #     actions=[
#     #         Action(name="search_gmail_threads", kwargs={"label": "design-review", "participant": "alex.dev@company.com", "keyword": "Design"}),
#     #         Action(name="create_figma_comment", kwargs={"artifact_id": "art_003", "author_email": "emma.brand@company.com", "body": "Add ARIA labels and keyboard navigation support.", "anchor_ref": "node-3:header", "created_ts": "2024-08-26T10:00:00Z"}),
#     #         Action(name="update_thread_labels", kwargs={"thread_id": "thread_001", "add_labels": ["a11y", "figma-sync"], "remove_labels": ["urgent"], "changed_ts": "2024-08-26T10:00:00Z"}),
#     #         Action(name="append_message_to_thread", kwargs={"thread_id": "thread_001", "from_email": "alex.dev@company.com", "body": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "created_ts": "2024-08-26T10:01:00Z"}),
#     #         Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_001"}),
#     #     ],
#     #     outputs=[
#     #     """[
#     #     {
#     #     "asset_id": "asset_001",
#     #     "profile": null,
#     #     "file_name": null,
#     #     "mime_type": null
#     #     },
#     #     {
#     #     "asset_id": "asset_002",
#     #     "profile": null,
#     #     "file_name": null,
#     #     "mime_type": null
#     #     }
#     #     ]"""
#     #     ]
#     # ),

#     # # complexity_edges: 14
#     # Task(
#     # annotator="0",
#     # user_id="EXP_47",
#     # instruction="You own settings-screen accessibility and brand guidance with FRAME scope. Target state: FRAME artifacts covered for owner mike.ux@company.com tagged “revise” modified_since 2024-08-01T00:00:00Z; export availability evidenced by assets for art_012; a brand note on art_012 by emma.brand@company.com at 2024-08-28T09:00:00Z anchored node-12:1 with body “Align tokens with brand v3.”; thread_010 labels show a11y and triaged present and design removed with changed_ts 2024-08-28T09:02:00Z; audit narrative “Brand v3 guidance posted for settings screen” at 2024-08-28T09:03:00Z; authoritative reference is the canonical artifact summary for art_012.",
#     # actions=[
#     #     Action(name="list_artifacts", kwargs={
#     #     "owner_email": "mike.ux@company.com",
#     #     "tag": "revise",
#     #     "artifact_type": "FRAME",
#     #     "modified_since": "2024-08-01T00:00:00Z"
#     #     }),
#     #     Action(name="list_assets_for_artifact", kwargs={"artifact_id": "art_012"}),
#     #     Action(name="create_figma_comment", kwargs={
#     #     "artifact_id": "art_012",
#     #     "author_email": "emma.brand@company.com",
#     #     "body": "Align tokens with brand v3.",
#     #     "anchor_ref": "node-12:1",
#     #     "created_ts": "2024-08-28T09:00:00Z"
#     #     }),
#     #     Action(name="update_thread_labels", kwargs={
#     #     "thread_id": "thread_010",
#     #     "add_labels": ["a11y", "triaged"],
#     #     "remove_labels": ["design"],
#     #     "changed_ts": "2024-08-28T09:02:00Z"
#     #     }),
#     #     Action(name="log_terminal_event", kwargs={
#     #     "log_ts": "2024-08-28T09:03:00Z",
#     #     "message": "Brand v3 guidance posted for settings screen"
#     #     }),
#     #     Action(name="get_artifact_summary", kwargs={"artifact_id": "art_012"}),
#     # ],
#     # outputs=[
#     # """{
#     # "artifact_id": "art_012",
#     # "artifact_name": "Settings Screen",
#     # "artifact_type": "FRAME",
#     # "owner_email": "mike.ux@company.com
#     # ",
#     # "deep_link": "https://www.figma.com/file/xyz789ghi012/Mobile-App?node-id=2%3A4
#     # ",
#     # "current_tags": [
#     # "settings",
#     # "mobile",
#     # "app",
#     # "revise"
#     # ],
#     # "modified_ts": "2024-08-23T10:30:00Z"
#     # }"""
#     # ]
#     # ),

#     # # complexity_edges: 13
#     # Task(
#     #     annotator="0",
#     #     user_id="HARD_401",
#     #     instruction=(
#     #         "You own a11y preparation hygiene for the marketing website FILE scope. "
#     #         "The audit-ready snapshot should evidence: FILE artifacts for owner lisa.marketing@company.com tagged website and modified on/after 2024-08-01T00:00:00Z confirming art_006; "
#     #         "for art_006, an audit-in-progress lifecycle with the tag present at 2024-08-28T13:00:00Z, a preparation note “Prepared audit for art_006” at 2024-08-28T13:05:00Z, and the tag cleared at 2024-08-28T13:20:00Z. "
#     #         "Return the canonical artifact summary for art_006."
#     #     ),
#     #     actions=[
#     #         Action(name="list_artifacts", kwargs={"owner_email": "lisa.marketing@company.com", "tag": "website", "artifact_type": "FILE", "modified_since": "2024-08-01T00:00:00Z"}),
#     #         Action(name="add_artifact_tag", kwargs={"artifact_id": "art_006", "tag": "audit-in-progress", "changed_ts": "2024-08-28T13:00:00Z"}),
#     #         Action(name="log_terminal_event", kwargs={"log_ts": "2024-08-28T13:05:00Z", "message": "Prepared audit for art_006"}),
#     #         Action(name="remove_artifact_tag", kwargs={"artifact_id": "art_006", "tag": "audit-in-progress", "changed_ts": "2024-08-28T13:20:00Z"}),
#     #         Action(name="get_artifact_summary", kwargs={"artifact_id": "art_006"}),
#     #     ],
#     #     outputs=[
#     #     """{
#     #     "artifact_id": "art_006",
#     #     "artifact_name": "Marketing Website",
#     #     "artifact_type": "FILE",
#     #     "owner_email": "lisa.marketing@company.com",
#     #     "deep_link": "https://www.figma.com/file/def456ghi789/Marketing-Website",
#     #     "current_tags": [
#     #     "marketing",
#     #     "website",
#     #     "landing-pages"
#     #     ],
#     #     "modified_ts": "2024-08-28T13:20:00Z"
#     #     }"""
#     #     ]
#     # ),

#     # # complexity_edges: 13
#     # Task(
#     #     annotator="0",
#     #     user_id="HARD_402",
#     #     instruction=(
#     #         "You own release-communications readiness for the design system under the release/ lineage. "
#     #         "The audit-ready snapshot should evidence: lineage discoverability via version_prefix “release/”; "
#     #         "for release_001, a draft in thread_006 from sarah.designer@company.com created at 2024-08-28T11:00:00Z with subject “Release 1.2.0 Announcement” and body “Highlights and changes included.” validated against attachment policy using message_id relmsg_0d5cb1ea; "
#     #         "thread posture where Design/Release and announced are present and draft is absent with changed_ts 2024-08-28T11:05:00Z. "
#     #         "Return the diff summary for release_001."
#     #     ),
#     #     actions=[
#     #         Action(name="list_releases", kwargs={"version_prefix": "release/"}),
#     #         Action(name="compose_release_email_draft", kwargs={
#     #         "release_id": "release_001",
#     #         "thread_id": "thread_006",
#     #         "from_email": "sarah.designer@company.com",
#     #         "created_ts": "2024-08-28T11:00:00Z",
#     #         "subject": "Release 1.2.0 Announcement",
#     #         "body": "Highlights and changes included."
#     #         }),
#     #         Action(name="guard_attachment_policy_on_draft", kwargs={"message_id": "relmsg_0d5cb1ea"}),
#     #         Action(name="update_thread_labels", kwargs={
#     #         "thread_id": "thread_006",
#     #         "add_labels": ["Design/Release", "announced"],
#     #         "remove_labels": ["draft"],
#     #         "changed_ts": "2024-08-28T11:05:00Z"
#     #         }),
#     #         Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
#     #     ],
#     #     outputs=[
#     #     """{
#     #     "release_id": "release_001",
#     #     "added": 0,
#     #     "updated": 0,
#     #     "removed": 0
#     #     }"""
#     #     ]
#     # ),

]
