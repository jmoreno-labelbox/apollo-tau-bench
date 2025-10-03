
tasks = [
    {
        "annotator": 0,
        "user_id": "task_01",
        "instruction": "Handle a review request submission for your frame as 'emma.creative@company.com' by exporting a PNG 2x asset for that frame with the filename 'hero-section-2x-r2.png' in the Gmail thread addressed to 'jake.design@company.com', 'chris.engineer@company.com', 'anna.brand@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "emma.creative@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-2x-r2.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_001",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-2x-r2.png",
                    "sender_id": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-2x-r2.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_02",
        "instruction": "As 'jake.design@company.com', coordinate the approval of the existing review thread 'Design Review: Homepage Hero Section' with the message 'Good Job' for asset 'asset_001'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_03",
        "instruction": "As 'jake.design@company.com', in the ongoing review thread 'Design Review: Homepage Hero Section', you should ask for modifications using the message 'please update the headline spacing and button contrast.' related to asset 'asset_001'. Once the author communicates that changes have been made with the message 'adjusted headline spacing and increased primary button contrast', proceed to approve it with the message 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_04",
        "instruction": "Representing 'jake.design@company.com', and in the current discussion with the subject 'Navigation Bar Responsive Design', you need to request adjustments using the message 'please refine pricing table spacing and switch CTA to primary-600.' for the artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_05",
        "instruction": "As 'anna.brand@company.com', your goal is to prepare a review request for your frame by creating a PNG 2x asset for that frame, saving it as 'pricing-page-2x-r2.png', and sending it through a gmail thread addressed to 'emma.creative@company.com', 'jake.design@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/pricing-page-2x-r2.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: pricing-page-2x-r2.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the pricing-page-2x-r2.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_06",
        "instruction": "Being 'jake.design@company.com', your task is to approve the existing review thread 'Admin Panel Accessibility Audit' with the comment 'Good Job, but done late' for the 'asset_007'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_07",
        "instruction": "You are 'jake.design@company.com' and it's necessary to review the 'Admin Panel Accessibility Audit', which is past SLA\u2014initiate changes in the existing thread with the message 'SLA breached; please prioritize fixes and resubmit'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: SLA breached; please prioritize fixes and resubmit</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_004",
                    "escalated_ts": "2024-08-23T12:00:00Z"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_004",
                    "artifact_id": "art_008",
                    "thread_id_nullable": "thread_004",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-18T15:30:00Z",
                    "sla_deadline_ts": "2024-08-21T15:30:00Z",
                    "sla_breached_flag": true,
                    "escalated_ts_nullable": "2024-08-23T12:00:00Z"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_08",
        "instruction": "You are 'jake.design@company.com'. Distribute release notes for 'Design System v1.3.0 - Form Components & Accessibility' to the existing release thread, ensuring inclusion of PNG 3x exports for newly added frames, and specify the changed frames from the release diff.",
        "actions": [
            {
                "name": "GetReleaseDetailsByName",
                "arguments": {
                    "release_name": "Design System v1.3.0 - Form Components & Accessibility"
                },
            },
            {
                "name": "GetReleaseDiffByReleaseId",
                "arguments": {
                    "release_id": "release_011"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:5",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:5.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:5.png"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_014",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:6.png"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:7",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:7.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_015",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:7.png"
                },
            },
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes"
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_013",
                    "body_html": "<h2>Design System v1.3.0 - Form Components & Accessibility</h2><p>Highlights:</p><ul><li>Added frame 1:5</li><li>Added frame 1:6</li><li>Added frame 1:7</li><li>Updated frame 1:3</li><li>Updated frame 1:4</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019",
                        "asset_020",
                        "asset_021"
                    ]
                }
            }
        ],
        "outputs": [
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
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_09",
        "instruction": "You are 'jake.design@company.com'. Construct a fresh App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with the tag 'mobile-app-v2.3.0', referencing prior release id as release_012, by introducing new frame '2:6' and revising frames '2:4' and '2:2' and exporting new PNG 2x frames to the recipients 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [
                        "2:4",
                        "2:2"
                    ],
                    "frames_removed": [],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Updated 2 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Updated frame 2:2,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_10",
        "instruction": "You are 'jake.design@company.com'. Construct a fresh App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with the tag 'mobile-app-v2.3.0', referencing prior release id as release_012, by introducing new frame '2:6' and removing frames '2:4' and exporting new PNG 2x frames to the recipients 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [],
                    "frames_removed": [
                        "2:4"
                    ],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Removed 1 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Removed frame 2:4,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_11",
        "instruction": "As 'jake.design@company.com', handle the creation of a new App release titled 'Mobile App v2.3.0 - Notifications & Settings Polish' with the tag 'mobile-app-v2.3.0' using the previous release id as release_012. Add new frame '2:6', update frames '2:4', and remove '2:2'. Export the new PNG 2x frames to 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [
                        "2:4"
                    ],
                    "frames_removed": [
                        "2:2"
                    ],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Updated 1 frames",
                        "Removed 1 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Removed frame 2:2,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_12",
        "instruction": "Acting as 'jake.design@company.com', in the current review thread 'Design Review: Homepage Hero Section', coordinate a request for changes with the message 'please update the headline spacing and button contrast.' for asset 'asset_001'. Once the author confirms changes with the message 'adjusted headline spacing and increased primary button contrast', approve with the message 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_13",
        "instruction": "You are 'jake.design@company.com' and your task is to propose modifications in the ongoing discussion under the subject 'Navigation Bar Responsive Design' by sending the message 'please refine pricing table spacing and switch CTA to primary-600.' along with the current artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_14",
        "instruction": "You are 'jake.design@company.com'. your responsibility is to approve the current review thread 'Admin Panel Accessibility Audit' with the message 'Good Job, but done late' for asset 'asset_007'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_15",
        "instruction": "As 'anna.brand@company.com', coordinate a review request submission for your frame by exporting a PNG 3x asset named 'hero-section-3x.png' and include it in a Gmail thread addressed to 'emma.creative@company.com' and 'jake.design@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-3x.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                },
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_16",
        "instruction": "Being 'jake.design@company.com', you are required to approve the existing review thread 'Design Review: Homepage Hero Section' with the message 'Good Job' for the asset 'asset_001'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_17",
        "instruction": "Assume the identity of 'emma.creative@company.com' and aim to request a review for your frame by generating a PNG 1x asset for that frame using the filename 'hero-section-2x-r2.png' within a Gmail thread addressed to 'jake.design@company.com', 'anna.brand@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "emma.creative@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 1x",
                    "file_size_bytes": 1000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-2x-r2.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_001",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-2x-r2.png",
                    "sender_id": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "anna.brand@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-2x-r2.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_18",
        "instruction": "Act as 'jake.design@company.com'. Your task is to give your approval on the ongoing review thread 'Design Review: Homepage Hero Section' by leaving the message 'Good Job' for the asset 'asset_001'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_19",
        "instruction": "You are 'jake.design@company.com'. Within the ongoing review thread 'Design Review: Homepage Hero Section', ask for alterations using the message 'please update the headline spacing and button contrast.' for the asset 'asset_001'. After receiving confirmation from the author that changes are made with the message 'adjusted headline spacing and increased primary button contrast', approve it with the message 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_20",
        "instruction": "You are 'jake.design@company.com' and you need to propose changes in the existing thread titled 'Navigation Bar Responsive Design' using the message 'please refine pricing table spacing and switch CTA to primary-600.' for the current artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_21",
        "instruction": "You are 'anna.brand@company.com' looking to submit a review request for your frame by exporting a PNG 2x asset with the filename 'pricing-page-2x-r2.png' within the Gmail thread directed to 'emma.creative@company.com', 'jake.design@company.com'",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/pricing-page-2x-r2.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: pricing-page-2x-r2.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the pricing-page-2x-r2.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_22",
        "instruction": "You are 'jake.design@company.com'. Coordinate the approval of the existing review thread 'Admin Panel Accessibility Audit' with the message 'Good Job, but done late' for asset 'asset_007'",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_23",
        "instruction": "You are 'jake.design@company.com' and must examine whether 'Admin Panel Accessibility Audit' has exceeded the SLA \u2014 initiate change requests within the current thread using the message 'SLA breached; please prioritize fixes and resubmit'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: SLA breached; please prioritize fixes and resubmit</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_004",
                    "escalated_ts": "2024-08-23T12:00:00Z"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_004",
                    "artifact_id": "art_008",
                    "thread_id_nullable": "thread_004",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-18T15:30:00Z",
                    "sla_deadline_ts": "2024-08-21T15:30:00Z",
                    "sla_breached_flag": true,
                    "escalated_ts_nullable": "2024-08-23T12:00:00Z"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_24",
        "instruction": "You are 'jake.design@company.com'. Disseminate release notes for 'Design System v1.3.0 - Form Components & Accessibility' in the current release thread, attach PNG 3x exports for the frames newly incorporated, and enumerate the modified frames from the release diff.",
        "actions": [
            {
                "name": "GetReleaseDetailsByName",
                "arguments": {
                    "release_name": "Design System v1.3.0 - Form Components & Accessibility"
                },
            },
            {
                "name": "GetReleaseDiffByReleaseId",
                "arguments": {
                    "release_id": "release_011"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:5",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:5.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:5.png"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_014",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:6.png"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:7",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:7.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_015",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:7.png"
                },
            },
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes"
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_013",
                    "body_html": "<h2>Design System v1.3.0 - Form Components & Accessibility</h2><p>Highlights:</p><ul><li>Added frame 1:5</li><li>Added frame 1:6</li><li>Added frame 1:7</li><li>Updated frame 1:3</li><li>Updated frame 1:4</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019",
                        "asset_020",
                        "asset_021"
                    ]
                }
            }
        ],
        "outputs": [
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
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_25",
        "instruction": "Identify as 'jake.design@company.com'. Initiate a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' using the tag 'mobile-app-v2.3.0' with the previous release id noted as release_012, including adding new frame '2:6' and updating frames '2:4' and '2:2'. Export the new PNG 2x frames to 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [
                        "2:4",
                        "2:2"
                    ],
                    "frames_removed": [],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Updated 2 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Updated frame 2:2,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_26",
        "instruction": "Recognize yourself as 'jake.design@company.com'. Develop a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' using the tag 'mobile-app-v2.3.0' with the prior release id as release_012, involving adding new frame '2:6' and removing frames '2:4'. Export the new PNG 2x frames to the recipients 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [],
                    "frames_removed": [
                        "2:4"
                    ],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Removed 1 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Removed frame 2:4,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_27",
        "instruction": "You are 'jake.design@company.com'. Handle the creation of a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with the tag 'mobile-app-v2.3.0', referencing the previous release id as release_012. Include the new frame '2:6', update frames '2:4', omit '2:2', and ensure the new PNG 2x frames are exported to 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [
                        "2:4"
                    ],
                    "frames_removed": [
                        "2:2"
                    ],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Updated 1 frames",
                        "Removed 1 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Removed frame 2:2,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_28",
        "instruction": "You are 'jake.design@company.com'. Coordinate within the existing review thread 'Design Review: Homepage Hero Section', requesting alterations with the message 'please update the headline spacing and button contrast.' for asset 'asset_001'. Once the author has confirmed the changes with the message 'adjusted headline spacing and increased primary button contrast', approve it by replying with 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_29",
        "instruction": "As 'jake.design@company.com', you seek to ask for modifications in the ongoing discussion with the subject 'Navigation Bar Responsive Design' and message 'please refine pricing table spacing and switch CTA to primary-600.' while maintaining the current artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_30",
        "instruction": "Act as 'jake.design@company.com', you have to approve the ongoing review thread 'Admin Panel Accessibility Audit' with the message 'Good Job, but done late' for the asset 'asset_007'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_31",
        "instruction": "You, 'anna.brand@company.com', intend to send a review request for your frame by exporting a PNG 3x asset for that frame with the filename 'hero-section-3x.png' using a Gmail thread sent to 'emma.creative@company.com' and 'jake.design@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-3x.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                },
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_32",
        "instruction": "You are 'jake.design@company.com'. You must authorize the current review thread 'Design Review: Homepage Hero Section' with the message 'Good Job' for the asset 'asset_001'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_33",
        "instruction": "As 'emma.creative@company.com', you need to create a review request for your frame by exporting a PNG 2x asset for that frame with the filename 'hero-section-2x-r2.png', and include it in a Gmail conversation addressed to 'jake.design@company.com', 'chris.engineer@company.com', 'anna.brand@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "emma.creative@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-2x-r2.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_001",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-2x-r2.png",
                    "sender_id": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-2x-r2.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_34",
        "instruction": "As 'jake.design@company.com', your task is to approve the existing review thread 'Design Review: Homepage Hero Section' with the message 'Good Job' for the asset 'asset_001'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_35",
        "instruction": "You are 'jake.design@company.com'. In the current review thread 'Design Review: Homepage Hero Section', request revisions with the message 'please update the headline spacing and button contrast.' concerning asset 'asset_001', and once the author acknowledges the modifications are done with the message 'adjusted headline spacing and increased primary button contrast', approve it by writing 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_36",
        "instruction": "You are 'jake.design@company.com' and need to seek amendments in the ongoing thread titled 'Navigation Bar Responsive Design' with the message 'please refine pricing table spacing and switch CTA to primary-600.' and for the present artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_37",
        "instruction": "As 'anna.brand@company.com', you aim to request a review for your frame by exporting a PNG 2x asset named 'pricing-page-2x-r2.png' in a Gmail thread addressed to 'emma.creative@company.com', 'jake.design@company.com'",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/pricing-page-2x-r2.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: pricing-page-2x-r2.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the pricing-page-2x-r2.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_38",
        "instruction": "Being 'jake.design@company.com', you are required to approve the existing review thread 'Admin Panel Accessibility Audit' with the message 'Good Job, but done late' for the asset 'asset_007'",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_39",
        "instruction": "You're using 'jake.design@company.com' and need to examine 'Admin Panel Accessibility Audit' because it's beyond SLA\u2014initiate a request for modifications in the current thread with the message 'SLA breached; please prioritize fixes and resubmit'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: SLA breached; please prioritize fixes and resubmit</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_004",
                    "escalated_ts": "2024-08-23T12:00:00Z"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_004",
                    "artifact_id": "art_008",
                    "thread_id_nullable": "thread_004",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-18T15:30:00Z",
                    "sla_deadline_ts": "2024-08-21T15:30:00Z",
                    "sla_breached_flag": true,
                    "escalated_ts_nullable": "2024-08-23T12:00:00Z"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_40",
        "instruction": "With 'jake.design@company.com', distribute release notes for 'Design System v1.3.0 - Form Components & Accessibility' within the ongoing release thread, incorporating PNG 3x exports for newly added frames, and enumerate the changed frames from the release diff.",
        "actions": [
            {
                "name": "GetReleaseDetailsByName",
                "arguments": {
                    "release_name": "Design System v1.3.0 - Form Components & Accessibility"
                },
            },
            {
                "name": "GetReleaseDiffByReleaseId",
                "arguments": {
                    "release_id": "release_011"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:5",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:5.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:5.png"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_014",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:6.png"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:7",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:7.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_015",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:7.png"
                },
            },
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes"
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_013",
                    "body_html": "<h2>Design System v1.3.0 - Form Components & Accessibility</h2><p>Highlights:</p><ul><li>Added frame 1:5</li><li>Added frame 1:6</li><li>Added frame 1:7</li><li>Updated frame 1:3</li><li>Updated frame 1:4</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019",
                        "asset_020",
                        "asset_021"
                    ]
                }
            }
        ],
        "outputs": [
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
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_41",
        "instruction": "Assume the role of 'jake.design@company.com'. Generate a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with the tag 'mobile-app-v2.3.0', referencing prior release ID release_012. This involves adding a new frame '2:6', updating frames '2:4' and '2:2', and exporting the new PNG 2x frames to 'stakeholders@company.com', 'product-managers@company.com', and 'engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [
                        "2:4",
                        "2:2"
                    ],
                    "frames_removed": [],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Updated 2 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Updated frame 2:2,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_42",
        "instruction": "Act as 'jake.design@company.com'. Develop a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' tagged as 'mobile-app-v2.3.0', using prior release id release_012. This requires adding a new frame '2:6', removing frames '2:4', and exporting the new PNG 2x frames to the addresses 'stakeholders@company.com', 'product-managers@company.com', and 'engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [],
                    "frames_removed": [
                        "2:4"
                    ],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Removed 1 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Removed frame 2:4,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_43",
        "instruction": "Assume the identity of 'jake.design@company.com'. Handle the creation of a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' using the tag 'mobile-app-v2.3.0' with the previous release id being release_012. Add the new frame '2:6', update the frames '2:4', remove '2:2', and export the new PNG 2x frames to the recipients 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [
                        "2:4"
                    ],
                    "frames_removed": [
                        "2:2"
                    ],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Updated 1 frames",
                        "Removed 1 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Removed frame 2:2,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_44",
        "instruction": "Act as 'jake.design@company.com'. Within the current review thread 'Design Review: Homepage Hero Section', request changes by sending the message 'please update the headline spacing and button contrast.' for asset 'asset_001'. Once the author confirms changes with the message 'adjusted headline spacing and increased primary button contrast', approve it with the message 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_45",
        "instruction": "Act as 'jake.design@company.com' to request modifications in the ongoing discussion titled 'Navigation Bar Responsive Design' with the message 'please refine pricing table spacing and switch CTA to primary-600.' while referring to the current artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_46",
        "instruction": "As 'jake.design@company.com', you are required to give the go-ahead for the existing review thread 'Admin Panel Accessibility Audit' with the message 'Good Job, but done late' in relation to asset 'asset_007'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_47",
        "instruction": "As 'anna.brand@company.com', your task is to submit a review request for your frame by exporting a PNG 3x asset for it, using the filename 'hero-section-3x.png', and share this in the Gmail thread with 'emma.creative@company.com' and 'jake.design@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-3x.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                },
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_48",
        "instruction": "Being 'jake.design@company.com', proceed to approve the existing review thread 'Design Review: Homepage Hero Section' by sending the message 'Good Job' for the asset 'asset_001'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_49",
        "instruction": "As 'emma.creative@company.com', initiate a review request for your frame by exporting a PNG 2x asset for that frame with filename 'hero-section-2x-r2.png' within the Gmail thread sent to 'jake.design@company.com', 'chris.engineer@company.com', 'anna.brand@company.com'",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "emma.creative@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-2x-r2.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_001",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-2x-r2.png",
                    "sender_id": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-2x-r2.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_50",
        "instruction": "Being 'jake.design@company.com', you should approve the existing review thread 'Design Review: Homepage Hero Section' with the message 'Good Job' for asset 'asset_001'",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_51",
        "instruction": "Identify yourself as 'jake.design@company.com'. In the ongoing review discussion 'Design Review: Homepage Hero Section', ask for modifications by messaging 'please update the headline spacing and button contrast.' regarding asset 'asset_001'. Once the author notifies you of the updates with 'adjusted headline spacing and increased primary button contrast', proceed to endorse it by replying 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_52",
        "instruction": "Act as 'jake.design@company.com' and aim to suggest alterations in the existing conversation titled 'Navigation Bar Responsive Design' using the message 'please refine pricing table spacing and switch CTA to primary-600.' with reference to the current artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_53",
        "instruction": "Identify yourself as 'anna.brand@company.com' and proceed to submit a review request concerning your frame by exporting a PNG 2x asset for that frame, naming it 'pricing-page-2x-r2.png', within the Gmail thread directed to 'emma.creative@company.com', 'jake.design@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/pricing-page-2x-r2.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: pricing-page-2x-r2.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the pricing-page-2x-r2.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_54",
        "instruction": "Act as 'jake.design@company.com' and you must authorize the current review thread 'Admin Panel Accessibility Audit' with the message 'Good Job, but done late' for the asset identified by 'asset_007'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_55",
        "instruction": "You are 'jake.design@company.com' and must assess that 'Admin Panel Accessibility Audit' is past SLA \u2014 request changes in the current thread with message 'SLA breached; please prioritize fixes and resubmit'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: SLA breached; please prioritize fixes and resubmit</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_004",
                    "escalated_ts": "2024-08-23T12:00:00Z"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_004",
                    "artifact_id": "art_008",
                    "thread_id_nullable": "thread_004",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-18T15:30:00Z",
                    "sla_deadline_ts": "2024-08-21T15:30:00Z",
                    "sla_breached_flag": true,
                    "escalated_ts_nullable": "2024-08-23T12:00:00Z"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_56",
        "instruction": "You are 'jake.design@company.com'. Issue release notes for 'Design System v1.3.0 - Form Components & Accessibility' to the ongoing release thread, including PNG 3x exports for newly added frames, and list the altered frames from the release diff.",
        "actions": [
            {
                "name": "GetReleaseDetailsByName",
                "arguments": {
                    "release_name": "Design System v1.3.0 - Form Components & Accessibility"
                },
            },
            {
                "name": "GetReleaseDiffByReleaseId",
                "arguments": {
                    "release_id": "release_011"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:5",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:5.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:5.png"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_014",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:6.png"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:7",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:7.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_015",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:7.png"
                },
            },
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes"
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_013",
                    "body_html": "<h2>Design System v1.3.0 - Form Components & Accessibility</h2><p>Highlights:</p><ul><li>Added frame 1:5</li><li>Added frame 1:6</li><li>Added frame 1:7</li><li>Updated frame 1:3</li><li>Updated frame 1:4</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019",
                        "asset_020",
                        "asset_021"
                    ]
                }
            }
        ],
        "outputs": [
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
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_57",
        "instruction": "Assume the identity of 'jake.design@company.com'. Develop a new App version labeled 'Mobile App v2.3.0 - Notifications & Settings Polish' using the tag 'mobile-app-v2.3.0', referencing the prior release id as release_012. Introduce the frame '2:6', refresh frames '2:4' and '2:2', and dispatch the freshly exported PNG 2x frames to 'stakeholders@company.com', 'product-managers@company.com', 'engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [
                        "2:4",
                        "2:2"
                    ],
                    "frames_removed": [],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Updated 2 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Updated frame 2:2,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_58",
        "instruction": "Assume the identity of 'jake.design@company.com'. Develop a new App version labeled 'Mobile App v2.3.0 - Notifications & Settings Polish' using the tag 'mobile-app-v2.3.0', referencing the prior release id as release_012. Introduce the frame '2:6', exclude frames '2:4', and dispatch the freshly exported PNG 2x frames to 'stakeholders@company.com', 'product-managers@company.com', 'engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [],
                    "frames_removed": [
                        "2:4"
                    ],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Removed 1 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Removed frame 2:4,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_59",
        "instruction": "You are 'jake.design@company.com'. Coordinate a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' with the tag 'mobile-app-v2.3.0', using the prior release id release_012. Add the new frame '2:6', update frames '2:4', remove '2:2', and export the new PNG 2x frames to 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [
                        "2:4"
                    ],
                    "frames_removed": [
                        "2:2"
                    ],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Updated 1 frames",
                        "Removed 1 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Removed frame 2:2,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_60",
        "instruction": "You are 'jake.design@company.com'. In the current review thread 'Design Review: Homepage Hero Section', request modifications with the message 'please update the headline spacing and button contrast.' for asset 'asset_001'. Once the author confirms the changes with the message 'adjusted headline spacing and increased primary button contrast', approve it with 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_61",
        "instruction": "You are 'jake.design@company.com'; you should request modifications in the ongoing thread with the subject 'Navigation Bar Responsive Design' using the message 'please refine pricing table spacing and switch CTA to primary-600.' and regarding the current artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_62",
        "instruction": "You are 'jake.design@company.com'. you must approve the existing review thread 'Admin Panel Accessibility Audit' with the message 'Good Job, but done late' for asset 'asset_007'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_63",
        "instruction": "As 'anna.brand@company.com', arrange to send a review request for your frame by generating a PNG 3x asset for that frame, naming it 'hero-section-3x.png', within the Gmail thread addressed to 'emma.creative@company.com' and 'jake.design@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-3x.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                },
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_64",
        "instruction": "As 'jake.design@company.com', organize the approval process for the existing review thread 'Design Review: Homepage Hero Section' and include the message 'Good Job' concerning asset 'asset_001'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_65",
        "instruction": "Act as 'emma.creative@company.com' and proceed to submit a review request regarding your frame by exporting a PNG 2x asset named 'hero-section-2x-r2.png'. This should be sent under a Gmail thread to 'jake.design@company.com', 'chris.engineer@company.com', 'anna.brand@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "emma.creative@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-2x-r2.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_001",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-2x-r2.png",
                    "sender_id": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-2x-r2.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_66",
        "instruction": "Assume the role of 'jake.design@company.com'. It is necessary for you to approve the current review thread 'Design Review: Homepage Hero Section' with the message 'Good Job' related to asset 'asset_001'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_67",
        "instruction": "Assume the identity of 'jake.design@company.com'. Within the review discussion 'Design Review: Homepage Hero Section', you should ask for modifications using the message 'please update the headline spacing and button contrast.' for asset 'asset_001'. Subsequently, upon the author confirming the modifications with the message 'adjusted headline spacing and increased primary button contrast', provide approval by saying 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_68",
        "instruction": "Act as 'jake.design@company.com' to solicit amendments in the ongoing thread titled 'Navigation Bar Responsive Design' utilizing the message 'please refine pricing table spacing and switch CTA to primary-600.' with the current artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_69",
        "instruction": "You, as 'anna.brand@company.com', intend to submit a review request for your frame by exporting a PNG 2x asset for that frame named 'pricing-page-2x-r2.png' in the Gmail thread addressed to 'emma.creative@company.com', 'jake.design@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/pricing-page-2x-r2.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: pricing-page-2x-r2.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the pricing-page-2x-r2.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_70",
        "instruction": "As 'jake.design@company.com', you must approve the existing review thread 'Admin Panel Accessibility Audit' with the message 'Good Job, but done late' for asset 'asset_007'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_71",
        "instruction": "Assume the role of 'jake.design@company.com' and review the 'Admin Panel Accessibility Audit' that is overdue according to the SLA \u2014 send a message in the current thread stating 'SLA breached; please prioritize fixes and resubmit'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: SLA breached; please prioritize fixes and resubmit</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_004",
                    "escalated_ts": "2024-08-23T12:00:00Z"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_004",
                    "artifact_id": "art_008",
                    "thread_id_nullable": "thread_004",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-18T15:30:00Z",
                    "sla_deadline_ts": "2024-08-21T15:30:00Z",
                    "sla_breached_flag": true,
                    "escalated_ts_nullable": "2024-08-23T12:00:00Z"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_72",
        "instruction": "Act as 'jake.design@company.com'. Distribute the release notes for 'Design System v1.3.0 - Form Components & Accessibility' in the existing release thread, ensuring to include PNG 3x exports for any newly added frames and enumerate the changed frames from the release diff.",
        "actions": [
            {
                "name": "GetReleaseDetailsByName",
                "arguments": {
                    "release_name": "Design System v1.3.0 - Form Components & Accessibility"
                },
            },
            {
                "name": "GetReleaseDiffByReleaseId",
                "arguments": {
                    "release_id": "release_011"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:5",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:5.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:5.png"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_014",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:6.png"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:7",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:7.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_015",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:7.png"
                },
            },
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes"
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_013",
                    "body_html": "<h2>Design System v1.3.0 - Form Components & Accessibility</h2><p>Highlights:</p><ul><li>Added frame 1:5</li><li>Added frame 1:6</li><li>Added frame 1:7</li><li>Updated frame 1:3</li><li>Updated frame 1:4</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019",
                        "asset_020",
                        "asset_021"
                    ]
                }
            }
        ],
        "outputs": [
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
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_73",
        "instruction": "Your email is 'jake.design@company.com'. Initiate a new App release titled 'Mobile App v2.3.0 - Notifications & Settings Polish', tagged with 'mobile-app-v2.3.0' and using release_012 as the prior release id. Include a new frame '2:6', update frames '2:4' and '2:2', and send the newly exported PNG 2x frames to 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [
                        "2:4",
                        "2:2"
                    ],
                    "frames_removed": [],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Updated 2 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Updated frame 2:2,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_74",
        "instruction": "Your email is 'jake.design@company.com'. Initiate a new App release titled 'Mobile App v2.3.0 - Notifications & Settings Polish', tagged with 'mobile-app-v2.3.0' and referencing release_012 as the previous release id. Add a new frame '2:6', remove frames '2:4', and send the newly exported PNG 2x frames to 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [],
                    "frames_removed": [
                        "2:4"
                    ],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Removed 1 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Removed frame 2:4,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_75",
        "instruction": "You are 'jake.design@company.com'. Initiate the creation of a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' using the tag 'mobile-app-v2.3.0', leveraging prior release id release_012. Include the addition of new frame '2:6', update frames '2:4', and eliminate '2:2'. Ensure exporting of new PNG 2x frames to the recipients 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [
                        "2:4"
                    ],
                    "frames_removed": [
                        "2:2"
                    ],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Updated 1 frames",
                        "Removed 1 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Removed frame 2:2,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_76",
        "instruction": "You are 'jake.design@company.com'. Within the review thread 'Design Review: Homepage Hero Section', request alterations with the message 'please update the headline spacing and button contrast.' for asset 'asset_001'. Once the author informs you that changes are made with the message 'adjusted headline spacing and increased primary button contrast', authorize it with the message 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_77",
        "instruction": "As 'jake.design@company.com', initiate a request for modifications in the existing conversation with the subject 'Navigation Bar Responsive Design', including the message 'please refine pricing table spacing and switch CTA to primary-600.' and the current artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_78",
        "instruction": "As 'jake.design@company.com', it's necessary to approve the current review thread 'Admin Panel Accessibility Audit' with the message 'Good Job, but done late' for asset 'asset_007'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_79",
        "instruction": "Acting as 'anna.brand@company.com', initiate a review request for your frame by exporting the asset as a PNG 3x with the filename 'hero-section-3x.png'. Send this under the Gmail thread addressed to 'emma.creative@company.com' and 'jake.design@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-3x.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                },
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_80",
        "instruction": "As 'jake.design@company.com', approve the existing review thread 'Design Review: Homepage Hero Section', including the message 'Good Job', for asset 'asset_001'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_81",
        "instruction": "As 'emma.creative@company.com', you should process a review request for your frame by exporting a PNG 2x asset named 'hero-section-2x-r2.png' within a Gmail thread directed to 'jake.design@company.com', 'chris.engineer@company.com', 'anna.brand@company.com'",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "emma.creative@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_001",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-2x-r2.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_001",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-2x-r2.png",
                    "sender_id": "emma.creative@company.com",
                    "recipients": [
                        "jake.design@company.com",
                        "chris.engineer@company.com",
                        "anna.brand@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-2x-r2.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_82",
        "instruction": "Being 'jake.design@company.com', you are required to approve the existing review thread titled 'Design Review: Homepage Hero Section' with the message 'Good Job' regarding asset 'asset_001'",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_83",
        "instruction": "Identify yourself as 'jake.design@company.com'. Within the ongoing discussion 'Design Review: Homepage Hero Section', request alterations by sending the message 'please update the headline spacing and button contrast.' regarding the asset 'asset_001'. Once the author responds confirming the changes with 'adjusted headline spacing and increased primary button contrast', give your approval using the message 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_84",
        "instruction": "Act as 'jake.design@company.com' and aim to ask for amendments in the current discussion titled 'Navigation Bar Responsive Design' by sending 'please refine pricing table spacing and switch CTA to primary-600.' related to the artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_85",
        "instruction": "You represent 'anna.brand@company.com' and aim to submit a review request for your frame by exporting a PNG 2x asset named 'pricing-page-2x-r2.png' within the Gmail thread sent to 'emma.creative@company.com', 'jake.design@company.com'",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/pricing-page-2x-r2.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: pricing-page-2x-r2.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the pricing-page-2x-r2.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_86",
        "instruction": "You are 'jake.design@company.com'. You are required to approve the existing review thread 'Admin Panel Accessibility Audit' with the message 'Good Job, but done late' for asset 'asset_007'",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_87",
        "instruction": "As 'jake.design@company.com', handle reviewing the 'Admin Panel Accessibility Audit' that is past SLA \u2014 initiate a request for changes in the current thread with the message 'SLA breached; please prioritize fixes and resubmit'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: SLA breached; please prioritize fixes and resubmit</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_004",
                    "escalated_ts": "2024-08-23T12:00:00Z"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_004",
                    "artifact_id": "art_008",
                    "thread_id_nullable": "thread_004",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-18T15:30:00Z",
                    "sla_deadline_ts": "2024-08-21T15:30:00Z",
                    "sla_breached_flag": true,
                    "escalated_ts_nullable": "2024-08-23T12:00:00Z"
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_88",
        "instruction": "Being 'jake.design@company.com', coordinate the publishing of release notes for 'Design System v1.3.0 - Form Components & Accessibility' in the existing release thread. Make sure to include PNG 3x exports for the newly added frames and enumerate the changed frames from the release diff.",
        "actions": [
            {
                "name": "GetReleaseDetailsByName",
                "arguments": {
                    "release_name": "Design System v1.3.0 - Form Components & Accessibility"
                },
            },
            {
                "name": "GetReleaseDiffByReleaseId",
                "arguments": {
                    "release_id": "release_011"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:5",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:5.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:5.png"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_014",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:6.png"
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "1:7",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abc123def456",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abc123def456_1:7.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_015",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abc123def456_1:7.png"
                },
            },
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design System v1.3.0 - Form Components & Accessibility - Release Notes"
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_013",
                    "body_html": "<h2>Design System v1.3.0 - Form Components & Accessibility</h2><p>Highlights:</p><ul><li>Added frame 1:5</li><li>Added frame 1:6</li><li>Added frame 1:7</li><li>Updated frame 1:3</li><li>Updated frame 1:4</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019",
                        "asset_020",
                        "asset_021"
                    ]
                }
            }
        ],
        "outputs": [
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
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_89",
        "instruction": "Assume the identity of 'jake.design@company.com'. Initiate a new App release 'Mobile App v2.3.0 - Notifications & Settings Polish' using the tag 'mobile-app-v2.3.0', with the previous release identified as release_012. Include a new frame '2:6', revise frames '2:4' and '2:2', and distribute the updated PNG 2x frames to 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [
                        "2:4",
                        "2:2"
                    ],
                    "frames_removed": [],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Updated 2 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Updated frame 2:2</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Updated frame 2:2,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_90",
        "instruction": "Operate as 'jake.design@company.com'. Develop a fresh App release 'Mobile App v2.3.0 - Notifications & Settings Polish' designated by tag 'mobile-app-v2.3.0' with earlier release id as release_012. Add a new frame '2:6', delete frames '2:4', and forward the new PNG 2x frames to 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [],
                    "frames_removed": [
                        "2:4"
                    ],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Removed 1 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Removed frame 2:4</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Removed frame 2:4,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_91",
        "instruction": "You are 'jake.design@company.com'. Handle a new App release titled 'Mobile App v2.3.0 - Notifications & Settings Polish' using the tag 'mobile-app-v2.3.0', with the previous release id as release_012. Include a new frame '2:6', update frames '2:4', remove '2:2', and export new PNG 2x frames to 'stakeholders@company.com','product-managers@company.com','engineering-leads@company.com'.",
        "actions": [
            {
                "name": "CreateNewRelease",
                "arguments": {
                    "figma_file_id": "figd_abcd1234",
                    "version_id": "v2.3.0",
                    "version_tag": "release/mobile-app-v2.3.0",
                    "release_name": "Mobile App v2.3.0 - Notifications & Settings Polish",
                    "owner_email": "jake.design@company.com"
                },
            },
            {
                "name": "CreateReleaseDiff",
                "arguments": {
                    "release_id": "release_013",
                    "prior_release_id": "release_012",
                    "frames_added": [
                        "2:6"
                    ],
                    "frames_updated": [
                        "2:4"
                    ],
                    "frames_removed": [
                        "2:2"
                    ],
                    "component_version_bumps": [
                        "App update"
                    ],
                    "changelog_highlights": [
                        "Added 1 frames",
                        "Updated 1 frames",
                        "Removed 1 frames"
                    ]
                },
            },
            {
                "name": "CreateNewArtifact",
                "arguments": {
                    "artifact_type": "FRAME",
                    "frame_id_nullable": "2:6",
                    "artifact_name": "Hero Section",
                    "figma_file_id": "figd_abcd1234",
                    "page_id": "1:2",
                    "owner_email": "jake.design@company.com",
                    "deep_link": "https://www.figma.com/file/figd_abcd1234_2:6.png",
                    "current_tags": [
                        "user",
                        "settings"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_013",
                    "export_profile": "PNG 2x",
                    "file_size_bytes": 2000,
                    "storage_ref": "gs://company-assets/figma-exports/figd_abcd1234_2:6.png"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                    "sender_id": "jake.design@company.com",
                    "recipients": [
                        "stakeholders@company.com",
                        "product-managers@company.com",
                        "engineering-leads@company.com"
                    ],
                    "current_labels": [
                        "Design/Release"
                    ],
                    "body_html": "<h2>Release Notes - Mobile App v2.3.0 - Notifications & Settings Polish</h2>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "NotifyStakeholders",
                "arguments": {
                    "thread_id": "thread_015",
                    "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                }
            }
        ],
        "outputs": [
                {
                    "thread": {
                        "thread_id": "thread_015",
                        "subject": "Mobile App v2.3.0 - Notifications & Settings Polish - Release Notes",
                        "sender_identity": "jake.design@company.com",
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
                        "sender_email": "jake.design@company.com",
                        "body_html": "<h2>Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes</h2><p>Highlights:</p><ul><li>Added frame 2:6</li><li>Updated frame 2:4</li><li>Removed frame 2:2</li></ul>",
                        "body_text_stripped": "Mobile App v2.3.0 - Notifications & Settings Polish — Release Notes Highlights: Added frame 2:6, Updated frame 2:4, Removed frame 2:2,",
                        "sent_ts": "2024-08-23T12:00:00Z",
                        "attachments_asset_ids": [
                            "asset_019"
                        ]
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_92",
        "instruction": "You are 'jake.design@company.com'. Within the existing review thread 'Design Review: Homepage Hero Section', request changes with the message 'please update the headline spacing and button contrast.' for asset 'asset_001'. After the author confirms the changes with the message 'adjusted headline spacing and increased primary button contrast', approve it using the message 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_93",
        "instruction": "You are 'jake.design@company.com' and need to request modifications in the ongoing thread with subject 'Navigation Bar Responsive Design' with message 'please refine pricing table spacing and switch CTA to primary-600.' and the current artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_94",
        "instruction": "You are 'jake.design@company.com'. you have to approve the current review thread 'Admin Panel Accessibility Audit' with message 'Good Job, but done late' for asset 'asset_007'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_95",
        "instruction": "As 'anna.brand@company.com', proceed to send a review request for your frame by exporting a PNG 3x asset for that frame, using the filename 'hero-section-3x.png', in a Gmail thread to 'emma.creative@company.com' and 'jake.design@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-3x.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                },
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_96",
        "instruction": "Representing 'jake.design@company.com', you should approve the current review thread 'Design Review: Homepage Hero Section' with the message 'Good Job' regarding asset 'asset_001'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_97",
        "instruction": "Assume the identity of 'jake.design@company.com'. In the ongoing review thread 'Design Review: Homepage Hero Section', you need to ask for changes by stating 'please update the headline spacing and button contrast.' regarding asset 'asset_001'. Then, upon receiving confirmation from the author with the message 'adjusted headline spacing and increased primary button contrast', approve it by responding with 'Good Job'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Design Review: Homepage Hero Section"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please update the headline spacing and button contrast.</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_001"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_001"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "emma.creative@company.com",
                    "body_html": "<p>Changes implemented: adjusted headline spacing and increased primary button contrast</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "emma.creative@company.com",
                    "content": "Changes implemented",
                    "source_message_id": "msg_018",
                    "resolved_flag": true
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_001",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job</p>",
                    "attachments_asset_ids": [
                        "asset_001"
                    ]
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_001",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_019",
                    "resolved_flag": true
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_001",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_021"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_001",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": false,
                        "approval_comment_ref_nullable": "comment_021"
                    },
                    "cycle": {
                        "cycle_id": "cycle_001",
                        "artifact_id": "art_001",
                        "thread_id_nullable": "thread_001",
                        "status": "APPROVED",
                        "created_ts": "2024-08-20T15:00:00Z",
                        "sla_deadline_ts": "2024-08-23T15:00:00Z",
                        "sla_breached_flag": false,
                        "escalated_ts_nullable": null
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_98",
        "instruction": "Assume the role of 'jake.design@company.com' and initiate change requests in the existing discussion titled 'Navigation Bar Responsive Design'. Your message should be 'please refine pricing table spacing and switch CTA to primary-600.' concerning the current artifact art_002.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Navigation Bar Responsive Design"
                },
            },
            {
                "name": "GetCompleteEmailThread",
                "arguments": {
                    "thread_id": "thread_010"
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "artifact_id": "art_002"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_010",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Requesting changes: please refine pricing table spacing and switch CTA to primary-600.</p>",
                    "attachments_asset_ids": []
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_002",
                    "author_email": "jake.design@company.com",
                    "content": "Requested changes",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_008",
                    "new_status": "CHANGES_REQUESTED",
                    "thread_id": "thread_010"
                }
            }
        ],
        "outputs": [
                {
                    "cycle_id": "cycle_008",
                    "artifact_id": "art_002",
                    "thread_id_nullable": "thread_010",
                    "status": "CHANGES_REQUESTED",
                    "created_ts": "2024-08-21T10:00:00Z",
                    "sla_deadline_ts": "2024-08-24T10:00:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_99",
        "instruction": "You are 'jake.design@company.com'. You need to give approval on the existing review thread 'Admin Panel Accessibility Audit' and include the message 'Good Job, but done late' for asset 'asset_007'.",
        "actions": [
            {
                "name": "GetThreadBySubject",
                "arguments": {
                    "subject": "Admin Panel Accessibility Audit"
                },
            },
            {
                "name": "SendEmailInThread",
                "arguments": {
                    "thread_id": "thread_004",
                    "sender_id": "jake.design@company.com",
                    "body_html": "<p>Approved: Good Job, but done late</p>",
                    "attachments_asset_ids": [
                        "asset_007"
                    ]
                },
            },
            {
                "name": "GetAssetById",
                "arguments": {
                    "asset_id": "asset_007"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_008",
                    "author_email": "jake.design@company.com",
                    "content": "Approved",
                    "source_message_id": "msg_017",
                    "resolved_flag": true
                },
            },
            {
                "name": "GetCycleByArtifactAndThread",
                "arguments": {
                    "thread_id": "thread_004"
                },
            },
            {
                "name": "ApproveReview",
                "arguments": {
                    "cycle_id": "cycle_004",
                    "approver_email": "jake.design@company.com",
                    "approval_comment_ref": "comment_019"
                }
            }
        ],
        "outputs": [
                {
                    "approval": {
                        "approval_id": "approval_012",
                        "cycle_id": "cycle_004",
                        "approver_email": "jake.design@company.com",
                        "approved_ts": "2024-08-23T12:00:00Z",
                        "sla_breached_flag": true,
                        "approval_comment_ref_nullable": "comment_019"
                    },
                    "cycle": {
                        "cycle_id": "cycle_004",
                        "artifact_id": "art_008",
                        "thread_id_nullable": "thread_004",
                        "status": "APPROVED",
                        "created_ts": "2024-08-18T15:30:00Z",
                        "sla_deadline_ts": "2024-08-21T15:30:00Z",
                        "sla_breached_flag": true,
                        "escalated_ts_nullable": "2024-08-21T16:00:00Z"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_100",
        "instruction": "You are 'anna.brand@company.com', and your task is to submit a review request for your frame by exporting a PNG 3x asset named 'hero-section-3x.png'. This should be included under a Gmail thread addressed to 'emma.creative@company.com' and 'jake.design@company.com'.",
        "actions": [
            {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "arguments": {
                    "artifact_type": "FRAME",
                    "owner_email": "anna.brand@company.com",
                    "tags": [
                        "needs-review"
                    ]
                },
            },
            {
                "name": "CreateNewAsset",
                "arguments": {
                    "artifact_id": "art_007",
                    "export_profile": "PNG 3x",
                    "file_size_bytes": 3000,
                    "storage_ref": "gs://company-assets/figma-exports/hero-section-3x.png"
                },
            },
            {
                "name": "CreateNewCycle",
                "arguments": {
                    "artifact_id": "art_007",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z"
                },
            },
            {
                "name": "StartEmailThread",
                "arguments": {
                    "subject": "Design Review: hero-section-3x.png",
                    "sender_id": "anna.brand@company.com",
                    "recipients": [
                        "emma.creative@company.com",
                        "jake.design@company.com"
                    ],
                    "current_labels": [
                        "Design/Needs-Review",
                        "figma",
                        "review"
                    ],
                    "body_html": "<p>Review for the hero-section-3x.png. See attachment.</p>",
                    "attachments_asset_ids": [
                        "asset_019"
                    ]
                },
            },
            {
                "name": "UpdateCycleStatus",
                "arguments": {
                    "cycle_id": "cycle_013",
                    "new_status": "NEEDS_REVIEW",
                    "thread_id": "thread_015"
                },
            },
            {
                "name": "AddComment",
                "arguments": {
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id": "msg_017",
                    "resolved_flag": false
                }
            }
        ],
        "outputs": [
                {
                    "comment_id": "comment_019",
                    "artifact_id": "art_007",
                    "author_email": "anna.brand@company.com",
                    "content": "Submitted for review",
                    "source_message_id_nullable": "msg_017",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "resolved_flag": false
                },
                {
                    "cycle_id": "cycle_013",
                    "artifact_id": "art_007",
                    "thread_id_nullable": "thread_015",
                    "status": "NEEDS_REVIEW",
                    "created_ts": "2024-08-23T12:00:00Z",
                    "sla_deadline_ts": "2024-08-28T12:30:00Z",
                    "sla_breached_flag": false,
                    "escalated_ts_nullable": null
                }
        ]
    }
]
