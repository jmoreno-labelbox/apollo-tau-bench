# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "res_001",
        "instruction": "As the design review coordinator for the Web UX team and with the current time being 2024-08-23T10:00:00Z, initiate an email-based design review for Figma artifact art_001 utilizing the 'PNG 2x' export. Inform recipients ['design-review@company.com','ux-team@company.com'] within a single thread labeled 'Design/Needs-Review' for the day. Ensure identifiers remain consistent and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T10:00:00Z",
                    "ended_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_002",
        "instruction": "In your role as the release publisher and with the time being 2024-08-23T11:00:00Z, it is necessary for product stakeholders to be aligned\u2014distribute a release handoff for artifact art_001, detailing changes from release_001. Attach using export profile 'PNG 2x' and send from emma.creative@company.com to ['stakeholders@company.com','product-managers@company.com']. Upon sending, tag the artifact with 'released/2024-08-23' and document the run.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "CreateReleaseRecord",
                "arguments": {
                    "artifact_id": "art_001",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "labels": [
                        "released/2024-08-23"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:00:00Z",
                    "ended_at": "2024-08-23T11:00:00Z",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "previous_release_id": "release_001",
                    "release_id": "rel-art_001-20240823-001",
                    "asset_id": "asset_en-002",
                    "export_id": "exp-art_001-20240823-png-001",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "released/2024-08-23"
                    ],
                    "run_id": "run_rl-001",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_003",
        "instruction": "As the accessibility audit lead, it is 2024-08-23T12:00:00Z; initiate an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Inform recipients ['accessibility@company.com','design-review@company.com'] in a single thread labeled 'Design/Accessibility'. Once the request is sent, replicate relevant responses as Figma comments, and label the artifact 'a11y/needs-audit'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T12:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Accessibility Audit: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "Design/Accessibility"
                    ],
                    "timestamp": "2024-08-23T12:00:00Z",
                    "request_id": "ax-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T12:00:00Z",
                    "request_id": "ax-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "a11y/needs-audit"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T12:00:00Z",
                    "request_id": "ax-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "accessibility_audit_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T12:00:00Z",
                    "ended_at": "2024-08-23T12:00:00Z",
                    "timestamp": "2024-08-23T12:00:00Z",
                    "request_id": "ax-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ax-001",
                    "message_id": "msg_ax-002",
                    "asset_id": "asset_en-002",
                    "tags": [
                        "a11y/needs-audit"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_004",
        "instruction": "Being the design systems triage lead, at 2024-08-23T13:00:00Z; organize a triage for Figma artifact art_001 ('Homepage Hero Section') employing the 'PNG 2x' export. Notify recipients ['design-systems@company.com','frontend-guild@company.com'] in a single thread labeled 'Design/Design-System'. After dispatching the request, replicate relevant replies as Figma comments, and assign the artifact the tag 'ds/triage-open'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design System Triage: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "labels": [
                        "Design/Design-System"
                    ],
                    "timestamp": "2024-08-23T13:00:00Z",
                    "request_id": "ds-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_ds-002"
                    ],
                    "timestamp": "2024-08-23T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "ds/triage-open"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T13:00:00Z",
                    "request_id": "ds-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_systems_triage",
                    "status": "completed",
                    "started_at": "2024-08-23T13:00:00Z",
                    "ended_at": "2024-08-23T13:00:00Z",
                    "timestamp": "2024-08-23T13:00:00Z",
                    "request_id": "ds-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ds-001",
                    "message_id": "msg_ds-002",
                    "asset_id": "asset_ds-002",
                    "tags": [
                        "ds/triage-open"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_005",
        "instruction": "As the review program manager at the given time 2024-08-23T14:00:00Z, proceed with the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Notify recipients ['design-review@company.com','ux-team@company.com'] in the single thread labeled 'Design/Needs-Review' by dispatching a reminder. Following this, reflect replies as Figma comments, apply quorum, and ensure identifiers remain deterministic and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_006",
        "instruction": "Assuming the role of the change request lead at 2024-08-23T14:30:00Z, convey the requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Notify recipients ['design-review@company.com','ux-team@company.com'] within a single thread labeled 'Design/Changes-Requested' by issuing a request. Afterward, reflect replies as Figma comments, transition the cycle to CHANGES_REQUESTED, and append the tag 'needs-changes'.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Changes Requested: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Changes-Requested"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_cr-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-23T14:30:00Z"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-changes"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "change_request",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "CHANGES_REQUESTED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_cr-001",
                    "message_id": "msg_cr-002",
                    "tags": [
                        "needs-changes"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_007",
        "instruction": "As the design review coordinator, at the time of 2024-08-23T10:05:00Z, proceed with the same-day email-based review for the Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Inform recipients ['design-review@company.com','ux-team@company.com'] in a single thread labeled 'Design/Needs-Review', maintain identifiers deterministic and reusable, and conclude the cycle by applying quorum.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:05:00Z",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_008",
        "instruction": "As the fix item status updater at 2024-08-23T14:00:00Z, your task is to update fix items from plan_012 for audit_012: set item_017 and item_018 to APPLIED, retain item_019 and item_020 as PENDING, and document the run.",
        "actions": [
            {
                "name": "UpdateFixItemStatus",
                "arguments": {
                    "item_id": "item_017",
                    "status": "APPLIED",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "UpdateFixItemStatus",
                "arguments": {
                    "item_id": "item_018",
                    "status": "APPLIED",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fix_item_status_update",
                    "status": "completed",
                    "started_at": "2024-08-23T14:00:00Z",
                    "ended_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "up-003"
                }
            }
        ],
        "outputs": [
                "\"item_id\":\"item_017\",\"status\":\"APPLIED\"",
                "\"item_id\":\"item_018\",\"status\":\"APPLIED\"",
                "\"run_id\":\"run_up-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_009",
        "instruction": "Take on the task of generating the audit report with the current time being 2024-08-23T14:30:00Z. Aim to create a consolidated audit report for audit_012 (artifact art_001), encompassing both accessibility and design system findings. After completing the report, output it as a PDF report asset and log the run.",
        "actions": [
            {
                "name": "GenerateCombinedAuditReport",
                "arguments": {
                    "audit_id": "audit_012",
                    "artifact_id": "art_001",
                    "output_format": "PDF",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "combined_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_012\"",
                "\"artifact_id\":\"art_001\"",
                "\"report_asset_id\":\"asset_au-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_010",
        "instruction": "Assume the role of the design review coordinator at 2024-08-24T09:00:00Z; organize an email-based design review on the same day for Figma artifact art_002 ('Pricing Page \u2013 Plans Grid') following the policy. Utilize the 'PNG 2x' export, inform ['design-review@company.com','growth-team@company.com'], ensure identifiers remain consistent, and continue in the day's existing thread.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "artifact_id": "art_002",
                    "started_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-002",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_002",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "en-004"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 2 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-004"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "thread_id": "thr_em-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-004"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_002",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "up-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-24T09:00:00Z",
                    "ended_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_002-20240824-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-004",
                    "thread_id": "thr_em-004",
                    "message_id": "msg_em-005",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_011",
        "instruction": "As the fix plan delivery owner, at 2024-08-23T13:50:00Z, your task is to oversee a hybrid delivery for plan_011 on artifact art_001, adhering to policy by duplicating pending items as Figma comments and generating one ticket per pending item; once completed, inform stakeholders using the canonical digest, attach the fixplan delivery tag, and log the run while ensuring identifiers remain deterministic.",
        "actions": [
            {
                "name": "ComputeFixPlanSummary",
                "arguments": {
                    "plan_id": "plan_011",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-001"
                },
            },
            {
                "name": "DeliverFixPlan",
                "arguments": {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-002"
                },
            },
            {
                "name": "CreateTicketsForPending",
                "arguments": {
                    "plan_id": "plan_011",
                    "tracker_project": "WEBUX",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-003"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Fix Plan Delivery: plan_011 — pending items",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "FixPlan/Owners"
                    ],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_fp-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "fixplan/delivered"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-006"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fixplan_create_and_deliver",
                    "status": "completed",
                    "started_at": "2024-08-23T13:50:00Z",
                    "ended_at": "2024-08-23T13:50:00Z",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-007"
                }
            }
        ],
        "outputs": [
                {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "pending_count": 6,
                    "ticket_ids": [
                        "tix-item_011",
                        "tix-item_012",
                        "tix-item_013",
                        "tix-item_014",
                        "tix-item_015",
                        "tix-item_016"
                    ],
                    "thread_id": "thr_fp-004",
                    "message_id": "msg_fp-005",
                    "tags": [
                        "fixplan/delivered"
                    ],
                    "run_id": "run_fp-007",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_012",
        "instruction": "Serving as the audit report generator for the Web UX team at 2024-08-23T14:30:00Z, your objective is to compile a combined audit report for audit_012 (artifact art_001) incorporating both accessibility and design system findings; upon completion of the report, save it as a PDF report asset, and log the run.",
        "actions": [
            {
                "name": "GenerateCombinedAuditReport",
                "arguments": {
                    "audit_id": "audit_012",
                    "artifact_id": "art_001",
                    "output_format": "PDF",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "combined_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_012\"",
                "\"artifact_id\":\"art_001\"",
                "\"report_asset_id\":\"asset_au-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_013",
        "instruction": "As the design systems triage lead on 2024-08-14T13:00:00Z, organize a triage for the Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export. Inform the recipients ['design-systems@company.com','frontend-guild@company.com'] through a consolidated thread titled 'Design/Design-System'. Post request, replicate pertinent responses as Figma comments and label the artifact with 'ds/triage-open'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-14T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design System Triage: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "labels": [
                        "Design/Design-System"
                    ],
                    "timestamp": "2024-08-14T13:00:00Z",
                    "request_id": "ds-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_ds-002"
                    ],
                    "timestamp": "2024-08-14T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "ds/triage-open"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-14T13:00:00Z",
                    "request_id": "ds-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_systems_triage",
                    "status": "completed",
                    "started_at": "2024-08-14T13:00:00Z",
                    "ended_at": "2024-08-14T13:00:00Z",
                    "timestamp": "2024-08-14T13:00:00Z",
                    "request_id": "ds-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ds-001",
                    "message_id": "msg_ds-002",
                    "asset_id": "asset_ds-002",
                    "tags": [
                        "ds/triage-open"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_014",
        "instruction": "In your role as the design review coordinator for the Web UX H team on 2024-08-23T10:05:00Z, proceed with the same-day email-based review of Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Alert the recipients ['design-review@company.com','ux-team@company.com'] in a unified thread titled 'Design/Needs-Review', ensuring all identifiers remain consistent and repeatable. Conclude the process by applying quorum.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:05:00Z",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_015",
        "instruction": "Act as the design review coordinator for the Web UX A team by 2024-08-23T10:00:00Z; initiate a design review via email for the Figma artifact art_001 using the 'PNG 2x' export, informing recipients ['design-review@company.com','ux-team@company.com'] in a single thread with the label 'Design/Needs-Review', ensuring the identifiers remain consistent and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T10:00:00Z",
                    "ended_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_016",
        "instruction": "Serve as the release publisher for the Web UX team by 2024-08-23T11:00:00Z. With the aim to align stakeholders, disseminate a release handoff for artifact art_001, outlining changes since release_001. Attach the file using the 'PNG 2x' export profile and send it from emma.creative@company.com to ['stakeholders@company.com','product-managers@company.com']; following distribution, label the artifact 'released/2024-08-23' and document the process.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "CreateReleaseRecord",
                "arguments": {
                    "artifact_id": "art_001",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "labels": [
                        "released/2024-08-23"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:00:00Z",
                    "ended_at": "2024-08-23T11:00:00Z",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "previous_release_id": "release_001",
                    "release_id": "rel-art_001-20240823-001",
                    "asset_id": "asset_en-002",
                    "export_id": "exp-art_001-20240823-png-001",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "released/2024-08-23"
                    ],
                    "run_id": "run_rl-001",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_017",
        "instruction": "As the design review coordinator for the Web UX team, with the current time being 2024-08-24T09:00:00Z, handle a same-day email-based design review for Figma artifact art_002 ('Pricing Page \u2013 Plans Grid') according to policy. Use the 'PNG 2x' export to notify ['design-review@company.com','growth-team@company.com'], ensure deterministic identifiers, and continue using the day's existing thread.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "artifact_id": "art_002",
                    "started_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-002",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_002",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "en-004"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 2 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-004"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "thread_id": "thr_em-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-004"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_002",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "up-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-24T09:00:00Z",
                    "ended_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_002-20240824-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-004",
                    "thread_id": "thr_em-004",
                    "message_id": "msg_em-005",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_018",
        "instruction": "Serving as the accessibility audit lead with the time set to 2024-08-22T12:00:00Z, initiate an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export. Issue notifications to ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'; after the request is sent, replicate pertinent replies as Figma comments and tag the artifact with 'a11y/needs-audit'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-22T12:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Accessibility Audit: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "Design/Accessibility"
                    ],
                    "timestamp": "2024-08-22T12:00:00Z",
                    "request_id": "ax-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-22T12:00:00Z",
                    "request_id": "ax-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "a11y/needs-audit"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-22T12:00:00Z",
                    "request_id": "ax-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "accessibility_audit_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-22T12:00:00Z",
                    "ended_at": "2024-08-22T12:00:00Z",
                    "timestamp": "2024-08-22T12:00:00Z",
                    "request_id": "ax-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ax-001",
                    "message_id": "msg_ax-002",
                    "asset_id": "asset_en-002",
                    "tags": [
                        "a11y/needs-audit"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_019",
        "instruction": "As the review program manager for the Web UX team, at the time of 2024-08-23T14:00:00Z, proceed with the same-day design review for Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export. Inform recipients ['design-review@company.com','ux-team@company.com'] within the single thread titled 'Design/Needs-Review' by dispatching a reminder. Once sent, replicate replies as Figma comments, establish quorum, and ensure identifiers remain consistent and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_020",
        "instruction": "Acting as the change request lead for the Web UX H team, with the timestamp of 2024-08-23T14:30:00Z, relay the requested modifications for Figma artifact art_001 ('Homepage Hero Section') employing the 'PNG 2x' export. Notify recipients ['design-review@company.com','ux-team@company.com'] within a single thread marked 'Design/Changes-Requested' by issuing a request. After dispatching, replicate replies as Figma comments, transition the cycle to CHANGES_REQUESTED, and append the tag 'needs-changes'.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Changes Requested: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Changes-Requested"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_cr-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-23T14:30:00Z"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-changes"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "change_request",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "CHANGES_REQUESTED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_cr-001",
                    "message_id": "msg_cr-002",
                    "tags": [
                        "needs-changes"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_021",
        "instruction": "Handle the role of design review coordinator for the Web UX G team with the time set at 2024-08-23T10:05:00Z. Proceed with the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Inform the recipients ['design-review@company.com','ux-team@company.com'] in a single email thread labeled 'Design/Needs-Review', ensure identifiers remain deterministic and reusable, and conclude the cycle by achieving quorum.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:05:00Z",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_022",
        "instruction": "You are assigned as the fix item status updater with the current time being 2024-08-24T14:00:00Z. Your task is to update fix items from plan_012 for audit_012: set item_017 and item_019 to APPLIED, leave item_018 and item_020 in PENDING, and document the run.",
        "actions": [
            {
                "name": "UpdateFixItemStatus",
                "arguments": {
                    "item_id": "item_017",
                    "status": "APPLIED",
                    "timestamp": "2024-08-24T14:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "UpdateFixItemStatus",
                "arguments": {
                    "item_id": "item_019",
                    "status": "APPLIED",
                    "timestamp": "2024-08-24T14:00:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fix_item_status_update",
                    "status": "completed",
                    "started_at": "2024-08-24T14:00:00Z",
                    "ended_at": "2024-08-24T14:00:00Z",
                    "timestamp": "2024-08-24T14:00:00Z",
                    "request_id": "up-003"
                }
            }
        ],
        "outputs": [
                "\"item_id\":\"item_017\",\"status\":\"APPLIED\"",
                "\"item_id\":\"item_019\",\"status\":\"APPLIED\"",
                "\"run_id\":\"run_up-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_023",
        "instruction": "As the design review coordinator for the Web UX B team at 2024-08-23T10:00:00Z, initiate an email-based design review for Figma artifact art_001 using the 'PNG 2x' export format. Notify the recipients ['design-review@company.com','ux-team@company.com'] in a single thread under the 'Design/Needs-Review' label, ensuring identifiers remain deterministic and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T10:00:00Z",
                    "ended_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_024",
        "instruction": "Serving as the release publisher for the Web UX A team at 2024-08-23T11:00:00Z, ensure stakeholders are aligned by sharing a release handoff for artifact art_001. Summarize the changes since release_001, using the 'PNG 2x' profile for the attachment. Send the details from emma.creative@company.com to ['stakeholders@company.com','product-managers@company.com'], then tag the artifact 'released/2024-08-23' after sending and document the run.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "CreateReleaseRecord",
                "arguments": {
                    "artifact_id": "art_001",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "labels": [
                        "released/2024-08-23"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:00:00Z",
                    "ended_at": "2024-08-23T11:00:00Z",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "previous_release_id": "release_001",
                    "release_id": "rel-art_001-20240823-001",
                    "asset_id": "asset_en-002",
                    "export_id": "exp-art_001-20240823-png-001",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "released/2024-08-23"
                    ],
                    "run_id": "run_rl-001",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_025",
        "instruction": "You serve as the audit report creator for the Web UX A team, and it is currently 2024-08-23T14:30:00Z. Your task is to put together a combined audit report for audit_012 (artifact art_001) that covers both accessibility and design system findings; once the report is generated, save it as a PDF report asset and log the completion of the process.",
        "actions": [
            {
                "name": "GenerateCombinedAuditReport",
                "arguments": {
                    "audit_id": "audit_012",
                    "artifact_id": "art_001",
                    "output_format": "PDF",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "combined_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_012\"",
                "\"artifact_id\":\"art_001\"",
                "\"report_asset_id\":\"asset_au-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_026",
        "instruction": "As the lead for the accessibility audit, the time is 2024-08-21T12:00:00Z; initiate an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, and alert recipients ['accessibility@company.com','design-review@company.com'] within a single thread labeled 'Design/Accessibility'. After the request is sent, replicate pertinent replies as Figma comments, and label the artifact 'a11y/needs-audit'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-21T12:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Accessibility Audit: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "Design/Accessibility"
                    ],
                    "timestamp": "2024-08-21T12:00:00Z",
                    "request_id": "ax-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-21T12:00:00Z",
                    "request_id": "ax-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "a11y/needs-audit"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-21T12:00:00Z",
                    "request_id": "ax-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "accessibility_audit_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-21T12:00:00Z",
                    "ended_at": "2024-08-21T12:00:00Z",
                    "timestamp": "2024-08-21T12:00:00Z",
                    "request_id": "ax-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ax-001",
                    "message_id": "msg_ax-002",
                    "asset_id": "asset_en-002",
                    "tags": [
                        "a11y/needs-audit"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_027",
        "instruction": "As the change request lead for the Web UX G team, and given the time is 2024-08-23T14:30:00Z, convey the requested changes for Figma artifact art_001 ('Homepage Hero Section') by using the 'PNG 2x' export. Inform the recipients ['design-review@company.com','ux-team@company.com'] through a single thread labeled 'Design/Changes-Requested' by sending a request. After dispatching, replicate replies as Figma comments, transition the cycle to CHANGES_REQUESTED, and apply the tag 'needs-changes'.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Changes Requested: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Changes-Requested"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_cr-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-23T14:30:00Z"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-changes"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "change_request",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "CHANGES_REQUESTED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_cr-001",
                    "message_id": "msg_cr-002",
                    "tags": [
                        "needs-changes"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_028",
        "instruction": "As the design systems triage lead and considering the time is 2024-08-15T13:00:00Z, handle a triage for Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export. Notify the recipients ['design-systems@company.com','frontend-guild@company.com'] using a single thread labeled 'Design/Design-System'. Following the request dispatch, replicate pertinent replies as Figma comments, and label the artifact 'ds/triage-open'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-15T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design System Triage: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "labels": [
                        "Design/Design-System"
                    ],
                    "timestamp": "2024-08-15T13:00:00Z",
                    "request_id": "ds-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_ds-002"
                    ],
                    "timestamp": "2024-08-15T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "ds/triage-open"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-15T13:00:00Z",
                    "request_id": "ds-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_systems_triage",
                    "status": "completed",
                    "started_at": "2024-08-15T13:00:00Z",
                    "ended_at": "2024-08-15T13:00:00Z",
                    "timestamp": "2024-08-15T13:00:00Z",
                    "request_id": "ds-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ds-001",
                    "message_id": "msg_ds-002",
                    "asset_id": "asset_ds-002",
                    "tags": [
                        "ds/triage-open"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_029",
        "instruction": "As the design review coordinator for the Web UX A team, with a current time of 2024-08-24T09:00:00Z, handle a same-day email-based design review for Figma artifact art_002 ('Pricing Page \u2013 Plans Grid'). Follow policy, utilize the 'PNG 2x' export, inform ['design-review@company.com','growth-team@company.com'], ensure identifiers stay deterministic, and continue using the day's thread.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "artifact_id": "art_002",
                    "started_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-002",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_002",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "en-004"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 2 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-004"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "thread_id": "thr_em-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-004"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_002",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "up-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-24T09:00:00Z",
                    "ended_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_002-20240824-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-004",
                    "thread_id": "thr_em-004",
                    "message_id": "msg_em-005",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_030",
        "instruction": "In your role as the review program manager for the Web UX A team, with the time being 2024-08-23T14:00:00Z, coordinate the same-day design review for Figma artifact art_001 ('Homepage Hero Section') with the 'PNG 2x' export. Notify ['design-review@company.com','ux-team@company.com'] on the single thread marked 'Design/Needs-Review' by dispatching a reminder. Once sent, translate replies as Figma comments, apply quorum, and maintain identifiers deterministic and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_031",
        "instruction": "As the release publisher for the Web UX B team, and the current time is 2024-08-23T11:00:00Z, ensure stakeholders are properly aligned by distributing a release handoff for artifact art_001, summarizing modifications since release_001. Utilize export profile 'PNG 2x' for the attachment and send it from emma.creative@company.com to ['stakeholders@company.com','product-managers@company.com']; once sent, assign the tag 'released/2024-08-23' to the artifact and document the process.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "CreateReleaseRecord",
                "arguments": {
                    "artifact_id": "art_001",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "labels": [
                        "released/2024-08-23"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:00:00Z",
                    "ended_at": "2024-08-23T11:00:00Z",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "previous_release_id": "release_001",
                    "release_id": "rel-art_001-20240823-001",
                    "asset_id": "asset_en-002",
                    "export_id": "exp-art_001-20240823-png-001",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "released/2024-08-23"
                    ],
                    "run_id": "run_rl-001",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_032",
        "instruction": "Serving as the change request lead for the Web UX F team, as of 2024-08-23T14:30:00Z, convey the requested alterations for the Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export. Notify the recipients ['design-review@company.com','ux-team@company.com'] on a unified thread labeled 'Design/Changes-Requested' by dispatching a request; subsequently, replicate replies as Figma comments, transition the cycle to CHANGES_REQUESTED, and apply the tag 'needs-changes'.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Changes Requested: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Changes-Requested"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_cr-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-23T14:30:00Z"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-changes"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "change_request",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "CHANGES_REQUESTED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_cr-001",
                    "message_id": "msg_cr-002",
                    "tags": [
                        "needs-changes"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_033",
        "instruction": "As the audit report generator for the Web UX B team, and with the current time being 2024-08-23T14:30:00Z, your task is to compile a joint audit report for audit_012 (artifact art_001) that encompasses both accessibility and design system findings. Once the report has been generated, ensure it is exported as a PDF report asset and document the execution.",
        "actions": [
            {
                "name": "GenerateCombinedAuditReport",
                "arguments": {
                    "audit_id": "audit_012",
                    "artifact_id": "art_001",
                    "output_format": "PDF",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "combined_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_012\"",
                "\"artifact_id\":\"art_001\"",
                "\"report_asset_id\":\"asset_au-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_034",
        "instruction": "Acting as the fix plan delivery owner for the Web UX team with the timestamp at 2024-08-23T13:50:00Z, your aim is to organize a hybrid delivery for plan_011 on artifact art_001 in line with the policy, which involves reflecting pending items as Figma comments and generating one ticket per pending item. Upon completion, inform stakeholders by using the canonical digest, apply the fixplan delivery tag, and log the execution while ensuring identifiers are consistent.",
        "actions": [
            {
                "name": "ComputeFixPlanSummary",
                "arguments": {
                    "plan_id": "plan_011",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-001"
                },
            },
            {
                "name": "DeliverFixPlan",
                "arguments": {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-002"
                },
            },
            {
                "name": "CreateTicketsForPending",
                "arguments": {
                    "plan_id": "plan_011",
                    "tracker_project": "WEBUX",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-003"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Fix Plan Delivery: plan_011 — pending items",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "FixPlan/Owners"
                    ],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_fp-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "fixplan/delivered"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-006"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fixplan_create_and_deliver",
                    "status": "completed",
                    "started_at": "2024-08-23T13:50:00Z",
                    "ended_at": "2024-08-23T13:50:00Z",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-007"
                }
            }
        ],
        "outputs": [
                {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "pending_count": 6,
                    "ticket_ids": [
                        "tix-item_011",
                        "tix-item_012",
                        "tix-item_013",
                        "tix-item_014",
                        "tix-item_015",
                        "tix-item_016"
                    ],
                    "thread_id": "thr_fp-004",
                    "message_id": "msg_fp-005",
                    "tags": [
                        "fixplan/delivered"
                    ],
                    "run_id": "run_fp-007",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_035",
        "instruction": "As the coordinator for the Web UX F team design review, at precisely 2024-08-23T10:05:00Z, handle the continuation of the same-day email review for Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export format. Communicate with recipients ['design-review@company.com','ux-team@company.com'] on a unified thread tagged 'Design/Needs-Review'. Ensure identifiers remain fixed and reusable, and conclude the process by applying quorum.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:05:00Z",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_036",
        "instruction": "In your role as the design systems triage lead at 2024-08-16T13:00:00Z, manage a triage for the Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Contact recipients ['design-systems@company.com','frontend-guild@company.com'] through a common thread titled 'Design/Design-System'. Upon sending the request, replicate pertinent replies as comments in Figma and label the artifact as 'ds/triage-open'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-16T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design System Triage: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "labels": [
                        "Design/Design-System"
                    ],
                    "timestamp": "2024-08-16T13:00:00Z",
                    "request_id": "ds-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_ds-002"
                    ],
                    "timestamp": "2024-08-16T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "ds/triage-open"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-16T13:00:00Z",
                    "request_id": "ds-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_systems_triage",
                    "status": "completed",
                    "started_at": "2024-08-16T13:00:00Z",
                    "ended_at": "2024-08-16T13:00:00Z",
                    "timestamp": "2024-08-16T13:00:00Z",
                    "request_id": "ds-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ds-001",
                    "message_id": "msg_ds-002",
                    "asset_id": "asset_ds-002",
                    "tags": [
                        "ds/triage-open"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_037",
        "instruction": "Manage the task of updating the status of fix items, current time is 2024-08-25T14:00:00Z. Your objective is to refresh fix items from plan_012 for audit_012: set item_017 and item_020 to APPLIED, keep item_018 and item_019 as PENDING, and log the execution.",
        "actions": [
            {
                "name": "UpdateFixItemStatus",
                "arguments": {
                    "item_id": "item_017",
                    "status": "APPLIED",
                    "timestamp": "2024-08-25T14:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "UpdateFixItemStatus",
                "arguments": {
                    "item_id": "item_020",
                    "status": "APPLIED",
                    "timestamp": "2024-08-25T14:00:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fix_item_status_update",
                    "status": "completed",
                    "started_at": "2024-08-25T14:00:00Z",
                    "ended_at": "2024-08-25T14:00:00Z",
                    "timestamp": "2024-08-25T14:00:00Z",
                    "request_id": "up-003"
                }
            }
        ],
        "outputs": [
                "\"item_id\":\"item_017\",\"status\":\"APPLIED\"",
                "\"item_id\":\"item_020\",\"status\":\"APPLIED\"",
                "\"run_id\":\"run_up-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_038",
        "instruction": "Oversee the role of review program manager for the Web UX B team with the current time as 2024-08-23T14:00:00Z; proceed with the ongoing same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Inform recipients ['design-review@company.com','ux-team@company.com'] on the singular thread titled 'Design/Needs-Review' by dispatching a reminder. Following the dispatch, reflect replies as Figma comments, ensure quorum is applied, and maintain deterministic and reusable identifiers.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_039",
        "instruction": "As the design review coordinator for the Web UX C team with the time noted as 2024-08-23T10:00:00Z, initiate an email-based design review for Figma artifact art_001 using the 'PNG 2x' export. Notify the recipients ['design-review@company.com','ux-team@company.com'] on a unified thread designated as 'Design/Needs-Review' for the day, ensuring identifiers remain deterministic and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T10:00:00Z",
                    "ended_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_040",
        "instruction": "Serving as the accessibility audit lead with the time recorded as 2024-08-20T12:00:00Z, start an accessibility audit for Figma artifact art_001 ('Homepage Hero Section'), utilizing the 'PNG 2x' export. Alert the recipients ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'. After dispatching the request, replicate relevant responses as Figma comments, and label the artifact 'a11y/needs-audit'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-20T12:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Accessibility Audit: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "Design/Accessibility"
                    ],
                    "timestamp": "2024-08-20T12:00:00Z",
                    "request_id": "ax-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-20T12:00:00Z",
                    "request_id": "ax-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "a11y/needs-audit"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-20T12:00:00Z",
                    "request_id": "ax-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "accessibility_audit_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-20T12:00:00Z",
                    "ended_at": "2024-08-20T12:00:00Z",
                    "timestamp": "2024-08-20T12:00:00Z",
                    "request_id": "ax-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ax-001",
                    "message_id": "msg_ax-002",
                    "asset_id": "asset_en-002",
                    "tags": [
                        "a11y/needs-audit"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_041",
        "instruction": "As the change request lead for the Web UX E team, the time is 2024-08-23T14:30:00Z; convey requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, inform recipients ['design-review@company.com','ux-team@company.com'] within a single thread labeled 'Design/Changes-Requested' by dispatching a request; subsequent to sending, replicate replies as Figma comments, transition the cycle to CHANGES_REQUESTED, and append the tag 'needs-changes'.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Changes Requested: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Changes-Requested"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_cr-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-23T14:30:00Z"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-changes"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "change_request",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "CHANGES_REQUESTED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_cr-001",
                    "message_id": "msg_cr-002",
                    "tags": [
                        "needs-changes"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_042",
        "instruction": "As the design systems triage lead and it's 2024-08-17T13:00:00Z; organize a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, inform recipients ['design-systems@company.com','frontend-guild@company.com'] within a single thread labeled 'Design/Design-System'; upon sending the request, reflect relevant replies as Figma comments, and label the artifact 'ds/triage-open'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-17T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design System Triage: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "labels": [
                        "Design/Design-System"
                    ],
                    "timestamp": "2024-08-17T13:00:00Z",
                    "request_id": "ds-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_ds-002"
                    ],
                    "timestamp": "2024-08-17T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "ds/triage-open"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-17T13:00:00Z",
                    "request_id": "ds-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_systems_triage",
                    "status": "completed",
                    "started_at": "2024-08-17T13:00:00Z",
                    "ended_at": "2024-08-17T13:00:00Z",
                    "timestamp": "2024-08-17T13:00:00Z",
                    "request_id": "ds-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ds-001",
                    "message_id": "msg_ds-002",
                    "asset_id": "asset_ds-002",
                    "tags": [
                        "ds/triage-open"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_043",
        "instruction": "Oversee the design review coordination for the Web UX E team at 2024-08-23T10:05:00Z; maintain the same-day email-centric review for Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export. Inform recipients ['design-review@company.com','ux-team@company.com'] through a unified thread titled 'Design/Needs-Review', ensure identifiers remain deterministic and reusable, and complete the process by reaching quorum.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:05:00Z",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_044",
        "instruction": "Manage the review program for the Web UX C team at 2024-08-23T14:00:00Z; keep the same-day design evaluation for Figma artifact art_001 ('Homepage Hero Section') through the 'PNG 2x' export, alert recipients ['design-review@company.com','ux-team@company.com'] on the sole thread named 'Design/Needs-Review' with a reminder. Upon sending, convert replies to Figma comments, reach quorum, and maintain identifiers deterministic and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_045",
        "instruction": "As the accessibility audit lead with the time being 2024-08-19T12:00:00Z, initiate an accessibility audit for the Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export. Inform recipients ['accessibility@company.com','design-review@company.com'] within a single thread titled 'Design/Accessibility'; once the request is sent, replicate pertinent replies as comments in Figma, and tag the artifact with 'a11y/needs-audit'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-19T12:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Accessibility Audit: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "Design/Accessibility"
                    ],
                    "timestamp": "2024-08-19T12:00:00Z",
                    "request_id": "ax-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-19T12:00:00Z",
                    "request_id": "ax-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "a11y/needs-audit"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-19T12:00:00Z",
                    "request_id": "ax-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "accessibility_audit_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-19T12:00:00Z",
                    "ended_at": "2024-08-19T12:00:00Z",
                    "timestamp": "2024-08-19T12:00:00Z",
                    "request_id": "ax-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ax-001",
                    "message_id": "msg_ax-002",
                    "asset_id": "asset_en-002",
                    "tags": [
                        "a11y/needs-audit"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_046",
        "instruction": "Being the fix plan delivery owner for the Web UX A team at the time 2024-08-23T13:50:00Z, your task is to oversee a hybrid delivery for plan_011 on artifact art_001 according to policy by copying pending items as Figma comments and generating one ticket per pending item. Upon completion, inform stakeholders through the canonical digest, apply the fixplan delivery tag, and document the run while ensuring identifiers remain consistent.",
        "actions": [
            {
                "name": "ComputeFixPlanSummary",
                "arguments": {
                    "plan_id": "plan_011",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-001"
                },
            },
            {
                "name": "DeliverFixPlan",
                "arguments": {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-002"
                },
            },
            {
                "name": "CreateTicketsForPending",
                "arguments": {
                    "plan_id": "plan_011",
                    "tracker_project": "WEBUX",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-003"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Fix Plan Delivery: plan_011 — pending items",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "FixPlan/Owners"
                    ],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_fp-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "fixplan/delivered"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-006"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fixplan_create_and_deliver",
                    "status": "completed",
                    "started_at": "2024-08-23T13:50:00Z",
                    "ended_at": "2024-08-23T13:50:00Z",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-007"
                }
            }
        ],
        "outputs": [
                {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "pending_count": 6,
                    "ticket_ids": [
                        "tix-item_011",
                        "tix-item_012",
                        "tix-item_013",
                        "tix-item_014",
                        "tix-item_015",
                        "tix-item_016"
                    ],
                    "thread_id": "thr_fp-004",
                    "message_id": "msg_fp-005",
                    "tags": [
                        "fixplan/delivered"
                    ],
                    "run_id": "run_fp-007",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_047",
        "instruction": "As the coordinator overseeing the design review for the Web UX D team, and with the current time being 2024-08-23T10:00:00Z, initiate a design review via email for Figma artifact art_001 utilizing the 'PNG 2x' export. Notify the recipients ['design-review@company.com','ux-team@company.com'] in a single email thread titled 'Design/Needs-Review', ensuring all identifiers are consistent and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T10:00:00Z",
                    "ended_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_048",
        "instruction": "In your role as the release publisher for the Web UX C team, at the designated time of 2024-08-23T11:00:00Z, align product stakeholders by distributing a release handoff for artifact art_001, with a summary of changes following release_001. Attach the document using export profile 'PNG 2x' and email it from emma.creative@company.com to the specified contacts ['stakeholders@company.com','product-managers@company.com']. Once sent, mark the artifact as 'released/2024-08-23' and log the execution.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "CreateReleaseRecord",
                "arguments": {
                    "artifact_id": "art_001",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "labels": [
                        "released/2024-08-23"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:00:00Z",
                    "ended_at": "2024-08-23T11:00:00Z",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "previous_release_id": "release_001",
                    "release_id": "rel-art_001-20240823-001",
                    "asset_id": "asset_en-002",
                    "export_id": "exp-art_001-20240823-png-001",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "released/2024-08-23"
                    ],
                    "run_id": "run_rl-001",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_049",
        "instruction": "As the audit report generator for the Web UX C team, with the current time being 2024-08-23T14:30:00Z, your objective is to compile a combined audit report for audit_012 (artifact art_001), incorporating both accessibility and design system findings. Once the report is compiled, export it as a PDF report asset and document the execution.",
        "actions": [
            {
                "name": "GenerateCombinedAuditReport",
                "arguments": {
                    "audit_id": "audit_012",
                    "artifact_id": "art_001",
                    "output_format": "PDF",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "combined_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_012\"",
                "\"artifact_id\":\"art_001\"",
                "\"report_asset_id\":\"asset_au-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_050",
        "instruction": "Being the fix plan delivery owner for the Web UX B team, and noting the time as 2024-08-23T13:50:00Z, your objective is to manage a hybrid delivery for plan_011 on artifact art_001 in compliance with policy. Achieve this by reflecting pending items as Figma comments and generating one ticket per pending item. Upon completion, inform stakeholders with the canonical digest, apply the fixplan delivery tag, and log the process while ensuring identifiers remain deterministic.",
        "actions": [
            {
                "name": "ComputeFixPlanSummary",
                "arguments": {
                    "plan_id": "plan_011",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-001"
                },
            },
            {
                "name": "DeliverFixPlan",
                "arguments": {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-002"
                },
            },
            {
                "name": "CreateTicketsForPending",
                "arguments": {
                    "plan_id": "plan_011",
                    "tracker_project": "WEBUX",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-003"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Fix Plan Delivery: plan_011 — pending items",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "FixPlan/Owners"
                    ],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_fp-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "fixplan/delivered"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-006"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fixplan_create_and_deliver",
                    "status": "completed",
                    "started_at": "2024-08-23T13:50:00Z",
                    "ended_at": "2024-08-23T13:50:00Z",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-007"
                }
            }
        ],
        "outputs": [
                {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "pending_count": 6,
                    "ticket_ids": [
                        "tix-item_011",
                        "tix-item_012",
                        "tix-item_013",
                        "tix-item_014",
                        "tix-item_015",
                        "tix-item_016"
                    ],
                    "thread_id": "thr_fp-004",
                    "message_id": "msg_fp-005",
                    "tags": [
                        "fixplan/delivered"
                    ],
                    "run_id": "run_fp-007",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_051",
        "instruction": "As the lead for the accessibility audit, with the time set at 2024-08-18T12:00:00Z, initiate an accessibility audit of the Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Notify the recipients ['accessibility@company.com','design-review@company.com'] in a unified thread labeled 'Design/Accessibility'. After dispatching the request, replicate pertinent replies as Figma comments and mark the artifact with 'a11y/needs-audit'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-18T12:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Accessibility Audit: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "Design/Accessibility"
                    ],
                    "timestamp": "2024-08-18T12:00:00Z",
                    "request_id": "ax-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-18T12:00:00Z",
                    "request_id": "ax-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "a11y/needs-audit"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-18T12:00:00Z",
                    "request_id": "ax-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "accessibility_audit_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-18T12:00:00Z",
                    "ended_at": "2024-08-18T12:00:00Z",
                    "timestamp": "2024-08-18T12:00:00Z",
                    "request_id": "ax-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ax-001",
                    "message_id": "msg_ax-002",
                    "asset_id": "asset_en-002",
                    "tags": [
                        "a11y/needs-audit"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_052",
        "instruction": "Acting as the coordinator for the Web UX E team design review, at 2024-08-23T10:00:00Z, start an email-based design review of the Figma artifact art_001 using the 'PNG 2x' export. Inform the recipients ['design-review@company.com','ux-team@company.com'] in a combined thread for that day labeled 'Design/Needs-Review', ensuring all identifiers remain deterministic and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T10:00:00Z",
                    "ended_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_053",
        "instruction": "You are tasked as the release publisher for the Web UX D team, and the current time is 2024-08-23T11:00:00Z. Product requires stakeholder alignment\u2014provide a release handoff for artifact art_001, detailing changes since release_001. Utilize export profile 'PNG 2x' for the attachment and dispatch it from emma.creative@company.com to ['stakeholders@company.com','product-managers@company.com']; following the dispatch, label the artifact 'released/2024-08-23' and document the execution.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "CreateReleaseRecord",
                "arguments": {
                    "artifact_id": "art_001",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "labels": [
                        "released/2024-08-23"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:00:00Z",
                    "ended_at": "2024-08-23T11:00:00Z",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "previous_release_id": "release_001",
                    "release_id": "rel-art_001-20240823-001",
                    "asset_id": "asset_en-002",
                    "export_id": "exp-art_001-20240823-png-001",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "released/2024-08-23"
                    ],
                    "run_id": "run_rl-001",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_054",
        "instruction": "As the design review coordinator for the Web UX B team, at 2024-08-24T09:00:00Z, oversee a same-day email-based design review for Figma artifact art_002 ('Pricing Page \u2013 Plans Grid') according to policy, using the 'PNG 2x' export, and inform ['design-review@company.com','growth-team@company.com'], ensuring identifiers remain consistent and the day's thread is reused.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "artifact_id": "art_002",
                    "started_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-002",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_002",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "en-004"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 2 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-004"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "thread_id": "thr_em-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-004"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_002",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "up-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-24T09:00:00Z",
                    "ended_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_002-20240824-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-004",
                    "thread_id": "thr_em-004",
                    "message_id": "msg_em-005",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_055",
        "instruction": "Act as the fix item status updater with the time set at 2024-08-26T14:00:00Z. Your objective is to update fix items from plan_012 for audit_012: classify item_018 and item_019 as APPLIED, keep item_017 and item_020 as PENDING, and log the run.",
        "actions": [
            {
                "name": "UpdateFixItemStatus",
                "arguments": {
                    "item_id": "item_018",
                    "status": "APPLIED",
                    "timestamp": "2024-08-26T14:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "UpdateFixItemStatus",
                "arguments": {
                    "item_id": "item_019",
                    "status": "APPLIED",
                    "timestamp": "2024-08-26T14:00:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fix_item_status_update",
                    "status": "completed",
                    "started_at": "2024-08-26T14:00:00Z",
                    "ended_at": "2024-08-26T14:00:00Z",
                    "timestamp": "2024-08-26T14:00:00Z",
                    "request_id": "up-003"
                }
            }
        ],
        "outputs": [
                "\"item_id\":\"item_018\",\"status\":\"APPLIED\"",
                "\"item_id\":\"item_019\",\"status\":\"APPLIED\"",
                "\"run_id\":\"run_up-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_056",
        "instruction": "Take the role of review program manager for the Web UX D team with the time being 2024-08-23T14:00:00Z; proceed with the same-day design review of Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Inform recipients ['design-review@company.com','ux-team@company.com'] on the single thread tagged 'Design/Needs-Review' by dispatching a reminder. Following the send, reflect replies as comments in Figma, implement quorum, ensuring identifiers remain deterministic and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_057",
        "instruction": "As the design systems triage lead at 2024-08-18T13:00:00Z, handle a triage for Figma artifact art_001 ('Homepage Hero Section') employing the 'PNG 2x' export. Notify the recipients ['design-systems@company.com','frontend-guild@company.com'] in a single thread titled 'Design/Design-System'. Once the request is dispatched, replicate relevant responses as Figma comments and label the artifact as 'ds/triage-open'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-18T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design System Triage: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "labels": [
                        "Design/Design-System"
                    ],
                    "timestamp": "2024-08-18T13:00:00Z",
                    "request_id": "ds-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_ds-002"
                    ],
                    "timestamp": "2024-08-18T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "ds/triage-open"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-18T13:00:00Z",
                    "request_id": "ds-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_systems_triage",
                    "status": "completed",
                    "started_at": "2024-08-18T13:00:00Z",
                    "ended_at": "2024-08-18T13:00:00Z",
                    "timestamp": "2024-08-18T13:00:00Z",
                    "request_id": "ds-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ds-001",
                    "message_id": "msg_ds-002",
                    "asset_id": "asset_ds-002",
                    "tags": [
                        "ds/triage-open"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_058",
        "instruction": "Being the design review coordinator for the Web UX D team at 2024-08-23T10:05:00Z, proceed with the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export. Notify the recipients ['design-review@company.com','ux-team@company.com'] within a single thread labeled 'Design/Needs-Review', ensure identifiers remain deterministic and reusable, and conclude the cycle by implementing quorum.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:05:00Z",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_059",
        "instruction": "As the change request lead for the Web UX D team, the time being 2024-08-23T14:30:00Z, communicate the requested changes for the Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export. Alert the recipients ['design-review@company.com','ux-team@company.com'] on a unified thread titled 'Design/Changes-Requested' by dispatching a request; once sent, reflect replies as Figma comments, transition the cycle to CHANGES_REQUESTED, and append the tag 'needs-changes'.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Changes Requested: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Changes-Requested"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_cr-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-23T14:30:00Z"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-changes"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "change_request",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "CHANGES_REQUESTED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_cr-001",
                    "message_id": "msg_cr-002",
                    "tags": [
                        "needs-changes"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_060",
        "instruction": "In your role as the audit report generator for the Web UX D team, at the time of 2024-08-23T14:30:00Z, coordinate the creation of a combined audit report for audit_012 (artifact art_001), incorporating both accessibility and design system findings. Following the report generation, export it as a PDF report asset and document the completed run.",
        "actions": [
            {
                "name": "GenerateCombinedAuditReport",
                "arguments": {
                    "audit_id": "audit_012",
                    "artifact_id": "art_001",
                    "output_format": "PDF",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "combined_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_012\"",
                "\"artifact_id\":\"art_001\"",
                "\"report_asset_id\":\"asset_au-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_061",
        "instruction": "You have the role of design review coordinator for the Web UX C team, and the time is 2024-08-24T09:00:00Z; conduct a same-day email-based design review for Figma artifact art_002 ('Pricing Page \u2013 Plans Grid') in compliance with policy, using the 'PNG 2x' export, and inform ['design-review@company.com','growth-team@company.com'], ensuring identifiers remain deterministic, and utilizing the day's thread.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "artifact_id": "art_002",
                    "started_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-002",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_002",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "en-004"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 2 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-004"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "thread_id": "thr_em-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-004"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_002",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "up-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-24T09:00:00Z",
                    "ended_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_002-20240824-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-004",
                    "thread_id": "thr_em-004",
                    "message_id": "msg_em-005",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_062",
        "instruction": "As the review program manager for the Web UX E team, and with the current time being 2024-08-23T14:00:00Z; carry on with the same-day design review for Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export. Communicate with recipients ['design-review@company.com','ux-team@company.com'] using the single thread labeled 'Design/Needs-Review' by issuing a reminder. Subsequently, replicate replies as Figma comments, implement quorum, and ensure identifiers remain deterministic and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_063",
        "instruction": "You hold the responsibility for executing the fix plan delivery for the Web UX C team as of 2024-08-23T13:50:00Z. Your aim is to organize a hybrid delivery for plan_011 on artifact art_001 in line with policy by replicating pending items as Figma comments and generating a ticket for each pending item; once complete, inform stakeholders through the canonical digest, apply the fixplan delivery tag, and log the run, ensuring that identifiers remain deterministic.",
        "actions": [
            {
                "name": "ComputeFixPlanSummary",
                "arguments": {
                    "plan_id": "plan_011",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-001"
                },
            },
            {
                "name": "DeliverFixPlan",
                "arguments": {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-002"
                },
            },
            {
                "name": "CreateTicketsForPending",
                "arguments": {
                    "plan_id": "plan_011",
                    "tracker_project": "WEBUX",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-003"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Fix Plan Delivery: plan_011 — pending items",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "FixPlan/Owners"
                    ],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_fp-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "fixplan/delivered"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-006"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fixplan_create_and_deliver",
                    "status": "completed",
                    "started_at": "2024-08-23T13:50:00Z",
                    "ended_at": "2024-08-23T13:50:00Z",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-007"
                }
            }
        ],
        "outputs": [
                {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "pending_count": 6,
                    "ticket_ids": [
                        "tix-item_011",
                        "tix-item_012",
                        "tix-item_013",
                        "tix-item_014",
                        "tix-item_015",
                        "tix-item_016"
                    ],
                    "thread_id": "thr_fp-004",
                    "message_id": "msg_fp-005",
                    "tags": [
                        "fixplan/delivered"
                    ],
                    "run_id": "run_fp-007",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_064",
        "instruction": "You serve as the design review coordinator for the Web UX F team with the time set at 2024-08-23T10:00:00Z; initiate an email-based design review for Figma artifact art_001 utilizing the 'PNG 2x' export, alert recipients ['design-review@company.com','ux-team@company.com'] on a single thread for the day marked 'Design/Needs-Review', and ensure that identifiers are deterministic and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T10:00:00Z",
                    "ended_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_065",
        "instruction": "Act as the release publisher for the Web UX E team, considering the time is 2024-08-23T11:00:00Z. Product needs stakeholder alignment\u2014provide a release handoff for artifact art_001, detailing changes since release_001. Utilize the export profile 'PNG 2x' for the attachment and dispatch it from emma.creative@company.com to ['stakeholders@company.com','product-managers@company.com']; once dispatched, label the artifact 'released/2024-08-23' and document the process.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "CreateReleaseRecord",
                "arguments": {
                    "artifact_id": "art_001",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "labels": [
                        "released/2024-08-23"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:00:00Z",
                    "ended_at": "2024-08-23T11:00:00Z",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "previous_release_id": "release_001",
                    "release_id": "rel-art_001-20240823-001",
                    "asset_id": "asset_en-002",
                    "export_id": "exp-art_001-20240823-png-001",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "released/2024-08-23"
                    ],
                    "run_id": "run_rl-001",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_066",
        "instruction": "Function as the design review coordinator for the Web UX C team, given the time is 2024-08-23T10:05:00Z; proceed with the same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') by employing the 'PNG 2x' export. Inform recipients ['design-review@company.com','ux-team@company.com'] in a unified thread titled 'Design/Needs-Review', ensuring identifiers remain deterministic and reusable, and conclude the cycle by implementing quorum.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:05:00Z",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_067",
        "instruction": "Act as the audit report generator for the Web UX E team with the current time set to 2024-08-23T14:30:00Z. Your objective is to create a combined audit report for audit_012 (artifact art_001) that includes both accessibility and design system findings; subsequently, export this as a PDF report asset, and ensure the run is documented.",
        "actions": [
            {
                "name": "GenerateCombinedAuditReport",
                "arguments": {
                    "audit_id": "audit_012",
                    "artifact_id": "art_001",
                    "output_format": "PDF",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "combined_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_012\"",
                "\"artifact_id\":\"art_001\"",
                "\"report_asset_id\":\"asset_au-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_068",
        "instruction": "Serve as the change request lead for the Web UX C team with the current time of 2024-08-23T14:30:00Z; facilitate the communication of requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, and alert recipients ['design-review@company.com','ux-team@company.com'] on a unified thread labeled 'Design/Changes-Requested' by dispatching a request; subsequently, reflect replies as Figma comments, transition the cycle to CHANGES_REQUESTED, and attach the tag 'needs-changes'.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Changes Requested: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Changes-Requested"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_cr-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-23T14:30:00Z"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-changes"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "change_request",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "CHANGES_REQUESTED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_cr-001",
                    "message_id": "msg_cr-002",
                    "tags": [
                        "needs-changes"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_069",
        "instruction": "As the leader of the accessibility audit, the specified time is 2024-08-17T12:00:00Z; initiate an accessibility audit for the Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Notify the recipients ['accessibility@company.com','design-review@company.com'] within a single thread labeled 'Design/Accessibility'. After sending out the request, replicate relevant responses as Figma comments and tag the artifact 'a11y/needs-audit'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-17T12:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Accessibility Audit: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "Design/Accessibility"
                    ],
                    "timestamp": "2024-08-17T12:00:00Z",
                    "request_id": "ax-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-17T12:00:00Z",
                    "request_id": "ax-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "a11y/needs-audit"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-17T12:00:00Z",
                    "request_id": "ax-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "accessibility_audit_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-17T12:00:00Z",
                    "ended_at": "2024-08-17T12:00:00Z",
                    "timestamp": "2024-08-17T12:00:00Z",
                    "request_id": "ax-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ax-001",
                    "message_id": "msg_ax-002",
                    "asset_id": "asset_en-002",
                    "tags": [
                        "a11y/needs-audit"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_070",
        "instruction": "Being the design systems triage lead and the time set for 2024-08-19T13:00:00Z; take charge of a triage for the Figma artifact art_001 ('Homepage Hero Section') with the 'PNG 2x' export. Inform recipients ['design-systems@company.com','frontend-guild@company.com'] via a singular thread labeled 'Design/Design-System'. Once the request is sent, replicate pertinent replies as Figma comments and mark the artifact with 'ds/triage-open'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-19T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design System Triage: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "labels": [
                        "Design/Design-System"
                    ],
                    "timestamp": "2024-08-19T13:00:00Z",
                    "request_id": "ds-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_ds-002"
                    ],
                    "timestamp": "2024-08-19T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "ds/triage-open"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-19T13:00:00Z",
                    "request_id": "ds-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_systems_triage",
                    "status": "completed",
                    "started_at": "2024-08-19T13:00:00Z",
                    "ended_at": "2024-08-19T13:00:00Z",
                    "timestamp": "2024-08-19T13:00:00Z",
                    "request_id": "ds-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ds-001",
                    "message_id": "msg_ds-002",
                    "asset_id": "asset_ds-002",
                    "tags": [
                        "ds/triage-open"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_071",
        "instruction": "As the fix plan delivery owner for the Web UX D team, operating at 2024-08-23T13:50:00Z, your objective is to manage a hybrid delivery for plan_011 on artifact art_001 in line with policy. Achieve this by reflecting pending items as Figma comments, generating one ticket per pending item, and subsequently informing stakeholders using the canonical digest. Make sure to add the fixplan delivery tag, record the run, and ensure identifiers remain deterministic.",
        "actions": [
            {
                "name": "ComputeFixPlanSummary",
                "arguments": {
                    "plan_id": "plan_011",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-001"
                },
            },
            {
                "name": "DeliverFixPlan",
                "arguments": {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-002"
                },
            },
            {
                "name": "CreateTicketsForPending",
                "arguments": {
                    "plan_id": "plan_011",
                    "tracker_project": "WEBUX",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-003"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Fix Plan Delivery: plan_011 — pending items",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "FixPlan/Owners"
                    ],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_fp-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "fixplan/delivered"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-006"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fixplan_create_and_deliver",
                    "status": "completed",
                    "started_at": "2024-08-23T13:50:00Z",
                    "ended_at": "2024-08-23T13:50:00Z",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-007"
                }
            }
        ],
        "outputs": [
                {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "pending_count": 6,
                    "ticket_ids": [
                        "tix-item_011",
                        "tix-item_012",
                        "tix-item_013",
                        "tix-item_014",
                        "tix-item_015",
                        "tix-item_016"
                    ],
                    "thread_id": "thr_fp-004",
                    "message_id": "msg_fp-005",
                    "tags": [
                        "fixplan/delivered"
                    ],
                    "run_id": "run_fp-007",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_072",
        "instruction": "Serving as the design review coordinator for the Web UX B team at 2024-08-23T10:05:00Z, carry on with the email-based review for the same day on Figma artifact art_001 ('Homepage Hero Section'), utilizing the 'PNG 2x' export. Inform recipients ['design-review@company.com','ux-team@company.com'] on a unified thread marked 'Design/Needs-Review', maintaining identifiers as deterministic and reusable, and conclude the cycle by establishing quorum.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:05:00Z",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_073",
        "instruction": "As the fix item status updater, with the current time being 2024-08-27T14:00:00Z, your aim is to update fix items from plan_012 for audit_012: label item_018 and item_020 as APPLIED, keep item_017 and item_019 as PENDING, and log the execution.",
        "actions": [
            {
                "name": "UpdateFixItemStatus",
                "arguments": {
                    "item_id": "item_018",
                    "status": "APPLIED",
                    "timestamp": "2024-08-27T14:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "UpdateFixItemStatus",
                "arguments": {
                    "item_id": "item_020",
                    "status": "APPLIED",
                    "timestamp": "2024-08-27T14:00:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fix_item_status_update",
                    "status": "completed",
                    "started_at": "2024-08-27T14:00:00Z",
                    "ended_at": "2024-08-27T14:00:00Z",
                    "timestamp": "2024-08-27T14:00:00Z",
                    "request_id": "up-003"
                }
            }
        ],
        "outputs": [
                "\"item_id\":\"item_018\",\"status\":\"APPLIED\"",
                "\"item_id\":\"item_020\",\"status\":\"APPLIED\"",
                "\"run_id\":\"run_up-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_074",
        "instruction": "Serving as the accessibility audit lead at 2024-08-16T12:00:00Z, initiate an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') by using the 'PNG 2x' export, inform recipients ['accessibility@company.com','design-review@company.com'] in a unified thread titled 'Design/Accessibility'; subsequent to dispatching the request, replicate pertinent responses as Figma comments, tagging the artifact 'a11y/needs-audit'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-16T12:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Accessibility Audit: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "Design/Accessibility"
                    ],
                    "timestamp": "2024-08-16T12:00:00Z",
                    "request_id": "ax-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-16T12:00:00Z",
                    "request_id": "ax-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "a11y/needs-audit"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-16T12:00:00Z",
                    "request_id": "ax-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "accessibility_audit_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-16T12:00:00Z",
                    "ended_at": "2024-08-16T12:00:00Z",
                    "timestamp": "2024-08-16T12:00:00Z",
                    "request_id": "ax-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ax-001",
                    "message_id": "msg_ax-002",
                    "asset_id": "asset_en-002",
                    "tags": [
                        "a11y/needs-audit"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_075",
        "instruction": "As the change request lead for the Web UX B team, at the time 2024-08-23T14:30:00Z, convey requested modifications for Figma artifact art_001 ('Homepage Hero Section') by utilizing the 'PNG 2x' export. Alert recipients ['design-review@company.com','ux-team@company.com'] through a single thread titled 'Design/Changes-Requested' by dispatching a request. Upon sending, replicate replies as Figma comments, transition the cycle to CHANGES_REQUESTED, and attach the tag 'needs-changes'.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Changes Requested: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Changes-Requested"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_cr-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-23T14:30:00Z"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-changes"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "change_request",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "CHANGES_REQUESTED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_cr-001",
                    "message_id": "msg_cr-002",
                    "tags": [
                        "needs-changes"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_076",
        "instruction": "As the audit report generator for the Web UX F team at the time 2024-08-23T14:30:00Z, your task is to create a joint audit report for audit_012 (artifact art_001), covering both accessibility and design system findings. Upon completion, export it as a PDF report asset and log the run.",
        "actions": [
            {
                "name": "GenerateCombinedAuditReport",
                "arguments": {
                    "audit_id": "audit_012",
                    "artifact_id": "art_001",
                    "output_format": "PDF",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "combined_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_012\"",
                "\"artifact_id\":\"art_001\"",
                "\"report_asset_id\":\"asset_au-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_077",
        "instruction": "As the review program manager for the Web UX F team, and with the current time being 2024-08-23T14:00:00Z, proceed with the same-day design review of Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export. Ensure to notify recipients ['design-review@company.com','ux-team@company.com'] through a single thread labeled 'Design/Needs-Review' by sending a reminder. Following the dispatch, reflect any replies as Figma comments, apply quorum, and maintain identifiers both deterministic and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_078",
        "instruction": "As the design review coordinator for the Web UX G team, at the time of 2024-08-23T10:00:00Z, initiate an email-based design review for Figma artifact art_001 using the 'PNG 2x' export. Notify the designated recipients ['design-review@company.com','ux-team@company.com'] in a single thread for the day labeled 'Design/Needs-Review', ensuring that identifiers are both deterministic and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T10:00:00Z",
                    "ended_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_079",
        "instruction": "Act as the design systems triage lead with the time set to 2024-08-20T13:00:00Z; handle a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, and inform recipients ['design-systems@company.com','frontend-guild@company.com'] within a single thread with the label 'Design/Design-System'. After dispatching the request, replicate pertinent replies as Figma comments, tagging the artifact as 'ds/triage-open'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-20T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design System Triage: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "labels": [
                        "Design/Design-System"
                    ],
                    "timestamp": "2024-08-20T13:00:00Z",
                    "request_id": "ds-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_ds-002"
                    ],
                    "timestamp": "2024-08-20T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "ds/triage-open"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-20T13:00:00Z",
                    "request_id": "ds-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_systems_triage",
                    "status": "completed",
                    "started_at": "2024-08-20T13:00:00Z",
                    "ended_at": "2024-08-20T13:00:00Z",
                    "timestamp": "2024-08-20T13:00:00Z",
                    "request_id": "ds-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ds-001",
                    "message_id": "msg_ds-002",
                    "asset_id": "asset_ds-002",
                    "tags": [
                        "ds/triage-open"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_080",
        "instruction": "Assume the role of release publisher for the Web UX F team with the moment marked as 2024-08-23T11:00:00Z. Ensure product stakeholders are aligned by distributing a release handoff for artifact art_001, summarizing modifications since release_001. Attach using the export profile 'PNG 2x' and dispatch from emma.creative@company.com to ['stakeholders@company.com','product-managers@company.com']; upon sending, label the artifact 'released/2024-08-23' and note the execution.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "CreateReleaseRecord",
                "arguments": {
                    "artifact_id": "art_001",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "labels": [
                        "released/2024-08-23"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:00:00Z",
                    "ended_at": "2024-08-23T11:00:00Z",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "previous_release_id": "release_001",
                    "release_id": "rel-art_001-20240823-001",
                    "asset_id": "asset_en-002",
                    "export_id": "exp-art_001-20240823-png-001",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "released/2024-08-23"
                    ],
                    "run_id": "run_rl-001",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_081",
        "instruction": "Act as the review program manager for the Web UX G team, considering the time is 2024-08-23T14:00:00Z. Proceed with the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Inform recipients ['design-review@company.com','ux-team@company.com'] on the single thread with the label 'Design/Needs-Review' by dispatching a reminder. Once sent, reflect replies as Figma comments, apply quorum, and maintain deterministic and reusable identifiers.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_082",
        "instruction": "Perform the role of audit report generator for the Web UX G team, with the current time being 2024-08-23T14:30:00Z. Your task is to produce a combined audit report for audit_012 (artifact art_001), covering both accessibility and design system findings. After preparing the report, export it as a PDF report asset and log the run.",
        "actions": [
            {
                "name": "GenerateCombinedAuditReport",
                "arguments": {
                    "audit_id": "audit_012",
                    "artifact_id": "art_001",
                    "output_format": "PDF",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "combined_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_012\"",
                "\"artifact_id\":\"art_001\"",
                "\"report_asset_id\":\"asset_au-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_083",
        "instruction": "As the change request lead for the Web UX A team, at the time of 2024-08-23T14:30:00Z, handle the communication of requested changes for Figma artifact art_001 ('Homepage Hero Section') utilizing the 'PNG 2x' export. Notify the recipients ['design-review@company.com','ux-team@company.com'] within a single thread labeled 'Design/Changes-Requested' by sending a request. After dispatching the request, reflect replies as Figma comments, transition the cycle to CHANGES_REQUESTED, and apply the tag 'needs-changes'.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Changes Requested: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Changes-Requested"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_cr-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-23T14:30:00Z"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-changes"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "change_request",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "CHANGES_REQUESTED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_cr-001",
                    "message_id": "msg_cr-002",
                    "tags": [
                        "needs-changes"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_084",
        "instruction": "As the fix plan delivery owner for the Web UX E team, at the time 2024-08-23T13:50:00Z, your objective is to coordinate a hybrid delivery for plan_011 on artifact art_001 in line with policy. This involves mirroring pending items as Figma comments and generating one ticket per pending item. Upon completion, inform stakeholders through the canonical digest, add the fixplan delivery tag, and document the run while maintaining deterministic identifiers.",
        "actions": [
            {
                "name": "ComputeFixPlanSummary",
                "arguments": {
                    "plan_id": "plan_011",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-001"
                },
            },
            {
                "name": "DeliverFixPlan",
                "arguments": {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-002"
                },
            },
            {
                "name": "CreateTicketsForPending",
                "arguments": {
                    "plan_id": "plan_011",
                    "tracker_project": "WEBUX",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-003"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Fix Plan Delivery: plan_011 — pending items",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "FixPlan/Owners"
                    ],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_fp-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "fix-owners@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "fixplan/delivered"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-006"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fixplan_create_and_deliver",
                    "status": "completed",
                    "started_at": "2024-08-23T13:50:00Z",
                    "ended_at": "2024-08-23T13:50:00Z",
                    "timestamp": "2024-08-23T13:50:00Z",
                    "request_id": "fp-007"
                }
            }
        ],
        "outputs": [
                {
                    "plan_id": "plan_011",
                    "delivery_method": "COMMENTS",
                    "pending_count": 6,
                    "ticket_ids": [
                        "tix-item_011",
                        "tix-item_012",
                        "tix-item_013",
                        "tix-item_014",
                        "tix-item_015",
                        "tix-item_016"
                    ],
                    "thread_id": "thr_fp-004",
                    "message_id": "msg_fp-005",
                    "tags": [
                        "fixplan/delivered"
                    ],
                    "run_id": "run_fp-007",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_085",
        "instruction": "As the design systems triage lead, the time currently is 2024-08-21T13:00:00Z. Handle a triage for the Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Inform the recipients ['design-systems@company.com','frontend-guild@company.com'] within a single thread titled 'Design/Design-System'. Once the request is sent, replicate significant replies as Figma comments and label the artifact 'ds/triage-open'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-21T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design System Triage: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "labels": [
                        "Design/Design-System"
                    ],
                    "timestamp": "2024-08-21T13:00:00Z",
                    "request_id": "ds-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_ds-002"
                    ],
                    "timestamp": "2024-08-21T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "ds/triage-open"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-21T13:00:00Z",
                    "request_id": "ds-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_systems_triage",
                    "status": "completed",
                    "started_at": "2024-08-21T13:00:00Z",
                    "ended_at": "2024-08-21T13:00:00Z",
                    "timestamp": "2024-08-21T13:00:00Z",
                    "request_id": "ds-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ds-001",
                    "message_id": "msg_ds-002",
                    "asset_id": "asset_ds-002",
                    "tags": [
                        "ds/triage-open"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_086",
        "instruction": "Being the design review coordinator for the Web UX H team and currently it's 2024-08-23T10:00:00Z, initiate an email-based design review for the Figma artifact art_001 utilizing the 'PNG 2x' export. Alert the recipients ['design-review@company.com','ux-team@company.com'] within a single thread for the day titled 'Design/Needs-Review', ensuring identifiers are consistent and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T10:00:00Z",
                    "ended_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_087",
        "instruction": "As the accessibility audit lead, with the time set at 2024-08-15T12:00:00Z, initiate an accessibility audit for the Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Notify recipients at ['accessibility@company.com','design-review@company.com'] in a single labeled thread 'Design/Accessibility'. Once the request is sent, reflect relevant replies as Figma comments and tag the artifact with 'a11y/needs-audit'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-15T12:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Accessibility Audit: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "Design/Accessibility"
                    ],
                    "timestamp": "2024-08-15T12:00:00Z",
                    "request_id": "ax-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-15T12:00:00Z",
                    "request_id": "ax-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "a11y/needs-audit"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-15T12:00:00Z",
                    "request_id": "ax-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "accessibility_audit_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-15T12:00:00Z",
                    "ended_at": "2024-08-15T12:00:00Z",
                    "timestamp": "2024-08-15T12:00:00Z",
                    "request_id": "ax-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ax-001",
                    "message_id": "msg_ax-002",
                    "asset_id": "asset_en-002",
                    "tags": [
                        "a11y/needs-audit"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_088",
        "instruction": "Being the design review coordinator for the Web UX D team, and at the time 2024-08-24T09:00:00Z, conduct a same-day email-based design review for the Figma artifact art_002 ('Pricing Page \u2013 Plans Grid') per policy, using the 'PNG 2x' export. Notify ['design-review@company.com','growth-team@company.com'], ensure identifiers remain deterministic, and maintain the day's thread for reuse.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "artifact_id": "art_002",
                    "started_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-002",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_002",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "en-004"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 2 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-004"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "thread_id": "thr_em-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-004"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_002",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "up-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-24T09:00:00Z",
                    "ended_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_002-20240824-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-004",
                    "thread_id": "thr_em-004",
                    "message_id": "msg_em-005",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_089",
        "instruction": "You are the release publisher for the Web UX G team and it is 2024-08-23T11:00:00Z. Product needs stakeholders aligned\u2014distribute a release handoff for artifact art_001, summarizing changes since release_001. Employ export profile 'PNG 2x' for the attachment and transmit from emma.creative@company.com to ['stakeholders@company.com','product-managers@company.com']; once sent, tag the artifact 'released/2024-08-23' and document the run.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "CreateReleaseRecord",
                "arguments": {
                    "artifact_id": "art_001",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "labels": [
                        "released/2024-08-23"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:00:00Z",
                    "ended_at": "2024-08-23T11:00:00Z",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "previous_release_id": "release_001",
                    "release_id": "rel-art_001-20240823-001",
                    "asset_id": "asset_en-002",
                    "export_id": "exp-art_001-20240823-png-001",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "released/2024-08-23"
                    ],
                    "run_id": "run_rl-001",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_090",
        "instruction": "As the design review coordinator for the Web UX A team, the time now is 2024-08-23T10:05:00Z; continue the ongoing same-day email-based review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export, inform recipients ['design-review@company.com','ux-team@company.com'] on a single thread labeled 'Design/Needs-Review', ensure identifiers are deterministic and reusable, and complete the cycle by applying quorum.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:05:00Z",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_091",
        "instruction": "As the design systems triage lead and the time is 2024-08-22T13:00:00Z, handle a triage for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export; notify recipients ['design-systems@company.com','frontend-guild@company.com'] on a single thread labeled 'Design/Design-System'. After sending the request, mirror relevant responses as Figma comments, and label the artifact 'ds/triage-open'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-22T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design System Triage: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "labels": [
                        "Design/Design-System"
                    ],
                    "timestamp": "2024-08-22T13:00:00Z",
                    "request_id": "ds-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-systems@company.com",
                        "frontend-guild@company.com"
                    ],
                    "body_html": "Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_ds-002"
                    ],
                    "timestamp": "2024-08-22T13:00:00Z",
                    "request_id": "ds-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ds-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "ds/triage-open"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-22T13:00:00Z",
                    "request_id": "ds-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_systems_triage",
                    "status": "completed",
                    "started_at": "2024-08-22T13:00:00Z",
                    "ended_at": "2024-08-22T13:00:00Z",
                    "timestamp": "2024-08-22T13:00:00Z",
                    "request_id": "ds-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ds-001",
                    "message_id": "msg_ds-002",
                    "asset_id": "asset_ds-002",
                    "tags": [
                        "ds/triage-open"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_092",
        "instruction": "As the accessibility audit lead and the time is 2024-08-14T12:00:00Z, initiate an accessibility audit for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export; notify recipients ['accessibility@company.com','design-review@company.com'] on a single thread labeled 'Design/Accessibility'. After sending the request, mirror relevant responses as Figma comments, and label the artifact 'a11y/needs-audit'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-14T12:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Accessibility Audit: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "labels": [
                        "Design/Accessibility"
                    ],
                    "timestamp": "2024-08-14T12:00:00Z",
                    "request_id": "ax-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "accessibility@company.com",
                        "design-review@company.com"
                    ],
                    "body_html": "Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-14T12:00:00Z",
                    "request_id": "ax-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_ax-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "a11y/needs-audit"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-14T12:00:00Z",
                    "request_id": "ax-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "accessibility_audit_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-14T12:00:00Z",
                    "ended_at": "2024-08-14T12:00:00Z",
                    "timestamp": "2024-08-14T12:00:00Z",
                    "request_id": "ax-004"
                }
            }
        ],
        "outputs": [
                {
                    "thread_id": "thr_ax-001",
                    "message_id": "msg_ax-002",
                    "asset_id": "asset_en-002",
                    "tags": [
                        "a11y/needs-audit"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_093",
        "instruction": "As the review program manager for the Web UX H team with the time at 2024-08-23T14:00:00Z, proceed with the same-day design review for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Notify the recipients ['design-review@company.com','ux-team@company.com'] within the single thread titled 'Design/Needs-Review' by sending out a reminder. Once sent, reflect replies as Figma comments, apply quorum, and ensure identifiers remain deterministic and reusable.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_094",
        "instruction": "As the change request lead for the Web UX team with the time at 2024-08-23T14:30:00Z, convey the requested changes for Figma artifact art_001 ('Homepage Hero Section') using the 'PNG 2x' export. Notify the recipients ['design-review@company.com','ux-team@company.com'] via a single thread labeled 'Design/Changes-Requested' by sending a request. After sending, reflect replies as Figma comments, transition the cycle to CHANGES_REQUESTED, and apply the tag 'needs-changes'.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Changes Requested: Homepage Hero Section",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Changes-Requested"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_cr-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_cr-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-23T14:30:00Z"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-changes"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "change_request",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "cr-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "CHANGES_REQUESTED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_cr-001",
                    "message_id": "msg_cr-002",
                    "tags": [
                        "needs-changes"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_095",
        "instruction": "As the design review coordinator for the Web UX E team, with the current time being 2024-08-24T09:00:00Z, conduct a same-day email-based design review for Figma artifact art_002 ('Pricing Page \u2013 Plans Grid') in accordance with policy. Utilize the 'PNG 2x' export and notify ['design-review@company.com','growth-team@company.com'], ensuring identifiers remain deterministic, and continue using the existing day's thread.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "artifact_id": "art_002",
                    "started_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-002",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_002",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "en-004"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 2 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-004"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_002-20240824-001",
                    "thread_id": "thr_em-004"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-004",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "growth-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-004"
                    ],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "em-005"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_002",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "up-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-24T09:00:00Z",
                    "ended_at": "2024-08-24T09:00:00Z",
                    "timestamp": "2024-08-24T09:00:00Z",
                    "request_id": "rv-004"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_002-20240824-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-004",
                    "thread_id": "thr_em-004",
                    "message_id": "msg_em-005",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_096",
        "instruction": "Being the fix item status updater at this time, 2024-08-28T14:00:00Z, your task is to update fix items from plan_012 for audit_012. Set item_019 and item_020 to APPLIED, maintain item_017 and item_018 as PENDING, and make sure to document the run.",
        "actions": [
            {
                "name": "UpdateFixItemStatus",
                "arguments": {
                    "item_id": "item_019",
                    "status": "APPLIED",
                    "timestamp": "2024-08-28T14:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "UpdateFixItemStatus",
                "arguments": {
                    "item_id": "item_020",
                    "status": "APPLIED",
                    "timestamp": "2024-08-28T14:00:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fix_item_status_update",
                    "status": "completed",
                    "started_at": "2024-08-28T14:00:00Z",
                    "ended_at": "2024-08-28T14:00:00Z",
                    "timestamp": "2024-08-28T14:00:00Z",
                    "request_id": "up-003"
                }
            }
        ],
        "outputs": [
                "\"item_id\":\"item_019\",\"status\":\"APPLIED\"",
                "\"item_id\":\"item_020\",\"status\":\"APPLIED\"",
                "\"run_id\":\"run_up-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_097",
        "instruction": "As the release publisher for the Web UX H team, and with the time being 2024-08-23T11:00:00Z, ensure stakeholder alignment by distributing a release handoff for artifact art_001. This should summarize changes since release_001. Apply export profile 'PNG 2x' for the attachment and dispatch it from emma.creative@company.com to ['stakeholders@company.com','product-managers@company.com']; once sent, tag the artifact 'released/2024-08-23' and log the completion.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "CreateReleaseRecord",
                "arguments": {
                    "artifact_id": "art_001",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_001-20240823-001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "labels": [
                        "released/2024-08-23"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "body_html": "Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:00:00Z",
                    "ended_at": "2024-08-23T11:00:00Z",
                    "timestamp": "2024-08-23T11:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "previous_release_id": "release_001",
                    "release_id": "rel-art_001-20240823-001",
                    "asset_id": "asset_en-002",
                    "export_id": "exp-art_001-20240823-png-001",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "released/2024-08-23"
                    ],
                    "run_id": "run_rl-001",
                    "status": "completed"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_098",
        "instruction": "As the audit report generator for the Web UX H team, with the current time being 2024-08-23T14:30:00Z, aim to create a combined audit report for audit_012 (artifact art_001) which includes both accessibility and design system findings. After crafting the report, export it as a PDF report asset, and document the completion.",
        "actions": [
            {
                "name": "GenerateCombinedAuditReport",
                "arguments": {
                    "audit_id": "audit_012",
                    "artifact_id": "art_001",
                    "output_format": "PDF",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "combined_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-23T14:30:00Z",
                    "ended_at": "2024-08-23T14:30:00Z",
                    "timestamp": "2024-08-23T14:30:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_012\"",
                "\"artifact_id\":\"art_001\"",
                "\"report_asset_id\":\"asset_au-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_099",
        "instruction": "As the design review coordinator for the Web UX team, handle the same-day email-based review for the Figma artifact art_001 ('Homepage Hero Section') with the 'PNG 2x' export format at 2024-08-23T10:05:00Z. Notify the recipients ['design-review@company.com','ux-team@company.com'] on a singular thread titled 'Design/Needs-Review'. Ensure identifiers remain deterministic and reusable, and conclude the process by applying quorum.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:05:00Z",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "SyncRepliesToFigmaComments",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "artifact_id": "art_001"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "design-review@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "RecordReviewApproval",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "approver_email": "ux-team@company.com",
                    "intent": "APPROVE"
                },
            },
            {
                "name": "UpdateReviewStatusByQuorum",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "APPROVED",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_100",
        "instruction": "Holding the role of design review coordinator for the Web UX I team, initiate an email-based design review for Figma artifact art_001 with the 'PNG 2x' export format at 2024-08-23T10:00:00Z. Inform the recipients ['design-review@company.com','ux-team@company.com'] using a single thread for the day, labeled 'Design/Needs-Review', and maintain deterministic and reusable identifiers.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rv-001",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ]
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Design Review Request: 1 frames ready for review",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "labels": [
                        "Design/Needs-Review"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "LinkCycleToThread",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "thread_id": "thr_em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com",
                        "ux-team@company.com"
                    ],
                    "body_html": "Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T10:00:00Z",
                    "ended_at": "2024-08-23T10:00:00Z",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "rev-art_001-20240823-001",
                    "cycle_status": "NEEDS_REVIEW",
                    "asset_id": "asset_en-002",
                    "thread_id": "thr_em-001",
                    "message_id": "msg_em-002",
                    "tags": [
                        "needs-review"
                    ],
                    "status": "completed"
                }
        ]
    }
]
