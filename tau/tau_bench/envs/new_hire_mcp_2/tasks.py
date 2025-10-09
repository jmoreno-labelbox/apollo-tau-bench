
tasks = [
    {
        "annotator": v2,
        "user_id": "032",
        "instruction": "Notify it assets regarding asset provisioning for cand_7 (Raj Patel) and ensure the request record remains consistent. Maintain /onboarding/robert_singh/asset_request.json including {'candidate':'cand_7','asset_type':'Laptop','requested_ts':'2024-08-06T14:20:00Z'}. Send msg_assets_robert_v2 to ['it-assets@company.com'] with subject 'asset provisioning - Raj Patel' and body 'see attached', labeled as label_1, link the email under thread_assets_robert_v2, and mark asset_req_5 as Sent with email_message_id msg_assets_robert_v2. Add a concise terminal note.",
        "actions": [
            {
                "name": "UpsertJsonArtifact",
                "arguments": {
                    "file_path": "/onboarding/robert_singh/asset_request.json",
                    "content_obj": {
                        "candidate": "cand_7",
                        "asset_type": "Laptop",
                        "requested_ts": "2024-08-06T14:20:00Z"
                    },
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_assets_robert_v2",
                    "subject": "asset provisioning - Raj Patel",
                    "body": "see attached",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_assets_robert_v2",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_assets_robert_v2",
                    "fields": {
                        "thread_id_nullable": "thread_assets_robert_v2"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "asset_req_5",
                    "fields": {
                        "status": "Sent",
                        "email_message_id_nullable": "msg_assets_robert_v2"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "sent asset provisioning notice for cand_7 with asset_req_5"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "071",
        "instruction": "Finalize a welcome confirmation for cand_4 (Sofia Martinez) with a labeled email and associated attachments. Save /onboarding/maria_rodriguez/welcome_confirm.md as text/markdown with '# welcome confirmed see details inside '. Send msg_welcome_confirm_maria to sofia.martinez@example.com with subject 'welcome confirmation - Sofia Martinez' and body 'welcome confirmed', label as label_6, attach welcome_confirm.md and the PDFs Company-Policies.pdf and Benefits-Guide.pdf from /onboarding/maria_rodriguez/, and link thread_welcome_confirm_maria.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/maria_rodriguez/welcome_confirm.md",
                    "content_text": "# welcome confirmed\nsee details inside\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_welcome_confirm_maria",
                    "subject": "welcome confirmation - Sofia Martinez",
                    "body": "welcome confirmed",
                    "to_emails": [
                        "sofia.martinez@example.com"
                    ],
                    "candidate_id": "cand_4",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_welcome_confirm_maria",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_welcome_confirm_maria",
                    "message_id": "msg_welcome_confirm_maria",
                    "filename": "welcome_confirm.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/maria_rodriguez/welcome_confirm.md"
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_maria_policies_pdf",
                    "message_id": "msg_welcome_confirm_maria",
                    "filename": "Company-Policies.pdf",
                    "mime_type": "application/pdf",
                    "file_path": "/onboarding/maria_rodriguez/Company-Policies.pdf"
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_maria_benefits_pdf",
                    "message_id": "msg_welcome_confirm_maria",
                    "filename": "Benefits-Guide.pdf",
                    "mime_type": "application/pdf",
                    "file_path": "/onboarding/maria_rodriguez/Benefits-Guide.pdf"
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_welcome_confirm_maria",
                    "fields": {
                        "thread_id_nullable": "thread_welcome_confirm_maria"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "060",
        "instruction": "Handle the resending of the policy pack for cand_1 (Michael Anderson). Create /onboarding/john_doe/policy_pack_v2.md as text/markdown with '# policy pack v2\n', then dispatch msg_policy_pack_resend_john to michael.anderson@example.com with the subject 'policy pack (resend) - Michael Anderson' and message 'see updated pack'. Use label_6 and ensure the file is attached.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/john_doe/policy_pack_v2.md",
                    "content_text": "# policy pack v2\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_policy_pack_resend_john",
                    "subject": "policy pack (resend) - Michael Anderson",
                    "body": "see updated pack",
                    "to_emails": [
                        "michael.anderson@example.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_policy_pack_resend_john",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_policy_pack_resend_john",
                    "message_id": "msg_policy_pack_resend_john",
                    "filename": "policy_pack_v2.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/john_doe/policy_pack_v2.md"
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "send_policy_pack_resend",
                    "params_json": {
                        "message_id": "msg_policy_pack_resend_john"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "056",
        "instruction": "You verify the desk setup for cand_5 (Jordan Williams). The final state must include: an email record sent - msg_desk_setup_alex to it-assets@company.com, the subject being 'desk setup - Jordan Williams', and the content 'monitor and dock confirmed', marked as label_1 and linked with thread_desk_setup_alex; a terminal log containing 'desk setup confirmed for cand_5 with peripherals'; checklist item item_11 updated to 'Completed' with a timestamp of 2025-01-01T09:00:00Z; and an audit entry that includes a reference to msg_desk_setup_alex.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_desk_setup_alex",
                    "subject": "desk setup - Jordan Williams",
                    "body": "monitor and dock confirmed",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_5",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_desk_setup_alex",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_desk_setup_alex",
                    "fields": {
                        "thread_id_nullable": "thread_desk_setup_alex"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "desk setup confirmed for cand_5 with peripherals"
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_11",
                    "fields": {
                        "status": "Completed",
                        "updated_ts": "2025-01-01T09:00:00Z"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "notify_desk_setup",
                    "params_json": {
                        "message_id": "msg_desk_setup_alex"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "048",
        "instruction": "Handle the manager-intro confirmation for cand_1 (Michael Anderson). Supply parameters: note_path=/onboarding/john_doe/manager_intro_note.md, note_mime=text/markdown, note_content='intro prepared', message_id=msg_manager_intro_john_2, subject='manager intro - Michael Anderson', body='intro sent', to_emails=['michael.anderson@example.com'], label_id=label_5, attach_id=attach_manager_intro_note_john_2, attach_filename=manager_intro_note.md, attach_mime=text/markdown, thread_id=thread_manager_intro_john_2, audit={'server_name':'gmail','tool_name':'send_manager_intro_john','params_json':{'message_id':'msg_manager_intro_john_2'}}.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/john_doe/manager_intro_note.md",
                    "content_text": "intro prepared\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_manager_intro_john_2",
                    "subject": "manager intro - Michael Anderson",
                    "body": "intro sent",
                    "to_emails": [
                        "michael.anderson@example.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_manager_intro_john_2",
                    "label_ids": [
                        "label_5"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_manager_intro_note_john_2",
                    "message_id": "msg_manager_intro_john_2",
                    "filename": "manager_intro_note.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/john_doe/manager_intro_note.md"
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_manager_intro_john_2",
                    "fields": {
                        "thread_id_nullable": "thread_manager_intro_john_2"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "send_manager_intro_john",
                    "params_json": {
                        "message_id": "msg_manager_intro_john_2"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "013",
        "instruction": "Verify access clearance for cand_4 (Sofia Martinez). The final state should capture successes logged for Email, SSO, and Slack; an existing markdown file at /onboarding/maria_rodriguez/access_clearance.md with the exact content 'email: success\nsso: success\nslack: success\n'; an email sent record msg_access_clear_maria to daniel.lee@example.com with subject 'access clearance - Sofia Martinez' and body 'all critical systems ready', tagged with label_3 and including the access_clearance.md attachment from that location.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_4",
                    "system_name": "Email",
                    "status": "Success"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_4",
                    "system_name": "SSO",
                    "status": "Success"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_4",
                    "system_name": "Slack",
                    "status": "Success"
                },
            },
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/maria_rodriguez/access_clearance.md",
                    "content_text": "email: success\nsso: success\nslack: success\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_access_clear_maria",
                    "subject": "access clearance - Sofia Martinez",
                    "body": "all critical systems ready",
                    "to_emails": [
                        "daniel.lee@example.com"
                    ],
                    "candidate_id": "cand_4",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_access_clear_maria",
                    "label_ids": [
                        "label_3"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_0020",
                    "message_id": "msg_access_clear_maria",
                    "filename": "access_clearance.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/maria_rodriguez/access_clearance.md"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "047",
        "instruction": "Coordinate the orientation-finalization protocol for cand_5 (Jordan Williams). Supply parameters: agenda_path=/onboarding/alex_thompson/orientation_agenda_2.md, agenda_mime=text/markdown, agenda_content='# orientation agenda\nwelcome and access\n', message_id=msg_orientation_alex_2, subject='day-1 orientation - Jordan Williams', body='agenda attached', to_emails=['jordan.williams@example.com'], label_id=label_4, attach_id=attach_orientation_agenda_alex_2, attach_filename=orientation_agenda_2.md, attach_mime=text/markdown, thread_id=thread_orientation_alex_2, audit={'server_name':'gmail','tool_name':'send_orientation_alex','params_json':{'message_id':'msg_orientation_alex_2'}}.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/alex_thompson/orientation_agenda_2.md",
                    "content_text": "# orientation agenda\nwelcome and access\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_orientation_alex_2",
                    "subject": "day-1 orientation - Jordan Williams",
                    "body": "agenda attached",
                    "to_emails": [
                        "jordan.williams@example.com"
                    ],
                    "candidate_id": "cand_5",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_orientation_alex_2",
                    "label_ids": [
                        "label_4"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_orientation_agenda_alex_2",
                    "message_id": "msg_orientation_alex_2",
                    "filename": "orientation_agenda_2.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/alex_thompson/orientation_agenda_2.md"
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_orientation_alex_2",
                    "fields": {
                        "thread_id_nullable": "thread_orientation_alex_2"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "send_orientation_alex",
                    "params_json": {
                        "message_id": "msg_orientation_alex_2"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "020",
        "instruction": "Handle the access-gap notification protocol for cand_7 (Raj Patel) concerning vpn. Include parameters: check=('VPN','Pending','pending account provisioning'); gap_path=/onboarding/robert_singh/vpn_gap.md, gap_mime=text/markdown, gap_content='vpn: pending - pending account provisioning'; notify_email={message_id:msg_vpn_gap_robert, to:['it-support@company.com'], subject:'Access Gap - VPN - Raj Patel', body:'see attached', label_id:label_3, thread_id:thread_vpn_gap_robert}; attach_filename=vpn_gap.md; audit={'server_name':'gmail','tool_name':'notify_vpn_gap_robert','params_json':{'message_id':'msg_vpn_gap_robert'}}.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_7",
                    "system_name": "VPN",
                    "status": "Pending",
                    "note_nullable": "pending account provisioning"
                },
            },
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/robert_singh/vpn_gap.md",
                    "content_text": "vpn: pending - pending account provisioning",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_vpn_gap_robert",
                    "subject": "Access Gap - VPN - Raj Patel",
                    "body": "see attached",
                    "to_emails": [
                        "it-support@company.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_vpn_gap_robert",
                    "label_ids": [
                        "label_3"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_vpn_gap_robert",
                    "message_id": "msg_vpn_gap_robert",
                    "filename": "vpn_gap.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/robert_singh/vpn_gap.md"
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_vpn_gap_robert",
                    "fields": {
                        "thread_id_nullable": "thread_vpn_gap_robert"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "notify_vpn_gap_robert",
                    "params_json": {
                        "message_id": "msg_vpn_gap_robert"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "009",
        "instruction": "Handle cand_6 (Lily Zhang) for orientation: log email/sso/slack as success and marketing platform as pending with a note 'pending vendor activation'; compose /onboarding/emily_chen/orientation_agenda.md as text/markdown with '# orientation agenda\nwelcome and access\n'; dispatch a labeled invite (msg_orientation_emily) to ['lily.zhang@example.com'] with subject 'day-1 orientation - Lily Zhang' and body 'agenda attached', including that agenda as an attachment; set orientation_invite_ts to 2024-08-23T09:30:00Z.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_6",
                    "system_name": "Email",
                    "status": "Success"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_6",
                    "system_name": "SSO",
                    "status": "Success"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_6",
                    "system_name": "Slack",
                    "status": "Success"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_6",
                    "system_name": "Marketing Platform",
                    "status": "Pending",
                    "note_nullable": "pending vendor activation"
                },
            },
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/emily_chen/orientation_agenda.md",
                    "content_text": "# orientation agenda\nwelcome and access\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_orientation_emily",
                    "subject": "day-1 orientation - Lily Zhang",
                    "body": "agenda attached",
                    "to_emails": [
                        "lily.zhang@example.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_orientation_emily",
                    "label_ids": [
                        "label_4"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_0022",
                    "message_id": "msg_orientation_emily",
                    "filename": "orientation_agenda.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/emily_chen/orientation_agenda.md"
                },
            },
            {
                "name": "SetCandidateFields",
                "arguments": {
                    "candidate_id": "cand_6",
                    "fields": {
                        "orientation_invite_ts_nullable": "2024-08-23T09:30:00Z"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "030",
        "instruction": "Coordinate the monitor allocation protocol for cand_7 (Raj Patel). Provide parameters: asset_tag=MON-DELL-002, message_id=msg_monitor_alloc_robert, subject='monitor allocation - Raj Patel', body='monitor assigned', to_emails=['it-assets@company.com'], label_name='Asset-Request', label_id='label_1', thread_id=thread_monitor_alloc_robert.",
        "actions": [
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "MON-DELL-002",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "CreateOrGetEmailLabel",
                "arguments": {
                    "name": "Asset-Request"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_monitor_alloc_robert",
                    "subject": "monitor allocation - Raj Patel",
                    "body": "monitor assigned",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_monitor_alloc_robert",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_monitor_alloc_robert",
                    "fields": {
                        "thread_id_nullable": "thread_monitor_alloc_robert"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "allocated MON-DELL-002 to cand_7"
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "notify_monitor_alloc",
                    "params_json": {
                        "message_id": "msg_monitor_alloc_robert"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "031",
        "instruction": "Handle the welcome-packet protocol initiation for cand_6 (Lily Zhang). Deliver these parameters: welcome_md_path=/onboarding/emily_chen/welcome_emily_chen.md, welcome_md_mime=text/markdown, welcome_md_content='# welcome emily\nstart date: 2024-08-23\n', welcome_email={message_id:msg_welcome_emily, to:['lily.zhang@example.com'], subject:'welcome to the team - Lily Zhang', body:'welcome!', label_id:label_6}, thread_id=thread_welcome_emily, candidate_update={onboarding_status:'Packet Sent', welcome_email_message_id_nullable:'msg_welcome_emily'}.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/emily_chen/welcome_emily_chen.md",
                    "content_text": "# welcome emily\nstart date: 2024-08-23\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_welcome_emily",
                    "subject": "welcome to the team - Lily Zhang",
                    "body": "welcome!",
                    "to_emails": [
                        "lily.zhang@example.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_welcome_emily",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "SetCandidateFields",
                "arguments": {
                    "candidate_id": "cand_6",
                    "fields": {
                        "onboarding_status": "Packet Sent",
                        "welcome_email_message_id_nullable": "msg_welcome_emily"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_welcome_emily",
                    "fields": {
                        "thread_id_nullable": "thread_welcome_emily"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "024",
        "instruction": "Coordinate the access-gap notification protocol trigger for cand_2 (Emma Thompson) concerning vpn onboarding. Include parameters: checks=[('VPN','Pending','awaiting network group')], summary_path=/onboarding/jane_smith/vpn_gap.md, summary_mime=text/markdown, summary_lines=['VPN: Pending - awaiting network group'], message_id=msg_vpn_gap_jane, subject='access gap - Emma Thompson', body='see vpn details', to_emails=['it-support@company.com'], label_name='Access-Issues', label_id='label_3', attach_id=attach_vpn_gap_jane, attach_filename=vpn_gap.md, attach_mime=text/markdown, thread_id=thread_vpn_gap_jane.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_2",
                    "system_name": "VPN",
                    "status": "Pending",
                    "note_nullable": "awaiting network group"
                },
            },
            {
                "name": "CreateAccessGapSummaryFile",
                "arguments": {
                    "file_path": "/onboarding/jane_smith/vpn_gap.md",
                    "content_lines": [
                        "VPN: Pending - awaiting network group"
                    ],
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "CreateOrGetEmailLabel",
                "arguments": {
                    "name": "Access-Issues"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_vpn_gap_jane",
                    "subject": "access gap - Emma Thompson",
                    "body": "see vpn details",
                    "to_emails": [
                        "it-support@company.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_vpn_gap_jane",
                    "label_ids": [
                        "label_3"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_vpn_gap_jane",
                    "message_id": "msg_vpn_gap_jane",
                    "filename": "vpn_gap.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/jane_smith/vpn_gap.md"
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_vpn_gap_jane",
                    "fields": {
                        "thread_id_nullable": "thread_vpn_gap_jane"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "101",
        "instruction": "Handle sending a concise checklist reminder for cand_2 (Emma Thompson). Generate /onboarding/jane_smith/pending_tasks_101.md as text/markdown with '- benefits enrollment\n- security training\n'. Dispatch msg_reminder_jane_101 to emma.thompson@example.com with subject 'pending tasks - Emma Thompson' and body 'please complete', apply label_id=label_2, and revise item_5 and item_6 to 'Reminder Sent' with reference to msg_reminder_jane_101.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/jane_smith/pending_tasks_101.md",
                    "content_text": "- benefits enrollment\n- security training\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_reminder_jane_101",
                    "subject": "pending tasks - Emma Thompson",
                    "body": "please complete",
                    "to_emails": [
                        "emma.thompson@example.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_reminder_jane_101",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_5",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_email_message_id_nullable": "msg_reminder_jane_101"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_6",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_email_message_id_nullable": "msg_reminder_jane_101"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "008",
        "instruction": "Coordinate a laptop exchange for cand_2 (Emma Thompson) from LT-DELL-003 to LT-MBP-002 and inform it-assets. Conclude with: LT-DELL-003 is released; LT-MBP-002 is assigned to cand_2; asset_req_1 indicates asset_tag_nullable 'LT-MBP-002'; a terminal note contains the message precisely 'swap cand_2 LT-DELL-003->LT-MBP-002'; a dispatched email record msg_asset_swap_jane is sent to ['it-assets@company.com'] with subject 'Asset Swap - Emma Thompson' and body 'Dell to MBP', tagged with label_1; an MCP audit entry is present with server_name 'gmail', tool_name 'asset_swap_notice_jane', and params_json {'message_id':'msg_asset_swap_jane'}.",
        "actions": [
            {
                "name": "ReleaseInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-003"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-002",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "asset_req_1",
                    "fields": {
                        "asset_tag_nullable": "LT-MBP-002"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "swap cand_2 LT-DELL-003->LT-MBP-002"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_asset_swap_jane",
                    "subject": "Asset Swap - Emma Thompson",
                    "body": "Dell to MBP",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_asset_swap_jane",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "asset_swap_notice_jane",
                    "params_json": {
                        "message_id": "msg_asset_swap_jane"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "041",
        "instruction": "Handle the welcome confirmation for cand_1 (Michael Anderson). Final state: a note is present at /onboarding/john_doe/welcome_confirm.md containing exactly '# welcome confirmed see details inside '; an email record msg_welcome_confirm_john has been sent to michael.anderson@example.com with subject 'welcome confirmation - Michael Anderson' and body 'welcome confirmed', marked with label_6 and linked with thread_welcome_confirm_john; the email incorporates attachment welcome_confirm.md derived from that note; an MCP audit entry is recorded with server_name 'gmail', tool_name 'send_welcome_confirm_john', and params_json {'message_id':'msg_welcome_confirm_john'}.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/john_doe/welcome_confirm.md",
                    "content_text": "# welcome confirmed\nsee details inside\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_welcome_confirm_john",
                    "subject": "welcome confirmation - Michael Anderson",
                    "body": "welcome confirmed",
                    "to_emails": [
                        "michael.anderson@example.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_welcome_confirm_john",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_welcome_confirm_john",
                    "message_id": "msg_welcome_confirm_john",
                    "filename": "welcome_confirm.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/john_doe/welcome_confirm.md"
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_welcome_confirm_john",
                    "fields": {
                        "thread_id_nullable": "thread_welcome_confirm_john"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "send_welcome_confirm_john",
                    "params_json": {
                        "message_id": "msg_welcome_confirm_john"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "042",
        "instruction": "Coordinate the asset-provisioning handoff for cand_7 (Raj Patel). Final state: /onboarding/robert_singh/asset_request.json contains {'candidate':'cand_7','asset_type':'Laptop','requested_ts':'2024-08-06T14:20:00Z'}; an email record msg_assets_handoff_robert has been dispatched to it-assets@company.com with subject 'asset provisioning handoff - Raj Patel' and body 'handoff sent', marked with label_1 and linked with thread_assets_handoff_robert; asset_req_5 indicates status 'Sent' and mentions msg_assets_handoff_robert; an audit entry has been created that cites msg_assets_handoff_robert.",
        "actions": [
            {
                "name": "UpsertJsonArtifact",
                "arguments": {
                    "file_path": "/onboarding/robert_singh/asset_request.json",
                    "content_obj": {
                        "candidate": "cand_7",
                        "asset_type": "Laptop",
                        "requested_ts": "2024-08-06T14:20:00Z"
                    },
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_assets_handoff_robert",
                    "subject": "asset provisioning handoff - Raj Patel",
                    "body": "handoff sent",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_assets_handoff_robert",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "asset_req_5",
                    "fields": {
                        "status": "Sent",
                        "email_message_id_nullable": "msg_assets_handoff_robert"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_assets_handoff_robert",
                    "fields": {
                        "thread_id_nullable": "thread_assets_handoff_robert"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "asset_provision_handoff",
                    "params_json": {
                        "message_id": "msg_assets_handoff_robert"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "043",
        "instruction": "Initiate the access-gap alert protocol for cand_4 (Sofia Martinez). Ensure you include parameters: checks=[('Email','Failed','exchange outage'),('SSO','Failed','idp sync pending')], summary_path=/onboarding/maria_rodriguez/access_gaps_2.md, summary_mime=text/markdown, summary_lines=['Email: Failed - exchange outage','SSO: Failed - idp sync pending'], message_id=msg_access_gap_maria_2, subject='access issues - Sofia Martinez', body='see details', to_emails=['it-support@company.com'], label_id=label_3, attach_id=attach_access_gap_maria_2, attach_filename=access_gaps_2.md, attach_mime=text/markdown.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_4",
                    "system_name": "Email",
                    "status": "Failed",
                    "note_nullable": "exchange outage"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_4",
                    "system_name": "SSO",
                    "status": "Failed",
                    "note_nullable": "idp sync pending"
                },
            },
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/maria_rodriguez/access_gaps_2.md",
                    "content_text": "Email: Failed - exchange outage\nSSO: Failed - idp sync pending\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_access_gap_maria_2",
                    "subject": "access issues - Sofia Martinez",
                    "body": "see details",
                    "to_emails": [
                        "it-support@company.com"
                    ],
                    "candidate_id": "cand_4",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_access_gap_maria_2",
                    "label_ids": [
                        "label_3"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_access_gap_maria_2",
                    "message_id": "msg_access_gap_maria_2",
                    "filename": "access_gaps_2.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/maria_rodriguez/access_gaps_2.md"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "027",
        "instruction": "Coordinate the welcome confirmation for cand_6 (Lily Zhang). Construct /onboarding/emily_chen/welcome_emily_confirm.md as text/markdown containing '# welcome confirmed\nsee details inside\n' and transmit msg_welcome_confirm_emily to lily.zhang@example.com with subject 'welcome confirmation - Lily Zhang' and body 'welcome confirmed', applying label_6 and attaching that file.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/emily_chen/welcome_emily_confirm.md",
                    "content_text": "# welcome confirmed\nsee details inside\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_welcome_confirm_emily",
                    "subject": "welcome confirmation - Lily Zhang",
                    "body": "welcome confirmed",
                    "to_emails": [
                        "lily.zhang@example.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_welcome_confirm_emily",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_welcome_confirm_emily",
                    "message_id": "msg_welcome_confirm_emily",
                    "filename": "welcome_emily_confirm.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/emily_chen/welcome_emily_confirm.md"
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "send_welcome_confirm",
                    "params_json": {
                        "message_id": "msg_welcome_confirm_emily"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "104",
        "instruction": "Handle the delivery of a policy acknowledgment reminder for cand_1 (Michael Anderson) and revise the associated checklist items. Dispatch msg_policy_nudge_john_104 to michael.anderson@example.com with subject 'policy ack - Michael Anderson' and body 'please review and ack', apply label_id=label_6, and amend item_1 and item_2 to 'Reminder Sent' by making reference to msg_policy_nudge_john_104.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_policy_nudge_john_104",
                    "subject": "policy ack - Michael Anderson",
                    "body": "please review and ack",
                    "to_emails": [
                        "michael.anderson@example.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_policy_nudge_john_104",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_1",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_email_message_id_nullable": "msg_policy_nudge_john_104"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_2",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_email_message_id_nullable": "msg_policy_nudge_john_104"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "105",
        "instruction": "Coordinate the re-sending of the orientation invitation for cand_7 (Raj Patel). Generate /onboarding/robert_singh/orientation_agenda_105.md as text/markdown containing '# orientation agenda\nresend copy\n'. Send msg_orientation_robert_105 to raj.patel@example.com with subject 'day-1 orientation (resend) - Raj Patel' and body 'agenda attached', apply label_id=label_4.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/robert_singh/orientation_agenda_105.md",
                    "content_text": "# orientation agenda\nresend copy\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_orientation_robert_105",
                    "subject": "day-1 orientation (resend) - Raj Patel",
                    "body": "agenda attached",
                    "to_emails": [
                        "raj.patel@example.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_orientation_robert_105",
                    "label_ids": [
                        "label_4"
                    ]
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "001",
        "instruction": "Handle the completion of the welcome packet for cand_1 (Michael Anderson). Coordinate the creation of /onboarding/john_doe/welcome_john_doe.md in text/markdown format including exactly '# Welcome John\nStart date: 2024-08-01\n'. Dispatch an email labeled welcome (message_id=msg_welcome_john, subject 'welcome to the team - Michael Anderson', body 'dear john, welcome!', to ['michael.anderson@example.com'], label_6) and retain it in thread_welcome_john. Attach the previously crafted markdown file and update cand_1 onboarding_status to 'Packet Sent' using welcome_email_message_id msg_welcome_john.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/john_doe/welcome_john_doe.md",
                    "content_text": "# Welcome John\nStart date: 2024-08-01\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_welcome_john",
                    "subject": "welcome to the team - Michael Anderson",
                    "body": "dear john, welcome!",
                    "to_emails": [
                        "michael.anderson@example.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_welcome_john",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_0019",
                    "message_id": "msg_welcome_john",
                    "filename": "welcome_john_doe.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/john_doe/welcome_john_doe.md"
                },
            },
            {
                "name": "SetCandidateFields",
                "arguments": {
                    "candidate_id": "cand_1",
                    "fields": {
                        "onboarding_status": "Packet Sent",
                        "welcome_email_message_id_nullable": "msg_welcome_john"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_welcome_john",
                    "fields": {
                        "thread_id_nullable": "thread_welcome_john"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "002",
        "instruction": "Conclude the asset provisioning outcome for cand_7 (Raj Patel) by employing the Assets-Provisioning protocol. Ensure the final state encompasses: asset_req_5 marked with status 'Sent' and email_message_id_nullable 'msg_assets_robert'; an email dispatch record with message_id msg_assets_robert to ['it-assets@company.com'], subject 'Asset Provisioning Request - Raj Patel', body 'See attached', and labeled Asset-Request with label_id label_1; a JSON artifact stored at /onboarding/robert_singh/asset_request.json containing {'candidate':'cand_7','asset_type':'Laptop','requested_ts':'2024-08-06T14:20:00Z'}; candidate cand_7 associated with asset_req_5; inventory item LT-MBP-001 allocated to cand_7; and an MCP audit on record with server_name gmail, tool_name asset_provision, params_json {'message_id':'msg_assets_robert'}.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "asset_req_5",
                    "fields": {
                        "status": "Sent",
                        "email_message_id_nullable": "msg_assets_robert"
                    }
                },
            },
            {
                "name": "CreateOrGetEmailLabel",
                "arguments": {
                    "name": "Asset-Request"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_assets_robert",
                    "subject": "Asset Provisioning Request - Raj Patel",
                    "body": "See attached",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_assets_robert",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpsertJsonArtifact",
                "arguments": {
                    "file_path": "/onboarding/robert_singh/asset_request.json",
                    "content_obj": {
                        "candidate": "cand_7",
                        "asset_type": "Laptop",
                        "requested_ts": "2024-08-06T14:20:00Z"
                    },
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "LinkAssetRequestToCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "request_id": "asset_req_5"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-001",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "asset_provision",
                    "params_json": {
                        "message_id": "msg_assets_robert"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "003",
        "instruction": "Address the access gaps for cand_4 (Sofia Martinez). Record: email failed 'exchange server issue', sso failed 'idp sync pending', slack failed 'depends on sso', github pending 'waiting for sso fix'. Write /onboarding/maria_rodriguez/access_gaps.md as text/markdown including exactly these four lines, each on a separate line: ['Email: Failed - exchange server issue','SSO: Failed - idp sync pending','Slack: Failed - depends on sso','GitHub: Pending - waiting for sso fix']. Dispatch msg_access_maria to ['it-support@company.com','daniel.lee@company.com'] with subject 'access issues alert - Sofia Martinez' and body 'see details'.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_4",
                    "system_name": "Email",
                    "status": "Failed",
                    "note_nullable": "exchange server issue"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_4",
                    "system_name": "SSO",
                    "status": "Failed",
                    "note_nullable": "idp sync pending"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_4",
                    "system_name": "Slack",
                    "status": "Failed",
                    "note_nullable": "depends on sso"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_4",
                    "system_name": "GitHub",
                    "status": "Pending",
                    "note_nullable": "waiting for sso fix"
                },
            },
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/maria_rodriguez/access_gaps.md",
                    "content_text": "Email: Failed - exchange server issue\nSSO: Failed - idp sync pending\nSlack: Failed - depends on sso\nGitHub: Pending - waiting for sso fix",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_access_maria",
                    "subject": "access issues alert - Sofia Martinez",
                    "body": "see details",
                    "to_emails": [
                        "it-support@company.com",
                        "daniel.lee@company.com"
                    ],
                    "candidate_id": "cand_4",
                    "draft_flag": false,
                    "sent_flag": true
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "004",
        "instruction": "Coordinate the Checklist-Follow-Up protocol for cand_2 (Emma Thompson). Ensure the final state includes: a markdown summary stored at /onboarding/jane_smith/pending_tasks.md with mime type text/markdown and content exactly '- HR Forms - Benefits Enrollment - Security Training '; an email record with message_id msg_reminder_jane sent to ['emma.thompson@example.com'] with subject 'Pending Onboarding Tasks' and body 'Please complete pending items', carrying the label Onboarding-Reminder identified by label_id label_2; update checklist items item_4, item_5, item_6, item_7 to status 'Reminder Sent' with reminder_sent_flag True and reminder_email_message_id_nullable 'msg_reminder_jane'; ensure candidate cand_2 has checklist_follow_up_ts_nullable set to '2025-01-01T09:00:00Z'; verify an MCP audit exists with server_name gmail, tool_name send_reminder, and params_json {'message_id':'msg_reminder_jane'}.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/jane_smith/pending_tasks.md",
                    "content_text": "- HR Forms\n- Benefits Enrollment\n- Security Training\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "CreateOrGetEmailLabel",
                "arguments": {
                    "name": "Onboarding-Reminder"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_reminder_jane",
                    "subject": "Pending Onboarding Tasks",
                    "body": "Please complete pending items",
                    "to_emails": [
                        "emma.thompson@example.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_reminder_jane",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "BulkUpdateChecklistItems",
                "arguments": {
                    "item_ids": [
                        "item_4",
                        "item_5",
                        "item_6",
                        "item_7"
                    ],
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_reminder_jane"
                    }
                },
            },
            {
                "name": "SetCandidateTimestamps",
                "arguments": {
                    "candidate_id": "cand_2",
                    "fields": {
                        "checklist_follow_up_ts_nullable": "2025-01-01T09:00:00Z"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "send_reminder",
                    "params_json": {
                        "message_id": "msg_reminder_jane"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "005",
        "instruction": "Handle the laptop exchange for cand_3 (William Davis), switching from LT-DELL-002 to LT-MBP-002. Notify it-assets by sending an email with message_id=msg_asset_swap_peter, subject='asset swap - William Davis', body='dell to mbp', to_emails=['it-assets@company.com'], label_id=label_1, and thread_id=thread_swap_peter. Audit gmail asset_swap_notice for {'message_id':'msg_asset_swap_peter'}.",
        "actions": [
            {
                "name": "ReleaseInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-002"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-002",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_asset_swap_peter",
                    "subject": "asset swap - William Davis",
                    "body": "dell to mbp",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_asset_swap_peter",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_asset_swap_peter",
                    "fields": {
                        "thread_id_nullable": "thread_swap_peter"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "asset_swap_notice",
                    "params_json": {
                        "message_id": "msg_asset_swap_peter"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "007",
        "instruction": "Complete the phone provisioning for cand_4 (Sofia Martinez). Set asset_req_6 to Completed status. Confirm msg_12 is the provisioning email and assign label_id label_1 (Asset-Request) to it. Finalize the assignment of PH-IPHONE-002 to cand_4. Add a phone setup note at /onboarding/maria_rodriguez/phone_setup.md with mime text/markdown and content 'iphone setup checklist'. Attach phone_setup.md to msg_12 using attachment_id attach_phone_setup_maria and the same file_path. Set checklist items item_8, item_9, item_10 as Completed. Record an mcp call for gmail using tool_name finalize_phone_request referencing msg_12.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "asset_req_6",
                    "fields": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_12",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-002",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/maria_rodriguez/phone_setup.md",
                    "content_text": "iphone setup checklist",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_phone_setup_maria",
                    "message_id": "msg_12",
                    "filename": "phone_setup.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/maria_rodriguez/phone_setup.md"
                },
            },
            {
                "name": "BulkUpdateChecklistItems",
                "arguments": {
                    "item_ids": [
                        "item_8",
                        "item_9",
                        "item_10"
                    ],
                    "fields": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "finalize_phone_request",
                    "params_json": {
                        "message_id": "msg_12"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "010",
        "instruction": "Handle the peripherals-allocation protocol for cand_5 (Jordan Williams). Ensure the final state includes: assignment of assets MON-DELL-001 and DS-DELL-001 to cand_5; a terminal log entry stating 'assigned monitor MON-DELL-001 and dock DS-DELL-001 to Jordan Williams'; a sent email record with message_id msg_peripherals_alex directed to ['it-assets@company.com'] with the subject 'Peripheral Allocation - Jordan Williams' and body 'monitor and dock assigned', tagged with label_id label_1; checklist items item_11, item_12, item_13, item_14 updated to a status of 'Completed'; an mcp audit for gmail utilizing tool_name notify_peripherals referencing msg_peripherals_alex.",
        "actions": [
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "MON-DELL-001",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "DS-DELL-001",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "assigned monitor MON-DELL-001 and dock DS-DELL-001 to Jordan Williams"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_peripherals_alex",
                    "subject": "Peripheral Allocation - Jordan Williams",
                    "body": "monitor and dock assigned",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_5",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_peripherals_alex",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "BulkUpdateChecklistItems",
                "arguments": {
                    "item_ids": [
                        "item_11",
                        "item_12",
                        "item_13",
                        "item_14"
                    ],
                    "fields": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "notify_peripherals",
                    "params_json": {
                        "message_id": "msg_peripherals_alex"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "011",
        "instruction": "Coordinate the dispatch of a concise checklist reminder for cand_1 (Michael Anderson). Record /onboarding/john_doe/pending_tasks.md in text/markdown format with '- it setup - benefits enrollment '. Dispatch msg_reminder_john2 to michael.anderson@example.com with the subject 'pending onboarding tasks - Michael Anderson' and body 'please complete items', tagged with label_2, and update items item_3 and item_4 to 'Reminder Sent' with reminder_email_message_id_nullable msg_reminder_john2.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/john_doe/pending_tasks.md",
                    "content_text": "- it setup\n- benefits enrollment\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_reminder_john2",
                    "subject": "pending onboarding tasks - Michael Anderson",
                    "body": "please complete items",
                    "to_emails": [
                        "michael.anderson@example.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_reminder_john2",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "BulkUpdateChecklistItems",
                "arguments": {
                    "item_ids": [
                        "item_3",
                        "item_4"
                    ],
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_email_message_id_nullable": "msg_reminder_john2"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "012",
        "instruction": "Complete the assets-provisioning closeout for cand_7 (Raj Patel). Supply the following parameters: asset_request='asset_req_5' final_status='Completed'; close_email={message_id:msg_assets_robert_close, to:['it-assets@company.com'], subject:'Asset Provisioning Completed - Raj Patel', body:'completed', label_id:label_1, thread_id:thread_assets_robert_close}; candidate_link={'asset_request_record_id_nullable':'asset_req_5'}; audit_text='closed asset_req_5 as Completed for Raj Patel'.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "asset_req_5",
                    "fields": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "closed asset_req_5 as Completed for Raj Patel"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_assets_robert_close",
                    "subject": "Asset Provisioning Completed - Raj Patel",
                    "body": "completed",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_assets_robert_close",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "SetCandidateFields",
                "arguments": {
                    "candidate_id": "cand_7",
                    "fields": {
                        "asset_request_record_id_nullable": "asset_req_5"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_assets_robert_close",
                    "fields": {
                        "thread_id_nullable": "thread_assets_robert_close"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "asset_provision_close",
                    "params_json": {
                        "message_id": "msg_assets_robert_close"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "015",
        "instruction": "Carry out the phone-allocation protocol for cand_3 (William Davis). Use the parameters: asset_tag='PH-IPHONE-001'; audit_text='assigned phone PH-IPHONE-001 to William Davis'; notify_email={message_id:msg_phone_peter, to:['it-assets@company.com'], subject:'Phone Allocation - William Davis', body:'iphone assigned', label_id:label_1, thread_id:thread_phone_peter}.",
        "actions": [
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-001",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "assigned phone PH-IPHONE-001 to William Davis"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_phone_peter",
                    "subject": "Phone Allocation - William Davis",
                    "body": "iphone assigned",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_phone_peter",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_phone_peter",
                    "fields": {
                        "thread_id_nullable": "thread_phone_peter"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "notify_phone_allocation",
                    "params_json": {
                        "message_id": "msg_phone_peter"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "016",
        "instruction": "Handle the policy-acknowledgment protocol for cand_6 (Lily Zhang). Provide parameters: ack_path=/onboarding/emily_chen/policy_ack.md, ack_mime=text/markdown, ack_content='i acknowledge company policies'; ack_email={message_id:msg_policy_ack_emily, to:['lily.zhang@example.com'], subject:'Policy Acknowledgment - Lily Zhang', body:'ack attached', label_id:label_6, thread_id:thread_policy_ack_emily, attach_filename:policy_ack.md}; candidate_fields={'policy_acknowledged':'true'}.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/emily_chen/policy_ack.md",
                    "content_text": "i acknowledge company policies",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_policy_ack_emily",
                    "subject": "Policy Acknowledgment - Lily Zhang",
                    "body": "ack attached",
                    "to_emails": [
                        "lily.zhang@example.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_policy_ack_emily",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_policy_ack_emily",
                    "message_id": "msg_policy_ack_emily",
                    "filename": "policy_ack.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/emily_chen/policy_ack.md"
                },
            },
            {
                "name": "SetCandidateFields",
                "arguments": {
                    "candidate_id": "cand_6",
                    "fields": {
                        "policy_acknowledged": "true"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_policy_ack_emily",
                    "fields": {
                        "thread_id_nullable": "thread_policy_ack_emily"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "send_policy_ack_emily",
                    "params_json": {
                        "message_id": "msg_policy_ack_emily"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "017",
        "instruction": "Coordinate the checklist-reminder protocol for cand_5 (Jordan Williams). Provide parameters: note_path=/onboarding/alex_thompson/pending_tasks.md, note_mime=text/markdown, note_content='- security training - benefits enrollment '; reminder_email={message_id:msg_reminder_alex, to:['jordan.williams@example.com'], subject:'Pending Onboarding Tasks - Jordan Williams', body:'please complete pending items', label_id:label_2}; update_items=[item_11,item_12] to status 'Reminder Sent' with reminder_sent_flag true and reminder_email_message_id_nullable 'msg_reminder_alex'; audit={'server_name':'gmail','tool_name':'send_reminder_alex','params_json':{'message_id':'msg_reminder_alex'}}.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/alex_thompson/pending_tasks.md",
                    "content_text": "- security training\n- benefits enrollment\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_reminder_alex",
                    "subject": "Pending Onboarding Tasks - Jordan Williams",
                    "body": "please complete pending items",
                    "to_emails": [
                        "jordan.williams@example.com"
                    ],
                    "candidate_id": "cand_5",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_reminder_alex",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_11",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_reminder_alex"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_12",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_reminder_alex"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "send_reminder_alex",
                    "params_json": {
                        "message_id": "msg_reminder_alex"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "018",
        "instruction": "Handle the laptop-replacement protocol for cand_4 (Sofia Martinez). Provide parameters: release_asset='LT-DELL-002', assign_asset='LT-MBP-001'; audit_text='replaced Sofia Martinez laptop from LT-DELL-002 to LT-MBP-001'; notify_email={message_id:msg_asset_replace_maria, to:['it-assets@company.com'], subject:'Asset Replacement - Sofia Martinez', body:'dell to mbp', label_id:label_1, thread_id:thread_asset_replace_maria};",
        "actions": [
            {
                "name": "ReleaseInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-002"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-001",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "replaced Sofia Martinez laptop from LT-DELL-002 to LT-MBP-001"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_asset_replace_maria",
                    "subject": "Asset Replacement - Sofia Martinez",
                    "body": "dell to mbp",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_4",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_asset_replace_maria",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_asset_replace_maria",
                    "fields": {
                        "thread_id_nullable": "thread_asset_replace_maria"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "021",
        "instruction": "Coordinate the welcome packet resend protocol for cand_3 (William Davis). Provide parameters: file_path=/onboarding/peter_jones/welcome_peter_jones_v2.md, file_mime=text/markdown, file_content='# welcome again peter\nplease review the attached docs.\n', message_id=msg_welcome_peter_v2, subject='welcome packet (resend) - William Davis', body='peter, welcome again. docs attached.', to_emails=['william.davis@example.com'], label_name='Welcome-Packet', label_id='label_6', attach_id=attach_welcome_peter_v2, attach_filename=welcome_peter_jones_v2.md, attach_mime=text/markdown, thread_id=thread_welcome_peter_v2.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/peter_jones/welcome_peter_jones_v2.md",
                    "content_text": "# welcome again peter\nplease review the attached docs.\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "CreateOrGetEmailLabel",
                "arguments": {
                    "name": "Welcome-Packet"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_welcome_peter_v2",
                    "subject": "welcome packet (resend) - William Davis",
                    "body": "peter, welcome again. docs attached.",
                    "to_emails": [
                        "william.davis@example.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_welcome_peter_v2",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_welcome_peter_v2",
                    "message_id": "msg_welcome_peter_v2",
                    "filename": "welcome_peter_jones_v2.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/peter_jones/welcome_peter_jones_v2.md"
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_welcome_peter_v2",
                    "fields": {
                        "thread_id_nullable": "thread_welcome_peter_v2"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "send_welcome_resend",
                    "params_json": {
                        "message_id": "msg_welcome_peter_v2"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "022",
        "instruction": "Handle the phone allocation procedure for cand_1 (Michael Anderson). Supply parameters: asset_tag=PH-IPHONE-001, message_id=msg_phone_alloc_john, subject='phone allocation - Michael Anderson', body='iphone assigned.', to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_phone_alloc_john, audit={'server_name':'gmail','tool_name':'notify_phone_alloc','params_json':{'message_id':'msg_phone_alloc_john'}}.",
        "actions": [
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-001",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_phone_alloc_john",
                    "subject": "phone allocation - Michael Anderson",
                    "body": "iphone assigned.",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_phone_alloc_john",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_phone_alloc_john",
                    "fields": {
                        "thread_id_nullable": "thread_phone_alloc_john"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "allocated PH-IPHONE-001 to cand_1"
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "notify_phone_alloc",
                    "params_json": {
                        "message_id": "msg_phone_alloc_john"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "023",
        "instruction": "Coordinate the orientation invite procedure for cand_5 (Jordan Williams). Submit parameters: agenda_path=/onboarding/alex_thompson/orientation_agenda.md, agenda_mime=text/markdown, agenda_content='# orientation agenda\nteam intros and setup\n', message_id=msg_orientation_alex, subject='day-1 orientation - Jordan Williams', body='agenda attached', to_emails=['jordan.williams@example.com'], label_name='Orientation-Invite', label_id='label_4', attach_id=attach_orientation_agenda_alex, attach_filename=orientation_agenda.md, attach_mime=text/markdown, orientation_ts=2024-08-20T09:00:00Z, thread_id=thread_orientation_alex.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/alex_thompson/orientation_agenda.md",
                    "content_text": "# orientation agenda\nteam intros and setup\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "CreateOrGetEmailLabel",
                "arguments": {
                    "name": "Orientation-Invite"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_orientation_alex",
                    "subject": "day-1 orientation - Jordan Williams",
                    "body": "agenda attached",
                    "to_emails": [
                        "jordan.williams@example.com"
                    ],
                    "candidate_id": "cand_5",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_orientation_alex",
                    "label_ids": [
                        "label_4"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_orientation_agenda_alex",
                    "message_id": "msg_orientation_alex",
                    "filename": "orientation_agenda.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/alex_thompson/orientation_agenda.md"
                },
            },
            {
                "name": "SetCandidateFields",
                "arguments": {
                    "candidate_id": "cand_5",
                    "fields": {
                        "orientation_invite_ts_nullable": "2024-08-20T09:00:00Z"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_orientation_alex",
                    "fields": {
                        "thread_id_nullable": "thread_orientation_alex"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "025",
        "instruction": "Handle the checklist-closeout protocol for cand_5 (Jordan Williams). Supply parameters: item_ids=['item_13','item_14'], message_id=msg_checklist_close_alex, subject='checklist closeout - Jordan Williams', body='remaining items completed', to_emails=['jordan.williams@example.com'], label_id=label_2, thread_id=thread_checklist_close_alex, log_text='closed remaining checklist items [item_13,item_14]', audit={'server_name':'gmail','tool_name':'send_closeout','params_json':{'message_id':'msg_checklist_close_alex'}}.",
        "actions": [
            {
                "name": "BulkUpdateChecklistItems",
                "arguments": {
                    "item_ids": [
                        "item_13",
                        "item_14"
                    ],
                    "fields": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_checklist_close_alex",
                    "subject": "checklist closeout - Jordan Williams",
                    "body": "remaining items completed",
                    "to_emails": [
                        "jordan.williams@example.com"
                    ],
                    "candidate_id": "cand_5",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_checklist_close_alex",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_checklist_close_alex",
                    "fields": {
                        "thread_id_nullable": "thread_checklist_close_alex"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "closed remaining checklist items [item_13,item_14]"
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "send_closeout",
                    "params_json": {
                        "message_id": "msg_checklist_close_alex"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "026",
        "instruction": "Coordinate the phone request closure protocol for cand_4 (Sofia Martinez). Deliver parameters: request_id=asset_req_6, new_status=Completed, message_id=msg_phone_close_maria, subject='phone request closed - Sofia Martinez', body='phone request completed', to_emails=['it-assets@company.com'], label_name='Asset-Request', label_id='label_1', thread_id=thread_phone_close_maria.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "asset_req_6",
                    "fields": {
                        "status": "Completed",
                        "email_message_id_nullable": "msg_phone_close_maria"
                    }
                },
            },
            {
                "name": "CreateOrGetEmailLabel",
                "arguments": {
                    "name": "Asset-Request"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_phone_close_maria",
                    "subject": "phone request closed - Sofia Martinez",
                    "body": "phone request completed",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_4",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_phone_close_maria",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_phone_close_maria",
                    "fields": {
                        "thread_id_nullable": "thread_phone_close_maria"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "notify_phone_close",
                    "params_json": {
                        "message_id": "msg_phone_close_maria"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "028",
        "instruction": "Handle the system-clearance notification protocol for cand_6 (Lily Zhang). Supply parameters: checks=[('Email','Success',None),('Marketing Platform','Success',None)], message_id=msg_clearance_emily, subject='system clearance - Lily Zhang', body='all core systems clear', to_emails=['it-support@company.com'], label_name='System-Alerts', label_id='label_7'.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_6",
                    "system_name": "Email",
                    "status": "Success"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_6",
                    "system_name": "Marketing Platform",
                    "status": "Success"
                },
            },
            {
                "name": "CreateOrGetEmailLabel",
                "arguments": {
                    "name": "System-Alerts"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_clearance_emily",
                    "subject": "system clearance - Lily Zhang",
                    "body": "all core systems clear",
                    "to_emails": [
                        "it-support@company.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_clearance_emily",
                    "label_ids": [
                        "label_7"
                    ]
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "notify_clearance",
                    "params_json": {
                        "message_id": "msg_clearance_emily"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "029",
        "instruction": "Coordinate the thread-link and notes protocol for cand_5 (Jordan Williams) on provisioning email msg_11. Supply parameters: notes_path=/onboarding/alex_thompson/provisioning_notes.md, notes_mime=text/markdown, notes_content='notes:\n- slack provisioned as planned\n', attach_id=attach_provisioning_notes_alex, attach_filename=provisioning_notes.md, attach_mime=text/markdown, label_id=label_1, thread_id=thread_slack_provisioning_link, audit_text='linked provisioning notes to msg_11 for cand_5'.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/alex_thompson/provisioning_notes.md",
                    "content_text": "notes:\n- slack provisioned as planned\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_provisioning_notes_alex",
                    "message_id": "msg_11",
                    "filename": "provisioning_notes.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/alex_thompson/provisioning_notes.md"
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_11",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_11",
                    "fields": {
                        "thread_id_nullable": "thread_slack_provisioning_link"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "linked provisioning notes to msg_11 for cand_5"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "033",
        "instruction": "Handle the access-gap alert protocol for cand_3 (William Davis) with an emphasis on slack. Ensure to provide parameters: access_entry={system:'Slack', status:'Pending', note:'awaiting sso group'}, summary_path=/onboarding/peter_jones/slack_gap.md, summary_mime=text/markdown, summary_lines=['Slack: Pending - awaiting sso group'], email={message_id:msg_slack_gap_peter, to:['it-support@company.com'], subject:'access gap - William Davis (slack)', body:'see summary', label_id:label_7}, attach_id=attach_slack_gap_peter, attach_filename=slack_gap.md.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_3",
                    "system_name": "Slack",
                    "status": "Pending",
                    "note_nullable": "awaiting sso group"
                },
            },
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/peter_jones/slack_gap.md",
                    "content_text": "Slack: Pending - awaiting sso group\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_slack_gap_peter",
                    "subject": "access gap - William Davis (slack)",
                    "body": "see summary",
                    "to_emails": [
                        "it-support@company.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_slack_gap_peter",
                    "label_ids": [
                        "label_7"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_slack_gap_peter",
                    "message_id": "msg_slack_gap_peter",
                    "filename": "slack_gap.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/peter_jones/slack_gap.md"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "034",
        "instruction": "Coordinate the orientation-invite protocol for cand_1 (Michael Anderson). Make sure to provide parameters: agenda_path=/onboarding/john_doe/orientation_agenda.md, agenda_mime=text/markdown, agenda_content='# orientation agenda\nwelcome and setup\n', email={message_id:msg_orientation_john_v2, to:['michael.anderson@example.com'], subject:'day-1 orientation - Michael Anderson', body:'agenda attached', label_id:label_4, thread_id:thread_orientation_john_v2}, candidate_update={orientation_invite_ts_nullable:'2024-07-31T10:00:00Z'}, attach_id=attach_orientation_agenda_john_v2, attach_filename=orientation_agenda.md.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/john_doe/orientation_agenda.md",
                    "content_text": "# orientation agenda\nwelcome and setup\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_orientation_john_v2",
                    "subject": "day-1 orientation - Michael Anderson",
                    "body": "agenda attached",
                    "to_emails": [
                        "michael.anderson@example.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_orientation_john_v2",
                    "label_ids": [
                        "label_4"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_orientation_agenda_john_v2",
                    "message_id": "msg_orientation_john_v2",
                    "filename": "orientation_agenda.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/john_doe/orientation_agenda.md"
                },
            },
            {
                "name": "SetCandidateFields",
                "arguments": {
                    "candidate_id": "cand_1",
                    "fields": {
                        "orientation_invite_ts_nullable": "2024-07-31T10:00:00Z"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_orientation_john_v2",
                    "fields": {
                        "thread_id_nullable": "thread_orientation_john_v2"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "035",
        "instruction": "Handle the checklist-reminder protocol for cand_7 (Raj Patel). Supply parameters: note_path=/onboarding/robert_singh/pending_tasks.md, note_mime=text/markdown, note_content='- hr forms\n- security training\n', reminder_email={message_id:msg_reminder_robert, to:['raj.patel@example.com'], subject:'pending tasks - Raj Patel', body:'please complete', label_id:label_2}, update_items=['item_15','item_16'] to status 'Reminder Sent' with reminder_sent_flag true and reminder_email_message_id_nullable 'msg_reminder_robert'.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/robert_singh/pending_tasks.md",
                    "content_text": "- hr forms\n- security training\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_reminder_robert",
                    "subject": "pending tasks - Raj Patel",
                    "body": "please complete",
                    "to_emails": [
                        "raj.patel@example.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_reminder_robert",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "BulkUpdateChecklistItems",
                "arguments": {
                    "item_ids": [
                        "item_15",
                        "item_16"
                    ],
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_reminder_robert"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "036",
        "instruction": "Coordinate the peripherals-allocation protocol for cand_3 (William Davis). Supply parameters: assign_assets=['MON-DELL-001','KB-LOGI-001'], notify_email={message_id:msg_peripherals_peter, to:['it-assets@company.com'], subject:'peripherals allocation - William Davis', body:'monitor and keyboard assigned', label_id:label_1, thread_id:thread_peripherals_peter}, audit_text='assigned MON-DELL-001 and KB-LOGI-001 to cand_3'.",
        "actions": [
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "MON-DELL-001",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "KB-LOGI-001",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_peripherals_peter",
                    "subject": "peripherals allocation - William Davis",
                    "body": "monitor and keyboard assigned",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_peripherals_peter",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_peripherals_peter",
                    "fields": {
                        "thread_id_nullable": "thread_peripherals_peter"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "assigned MON-DELL-001 and KB-LOGI-001 to cand_3"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "037",
        "instruction": "Handle the phone-allocation protocol for cand_1 (Michael Anderson). Assign PH-IPHONE-001 to cand_1, notify it-assets with msg_phone_john_v2 using the subject 'phone allocation - Michael Anderson' and the body 'iphone assigned', labeled label_1 and linked under thread_phone_john_v2, then add a brief log.",
        "actions": [
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-001",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_phone_john_v2",
                    "subject": "phone allocation - Michael Anderson",
                    "body": "iphone assigned",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_phone_john_v2",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_phone_john_v2",
                    "fields": {
                        "thread_id_nullable": "thread_phone_john_v2"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "assigned PH-IPHONE-001 to cand_1"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "038",
        "instruction": "Coordinate the benefits-reminder protocol for cand_2 (Emma Thompson). Supply parameters: note_path=/onboarding/jane_smith/pending_tasks.md, note_mime=text/markdown, note_content='- benefits enrollment\n- direct deposit\n', use reminder_email={message_id:msg_benefits_reminder_jane, to:['emma.thompson@example.com'], subject:'benefits reminder - Emma Thompson', body:'please complete benefits setup', label_id:label_2}, and update_items=['item_5','item_6'] to status 'Reminder Sent' with reminder_sent_flag set to true and reminder_email_message_id_nullable 'msg_benefits_reminder_jane'.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/jane_smith/pending_tasks.md",
                    "content_text": "- benefits enrollment\n- direct deposit\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_benefits_reminder_jane",
                    "subject": "benefits reminder - Emma Thompson",
                    "body": "please complete benefits setup",
                    "to_emails": [
                        "emma.thompson@example.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_benefits_reminder_jane",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "BulkUpdateChecklistItems",
                "arguments": {
                    "item_ids": [
                        "item_5",
                        "item_6"
                    ],
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_benefits_reminder_jane"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "039",
        "instruction": "Handle the confirmation of access status for cand_6 (Lily Zhang) by noting the SSO success and pending status on the marketing platform with the remark 'vendor activation pending'. Dispatch a labeled email msg_access_status_emily to ['it-support@company.com'] with the subject 'access status - Lily Zhang' and include the body 'latest status enclosed' with label_id label_7.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_6",
                    "system_name": "SSO",
                    "status": "Success"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_6",
                    "system_name": "Marketing Platform",
                    "status": "Pending",
                    "note_nullable": "vendor activation pending"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_access_status_emily",
                    "subject": "access status - Lily Zhang",
                    "body": "latest status enclosed",
                    "to_emails": [
                        "it-support@company.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_access_status_emily",
                    "label_ids": [
                        "label_7"
                    ]
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "040",
        "instruction": "Coordinate the execution of the manager-intro protocol for cand_1 (Michael Anderson). Supply the following parameters: intro_note_path=/onboarding/john_doe/manager_intro.md, intro_note_mime=text/markdown, intro_note_content='# manager intro\nwelcome call\n'. Send an email with {message_id:msg_intro_john_v2, to:['michael.anderson@example.com'], subject:'manager intro - Michael Anderson', body:'calendar hold sent', label_id:label_5, thread_id:thread_intro_john_v2}, and update the candidate information with {manager_intro_invite_ts_nullable:'2024-07-31T10:30:00Z'}.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/john_doe/manager_intro.md",
                    "content_text": "# manager intro\nwelcome call\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_intro_john_v2",
                    "subject": "manager intro - Michael Anderson",
                    "body": "calendar hold sent",
                    "to_emails": [
                        "michael.anderson@example.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_intro_john_v2",
                    "label_ids": [
                        "label_5"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_intro_john_v2",
                    "fields": {
                        "thread_id_nullable": "thread_intro_john_v2"
                    }
                },
            },
            {
                "name": "SetCandidateFields",
                "arguments": {
                    "candidate_id": "cand_1",
                    "fields": {
                        "manager_intro_invite_ts_nullable": "2024-07-31T10:30:00Z"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "044",
        "instruction": "Handle the checklist-reminder protocol for cand_2 (Emma Thompson). Supply parameters: note_path=/onboarding/jane_smith/pending_tasks_2.md, note_mime=text/markdown, note_content='- benefits enrollment\n- security training\n', message_id=msg_reminder_jane_2, subject='pending onboarding tasks - Emma Thompson', body='please complete pending items', to_emails=['emma.thompson@example.com'], label_id=label_2, update_items=[item_5,item_6].",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/jane_smith/pending_tasks_2.md",
                    "content_text": "- benefits enrollment\n- security training\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_reminder_jane_2",
                    "subject": "pending onboarding tasks - Emma Thompson",
                    "body": "please complete pending items",
                    "to_emails": [
                        "emma.thompson@example.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_reminder_jane_2",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_5",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_reminder_jane_2"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_6",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_reminder_jane_2"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "045",
        "instruction": "Coordinate the laptop-swap notice protocol for cand_3 (William Davis). Supply parameters: old_tag=LT-DELL-002, new_tag=LT-MBP-001, message_id=msg_asset_swap_peter_2, subject='asset swap - William Davis', body='dell to mbp', to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_swap_peter_2, audit_text='swapped William Davis from LT-DELL-002 to LT-MBP-001'.",
        "actions": [
            {
                "name": "ReleaseInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-002"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-001",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_asset_swap_peter_2",
                    "subject": "asset swap - William Davis",
                    "body": "dell to mbp",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_asset_swap_peter_2",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_asset_swap_peter_2",
                    "fields": {
                        "thread_id_nullable": "thread_swap_peter_2"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "swapped William Davis from LT-DELL-002 to LT-MBP-001"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "046",
        "instruction": "Handle the peripherals-allocation notice for cand_6 (Lily Zhang). Supply parameters: tags=['MON-DELL-001','DS-DELL-001'], message_id=msg_peripherals_emily_2, subject='peripheral allocation - Lily Zhang', body='monitor and dock assigned', to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_peripherals_emily_2,",
        "actions": [
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "MON-DELL-001",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "DS-DELL-001",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_peripherals_emily_2",
                    "subject": "peripheral allocation - Lily Zhang",
                    "body": "monitor and dock assigned",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_peripherals_emily_2",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_peripherals_emily_2",
                    "fields": {
                        "thread_id_nullable": "thread_peripherals_emily_2"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "049",
        "instruction": "Coordinate the phone-request closeout for cand_4 (Sofia Martinez). Supply the parameters: request_id=asset_req_6, status='Completed', message_id=msg_phone_close_maria, subject='phone request closeout - Sofia Martinez', body='completed', to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_phone_close_maria, audit_text='closed asset_req_6 for cand_4'.",
        "actions": [
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "asset_req_6",
                    "fields": {
                        "status": "Completed",
                        "email_message_id_nullable": "msg_phone_close_maria"
                    }
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_phone_close_maria",
                    "subject": "phone request closeout - Sofia Martinez",
                    "body": "completed",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_4",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_phone_close_maria",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_phone_close_maria",
                    "fields": {
                        "thread_id_nullable": "thread_phone_close_maria"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "closed asset_req_6 for cand_4"
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "notify_phone_closeout",
                    "params_json": {
                        "message_id": "msg_phone_close_maria"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "050",
        "instruction": "Handle the linking of a policy acknowledgment for cand_2 (Emma Thompson). Save /onboarding/jane_smith/policy_ack.md as text/markdown with 'policy ack', and send msg_policy_ack_jane to emma.thompson@example.com using subject 'policy ack - Emma Thompson' and body 'ack received', labeled with label_6 and attach that file.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/jane_smith/policy_ack.md",
                    "content_text": "policy ack\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_policy_ack_jane",
                    "subject": "policy ack - Emma Thompson",
                    "body": "ack received",
                    "to_emails": [
                        "emma.thompson@example.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_policy_ack_jane",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_policy_ack_jane",
                    "message_id": "msg_policy_ack_jane",
                    "filename": "policy_ack.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/jane_smith/policy_ack.md"
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "link_policy_ack",
                    "params_json": {
                        "message_id": "msg_policy_ack_jane"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "051",
        "instruction": "Coordinate the refreshing of the welcome attachment for cand_3 (William Davis). Save /onboarding/peter_jones/welcome_addendum.md as text/markdown with 'addendum v2', and send msg_welcome_addendum_peter to william.davis@example.com using subject 'welcome addendum - William Davis' and body 'see addendum', labeled with label_6 and attach the addendum.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/peter_jones/welcome_addendum.md",
                    "content_text": "addendum v2\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_welcome_addendum_peter",
                    "subject": "welcome addendum - William Davis",
                    "body": "see addendum",
                    "to_emails": [
                        "william.davis@example.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_welcome_addendum_peter",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_welcome_addendum_peter",
                    "message_id": "msg_welcome_addendum_peter",
                    "filename": "welcome_addendum.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/peter_jones/welcome_addendum.md"
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "send_welcome_addendum",
                    "params_json": {
                        "message_id": "msg_welcome_addendum_peter"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "052",
        "instruction": "You reissue the orientation invite for cand_6 (Lily Zhang). Store /onboarding/emily_chen/orientation_agenda_resend.md as text/markdown with '# orientation agenda\nresend copy\n', and send msg_orientation_emily_resend to lily.zhang@example.com with subject 'day-1 orientation (resend) - Lily Zhang' and body 'agenda attached', tagged with label_4, including the resend agenda in the attachment.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/emily_chen/orientation_agenda_resend.md",
                    "content_text": "# orientation agenda\nresend copy\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_orientation_emily_resend",
                    "subject": "day-1 orientation (resend) - Lily Zhang",
                    "body": "agenda attached",
                    "to_emails": [
                        "lily.zhang@example.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_orientation_emily_resend",
                    "label_ids": [
                        "label_4"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_orientation_agenda_emily_resend",
                    "message_id": "msg_orientation_emily_resend",
                    "filename": "orientation_agenda_resend.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/emily_chen/orientation_agenda_resend.md"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "053",
        "instruction": "Handle the asset-reassignment protocol for cand_2 (Emma Thompson) to relocate to LT-MBP-002. Supply parameters: release_tag=LT-DELL-003, assign_tag=LT-MBP-002, message_id=msg_asset_reassign_jane, subject='asset reassignment - Emma Thompson', body='moved to mbp', to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_asset_reassign_jane, audit_text='reassigned Emma Thompson from LT-DELL-003 to LT-MBP-002'.",
        "actions": [
            {
                "name": "ReleaseInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-003"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-002",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_asset_reassign_jane",
                    "subject": "asset reassignment - Emma Thompson",
                    "body": "moved to mbp",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_asset_reassign_jane",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_asset_reassign_jane",
                    "fields": {
                        "thread_id_nullable": "thread_asset_reassign_jane"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "reassigned Emma Thompson from LT-DELL-003 to LT-MBP-002"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "054",
        "instruction": "Handle the recording of an access pass for cand_3 (William Davis) and inform support. Record Email pass and SSO pass with notes 'ok', and dispatch msg_access_pass_peter to ['it-support@company.com'] with the subject 'access pass - William Davis' and the body 'all good', marked with label_7.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_3",
                    "system_name": "Email",
                    "status": "Pass",
                    "note_nullable": "ok"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_3",
                    "system_name": "SSO",
                    "status": "Pass",
                    "note_nullable": "ok"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_access_pass_peter",
                    "subject": "access pass - William Davis",
                    "body": "all good",
                    "to_emails": [
                        "it-support@company.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_access_pass_peter",
                    "label_ids": [
                        "label_7"
                    ]
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "055",
        "instruction": "Coordinate the execution of the benefits-reminder protocol for cand_6 (Lily Zhang). Supply parameters: note_path=/onboarding/emily_chen/benefits_pending.md, note_mime=text/markdown, note_content='- benefits enrollment\n', message_id=msg_benefits_reminder_emily, subject='benefits reminder - Lily Zhang', body='please complete benefits', to_emails=['lily.zhang@example.com'], label_id=label_2, update_items=[item_9], thread_id=thread_benefits_reminder_emily.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/emily_chen/benefits_pending.md",
                    "content_text": "- benefits enrollment\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_benefits_reminder_emily",
                    "subject": "benefits reminder - Lily Zhang",
                    "body": "please complete benefits",
                    "to_emails": [
                        "lily.zhang@example.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_benefits_reminder_emily",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_9",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_benefits_reminder_emily"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_benefits_reminder_emily",
                    "fields": {
                        "thread_id_nullable": "thread_benefits_reminder_emily"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "send_benefits_reminder",
                    "params_json": {
                        "message_id": "msg_benefits_reminder_emily"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "057",
        "instruction": "Handle the laptop-ready notice for cand_7 (Raj Patel). Supply parameters: message_id=msg_laptop_ready_robert, subject='laptop ready - Raj Patel', body='pick up scheduled', to_emails=['raj.patel@example.com'], label_id=label_1, thread_id=thread_laptop_ready_robert, and update asset_req_5 to status 'Sent' with email_message_id_nullable msg_laptop_ready_robert.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_laptop_ready_robert",
                    "subject": "laptop ready - Raj Patel",
                    "body": "pick up scheduled",
                    "to_emails": [
                        "raj.patel@example.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_laptop_ready_robert",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_laptop_ready_robert",
                    "fields": {
                        "thread_id_nullable": "thread_laptop_ready_robert"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "notify_laptop_ready",
                    "params_json": {
                        "message_id": "msg_laptop_ready_robert"
                    }
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "asset_req_5",
                    "fields": {
                        "status": "Sent",
                        "email_message_id_nullable": "msg_laptop_ready_robert"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "laptop ready notice sent for cand_7"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "058",
        "instruction": "Coordinate the access-summary record for cand_2 (Emma Thompson). Supply parameters: checks=[('Slack','Pass','ok'),('GitHub','Pending','awaiting sso')], message_id=msg_access_summary_jane, subject='access summary - Emma Thompson', body='status included', to_emails=['it-support@company.com'], label_id=label_7, thread_id=thread_access_summary_jane, and audit gmail notify_access_summary for {'message_id':'msg_access_summary_jane'}.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_2",
                    "system_name": "Slack",
                    "status": "Pass",
                    "note_nullable": "ok"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_2",
                    "system_name": "GitHub",
                    "status": "Pending",
                    "note_nullable": "awaiting sso"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_access_summary_jane",
                    "subject": "access summary - Emma Thompson",
                    "body": "status included",
                    "to_emails": [
                        "it-support@company.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_access_summary_jane",
                    "label_ids": [
                        "label_7"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_access_summary_jane",
                    "fields": {
                        "thread_id_nullable": "thread_access_summary_jane"
                    }
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "notify_access_summary",
                    "params_json": {
                        "message_id": "msg_access_summary_jane"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "059",
        "instruction": "Handle the supplies-request notification for cand_4 (Sofia Martinez). Supply parameters: message_id=msg_supplies_maria, subject='supplies request - Sofia Martinez', body='starter kit requested', to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_supplies_maria, audit_text='starter kit requested for cand_4'.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_supplies_maria",
                    "subject": "supplies request - Sofia Martinez",
                    "body": "starter kit requested",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_4",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_supplies_maria",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_supplies_maria",
                    "fields": {
                        "thread_id_nullable": "thread_supplies_maria"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "starter kit requested for cand_4"
                },
            },
            {
                "name": "RecordMcpToolCall",
                "arguments": {
                    "server_name": "gmail",
                    "tool_name": "notify_supplies_request",
                    "params_json": {
                        "message_id": "msg_supplies_maria"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "061",
        "instruction": "Oversee the confirmation of the welcome for cand_2 (Emma Thompson) using a brief note and a labeled email to jane. Preserve /onboarding/jane_smith/welcome_confirm.md as text/markdown with '# welcome confirmed\nsee details inside\n'. Deliver msg_welcome_confirm_jane not to michael.anderson@example.com but to emma.thompson@example.com with subject 'welcome confirmation - Emma Thompson' and body 'welcome confirmed'. Tag it as label_6, append welcome_confirm.md along with Company-Policies.pdf and Benefits-Guide.pdf, associate thread to thread_welcome_confirm_jane, and establish candidate welcome_email_message_id_nullable as msg_welcome_confirm_jane.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/jane_smith/welcome_confirm.md",
                    "content_text": "# welcome confirmed\nsee details inside\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_welcome_confirm_jane",
                    "subject": "welcome confirmation - Emma Thompson",
                    "body": "welcome confirmed",
                    "to_emails": [
                        "emma.thompson@example.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_welcome_confirm_jane",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_welcome_confirm_jane",
                    "message_id": "msg_welcome_confirm_jane",
                    "filename": "welcome_confirm.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/jane_smith/welcome_confirm.md"
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_jane_policies_pdf",
                    "message_id": "msg_welcome_confirm_jane",
                    "filename": "Company-Policies.pdf",
                    "mime_type": "application/pdf",
                    "file_path": "/onboarding/jane_smith/Company-Policies.pdf"
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_jane_benefits_pdf",
                    "message_id": "msg_welcome_confirm_jane",
                    "filename": "Benefits-Guide.pdf",
                    "mime_type": "application/pdf",
                    "file_path": "/onboarding/jane_smith/Benefits-Guide.pdf"
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_welcome_confirm_jane",
                    "fields": {
                        "thread_id_nullable": "thread_welcome_confirm_jane"
                    }
                },
            },
            {
                "name": "SetCandidateFields",
                "arguments": {
                    "candidate_id": "cand_2",
                    "fields": {
                        "welcome_email_message_id_nullable": "msg_welcome_confirm_jane"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "062",
        "instruction": "You need to handle a laptop replacement for cand_3 (William Davis), switching from LT-DELL-002 to LT-MBP-001, and then notify it. Include a brief swap note at /onboarding/peter_jones/swap_note.md (text/markdown, 'swap: LT-DELL-002 -> LT-MBP-001'). Forward msg_swap_peter to it-assets@company.com with subject 'asset swap - William Davis' and body 'dell to mbp', label label_1, attach the note, and provide a link to thread_swap_peter.",
        "actions": [
            {
                "name": "ReleaseInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-002"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-001",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/peter_jones/swap_note.md",
                    "content_text": "swap: LT-DELL-002 -> LT-MBP-001",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_swap_peter",
                    "subject": "asset swap - William Davis",
                    "body": "dell to mbp",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_swap_peter",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_swap_note_peter",
                    "message_id": "msg_swap_peter",
                    "filename": "swap_note.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/peter_jones/swap_note.md"
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_swap_peter",
                    "fields": {
                        "thread_id_nullable": "thread_swap_peter"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "063",
        "instruction": "Coordinate the escalation of access issues for cand_4 (Sofia Martinez) with a succinct summary and a designated alert. Document Email Failed 'exchange server issue' and SSO Failed 'idp sync pending'. Prepare /onboarding/maria_rodriguez/access_summary.md (text/markdown) with 'email: failed - exchange server issue\nsso: failed - idp sync pending\n'. Dispatch msg_access_alert_maria to it-support@company.com with subject 'access issues - Sofia Martinez' and body 'see summary', label label_3, append the summary, and include a link thread_access_alert_maria.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_4",
                    "system_name": "Email",
                    "status": "Failed",
                    "note_nullable": "exchange server issue"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_4",
                    "system_name": "SSO",
                    "status": "Failed",
                    "note_nullable": "idp sync pending"
                },
            },
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/maria_rodriguez/access_summary.md",
                    "content_text": "email: failed - exchange server issue\nsso: failed - idp sync pending\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_access_alert_maria",
                    "subject": "access issues - Sofia Martinez",
                    "body": "see summary",
                    "to_emails": [
                        "it-support@company.com"
                    ],
                    "candidate_id": "cand_4",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_access_alert_maria",
                    "label_ids": [
                        "label_3"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_access_summary_maria",
                    "message_id": "msg_access_alert_maria",
                    "filename": "access_summary.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/maria_rodriguez/access_summary.md"
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_access_alert_maria",
                    "fields": {
                        "thread_id_nullable": "thread_access_alert_maria"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "064",
        "instruction": "Handle a targeted checklist reminder for cand_5 (Jordan Williams) and update the list of items. Save /onboarding/alex_thompson/pending_tasks.md as text/markdown with '- kubernetes access\n- security training\n', and send msg_reminder_alex2 to jordan.williams@example.com using the subject 'pending tasks - Jordan Williams' and body 'please complete', labeled with label_2, while updating item_13 and item_14 to 'Reminder Sent' with reminder_email_message_id_nullable msg_reminder_alex2.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/alex_thompson/pending_tasks.md",
                    "content_text": "- kubernetes access\n- security training\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_reminder_alex2",
                    "subject": "pending tasks - Jordan Williams",
                    "body": "please complete",
                    "to_emails": [
                        "jordan.williams@example.com"
                    ],
                    "candidate_id": "cand_5",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_reminder_alex2",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "BulkUpdateChecklistItems",
                "arguments": {
                    "item_ids": [
                        "item_13",
                        "item_14"
                    ],
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_reminder_alex2"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "065",
        "instruction": "Coordinate the finalization of phone allocation for cand_1 (Michael Anderson) and notify accordingly. Assign PH-IPHONE-001 to cand_1. Include a brief setup note at /onboarding/john_doe/phone_setup.md (text/markdown) with 'iphone issued to Michael Anderson'. Send msg_phone_alloc_john2 to it-assets@company.com with subject 'phone allocation - Michael Anderson' and body 'iphone assigned', label label_1, attach the setup note, and link thread_phone_alloc_john2.",
        "actions": [
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-001",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/john_doe/phone_setup.md",
                    "content_text": "iphone issued to Michael Anderson",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_phone_alloc_john2",
                    "subject": "phone allocation - Michael Anderson",
                    "body": "iphone assigned",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_phone_alloc_john2",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_phone_setup_john",
                    "message_id": "msg_phone_alloc_john2",
                    "filename": "phone_setup.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/john_doe/phone_setup.md"
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_phone_alloc_john2",
                    "fields": {
                        "thread_id_nullable": "thread_phone_alloc_john2"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "066",
        "instruction": "Handle the submission of the asset request for cand_7 (Raj Patel) by dispatching the request JSON along with a labeled handoff email. Update asset_req_5 to Sent using the email id msg_assets_robert2. Create /onboarding/robert_singh/asset_request.json containing {'candidate':'cand_7','asset_type':'Laptop','requested_ts':'2024-08-06T14:20:00Z'}. Dispatch msg_assets_robert2 to it-assets@company.com with the subject 'asset provisioning request - Raj Patel' and the body 'see attached', utilize label_1, link to thread_assets_robert2, and make sure the candidate is associated with asset_req_5.",
        "actions": [
            {
                "name": "UpsertJsonArtifact",
                "arguments": {
                    "file_path": "/onboarding/robert_singh/asset_request.json",
                    "content_obj": {
                        "candidate": "cand_7",
                        "asset_type": "Laptop",
                        "requested_ts": "2024-08-06T14:20:00Z"
                    },
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_assets_robert2",
                    "subject": "asset provisioning request - Raj Patel",
                    "body": "see attached",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_assets_robert2",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "asset_req_5",
                    "fields": {
                        "status": "Sent",
                        "email_message_id_nullable": "msg_assets_robert2"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_assets_robert2",
                    "fields": {
                        "thread_id_nullable": "thread_assets_robert2"
                    }
                },
            },
            {
                "name": "LinkAssetRequestToCandidate",
                "arguments": {
                    "candidate_id": "cand_7",
                    "request_id": "asset_req_5"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "067",
        "instruction": "Coordinate the completion of orientation for cand_6 (Lily Zhang) by preparing an agenda and an invitation. Save /onboarding/emily_chen/orientation_agenda.md as text/markdown containing '# orientation agenda\nwelcome and access\n', and send msg_orientation_emily2 to lily.zhang@example.com with the subject 'day-1 orientation - Lily Zhang' and the body 'agenda attached', including the agenda as an attachment, and set orientation_invite_ts_nullable to 2024-08-23T09:30:00Z.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/emily_chen/orientation_agenda.md",
                    "content_text": "# orientation agenda\nwelcome and access\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_6"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_orientation_emily2",
                    "subject": "day-1 orientation - Lily Zhang",
                    "body": "agenda attached",
                    "to_emails": [
                        "lily.zhang@example.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_orientation_agenda_emily2",
                    "message_id": "msg_orientation_emily2",
                    "filename": "orientation_agenda.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/emily_chen/orientation_agenda.md"
                },
            },
            {
                "name": "SetCandidateFields",
                "arguments": {
                    "candidate_id": "cand_6",
                    "fields": {
                        "orientation_invite_ts_nullable": "2024-08-23T09:30:00Z"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "068",
        "instruction": "Handle the finalization of two checklist items for cand_2 (Emma Thompson) and confirm via email. Mark item_5 and item_6 as Completed. Dispatch msg_closeout_jane to emma.thompson@example.com with the subject 'checklist closeout - Emma Thompson' and body 'items completed', including label label_2, and attach link thread_closeout_jane.",
        "actions": [
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_5",
                    "fields": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_6",
                    "fields": {
                        "status": "Completed"
                    }
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_closeout_jane",
                    "subject": "checklist closeout - Emma Thompson",
                    "body": "items completed",
                    "to_emails": [
                        "emma.thompson@example.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_closeout_jane",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_closeout_jane",
                    "fields": {
                        "thread_id_nullable": "thread_closeout_jane"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "069",
        "instruction": "Coordinate the assignment of peripherals for cand_3 (William Davis) and inform IT. Designate MON-DELL-002 and HS-SONY-001 for cand_3. Deliver msg_peripherals_peter2 to it-assets@company.com with the subject 'peripherals allocation - William Davis' and body 'monitor and headset assigned', using label label_1, and attach link thread_peripherals_peter2.",
        "actions": [
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "MON-DELL-002",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "HS-SONY-001",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_peripherals_peter2",
                    "subject": "peripherals allocation - William Davis",
                    "body": "monitor and headset assigned",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_peripherals_peter2",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_peripherals_peter2",
                    "fields": {
                        "thread_id_nullable": "thread_peripherals_peter2"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "070",
        "instruction": "Handle the inclusion of provisioning notes for cand_5 (Jordan Williams) in the current request conversation. Draft /onboarding/alex_thompson/provisioning_notes.md as text/markdown with 'notes: - slack provisioned as planned '. Attach it to msg_10 using the forthcoming attachment id and assign the email label_1. Log 'linked provisioning notes to msg_10'.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/alex_thompson/provisioning_notes.md",
                    "content_text": "notes:\n- slack provisioned as planned\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_0017",
                    "message_id": "msg_10",
                    "filename": "provisioning_notes.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/alex_thompson/provisioning_notes.md"
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_10",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "linked provisioning notes to msg_10"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "072",
        "instruction": "Coordinate a gentle reminder for cand_2 (Emma Thompson) with a quick status update. Ensure the final record includes a sent email with id msg_nudge_jane to ['emma.thompson@example.com'], utilizing subject 'status check - Emma Thompson' and body 'just checking in', tagged as Onboarding-Reminder (label_2), and associated with the thread 'thread_nudge_jane'.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_nudge_jane",
                    "subject": "status check - Emma Thompson",
                    "body": "just checking in",
                    "to_emails": [
                        "emma.thompson@example.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_nudge_jane",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_nudge_jane",
                    "fields": {
                        "thread_id_nullable": "thread_nudge_jane"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "073",
        "instruction": "Handle a concise checklist reminder for cand_7 (Raj Patel). Utilize /onboarding/robert_singh/pending_tasks.md as text/markdown with '- account setup\n- code repository access\n'. Dispatch msg_reminder_robert2 to ['raj.patel@example.com'] with subject 'pending tasks - Raj Patel' and body 'please complete', labeled label_2. Revise item_15 and item_16 to 'Reminder Sent' with reminder_email_message_id_nullable 'msg_reminder_robert2'.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/robert_singh/pending_tasks.md",
                    "content_text": "- account setup\n- code repository access\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_reminder_robert2",
                    "subject": "pending tasks - Raj Patel",
                    "body": "please complete",
                    "to_emails": [
                        "raj.patel@example.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_reminder_robert2",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_15",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_email_message_id_nullable": "msg_reminder_robert2"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_16",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_email_message_id_nullable": "msg_reminder_robert2"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "074",
        "instruction": "Coordinate a nudge for cand_4 (Sofia Martinez) regarding design access through a reminder and item updates. Issue msg_design_reminder_maria to sofia.martinez@example.com with subject 'pending design access - Sofia Martinez' and body 'please complete', label label_2, modify item_9 and item_10 to 'Reminder Sent', and associate thread_design_reminder_maria.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_design_reminder_maria",
                    "subject": "pending design access - Sofia Martinez",
                    "body": "please complete",
                    "to_emails": [
                        "sofia.martinez@example.com"
                    ],
                    "candidate_id": "cand_4",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_design_reminder_maria",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_9",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_design_reminder_maria"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_10",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_design_reminder_maria"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_design_reminder_maria",
                    "fields": {
                        "thread_id_nullable": "thread_design_reminder_maria"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "075",
        "instruction": "Handle the monitor exchange for cand_3 (William Davis) and notify accordingly. Release MON-LG-001 and allocate MON-DELL-001 to cand_3, then dispatch msg_monitor_swap_peter to it-assets@company.com with subject 'monitor swap - William Davis' and body 'lg to dell', labeled label_1 and attached to thread_monitor_swap_peter. Additionally, log 'swapped monitor for cand_3 from MON-LG-001 to MON-DELL-001'.",
        "actions": [
            {
                "name": "ReleaseInventoryAsset",
                "arguments": {
                    "asset_tag": "MON-LG-001"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "MON-DELL-001",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_monitor_swap_peter",
                    "subject": "monitor swap - William Davis",
                    "body": "lg to dell",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_monitor_swap_peter",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_monitor_swap_peter",
                    "fields": {
                        "thread_id_nullable": "thread_monitor_swap_peter"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "swapped monitor for cand_3 from MON-LG-001 to MON-DELL-001"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "076",
        "instruction": "Coordinate the sending of an updated welcome note for cand_1 (Michael Anderson). Save /onboarding/john_doe/welcome_update.md as text/markdown with '# welcome update\nupdated docs\n', and dispatch msg_welcome_update_john to michael.anderson@example.com with the subject 'welcome update - Michael Anderson' and body 'updated docs', labeled with label_6 and the file attached.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/john_doe/welcome_update.md",
                    "content_text": "# welcome update\nupdated docs\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_welcome_update_john",
                    "subject": "welcome update - Michael Anderson",
                    "body": "updated docs",
                    "to_emails": [
                        "michael.anderson@example.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_welcome_update_john",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_welcome_update_john",
                    "message_id": "msg_welcome_update_john",
                    "filename": "welcome_update.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/john_doe/welcome_update.md"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "077",
        "instruction": "Handle the confirmation of orientation readiness for cand_6 (Lily Zhang) by sending a simple invitation. Dispatch msg_orientation_ready_emily to lily.zhang@example.com with the subject 'orientation ready - Lily Zhang' and body 'access ok', alongside label label_4, and link thread_orientation_ready_emily.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_orientation_ready_emily",
                    "subject": "orientation ready - Lily Zhang",
                    "body": "access ok",
                    "to_emails": [
                        "lily.zhang@example.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_orientation_ready_emily",
                    "label_ids": [
                        "label_4"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_orientation_ready_emily",
                    "fields": {
                        "thread_id_nullable": "thread_orientation_ready_emily"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "078",
        "instruction": "Coordinate the assignment of a docking station for cand_5 (Jordan Williams) and ensure notification. Assign DS-DELL-001 to cand_5. Dispatch msg_dock_alex to it-assets@company.com with the subject 'dock allocation - Jordan Williams' and body 'dock assigned', label label_1, and link thread_dock_alex.",
        "actions": [
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "DS-DELL-001",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_dock_alex",
                    "subject": "dock allocation - Jordan Williams",
                    "body": "dock assigned",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_5",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_dock_alex",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_dock_alex",
                    "fields": {
                        "thread_id_nullable": "thread_dock_alex"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "079",
        "instruction": "Attach phone setup notes for cand_4 (Sofia Martinez) to the current phone request thread. Save /onboarding/maria_rodriguez/phone_setup.md as text/markdown with 'phone setup for maria'. Use the subsequent sequential attachment id to attach it to msg_12, maintain label_1 on the email, and connect to thread_phone_setup_maria.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/maria_rodriguez/phone_setup.md",
                    "content_text": "phone setup for maria",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_0019",
                    "message_id": "msg_12",
                    "filename": "phone_setup.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/maria_rodriguez/phone_setup.md"
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_12",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_12",
                    "fields": {
                        "thread_id_nullable": "thread_phone_setup_maria"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "080",
        "instruction": "Allocate a headset for cand_2 (Emma Thompson) and confirm this via email. Assign HS-BOSE-001 to cand_2. Forward msg_headset_jane to it-assets@company.com with the subject 'headset allocation - Emma Thompson' and message body 'headset assigned', including label_1, and link to thread_headset_jane.",
        "actions": [
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "HS-BOSE-001",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_headset_jane",
                    "subject": "headset allocation - Emma Thompson",
                    "body": "headset assigned",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_headset_jane",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_headset_jane",
                    "fields": {
                        "thread_id_nullable": "thread_headset_jane"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "081",
        "instruction": "Handle the welcome confirmation for cand_1 (Michael Anderson). Use message_id=msg_welcome_confirm_81 with subject 'welcome confirmation - Michael Anderson' and body 'welcome confirmed', to_emails=['michael.anderson@example.com'], label_id=label_6, file_path=/onboarding/john_doe/welcome_confirm.md (text/markdown, '# welcome confirmed\nsee details inside\n'), attach_id=attach_welcome_confirm_81.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/john_doe/welcome_confirm.md",
                    "content_text": "# welcome confirmed\nsee details inside\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_1"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_welcome_confirm_81",
                    "subject": "welcome confirmation - Michael Anderson",
                    "body": "welcome confirmed",
                    "to_emails": [
                        "michael.anderson@example.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_welcome_confirm_81",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_welcome_confirm_81",
                    "message_id": "msg_welcome_confirm_81",
                    "filename": "welcome_confirm.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/john_doe/welcome_confirm.md"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "082",
        "instruction": "Dispatch the orientation invite for cand_2 (Emma Thompson). Preserve /onboarding/jane_smith/orientation_agenda.md as text/markdown with '# orientation agenda\nwelcome and setup\n', and forward msg_orientation_82 to ['emma.thompson@example.com'] using subject 'orientation invite - Emma Thompson' and body 'agenda attached', tagged with label_4 and affixing the agenda.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/jane_smith/orientation_agenda.md",
                    "content_text": "# orientation agenda\nwelcome and setup\n",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_orientation_82",
                    "subject": "orientation invite - Emma Thompson",
                    "body": "agenda attached",
                    "to_emails": [
                        "emma.thompson@example.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_orientation_82",
                    "label_ids": [
                        "label_4"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_orientation_agenda_82",
                    "message_id": "msg_orientation_82",
                    "filename": "orientation_agenda.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/jane_smith/orientation_agenda.md"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "083",
        "instruction": "Handle a manager introduction for cand_3 (William Davis). Utilize message_id=msg_intro_83 with subject 'manager introduction - William Davis' and body 'welcome and intro', to_emails=['william.davis@example.com','mike.nguyen@example.com'], label_id=label_5, thread_id=thread_intro_83. Additionally, tag the candidate with manager_intro_invite_ts 2025-01-01T10:30:00Z.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_intro_83",
                    "subject": "manager introduction - William Davis",
                    "body": "welcome and intro",
                    "to_emails": [
                        "william.davis@example.com",
                        "mike.nguyen@example.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_intro_83",
                    "label_ids": [
                        "label_5"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_intro_83",
                    "fields": {
                        "thread_id_nullable": "thread_intro_83"
                    }
                },
            },
            {
                "name": "SetCandidateFields",
                "arguments": {
                    "candidate_id": "cand_3",
                    "fields": {
                        "manager_intro_invite_ts_nullable": "2025-01-01T10:30:00Z"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "084",
        "instruction": "Coordinate a concise checklist reminder for cand_1 (Michael Anderson). Implement message_id=msg_reminder_84 with subject 'pending items - Michael Anderson' and body 'please complete items', to_emails=['michael.anderson@example.com'], label_id=label_2, thread_id=thread_reminder_84. Set item_3 and item_4 as 'Reminder Sent' with reminder_sent_flag true and reminder_email_message_id_nullable msg_reminder_84.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_reminder_84",
                    "subject": "pending items - Michael Anderson",
                    "body": "please complete items",
                    "to_emails": [
                        "michael.anderson@example.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_reminder_84",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_3",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_reminder_84"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_4",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_reminder_84"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_reminder_84",
                    "fields": {
                        "thread_id_nullable": "thread_reminder_84"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "085",
        "instruction": "Confirm the asset handoff for cand_7 (Raj Patel). The final state consists of the request asset_req_5 marked as Sent with email_message_id msg_assets_handoff_85, a JSON artifact located at /onboarding/robert_singh/asset_request.json containing {'candidate':'cand_7','asset_type':'Laptop','requested_ts':'2024-08-06T14:20:00Z'}, and a record of the sent email msg_assets_handoff_85 to ['it-assets@company.com'] using subject 'asset handoff - Raj Patel' and body 'handoff confirmed', tagged as Asset-Request (label_1).",
        "actions": [
            {
                "name": "UpsertJsonArtifact",
                "arguments": {
                    "file_path": "/onboarding/robert_singh/asset_request.json",
                    "content_obj": {
                        "candidate": "cand_7",
                        "asset_type": "Laptop",
                        "requested_ts": "2024-08-06T14:20:00Z"
                    },
                    "candidate_id": "cand_7"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_assets_handoff_85",
                    "subject": "asset handoff - Raj Patel",
                    "body": "handoff confirmed",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_assets_handoff_85",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateAssetRequest",
                "arguments": {
                    "request_id": "asset_req_5",
                    "fields": {
                        "status": "Sent",
                        "email_message_id_nullable": "msg_assets_handoff_85"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "086",
        "instruction": "Verify phone allocation for cand_4 (Sofia Martinez). Utilize asset_tag=PH-IPHONE-002 for assignment to cand_4, message_id=msg_phone_alloc_86 with subject 'phone allocation - Sofia Martinez' and body 'iphone assigned', to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_phone_alloc_86.",
        "actions": [
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "PH-IPHONE-002",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_phone_alloc_86",
                    "subject": "phone allocation - Sofia Martinez",
                    "body": "iphone assigned",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_4",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_phone_alloc_86",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_phone_alloc_86",
                    "fields": {
                        "thread_id_nullable": "thread_phone_alloc_86"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "phone PH-IPHONE-002 assigned to cand_4"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "087",
        "instruction": "Compile an access summary for cand_2 (Emma Thompson) and inform support. Checks: ('Slack','Pass','ok'), ('GitHub','Pending','awaiting sso'). Utilize message_id=msg_access_summary_87 with subject 'access summary - Emma Thompson' and body 'status included', to_emails=['it-support@company.com'], label_id=label_7.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_2",
                    "system_name": "Slack",
                    "status": "Pass",
                    "note_nullable": "ok"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_2",
                    "system_name": "GitHub",
                    "status": "Pending",
                    "note_nullable": "awaiting sso"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_access_summary_87",
                    "subject": "access summary - Emma Thompson",
                    "body": "status included",
                    "to_emails": [
                        "it-support@company.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_access_summary_87",
                    "label_ids": [
                        "label_7"
                    ]
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "088",
        "instruction": "Dispatch a week-one reminder for cand_5 (Jordan Williams). Utilize message_id=msg_week1_88 with subject 'pending items - Jordan Williams' and body 'please review', to_emails=['jordan.williams@example.com'], label_id=label_2, thread_id=thread_week1_88. Set item_13 and item_14 to 'Reminder Sent' with reminder_sent_flag true and reminder_email_message_id_nullable msg_week1_88.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_week1_88",
                    "subject": "pending items - Jordan Williams",
                    "body": "please review",
                    "to_emails": [
                        "jordan.williams@example.com"
                    ],
                    "candidate_id": "cand_5",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_week1_88",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_13",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_week1_88"
                    }
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_14",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_week1_88"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_week1_88",
                    "fields": {
                        "thread_id_nullable": "thread_week1_88"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "089",
        "instruction": "Handle a laptop exchange for cand_3 (William Davis) from LT-DELL-002 to LT-MBP-002 and inform it assets. Utilize message_id=msg_swap_89 with subject 'asset swap - William Davis' and content 'dell to mbp', directing it to ['it-assets@company.com'], label_id=label_1, thread_id=thread_swap_89.",
        "actions": [
            {
                "name": "ReleaseInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-002"
                },
            },
            {
                "name": "AssignInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-MBP-002",
                    "candidate_id": "cand_3"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_swap_89",
                    "subject": "asset swap - William Davis",
                    "body": "dell to mbp",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_swap_89",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_swap_89",
                    "fields": {
                        "thread_id_nullable": "thread_swap_89"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "090",
        "instruction": "Coordinate policy delivery for cand_2 (Emma Thompson). Employ /onboarding/jane_smith/company_policies_note.md as text/markdown with the instruction 'please review the policies'. Dispatch msg_policy_90 to ['emma.thompson@example.com'] with subject 'policies - Emma Thompson' and content 'please review', assigning label_6, and attach the note using attachment_id attach_0021.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/jane_smith/company_policies_note.md",
                    "content_text": "please review the policies",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_2"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_policy_90",
                    "subject": "policies - Emma Thompson",
                    "body": "please review",
                    "to_emails": [
                        "emma.thompson@example.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_policy_90",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_0021",
                    "message_id": "msg_policy_90",
                    "filename": "company_policies_note.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/jane_smith/company_policies_note.md"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "091",
        "instruction": "Handle sending a benefits reminder for cand_6 (Lily Zhang). Utilize message_id=msg_benefits_91 with subject 'benefits enrollment - Lily Zhang' and body 'enroll by friday', to_emails=['lily.zhang@example.com'], label_id=label_2, thread_id=thread_benefits_91.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_benefits_91",
                    "subject": "benefits enrollment - Lily Zhang",
                    "body": "enroll by friday",
                    "to_emails": [
                        "lily.zhang@example.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_benefits_91",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_benefits_91",
                    "fields": {
                        "thread_id_nullable": "thread_benefits_91"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "092",
        "instruction": "Coordinate the confirmation of desk peripherals for cand_5 (Jordan Williams) and inform it assets. Apply message_id=msg_peripherals_92 with subject 'desk peripherals - Jordan Williams' and body 'monitor and dock set', to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_peripherals_92. Include a brief log 'peripherals confirmed for cand_5'.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_peripherals_92",
                    "subject": "desk peripherals - Jordan Williams",
                    "body": "monitor and dock set",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_5",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_peripherals_92",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_peripherals_92",
                    "fields": {
                        "thread_id_nullable": "thread_peripherals_92"
                    }
                },
            },
            {
                "name": "InsertTerminalLog",
                "arguments": {
                    "message_text": "peripherals confirmed for cand_5"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "093",
        "instruction": "Handle a brief welcome check-in for cand_4 (Sofia Martinez) and record the outreach in a concise file. Utilize message_id=msg_checkin_93 with subject 'welcome check-in - Sofia Martinez' and body 'how is the first week going', to_emails=['sofia.martinez@example.com'], label_id=label_6, thread_id=thread_checkin_93, and save as text/markdown at /onboarding/maria_rodriguez/checkin_93.md with 'check-in sent for week-1'.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/maria_rodriguez/checkin_93.md",
                    "content_text": "check-in sent for week-1",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_4"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_checkin_93",
                    "subject": "welcome check-in - Sofia Martinez",
                    "body": "how is the first week going",
                    "to_emails": [
                        "sofia.martinez@example.com"
                    ],
                    "candidate_id": "cand_4",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_checkin_93",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_checkin_93",
                    "fields": {
                        "thread_id_nullable": "thread_checkin_93"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "094",
        "instruction": "Inform support about the final access for cand_3 (William Davis). Verify: ('Email','Pass','ok'), ('SSO','Pass','ok'). Use message_id=msg_access_final_94 with subject 'access final - William Davis' and body 'all set', to_emails=['it-support@company.com'], label_id=label_7.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_3",
                    "system_name": "Email",
                    "status": "Pass",
                    "note_nullable": "ok"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_3",
                    "system_name": "SSO",
                    "status": "Pass",
                    "note_nullable": "ok"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_access_final_94",
                    "subject": "access final - William Davis",
                    "body": "all set",
                    "to_emails": [
                        "it-support@company.com"
                    ],
                    "candidate_id": "cand_3",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_access_final_94",
                    "label_ids": [
                        "label_7"
                    ]
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "095",
        "instruction": "Handle a benefits follow-up for cand_1 (Michael Anderson). Apply message_id=msg_benefits_95 with subject 'benefits follow-up - Michael Anderson' and body 'please finish enrollment', to_emails=['michael.anderson@example.com'], label_id=label_2, thread_id=thread_benefits_95.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_benefits_95",
                    "subject": "benefits follow-up - Michael Anderson",
                    "body": "please finish enrollment",
                    "to_emails": [
                        "michael.anderson@example.com"
                    ],
                    "candidate_id": "cand_1",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_benefits_95",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_benefits_95",
                    "fields": {
                        "thread_id_nullable": "thread_benefits_95"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "096",
        "instruction": "Coordinate asset return confirmation for cand_2 (Emma Thompson) of LT-DELL-003 and inform it assets. Implement message_id=msg_asset_return_96 with subject 'asset return - Emma Thompson' and body 'device received', to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_asset_return_96.",
        "actions": [
            {
                "name": "ReleaseInventoryAsset",
                "arguments": {
                    "asset_tag": "LT-DELL-003"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_asset_return_96",
                    "subject": "asset return - Emma Thompson",
                    "body": "device received",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_2",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_asset_return_96",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_asset_return_96",
                    "fields": {
                        "thread_id_nullable": "thread_asset_return_96"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "097",
        "instruction": "Handle an onboarding reminder for cand_6 (Lily Zhang). Apply message_id=msg_reminder_97 with subject 'onboarding reminder - Lily Zhang' and body 'please finish tasks', to_emails=['lily.zhang@example.com'], label_id=label_2, thread_id=thread_reminder_97. Mark item_15 as 'Reminder Sent' with reminder_sent_flag set to true and reminder_email_message_id_nullable as msg_reminder_97.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_reminder_97",
                    "subject": "onboarding reminder - Lily Zhang",
                    "body": "please finish tasks",
                    "to_emails": [
                        "lily.zhang@example.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_reminder_97",
                    "label_ids": [
                        "label_2"
                    ]
                },
            },
            {
                "name": "UpdateChecklistItem",
                "arguments": {
                    "item_id": "item_15",
                    "fields": {
                        "status": "Reminder Sent",
                        "reminder_sent_flag": true,
                        "reminder_email_message_id_nullable": "msg_reminder_97"
                    }
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_reminder_97",
                    "fields": {
                        "thread_id_nullable": "thread_reminder_97"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "098",
        "instruction": "Coordinate the final welcome for cand_5 (Jordan Williams). Generate /onboarding/alex_thompson/welcome_resources.md as text/markdown with 'resources and links', and convey msg_welcome_final_98 to jordan.williams@example.com, using subject 'welcome final - Jordan Williams' and body 'see resources', labeled under label_6, including that file.",
        "actions": [
            {
                "name": "UpsertOnboardingFile",
                "arguments": {
                    "file_path": "/onboarding/alex_thompson/welcome_resources.md",
                    "content_text": "resources and links",
                    "mime_type": "text/markdown",
                    "candidate_id": "cand_5"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_welcome_final_98",
                    "subject": "welcome final - Jordan Williams",
                    "body": "see resources",
                    "to_emails": [
                        "jordan.williams@example.com"
                    ],
                    "candidate_id": "cand_5",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_welcome_final_98",
                    "label_ids": [
                        "label_6"
                    ]
                },
            },
            {
                "name": "InsertAttachmentRecord",
                "arguments": {
                    "attachment_id": "attach_welcome_resources_98",
                    "message_id": "msg_welcome_final_98",
                    "filename": "welcome_resources.md",
                    "mime_type": "text/markdown",
                    "file_path": "/onboarding/alex_thompson/welcome_resources.md"
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "099",
        "instruction": "Handle a concise systems verification for cand_7 (Raj Patel). Verification details: ('Email','Pass','ok'), ('Slack','Pass','ok'). Utilize message_id=msg_systems_check_99 with subject 'systems check - Raj Patel' and content 'ready to go', to_emails=['it-support@company.com'], label_id=label_7.",
        "actions": [
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_7",
                    "system_name": "Email",
                    "status": "Pass",
                    "note_nullable": "ok"
                },
            },
            {
                "name": "InsertAccessCheck",
                "arguments": {
                    "candidate_id": "cand_7",
                    "system_name": "Slack",
                    "status": "Pass",
                    "note_nullable": "ok"
                },
            },
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_systems_check_99",
                    "subject": "systems check - Raj Patel",
                    "body": "ready to go",
                    "to_emails": [
                        "it-support@company.com"
                    ],
                    "candidate_id": "cand_7",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_systems_check_99",
                    "label_ids": [
                        "label_7"
                    ]
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
    ,
    {
        "annotator": v2,
        "user_id": "100",
        "instruction": "Coordinate laptop collection confirmation for cand_6 (Lily Zhang) and alert it assets. Utilize message_id=msg_pickup_100 with subject 'laptop pickup - Lily Zhang' and message 'scheduled 10am', to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_pickup_100.",
        "actions": [
            {
                "name": "InsertEmail",
                "arguments": {
                    "message_id": "msg_pickup_100",
                    "subject": "laptop pickup - Lily Zhang",
                    "body": "scheduled 10am",
                    "to_emails": [
                        "it-assets@company.com"
                    ],
                    "candidate_id": "cand_6",
                    "draft_flag": false,
                    "sent_flag": true
                },
            },
            {
                "name": "AddLabelsToEmail",
                "arguments": {
                    "message_id": "msg_pickup_100",
                    "label_ids": [
                        "label_1"
                    ]
                },
            },
            {
                "name": "UpdateEmailMetadata",
                "arguments": {
                    "message_id": "msg_pickup_100",
                    "fields": {
                        "thread_id_nullable": "thread_pickup_100"
                    }
                }
            }
        ],
        "outputs": [
                "ok"
        ]
    }
]
