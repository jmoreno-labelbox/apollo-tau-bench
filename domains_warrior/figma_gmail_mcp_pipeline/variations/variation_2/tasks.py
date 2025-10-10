from domains.dto import Action, Task

TASKS = [
    Task(
    annotator="0",
    user_id="task_01",
    instruction=(
        "You are 'sarah.designer@company.com' and you want to submit a review request for your frame by exporting a PNG 2x asset for that frame with filename 'hero-section-2x-r2.png'"
        "under gmail thread addressed to 'mike.ux@company.com', 'alex.dev@company.com', 'lisa.marketing@company.com'"
    ),
    actions=[
        Action(
            name="get_all_artifacts_of_type_with_tags_and_email",
            kwargs={"artifact_type": "FRAME", "owner_email":"sarah.designer@company.com", "tags":["needs-review"]},
        ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_001",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/hero-section-2x-r2.png"
        }),
        Action(name="create_new_cycle", kwargs={
            "artifact_id": "art_001",
            "sla_deadline_ts": "2024-08-28T12:30:00Z"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Design Review: hero-section-2x-r2.png",
            "sender_id": "sarah.designer@company.com",
            "recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"],
            "current_labels": ["Design/Needs-Review", "figma", "review"],
            "body_html": "<p>Review for the hero-section-2x-r2.png. See attachment.</p>",
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_013",
            "new_status": "NEEDS_REVIEW",
            "thread_id": "thread_015"
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Submitted for review",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
    ],
    outputs=[
        {
            "comment_id": "comment_019",
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Submitted for review",
            "source_message_id_nullable": "msg_017",
            "created_ts": "2024-08-23T12:00:00Z",
            "resolved_flag": False
        },
        # {
        #     "messages": [
        #         "2025-08-26T12:00:00Z : Asset 'asset_019' (PNG 2x) exported for artifact 'art_001' → gs://company-assets/figma-exports/hero-section-2x-r2.png.",
        #         "2025-08-26T12:00:00Z : Review cycle 'cycle_013' created for 'art_001' with SLA deadline '2024-08-28T12:30:00Z'.",
        #         "2025-08-26T12:00:00Z : Email thread 'thread_015' started by sarah.designer@company.com with subject 'Design Review: Homepage Hero Section (Round 2)'.",
        #         "2025-08-26T12:00:00Z : Message 'msg_017' posted with attachment 'asset_019'.",
        #         "2025-08-26T15:00:00Z : Cycle 'cycle_013' status set to NEEDS_REVIEW and linked to thread 'thread_015'.",
        #         "2025-08-26T12:00:00Z : Comment 'comment_019' added on 'art_001' referencing message 'msg_017'.",
        #         "2025-08-27T12:30:00Z : Approval 'approval_012' recorded by mike.ux@company.com; cycle 'cycle_013' set to APPROVED."
        #     ]
        # }
    ]
),
Task(
    annotator="0",
    user_id="task_02",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Design Review: Homepage Hero Section'  with message 'Good Job' for asset 'asset_001'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_03",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_04",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_05",
    instruction=(
        "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 2x asset for that frame with filename 'pricing-page-2x-r2.png' "
        "under gmail thread addressed to 'sarah.designer@company.com', 'mike.ux@company.com'"
    ),
    actions=[
        Action(
            name="get_all_artifacts_of_type_with_tags_and_email",
            kwargs={"artifact_type": "FRAME", "owner_email": "lisa.marketing@company.com", "tags": ["needs-review"]},
        ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_007",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/pricing-page-2x-r2.png"
        }),
        Action(name="create_new_cycle", kwargs={
            "artifact_id": "art_007",
            "sla_deadline_ts": "2024-08-28T12:30:00Z"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Design Review: pricing-page-2x-r2.png",
            "sender_id": "lisa.marketing@company.com",
            "recipients": ["sarah.designer@company.com", "mike.ux@company.com"],
            "current_labels": ["Design/Needs-Review", "figma", "review"],
            "body_html": "<p>Review for the pricing-page-2x-r2.png. See attachment.</p>",
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_013",
            "new_status": "NEEDS_REVIEW",
            "thread_id": "thread_015"
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_007",
            "author_email": "lisa.marketing@company.com",
            "content": "Submitted for review",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_013",
            "artifact_id": "art_007",
            "thread_id_nullable": "thread_015",
            "status": "NEEDS_REVIEW",
            "created_ts": "2024-08-23T12:00:00Z",
            "sla_deadline_ts": "2024-08-28T12:30:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_06",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_07",
    instruction=(
        "You are 'mike.ux@company.com' and you need to review for 'Admin Panel Accessibility Audit' is past SLA — request changes in the existing thread with message 'SLA breached; please prioritize fixes and resubmit'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(
            name="get_complete_email_thread",
            kwargs={"thread_id":"thread_004"},
        ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: SLA breached; please prioritize fixes and resubmit</p>",
            "attachments_asset_ids": ["asset_007"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_004",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_004",
            "escalated_ts": "2024-08-23T12:00:00Z"
        })
    ],
    outputs=[
        {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-23T12:00:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_08",
    instruction=(
        "You are 'mike.ux@company.com'. Publish release notes for 'Design System v1.3.0 - Form Components & Accessibility' "
        "to the existing release thread, including PNG 3x exports for newly added frames, "
        "and list the changed frames from the release diff."
    ),
    actions=[
        Action(name="get_release_details_by_name", kwargs={
            "release_name": "Design System v1.3.0 - Form Components & Accessibility"
        }),
        Action(name="get_release_diff_by_release_id", kwargs={
            "release_id": "release_011"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:5",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:5.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:5.png"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_014",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:6.png"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:7",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:7.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_015",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:7.png"
        }),
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes",
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_013",
            "body_html": (
                "<h2>Design System v1.3.0 - Form Components & Accessibility</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 1:5</li>"
                "<li>Added frame 1:6</li>"
                "<li>Added frame 1:7</li>"
                "<li>Updated frame 1:3</li>"
                "<li>Updated frame 1:4</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019", "asset_020", "asset_021"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_013",
            "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes",
            "sender_identity": "design-automation@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T11:15:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_017",
            "thread_id": "thread_013",
            "sender_email": "design-automation@company.com",
            "body_html": "<h2>Design System v1.3.0 - Form Components & Accessibility</h2><p>Highlights:</p><ul><li>Added frame 1:5</li><li>Added frame 1:6</li><li>Added frame 1:7</li><li>Updated frame 1:3</li><li>Updated frame 1:4</li></ul>",        
            "body_text_stripped": "Design System v1.3.0 - Form Components & Accessibility Highlights: Added frame 1:5, Added frame 1:6, Added frame 1:7, Updated frame 1:3, Updated frame 1:4,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019",
                "asset_020",
                "asset_021"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_09",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and updating frames '2:4' and '2:2' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": ["2:4", "2:2"],
            "frames_removed": [],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Updated 2 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Updated frame 2:4</li>"
                "<li>Updated frame 2:2</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_015",
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_identity": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T12:00:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_018",
            "thread_id": "thread_015",
            "sender_email": "mike.ux@company.com",
            "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
            "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Updated frame 2:2,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_10",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and removing frames '2:4' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": [],
            "frames_removed": ["2:4"],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Removed 1 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Removed frame 2:4</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_015",
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_identity": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T12:00:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_018",
            "thread_id": "thread_015",
            "sender_email": "mike.ux@company.com",
            "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
            "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Removed frame 2:4,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_11",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and updating frames '2:4' and removing '2:2' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": ["2:4"],
            "frames_removed": ["2:2"],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Updated 1 frames",
                "Removed 1 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Updated frame 2:4</li>"
                "<li>Removed frame 2:2</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
    {
        "thread": {
        "thread_id": "thread_015",
        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
        "sender_identity": "mike.ux@company.com",
        "recipients": [
            "stakeholders@company.com",
            "product-managers@company.com",
            "engineering-leads@company.com"
        ],
        "current_labels": [
            "Design/Release"
        ],
        "created_ts": "2024-08-23T12:00:00Z",
        "updated_ts": "2024-08-23T12:00:00Z"
        },
        "message": {
        "message_id": "msg_018",
        "thread_id": "thread_015",
        "sender_email": "mike.ux@company.com",
        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Removed frame 2:2,",
        "sent_ts": "2024-08-23T12:00:00Z",
        "attachments_asset_ids": [
            "asset_019"
        ]
        }
    }
    ]
),
Task(
    annotator="0",
    user_id="task_12",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_13",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_14",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
annotator="0",
user_id="task_15",
instruction=(
    "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 3x asset for that frame with filename 'hero-section-3x.png'"
    "under gmail thread addressed to 'sarah.designer@company.com' and 'mike.ux@company.com'"
),
actions=[
    Action(
        name="get_all_artifacts_of_type_with_tags_and_email",
        kwargs={"artifact_type": "FRAME", "owner_email":"lisa.marketing@company.com", "tags":["needs-review"]},
    ),
    Action(name="create_new_asset", kwargs={
        "artifact_id": "art_007",
        "export_profile": "PNG 3x",
        "file_size_bytes": 3000,
        "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
    }),
    Action(name="create_new_cycle", kwargs={
        "artifact_id": "art_007",
        "sla_deadline_ts": "2024-08-28T12:30:00Z"
    }),
    Action(name="start_email_thread", kwargs={
        "subject": "Design Review: hero-section-3x.png",
        "sender_id": "lisa.marketing@company.com",
        "recipients": ['sarah.designer@company.com','mike.ux@company.com'],
        "current_labels": ["Design/Needs-Review", "figma", "review"],
        "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
        "attachments_asset_ids": ["asset_019"]
    }),
    Action(name="update_cycle_status", kwargs={
        "cycle_id": "cycle_013",
        "new_status": "NEEDS_REVIEW",
        "thread_id": "thread_015"
    }),
    Action(name="add_comment", kwargs={
        "artifact_id": "art_007",
        "author_email": "lisa.marketing@company.com",
        "content": "Submitted for review",
        "source_message_id": "msg_017",
        "resolved_flag": False
    }),
],
outputs=[
    {
                                                                    "comment_id": "comment_019",
                                                                    "artifact_id": "art_007",
                                                                    "author_email": "lisa.marketing@company.com",
                                                                    "content": "Submitted for review",
                                                                    "source_message_id_nullable": "msg_017",
                                                                    "created_ts": "2024-08-23T12:00:00Z",
                                                                    "resolved_flag": False
                                                                },
    {
                                                                    "cycle_id": "cycle_013",
                                                                    "artifact_id": "art_007",
                                                                    "thread_id_nullable": "thread_015",
                                                                    "status": "NEEDS_REVIEW",
                                                                    "created_ts": "2024-08-23T12:00:00Z",
                                                                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                                                                    "sla_breached_flag": False,
                                                                    "escalated_ts_nullable": None
                                                                }
]
),
Task(
    annotator="0",
    user_id="task_16",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Design Review: Homepage Hero Section'  with message 'Good Job' for asset 'asset_001'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_17",
    instruction=(
        "You are 'sarah.designer@company.com' and you want to submit a review request for your frame by exporting a PNG 1x asset for that frame with filename 'hero-section-2x-r2.png'"
        "under gmail thread addressed to 'mike.ux@company.com', 'lisa.marketing@company.com'"
    ),
    actions=[
        Action(
            name="get_all_artifacts_of_type_with_tags_and_email",
            kwargs={"artifact_type": "FRAME", "owner_email":"sarah.designer@company.com", "tags":["needs-review"]},
        ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_001",
            "export_profile": "PNG 1x",
            "file_size_bytes": 1000,
            "storage_ref": "gs://company-assets/figma-exports/hero-section-2x-r2.png"
        }),
        Action(name="create_new_cycle", kwargs={
            "artifact_id": "art_001",
            "sla_deadline_ts": "2024-08-28T12:30:00Z"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Design Review: hero-section-2x-r2.png",
            "sender_id": "sarah.designer@company.com",
            "recipients": ["mike.ux@company.com", "lisa.marketing@company.com"],
            "current_labels": ["Design/Needs-Review", "figma", "review"],
            "body_html": "<p>Review for the hero-section-2x-r2.png. See attachment.</p>",
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_013",
            "new_status": "NEEDS_REVIEW",
            "thread_id": "thread_015"
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Submitted for review",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
    ],
    outputs=[
        {
            "comment_id": "comment_019",
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Submitted for review",
            "source_message_id_nullable": "msg_017",
            "created_ts": "2024-08-23T12:00:00Z",
            "resolved_flag": False
        },

    ]
),
Task(
    annotator="0",
    user_id="task_18",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Design Review: Homepage Hero Section'  with message 'Good Job' for asset 'asset_001'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_19",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_20",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_21",
    instruction=(
        "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 2x asset for that frame with filename 'pricing-page-2x-r2.png' "
        "under gmail thread addressed to 'sarah.designer@company.com', 'mike.ux@company.com'"
    ),
    actions=[
        Action(
            name="get_all_artifacts_of_type_with_tags_and_email",
            kwargs={"artifact_type": "FRAME", "owner_email": "lisa.marketing@company.com", "tags": ["needs-review"]},
        ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_007",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/pricing-page-2x-r2.png"
        }),
        Action(name="create_new_cycle", kwargs={
            "artifact_id": "art_007",
            "sla_deadline_ts": "2024-08-28T12:30:00Z"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Design Review: pricing-page-2x-r2.png",
            "sender_id": "lisa.marketing@company.com",
            "recipients": ["sarah.designer@company.com", "mike.ux@company.com"],
            "current_labels": ["Design/Needs-Review", "figma", "review"],
            "body_html": "<p>Review for the pricing-page-2x-r2.png. See attachment.</p>",
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_013",
            "new_status": "NEEDS_REVIEW",
            "thread_id": "thread_015"
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_007",
            "author_email": "lisa.marketing@company.com",
            "content": "Submitted for review",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_013",
            "artifact_id": "art_007",
            "thread_id_nullable": "thread_015",
            "status": "NEEDS_REVIEW",
            "created_ts": "2024-08-23T12:00:00Z",
            "sla_deadline_ts": "2024-08-28T12:30:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_22",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_23",
    instruction=(
        "You are 'mike.ux@company.com' and you need to review for 'Admin Panel Accessibility Audit' is past SLA — request changes in the existing thread with message 'SLA breached; please prioritize fixes and resubmit'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(
            name="get_complete_email_thread",
            kwargs={"thread_id":"thread_004"},
        ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: SLA breached; please prioritize fixes and resubmit</p>",
            "attachments_asset_ids": ["asset_007"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_004",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_004",
            "escalated_ts": "2024-08-23T12:00:00Z"
        })
    ],
    outputs=[
        {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-23T12:00:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_24",
    instruction=(
        "You are 'mike.ux@company.com'. Publish release notes for 'Design System v1.3.0 - Form Components & Accessibility' "
        "to the existing release thread, including PNG 3x exports for newly added frames, "
        "and list the changed frames from the release diff."
    ),
    actions=[
        Action(name="get_release_details_by_name", kwargs={
            "release_name": "Design System v1.3.0 - Form Components & Accessibility"
        }),
        Action(name="get_release_diff_by_release_id", kwargs={
            "release_id": "release_011"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:5",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:5.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:5.png"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_014",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:6.png"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:7",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:7.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_015",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:7.png"
        }),
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes",
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_013",
            "body_html": (
                "<h2>Design System v1.3.0 - Form Components & Accessibility</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 1:5</li>"
                "<li>Added frame 1:6</li>"
                "<li>Added frame 1:7</li>"
                "<li>Updated frame 1:3</li>"
                "<li>Updated frame 1:4</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019", "asset_020", "asset_021"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_013",
            "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes",
            "sender_identity": "design-automation@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T11:15:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_017",
            "thread_id": "thread_013",
            "sender_email": "design-automation@company.com",
            "body_html": "<h2>Design System v1.3.0 - Form Components & Accessibility</h2><p>Highlights:</p><ul><li>Added frame 1:5</li><li>Added frame 1:6</li><li>Added frame 1:7</li><li>Updated frame 1:3</li><li>Updated frame 1:4</li></ul>",        
            "body_text_stripped": "Design System v1.3.0 - Form Components & Accessibility Highlights: Added frame 1:5, Added frame 1:6, Added frame 1:7, Updated frame 1:3, Updated frame 1:4,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019",
                "asset_020",
                "asset_021"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_25",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and updating frames '2:4' and '2:2' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": ["2:4", "2:2"],
            "frames_removed": [],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Updated 2 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Updated frame 2:4</li>"
                "<li>Updated frame 2:2</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_015",
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_identity": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T12:00:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_018",
            "thread_id": "thread_015",
            "sender_email": "mike.ux@company.com",
            "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
            "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Updated frame 2:2,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_26",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and removing frames '2:4' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": [],
            "frames_removed": ["2:4"],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Removed 1 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Removed frame 2:4</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_015",
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_identity": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T12:00:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_018",
            "thread_id": "thread_015",
            "sender_email": "mike.ux@company.com",
            "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
            "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Removed frame 2:4,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_27",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and updating frames '2:4' and removing '2:2' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": ["2:4"],
            "frames_removed": ["2:2"],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Updated 1 frames",
                "Removed 1 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Updated frame 2:4</li>"
                "<li>Removed frame 2:2</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
    {
        "thread": {
        "thread_id": "thread_015",
        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
        "sender_identity": "mike.ux@company.com",
        "recipients": [
            "stakeholders@company.com",
            "product-managers@company.com",
            "engineering-leads@company.com"
        ],
        "current_labels": [
            "Design/Release"
        ],
        "created_ts": "2024-08-23T12:00:00Z",
        "updated_ts": "2024-08-23T12:00:00Z"
        },
        "message": {
        "message_id": "msg_018",
        "thread_id": "thread_015",
        "sender_email": "mike.ux@company.com",
        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Removed frame 2:2,",
        "sent_ts": "2024-08-23T12:00:00Z",
        "attachments_asset_ids": [
            "asset_019"
        ]
        }
    }
    ]
),
Task(
    annotator="0",
    user_id="task_28",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_29",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_30",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
annotator="0",
user_id="task_31",
instruction=(
    "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 3x asset for that frame with filename 'hero-section-3x.png'"
    "under gmail thread addressed to 'sarah.designer@company.com' and 'mike.ux@company.com'"
),
actions=[
    Action(
        name="get_all_artifacts_of_type_with_tags_and_email",
        kwargs={"artifact_type": "FRAME", "owner_email":"lisa.marketing@company.com", "tags":["needs-review"]},
    ),
    Action(name="create_new_asset", kwargs={
        "artifact_id": "art_007",
        "export_profile": "PNG 3x",
        "file_size_bytes": 3000,
        "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
    }),
    Action(name="create_new_cycle", kwargs={
        "artifact_id": "art_007",
        "sla_deadline_ts": "2024-08-28T12:30:00Z"
    }),
    Action(name="start_email_thread", kwargs={
        "subject": "Design Review: hero-section-3x.png",
        "sender_id": "lisa.marketing@company.com",
        "recipients": ['sarah.designer@company.com','mike.ux@company.com'],
        "current_labels": ["Design/Needs-Review", "figma", "review"],
        "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
        "attachments_asset_ids": ["asset_019"]
    }),
    Action(name="update_cycle_status", kwargs={
        "cycle_id": "cycle_013",
        "new_status": "NEEDS_REVIEW",
        "thread_id": "thread_015"
    }),
    Action(name="add_comment", kwargs={
        "artifact_id": "art_007",
        "author_email": "lisa.marketing@company.com",
        "content": "Submitted for review",
        "source_message_id": "msg_017",
        "resolved_flag": False
    }),
],
outputs=[
    {
            "comment_id": "comment_019",
            "artifact_id": "art_007",
            "author_email": "lisa.marketing@company.com",
            "content": "Submitted for review",
            "source_message_id_nullable": "msg_017",
            "created_ts": "2024-08-23T12:00:00Z",
            "resolved_flag": False
        },
    {
            "cycle_id": "cycle_013",
            "artifact_id": "art_007",
            "thread_id_nullable": "thread_015",
            "status": "NEEDS_REVIEW",
            "created_ts": "2024-08-23T12:00:00Z",
            "sla_deadline_ts": "2024-08-28T12:30:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
]
),
Task(
    annotator="0",
    user_id="task_32",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Design Review: Homepage Hero Section'  with message 'Good Job' for asset 'asset_001'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_33",
    instruction=(
        "You are 'sarah.designer@company.com' and you want to submit a review request for your frame by exporting a PNG 2x asset for that frame with filename 'hero-section-2x-r2.png'"
        "under gmail thread addressed to 'mike.ux@company.com', 'alex.dev@company.com', 'lisa.marketing@company.com'"
    ),
    actions=[
        Action(
            name="get_all_artifacts_of_type_with_tags_and_email",
            kwargs={"artifact_type": "FRAME", "owner_email":"sarah.designer@company.com", "tags":["needs-review"]},
        ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_001",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/hero-section-2x-r2.png"
        }),
        Action(name="create_new_cycle", kwargs={
            "artifact_id": "art_001",
            "sla_deadline_ts": "2024-08-28T12:30:00Z"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Design Review: hero-section-2x-r2.png",
            "sender_id": "sarah.designer@company.com",
            "recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"],
            "current_labels": ["Design/Needs-Review", "figma", "review"],
            "body_html": "<p>Review for the hero-section-2x-r2.png. See attachment.</p>",
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_013",
            "new_status": "NEEDS_REVIEW",
            "thread_id": "thread_015"
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Submitted for review",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
    ],
    outputs=[
        {
            "comment_id": "comment_019",
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Submitted for review",
            "source_message_id_nullable": "msg_017",
            "created_ts": "2024-08-23T12:00:00Z",
            "resolved_flag": False
        },

    ]
),
Task(
    annotator="0",
    user_id="task_34",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Design Review: Homepage Hero Section'  with message 'Good Job' for asset 'asset_001'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
    
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_35",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_36",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_37",
    instruction=(
        "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 2x asset for that frame with filename 'pricing-page-2x-r2.png' "
        "under gmail thread addressed to 'sarah.designer@company.com', 'mike.ux@company.com'"
    ),
    actions=[
        Action(
            name="get_all_artifacts_of_type_with_tags_and_email",
            kwargs={"artifact_type": "FRAME", "owner_email": "lisa.marketing@company.com", "tags": ["needs-review"]},
        ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_007",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/pricing-page-2x-r2.png"
        }),
        Action(name="create_new_cycle", kwargs={
            "artifact_id": "art_007",
            "sla_deadline_ts": "2024-08-28T12:30:00Z"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Design Review: pricing-page-2x-r2.png",
            "sender_id": "lisa.marketing@company.com",
            "recipients": ["sarah.designer@company.com", "mike.ux@company.com"],
            "current_labels": ["Design/Needs-Review", "figma", "review"],
            "body_html": "<p>Review for the pricing-page-2x-r2.png. See attachment.</p>",
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_013",
            "new_status": "NEEDS_REVIEW",
            "thread_id": "thread_015"
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_007",
            "author_email": "lisa.marketing@company.com",
            "content": "Submitted for review",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_013",
            "artifact_id": "art_007",
            "thread_id_nullable": "thread_015",
            "status": "NEEDS_REVIEW",
            "created_ts": "2024-08-23T12:00:00Z",
            "sla_deadline_ts": "2024-08-28T12:30:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_38",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_39",
    instruction=(
        "You are 'mike.ux@company.com' and you need to review for 'Admin Panel Accessibility Audit' is past SLA — request changes in the existing thread with message 'SLA breached; please prioritize fixes and resubmit'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(
            name="get_complete_email_thread",
            kwargs={"thread_id":"thread_004"},
        ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: SLA breached; please prioritize fixes and resubmit</p>",
            "attachments_asset_ids": ["asset_007"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_004",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_004",
            "escalated_ts": "2024-08-23T12:00:00Z"
        })
    ],
    outputs=[
        {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-23T12:00:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_40",
    instruction=(
        "You are 'mike.ux@company.com'. Publish release notes for 'Design System v1.3.0 - Form Components & Accessibility' "
        "to the existing release thread, including PNG 3x exports for newly added frames, "
        "and list the changed frames from the release diff."
    ),
    actions=[
        Action(name="get_release_details_by_name", kwargs={
            "release_name": "Design System v1.3.0 - Form Components & Accessibility"
        }),
        Action(name="get_release_diff_by_release_id", kwargs={
            "release_id": "release_011"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:5",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:5.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:5.png"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_014",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:6.png"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:7",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:7.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_015",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:7.png"
        }),
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes",
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_013",
            "body_html": (
                "<h2>Design System v1.3.0 - Form Components & Accessibility</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 1:5</li>"
                "<li>Added frame 1:6</li>"
                "<li>Added frame 1:7</li>"
                "<li>Updated frame 1:3</li>"
                "<li>Updated frame 1:4</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019", "asset_020", "asset_021"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_013",
            "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes",
            "sender_identity": "design-automation@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T11:15:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_017",
            "thread_id": "thread_013",
            "sender_email": "design-automation@company.com",
            "body_html": "<h2>Design System v1.3.0 - Form Components & Accessibility</h2><p>Highlights:</p><ul><li>Added frame 1:5</li><li>Added frame 1:6</li><li>Added frame 1:7</li><li>Updated frame 1:3</li><li>Updated frame 1:4</li></ul>",        
            "body_text_stripped": "Design System v1.3.0 - Form Components & Accessibility Highlights: Added frame 1:5, Added frame 1:6, Added frame 1:7, Updated frame 1:3, Updated frame 1:4,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019",
                "asset_020",
                "asset_021"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_41",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and updating frames '2:4' and '2:2' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": ["2:4", "2:2"],
            "frames_removed": [],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Updated 2 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Updated frame 2:4</li>"
                "<li>Updated frame 2:2</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_015",
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_identity": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T12:00:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_018",
            "thread_id": "thread_015",
            "sender_email": "mike.ux@company.com",
            "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
            "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Updated frame 2:2,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_42",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and removing frames '2:4' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": [],
            "frames_removed": ["2:4"],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Removed 1 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Removed frame 2:4</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_015",
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_identity": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T12:00:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_018",
            "thread_id": "thread_015",
            "sender_email": "mike.ux@company.com",
            "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
            "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Removed frame 2:4,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_43",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and updating frames '2:4' and removing '2:2' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": ["2:4"],
            "frames_removed": ["2:2"],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Updated 1 frames",
                "Removed 1 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Updated frame 2:4</li>"
                "<li>Removed frame 2:2</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
    {
        "thread": {
        "thread_id": "thread_015",
        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
        "sender_identity": "mike.ux@company.com",
        "recipients": [
            "stakeholders@company.com",
            "product-managers@company.com",
            "engineering-leads@company.com"
        ],
        "current_labels": [
            "Design/Release"
        ],
        "created_ts": "2024-08-23T12:00:00Z",
        "updated_ts": "2024-08-23T12:00:00Z"
        },
        "message": {
        "message_id": "msg_018",
        "thread_id": "thread_015",
        "sender_email": "mike.ux@company.com",
        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Removed frame 2:2,",
        "sent_ts": "2024-08-23T12:00:00Z",
        "attachments_asset_ids": [
            "asset_019"
        ]
        }
    }
    ]
),
Task(
    annotator="0",
    user_id="task_44",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_45",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_46",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
annotator="0",
user_id="task_47",
instruction=(
    "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 3x asset for that frame with filename 'hero-section-3x.png'"
    "under gmail thread addressed to 'sarah.designer@company.com' and 'mike.ux@company.com'"
),
actions=[
    Action(
        name="get_all_artifacts_of_type_with_tags_and_email",
        kwargs={"artifact_type": "FRAME", "owner_email":"lisa.marketing@company.com", "tags":["needs-review"]},
    ),
    Action(name="create_new_asset", kwargs={
        "artifact_id": "art_007",
        "export_profile": "PNG 3x",
        "file_size_bytes": 3000,
        "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
    }),
    Action(name="create_new_cycle", kwargs={
        "artifact_id": "art_007",
        "sla_deadline_ts": "2024-08-28T12:30:00Z"
    }),
    Action(name="start_email_thread", kwargs={
        "subject": "Design Review: hero-section-3x.png",
        "sender_id": "lisa.marketing@company.com",
        "recipients": ['sarah.designer@company.com','mike.ux@company.com'],
        "current_labels": ["Design/Needs-Review", "figma", "review"],
        "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
        "attachments_asset_ids": ["asset_019"]
    }),
    Action(name="update_cycle_status", kwargs={
        "cycle_id": "cycle_013",
        "new_status": "NEEDS_REVIEW",
        "thread_id": "thread_015"
    }),
    Action(name="add_comment", kwargs={
        "artifact_id": "art_007",
        "author_email": "lisa.marketing@company.com",
        "content": "Submitted for review",
        "source_message_id": "msg_017",
        "resolved_flag": False
    }),
],
outputs=[
    {
                "comment_id": "comment_019",
                "artifact_id": "art_007",
                "author_email": "lisa.marketing@company.com",
                "content": "Submitted for review",
                "source_message_id_nullable": "msg_017",
                "created_ts": "2024-08-23T12:00:00Z",
                "resolved_flag": False
            },
    {
                "cycle_id": "cycle_013",
                "artifact_id": "art_007",
                "thread_id_nullable": "thread_015",
                "status": "NEEDS_REVIEW",
                "created_ts": "2024-08-23T12:00:00Z",
                "sla_deadline_ts": "2024-08-28T12:30:00Z",
                "sla_breached_flag": False,
                "escalated_ts_nullable": None
            }
]
),
Task(
    annotator="0",
    user_id="task_48",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Design Review: Homepage Hero Section'  with message 'Good Job' for asset 'asset_001'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_49",
    instruction=(
        "You are 'sarah.designer@company.com' and you want to submit a review request for your frame by exporting a PNG 2x asset for that frame with filename 'hero-section-2x-r2.png'"
        "under gmail thread addressed to 'mike.ux@company.com', 'alex.dev@company.com', 'lisa.marketing@company.com'"
    ),
    actions=[
        Action(
            name="get_all_artifacts_of_type_with_tags_and_email",
            kwargs={"artifact_type": "FRAME", "owner_email":"sarah.designer@company.com", "tags":["needs-review"]},
        ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_001",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/hero-section-2x-r2.png"
        }),
        Action(name="create_new_cycle", kwargs={
            "artifact_id": "art_001",
            "sla_deadline_ts": "2024-08-28T12:30:00Z"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Design Review: hero-section-2x-r2.png",
            "sender_id": "sarah.designer@company.com",
            "recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"],
            "current_labels": ["Design/Needs-Review", "figma", "review"],
            "body_html": "<p>Review for the hero-section-2x-r2.png. See attachment.</p>",
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_013",
            "new_status": "NEEDS_REVIEW",
            "thread_id": "thread_015"
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Submitted for review",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
    ],
    outputs=[
        {
            "comment_id": "comment_019",
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Submitted for review",
            "source_message_id_nullable": "msg_017",
            "created_ts": "2024-08-23T12:00:00Z",
            "resolved_flag": False
        },
    ]
),
Task(
    annotator="0",
    user_id="task_50",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Design Review: Homepage Hero Section'  with message 'Good Job' for asset 'asset_001'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_51",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_52",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_53",
    instruction=(
        "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 2x asset for that frame with filename 'pricing-page-2x-r2.png' "
        "under gmail thread addressed to 'sarah.designer@company.com', 'mike.ux@company.com'"
    ),
    actions=[
        Action(
            name="get_all_artifacts_of_type_with_tags_and_email",
            kwargs={"artifact_type": "FRAME", "owner_email": "lisa.marketing@company.com", "tags": ["needs-review"]},
        ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_007",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/pricing-page-2x-r2.png"
        }),
        Action(name="create_new_cycle", kwargs={
            "artifact_id": "art_007",
            "sla_deadline_ts": "2024-08-28T12:30:00Z"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Design Review: pricing-page-2x-r2.png",
            "sender_id": "lisa.marketing@company.com",
            "recipients": ["sarah.designer@company.com", "mike.ux@company.com"],
            "current_labels": ["Design/Needs-Review", "figma", "review"],
            "body_html": "<p>Review for the pricing-page-2x-r2.png. See attachment.</p>",
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_013",
            "new_status": "NEEDS_REVIEW",
            "thread_id": "thread_015"
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_007",
            "author_email": "lisa.marketing@company.com",
            "content": "Submitted for review",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_013",
            "artifact_id": "art_007",
            "thread_id_nullable": "thread_015",
            "status": "NEEDS_REVIEW",
            "created_ts": "2024-08-23T12:00:00Z",
            "sla_deadline_ts": "2024-08-28T12:30:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_54",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_55",
    instruction=(
        "You are 'mike.ux@company.com' and you need to review for 'Admin Panel Accessibility Audit' is past SLA — request changes in the existing thread with message 'SLA breached; please prioritize fixes and resubmit'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(
            name="get_complete_email_thread",
            kwargs={"thread_id":"thread_004"},
        ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: SLA breached; please prioritize fixes and resubmit</p>",
            "attachments_asset_ids": ["asset_007"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_004",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_004",
            "escalated_ts": "2024-08-23T12:00:00Z"
        })
    ],
    outputs=[
        {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-23T12:00:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_56",
    instruction=(
        "You are 'mike.ux@company.com'. Publish release notes for 'Design System v1.3.0 - Form Components & Accessibility' "
        "to the existing release thread, including PNG 3x exports for newly added frames, "
        "and list the changed frames from the release diff."
    ),
    actions=[
        Action(name="get_release_details_by_name", kwargs={
            "release_name": "Design System v1.3.0 - Form Components & Accessibility"
        }),
        Action(name="get_release_diff_by_release_id", kwargs={
            "release_id": "release_011"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:5",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:5.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:5.png"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_014",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:6.png"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:7",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:7.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_015",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:7.png"
        }),
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes",
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_013",
            "body_html": (
                "<h2>Design System v1.3.0 - Form Components & Accessibility</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 1:5</li>"
                "<li>Added frame 1:6</li>"
                "<li>Added frame 1:7</li>"
                "<li>Updated frame 1:3</li>"
                "<li>Updated frame 1:4</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019", "asset_020", "asset_021"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_013",
            "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes",
            "sender_identity": "design-automation@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T11:15:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_017",
            "thread_id": "thread_013",
            "sender_email": "design-automation@company.com",
            "body_html": "<h2>Design System v1.3.0 - Form Components & Accessibility</h2><p>Highlights:</p><ul><li>Added frame 1:5</li><li>Added frame 1:6</li><li>Added frame 1:7</li><li>Updated frame 1:3</li><li>Updated frame 1:4</li></ul>",        
            "body_text_stripped": "Design System v1.3.0 - Form Components & Accessibility Highlights: Added frame 1:5, Added frame 1:6, Added frame 1:7, Updated frame 1:3, Updated frame 1:4,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019",
                "asset_020",
                "asset_021"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_57",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and updating frames '2:4' and '2:2' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": ["2:4", "2:2"],
            "frames_removed": [],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Updated 2 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Updated frame 2:4</li>"
                "<li>Updated frame 2:2</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_015",
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_identity": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T12:00:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_018",
            "thread_id": "thread_015",
            "sender_email": "mike.ux@company.com",
            "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
            "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Updated frame 2:2,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_58",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and removing frames '2:4' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": [],
            "frames_removed": ["2:4"],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Removed 1 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Removed frame 2:4</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_015",
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_identity": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T12:00:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_018",
            "thread_id": "thread_015",
            "sender_email": "mike.ux@company.com",
            "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
            "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Removed frame 2:4,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_59",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and updating frames '2:4' and removing '2:2' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": ["2:4"],
            "frames_removed": ["2:2"],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Updated 1 frames",
                "Removed 1 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Updated frame 2:4</li>"
                "<li>Removed frame 2:2</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
    {
        "thread": {
        "thread_id": "thread_015",
        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
        "sender_identity": "mike.ux@company.com",
        "recipients": [
            "stakeholders@company.com",
            "product-managers@company.com",
            "engineering-leads@company.com"
        ],
        "current_labels": [
            "Design/Release"
        ],
        "created_ts": "2024-08-23T12:00:00Z",
        "updated_ts": "2024-08-23T12:00:00Z"
        },
        "message": {
        "message_id": "msg_018",
        "thread_id": "thread_015",
        "sender_email": "mike.ux@company.com",
        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Removed frame 2:2,",
        "sent_ts": "2024-08-23T12:00:00Z",
        "attachments_asset_ids": [
            "asset_019"
        ]
        }
    }
    ]
),
Task(
    annotator="0",
    user_id="task_60",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_61",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_62",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
annotator="0",
user_id="task_63",
instruction=(
    "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 3x asset for that frame with filename 'hero-section-3x.png'"
    "under gmail thread addressed to 'sarah.designer@company.com' and 'mike.ux@company.com'"
),
actions=[
    Action(
        name="get_all_artifacts_of_type_with_tags_and_email",
        kwargs={"artifact_type": "FRAME", "owner_email":"lisa.marketing@company.com", "tags":["needs-review"]},
    ),
    Action(name="create_new_asset", kwargs={
        "artifact_id": "art_007",
        "export_profile": "PNG 3x",
        "file_size_bytes": 3000,
        "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
    }),
    Action(name="create_new_cycle", kwargs={
        "artifact_id": "art_007",
        "sla_deadline_ts": "2024-08-28T12:30:00Z"
    }),
    Action(name="start_email_thread", kwargs={
        "subject": "Design Review: hero-section-3x.png",
        "sender_id": "lisa.marketing@company.com",
        "recipients": ['sarah.designer@company.com','mike.ux@company.com'],
        "current_labels": ["Design/Needs-Review", "figma", "review"],
        "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
        "attachments_asset_ids": ["asset_019"]
    }),
    Action(name="update_cycle_status", kwargs={
        "cycle_id": "cycle_013",
        "new_status": "NEEDS_REVIEW",
        "thread_id": "thread_015"
    }),
    Action(name="add_comment", kwargs={
        "artifact_id": "art_007",
        "author_email": "lisa.marketing@company.com",
        "content": "Submitted for review",
        "source_message_id": "msg_017",
        "resolved_flag": False
    }),
],
outputs=[
    {
                    "comment_id": "comment_019",
                    "artifact_id": "art_007",
                    "author_email": "lisa.marketing@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": False
                },
    {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": False,
                    "escalated_ts_nullable": None
                }
]
),
Task(
    annotator="0",
    user_id="task_64",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Design Review: Homepage Hero Section'  with message 'Good Job' for asset 'asset_001'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_65",
    instruction=(
        "You are 'sarah.designer@company.com' and you want to submit a review request for your frame by exporting a PNG 2x asset for that frame with filename 'hero-section-2x-r2.png'"
        "under gmail thread addressed to 'mike.ux@company.com', 'alex.dev@company.com', 'lisa.marketing@company.com'"
    ),
    actions=[
        Action(
            name="get_all_artifacts_of_type_with_tags_and_email",
            kwargs={"artifact_type": "FRAME", "owner_email":"sarah.designer@company.com", "tags":["needs-review"]},
        ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_001",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/hero-section-2x-r2.png"
        }),
        Action(name="create_new_cycle", kwargs={
            "artifact_id": "art_001",
            "sla_deadline_ts": "2024-08-28T12:30:00Z"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Design Review: hero-section-2x-r2.png",
            "sender_id": "sarah.designer@company.com",
            "recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"],
            "current_labels": ["Design/Needs-Review", "figma", "review"],
            "body_html": "<p>Review for the hero-section-2x-r2.png. See attachment.</p>",
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_013",
            "new_status": "NEEDS_REVIEW",
            "thread_id": "thread_015"
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Submitted for review",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
    ],
    outputs=[
        {
            "comment_id": "comment_019",
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Submitted for review",
            "source_message_id_nullable": "msg_017",
            "created_ts": "2024-08-23T12:00:00Z",
            "resolved_flag": False
        },

    ]
),
Task(
    annotator="0",
    user_id="task_66",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Design Review: Homepage Hero Section'  with message 'Good Job' for asset 'asset_001'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_67",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_68",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_69",
    instruction=(
        "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 2x asset for that frame with filename 'pricing-page-2x-r2.png' "
        "under gmail thread addressed to 'sarah.designer@company.com', 'mike.ux@company.com'"
    ),
    actions=[
        Action(
            name="get_all_artifacts_of_type_with_tags_and_email",
            kwargs={"artifact_type": "FRAME", "owner_email": "lisa.marketing@company.com", "tags": ["needs-review"]},
        ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_007",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/pricing-page-2x-r2.png"
        }),
        Action(name="create_new_cycle", kwargs={
            "artifact_id": "art_007",
            "sla_deadline_ts": "2024-08-28T12:30:00Z"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Design Review: pricing-page-2x-r2.png",
            "sender_id": "lisa.marketing@company.com",
            "recipients": ["sarah.designer@company.com", "mike.ux@company.com"],
            "current_labels": ["Design/Needs-Review", "figma", "review"],
            "body_html": "<p>Review for the pricing-page-2x-r2.png. See attachment.</p>",
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_013",
            "new_status": "NEEDS_REVIEW",
            "thread_id": "thread_015"
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_007",
            "author_email": "lisa.marketing@company.com",
            "content": "Submitted for review",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_013",
            "artifact_id": "art_007",
            "thread_id_nullable": "thread_015",
            "status": "NEEDS_REVIEW",
            "created_ts": "2024-08-23T12:00:00Z",
            "sla_deadline_ts": "2024-08-28T12:30:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_70",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_71",
    instruction=(
        "You are 'mike.ux@company.com' and you need to review for 'Admin Panel Accessibility Audit' is past SLA — request changes in the existing thread with message 'SLA breached; please prioritize fixes and resubmit'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(
            name="get_complete_email_thread",
            kwargs={"thread_id":"thread_004"},
        ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: SLA breached; please prioritize fixes and resubmit</p>",
            "attachments_asset_ids": ["asset_007"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_004",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_004",
            "escalated_ts": "2024-08-23T12:00:00Z"
        })
    ],
    outputs=[
        {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-23T12:00:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_72",
    instruction=(
        "You are 'mike.ux@company.com'. Publish release notes for 'Design System v1.3.0 - Form Components & Accessibility' "
        "to the existing release thread, including PNG 3x exports for newly added frames, "
        "and list the changed frames from the release diff."
    ),
    actions=[
        Action(name="get_release_details_by_name", kwargs={
            "release_name": "Design System v1.3.0 - Form Components & Accessibility"
        }),
        Action(name="get_release_diff_by_release_id", kwargs={
            "release_id": "release_011"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:5",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:5.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:5.png"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_014",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:6.png"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:7",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:7.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_015",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:7.png"
        }),
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes",
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_013",
            "body_html": (
                "<h2>Design System v1.3.0 - Form Components & Accessibility</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 1:5</li>"
                "<li>Added frame 1:6</li>"
                "<li>Added frame 1:7</li>"
                "<li>Updated frame 1:3</li>"
                "<li>Updated frame 1:4</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019", "asset_020", "asset_021"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_013",
            "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes",
            "sender_identity": "design-automation@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T11:15:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_017",
            "thread_id": "thread_013",
            "sender_email": "design-automation@company.com",
            "body_html": "<h2>Design System v1.3.0 - Form Components & Accessibility</h2><p>Highlights:</p><ul><li>Added frame 1:5</li><li>Added frame 1:6</li><li>Added frame 1:7</li><li>Updated frame 1:3</li><li>Updated frame 1:4</li></ul>",        
            "body_text_stripped": "Design System v1.3.0 - Form Components & Accessibility Highlights: Added frame 1:5, Added frame 1:6, Added frame 1:7, Updated frame 1:3, Updated frame 1:4,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019",
                "asset_020",
                "asset_021"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_73",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and updating frames '2:4' and '2:2' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": ["2:4", "2:2"],
            "frames_removed": [],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Updated 2 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Updated frame 2:4</li>"
                "<li>Updated frame 2:2</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_015",
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_identity": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T12:00:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_018",
            "thread_id": "thread_015",
            "sender_email": "mike.ux@company.com",
            "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
            "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Updated frame 2:2,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_74",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and removing frames '2:4' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": [],
            "frames_removed": ["2:4"],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Removed 1 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Removed frame 2:4</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_015",
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_identity": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T12:00:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_018",
            "thread_id": "thread_015",
            "sender_email": "mike.ux@company.com",
            "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
            "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Removed frame 2:4,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_75",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and updating frames '2:4' and removing '2:2' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": ["2:4"],
            "frames_removed": ["2:2"],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Updated 1 frames",
                "Removed 1 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Updated frame 2:4</li>"
                "<li>Removed frame 2:2</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
    {
        "thread": {
        "thread_id": "thread_015",
        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
        "sender_identity": "mike.ux@company.com",
        "recipients": [
            "stakeholders@company.com",
            "product-managers@company.com",
            "engineering-leads@company.com"
        ],
        "current_labels": [
            "Design/Release"
        ],
        "created_ts": "2024-08-23T12:00:00Z",
        "updated_ts": "2024-08-23T12:00:00Z"
        },
        "message": {
        "message_id": "msg_018",
        "thread_id": "thread_015",
        "sender_email": "mike.ux@company.com",
        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Removed frame 2:2,",
        "sent_ts": "2024-08-23T12:00:00Z",
        "attachments_asset_ids": [
            "asset_019"
        ]
        }
    }
    ]
),
Task(
    annotator="0",
    user_id="task_76",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_77",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_78",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
annotator="0",
user_id="task_79",
instruction=(
    "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 3x asset for that frame with filename 'hero-section-3x.png'"
    "under gmail thread addressed to 'sarah.designer@company.com' and 'mike.ux@company.com'"
),
actions=[
    Action(
        name="get_all_artifacts_of_type_with_tags_and_email",
        kwargs={"artifact_type": "FRAME", "owner_email":"lisa.marketing@company.com", "tags":["needs-review"]},
    ),
    Action(name="create_new_asset", kwargs={
        "artifact_id": "art_007",
        "export_profile": "PNG 3x",
        "file_size_bytes": 3000,
        "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
    }),
    Action(name="create_new_cycle", kwargs={
        "artifact_id": "art_007",
        "sla_deadline_ts": "2024-08-28T12:30:00Z"
    }),
    Action(name="start_email_thread", kwargs={
        "subject": "Design Review: hero-section-3x.png",
        "sender_id": "lisa.marketing@company.com",
        "recipients": ['sarah.designer@company.com','mike.ux@company.com'],
        "current_labels": ["Design/Needs-Review", "figma", "review"],
        "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
        "attachments_asset_ids": ["asset_019"]
    }),
    Action(name="update_cycle_status", kwargs={
        "cycle_id": "cycle_013",
        "new_status": "NEEDS_REVIEW",
        "thread_id": "thread_015"
    }),
    Action(name="add_comment", kwargs={
        "artifact_id": "art_007",
        "author_email": "lisa.marketing@company.com",
        "content": "Submitted for review",
        "source_message_id": "msg_017",
        "resolved_flag": False
    }),
],
outputs=[
    {
                "comment_id": "comment_019",
                "artifact_id": "art_007",
                "author_email": "lisa.marketing@company.com",
                "content": "Submitted for review",
                "source_message_id_nullable": "msg_017",
                "created_ts": "2024-08-23T12:00:00Z",
                "resolved_flag": False
            },
{
                "cycle_id": "cycle_013",
                "artifact_id": "art_007",
                "thread_id_nullable": "thread_015",
                "status": "NEEDS_REVIEW",
                "created_ts": "2024-08-23T12:00:00Z",
                "sla_deadline_ts": "2024-08-28T12:30:00Z",
                "sla_breached_flag": False,
                "escalated_ts_nullable": None
            }
]
),
Task(
    annotator="0",
    user_id="task_80",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Design Review: Homepage Hero Section'  with message 'Good Job' for asset 'asset_001'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_81",
    instruction=(
        "You are 'sarah.designer@company.com' and you want to submit a review request for your frame by exporting a PNG 2x asset for that frame with filename 'hero-section-2x-r2.png'"
        "under gmail thread addressed to 'mike.ux@company.com', 'alex.dev@company.com', 'lisa.marketing@company.com'"
    ),
    actions=[
        Action(
            name="get_all_artifacts_of_type_with_tags_and_email",
            kwargs={"artifact_type": "FRAME", "owner_email":"sarah.designer@company.com", "tags":["needs-review"]},
        ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_001",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/hero-section-2x-r2.png"
        }),
        Action(name="create_new_cycle", kwargs={
            "artifact_id": "art_001",
            "sla_deadline_ts": "2024-08-28T12:30:00Z"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Design Review: hero-section-2x-r2.png",
            "sender_id": "sarah.designer@company.com",
            "recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"],
            "current_labels": ["Design/Needs-Review", "figma", "review"],
            "body_html": "<p>Review for the hero-section-2x-r2.png. See attachment.</p>",
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_013",
            "new_status": "NEEDS_REVIEW",
            "thread_id": "thread_015"
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Submitted for review",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
    ],
    outputs=[
        {
            "comment_id": "comment_019",
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Submitted for review",
            "source_message_id_nullable": "msg_017",
            "created_ts": "2024-08-23T12:00:00Z",
            "resolved_flag": False
        },

    ]
),
Task(
    annotator="0",
    user_id="task_82",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Design Review: Homepage Hero Section'  with message 'Good Job' for asset 'asset_001'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_83",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_84",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_85",
    instruction=(
        "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 2x asset for that frame with filename 'pricing-page-2x-r2.png' "
        "under gmail thread addressed to 'sarah.designer@company.com', 'mike.ux@company.com'"
    ),
    actions=[
        Action(
            name="get_all_artifacts_of_type_with_tags_and_email",
            kwargs={"artifact_type": "FRAME", "owner_email": "lisa.marketing@company.com", "tags": ["needs-review"]},
        ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_007",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/pricing-page-2x-r2.png"
        }),
        Action(name="create_new_cycle", kwargs={
            "artifact_id": "art_007",
            "sla_deadline_ts": "2024-08-28T12:30:00Z"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Design Review: pricing-page-2x-r2.png",
            "sender_id": "lisa.marketing@company.com",
            "recipients": ["sarah.designer@company.com", "mike.ux@company.com"],
            "current_labels": ["Design/Needs-Review", "figma", "review"],
            "body_html": "<p>Review for the pricing-page-2x-r2.png. See attachment.</p>",
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_013",
            "new_status": "NEEDS_REVIEW",
            "thread_id": "thread_015"
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_007",
            "author_email": "lisa.marketing@company.com",
            "content": "Submitted for review",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_013",
            "artifact_id": "art_007",
            "thread_id_nullable": "thread_015",
            "status": "NEEDS_REVIEW",
            "created_ts": "2024-08-23T12:00:00Z",
            "sla_deadline_ts": "2024-08-28T12:30:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_86",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_87",
    instruction=(
        "You are 'mike.ux@company.com' and you need to review for 'Admin Panel Accessibility Audit' is past SLA — request changes in the existing thread with message 'SLA breached; please prioritize fixes and resubmit'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(
            name="get_complete_email_thread",
            kwargs={"thread_id":"thread_004"},
        ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: SLA breached; please prioritize fixes and resubmit</p>",
            "attachments_asset_ids": ["asset_007"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_004",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_004",
            "escalated_ts": "2024-08-23T12:00:00Z"
        })
    ],
    outputs=[
        {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-23T12:00:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_88",
    instruction=(
        "You are 'mike.ux@company.com'. Publish release notes for 'Design System v1.3.0 - Form Components & Accessibility' "
        "to the existing release thread, including PNG 3x exports for newly added frames, "
        "and list the changed frames from the release diff."
    ),
    actions=[
        Action(name="get_release_details_by_name", kwargs={
            "release_name": "Design System v1.3.0 - Form Components & Accessibility"
        }),
        Action(name="get_release_diff_by_release_id", kwargs={
            "release_id": "release_011"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:5",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:5.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:5.png"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_014",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:6.png"
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"1:7",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abc123def456", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abc123def456_1:7.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_015",
            "export_profile": "PNG 3x",
            "file_size_bytes": 3000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:7.png"
        }),
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes",
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_013",
            "body_html": (
                "<h2>Design System v1.3.0 - Form Components & Accessibility</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 1:5</li>"
                "<li>Added frame 1:6</li>"
                "<li>Added frame 1:7</li>"
                "<li>Updated frame 1:3</li>"
                "<li>Updated frame 1:4</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019", "asset_020", "asset_021"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_013",
            "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes",
            "sender_identity": "design-automation@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T11:15:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_017",
            "thread_id": "thread_013",
            "sender_email": "design-automation@company.com",
            "body_html": "<h2>Design System v1.3.0 - Form Components & Accessibility</h2><p>Highlights:</p><ul><li>Added frame 1:5</li><li>Added frame 1:6</li><li>Added frame 1:7</li><li>Updated frame 1:3</li><li>Updated frame 1:4</li></ul>",        
            "body_text_stripped": "Design System v1.3.0 - Form Components & Accessibility Highlights: Added frame 1:5, Added frame 1:6, Added frame 1:7, Updated frame 1:3, Updated frame 1:4,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019",
                "asset_020",
                "asset_021"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_89",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and updating frames '2:4' and '2:2' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": ["2:4", "2:2"],
            "frames_removed": [],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Updated 2 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Updated frame 2:4</li>"
                "<li>Updated frame 2:2</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_015",
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_identity": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T12:00:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_018",
            "thread_id": "thread_015",
            "sender_email": "mike.ux@company.com",
            "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
            "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Updated frame 2:2,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_90",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and removing frames '2:4' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": [],
            "frames_removed": ["2:4"],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Removed 1 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Removed frame 2:4</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
        {
            "thread": {
            "thread_id": "thread_015",
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_identity": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": [
                "Design/Release"
            ],
            "created_ts": "2024-08-23T12:00:00Z",
            "updated_ts": "2024-08-23T12:00:00Z"
            },
            "message": {
            "message_id": "msg_018",
            "thread_id": "thread_015",
            "sender_email": "mike.ux@company.com",
            "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
            "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Removed frame 2:4,",
            "sent_ts": "2024-08-23T12:00:00Z",
            "attachments_asset_ids": [
                "asset_019"
            ]
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_91",
    instruction=(
        "You are 'mike.ux@company.com'. Create a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with with tag 'mobile-app-v2.3.0' "
        "with prior release id as release_012, by adding new frame '2:6' and updating frames '2:4' and removing '2:2' and exporting new PNG 2x frames to the recipient 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'"
    ),
    actions=[
        Action(name="create_new_release", kwargs={
            "figma_file_id": "figd_abcd1234",
            "version_id": "v2.3.0",
            "version_tag": "release/mobile-app-v2.3.0",
            "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
            "owner_email": "mike.ux@company.com"
        }),
        Action(name="create_release_diff", kwargs={
            "release_id": "release_013",
            "prior_release_id": "release_012",
            "frames_added": ["2:6"],
            "frames_updated": ["2:4"],
            "frames_removed": ["2:2"],
            "component_version_bumps": ["App update"],
            "changelog_highlights": [
                "Added 1 frames",
                "Updated 1 frames",
                "Removed 1 frames"
            ]
        }),
        Action(
                name="create_new_artifact",
                kwargs={
                    "artifact_type":"FRAME",
                    "frame_id_nullable":"2:6",
                    "artifact_name":"Hero Section", 
                    "figma_file_id":"figd_abcd1234", 
                    "page_id":"1:2", 
                    "owner_email":"mike.ux@company.com", 
                    "deep_link":"https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags":["user", "settings"],
                    },
            ),
        Action(name="create_new_asset", kwargs={
            "artifact_id": "art_013",
            "export_profile": "PNG 2x",
            "file_size_bytes": 2000,
            "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
        }),
        Action(name="start_email_thread", kwargs={
            "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
            "sender_id": "mike.ux@company.com",
            "recipients": [
                "stakeholders@company.com",
                "product-managers@company.com",
                "engineering-leads@company.com"
            ],
            "current_labels": ["Design/Release"],
            "body_html": (
                "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>"
            ),
            "attachments_asset_ids": ["asset_019"]
        }),
        Action(name="notify_stakeholders", kwargs={
            "thread_id": "thread_015",
            "body_html": (
                "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2>"
                "<p>Highlights:</p>"
                "<ul>"
                "<li>Added frame 2:6</li>"
                "<li>Updated frame 2:4</li>"
                "<li>Removed frame 2:2</li>"
                "</ul>"
            ),
            "attachments_asset_ids": ["asset_019"]
        })
    ],
    outputs=[
    {
        "thread": {
        "thread_id": "thread_015",
        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
        "sender_identity": "mike.ux@company.com",
        "recipients": [
            "stakeholders@company.com",
            "product-managers@company.com",
            "engineering-leads@company.com"
        ],
        "current_labels": [
            "Design/Release"
        ],
        "created_ts": "2024-08-23T12:00:00Z",
        "updated_ts": "2024-08-23T12:00:00Z"
        },
        "message": {
        "message_id": "msg_018",
        "thread_id": "thread_015",
        "sender_email": "mike.ux@company.com",
        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish \u2014 Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Removed frame 2:2,",
        "sent_ts": "2024-08-23T12:00:00Z",
        "attachments_asset_ids": [
            "asset_019"
        ]
        }
    }
    ]
),
Task(
    annotator="0",
    user_id="task_92",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_93",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_94",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
annotator="0",
user_id="task_95",
instruction=(
    "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 3x asset for that frame with filename 'hero-section-3x.png'"
    "under gmail thread addressed to 'sarah.designer@company.com' and 'mike.ux@company.com'"
),
actions=[
    Action(
        name="get_all_artifacts_of_type_with_tags_and_email",
        kwargs={"artifact_type": "FRAME", "owner_email":"lisa.marketing@company.com", "tags":["needs-review"]},
    ),
    Action(name="create_new_asset", kwargs={
        "artifact_id": "art_007",
        "export_profile": "PNG 3x",
        "file_size_bytes": 3000,
        "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
    }),
    Action(name="create_new_cycle", kwargs={
        "artifact_id": "art_007",
        "sla_deadline_ts": "2024-08-28T12:30:00Z"
    }),
    Action(name="start_email_thread", kwargs={
        "subject": "Design Review: hero-section-3x.png",
        "sender_id": "lisa.marketing@company.com",
        "recipients": ['sarah.designer@company.com','mike.ux@company.com'],
        "current_labels": ["Design/Needs-Review", "figma", "review"],
        "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
        "attachments_asset_ids": ["asset_019"]
    }),
    Action(name="update_cycle_status", kwargs={
        "cycle_id": "cycle_013",
        "new_status": "NEEDS_REVIEW",
        "thread_id": "thread_015"
    }),
    Action(name="add_comment", kwargs={
        "artifact_id": "art_007",
        "author_email": "lisa.marketing@company.com",
        "content": "Submitted for review",
        "source_message_id": "msg_017",
        "resolved_flag": False
    }),
],
outputs=[
{
"comment_id": "comment_019",
"artifact_id": "art_007",
"author_email": "lisa.marketing@company.com",
"content": "Submitted for review",
"source_message_id_nullable": "msg_017",
"created_ts": "2024-08-23T12:00:00Z",
"resolved_flag": False
},
{
"cycle_id": "cycle_013",
"artifact_id": "art_007",
"thread_id_nullable": "thread_015",
"status": "NEEDS_REVIEW",
"created_ts": "2024-08-23T12:00:00Z",
"sla_deadline_ts": "2024-08-28T12:30:00Z",
"sla_breached_flag": False,
"escalated_ts_nullable": None
}
]
),
Task(
    annotator="0",
    user_id="task_96",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Design Review: Homepage Hero Section'  with message 'Good Job' for asset 'asset_001'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_97",
    instruction=(
        "You are 'mike.ux@company.com'. In the existing review thread 'Design Review: Homepage Hero Section' you need to request changes with message 'please update the headline spacing and button contrast.' for asset 'asset_001', "
        "then after the author confirms changes are implemented with meassage 'adjusted headline spacing and increased primary button contrast', and  approve it with message 'Good Job'."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Design Review: Homepage Hero Section"
        }),
        Action(
                name="get_complete_email_thread",
                kwargs={"thread_id":"thread_001"},
            ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_001"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_001"
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_001",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_001"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "sarah.designer@company.com",
            "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "sarah.designer@company.com",
            "content": "Changes implemented",
            "source_message_id": "msg_018",
            "resolved_flag": True
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_001",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job</p>",
            "attachments_asset_ids":["asset_001"]
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_001",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_019",
            "resolved_flag": True
        }),
        
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_021"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_001",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": False,
            "approval_comment_ref_nullable": "comment_021"
            },
            "cycle": {
            "cycle_id": "cycle_001",
            "artifact_id": "art_001",
            "thread_id_nullable": "thread_001",
            "status": "APPROVED",
            "created_ts": "2024-08-20T15:00:00Z",
            "sla_deadline_ts": "2024-08-23T15:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_98",
    instruction=(
        "You are 'mike.ux@company.com' and you want to request changes in the existing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.'"
        " and the current artifact art_002."
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Navigation Bar Responsive Design",
        }),
        Action(name="get_complete_email_thread", kwargs={
            "thread_id": "thread_010"
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_010", "artifact_id":"art_002"
        }),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_010",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
            "attachments_asset_ids": []
        }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_002",
            "author_email": "mike.ux@company.com",
            "content": "Requested changes",
            "source_message_id": "msg_017",
            "resolved_flag": False
        }),
        Action(name="update_cycle_status", kwargs={
            "cycle_id": "cycle_008",
            "new_status": "CHANGES_REQUESTED",
            "thread_id": "thread_010"
        }),
    ],
    outputs=[
        {
            "cycle_id": "cycle_008",
            "artifact_id": "art_002",
            "thread_id_nullable": "thread_010",
            "status": "CHANGES_REQUESTED",
            "created_ts": "2024-08-21T10:00:00Z",
            "sla_deadline_ts": "2024-08-24T10:00:00Z",
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
    ]
),
Task(
    annotator="0",
    user_id="task_99",
    instruction=(
        "You are 'mike.ux@company.com'. you need to approve existing review thread 'Admin Panel Accessibility Audit'  with message 'Good Job, but done late' for asset 'asset_007'"
    ),
    actions=[
        Action(name="get_thread_by_subject", kwargs={
            "subject": "Admin Panel Accessibility Audit"
        }),
        # Action(
        #         name="get_complete_email_thread",
        #         kwargs={"thread_id":"thread_001"},
        #     ),
        Action(name="send_email_in_thread", kwargs={
            "thread_id": "thread_004",
            "sender_id": "mike.ux@company.com",
            "body_html": "<p>Approved: Good Job, but done late</p>",
            "attachments_asset_ids":["asset_007"]
        }),
        Action(name="get_asset_by_id",kwargs={
            "asset_id": "asset_007"
            }),
        Action(name="add_comment", kwargs={
            "artifact_id": "art_008",
            "author_email": "mike.ux@company.com",
            "content": "Approved",
            "source_message_id": "msg_017",
            "resolved_flag": True
        }),
        Action(name="get_cycle_by_artifact_and_thread", kwargs={
            "thread_id": "thread_004"
        }),
        Action(name="approve_review", kwargs={
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approval_comment_ref": "comment_019"
        })
    ],
    outputs=[
        {
            "approval": {
            "approval_id": "approval_012",
            "cycle_id": "cycle_004",
            "approver_email": "mike.ux@company.com",
            "approved_ts": "2024-08-23T12:00:00Z",
            "sla_breached_flag": True,
            "approval_comment_ref_nullable": "comment_019"
            },
            "cycle": {
            "cycle_id": "cycle_004",
            "artifact_id": "art_008",
            "thread_id_nullable": "thread_004",
            "status": "APPROVED",
            "created_ts": "2024-08-18T15:30:00Z",
            "sla_deadline_ts": "2024-08-21T15:30:00Z",
            "sla_breached_flag": True,
            "escalated_ts_nullable": "2024-08-21T16:00:00Z"
            }
        }
    ]
),
Task(
annotator="0",
user_id="task_100",
instruction=(
    "You are 'lisa.marketing@company.com' and you want to submit a review request for your frame by exporting a PNG 3x asset for that frame with filename 'hero-section-3x.png'"
    "under gmail thread addressed to 'sarah.designer@company.com' and 'mike.ux@company.com'"
),
actions=[
    Action(
        name="get_all_artifacts_of_type_with_tags_and_email",
        kwargs={"artifact_type": "FRAME", "owner_email":"lisa.marketing@company.com", "tags":["needs-review"]},
    ),
    Action(name="create_new_asset", kwargs={
        "artifact_id": "art_007",
        "export_profile": "PNG 3x",
        "file_size_bytes": 3000,
        "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
    }),
    Action(name="create_new_cycle", kwargs={
        "artifact_id": "art_007",
        "sla_deadline_ts": "2024-08-28T12:30:00Z"
    }),
    Action(name="start_email_thread", kwargs={
        "subject": "Design Review: hero-section-3x.png",
        "sender_id": "lisa.marketing@company.com",
        "recipients": ['sarah.designer@company.com','mike.ux@company.com'],
        "current_labels": ["Design/Needs-Review", "figma", "review"],
        "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
        "attachments_asset_ids": ["asset_019"]
    }),
    Action(name="update_cycle_status", kwargs={
        "cycle_id": "cycle_013",
        "new_status": "NEEDS_REVIEW",
        "thread_id": "thread_015"
    }),
    Action(name="add_comment", kwargs={
        "artifact_id": "art_007",
        "author_email": "lisa.marketing@company.com",
        "content": "Submitted for review",
        "source_message_id": "msg_017",
        "resolved_flag": False
    }),
],
outputs=[
    {
        "comment_id": "comment_019",
        "artifact_id": "art_007",
        "author_email": "lisa.marketing@company.com",
        "content": "Submitted for review",
        "source_message_id_nullable": "msg_017",
        "created_ts": "2024-08-23T12:00:00Z",
        "resolved_flag": False
    },
{
        "cycle_id": "cycle_013",
        "artifact_id": "art_007",
        "thread_id_nullable": "thread_015",
        "status": "NEEDS_REVIEW",
        "created_ts": "2024-08-23T12:00:00Z",
        "sla_deadline_ts": "2024-08-28T12:30:00Z",
        "sla_breached_flag": False,
        "escalated_ts_nullable": None
    }
]
),























]










# Action(
            #     name="get_artifact_with_id",
            #     kwargs={"artifact_id": "art_001"},
            # ),
            # Action(
            #     name="get_all_artifacts_of_type_with_tags_and_email",
            #     kwargs={"artifact_type": "FRAME", "owner_email":"sarah.designer@company.com", "tags":["needs-review"]},
            # ),
            # Action(
            #     name="create_new_artifact",
            #     kwargs={
            #         "artifact_type":"FRAME",
            #         "frame_id_nullable":"3:3",
            #         "artifact_name":"Hero Section", 
            #         "figma_file_id":"figd_abc123def456", 
            #         "page_id":"1:2", 
            #         "owner_email":"sarah.designer@company.com", 
            #         "deep_link":"https://www.figma.com/file/abc123def456/Design-System?node-id=1%3A3sdf",
            #         "current_tags":["user", "settings"],
            #         },
            # ),
            # Action(
            #     name="get_artifacts_with_file_id",
            #     kwargs={"figma_file_id": "figd_xyz789ghi012","artifact_type":"FRAME", "page_id":"2:1", "frame_id":"2:2"},
            # ),
            # Action(
            #     name="get_asset_by_id",
            #     kwargs={"asset_id": "asset_003"},
            # ),
            # Action(
            #     name="create_new_asset",
            #     kwargs={
            #         "artifact_id":"art_001", 
            #         "export_profile":"PNG 2x", 
            #         "file_size_bytes":245760, 
            #         "storage_ref":"gs://company-assets/figma-exports/hero-section.svg",
            #         },
            # ),
            # Action(
            #     name="get_assets_by_artifact_id",
            #     kwargs={"artifact_id": "art_001"},
            # ),
            # Action(
            #     name="create_new_cycle",
            #     kwargs={"artifact_id":"art_011", "sla_deadline_ts":"2024-08-26T10:30:00Z"},
            # ),
            # Action(
            #     name="update_cycle_status",
            #     kwargs={"cycle_id": "cycle_012", "new_status": "APPROVED","escalated_ts":"025-08-26T12:00:00Z","thread_id":None},
            # ),
            # Action(
            #     name="get_cycle_by_id",
            #     kwargs={"cycle_id":"cycle_013"},
            # ),
            # Action(
            #     name="start_email_thread",
            #     kwargs={
            #         "subject":"Design Review", 
            #         "sender_id":"sarah.designer@company.com", 
            #         "recipients":["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com"], 
            #         "current_labels":["design-review", "urgent", "figma"], 
            #         "body_html":"<p>Hi team,</p><p>I've completed the homepage hero section design. Please review the attached Figma file and let me know your feedback.</p><p>Key changes:</p><ul><li>Updated CTA button styling</li><li>Improved responsive layout</li><li>Enhanced typography hierarchy</li></ul><p>Best regards,<br>Sarah</p>", 
            #         "attachments_asset_ids":["asset_001", "asset_002"]
            #         },
            # ),
            # Action(
            #     name="send_email_in_thread",
            #     kwargs={"thread_id":"thread_015", "sender_id":"lisa.marketing@company.com", "body_html":"<p>Hi team,</p><p>I've completed the homepage hero section design Approved"},
            # ),
            # Action(
            #     name="get_complete_email_thread",
            #     kwargs={"thread_id":"thread_015"},
            # ),
            # Action(
            #     name="add_comment",
            #     kwargs={"artifact_id":"art_001", "author_email":"alex.dev@company.com", "content":"XYZ", "resolved_flag":False, "source_message_id":"msg_002"},
            # ),

            # Action(
            #     name="approve_review",
            #     kwargs={"cycle_id":"cycle_001", "approver_email":"arah.designer@company.co","approval_comment_ref":"comment_003"},
            # ),
            # Action(
            #     name="create_new_release",
            #     kwargs={"figma_file_id":"figd_xyz789ghi012", "version_id":"v2.1.0", "version_tag":"release/mobile-app-v2.1.0", "release_name":"Mobile App v2.1.0 ", "owner_email":"mike.ux@company.com","thread_id":"thread_007"},
            # ),
            # Action(
            #     name="get_release_by_id",
            #     kwargs={"release_id":"release_008"},
            # ),
            # Action(
            #     name="create_release_diff",
            #     kwargs={"release_id":"release_013","prior_release_id":"release_001","frames_added":["1:20"],"frames_updated":["1:15", "1:16", "1:17"], "frames_removed": ["1:3","1:4"],"component_version_bumps":["Button-v1.2", "Card-v1.1", "Modal-v1.0"],"changelog_highlights":["Added new form components", "Enhanced button variants"]},
            # ),
            # Action(
            #     name="get_release_diff_by_release_id",
            #     kwargs={"release_id":"release_013"},
            # ),
            # Action(
            #     name="compare_before_after_visuals",
            #     kwargs={"before_release_id":"release_001", "after_release_id":"release_013"},
            # ),
            # Action(
            #     name="notify_stakeholders",
            #     kwargs={"thread_id":"thread_004", "body_html":"<p>release notes</p>", "attachments_asset_ids":["asset_007"]},
            # ),