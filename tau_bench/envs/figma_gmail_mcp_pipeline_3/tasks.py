
tasks = [
    {
        "annotator": 0,
        "user_id": "task_100",
        "instruction": "As the design review coordinator for the Web UX team on 2024-08-24T11:15:00Z, commence an email-based design review of Figma artifact art_003 utilizing export profile 'PNG 2x'. Dispatch from emma.creative@company.com to [jake.design@company.com, chris.engineer@company.com, anna.brand@company.com]. Confirm the email for review includes the exported asset.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_003",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T11:15:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_003",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T11:15:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_003 — 2024-08-24",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "timestamp": "2024-08-24T11:15:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_003.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-24T11:15:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-24T11:15:00Z",
                    "ended_at": "2024-08-24T11:15:00Z",
                    "timestamp": "2024-08-24T11:15:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"export_id\":\"exp-art_003-20240824-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_99",
        "instruction": "As the design review coordinator for the Web UX team on 2024-08-23T09:10:00Z, handle an email-based design review for artifact art_001 with the export profile 'PNG 2x'. Send from emma.creative@company.com to [jake.design@company.com, chris.engineer@company.com, anna.brand@company.com]. Ensure the artifact is marked for review, attach the exported asset in the email, and log the process.",
        "actions": [
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "rl-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "rl-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "rl-003"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_rl-003",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_rl-002"
                    ],
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "rl-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T09:10:00Z",
                    "ended_at": "2024-08-23T09:10:00Z",
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "rl-005"
                }
            }
        ],
        "outputs": [
                "\"export_id\":\"exp-art_001-20240823-png-001\"",
                "\"thread_id\":\"thr_rl-003\"",
                "\"message_id\":\"msg_rl-004\"",
                "\"run_id\":\"run_rl-005\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_98",
        "instruction": "Serving as the accessibility audit lead for the Web UX team, and noting the time as 2024-08-23T12:05:00Z. Carry out a review of A11Y findings related to COLOR_CONTRAST and ALT_TEXT for audit audit_003 on Figma artifact art_003, then generate a PDF accessibility report exclusively based on those findings and log the activity.",
        "actions": [
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "audit_003",
                    "violation_type": "COLOR_CONTRAST"
                },
            },
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "audit_003",
                    "violation_type": "ALT_TEXT"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_003",
                    "audit_id": "audit_003",
                    "format": "pdf",
                    "timestamp": "2024-08-23T12:05:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "a11y_audit",
                    "status": "completed",
                    "started_at": "2024-08-23T12:05:00Z",
                    "ended_at": "2024-08-23T12:05:00Z",
                    "timestamp": "2024-08-23T12:05:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_003\"",
                "\"asset_id\":\"exp-art_003-20240823-pdf-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_97",
        "instruction": "As the release publisher for the Design System team, the date is 2024-08-22T17:00:00Z. Distribute a release handoff for the Figma artifact art_001 by referencing release_001, sent from emma.creative@company.com to [chris.engineer@company.com, anna.brand@company.com, jake.design@company.com]. Use the 'PNG 2x' profile to export the asset and incorporate it into the email.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — release_001 — 2024-08-22",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "chris.engineer@company.com",
                        "anna.brand@company.com",
                        "jake.design@company.com"
                    ],
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hello stakeholders,\nPlease find the release notes for release_001, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/20240822"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-22T17:00:00Z",
                    "ended_at": "2024-08-22T17:00:00Z",
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"export_id\":\"exp-art_001-20240822-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_96",
        "instruction": "Acting as the design review coordinator for the Web UX team at 2024-08-23T10:00:00Z, initiate the review process for Figma artifact art_001 via email using the 'PNG 2x' export profile. Dispatch the email from emma.creative@company.com to the addresses [jake.design@company.com, chris.engineer@company.com, anna.brand@company.com], ensuring the inclusion of the exported asset in the review email.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "en-001"
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
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-002"
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
                "\"export_id\":\"exp-art_001-20240823-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_95",
        "instruction": "As the systems audit lead with the current time set at 2024-08-24T11:20:00Z, assess the findings labeled UNMAPPED and AMBIGUOUS from DS for audit audit_006 concerning artifact art_009. Generate a PDF report and post a Figma comment utilizing the standard audit-report template. Subsequently, adjust the tags by adding ['ds-reviewed'] and removing ['needs-review'], and log the completed activity.",
        "actions": [
            {
                "name": "GetAudit",
                "arguments": {
                    "audit_id": "audit_006"
                },
            },
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "audit_006",
                    "finding_type": "UNMAPPED"
                },
            },
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "audit_006",
                    "finding_type": "AMBIGUOUS"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_009",
                    "audit_id": "audit_006",
                    "format": "pdf",
                    "timestamp": "2024-08-24T11:20:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_009",
                    "author_email": "design-review@company.com",
                    "content": "Audit report sent — art_009 — audit_006 — 2024-08-24 — asset exp-art_009-20240824-pdf-001",
                    "timestamp": "2024-08-24T11:20:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_009",
                    "add_tags": [
                        "ds-reviewed"
                    ],
                    "remove_tags": [
                        "needs-review"
                    ],
                    "timestamp": "2024-08-24T11:20:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "ds_audit_report_and_tags",
                    "status": "completed",
                    "started_at": "2024-08-24T11:20:00Z",
                    "ended_at": "2024-08-24T11:20:00Z",
                    "timestamp": "2024-08-24T11:20:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_006\"",
                "\"asset_id\":\"exp-art_009-20240824-pdf-001\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_94",
        "instruction": "Act as the design review coordinator with the time set at 2024-09-02T12:30:00Z. Keep the discussion centralized\u2014For review cycle cycle_012 (artifact art_012), proceed with the current thread thread_012 by sending a changes-requested follow-up; apply label ['changes-requested']; document the update.",
        "actions": [
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_012"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_012"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_012",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-09-02T12:30:00Z",
                    "timestamp": "2024-09-02T12:30:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_012",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Changes requested for art_012. Continuing in today’s thread.",
                    "timestamp": "2024-09-02T12:30:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_012",
                    "add_labels": [
                        "changes-requested"
                    ],
                    "timestamp": "2024-09-02T12:30:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_changes_requested",
                    "status": "completed",
                    "started_at": "2024-09-02T12:30:00Z",
                    "ended_at": "2024-09-02T12:30:00Z",
                    "timestamp": "2024-09-02T12:30:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_012\"",
                "\"thread_id\":\"thread_012\"",
                "\"message_id\":\"msg_em-001\"",
                "\"run_id\":\"run_rv-001\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_92",
        "instruction": "As the design review coordinator, the current time is 2024-08-20T10:05:00Z. Initiate an email-based design review for artifact art_001 using export profile 'PNG 2x', from emma.creative@company.com to ['chris.engineer@company.com','anna.brand@company.com']; begin today's thread, attach the export, apply the 'needs-review' label, link to the cycle, and do not record the automation run.",
        "actions": [
            {
                "name": "ListReviewCycles",
                "arguments": {
                {}
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-20T10:05:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — art_001 — 2024-08-20",
                    "participant_email": "chris.engineer@company.com"
                },
            },
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — art_001 — 2024-08-20",
                    "participant_email": "anna.brand@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_001 — 2024-08-20",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "timestamp": "2024-08-20T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-20T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "needs-review"
                    ],
                    "timestamp": "2024-08-20T10:05:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "AttachThreadToReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "thread_id": "thr_em-001",
                    "updated_at": "2024-08-20T10:05:00Z",
                    "timestamp": "2024-08-20T10:05:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_001-20240820-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_92",
        "instruction": "As the design review coordinator, the current time is 2024-08-20T10:05:00Z. Initiate an email-based design review for artifact art_001 using export profile 'PNG 2x', from emma.creative@company.com to ['chris.engineer@company.com','anna.brand@company.com']; begin today's thread, attach the export, apply the 'needs-review' label, link to the cycle, and do not record the automation run.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_003",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ListGmailMessages",
                "arguments": {
                    "thread_id": "thread_003",
                    "request_id": "em-002"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_003",
                    "author_email": "design-review@company.com",
                    "content": "Synced from Gmail thread thread_003 on 2024-08-24.",
                    "timestamp": "2024-08-24T17:55:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_003",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Thread thread_003 synced to art_003 on 2024-08-24.",
                    "timestamp": "2024-08-24T17:55:00Z",
                    "request_id": "em-003"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_003",
                    "add_labels": [
                        "synced-to-figma"
                    ],
                    "timestamp": "2024-08-24T17:55:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_003",
                    "request_id": "em-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "sync_email_to_figma",
                    "status": "completed",
                    "started_at": "2024-08-24T17:55:00Z",
                    "ended_at": "2024-08-24T17:55:00Z",
                    "timestamp": "2024-08-24T17:55:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_003\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"labels\":[\"synced-to-figma\"]",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_91",
        "instruction": "As the governance steward at the time 2024-09-02T18:00:00Z, once you have the final sign-off, modify the tags on artifact art_012 by adding ['approved','responsive'] and excluding ['needs-review']; document the precise tag alterations concisely in a tokenized Figma note; log the update.",
        "actions": [
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_012",
                    "add_tags": [
                        "approved",
                        "responsive"
                    ],
                    "remove_tags": [
                        "needs-review"
                    ],
                    "timestamp": "2024-09-02T18:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_012",
                    "author_email": "design-review@company.com",
                    "content": "Governance update — art_012 — add [approved,responsive] — remove [needs-review] — 2024-09-02",
                    "timestamp": "2024-09-02T18:00:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "governance_update",
                    "status": "completed",
                    "started_at": "2024-09-02T18:00:00Z",
                    "ended_at": "2024-09-02T18:00:00Z",
                    "timestamp": "2024-09-02T18:00:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"artifact_id\":\"art_012\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"run_id\":\"run_up-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_90",
        "instruction": "You are responsible for auditing the design-system with the timestamp as 2024-08-24T12:05:00Z. Ambiguity requires assessment\u2014For audit audit_003 targeting artifact art_003, examine design-system findings focused on AMBIGUOUS mappings, prepare a PDF report founded on those findings, submit a Figma comment using the standard audit-report template, and log the activity.",
        "actions": [
            {
                "name": "GetAudit",
                "arguments": {
                    "audit_id": "audit_003"
                },
            },
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "audit_003",
                    "finding_type": "AMBIGUOUS"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_003",
                    "audit_id": "audit_003",
                    "format": "pdf",
                    "timestamp": "2024-08-24T12:05:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "UpdateAuditStatus",
                "arguments": {
                    "audit_id": "audit_003",
                    "status": "COMPLETED",
                    "updated_at": "2024-08-24T12:05:00Z",
                    "timestamp": "2024-08-24T12:05:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_003",
                    "author_email": "design-review@company.com",
                    "content": "Audit report sent — art_003 — audit_003 — 2024-08-24 — asset exp-art_003-20240824-pdf-001",
                    "timestamp": "2024-08-24T12:05:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "ds_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-24T12:05:00Z",
                    "ended_at": "2024-08-24T12:05:00Z",
                    "timestamp": "2024-08-24T12:05:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_003\"",
                "\"asset_id\":\"exp-art_003-20240824-pdf-001\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_89",
        "instruction": "You are leading the accessibility audit with the current time as 2024-08-24T09:40:00Z. Contrast is essential for sign-off\u2014For audit audit_004 concerning artifact art_004, evaluate findings specifically relating to COLOR_CONTRAST, compile a PDF accessibility report exclusively based on those findings, post a Figma comment following the standard audit-report template, and document the activity.",
        "actions": [
            {
                "name": "GetAudit",
                "arguments": {
                    "audit_id": "audit_004"
                },
            },
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "audit_004",
                    "violation_type": "COLOR_CONTRAST"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_004",
                    "audit_id": "audit_004",
                    "format": "pdf",
                    "timestamp": "2024-08-24T09:40:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_004",
                    "author_email": "design-review@company.com",
                    "content": "Audit report sent — art_004 — audit_004 — 2024-08-24 — asset exp-art_004-20240824-pdf-001",
                    "timestamp": "2024-08-24T09:40:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "a11y_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-24T09:40:00Z",
                    "ended_at": "2024-08-24T09:40:00Z",
                    "timestamp": "2024-08-24T09:40:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_004\"",
                "\"asset_id\":\"exp-art_004-20240824-pdf-001\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_88",
        "instruction": "In your role as the design review coordinator on 2024-09-02T09:55:00Z, maintain thread continuity for approvals\u2014continue the current conversation in thread_011 regarding artifact art_011 with a follow-up that includes the most recent 'PNG 2x' export; avoid beginning a new subject; record the activity.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_011",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-09-02T09:55:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_011",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_011",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-09-02T09:55:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_review_followup",
                    "status": "completed",
                    "started_at": "2024-09-02T09:55:00Z",
                    "ended_at": "2024-09-02T09:55:00Z",
                    "timestamp": "2024-09-02T09:55:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_011\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_011-20240902-png-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_87",
        "instruction": "As the audit lead on 2024-08-24T12:20:00Z, handle a cross-team readout\u2014For audit audit_002 concerning artifact art_008, verify that combined A11Y (COLOR_CONTRAST) and DS (UNMAPPED) coverage is accounted for; create a PDF report, use the standard audit-report template to leave a Figma comment, and document the activity.",
        "actions": [
            {
                "name": "GetAudit",
                "arguments": {
                    "audit_id": "audit_002"
                },
            },
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "audit_002",
                    "violation_type": "COLOR_CONTRAST"
                },
            },
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "audit_002",
                    "finding_type": "UNMAPPED"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_008",
                    "audit_id": "audit_002",
                    "format": "pdf",
                    "timestamp": "2024-08-24T12:20:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "design-review@company.com",
                    "content": "Audit report sent — art_008 — audit_002 — 2024-08-24 — asset exp-art_008-20240824-pdf-001",
                    "timestamp": "2024-08-24T12:20:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "combined_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-24T12:20:00Z",
                    "ended_at": "2024-08-24T12:20:00Z",
                    "timestamp": "2024-08-24T12:20:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_002\"",
                "\"asset_id\":\"exp-art_008-20240824-pdf-001\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_86",
        "instruction": "Being the audit lead at 2024-08-23T14:20:00Z, coordinate feedback merging into a single packet for audit audit_003 on artifact art_003. Ensure unified A11Y (COLOR_CONTRAST) and DS (AMBIGUOUS) coverage is included. Generate a PDF report, leave a Figma comment using the standard audit-report template, and log the activity.",
        "actions": [
            {
                "name": "GetAudit",
                "arguments": {
                    "audit_id": "audit_003"
                },
            },
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "audit_003",
                    "violation_type": "COLOR_CONTRAST"
                },
            },
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "audit_003",
                    "finding_type": "AMBIGUOUS"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_003",
                    "audit_id": "audit_003",
                    "format": "pdf",
                    "timestamp": "2024-08-23T14:20:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_003",
                    "author_email": "design-review@company.com",
                    "content": "Audit report sent — art_003 — audit_003 — 2024-08-23 — asset exp-art_003-20240823-pdf-001",
                    "timestamp": "2024-08-23T14:20:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "UpdateAuditStatus",
                "arguments": {
                    "audit_id": "audit_003",
                    "status": "COMPLETED",
                    "updated_at": "2024-08-23T14:20:00Z",
                    "timestamp": "2024-08-23T14:20:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "audit_combined_report",
                    "status": "completed",
                    "started_at": "2024-08-23T14:20:00Z",
                    "ended_at": "2024-08-23T14:20:00Z",
                    "timestamp": "2024-08-23T14:20:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_003\"",
                "\"asset_id\":\"exp-art_003-20240823-pdf-001\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_85",
        "instruction": "As the design review coordinator for the Web UX team at 2024-08-24T10:20:00Z, handle an email-based design review for the promo banner variant using Figma artifact art_007 with export profile 'PNG 2x'. Email from emma.creative@company.com to ['chris.engineer@company.com', 'anna.brand@company.com'], maintain thread consistency for the day, attach the exported asset, apply the 'needs-review' label, and log the activity.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T10:20:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_007 — 2024-08-24",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "timestamp": "2024-08-24T10:20:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_007.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-24T10:20:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "needs-review"
                    ],
                    "timestamp": "2024-08-24T10:20:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_review_email",
                    "status": "completed",
                    "started_at": "2024-08-24T10:20:00Z",
                    "ended_at": "2024-08-24T10:20:00Z",
                    "timestamp": "2024-08-24T10:20:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_007-20240824-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_84",
        "instruction": "Act as the design review coordinator for the Web UX team, and at the time of 2024-08-23T12:10:00Z, initiate an email-based design review for Figma artifact art_006 using export profile 'PNG 2x', from emma.creative@company.com to ['jake.design@company.com']. Keep the day's thread consistent, attach the exported asset, use the 'needs-review' label, and document the activity.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_006",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T12:10:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_006 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com"
                    ],
                    "timestamp": "2024-08-23T12:10:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_006.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-23T12:10:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "needs-review"
                    ],
                    "timestamp": "2024-08-23T12:10:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "design_review_email",
                    "status": "completed",
                    "started_at": "2024-08-23T12:10:00Z",
                    "ended_at": "2024-08-23T12:10:00Z",
                    "timestamp": "2024-08-23T12:10:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_006-20240823-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_83",
        "instruction": "As the design review coordinator, and given the time is 2024-09-02T17:00:00Z, ensure to integrate the latest Gmail thread message, thread_012, into the Figma artifact art_012 as a comment; mark it as 'synced-to-figma' in the thread, check it through thread metadata, and document the synchronization.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_012",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ListGmailMessages",
                "arguments": {
                    "thread_id": "thread_012",
                    "request_id": "em-002"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_012",
                    "author_email": "design-review@company.com",
                    "content": "Synced from Gmail thread thread_012 on 2024-09-02.",
                    "timestamp": "2024-09-02T17:00:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_012",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Thread thread_012 synced to art_012 on 2024-09-02.",
                    "timestamp": "2024-09-02T17:00:00Z",
                    "request_id": "em-003"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_012",
                    "add_labels": [
                        "synced-to-figma"
                    ],
                    "timestamp": "2024-09-02T17:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_012",
                    "request_id": "em-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "sync_email_to_figma",
                    "status": "completed",
                    "started_at": "2024-09-02T17:00:00Z",
                    "ended_at": "2024-09-02T17:00:00Z",
                    "timestamp": "2024-09-02T17:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_012\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"labels\":[\"synced-to-figma\"]",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_82",
        "instruction": "As the design review coordinator, the current time is 2024-08-23T18:45:00Z. For end-of-day context regarding infra, transfer the latest message from Gmail thread thread_005 into the Figma artifact art_004 as a comment; confirm in-thread, tag it 'synced-to-figma', verify using thread metadata, and document the sync.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_005",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ListGmailMessages",
                "arguments": {
                    "thread_id": "thread_005",
                    "request_id": "em-002"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_004",
                    "author_email": "design-review@company.com",
                    "content": "Synced from Gmail thread thread_005 on 2024-08-23.",
                    "timestamp": "2024-08-23T18:45:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_005",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Thread thread_005 synced to art_004 on 2024-08-23.",
                    "timestamp": "2024-08-23T18:45:00Z",
                    "request_id": "em-003"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_005",
                    "add_labels": [
                        "synced-to-figma"
                    ],
                    "timestamp": "2024-08-23T18:45:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_005",
                    "request_id": "em-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "sync_email_to_figma",
                    "status": "completed",
                    "started_at": "2024-08-23T18:45:00Z",
                    "ended_at": "2024-08-23T18:45:00Z",
                    "timestamp": "2024-08-23T18:45:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_005\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"labels\":[\"synced-to-figma\"]",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_81",
        "instruction": "As the review program manager, the current time is 2024-08-24T09:50:00Z. Coordinate with the Saturday cut\u2014For the review cycle cycle_010, document approvals for ['chris.engineer@company.com', 'jake.design@company.com'] at ['2024-08-24T09:55:00Z', '2024-08-24T09:57:00Z'], mark as APPROVED at the latest timestamp if a quorum is met, and log the activity.",
        "actions": [
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_010"
                },
            },
            {
                "name": "UpdateReviewApproval",
                "arguments": {
                    "cycle_id": "cycle_010",
                    "approver_email": "chris.engineer@company.com",
                    "approved_ts_nullable": "2024-08-24T09:55:00Z",
                    "timestamp": "2024-08-24T09:50:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "UpdateReviewApproval",
                "arguments": {
                    "cycle_id": "cycle_010",
                    "approver_email": "jake.design@company.com",
                    "approved_ts_nullable": "2024-08-24T09:57:00Z",
                    "timestamp": "2024-08-24T09:50:00Z",
                    "request_id": "rv-002"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_010",
                    "status": "APPROVED",
                    "updated_at": "2024-08-24T09:57:00Z",
                    "timestamp": "2024-08-24T09:57:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "approvals_append",
                    "status": "completed",
                    "started_at": "2024-08-24T09:50:00Z",
                    "ended_at": "2024-08-24T09:57:00Z",
                    "timestamp": "2024-08-24T09:57:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_010\"",
                "\"cycle_status\":\"approved\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_80",
        "instruction": "Being the audit lead on 2024-08-23T14:00:00Z, leadership needs a unified view\u2014For audit audit_009 on artifact art_006, make sure both A11Y and DS dimensions are included, generate a combined PDF report, add a Figma comment to confirm report delivery using the standard audit-report template, and document the activity.",
        "actions": [
            {
                "name": "GetAudit",
                "arguments": {
                    "audit_id": "audit_009"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_006",
                    "audit_id": "audit_009",
                    "format": "pdf",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "UpdateAuditStatus",
                "arguments": {
                    "audit_id": "audit_009",
                    "status": "COMPLETED",
                    "updated_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_006",
                    "author_email": "design-review@company.com",
                    "content": "Audit report sent — art_006 — audit_009 — 2024-08-23 — asset exp-art_006-20240823-pdf-001",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "combined_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-23T14:00:00Z",
                    "ended_at": "2024-08-23T14:00:00Z",
                    "timestamp": "2024-08-23T14:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_009\"",
                "\"asset_id\":\"exp-art_006-20240823-pdf-001\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_79",
        "instruction": "As the design-system auditor on 2024-09-02T11:20:00Z, produce a DS TOKENS\u2013based PDF audit report for audit audit_012 on artifact art_012, ensure the audit is labeled COMPLETED, and inform ['design-review@company.com'] using the generic email template (subject: 'Update \u2014 2024-09-02') from design-review@company.com with the PDF attached; confirm by checking the thread\u2019s metadata. There's no requirement to log the run.",
        "actions": [
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "audit_012",
                    "finding_type": "TOKENS"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_012",
                    "audit_id": "audit_012",
                    "format": "pdf",
                    "timestamp": "2024-09-02T11:20:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "UpdateAuditStatus",
                "arguments": {
                    "audit_id": "audit_012",
                    "status": "COMPLETED",
                    "updated_at": "2024-09-02T11:20:00Z",
                    "timestamp": "2024-09-02T11:20:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Update — 2024-09-02",
                    "sender_email": "design-review@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-09-02T11:20:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "design-review@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "attachments_asset_ids": [
                        "exp-art_012-20240902-pdf-001"
                    ],
                    "timestamp": "2024-09-02T11:20:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "timestamp": "2024-09-02T11:20:00Z",
                    "request_id": "em-003"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_012\"",
                "\"asset_id\":\"exp-art_012-20240902-pdf-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_78",
        "instruction": "Assume the role of design-system auditor at 2024-08-24T11:40:00Z as a component replacement is being considered\u2014Inspect audit audit_010 on artifact art_010 for design-system issues like ['TOKENS']; develop a PDF report reflecting these findings; complete the audit; dispatch the PDF by email from design-review@company.com to ['design-review@company.com'] using the generic template (subject: 'Update \u2014 2024-08-24'); check the metadata of the sent thread. There's no requirement to log this run.",
        "actions": [
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "audit_010",
                    "finding_type": "TOKENS"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_010",
                    "audit_id": "audit_010",
                    "format": "pdf",
                    "timestamp": "2024-08-24T11:40:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "UpdateAuditStatus",
                "arguments": {
                    "audit_id": "audit_010",
                    "status": "COMPLETED",
                    "updated_at": "2024-08-24T11:40:00Z",
                    "timestamp": "2024-08-24T11:40:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Update — 2024-08-24",
                    "sender_email": "design-review@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-08-24T11:40:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "design-review@company.com",
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "attachments_asset_ids": [
                        "exp-art_010-20240824-pdf-001"
                    ],
                    "timestamp": "2024-08-24T11:40:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "request_id": "em-003"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_010\"",
                "\"asset_id\":\"exp-art_010-20240824-pdf-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_77",
        "instruction": "As the design-system auditor dated 2024-08-24T11:20:00Z, with the library version update on the horizon, inspect audit audit_003 on artifact art_003 for design-system issues such as ['COMPONENT_MISMATCH','SPACING'], compile a PDF report based on these findings, finalize the audit, email the generated PDF from design-review@company.com to ['design-review@company.com'] using the generic template, confirm the email thread was sent, and refrain from logging this automation run.",
        "actions": [
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "audit_003",
                    "finding_type": "COMPONENT_MISMATCH"
                },
            },
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "audit_003",
                    "finding_type": "SPACING"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_003",
                    "audit_id": "audit_003",
                    "format": "pdf",
                    "timestamp": "2024-08-24T11:20:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "UpdateAuditStatus",
                "arguments": {
                    "audit_id": "audit_003",
                    "status": "COMPLETED",
                    "updated_at": "2024-08-24T11:20:00Z",
                    "timestamp": "2024-08-24T11:20:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Update — 2024-08-24",
                    "sender_email": "design-review@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-08-24T11:20:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "design-review@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "attachments_asset_ids": [
                        "exp-art_003-20240824-pdf-001"
                    ],
                    "timestamp": "2024-08-24T11:20:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "timestamp": "2024-08-24T11:20:00Z",
                    "request_id": "em-003"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_003\"",
                "\"asset_id\":\"exp-art_003-20240824-pdf-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_76",
        "instruction": "Serving as the design review coordinator when it's 2024-08-24T17:45:00Z, conclude the settings epic by confirming the integration of the newest note from Gmail thread thread_011 into Figma artifact art_011 as an attributed comment. Confirm within the same Gmail thread using the sync-confirmation template, attach the 'synced-to-figma' label, check the thread metadata to verify delivery, and document the sync.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_011"
                },
            },
            {
                "name": "ListGmailMessages",
                "arguments": {
                    "thread_id": "thread_011"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_011",
                    "author_email": "design-review@company.com",
                    "content": "Synced from Gmail thread thread_011 on 2024-08-24.",
                    "timestamp": "2024-08-24T17:45:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_011",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Thread thread_011 synced to art_011 on 2024-08-24.",
                    "timestamp": "2024-08-24T17:45:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_011",
                    "add_labels": [
                        "synced-to-figma"
                    ],
                    "timestamp": "2024-08-24T17:45:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_011",
                    "timestamp": "2024-08-24T17:45:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "sync_email_to_figma",
                    "status": "completed",
                    "started_at": "2024-08-24T17:45:00Z",
                    "ended_at": "2024-08-24T17:45:00Z",
                    "timestamp": "2024-08-24T17:45:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_011\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"labels\":[\"synced-to-figma\"]",
                "\"run_id\":\"run_up-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_75",
        "instruction": "As the design review coordinator, operating at 2024-08-24T17:30:00Z, note the handoff discussion from Gmail thread thread_007 by adding the latest update as an attributed comment on Figma artifact art_005. Recognize the sync within the thread, attach the 'synced-to-figma' label, and ensure the delivery by checking the thread metadata.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_007",
                    "timestamp": "2024-08-24T17:30:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ListGmailMessages",
                "arguments": {
                    "thread_id": "thread_007",
                    "timestamp": "2024-08-24T17:30:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_005",
                    "author_email": "design-review@company.com",
                    "content": "Synced from Gmail thread thread_007 on 2024-08-24.",
                    "timestamp": "2024-08-24T17:30:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_007",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Thread thread_007 synced to art_005 on 2024-08-24.",
                    "timestamp": "2024-08-24T17:30:00Z",
                    "request_id": "em-003"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_007",
                    "add_labels": [
                        "synced-to-figma"
                    ],
                    "timestamp": "2024-08-24T17:30:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_007",
                    "timestamp": "2024-08-24T17:30:00Z",
                    "request_id": "em-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "sync_email_to_figma",
                    "status": "completed",
                    "started_at": "2024-08-24T17:30:00Z",
                    "ended_at": "2024-08-24T17:30:00Z",
                    "timestamp": "2024-08-24T17:30:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_007\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"labels\":[\"synced-to-figma\"]",
                "\"run_id\":\"run_up-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_74",
        "instruction": "You are heading the review program and the current date and time is 2024-08-24T10:40:00Z. In preparation for the weekend freeze, for review cycle cycle_008, document the approvals for ['jake.design@company.com','emma.creative@company.com'] at ['2024-08-24T10:45:00Z','2024-08-24T10:55:00Z']. If a quorum is confirmed at the time of the latest approval, update the cycle status to APPROVED, replace all 'needs-review' tags on the cycle's artifacts with 'approved/20240824'. There is no necessity to log the automation run.",
        "actions": [
            {
                "name": "UpdateReviewApproval",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "approver_email": "jake.design@company.com",
                    "approved_ts_nullable": "2024-08-24T10:45:00Z",
                    "timestamp": "2024-08-24T10:40:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "UpdateReviewApproval",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "approver_email": "emma.creative@company.com",
                    "approved_ts_nullable": "2024-08-24T10:55:00Z",
                    "timestamp": "2024-08-24T10:40:00Z",
                    "request_id": "rv-002"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "status": "APPROVED",
                    "updated_at": "2024-08-24T10:55:00Z",
                    "timestamp": "2024-08-24T10:55:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "approved/20240824"
                    ],
                    "remove_tags": [
                        "needs-review"
                    ],
                    "timestamp": "2024-08-24T10:55:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_008\"",
                "\"cycle_status\":\"approved\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_73",
        "instruction": "You are managing the design review and the date and time is 2024-09-02T14:50:00Z. A sidebar fix has just been implemented\u2014initiate a re-review request for Figma artifact art_002 directed to ['jake.design@company.com','chris.engineer@company.com'] using the standard re-review notice. Continue with the current same-day thread if available (check by participant 'jake.design@company.com'; if not, start a new one), tag it with 'design-review', and log the update.",
        "actions": [
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Re-review Needed — art_002 — 2024-09-02",
                    "participant_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Re-review Needed — art_002 — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com"
                    ],
                    "timestamp": "2024-09-02T14:50:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com"
                    ],
                    "body_html": "Fixes have been applied on art_002; please re-review the latest assets.",
                    "timestamp": "2024-09-02T14:50:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thr_em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-09-02T14:50:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "rereview_kickoff",
                    "status": "completed",
                    "started_at": "2024-09-02T14:50:00Z",
                    "ended_at": "2024-09-02T14:50:00Z",
                    "timestamp": "2024-09-02T14:50:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"artifact_id\":\"art_002\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"labels\":[\"design-review\"]",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_72",
        "instruction": "Acting as the design review coordinator and with the current time as 2024-09-02T14:10:00Z, request a re-review for Figma artifact art_001 for ['emma.creative@company.com'] after a quick rollback test succeeds using the standard re-review notice; uphold the same-day review subject (continuing with the existing thread 'Data Table Component Review'), include the label 'design-review', and document the update.",
        "actions": [
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Data Table Component Review"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_009",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "emma.creative@company.com"
                    ],
                    "body_html": "Fixes have been applied on art_001; please re-review the latest assets.",
                    "timestamp": "2024-09-02T14:10:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_009",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-09-02T14:10:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "rereview_kickoff",
                    "status": "completed",
                    "started_at": "2024-09-02T14:10:00Z",
                    "ended_at": "2024-09-02T14:10:00Z",
                    "timestamp": "2024-09-02T14:10:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"artifact_id\":\"art_001\"",
                "\"thread_id\":\"thread_009\"",
                "\"message_id\":\"msg_em-001\"",
                "\"labels\":[\"design-review\"]",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_71",
        "instruction": "As the governance steward, currently dated 2024-08-23T18:50:00Z, approve the recent tasks\u2014modify tags on artifact art_003 to include ['approved'] and exclude ['needs-review']; dispatch a confirmation note today from design-review@company.com to ['design-review@company.com'] using the generic template (extend the ongoing day's thread if it's available), attach the label 'governance', and log the update.",
        "actions": [
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_003",
                    "add_tags": [
                        "approved"
                    ],
                    "remove_tags": [
                        "needs-review"
                    ],
                    "timestamp": "2024-08-23T18:50:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Update — 2024-08-23",
                    "participant_email": "design-review@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Update — 2024-08-23",
                    "sender_email": "design-review@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-08-23T18:50:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-002",
                    "sender_email": "design-review@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "timestamp": "2024-08-23T18:50:00Z",
                    "request_id": "em-003"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-002",
                    "add_labels": [
                        "governance"
                    ],
                    "timestamp": "2024-08-23T18:50:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "governance_update",
                    "status": "completed",
                    "started_at": "2024-08-23T18:50:00Z",
                    "ended_at": "2024-08-23T18:50:00Z",
                    "timestamp": "2024-08-23T18:50:00Z",
                    "request_id": "up-003"
                }
            }
        ],
        "outputs": [
                "\"artifact_id\":\"art_003\"",
                "\"thread_id\":\"thr_em-002\"",
                "\"message_id\":\"msg_em-003\"",
                "\"labels\":[\"governance\"]",
                "\"run_id\":\"run_up-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_70",
        "instruction": "Acting as the design review coordinator for the Web UX team at 2024-09-02T13:05:00Z, commence the email-based design review for the Figma artifact art_012 using the 'PNG 2x' export profile. Dispatch this from emma.creative@company.com to ['chris.engineer@company.com','jake.design@company.com']. Maintain the daily thread consistently, make sure the exported asset is attached, apply the 'design-review' label, and verify the thread. Recording the automation run is unnecessary.",
        "actions": [
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_012",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-09-02T13:05:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_012",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-09-02T13:05:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_012 — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "chris.engineer@company.com",
                        "jake.design@company.com"
                    ],
                    "timestamp": "2024-09-02T13:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "chris.engineer@company.com",
                        "jake.design@company.com"
                    ],
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_012.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-09-02T13:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-09-02T13:05:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "request_id": "em-003"
                }
            }
        ],
        "outputs": [
                "\"artifact_id\":\"art_012\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_012-20240902-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"labels\":[\"design-review\"]",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_69",
        "instruction": "As the design review coordinator at 2024-09-02T11:05:00Z, initiate the email-based design review for the Figma artifact art_010 using the 'PNG 2x' export profile. Send this from emma.creative@company.com to ['design-review@company.com']. If there is a thread for the same day, continue it, ensure to include the exported asset in the review email, apply the 'design-review' label, and document the activity.",
        "actions": [
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — art_010 — 2024-09-02",
                    "participant_email": "design-review@company.com"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_010",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-09-02T11:05:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_010 — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-09-02T11:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_010.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-09-02T11:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-09-02T11:05:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-09-02T11:05:00Z",
                    "ended_at": "2024-09-02T11:05:00Z",
                    "timestamp": "2024-09-02T11:05:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"artifact_id\":\"art_010\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_010-20240902-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"labels\":[\"design-review\"]",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_68",
        "instruction": "In your role as the accessibility audit lead, please note that the time is 2024-09-02T09:20:00Z. The handoff is being delayed by contrast checks\u2014For audit audit_002 on artifact art_008, examine the findings for ['COLOR_CONTRAST'], generate a PDF accessibility report exclusively from these findings, signify completion of the audit, and dispatch the PDF via email from design-review@company.com to ['design-review@company.com'] using the standard template. Confirm the presence of the sent thread. There is no need to document the automation run.",
        "actions": [
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "audit_002",
                    "violation_type": "COLOR_CONTRAST"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_008",
                    "audit_id": "audit_002",
                    "format": "pdf",
                    "timestamp": "2024-09-02T09:20:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "UpdateAuditStatus",
                "arguments": {
                    "audit_id": "audit_002",
                    "status": "COMPLETED",
                    "updated_at": "2024-09-02T09:20:00Z",
                    "timestamp": "2024-09-02T09:20:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Update — 2024-09-02",
                    "sender_email": "design-review@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-09-02T09:20:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "design-review@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "attachments_asset_ids": [
                        "exp-art_008-20240902-pdf-001"
                    ],
                    "timestamp": "2024-09-02T09:20:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "request_id": "em-003"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_002\"",
                "\"asset_id\":\"exp-art_008-20240902-pdf-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_67",
        "instruction": "As the design review coordinator, note that the current time is 2024-09-02T16:40:00Z. Once the targeted patch has been delivered, prompt a re-review for Figma artifact art_005 directed at ['emma.creative@company.com','jake.design@company.com'] with the standard re-review notification. Continue the conversation in the ongoing same-day email thread for the artifact ('User Profile Screen Implementation') without starting a new subject. Apply the 'design-review' label and log the update.",
        "actions": [
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "User Profile Screen Implementation"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_007",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "body_html": "Fixes have been applied on art_005; please re-review the latest assets.",
                    "timestamp": "2024-09-02T16:40:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_007",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-09-02T16:40:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "rereview_kickoff",
                    "status": "completed",
                    "started_at": "2024-09-02T16:40:00Z",
                    "ended_at": "2024-09-02T16:40:00Z",
                    "timestamp": "2024-09-02T16:40:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"artifact_id\":\"art_005\"",
                "\"thread_id\":\"thread_007\"",
                "\"message_id\":\"msg_em-001\"",
                "\"labels\":[\"design-review\"]",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_66",
        "instruction": "Handle the design review process for the Web UX team with the current time being 2024-09-02T17:10:00Z. Grid updates have just been implemented\u2014initiate an email-based design review for the Figma artifact art_004 using export profile 'PNG 2x'; ensure there is a single email thread per artifact for the day, and continue within the existing thread if already initiated; guarantee the review email includes the exported asset, dispatched from emma.creative@company.com to ['design-review@company.com']; as part of the initiation, apply the tag 'needs-review' to the artifact; apply the Gmail label 'design-review'. Recording the automation run is not necessary.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_004",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-09-02T17:10:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_004",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-09-02T17:10:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — art_004 — 2024-09-02",
                    "participant_email": "design-review@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_004 — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-09-02T17:10:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_004.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-09-02T17:10:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-09-02T17:10:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_004-20240902-png-001\"",
                "\"labels\":[\"design-review\"]",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_65",
        "instruction": "Coordinate the design review process for the Web UX team at the time 2024-09-02T13:40:00Z. Several teams are modifying shared primitives\u2014initiate a unified email-based design review and attach 'PNG 2x' exports from ['art_009','art_010'] in a single email to ['stakeholders@company.com','ux-team@company.com']; utilize the email.review_request_consolidated.v1 template with subject 'Review Request \u2014 Consolidated \u2014 2024-09-02'; ensure to maintain one consolidated email thread for the day, applying the label 'design-review'. Do not log the automation run.",
        "actions": [
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — Consolidated — 2024-09-02",
                    "participant_email": "stakeholders@company.com"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_009",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-09-02T13:40:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_010",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-09-02T13:40:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — Consolidated — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "ux-team@company.com"
                    ],
                    "timestamp": "2024-09-02T13:40:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x exports.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001",
                        "asset_en-002"
                    ],
                    "timestamp": "2024-09-02T13:40:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-09-02T13:40:00Z",
                    "request_id": "up-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"asset_ids\":[\"asset_en-001\",\"asset_en-002\"]",
                "\"export_ids\":[\"exp-art_009-20240902-png-001\",\"exp-art_010-20240902-png-001\"]",
                "\"labels\":[\"design-review\"]",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_64",
        "instruction": "As the design review coordinator for the Web UX team, and with the current time being 2024-09-02T10:40:00Z, facilitate the sharing of the morning build with leadership\u2014initiate an email-based design review for Figma artifact art_002 employing export profile 'PNG 2x'; maintain a singular email thread per artifact for the day and continue within an existing thread if one has been initiated; ensure that the review email comprises the exported asset sent to ['stakeholders@company.com','product-managers@company.com']; assign the label 'design-review'. It's unnecessary to record the automation run.",
        "actions": [
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — art_002 — 2024-09-02",
                    "participant_email": "stakeholders@company.com"
                },
            },
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_002-20240902-001",
                    "artifact_id": "art_002",
                    "started_at": "2024-09-02T10:40:00Z",
                    "timestamp": "2024-09-02T10:40:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_002",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-09-02T10:40:00Z",
                    "request_id": "en-001"
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
                    "timestamp": "2024-09-02T10:40:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_002 — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com"
                    ],
                    "timestamp": "2024-09-02T10:40:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_002.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-09-02T10:40:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-09-02T10:40:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"rev-art_002-20240902-001\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_002-20240902-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"labels\":[\"design-review\"]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_63",
        "instruction": "You are the governance steward and the current time is 2024-08-23T09:05:00Z. Coordinate the alignment of metadata prior to the design review\u2014modify tags on artifact art_001 by incorporating ['design-system','responsive'] and eliminating ['needs-review']; dispatch a same-day message from emma.creative@company.com to ['design-review@company.com'] utilizing the generic template (continue participating in an existing same-day thread if it exists), attach the label 'governance', and document the change.",
        "actions": [
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "design-system",
                        "responsive"
                    ],
                    "remove_tags": [
                        "needs-review"
                    ],
                    "timestamp": "2024-08-23T09:05:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Update — 2024-08-23",
                    "participant_email": "design-review@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Update — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-08-23T09:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "timestamp": "2024-08-23T09:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "governance"
                    ],
                    "timestamp": "2024-08-23T09:05:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "governance_update",
                    "status": "completed",
                    "started_at": "2024-08-23T09:05:00Z",
                    "ended_at": "2024-08-23T09:05:00Z",
                    "timestamp": "2024-08-23T09:05:00Z",
                    "request_id": "up-003"
                }
            }
        ],
        "outputs": [
                "\"artifact_id\":\"art_001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"labels\":[\"governance\"]",
                "\"run_id\":\"run_up-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_62",
        "instruction": "As the review program manager, and the time being 2024-09-02T10:00:00Z, once a clean smoke test is done, document approvals for review cycle cycle_003 from ['anna.brand@company.com'] at ['2024-09-02T10:05:00Z']; mark the cycle as approved only if quorum (two same-day approvals) is achieved, otherwise keep the status as is. Send a confirmation email to ['design-review@company.com'] using the generic template (if an existing same-day thread is available, continue it), associate the thread with cycle_003, and omit recording the automation run.",
        "actions": [
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_003"
                },
            },
            {
                "name": "UpdateReviewApproval",
                "arguments": {
                    "cycle_id": "cycle_003",
                    "approver_email": "anna.brand@company.com",
                    "approved_ts_nullable": "2024-09-02T10:05:00Z",
                    "timestamp": "2024-09-02T10:00:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Update — 2024-09-02",
                    "participant_email": "design-review@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Update — 2024-09-02",
                    "sender_email": "design-review@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-09-02T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "design-review@company.com",
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "timestamp": "2024-09-02T10:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "AttachThreadToReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_003",
                    "thread_id": "thr_em-001",
                    "updated_at": "2024-09-02T10:00:00Z",
                    "timestamp": "2024-09-02T10:00:00Z",
                    "request_id": "rv-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_003\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_61",
        "instruction": "As the design review coordinator, with the current time of 2024-08-24T17:15:00Z, ensure to document the late-day update. Integrate Gmail thread thread_010 into Figma artifact art_002 by adding an attributed comment (no need for a per-message id), confirm within the thread using the sync-confirmation template, apply the 'synced-to-figma' label to the thread, and log the sync activity.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "design-review@company.com",
                    "content": "Synced from Gmail thread thread_010 on 2024-08-24.",
                    "timestamp": "2024-08-24T17:15:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Thread thread_010 synced to art_002 on 2024-08-24.",
                    "timestamp": "2024-08-24T17:15:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_010",
                    "add_labels": [
                        "synced-to-figma"
                    ],
                    "timestamp": "2024-08-24T17:15:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "sync_email_to_figma",
                    "status": "completed",
                    "started_at": "2024-08-24T17:15:00Z",
                    "ended_at": "2024-08-24T17:15:00Z",
                    "timestamp": "2024-08-24T17:15:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_010\"",
                "\"comment_id\":\"comment_en-001\"",
                "\"message_id\":\"msg_em-001\"",
                "\"labels\":[\"synced-to-figma\"]",
                "\"run_id\":\"run_up-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_60",
        "instruction": "You manage the release publication with the time at 2024-08-20T13:30:00Z. Notify partner teams prior to staging\u2014circulate a release handoff for artifact art_005, making reference to release_002, and attach an exported asset 'PNG 2x' in the email from jake.design@company.com to ['emma.creative@company.com', 'chris.engineer@company.com'].",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_002"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_005",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-20T13:30:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — release_002 — 2024-08-20",
                    "sender_email": "jake.design@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "chris.engineer@company.com"
                    ],
                    "timestamp": "2024-08-20T13:30:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "jake.design@company.com",
                    "body_html": "Hello stakeholders,\nPlease find the release notes for release_002, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-20T13:30:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_005",
                    "add_tags": [
                        "released/20240820"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-20T13:30:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-20T13:30:00Z",
                    "ended_at": "2024-08-20T13:30:00Z",
                    "timestamp": "2024-08-20T13:30:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_005-20240820-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_59",
        "instruction": "You oversee the design review process for the Web UX team, with the current time being 2024-09-02T12:15:00Z. A device matrix check is in line\u2014dispatch an email-oriented design review for Figma artifact art_010 using the export profile 'PNG 2x', from emma.creative@company.com to ['sophie.marketing@company.com']; ensure the day's email thread remains coherent and the exported asset is attached.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_010-20240902-001",
                    "artifact_id": "art_010",
                    "started_at": "2024-09-02T12:15:00Z",
                    "timestamp": "2024-09-02T12:15:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_010",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-09-02T12:15:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_010",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-09-02T12:15:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — art_010 — 2024-09-02",
                    "participant_email": "sophie.marketing@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_010 — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "sophie.marketing@company.com"
                    ],
                    "timestamp": "2024-09-02T12:15:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_010.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-09-02T12:15:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-09-02T12:15:00Z",
                    "ended_at": "2024-09-02T12:15:00Z",
                    "timestamp": "2024-09-02T12:15:00Z",
                    "request_id": "rv-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"rev-art_010-20240902-001\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_010-20240902-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rv-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_58",
        "instruction": "As the governance steward at 2024-08-24T10:05:00Z, note the expanded component coverage\u2014modify tags on artifact art_003 by adding ['components', 'tokens'] while removing none; document the update and make an entry in the review thread for the day, dispatching the note from emma.creative@company.com to ['design-review@company.com'] using the standard update email template (subject: 'Update \u2014 {date}').",
        "actions": [
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_003",
                    "add_tags": [
                        "components",
                        "tokens"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T10:05:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Update — 2024-08-24",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-08-24T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "timestamp": "2024-08-24T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "governance_update",
                    "status": "completed",
                    "started_at": "2024-08-24T10:05:00Z",
                    "ended_at": "2024-08-24T10:05:00Z",
                    "timestamp": "2024-08-24T10:05:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"artifact_id\":\"art_003\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_up-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_57",
        "instruction": "Being the release publisher at the time 2024-08-19T17:10:00Z, Marketing anticipates a preview for the newsletter tomorrow\u2014provide a release handoff for artifact art_008 with reference to release_004. Ensure the inclusion of an exported asset 'PNG 2x' in the email sent from chris.engineer@company.com to ['anna.brand@company.com'].",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_004"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_008",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-19T17:10:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — release_004 — 2024-08-19",
                    "sender_email": "chris.engineer@company.com",
                    "recipients": [
                        "anna.brand@company.com"
                    ],
                    "timestamp": "2024-08-19T17:10:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "chris.engineer@company.com",
                    "body_html": "Hello stakeholders,\nPlease find the release notes for release_004, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-19T17:10:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_008",
                    "add_tags": [
                        "released/20240819"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-19T17:10:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-19T17:10:00Z",
                    "ended_at": "2024-08-19T17:10:00Z",
                    "timestamp": "2024-08-19T17:10:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_008-20240819-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_56",
        "instruction": "As the review program manager, the current time is 2024-08-23T15:20:00Z. A final sign-off is required\u2014For review cycle cycle_007, document approvals for ['emma.creative@company.com'] at ['2024-08-23T15:25:00Z'], and indicate if quorum has been reached if necessary.",
        "actions": [
            {
                "name": "UpdateReviewApproval",
                "arguments": {
                    "cycle_id": "cycle_007",
                    "approver_email": "emma.creative@company.com",
                    "approved_ts_nullable": "2024-08-23T15:25:00Z",
                    "timestamp": "2024-08-23T15:20:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "approvals_append",
                    "status": "completed",
                    "started_at": "2024-08-23T15:20:00Z",
                    "ended_at": "2024-08-23T15:20:00Z",
                    "timestamp": "2024-08-23T15:20:00Z",
                    "request_id": "rv-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_007\"",
                "\"approver\":\"emma.creative@company.com\"",
                "\"run_id\":\"run_rv-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_55",
        "instruction": "You have the role of design review coordinator and the current time is 2024-09-02T12:20:00Z. A blocker ping has just arrived\u2014For review cycle cycle_012, send a changes-requested update to ['chris.engineer@company.com', 'jake.design@company.com'] with labels ['Design','design-review']; no automation run record is required.",
        "actions": [
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_012"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_012",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-09-02T12:20:00Z",
                    "timestamp": "2024-09-02T12:20:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_012",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "chris.engineer@company.com",
                        "jake.design@company.com"
                    ],
                    "body_html": "Changes requested for art_012. Continuing in today’s thread.",
                    "timestamp": "2024-09-02T12:20:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_012",
                    "add_labels": [
                        "Design",
                        "design-review"
                    ],
                    "timestamp": "2024-09-02T12:20:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "AttachThreadToReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_012",
                    "thread_id": "thread_012",
                    "updated_at": "2024-09-02T12:20:00Z",
                    "timestamp": "2024-09-02T12:20:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_012\"",
                "\"thread_id\":\"thread_012\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_54",
        "instruction": "Serve as the design review coordinator with the time set at 2024-08-23T18:30:00Z. Document end-of-day decisions\u2014align the latest message from Gmail thread thread_009 with Figma artifact art_009 as a comment. Incorporate the source message reference if available (otherwise, continue without it); subsequently, respond in the same thread utilizing the sync-confirmation template to confirm the synchronization. Apply the email label 'synced-to-figma' and record the synchronization.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_009"
                },
            },
            {
                "name": "ListGmailMessages",
                "arguments": {
                    "thread_id": "thread_009"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_009",
                    "author_email": "design-review@company.com",
                    "content": "Synced from Gmail thread thread_009 on 2024-08-23.",
                    "source_message_id_nullable": "msg_010",
                    "timestamp": "2024-08-23T18:30:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_009",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Thread thread_009 synced to art_009 on 2024-08-23.",
                    "timestamp": "2024-08-23T18:30:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_009",
                    "add_labels": [
                        "synced-to-figma"
                    ],
                    "timestamp": "2024-08-23T18:30:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "sync_email_to_figma",
                    "status": "completed",
                    "started_at": "2024-08-23T18:30:00Z",
                    "ended_at": "2024-08-23T18:30:00Z",
                    "timestamp": "2024-08-23T18:30:00Z",
                    "request_id": "up-003"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_009\"",
                "\"comment_id\":\"comment_up-001\"",
                "\"message_id\":\"msg_em-001\"",
                "\"labels\":[\"synced-to-figma\"]",
                "\"run_id\":\"run_up-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_53",
        "instruction": "Act as the design review coordinator for the Web UX team with the current time being 2024-08-24T09:40:00Z. The UX guild requires an early evaluation of tokens\u2014coordinate an email-based design review of the Figma artifact art_003, employing the export profile 'PNG 2x'. Send from emma.creative@company.com to ['ux-team@company.com']. Ensure the review email includes the exported asset and appends the label 'design-review'. Do not document the execution.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_003-20240824-001",
                    "artifact_id": "art_003",
                    "started_at": "2024-08-24T09:40:00Z",
                    "timestamp": "2024-08-24T09:40:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_003",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T09:40:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_003",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T09:40:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — art_003 — 2024-08-24",
                    "participant_email": "ux-team@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_003 — 2024-08-24",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "ux-team@company.com"
                    ],
                    "timestamp": "2024-08-24T09:40:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_003.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-24T09:40:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-08-24T09:40:00Z",
                    "request_id": "em-003"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"rev-art_003-20240824-001\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_003-20240824-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"labels\":[\"design-review\"]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_52",
        "instruction": "Act as the lead for the accessibility audit and note that the time is 2024-08-24T11:00:00Z. Given the QA's observations of sizing quirks on dashboards, for audit audit_002 regarding artifact art_008, evaluate findings in relation to ['COLOR_CONTRAST','FOCUS_ORDER']. Create a PDF accessibility report precisely based on those findings. Mark the audit as completed, send the report via email to ['design-review@company.com'] using the generic template, apply the email label 'a11y-report', and refrain from recording the execution.",
        "actions": [
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "audit_002",
                    "violation_type": "COLOR_CONTRAST"
                },
            },
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "audit_002",
                    "violation_type": "FOCUS_ORDER"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_008",
                    "audit_id": "audit_002",
                    "format": "pdf",
                    "timestamp": "2024-08-24T11:00:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "UpdateAuditStatus",
                "arguments": {
                    "audit_id": "audit_002",
                    "status": "COMPLETED",
                    "updated_at": "2024-08-24T11:00:00Z",
                    "timestamp": "2024-08-24T11:00:00Z",
                    "request_id": "au-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Update — 2024-08-24",
                    "sender_email": "design-review@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-08-24T11:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "design-review@company.com",
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "attachments_asset_ids": [
                        "exp-art_008-20240824-pdf-001"
                    ],
                    "timestamp": "2024-08-24T11:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "a11y-report"
                    ],
                    "timestamp": "2024-08-24T11:00:00Z",
                    "request_id": "em-003"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_002\"",
                "\"report_asset_id\":\"exp-art_008-20240824-pdf-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"labels\":[\"a11y-report\"]",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_51",
        "instruction": "Serve as the design review coordinator for the Web UX team. The current time is 2024-09-02T09:05:00Z. With the Monday stand-up meeting scheduled in an hour, initiate a design review via email for Figma artifact art_001 using the export profile 'PNG 2x'. Maintain one email thread per artifact for the entire day and continue with an existing thread if it has already been initiated. Ensure that the review email includes the exported asset sent to ['anna.brand@company.com'].",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240902-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-09-02T09:05:00Z",
                    "timestamp": "2024-09-02T09:05:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-09-02T09:05:00Z",
                    "request_id": "en-001"
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
                    "timestamp": "2024-09-02T09:05:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — art_001 — 2024-09-02",
                    "participant_email": "anna.brand@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_001 — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "anna.brand@company.com"
                    ],
                    "timestamp": "2024-09-02T09:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-09-02T09:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-09-02T09:05:00Z",
                    "ended_at": "2024-09-02T09:05:00Z",
                    "timestamp": "2024-09-02T09:05:00Z",
                    "request_id": "rv-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"rev-art_001-20240902-001\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_001-20240902-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rv-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_50",
        "instruction": "Acting as the design review coordinator for the Web UX team, and noting the time as 2024-08-23T11:45:00Z, the review alias is prepared\u2014commence an email-based design review of Figma artifact art_001 using the 'PNG 2x' export profile, to be sent from emma.creative@company.com to ['design-review@company.com']. Ensure that the review email incorporates the exported asset and apply the 'design-review' label. Logging the run is unnecessary.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240823-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-23T11:45:00Z",
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "en-001"
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
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — art_001 — 2024-08-23",
                    "participant_email": "design-review@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "em-003"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"rev-art_001-20240823-001\"",
                "\"cycle_status\":\"IN_FLIGHT\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_001-20240823-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_49",
        "instruction": "As the release publisher, the time is set to 2024-09-02T09:30:00Z. The PMs have requested a Monday morning roll-up\u2014distribute a release handoff for artifact art_002 referring to release_012. Attach the 'PNG 2x' export and send an email from jake.design@company.com to ['product-managers@company.com', 'stakeholders@company.com']. Summarize the differences from the preceding release tag.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_012"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_002",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-09-02T09:30:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_002-20240902-001 — 2024-09-02",
                    "sender_email": "jake.design@company.com",
                    "recipients": [
                        "product-managers@company.com",
                        "stakeholders@company.com"
                    ],
                    "timestamp": "2024-09-02T09:30:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "jake.design@company.com",
                    "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_002-20240902-001, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-09-02T09:30:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_002",
                    "add_tags": [
                        "released/20240902"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-09-02T09:30:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-09-02T09:30:00Z",
                    "ended_at": "2024-09-02T09:30:00Z",
                    "timestamp": "2024-09-02T09:30:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_002-20240902-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_48",
        "instruction": "As the accessibility audit lead with the time is 2024-08-24T10:30:00Z, focus on evaluating contrast and flow\u2014For audit audit_001 on artifact art_001, examine findings regarding ['COLOR_CONTRAST', 'FOCUS_ORDER'], compile a PDF accessibility report strictly based on those findings, and log the activity.",
        "actions": [
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "audit_001",
                    "violation_type": "COLOR_CONTRAST"
                },
            },
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "audit_001",
                    "violation_type": "FOCUS_ORDER"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_001",
                    "audit_id": "audit_001",
                    "format": "pdf",
                    "timestamp": "2024-08-24T10:30:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "UpdateAuditStatus",
                "arguments": {
                    "audit_id": "audit_001",
                    "status": "COMPLETED",
                    "updated_at": "2024-08-24T10:30:00Z",
                    "timestamp": "2024-08-24T10:30:00Z",
                    "request_id": "au-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "a11y_audit_report",
                    "status": "completed",
                    "started_at": "2024-08-24T10:30:00Z",
                    "ended_at": "2024-08-24T10:30:00Z",
                    "timestamp": "2024-08-24T10:30:00Z",
                    "request_id": "au-003"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_001\"",
                "\"asset_id\":\"exp-art_001-20240824-pdf-001\"",
                "\"run_id\":\"run_au-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_47",
        "instruction": "As the design review coordinator and the time is 2024-09-02T16:20:00Z, with the final polish now completed, initiate a re-review request for Figma artifact art_012 directed to ['jake.design@company.com'] using the standard re-review notice; ensure same-day consistency (continue an existing thread if present, or start a new one otherwise), and document the activity.",
        "actions": [
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Re-review Needed — art_012 — 2024-09-02",
                    "participant_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Re-review Needed — art_012 — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com"
                    ],
                    "timestamp": "2024-09-02T16:20:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Fixes have been applied on art_012; please re-review the latest assets.",
                    "timestamp": "2024-09-02T16:20:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "rereview_kickoff",
                    "status": "completed",
                    "started_at": "2024-09-02T16:20:00Z",
                    "ended_at": "2024-09-02T16:20:00Z",
                    "timestamp": "2024-09-02T16:20:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_46",
        "instruction": "As the design review coordinator, at 2024-08-21T16:30:00Z, respond to a follow-up SLA alert triggered due to a breach in review cycle cycle_004 for artifact art_008 by sending a changes-requested escalation notice to ['design-automation@company.com','product-managers@company.com'] using the standard changes-requested template. Ensure same-day continuity by continuing the current thread for product-managers@company.com if it exists; if not, initiate one. Apply the label ['Design/Escalation'], attach the thread to the review cycle. Recording the automation run is not required.",
        "actions": [
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_004"
                },
            },
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Changes Requested — 2024-08-21",
                    "participant_email": "product-managers@company.com"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-21T16:30:00Z",
                    "timestamp": "2024-08-21T16:30:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Changes Requested — 2024-08-21",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-automation@company.com",
                        "product-managers@company.com"
                    ],
                    "timestamp": "2024-08-21T16:30:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Changes requested for art_008. Continuing in today’s thread.",
                    "timestamp": "2024-08-21T16:30:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "Design/Escalation"
                    ],
                    "timestamp": "2024-08-21T16:30:00Z",
                    "request_id": "em-003"
                },
            },
            {
                "name": "AttachThreadToReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "thread_id": "thr_em-001",
                    "updated_at": "2024-08-21T16:30:00Z",
                    "timestamp": "2024-08-21T16:30:00Z",
                    "request_id": "rv-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_004\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"labels\":[\"Design/Escalation\"]",
                "\"status\":\"changes_requested\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_45",
        "instruction": "Handle the role of design review coordinator for the Web UX team at 2024-08-24T11:10:00Z. To optimize feedback on shared dependencies, coordinate a unified email-based design review and attach 'PNG 2x' exports from ['art_004', 'art_005'] in a single message to ['design-review@company.com']; ensure one thread is maintained for the day's consolidated review. Logging the run is not necessary.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_004",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T11:10:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_005",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T11:10:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_004",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T11:10:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_005",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T11:10:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — Consolidated — 2024-08-24",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-08-24T11:10:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x exports.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001",
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-24T11:10:00Z",
                    "request_id": "em-002"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"asset_ids\":[\"asset_en-001\",\"asset_en-002\"]",
                "\"export_ids\":[\"exp-art_004-20240824-png-001\",\"exp-art_005-20240824-png-001\"]",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_44",
        "instruction": "Serving as the design review coordinator for the Web UX team, the time shows 2024-09-02T11:25:00Z. Maintain the consistency of the day\u2019s thread\u2014commence an email-based design review of Figma artifact art_009 using the export profile 'PNG 2x', from emma.creative@company.com to ['jake.design@company.com'], and incorporate the exported asset.",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_009-20240902-001",
                    "artifact_id": "art_009",
                    "started_at": "2024-09-02T11:25:00Z",
                    "timestamp": "2024-09-02T11:25:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_009",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-09-02T11:25:00Z",
                    "request_id": "en-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_009",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-09-02T11:25:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_009 — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com"
                    ],
                    "timestamp": "2024-09-02T11:25:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_009.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-09-02T11:25:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-09-02T11:25:00Z",
                    "ended_at": "2024-09-02T11:25:00Z",
                    "timestamp": "2024-09-02T11:25:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"rev-art_009-20240902-001\"",
                "\"asset_id\":\"asset_en-002\"",
                "\"export_id\":\"exp-art_009-20240902-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_43",
        "instruction": "As the release publisher, the current time is 2024-08-21T12:40:00Z. Brand is arranging guidelines updates\u2014send out a release handoff for artifact art_007 making a reference to release_005, attach an exported asset 'PNG 2x' in the email from anna.brand@company.com to ['sophie.marketing@company.com'].",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_005"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-21T12:40:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_007-20240821-001 — 2024-08-21",
                    "sender_email": "anna.brand@company.com",
                    "recipients": [
                        "sophie.marketing@company.com"
                    ],
                    "timestamp": "2024-08-21T12:40:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "anna.brand@company.com",
                    "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_007-20240821-001, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-21T12:40:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_007",
                    "add_tags": [
                        "released/20240821"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-21T12:40:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-21T12:40:00Z",
                    "ended_at": "2024-08-21T12:40:00Z",
                    "timestamp": "2024-08-21T12:40:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_007-20240821-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_42",
        "instruction": "You are the design review coordinator and the current time is 2024-08-23T16:40:00Z. Ensure continuity for the team\u2014For review cycle cycle_003 on artifact art_007, convey that changes are necessary by responding in the already existing same-day email thread thread_003 to the initial recipients ['jake.design@company.com','chris.engineer@company.com'] using the standard changes-requested template; avoid creating a new subject; attach this thread to the review cycle and log the update.",
        "actions": [
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_003"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_003",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-23T16:40:00Z",
                    "timestamp": "2024-08-23T16:40:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_003"
                },
            },
            {
                "name": "ListGmailMessages",
                "arguments": {
                    "thread_id": "thread_003"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_003",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Changes requested for art_007. Continuing in today’s thread.",
                    "timestamp": "2024-08-23T16:40:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AttachThreadToReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_003",
                    "thread_id": "thread_003",
                    "updated_at": "2024-08-23T16:40:00Z",
                    "timestamp": "2024-08-23T16:40:00Z",
                    "request_id": "rv-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "changes_requested_escalation",
                    "status": "completed",
                    "started_at": "2024-08-23T16:40:00Z",
                    "ended_at": "2024-08-23T16:40:00Z",
                    "timestamp": "2024-08-23T16:40:00Z",
                    "request_id": "rv-003"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_003\"",
                "\"thread_id\":\"thread_003\"",
                "\"message_id\":\"msg_em-001\"",
                "\"run_id\":\"run_rv-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_41",
        "instruction": "You are the governance steward and the current time is 2024-09-02T09:05:00Z. With sign-off verified, handle the update of tags on artifact art_011 by including ['approved'] and excluding ['needs-review']; log the update and dispatch a brief note to ['design-review@company.com'] within the day\u2019s review thread\u2014maintain a single same-day thread (extend it if it is present; otherwise initiate one) utilizing the standard update template.",
        "actions": [
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_011",
                    "add_tags": [
                        "approved"
                    ],
                    "remove_tags": [
                        "needs-review"
                    ],
                    "timestamp": "2024-09-02T09:05:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Update — 2024-09-02",
                    "participant_email": "design-review@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Update — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-09-02T09:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "timestamp": "2024-09-02T09:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "governance_update",
                    "status": "completed",
                    "started_at": "2024-09-02T09:05:00Z",
                    "ended_at": "2024-09-02T09:05:00Z",
                    "timestamp": "2024-09-02T09:05:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"artifact_id\":\"art_011\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_up-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_40",
        "instruction": "As the design review coordinator at 2024-09-02T14:30:00Z, once the morning triage fixes are complete, initiate a re-review request for Figma artifact art_003 directed to ['chris.engineer@company.com', 'anna.brand@company.com'] using the usual re-review notification; maintain a single thread for that day (continue existing if available, otherwise initiate a new one), include the latest 'PNG 2x' export, affix the email label 'design-review', append the kickoff tag 'needs-review' on art_003, and document the action.",
        "actions": [
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Re-review Needed — art_003 — 2024-09-02"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_003",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-09-02T14:30:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Re-review Needed — art_003 — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "timestamp": "2024-09-02T14:30:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Fixes have been applied on art_003; please re-review the latest assets.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-09-02T14:30:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-09-02T14:30:00Z",
                    "request_id": "em-003"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_003",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-09-02T14:30:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "rereview_kickoff",
                    "status": "completed",
                    "started_at": "2024-09-02T14:30:00Z",
                    "ended_at": "2024-09-02T14:30:00Z",
                    "timestamp": "2024-09-02T14:30:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_003-20240902-png-001\"",
                "\"labels\":[\"design-review\"]",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_39",
        "instruction": "Act as the design review coordinator; the current time is 2024-08-23T18:15:00Z. Document end-of-day decisions by incorporating the Gmail thread reference from thread_008 into Figma artifact art_010 as a comment (only include the thread reference, message-level metadata is unnecessary). Subsequently, respond within the thread with the confirmation 'Synced to Figma for art_010 on 2024-08-23.', apply the email label 'synced-to-figma', and log the sync.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_008"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_010",
                    "author_email": "design-review@company.com",
                    "content": "Synced from Gmail thread thread_008 on 2024-08-23.",
                    "timestamp": "2024-08-23T18:15:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_008",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Synced to Figma for art_010 on 2024-08-23.",
                    "timestamp": "2024-08-23T18:15:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_008",
                    "add_labels": [
                        "synced-to-figma"
                    ],
                    "timestamp": "2024-08-23T18:15:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "sync_email_to_figma",
                    "status": "completed",
                    "started_at": "2024-08-23T18:15:00Z",
                    "ended_at": "2024-08-23T18:15:00Z",
                    "timestamp": "2024-08-23T18:15:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_008\"",
                "\"comment_id\":\"comment_up-001\"",
                "\"message_id\":\"msg_em-001\"",
                "\"labels\":[\"synced-to-figma\"]",
                "\"run_id\":\"run_up-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_38",
        "instruction": "In your role as the design systems triage lead at 2024-09-02T16:40:00Z, maintain close coordination with marketing by crafting a minimal fix plan for audit aud-art_012-20240902-001 on artifact art_012, under the ownership of jake.design@company.com. Derive the plan exclusively from DS findings in ['COMPONENT_MISMATCH','SPACING','TOKENS'] (submit an empty plan if none exist); send the plan via EMAIL to ['anna.brand@company.com'] employing the standard fix-plan template, and document the activity.",
        "actions": [
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "aud-art_012-20240902-001",
                    "finding_type": "COMPONENT_MISMATCH"
                },
            },
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "aud-art_012-20240902-001",
                    "finding_type": "SPACING"
                },
            },
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "aud-art_012-20240902-001",
                    "finding_type": "TOKENS"
                },
            },
            {
                "name": "CreateFixPlan",
                "arguments": {
                    "audit_id": "aud-art_012-20240902-001",
                    "owner_email": "jake.design@company.com",
                    "delivery_method": "EMAIL",
                    "timestamp": "2024-09-02T16:40:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "DeliverFixPlan",
                "arguments": {
                    "plan_id": "fp-art_012-20240902-001",
                    "method": "EMAIL",
                    "recipients": [
                        "anna.brand@company.com"
                    ],
                    "timestamp": "2024-09-02T16:40:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fixplan_create_and_deliver",
                    "status": "completed",
                    "started_at": "2024-09-02T16:40:00Z",
                    "ended_at": "2024-09-02T16:40:00Z",
                    "timestamp": "2024-09-02T16:40:00Z",
                    "request_id": "up-001"
                }
            }
        ],
        "outputs": [
                "\"plan_id\":\"fp-art_012-20240902-001\"",
                "\"run_id\":\"run_up-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_37",
        "instruction": "As the lead for design systems triage at 2024-08-24T16:00:00Z, prioritize inbox-first delivery by organizing a minimal fix plan for audit aud-art_003-20240824-001 on artifact art_003, managed by emma.creative@company.com. Examine DS findings regarding ['COMPONENT_MISMATCH','SPACING'] to formulate the plan; upsert only the available items. Dispatch the plan as an EMAIL asset to ['stakeholders@company.com'] and leave a confirmation note in Figma on art_003.",
        "actions": [
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "aud-art_003-20240824-001",
                    "finding_type": "COMPONENT_MISMATCH"
                },
            },
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "aud-art_003-20240824-001",
                    "finding_type": "SPACING"
                },
            },
            {
                "name": "CreateFixPlan",
                "arguments": {
                    "audit_id": "aud-art_003-20240824-001",
                    "owner_email": "emma.creative@company.com",
                    "delivery_method": "EMAIL",
                    "timestamp": "2024-08-24T16:00:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "UpsertFixItems",
                "arguments": {
                    "plan_id": "fp-art_003-20240824-001",
                    "items": [],
                    "timestamp": "2024-08-24T16:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "DeliverFixPlan",
                "arguments": {
                    "plan_id": "fp-art_003-20240824-001",
                    "method": "EMAIL",
                    "recipients": [
                        "stakeholders@company.com"
                    ],
                    "timestamp": "2024-08-24T16:00:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_003",
                    "author_email": "design-review@company.com",
                    "content": "EMAIL",
                    "timestamp": "2024-08-24T16:00:00Z",
                    "request_id": "up-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "fixplan_create_and_deliver",
                    "status": "completed",
                    "started_at": "2024-08-24T16:00:00Z",
                    "ended_at": "2024-08-24T16:00:00Z",
                    "timestamp": "2024-08-24T16:00:00Z",
                    "request_id": "up-004"
                }
            }
        ],
        "outputs": [
                "\"plan_id\":\"fp-art_003-20240824-001\"",
                "\"comment_id\":\"comment_up-003\"",
                "\"run_id\":\"run_up-004\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_36",
        "instruction": "You are the release publisher and the time is 2024-08-23T12:30:00Z. Platform is preparing a ship-room review\u2014coordinate a release handoff for artifact art_010 referencing release_005; export and attach the 'PNG 2x' asset, send an email from sophie.marketing@company.com to ['stakeholders@company.com'] using the release template, apply the email label 'release', tag art_010 with 'released/2024-08-23' after sending, and ensure the run is recorded.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_005"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_010",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T12:30:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_010-20240823-001 — 2024-08-23",
                    "sender_email": "sophie.marketing@company.com",
                    "recipients": [
                        "stakeholders@company.com"
                    ],
                    "timestamp": "2024-08-23T12:30:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "sophie.marketing@company.com",
                    "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_010-20240823-001, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-23T12:30:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "release"
                    ],
                    "timestamp": "2024-08-23T12:30:00Z",
                    "request_id": "em-003"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_010",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T12:30:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-23T12:30:00Z",
                    "ended_at": "2024-08-23T12:30:00Z",
                    "timestamp": "2024-08-23T12:30:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_010-20240823-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"labels\":[\"release\"]",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_35",
        "instruction": "You are the design systems triage lead and the time is 2024-09-02T15:30:00Z. Prior to tomorrow\u2019s stakeholders check-in, for audit aud-art_003-20240902-001 on artifact art_003 (owner emma.creative@company.com), handle the fixplan_create_and_deliver workflow: construct the minimal plan strictly from DS findings in ['COMPONENT_MISMATCH','SPACING'], deliver it as a PDF asset, leave a brief confirmation in Figma, and there is no requirement to record the automation run.",
        "actions": [
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "aud-art_003-20240902-001",
                    "finding_type": "COMPONENT_MISMATCH"
                },
            },
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "aud-art_003-20240902-001",
                    "finding_type": "SPACING"
                },
            },
            {
                "name": "CreateFixPlan",
                "arguments": {
                    "audit_id": "aud-art_003-20240902-001",
                    "owner_email": "emma.creative@company.com",
                    "delivery_method": "PDF",
                    "timestamp": "2024-09-02T15:30:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "UpsertFixItems",
                "arguments": {
                    "plan_id": "fp-art_003-20240902-001",
                    "items": [],
                    "timestamp": "2024-09-02T15:30:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "DeliverFixPlan",
                "arguments": {
                    "plan_id": "fp-art_003-20240902-001",
                    "method": "PDF",
                    "timestamp": "2024-09-02T15:30:00Z",
                    "request_id": "up-002"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_003",
                    "author_email": "emma.creative@company.com",
                    "content": "PDF",
                    "timestamp": "2024-09-02T15:30:00Z",
                    "request_id": "up-003"
                }
            }
        ],
        "outputs": [
                "\"plan_id\":\"fp-art_003-20240902-001\"",
                "\"comment_id\":\"comment_up-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_34",
        "instruction": "As the design review coordinator at 2024-08-24T18:00:00Z, integrate Gmail thread thread_004 into Figma artifact art_008 before the EOD handoff by making a thread-level comment that includes the thread id. Afterward, respond in the same Gmail thread from emma.creative@company.com using the sync confirmation template, apply the 'synced-to-figma' email label, and log the sync.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "design-review@company.com",
                    "content": "Synced from Gmail thread thread_004 on 2024-08-24.",
                    "timestamp": "2024-08-24T18:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Thread thread_004 synced to art_008 on 2024-08-24.",
                    "timestamp": "2024-08-24T18:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_004",
                    "add_labels": [
                        "synced-to-figma"
                    ],
                    "timestamp": "2024-08-24T18:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "sync_email_to_figma",
                    "status": "completed",
                    "started_at": "2024-08-24T18:00:00Z",
                    "ended_at": "2024-08-24T18:00:00Z",
                    "timestamp": "2024-08-24T18:00:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_004\"",
                "\"comment_id\":\"comment_up-001\"",
                "\"message_id\":\"msg_em-001\"",
                "\"labels\":[\"synced-to-figma\"]",
                "\"run_id\":\"run_up-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_33",
        "instruction": "As the release publisher, and the time being 2024-08-23T11:10:00Z, prepare a release handoff for artifact art_011 by summarizing changes since the earlier release tag for release_011. Attach an exported asset using profile 'PNG 2x' in an email from emma.creative@company.com and send it to ['chris.engineer@company.com', 'jake.design@company.com']. Once you have sent the email, if the release date is 2024-08-23, apply the tag 'released/2024-08-23' to the artifact.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_011"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_011",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:10:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_011-20240823-001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "chris.engineer@company.com",
                        "jake.design@company.com"
                    ],
                    "timestamp": "2024-08-23T11:10:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_011-20240823-001, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-23T11:10:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_011",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T11:10:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:10:00Z",
                    "ended_at": "2024-08-23T11:10:00Z",
                    "timestamp": "2024-08-23T11:10:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_011-20240823-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_32",
        "instruction": "On 2024-09-02T11:00:00Z, as the design-system auditor, handle the emergence of taxonomy drift for audit audit_011 on artifact art_011. Examine design-system findings related to ['UNMAPPED','AMBIGUOUS'], create a PDF report based on those findings, complete the audit, and email the PDF to ['design-review@company.com'] using the standard template. Add a brief Figma comment on art_011 referencing the report asset, but do not log the activity.",
        "actions": [
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "audit_011",
                    "finding_type": "UNMAPPED"
                },
            },
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "audit_011",
                    "finding_type": "AMBIGUOUS"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_011",
                    "audit_id": "audit_011",
                    "format": "pdf",
                    "timestamp": "2024-09-02T11:00:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "UpdateAuditStatus",
                "arguments": {
                    "audit_id": "audit_011",
                    "status": "COMPLETED",
                    "updated_at": "2024-09-02T11:00:00Z",
                    "timestamp": "2024-09-02T11:00:00Z",
                    "request_id": "au-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Update — 2024-09-02",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-09-02T11:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "attachments_asset_ids": [
                        "exp-art_011-20240902-pdf-001"
                    ],
                    "timestamp": "2024-09-02T11:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_011",
                    "author_email": "emma.creative@company.com",
                    "content": "Audit report sent — art_011 — audit_011 — 2024-09-02 — asset exp-art_011-20240902-pdf-001",
                    "timestamp": "2024-09-02T11:00:00Z",
                    "request_id": "up-001"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_011\"",
                "\"audit_status\":\"completed\"",
                "\"report_asset_id\":\"exp-art_011-20240902-pdf-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"comment_id\":\"comment_up-001\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_31",
        "instruction": "As the design review coordinator, on 2024-08-24T12:50:00Z, maintain continuity in the existing email conversation thread_006 for artifact art_003 by following up with the latest 'PNG 2x' export. Avoid creating a new subject line; once sent, assign the email label 'design-review'. Then, add a one-line confirmation as a Figma comment on art_003 that references thread_006, and ensure to log the activity.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_006"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_003",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T12:50:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_006",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_003.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-24T12:50:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_006",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-08-24T12:50:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_003",
                    "author_email": "emma.creative@company.com",
                    "content": "Synced from Gmail thread thread_006 on 2024-08-24.",
                    "timestamp": "2024-08-24T12:50:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_followup",
                    "status": "completed",
                    "started_at": "2024-08-24T12:50:00Z",
                    "ended_at": "2024-08-24T12:50:00Z",
                    "timestamp": "2024-08-24T12:50:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_006\"",
                "\"message_id\":\"msg_em-001\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_003-20240824-png-001\"",
                "\"comment_id\":\"comment_up-001\"",
                "\"labels\":[\"design-review\"]",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_30",
        "instruction": "As the governance steward, at the time 2024-08-24T11:35:00Z, with a scheduled IA refresh, alter the tags on artifact art_002 by adding ['navigation', 'global'] and removing none; document the update and make a note in the day\u2019s review thread from emma.creative@company.com directed to ['design-review@company.com'].",
        "actions": [
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_002",
                    "add_tags": [
                        "navigation",
                        "global"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T11:35:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Update — 2024-08-24",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-08-24T11:35:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hello,\nPlease see details attached.\nThanks.",
                    "timestamp": "2024-08-24T11:35:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "governance_update",
                    "status": "completed",
                    "started_at": "2024-08-24T11:35:00Z",
                    "ended_at": "2024-08-24T11:35:00Z",
                    "timestamp": "2024-08-24T11:35:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"artifact_id\":\"art_002\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_up-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_29",
        "instruction": "As the design review coordinator, with the date being 2024-08-21T16:10:00Z, an SLA breach activated the on-call alert. Because of the breach associated with review cycle cycle_004, send an escalation notice marked with 'changes-requested' to the corresponding thread with labels ['Design/Escalation']; ensure the discussion remains connected to the original thread.",
        "actions": [
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_004"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-21T16:10:00Z",
                    "timestamp": "2024-08-21T16:10:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Changes requested for art_008. Continuing in today’s thread.",
                    "timestamp": "2024-08-21T16:10:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_004",
                    "add_labels": [
                        "Design/Escalation"
                    ],
                    "timestamp": "2024-08-21T16:10:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "AttachThreadToReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "thread_id": "thread_004",
                    "updated_at": "2024-08-21T16:10:00Z",
                    "timestamp": "2024-08-21T16:10:00Z",
                    "request_id": "rv-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "changes_requested_escalation",
                    "status": "completed",
                    "started_at": "2024-08-21T16:10:00Z",
                    "ended_at": "2024-08-21T16:10:00Z",
                    "timestamp": "2024-08-21T16:10:00Z",
                    "request_id": "rv-003"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_004\"",
                "\"thread_id\":\"thread_004\"",
                "\"labels\":[\"Design/Escalation\"]",
                "\"run_id\":\"run_rv-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_28",
        "instruction": "As the leader of the accessibility audit, the time is 2024-09-02T09:00:00Z. Prior to sign-off, for audit audit_012 on artifact art_012, examine findings across ['COLOR_CONTRAST', 'FOCUS_ORDER']. Generate a PDF accessibility report solely based on these findings, and document the activity accordingly.",
        "actions": [
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "audit_012",
                    "violation_type": "COLOR_CONTRAST"
                },
            },
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "audit_012",
                    "violation_type": "FOCUS_ORDER"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_012",
                    "audit_id": "audit_012",
                    "format": "pdf",
                    "timestamp": "2024-09-02T09:00:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "a11y_audit_report",
                    "status": "completed",
                    "started_at": "2024-09-02T09:00:00Z",
                    "ended_at": "2024-09-02T09:00:00Z",
                    "timestamp": "2024-09-02T09:00:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"audit_012\"",
                "\"asset_id\":\"exp-art_012-20240902-pdf-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_27",
        "instruction": "As the release publisher, it's 2024-08-21T11:20:00Z. Design Ops requested a concise story for the preliminary leadership meeting. Provide a release handoff for artifact art_009 and note changes since the last release tag for release_004. Be sure to attach an exported asset using profile 'PNG 2x' in an email from chris.engineer@company.com to ['jake.design@company.com', 'anna.brand@company.com']. The release date is 2024-08-23. After dispatching, apply the tag 'released/2024-08-23' to the artifact.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_004"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_009",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-21T11:20:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_009-20240821-001 — 2024-08-21",
                    "sender_email": "chris.engineer@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "anna.brand@company.com"
                    ],
                    "timestamp": "2024-08-21T11:20:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "chris.engineer@company.com",
                    "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_009-20240821-001, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-21T11:20:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_009",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-21T11:20:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-21T11:20:00Z",
                    "ended_at": "2024-08-21T11:20:00Z",
                    "timestamp": "2024-08-21T11:20:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_009-20240821-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_26",
        "instruction": "Serving as the design review coordinator at 2024-09-02T12:00:00Z, a reminder for the SLA arrived just ahead of lunch. For the review cycle cycle_011 concerning artifact art_011, send out a changes-requested update and raise it within the corresponding thread using labels ['Design/Escalation'];",
        "actions": [
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_011"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_011",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-09-02T12:00:00Z",
                    "timestamp": "2024-09-02T12:00:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_011",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Changes requested for art_011. Continuing in today’s thread.",
                    "timestamp": "2024-09-02T12:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_011",
                    "add_labels": [
                        "Design/Escalation"
                    ],
                    "timestamp": "2024-09-02T12:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "AttachThreadToReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_011",
                    "thread_id": "thread_011",
                    "updated_at": "2024-09-02T12:00:00Z",
                    "timestamp": "2024-09-02T12:00:00Z",
                    "request_id": "rv-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "changes_requested_escalation",
                    "status": "completed",
                    "started_at": "2024-09-02T12:00:00Z",
                    "ended_at": "2024-09-02T12:00:00Z",
                    "timestamp": "2024-09-02T12:00:00Z",
                    "request_id": "rv-003"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_011\"",
                "\"thread_id\":\"thread_011\"",
                "\"labels\":[\"Design/Escalation\"]",
                "\"run_id\":\"run_rv-003\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_25",
        "instruction": "As the release publisher with the time being 2024-08-21T10:00:00Z, Security requires a succinct diff summary. Provide a release handoff for artifact art_002 that highlights modifications since the earlier release tag for release_001. In your email from emma.creative@company.com to ['jake.design@company.com'], attach an exported asset using the 'PNG 2x' profile. Following this, label the artifact with the tag 'released/2024-08-21' after dispatching.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_002",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-21T10:00:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_002-20240821-001 — 2024-08-21",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com"
                    ],
                    "timestamp": "2024-08-21T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_002-20240821-001, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-21T10:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_002",
                    "add_tags": [
                        "released/2024-08-21"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-21T10:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-21T10:00:00Z",
                    "ended_at": "2024-08-21T10:00:00Z",
                    "timestamp": "2024-08-21T10:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_002-20240821-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_24",
        "instruction": "Acting as the design review coordinator and with the time set at 2024-08-23T13:20:00Z, maintain an organized thread for artifact art_001\u2014resume discussions in the ongoing email conversation thread_001, including the most recent export 'PNG 2x'. Update the 'needs-review' tag on the artifact for today's review session; refrain from initiating a new thread; log the activity in the review kickoff log. Use the text 'Hi team, Please review the attached PNG 2x export for art_001. Thanks.' for the email body.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ListGmailMessages",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T13:20:00Z",
                    "request_id": "en-001"
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
                    "timestamp": "2024-08-23T13:20:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-23T13:20:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T13:20:00Z",
                    "ended_at": "2024-08-23T13:20:00Z",
                    "timestamp": "2024-08-23T13:20:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_001\"",
                "\"message_id\":\"msg_em-001\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_001-20240823-png-001\"",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_23",
        "instruction": "As the review program manager, with the current time being 2024-09-02T09:40:00Z, for the initial Monday sprint this month, during the review cycle cycle_012, manage approvals for ['jake.design@company.com'] at ['2024-09-02T09:45:00Z'], and indicate if quorum has been achieved, if applicable.",
        "actions": [
            {
                "name": "UpdateReviewApproval",
                "arguments": {
                    "cycle_id": "cycle_012",
                    "approver_email": "jake.design@company.com",
                    "approved_ts_nullable": "2024-09-02T09:45:00Z",
                    "timestamp": "2024-09-02T09:40:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "approvals_append",
                    "status": "completed",
                    "started_at": "2024-09-02T09:40:00Z",
                    "ended_at": "2024-09-02T09:40:00Z",
                    "timestamp": "2024-09-02T09:40:00Z",
                    "request_id": "rv-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_012\"",
                "\"run_id\":\"run_rv-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_22",
        "instruction": "Serving as the design review coordinator for the Web UX team at 2024-08-24T10:05:00Z, kick off the morning\u2019s sync with a design review for Figma artifact art_003. As part of the initiation, attach the 'needs-review' tag to the artifact and email the exported asset 'PNG 2x' to ['jake.design@company.com'].",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_003",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T10:05:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_003",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-24T10:05:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_003 — 2024-08-24",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com"
                    ],
                    "timestamp": "2024-08-24T10:05:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_003.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-24T10:05:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-24T10:05:00Z",
                    "ended_at": "2024-08-24T10:05:00Z",
                    "timestamp": "2024-08-24T10:05:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_003-20240824-png-001\"",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_21",
        "instruction": "As the design review coordinator for the Web UX team at 2024-08-23T11:45:00Z, the review alias is ready. Start an email-based design review of Figma artifact art_001 using export profile 'PNG 2x'. Send it from emma.creative@company.com to ['design-review@company.com']; make sure the review email contains the exported asset and add the label 'design-review'.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "en-001"
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
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "design-review@company.com"
                    ],
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "add_labels": [
                        "design-review"
                    ],
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "em-003"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:45:00Z",
                    "ended_at": "2024-08-23T11:45:00Z",
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"labels\":[\"design-review\"]",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_001-20240823-png-001\"",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_20",
        "instruction": "Being the design review coordinator as of 2024-08-24T17:00:00Z, ensure to synchronize the most recent message from Gmail thread thread_006 into Figma artifact art_003 as a comment before finishing the day, and log the synchronization.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_006"
                },
            },
            {
                "name": "ListGmailMessages",
                "arguments": {
                    "thread_id": "thread_006"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_003",
                    "author_email": "design-review@company.com",
                    "content": "Synced from Gmail thread thread_006 on 2024-08-24.",
                    "timestamp": "2024-08-24T17:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "sync_email_to_figma",
                    "status": "completed",
                    "started_at": "2024-08-24T17:00:00Z",
                    "ended_at": "2024-08-24T17:00:00Z",
                    "timestamp": "2024-08-24T17:00:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_006\"",
                "\"artifact_id\":\"art_003\"",
                "\"comment_id\":\"comment_up-001\"",
                "\"run_id\":\"run_up-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_19",
        "instruction": "As the release publisher with the current time being 2024-08-21T09:15:00Z, inform partner engineering about the upcoming verification run. Distribute a release handoff for artifact art_004 that summarizes the modifications since the last release tag for release_003. Ensure an exported asset using profile 'PNG 2x' is included in the email from jake.design@company.com to ['chris.engineer@company.com']. Following the dispatch, append the tag 'released / 2024-08-21' to the artifact and document the run.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_003"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_004",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-21T09:15:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_004-20240821-001 — 2024-08-21",
                    "sender_email": "jake.design@company.com",
                    "recipients": [
                        "chris.engineer@company.com"
                    ],
                    "timestamp": "2024-08-21T09:15:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "jake.design@company.com",
                    "recipients": [
                        "chris.engineer@company.com"
                    ],
                    "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_004-20240821-001, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-21T09:15:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_004",
                    "add_tags": [
                        "released/2024-08-21"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-21T09:15:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-21T09:15:00Z",
                    "ended_at": "2024-08-21T09:15:00Z",
                    "timestamp": "2024-08-21T09:15:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_004-20240821-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_18",
        "instruction": "Acting as the design review coordinator, and the present time is 2024-08-24T12:30:00Z, when banner slot has copy tweaks, distribute a changes-requested update for review cycle cycle_005. Escalate to ['chris.engineer@company.com'] with labels ['design-review','Design/Escalation']; ensure the conversation remains within the same day's thread.",
        "actions": [
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_005",
                    "add_labels": [
                        "design-review",
                        "Design/Escalation"
                    ],
                    "remove_labels": [],
                    "timestamp": "2024-08-24T12:30:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_005",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "chris.engineer@company.com"
                    ],
                    "body_html": "Changes requested for art_003. Continuing in today’s thread.",
                    "timestamp": "2024-08-24T12:30:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_005",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-24T12:30:00Z",
                    "timestamp": "2024-08-24T12:30:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "changes_requested_escalation",
                    "status": "completed",
                    "started_at": "2024-08-24T12:30:00Z",
                    "ended_at": "2024-08-24T12:30:00Z",
                    "timestamp": "2024-08-24T12:30:00Z",
                    "request_id": "rv-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_005\"",
                "\"thread_id\":\"thread_005\"",
                "\"labels\":[\"design-review\",\"Design/Escalation\"]",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rv-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_17",
        "instruction": "As the design review coordinator for the Web UX team, and with the current time being 2024-08-23T11:45:00Z, initiate a lunchtime overview of the homepage. Send an email-based design review by attaching the export 'PNG 2x' from 'art_001' in one message to ['jake.design@company.com', 'chris.engineer@company.com', 'anna.brand@company.com']; maintain a single email thread for the review throughout the day.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "en-001"
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
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:45:00Z",
                    "ended_at": "2024-08-23T11:45:00Z",
                    "timestamp": "2024-08-23T11:45:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_001-20240823-png-001\"",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_16",
        "instruction": "As the review program manager at 2024-08-24T09:20:00Z, coordinate the locking of the Friday rollout for review cycle cycle_008 by recording approvals from ['chris.engineer@company.com', 'jake.design@company.com'] at ['2024-08-24T09:25:00Z', '2024-08-24T09:29:00Z'], and note if the quorum has been reached.",
        "actions": [
            {
                "name": "UpdateReviewApproval",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "approver_email": "chris.engineer@company.com",
                    "approved_ts_nullable": "2024-08-24T09:25:00Z",
                    "timestamp": "2024-08-24T09:20:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "UpdateReviewApproval",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "approver_email": "jake.design@company.com",
                    "approved_ts_nullable": "2024-08-24T09:29:00Z",
                    "timestamp": "2024-08-24T09:20:00Z",
                    "request_id": "rv-002"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "status": "APPROVED",
                    "updated_at": "2024-08-24T09:20:00Z",
                    "timestamp": "2024-08-24T09:20:00Z",
                    "request_id": "rv-003"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "approved/2024-08-24"
                    ],
                    "remove_tags": [
                        "needs-review"
                    ],
                    "timestamp": "2024-08-24T09:20:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "approvals_append",
                    "status": "completed",
                    "started_at": "2024-08-24T09:20:00Z",
                    "ended_at": "2024-08-24T09:20:00Z",
                    "timestamp": "2024-08-24T09:20:00Z",
                    "request_id": "rv-004"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_008\"",
                "\"cycle_status\":\"approved\"",
                "\"run_id\":\"run_rv-004\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_15",
        "instruction": "As the design review coordinator for the Web UX team, with the current time being 2024-08-24T09:15:00Z, initiate an email-based design review for Figma artifact art_001 utilizing the export profile 'PNG 2x'. Maintain a single email thread per artifact for the day, and continue in the existing thread if it has already been initiated. Make sure the review email includes the exported asset and is sent to ['jake.design@company.com', 'chris.engineer@company.com']. Recording the run is not necessary.",
        "actions": [
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — art_001 — 2024-08-24",
                    "participant_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_001-20240824-001",
                    "artifact_id": "art_001",
                    "started_at": "2024-08-24T09:15:00Z",
                    "timestamp": "2024-08-24T09:15:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-24T09:15:00Z",
                    "request_id": "en-001"
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
                    "timestamp": "2024-08-24T09:15:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_001 — 2024-08-24",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com"
                    ],
                    "timestamp": "2024-08-24T09:15:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com"
                    ],
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-24T09:15:00Z",
                    "request_id": "em-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"rev-art_001-20240824-001\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_001-20240824-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_14",
        "instruction": "Serving as the design review coordinator and at the time 2024-08-24T09:15:00Z, after overnight fixes have been implemented for the homepage, solicit a re-review for Figma artifact art_001 addressed to ['jake.design@company.com', 'chris.engineer@company.com'] utilizing the standard re-review notice. Initiate a new email thread for today\u2019s re-review and document the activity.",
        "actions": [
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — art_001 — 2024-08-24",
                    "participant_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Re-review Needed — art_001 — 2024-08-24",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com"
                    ],
                    "timestamp": "2024-08-24T09:15:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com"
                    ],
                    "body_html": "Fixes have been applied on art_001; please re-review the latest assets.",
                    "timestamp": "2024-08-24T09:15:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "rereview_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-24T09:15:00Z",
                    "ended_at": "2024-08-24T09:15:00Z",
                    "timestamp": "2024-08-24T09:15:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"status\":\"completed\"",
                "\"run_id\":\"run_rv-001\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_13",
        "instruction": "As the design review coordinator for the Web UX team and at the time 2024-08-23T11:25:00Z, maintain a tidy inbox during the lunch crunch\u2014initiate an email-based design review for Figma artifact art_002 utilizing export profile 'PNG 2x'. Ensure a single email thread is kept per artifact for the day, and continue using the existing thread if it has already been initiated. Ensure that the review email incorporates the exported asset sent to ['anna.brand@company.com'].",
        "actions": [
            {
                "name": "FindGmailThreads",
                "arguments": {
                    "subject_contains": "Review Request — art_002 — 2024-08-23",
                    "participant_email": "anna.brand@company.com"
                },
            },
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_002-20240823-001",
                    "artifact_id": "art_002",
                    "started_at": "2024-08-23T11:25:00Z",
                    "timestamp": "2024-08-23T11:25:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_002",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T11:25:00Z",
                    "request_id": "en-002"
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
                    "timestamp": "2024-08-23T11:25:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_002 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "anna.brand@company.com"
                    ],
                    "initial_labels": [],
                    "timestamp": "2024-08-23T11:25:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "anna.brand@company.com"
                    ],
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_002.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-002"
                    ],
                    "timestamp": "2024-08-23T11:25:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T11:25:00Z",
                    "ended_at": "2024-08-23T11:25:00Z",
                    "timestamp": "2024-08-23T11:25:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"rev-art_002-20240823-001\"",
                "\"asset_id\":\"asset_en-002\"",
                "\"export_id\":\"exp-art_002-20240823-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_12",
        "instruction": "Coordinate the release publishing as the time reads 2024-08-22T18:00:00Z. The product team requires a clear narrative for the upcoming digest\u2014provide a release handoff for artifact art_003 detailing changes since the prior release tag for release_001. Ensure to attach an exported asset using profile 'PNG 2x' in the email from emma.creative@company.com to ['jake.design@company.com', 'chris.engineer@company.com']; after sending, if the release date aligns with 2024-08-23, attach the tag 'released/2024-08-23' to the artifact.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_003",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-22T18:00:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — rel-art_003-20240822-001 — 2024-08-22",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com"
                    ],
                    "initial_labels": [],
                    "timestamp": "2024-08-22T18:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com"
                    ],
                    "body_html": "Hello stakeholders,\nPlease find the release notes for rel-art_003-20240822-001, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-22T18:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_003",
                    "add_tags": [
                        "released/2024-08-23"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-22T18:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-22T18:00:00Z",
                    "ended_at": "2024-08-22T18:00:00Z",
                    "timestamp": "2024-08-22T18:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_003-20240822-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_11",
        "instruction": "Handle a design review for the Web UX team with the current time as 2024-08-23T10:35:00Z. A stakeholder preview is scheduled right after lunch\u2014initiate a design review for Figma artifact art_003. During kickoff, append the tag 'needs-review' to the artifact, and ensure the exported asset 'PNG 2x' is included in the email to ['jake.design@company.com', 'chris.engineer@company.com'].",
        "actions": [
            {
                "name": "CreateReviewCycle",
                "arguments": {
                    "cycle_id": "rev-art_003-20240823-001",
                    "artifact_id": "art_003",
                    "started_at": "2024-08-23T10:35:00Z",
                    "timestamp": "2024-08-23T10:35:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_003",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:35:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_003",
                    "add_tags": [
                        "needs-review"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-23T10:35:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_003 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com"
                    ],
                    "timestamp": "2024-08-23T10:35:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com"
                    ],
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_003.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-23T10:35:00Z",
                    "request_id": "em-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"rev-art_003-20240823-001\"",
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_003-20240823-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_10",
        "instruction": "Serve as the review program manager at 2024-08-23T15:00:00Z. With sign-off impacting the deployment window, for review cycle cycle_001, register approvals for ['jake.design@company.com', 'chris.engineer@company.com'] at times ['2024-08-23T15:05:00Z', '2024-08-23T15:07:00Z'], and confirm quorum achieved if applicable.",
        "actions": [
            {
                "name": "GetReviewCycle",
                "arguments": {
                    "cycle_id": "cycle_001"
                },
            },
            {
                "name": "UpdateReviewApproval",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approved_ts_nullable": "2024-08-23T15:05:00Z",
                    "timestamp": "2024-08-23T15:00:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "UpdateReviewApproval",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "chris.engineer@company.com",
                    "approved_ts_nullable": "2024-08-23T15:07:00Z",
                    "timestamp": "2024-08-23T15:00:00Z",
                    "request_id": "rv-002"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "status": "APPROVED",
                    "updated_at": "2024-08-23T15:00:00Z",
                    "timestamp": "2024-08-23T15:00:00Z",
                    "request_id": "rv-003"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "approved/2024-08-23"
                    ],
                    "remove_tags": [
                        "needs-review"
                    ],
                    "timestamp": "2024-08-23T15:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "approvals_append",
                    "status": "completed",
                    "started_at": "2024-08-23T15:00:00Z",
                    "ended_at": "2024-08-23T15:00:00Z",
                    "timestamp": "2024-08-23T15:00:00Z",
                    "request_id": "rv-004"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_001\"",
                "\"cycle_status\":\"approved\"",
                "\"run_id\":\"run_rv-004\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_09",
        "instruction": "Act as the design review coordinator at the time 2024-08-24T16:45:00Z. The team seeks to have the most recent feedback noted before Monday\u2019s stand-up\u2014integrate the newest message from Gmail thread thread_011 into Figma artifact art_011 as a comment and make sure to log the sync.",
        "actions": [
            {
                "name": "GetGmailThread",
                "arguments": {
                    "thread_id": "thread_011"
                },
            },
            {
                "name": "ListGmailMessages",
                "arguments": {
                    "thread_id": "thread_011"
                },
            },
            {
                "name": "CreateFigmaComment",
                "arguments": {
                    "artifact_id": "art_011",
                    "author_email": "design-review@company.com",
                    "content": "Synced from Gmail thread thread_011 on 2024-08-24.",
                    "timestamp": "2024-08-24T16:45:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "sync_email_to_figma",
                    "status": "completed",
                    "started_at": "2024-08-24T16:45:00Z",
                    "ended_at": "2024-08-24T16:45:00Z",
                    "timestamp": "2024-08-24T16:45:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"thread_id\":\"thread_011\"",
                "\"artifact_id\":\"art_011\"",
                "\"comment_id\":\"comment_up-001\"",
                "\"run_id\":\"run_up-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_08",
        "instruction": "Assume the role of the design review coordinator at 2024-08-23T17:10:00Z. After a late-afternoon QA sweep revealed several regressions, for review cycle cycle_001, issue a changes-requested update and escalate to ['anna.brand@company.com'] with labels ['Design/Escalation','design-review']; ensure the ongoing discussion remains within the same day\u2019s thread.",
        "actions": [
            {
                "name": "ApplyGmailLabels",
                "arguments": {
                    "thread_id": "thread_001",
                    "add_labels": [
                        "Design/Escalation",
                        "design-review"
                    ],
                    "remove_labels": [],
                    "timestamp": "2024-08-23T17:10:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "ListReviewCycles",
                "arguments": {
                {}
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "anna.brand@company.com"
                    ],
                    "body_html": "Changes requested for art_001. Continuing in today’s thread.",
                    "timestamp": "2024-08-23T17:10:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "UpdateReviewCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "status": "CHANGES_REQUESTED",
                    "updated_at": "2024-08-23T17:10:00Z",
                    "timestamp": "2024-08-23T17:10:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "changes_requested_escalation",
                    "status": "completed",
                    "started_at": "2024-08-23T17:10:00Z",
                    "ended_at": "2024-08-23T17:10:00Z",
                    "timestamp": "2024-08-23T17:10:00Z",
                    "request_id": "rv-002"
                }
            }
        ],
        "outputs": [
                "\"cycle_id\":\"cycle_001\"",
                "\"labels\":[\"Design/Escalation\",\"design-review\"]",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rv-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_07",
        "instruction": "Act as the release publisher with the current time being 2024-08-22T17:00:00Z. A hotfix window is scheduled for tonight, and stakeholders require a concise summary before entering the ship room. Provide a release handoff for artifact art_001, summarizing the changes since the previous release tag for release_001. Include an exported asset using profile 'PNG 2x' in the email from emma.creative@company.com to ['chris.engineer@company.com', 'anna.brand@company.com', 'jake.design@company.com']; following the send, apply the tag 'released/2024-08-22' to the artifact.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — release_001 — 2024-08-22",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "chris.engineer@company.com",
                        "anna.brand@company.com",
                        "jake.design@company.com"
                    ],
                    "initial_labels": [],
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hello stakeholders,\nPlease find the release notes for release_001, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/2024-08-22"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-22T17:00:00Z",
                    "ended_at": "2024-08-22T17:00:00Z",
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"asset_id\":\"asset_en-001\"",
                "\"export_id\":\"exp-art_001-20240822-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "TASK_06",
        "instruction": "Act as the design review coordinator for the Web UX team as of 2024-08-23T09:10:00Z. Start an email-based design review for artifact art_001 using the 'PNG 2x' export profile from emma.creative@company.com. Address it to [jake.design@company.com, chris.engineer@company.com, anna.brand@company.com], mark the artifact for review, ensure the exported asset is part of the templated email, and log the run.",
        "actions": [
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "needs-review"
                    ],
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "rv-001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "rv-002"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "rv-003"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_rv-003",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_rv-002"
                    ],
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "rv-004"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T09:10:00Z",
                    "ended_at": "2024-08-23T09:10:00Z",
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "rv-005"
                }
            }
        ],
        "outputs": [
                "\"export_id\":\"exp-art_001-20240823-png-001\"",
                "\"thread_id\":\"thr_rv-003\"",
                "\"message_id\":\"msg_rv-004\"",
                "\"run_id\":\"run_rv-005\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_05",
        "instruction": "Handle the design review coordination for the Web UX team as of 2024-08-23T09:10:00Z. Begin a design review via email for Figma artifact art_001 utilizing export profile 'PNG 2x'. Send this from emma.creative@company.com to the following recipients: [jake.design@company.com, chris.engineer@company.com, anna.brand@company.com]. Ensure the review email includes the exported asset.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "en-001"
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
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "initial_labels": [],
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "review_kickoff",
                    "status": "completed",
                    "started_at": "2024-08-23T09:10:00Z",
                    "ended_at": "2024-08-23T09:10:00Z",
                    "timestamp": "2024-08-23T09:10:00Z",
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"export_id\":\"exp-art_001-20240823-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_04",
        "instruction": "Acting as the design systems triage lead at the current time of 2024-08-23T13:10:00Z, coordinate a minimal fix plan for audit aud-art_003-20240823-001 on Figma artifact art_003, under the ownership of emma.creative@company.com. Concentrate on issues related to the design system, such as component mismatches and ensuring spacing consistency. Communicate the plan through COMMENTS tied to the artifact, and document this activity under the name ds_audit_fix. Rely only on the given data or information from tools; if no relevant findings exist, provide an empty plan through COMMENTS, refraining from creating items.",
        "actions": [
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "aud-art_003-20240823-001",
                    "finding_type": "COMPONENT_MISMATCH"
                },
            },
            {
                "name": "ListAuditFindingsDs",
                "arguments": {
                    "audit_id": "aud-art_003-20240823-001",
                    "finding_type": "SPACING"
                },
            },
            {
                "name": "CreateFixPlan",
                "arguments": {
                    "audit_id": "aud-art_003-20240823-001",
                    "owner_email": "emma.creative@company.com",
                    "delivery_method": "COMMENTS",
                    "timestamp": "2024-08-23T13:10:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "DeliverFixPlan",
                "arguments": {
                    "plan_id": "fp-art_003-20240823-001",
                    "method": "COMMENTS",
                    "timestamp": "2024-08-23T13:10:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "ds_audit_fix",
                    "status": "completed",
                    "started_at": "2024-08-23T13:10:00Z",
                    "ended_at": "2024-08-23T13:10:00Z",
                    "timestamp": "2024-08-23T13:10:00Z",
                    "request_id": "up-002"
                }
            }
        ],
        "outputs": [
                "\"plan_id\":\"fp-art_003-20240823-001\"",
                "\"method\":\"COMMENTS\"",
                "\"run_id\":\"run_up-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_03",
        "instruction": "As the accessibility audit lead for the Web UX team, and given the current time of 2024-08-23T12:05:00Z, you need to handle audit aud-art_003-20240823-001 on Figma artifact art_003. Review the accessibility findings within the specified categories: COLOR_CONTRAST, ALT_TEXT, and FOCUS_ORDER, confirming each category is adequately covered. Afterward, compile a PDF accessibility report strictly reflecting these findings and log the activity. Avoid fabricating any values.",
        "actions": [
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "aud-art_003-20240823-001",
                    "violation_type": "COLOR_CONTRAST"
                },
            },
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "aud-art_003-20240823-001",
                    "violation_type": "ALT_TEXT"
                },
            },
            {
                "name": "ListAuditFindingsA11y",
                "arguments": {
                    "audit_id": "aud-art_003-20240823-001",
                    "violation_type": "FOCUS_ORDER"
                },
            },
            {
                "name": "generateAuditReport",
                "arguments": {
                    "artifact_id": "art_003",
                    "audit_id": "aud-art_003-20240823-001",
                    "format": "pdf",
                    "timestamp": "2024-08-23T12:05:00Z",
                    "request_id": "au-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "a11y_audit",
                    "status": "completed",
                    "started_at": "2024-08-23T12:05:00Z",
                    "ended_at": "2024-08-23T12:05:00Z",
                    "timestamp": "2024-08-23T12:05:00Z",
                    "request_id": "au-002"
                }
            }
        ],
        "outputs": [
                "\"audit_id\":\"aud-art_003-20240823-001\"",
                "\"asset_id\":\"exp-art_003-20240823-pdf-001\"",
                "\"run_id\":\"run_au-002\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_02",
        "instruction": "Manage the release publishing for the Design System team as of 2024-08-22T17:00:00Z. Distribute a release handoff for Figma artifact art_001 citing release_001, and send it from emma.creative@company.com to [chris.engineer@company.com, anna.brand@company.com, jake.design@company.com]. Use the profile 'PNG 2x' to export the asset and make sure to attach it within the email.",
        "actions": [
            {
                "name": "GetReleaseDiff",
                "arguments": {
                    "release_id": "release_001"
                },
            },
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "en-001"
                },
            },
            {
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Release Handoff — release_001 — 2024-08-22",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "chris.engineer@company.com",
                        "anna.brand@company.com",
                        "jake.design@company.com"
                    ],
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hello stakeholders,\nPlease find the release notes for release_001, including changes.\nRegards.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "em-002"
                },
            },
            {
                "name": "GovernanceUpdate",
                "arguments": {
                    "artifact_id": "art_001",
                    "add_tags": [
                        "released/20240822"
                    ],
                    "remove_tags": [],
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "up-001"
                },
            },
            {
                "name": "RecordAutomationRun",
                "arguments": {
                    "task_name": "release_handoff",
                    "status": "completed",
                    "started_at": "2024-08-22T17:00:00Z",
                    "ended_at": "2024-08-22T17:00:00Z",
                    "timestamp": "2024-08-22T17:00:00Z",
                    "request_id": "rl-001"
                }
            }
        ],
        "outputs": [
                "\"export_id\":\"exp-art_001-20240822-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rl-001\"",
                "\"status\":\"completed\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_01",
        "instruction": "Handle the role of design review coordinator for the Web UX team as of 2024-08-23T10:00:00Z. Initiate a design review via email for Figma artifact art_001 using the export profile 'PNG 2x'. Send this from emma.creative@company.com to [jake.design@company.com, chris.engineer@company.com, anna.brand@company.com]. Ensure that the review email contains the exported asset.",
        "actions": [
            {
                "name": "ExportAssets",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "en-001"
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
                "name": "CreateGmailThread",
                "arguments": {
                    "subject": "Review Request — art_001 — 2024-08-23",
                    "sender_email": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "initial_labels": [],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-001"
                },
            },
            {
                "name": "AppendGmailMessage",
                "arguments": {
                    "thread_id": "thr_em-001",
                    "sender_email": "emma.creative@company.com",
                    "body_html": "Hi team,\nPlease review the attached PNG 2x export for art_001.\nThanks.",
                    "attachments_asset_ids": [
                        "asset_en-001"
                    ],
                    "timestamp": "2024-08-23T10:00:00Z",
                    "request_id": "em-002"
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
                    "request_id": "rv-001"
                }
            }
        ],
        "outputs": [
                "\"export_id\":\"exp-art_001-20240823-png-001\"",
                "\"thread_id\":\"thr_em-001\"",
                "\"message_id\":\"msg_em-002\"",
                "\"run_id\":\"run_rv-001\"",
                "\"status\":\"completed\""
        ]
    }
]
