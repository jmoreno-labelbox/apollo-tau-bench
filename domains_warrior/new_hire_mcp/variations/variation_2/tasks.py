from domains.dto import Task, Action

TASKS = [
Task(
        annotator="v2",
        user_id="032",
        instruction=(
            "You notify it assets about asset provisioning for cand_7 (robert singh) and keep the request record consistent. "
            "You maintain /onboarding/robert_singh/asset_request.json with {'candidate':'cand_7','asset_type':'Laptop','requested_ts':'2024-08-06T14:20:00Z'}. "
            "You send msg_assets_robert_v2 to ['it-assets@company.com'] with subject 'asset provisioning - robert singh' and body 'see attached', labeled label_1, link the email under thread_assets_robert_v2, and set asset_req_5 to Sent with email_message_id msg_assets_robert_v2. "
            "You add a brief terminal note."
        ),
        actions=[
            Action(name="upsert_json_artifact", kwargs={"file_path": "/onboarding/robert_singh/asset_request.json",
                                                        "content_obj": {"candidate": "cand_7", "asset_type": "Laptop",
                                                                        "requested_ts": "2024-08-06T14:20:00Z"},
                                                        "candidate_id": "cand_7"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_assets_robert_v2", "subject": "asset provisioning - robert singh",
                           "body": "see attached", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_7",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_assets_robert_v2", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_assets_robert_v2",
                                                         "fields": {"thread_id_nullable": "thread_assets_robert_v2"}}),
            Action(name="update_asset_request", kwargs={"request_id": "asset_req_5", "fields": {"status": "Sent",
                                                                                                "email_message_id_nullable": "msg_assets_robert_v2"}}),
            Action(name="insert_terminal_log",
                   kwargs={"message_text": "sent asset provisioning notice for cand_7 with asset_req_5"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="071",
        instruction=(
            "You complete a welcome confirmation for cand_4 (maria rodriguez) with a labeled email and attachments. "
            "You save /onboarding/maria_rodriguez/welcome_confirm.md as text/markdown with '# welcome confirmed\nsee details inside\n'. "
            "You send msg_welcome_confirm_maria to maria.rodriguez@example.com with subject 'welcome confirmation - maria rodriguez' and body 'welcome confirmed', label label_6, "
            "attach welcome_confirm.md and the PDFs Company-Policies.pdf and Benefits-Guide.pdf from /onboarding/maria_rodriguez/, and link thread_welcome_confirm_maria."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/maria_rodriguez/welcome_confirm.md",
                                                          "content_text": "# welcome confirmed\nsee details inside\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_4"}),
            Action(name="insert_email", kwargs={"message_id": "msg_welcome_confirm_maria",
                                                "subject": "welcome confirmation - maria rodriguez",
                                                "body": "welcome confirmed",
                                                "to_emails": ["maria.rodriguez@example.com"], "candidate_id": "cand_4",
                                                "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_welcome_confirm_maria", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_welcome_confirm_maria", "message_id": "msg_welcome_confirm_maria",
                           "filename": "welcome_confirm.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/maria_rodriguez/welcome_confirm.md"}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_maria_policies_pdf", "message_id": "msg_welcome_confirm_maria",
                           "filename": "Company-Policies.pdf", "mime_type": "application/pdf",
                           "file_path": "/onboarding/maria_rodriguez/Company-Policies.pdf"}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_maria_benefits_pdf", "message_id": "msg_welcome_confirm_maria",
                           "filename": "Benefits-Guide.pdf", "mime_type": "application/pdf",
                           "file_path": "/onboarding/maria_rodriguez/Benefits-Guide.pdf"}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_welcome_confirm_maria", "fields": {
                "thread_id_nullable": "thread_welcome_confirm_maria"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="060",
        instruction=(
            "You resend the policy pack for cand_1 (john doe). You create /onboarding/john_doe/policy_pack_v2.md as text/markdown with '# policy pack v2\\n', "
            "and you send msg_policy_pack_resend_john to john.doe@example.com using subject 'policy pack (resend) - john doe' and body 'see updated pack', labeled with label_6 and attaching the file."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/john_doe/policy_pack_v2.md", "content_text": "# policy pack v2\n",
                           "mime_type": "text/markdown", "candidate_id": "cand_1"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_policy_pack_resend_john", "subject": "policy pack (resend) - john doe",
                           "body": "see updated pack", "to_emails": ["john.doe@example.com"], "candidate_id": "cand_1",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_policy_pack_resend_john", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record", kwargs={"attachment_id": "attach_policy_pack_resend_john",
                                                            "message_id": "msg_policy_pack_resend_john",
                                                            "filename": "policy_pack_v2.md",
                                                            "mime_type": "text/markdown",
                                                            "file_path": "/onboarding/john_doe/policy_pack_v2.md"}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "send_policy_pack_resend",
                                                        "params_json": {"message_id": "msg_policy_pack_resend_john"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="056",
        instruction=(
            "You confirm desk setup for cand_5 (alex thompson). Final state: a sent email record "
            "msg_desk_setup_alex to it-assets@company.com with subject 'desk setup - alex thompson' and body "
            "'monitor and dock confirmed', labeled label_1 and associated with thread_desk_setup_alex; a terminal "
            "log exists with the exact text 'desk setup confirmed for cand_5 with peripherals'; checklist item "
            "item_11 is 'Completed' with updated_ts 2025-01-01T09:00:00Z; and an audit entry references "
            "msg_desk_setup_alex."
        ),
        actions=[
            Action(name="insert_email", kwargs={
                "message_id": "msg_desk_setup_alex",
                "subject": "desk setup - alex thompson",
                "body": "monitor and dock confirmed",
                "to_emails": ["it-assets@company.com"],
                "candidate_id": "cand_5",
                "draft_flag": False,
                "sent_flag": True
            }),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_desk_setup_alex", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={
                "message_id": "msg_desk_setup_alex",
                "fields": {"thread_id_nullable": "thread_desk_setup_alex"}
            }),
            Action(name="insert_terminal_log",
                   kwargs={"message_text": "desk setup confirmed for cand_5 with peripherals"}),
            Action(name="update_checklist_item", kwargs={
                "item_id": "item_11",
                "fields": {"status": "Completed", "updated_ts": "2025-01-01T09:00:00Z"}
            }),
            Action(name="record_mcp_tool_call", kwargs={
                "server_name": "gmail",
                "tool_name": "notify_desk_setup",
                "params_json": {"message_id": "msg_desk_setup_alex"}
            }),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="048",
        instruction=(
            "You run the manager-intro confirmation for cand_1 (john doe). "
            "Provide parameters: note_path=/onboarding/john_doe/manager_intro_note.md, note_mime=text/markdown, note_content='intro prepared', "
            "message_id=msg_manager_intro_john_2, subject='manager intro - john doe', body='intro sent', to_emails=['john.doe@example.com'], "
            "label_id=label_5, attach_id=attach_manager_intro_note_john_2, attach_filename=manager_intro_note.md, attach_mime=text/markdown, "
            "thread_id=thread_manager_intro_john_2, audit={'server_name':'gmail','tool_name':'send_manager_intro_john','params_json':{'message_id':'msg_manager_intro_john_2'}}."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/john_doe/manager_intro_note.md",
                                                          "content_text": "intro prepared\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_1"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_manager_intro_john_2", "subject": "manager intro - john doe",
                           "body": "intro sent", "to_emails": ["john.doe@example.com"], "candidate_id": "cand_1",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_manager_intro_john_2", "label_ids": ["label_5"]}),
            Action(name="insert_attachment_record", kwargs={"attachment_id": "attach_manager_intro_note_john_2",
                                                            "message_id": "msg_manager_intro_john_2",
                                                            "filename": "manager_intro_note.md",
                                                            "mime_type": "text/markdown",
                                                            "file_path": "/onboarding/john_doe/manager_intro_note.md"}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_manager_intro_john_2", "fields": {
                "thread_id_nullable": "thread_manager_intro_john_2"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "send_manager_intro_john",
                                                        "params_json": {"message_id": "msg_manager_intro_john_2"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="013",
        instruction=(
            "You confirm access clearance for cand_4 (maria rodriguez). Final state: successes are recorded for "
            "Email, SSO, and Slack; a markdown file exists at /onboarding/maria_rodriguez/access_clearance.md with "
            "exact content 'email: success\\nsso: success\\nslack: success\\n'; a sent email record "
            "msg_access_clear_maria to david.kim@example.com with subject 'access clearance - maria rodriguez' and "
            "body 'all critical systems ready', labeled label_3 and carrying the access_clearance.md attachment "
            "from that path."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_4", "system_name": "Email", "status": "Success"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_4", "system_name": "SSO", "status": "Success"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_4", "system_name": "Slack", "status": "Success"}),
            Action(name="upsert_onboarding_file", kwargs={
                "file_path": "/onboarding/maria_rodriguez/access_clearance.md",
                "content_text": "email: success\nsso: success\nslack: success\n",
                "mime_type": "text/markdown",
                "candidate_id": "cand_4"
            }),
            Action(name="insert_email", kwargs={
                "message_id": "msg_access_clear_maria",
                "subject": "access clearance - maria rodriguez",
                "body": "all critical systems ready",
                "to_emails": ["david.kim@example.com"],
                "candidate_id": "cand_4",
                "draft_flag": False,
                "sent_flag": True
            }),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_access_clear_maria", "label_ids": ["label_3"]}),
            Action(name="insert_attachment_record", kwargs={
                "attachment_id": "attach_0020",
                "message_id": "msg_access_clear_maria",
                "filename": "access_clearance.md",
                "mime_type": "text/markdown",
                "file_path": "/onboarding/maria_rodriguez/access_clearance.md"
            }),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="047",
        instruction=(
            "You run the orientation-finalization protocol for cand_5 (alex thompson). "
            "Provide parameters: agenda_path=/onboarding/alex_thompson/orientation_agenda_2.md, agenda_mime=text/markdown, agenda_content='# orientation agenda\\nwelcome and access\\n', "
            "message_id=msg_orientation_alex_2, subject='day-1 orientation - alex thompson', body='agenda attached', to_emails=['alex.thompson@example.com'], "
            "label_id=label_4, attach_id=attach_orientation_agenda_alex_2, attach_filename=orientation_agenda_2.md, attach_mime=text/markdown, "
            "thread_id=thread_orientation_alex_2, audit={'server_name':'gmail','tool_name':'send_orientation_alex','params_json':{'message_id':'msg_orientation_alex_2'}}."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/alex_thompson/orientation_agenda_2.md",
                           "content_text": "# orientation agenda\nwelcome and access\n", "mime_type": "text/markdown",
                           "candidate_id": "cand_5"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_orientation_alex_2", "subject": "day-1 orientation - alex thompson",
                           "body": "agenda attached", "to_emails": ["alex.thompson@example.com"],
                           "candidate_id": "cand_5", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_orientation_alex_2", "label_ids": ["label_4"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_orientation_agenda_alex_2", "message_id": "msg_orientation_alex_2",
                           "filename": "orientation_agenda_2.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/alex_thompson/orientation_agenda_2.md"}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_orientation_alex_2", "fields": {
                "thread_id_nullable": "thread_orientation_alex_2"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "send_orientation_alex",
                                                        "params_json": {"message_id": "msg_orientation_alex_2"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="020",
        instruction=(
            "You execute the access-gap notification protocol for cand_7 (robert singh) regarding vpn. "
            "Provide parameters: check=('VPN','Pending','pending account provisioning'); "
            "gap_path=/onboarding/robert_singh/vpn_gap.md, gap_mime=text/markdown, gap_content='vpn: pending - pending account provisioning'; "
            "notify_email={message_id:msg_vpn_gap_robert, to:['it-support@company.com'], subject:'Access Gap - VPN - Robert Singh', body:'see attached', label_id:label_3, thread_id:thread_vpn_gap_robert}; "
            "attach_filename=vpn_gap.md; "
            "audit={'server_name':'gmail','tool_name':'notify_vpn_gap_robert','params_json':{'message_id':'msg_vpn_gap_robert'}}."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_7", "system_name": "VPN", "status": "Pending",
                           "note_nullable": "pending account provisioning"}),
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/robert_singh/vpn_gap.md",
                                                          "content_text": "vpn: pending - pending account provisioning",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_7"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_vpn_gap_robert", "subject": "Access Gap - VPN - Robert Singh",
                           "body": "see attached", "to_emails": ["it-support@company.com"], "candidate_id": "cand_7",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_vpn_gap_robert", "label_ids": ["label_3"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_vpn_gap_robert", "message_id": "msg_vpn_gap_robert",
                           "filename": "vpn_gap.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/robert_singh/vpn_gap.md"}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_vpn_gap_robert",
                                                         "fields": {"thread_id_nullable": "thread_vpn_gap_robert"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "notify_vpn_gap_robert",
                                                        "params_json": {"message_id": "msg_vpn_gap_robert"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="009",
        instruction=(
            "You ready cand_6 (emily chen) for orientation: record email/sso/slack as success and marketing platform as pending with note 'pending vendor activation'; "
            "write /onboarding/emily_chen/orientation_agenda.md as text/markdown with '# orientation agenda\\nwelcome and access\\n'; "
            "send a labeled invite (msg_orientation_emily) to ['emily.chen@example.com'] with subject 'day-1 orientation - emily chen' and body 'agenda attached', attaching that agenda; "
            "set orientation_invite_ts to 2024-08-23T09:30:00Z."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_6", "system_name": "Email", "status": "Success"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_6", "system_name": "SSO", "status": "Success"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_6", "system_name": "Slack", "status": "Success"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_6", "system_name": "Marketing Platform", "status": "Pending",
                           "note_nullable": "pending vendor activation"}),
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/emily_chen/orientation_agenda.md",
                                                          "content_text": "# orientation agenda\nwelcome and access\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_6"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_orientation_emily", "subject": "day-1 orientation - emily chen",
                           "body": "agenda attached", "to_emails": ["emily.chen@example.com"], "candidate_id": "cand_6",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_orientation_emily", "label_ids": ["label_4"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_0022", "message_id": "msg_orientation_emily",
                           "filename": "orientation_agenda.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/emily_chen/orientation_agenda.md"}),
            Action(name="set_candidate_fields", kwargs={"candidate_id": "cand_6",
                                                        "fields": {
                                                            "orientation_invite_ts_nullable": "2024-08-23T09:30:00Z"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="030",
        instruction=(
            "You perform the monitor allocation protocol for cand_7 (robert singh). "
            "Provide parameters: asset_tag=MON-DELL-002, "
            "message_id=msg_monitor_alloc_robert, subject='monitor allocation - robert singh', body='monitor assigned', "
            "to_emails=['it-assets@company.com'], "
            "label_name='Asset-Request', label_id='label_1', "
            "thread_id=thread_monitor_alloc_robert."
        ),
        actions=[
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "MON-DELL-002", "candidate_id": "cand_7"}),
            Action(name="create_or_get_email_label", kwargs={"name": "Asset-Request"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_monitor_alloc_robert", "subject": "monitor allocation - robert singh",
                           "body": "monitor assigned", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_7",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_monitor_alloc_robert", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_monitor_alloc_robert", "fields": {
                "thread_id_nullable": "thread_monitor_alloc_robert"}}),
            Action(name="insert_terminal_log", kwargs={"message_text": "allocated MON-DELL-002 to cand_7"}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "notify_monitor_alloc",
                                                        "params_json": {"message_id": "msg_monitor_alloc_robert"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="031",
        instruction=(
            "You initiate the welcome-packet protocol for cand_6 (emily chen). "
            "Provide parameters: welcome_md_path=/onboarding/emily_chen/welcome_emily_chen.md, welcome_md_mime=text/markdown, "
            "welcome_md_content='# welcome emily\\nstart date: 2024-08-23\\n', "
            "welcome_email={message_id:msg_welcome_emily, to:['emily.chen@example.com'], subject:'welcome to the team - emily chen', body:'welcome!', label_id:label_6}, "
            "thread_id=thread_welcome_emily, "
            "candidate_update={onboarding_status:'Packet Sent', welcome_email_message_id_nullable:'msg_welcome_emily'}."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/emily_chen/welcome_emily_chen.md",
                                                          "content_text": "# welcome emily\nstart date: 2024-08-23\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_6"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_welcome_emily", "subject": "welcome to the team - emily chen",
                           "body": "welcome!", "to_emails": ["emily.chen@example.com"], "candidate_id": "cand_6",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_welcome_emily", "label_ids": ["label_6"]}),
            Action(name="set_candidate_fields", kwargs={"candidate_id": "cand_6",
                                                        "fields": {"onboarding_status": "Packet Sent",
                                                                   "welcome_email_message_id_nullable": "msg_welcome_emily"}}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_welcome_emily",
                                                         "fields": {"thread_id_nullable": "thread_welcome_emily"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="024",
        instruction=(
            "You trigger the access-gap notification protocol for cand_2 (jane smith) regarding vpn onboarding. "
            "Provide parameters: "
            "checks=[('VPN','Pending','awaiting network group')], "
            "summary_path=/onboarding/jane_smith/vpn_gap.md, summary_mime=text/markdown, summary_lines=['VPN: Pending - awaiting network group'], "
            "message_id=msg_vpn_gap_jane, subject='access gap - jane smith', body='see vpn details', "
            "to_emails=['it-support@company.com'], "
            "label_name='Access-Issues', label_id='label_3', "
            "attach_id=attach_vpn_gap_jane, attach_filename=vpn_gap.md, attach_mime=text/markdown, "
            "thread_id=thread_vpn_gap_jane."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_2", "system_name": "VPN", "status": "Pending",
                           "note_nullable": "awaiting network group"}),
            Action(name="create_access_gap_summary_file", kwargs={"file_path": "/onboarding/jane_smith/vpn_gap.md",
                                                                  "content_lines": [
                                                                      "VPN: Pending - awaiting network group"],
                                                                  "candidate_id": "cand_2"}),
            Action(name="create_or_get_email_label", kwargs={"name": "Access-Issues"}),
            Action(name="insert_email", kwargs={"message_id": "msg_vpn_gap_jane", "subject": "access gap - jane smith",
                                                "body": "see vpn details", "to_emails": ["it-support@company.com"],
                                                "candidate_id": "cand_2", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_vpn_gap_jane", "label_ids": ["label_3"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_vpn_gap_jane", "message_id": "msg_vpn_gap_jane",
                           "filename": "vpn_gap.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/jane_smith/vpn_gap.md"}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_vpn_gap_jane", "fields": {"thread_id_nullable": "thread_vpn_gap_jane"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="101",
        instruction=(
            "You send a brief checklist reminder for cand_2 (jane smith). "
            "Create /onboarding/jane_smith/pending_tasks_101.md as text/markdown with '- benefits enrollment\\n- security training\\n'. "
            "Send msg_reminder_jane_101 to jane.smith@example.com with subject 'pending tasks - jane smith' and body 'please complete', "
            "apply label_id=label_2, and update item_5 and item_6 to 'Reminder Sent' referencing msg_reminder_jane_101."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/jane_smith/pending_tasks_101.md",
                                                          "content_text": "- benefits enrollment\n- security training\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_2"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_reminder_jane_101", "subject": "pending tasks - jane smith",
                           "body": "please complete", "to_emails": ["jane.smith@example.com"], "candidate_id": "cand_2",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_reminder_jane_101", "label_ids": ["label_2"]}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_5", "fields": {"status": "Reminder Sent",
                                                                                         "reminder_email_message_id_nullable": "msg_reminder_jane_101"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_6", "fields": {"status": "Reminder Sent",
                                                                                         "reminder_email_message_id_nullable": "msg_reminder_jane_101"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="008",
        instruction=(
            "You complete a laptop swap for cand_2 (jane smith) from LT-DELL-003 to LT-MBP-002 and notify it-assets. "
            "Final state: LT-DELL-003 is released; LT-MBP-002 is assigned to cand_2; asset_req_1 reflects asset_tag_nullable 'LT-MBP-002'; "
            "a terminal note exists with message exactly 'swap cand_2 LT-DELL-003->LT-MBP-002'; a sent email record msg_asset_swap_jane goes to "
            "['it-assets@company.com'] with subject 'Asset Swap - Jane Smith' and body 'Dell to MBP', labeled with label_1; "
            "an MCP audit entry exists with server_name 'gmail', tool_name 'asset_swap_notice_jane', and params_json {'message_id':'msg_asset_swap_jane'}."
        ),
        actions=[
            Action(name="release_inventory_asset", kwargs={"asset_tag": "LT-DELL-003"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "LT-MBP-002", "candidate_id": "cand_2"}),
            Action(name="update_asset_request",
                   kwargs={"request_id": "asset_req_1", "fields": {"asset_tag_nullable": "LT-MBP-002"}}),
            Action(name="insert_terminal_log",
                   kwargs={"message_text": "swap cand_2 LT-DELL-003->LT-MBP-002"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_asset_swap_jane", "subject": "Asset Swap - Jane Smith",
                           "body": "Dell to MBP", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_2",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_asset_swap_jane", "label_ids": ["label_1"]}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "asset_swap_notice_jane",
                                                        "params_json": {"message_id": "msg_asset_swap_jane"}}),
        ],
        outputs=["ok"],
    ),

    Task(
        annotator="v2",
        user_id="041",
        instruction=(
            "You Confirm welcome for cand_1 (john doe). Final state: a note exists at "
            "/onboarding/john_doe/welcome_confirm.md with exactly '# welcome confirmed\nsee details inside\n'; "
            "a sent email record msg_welcome_confirm_john to john.doe@example.com with subject 'welcome confirmation - john doe' "
            "and body 'welcome confirmed', labeled label_6 and associated with thread_welcome_confirm_john; the email includes "
            "attachment welcome_confirm.md sourced from that note; an MCP audit entry exists with server_name 'gmail', "
            "tool_name 'send_welcome_confirm_john', and params_json {'message_id':'msg_welcome_confirm_john'}."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/john_doe/welcome_confirm.md",
                                                          "content_text": "# welcome confirmed\nsee details inside\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_1"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_welcome_confirm_john", "subject": "welcome confirmation - john doe",
                           "body": "welcome confirmed", "to_emails": ["john.doe@example.com"], "candidate_id": "cand_1",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_welcome_confirm_john", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_welcome_confirm_john", "message_id": "msg_welcome_confirm_john",
                           "filename": "welcome_confirm.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/john_doe/welcome_confirm.md"}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_welcome_confirm_john", "fields": {
                "thread_id_nullable": "thread_welcome_confirm_john"}}),
            Action(name="record_mcp_tool_call",
                   kwargs={"server_name": "gmail", "tool_name": "send_welcome_confirm_john",
                           "params_json": {"message_id": "msg_welcome_confirm_john"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="042",
        instruction=(
            "You Complete the asset-provisioning handoff for cand_7 (robert singh). Final state: "
            "/onboarding/robert_singh/asset_request.json contains {'candidate':'cand_7','asset_type':'Laptop','requested_ts':'2024-08-06T14:20:00Z'}; "
            "a sent email record msg_assets_handoff_robert to it-assets@company.com with subject 'asset provisioning handoff - robert singh' "
            "and body 'handoff sent', labeled label_1 and associated with thread_assets_handoff_robert; asset_req_5 shows status 'Sent' and "
            "references msg_assets_handoff_robert; an audit entry exists that references msg_assets_handoff_robert."
        ),
        actions=[
            Action(name="upsert_json_artifact", kwargs={"file_path": "/onboarding/robert_singh/asset_request.json",
                                                        "content_obj": {"candidate": "cand_7", "asset_type": "Laptop",
                                                                        "requested_ts": "2024-08-06T14:20:00Z"},
                                                        "candidate_id": "cand_7"}),
            Action(name="insert_email", kwargs={"message_id": "msg_assets_handoff_robert",
                                                "subject": "asset provisioning handoff - robert singh",
                                                "body": "handoff sent", "to_emails": ["it-assets@company.com"],
                                                "candidate_id": "cand_7", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_assets_handoff_robert", "label_ids": ["label_1"]}),
            Action(name="update_asset_request", kwargs={"request_id": "asset_req_5", "fields": {"status": "Sent",
                                                                                                "email_message_id_nullable": "msg_assets_handoff_robert"}}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_assets_handoff_robert", "fields": {
                "thread_id_nullable": "thread_assets_handoff_robert"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "asset_provision_handoff",
                                                        "params_json": {"message_id": "msg_assets_handoff_robert"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="043",
        instruction=(
            "You run the access-gap alert protocol for cand_4 (maria rodriguez). "
            "Provide parameters: checks=[('Email','Failed','exchange outage'),('SSO','Failed','idp sync pending')], "
            "summary_path=/onboarding/maria_rodriguez/access_gaps_2.md, summary_mime=text/markdown, summary_lines=['Email: Failed - exchange outage','SSO: Failed - idp sync pending'], "
            "message_id=msg_access_gap_maria_2, subject='access issues - maria rodriguez', body='see details', to_emails=['it-support@company.com'], "
            "label_id=label_3, attach_id=attach_access_gap_maria_2, attach_filename=access_gaps_2.md, attach_mime=text/markdown."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_4", "system_name": "Email", "status": "Failed",
                           "note_nullable": "exchange outage"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_4", "system_name": "SSO", "status": "Failed",
                           "note_nullable": "idp sync pending"}),
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/maria_rodriguez/access_gaps_2.md",
                                                          "content_text": "Email: Failed - exchange outage\nSSO: Failed - idp sync pending\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_4"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_access_gap_maria_2", "subject": "access issues - maria rodriguez",
                           "body": "see details", "to_emails": ["it-support@company.com"], "candidate_id": "cand_4",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_access_gap_maria_2", "label_ids": ["label_3"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_access_gap_maria_2", "message_id": "msg_access_gap_maria_2",
                           "filename": "access_gaps_2.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/maria_rodriguez/access_gaps_2.md"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="027",
        instruction=(
            "You perform the welcome confirmation for cand_6 (emily chen). You create /onboarding/emily_chen/welcome_emily_confirm.md as text/markdown with '# welcome confirmed\\nsee details inside\\n', "
            "and you send msg_welcome_confirm_emily to emily.chen@example.com using subject 'welcome confirmation - emily chen' and body 'welcome confirmed', labeled with label_6 and attaching that file."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/emily_chen/welcome_emily_confirm.md",
                           "content_text": "# welcome confirmed\nsee details inside\n", "mime_type": "text/markdown",
                           "candidate_id": "cand_6"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_welcome_confirm_emily", "subject": "welcome confirmation - emily chen",
                           "body": "welcome confirmed", "to_emails": ["emily.chen@example.com"],
                           "candidate_id": "cand_6", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_welcome_confirm_emily", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_welcome_confirm_emily", "message_id": "msg_welcome_confirm_emily",
                           "filename": "welcome_emily_confirm.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/emily_chen/welcome_emily_confirm.md"}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "send_welcome_confirm",
                                                        "params_json": {"message_id": "msg_welcome_confirm_emily"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="104",
        instruction=(
            "You send a policy acknowledgment nudge for cand_1 (john doe) and update related checklist items. "
            "Send msg_policy_nudge_john_104 to john.doe@example.com with subject 'policy ack - john doe' and body 'please review and ack', apply label_id=label_6, "
            "and update item_1 and item_2 to 'Reminder Sent' referencing msg_policy_nudge_john_104."
        ),
        actions=[
            Action(name="insert_email",
                   kwargs={"message_id": "msg_policy_nudge_john_104", "subject": "policy ack - john doe",
                           "body": "please review and ack", "to_emails": ["john.doe@example.com"],
                           "candidate_id": "cand_1", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_policy_nudge_john_104", "label_ids": ["label_6"]}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_1", "fields": {"status": "Reminder Sent",
                                                                                         "reminder_email_message_id_nullable": "msg_policy_nudge_john_104"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_2", "fields": {"status": "Reminder Sent",
                                                                                         "reminder_email_message_id_nullable": "msg_policy_nudge_john_104"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="105",
        instruction=(
            "You resend the orientation invite for cand_7 (robert singh). "
            "Create /onboarding/robert_singh/orientation_agenda_105.md as text/markdown with '# orientation agenda\\nresend copy\\n'. "
            "Send msg_orientation_robert_105 to robert.singh@example.com with subject 'day-1 orientation (resend) - robert singh' and body 'agenda attached', apply label_id=label_4."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/robert_singh/orientation_agenda_105.md",
                           "content_text": "# orientation agenda\nresend copy\n", "mime_type": "text/markdown",
                           "candidate_id": "cand_7"}),
            Action(name="insert_email", kwargs={"message_id": "msg_orientation_robert_105",
                                                "subject": "day-1 orientation (resend) - robert singh",
                                                "body": "agenda attached", "to_emails": ["robert.singh@example.com"],
                                                "candidate_id": "cand_7", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_orientation_robert_105", "label_ids": ["label_4"]}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="001",
        instruction=(
            "You complete the welcome packet for cand_1 (john doe). "
            "Create /onboarding/john_doe/welcome_john_doe.md as text/markdown with exactly '# Welcome John\\nStart date: 2024-08-01\\n'. "
            "Send a labeled welcome email (message_id=msg_welcome_john, subject 'welcome to the team - john doe', body 'dear john, welcome!', to ['john.doe@example.com'], label_6) and keep it in thread_welcome_john. "
            "Attach the markdown you created and set cand_1 onboarding_status to 'Packet Sent' with welcome_email_message_id msg_welcome_john."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/john_doe/welcome_john_doe.md",
                                                          "content_text": "# Welcome John\nStart date: 2024-08-01\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_1"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_welcome_john", "subject": "welcome to the team - john doe",
                           "body": "dear john, welcome!", "to_emails": ["john.doe@example.com"],
                           "candidate_id": "cand_1", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_welcome_john", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_0019", "message_id": "msg_welcome_john",
                           "filename": "welcome_john_doe.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/john_doe/welcome_john_doe.md"}),
            Action(name="set_candidate_fields", kwargs={"candidate_id": "cand_1",
                                                        "fields": {"onboarding_status": "Packet Sent",
                                                                   "welcome_email_message_id_nullable": "msg_welcome_john"}}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_welcome_john", "fields": {"thread_id_nullable": "thread_welcome_john"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="002",
        instruction=(
            "You finalize the asset provisioning outcome for cand_7 (Robert Singh) using the Assets-Provisioning protocol. "
            "The final state must include: asset_req_5 with status 'Sent' and email_message_id_nullable 'msg_assets_robert'; "
            "a sent email record message_id msg_assets_robert to ['it-assets@company.com'] with subject 'Asset Provisioning Request - Robert Singh' and body 'See attached', labeled Asset-Request with label_id label_1; "
            "a JSON artifact at /onboarding/robert_singh/asset_request.json containing {'candidate':'cand_7','asset_type':'Laptop','requested_ts':'2024-08-06T14:20:00Z'}; "
            "candidate cand_7 linked to asset_req_5; "
            "inventory asset LT-MBP-001 assigned to cand_7; "
            "an MCP audit exists with server_name gmail, tool_name asset_provision, params_json {'message_id':'msg_assets_robert'}."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "asset_req_5", "fields": {"status": "Sent",
                                                                                                "email_message_id_nullable": "msg_assets_robert"}}),
            Action(name="create_or_get_email_label", kwargs={"name": "Asset-Request"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_assets_robert", "subject": "Asset Provisioning Request - Robert Singh",
                           "body": "See attached", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_7",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_assets_robert", "label_ids": ["label_1"]}),
            Action(name="upsert_json_artifact", kwargs={"file_path": "/onboarding/robert_singh/asset_request.json",
                                                        "content_obj": {"candidate": "cand_7", "asset_type": "Laptop",
                                                                        "requested_ts": "2024-08-06T14:20:00Z"},
                                                        "candidate_id": "cand_7"}),
            Action(name="link_asset_request_to_candidate",
                   kwargs={"candidate_id": "cand_7", "request_id": "asset_req_5"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "LT-MBP-001", "candidate_id": "cand_7"}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "asset_provision",
                                                        "params_json": {"message_id": "msg_assets_robert"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="003",
        instruction=(
            "You escalate access gaps for cand_4 (maria rodriguez). "
            "Record: email failed 'exchange server issue', sso failed 'idp sync pending', slack failed 'depends on sso', github pending 'waiting for sso fix'. "
            "Write /onboarding/maria_rodriguez/access_gaps.md as text/markdown with exactly these four lines, each on its own line: "
            "['Email: Failed - exchange server issue','SSO: Failed - idp sync pending','Slack: Failed - depends on sso','GitHub: Pending - waiting for sso fix']. "
            "Send msg_access_maria to ['it-support@company.com','david.kim@company.com'] with subject 'access issues alert - maria rodriguez' and body 'see details', "
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_4", "system_name": "Email", "status": "Failed",
                           "note_nullable": "exchange server issue"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_4", "system_name": "SSO", "status": "Failed",
                           "note_nullable": "idp sync pending"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_4", "system_name": "Slack", "status": "Failed",
                           "note_nullable": "depends on sso"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_4", "system_name": "GitHub", "status": "Pending",
                           "note_nullable": "waiting for sso fix"}),
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/maria_rodriguez/access_gaps.md",
                           "content_text": "Email: Failed - exchange server issue\nSSO: Failed - idp sync pending\nSlack: Failed - depends on sso\nGitHub: Pending - waiting for sso fix",
                           "mime_type": "text/markdown", "candidate_id": "cand_4"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_access_maria", "subject": "access issues alert - maria rodriguez",
                           "body": "see details", "to_emails": ["it-support@company.com", "david.kim@company.com"],
                           "candidate_id": "cand_4", "draft_flag": False, "sent_flag": True}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="004",
        instruction=(
            "You perform the Checklist-Follow-Up protocol for cand_2 (Jane Smith). "
            "The final state must include: a markdown summary at /onboarding/jane_smith/pending_tasks.md with mime text/markdown and content exactly '- HR Forms\n- Benefits Enrollment\n- Security Training\n'; "
            "a sent email record message_id msg_reminder_jane to ['jane.smith@example.com'] with subject 'Pending Onboarding Tasks' and body 'Please complete pending items', labeled Onboarding-Reminder with label_id label_2; "
            "checklist items item_4, item_5, item_6, item_7 updated to status 'Reminder Sent' with reminder_sent_flag True and reminder_email_message_id_nullable 'msg_reminder_jane'; "
            "candidate cand_2 updated with checklist_follow_up_ts_nullable '2025-01-01T09:00:00Z'; "
            "an MCP audit exists with server_name gmail, tool_name send_reminder, params_json {'message_id':'msg_reminder_jane'}."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/jane_smith/pending_tasks.md",
                                                          "content_text": "- HR Forms\n- Benefits Enrollment\n- Security Training\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_2"}),
            Action(name="create_or_get_email_label", kwargs={"name": "Onboarding-Reminder"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_reminder_jane", "subject": "Pending Onboarding Tasks",
                           "body": "Please complete pending items", "to_emails": ["jane.smith@example.com"],
                           "candidate_id": "cand_2", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_reminder_jane", "label_ids": ["label_2"]}),
            Action(name="bulk_update_checklist_items", kwargs={"item_ids": ["item_4", "item_5", "item_6", "item_7"],
                                                               "fields": {"status": "Reminder Sent",
                                                                          "reminder_sent_flag": True,
                                                                          "reminder_email_message_id_nullable": "msg_reminder_jane"}}),
            Action(name="set_candidate_timestamps", kwargs={"candidate_id": "cand_2", "fields": {
                "checklist_follow_up_ts_nullable": "2025-01-01T09:00:00Z"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "send_reminder",
                                                        "params_json": {"message_id": "msg_reminder_jane"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="005",
        instruction=(
            "You complete the laptop swap for cand_3 (peter jones) from LT-DELL-002 to LT-MBP-002. "
            "You notify it-assets with a sent email using message_id=msg_asset_swap_peter, subject='asset swap - peter jones', body='dell to mbp', to_emails=['it-assets@company.com'], label_id=label_1, and thread_id=thread_swap_peter. "
            "You audit gmail asset_swap_notice for {'message_id':'msg_asset_swap_peter'}."
        ),
        actions=[
            Action(name="release_inventory_asset", kwargs={"asset_tag": "LT-DELL-002"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "LT-MBP-002", "candidate_id": "cand_3"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_asset_swap_peter", "subject": "asset swap - peter jones",
                           "body": "dell to mbp", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_3",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_asset_swap_peter", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_asset_swap_peter",
                                                         "fields": {"thread_id_nullable": "thread_swap_peter"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "asset_swap_notice",
                                                        "params_json": {"message_id": "msg_asset_swap_peter"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="007",
        instruction=(
            "You close out phone provisioning for cand_4 (maria rodriguez). "
            "You mark asset_req_6 as Completed. "
            "You confirm msg_12 is the provisioning email and apply label_id label_1 (Asset-Request) to it. "
            "You finalize assignment of PH-IPHONE-002 to cand_4. "
            "You add a phone setup note at /onboarding/maria_rodriguez/phone_setup.md with mime text/markdown and content 'iphone setup checklist'. "
            "You attach phone_setup.md to msg_12 using attachment_id attach_phone_setup_maria and the same file_path. "
            "You mark checklist items item_8, item_9, item_10 as Completed. "
            "You record an mcp call for gmail with tool_name finalize_phone_request referencing msg_12."
        ),
        actions=[
            Action(name="update_asset_request",
                   kwargs={"request_id": "asset_req_6", "fields": {"status": "Completed"}}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_12", "label_ids": ["label_1"]}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "PH-IPHONE-002", "candidate_id": "cand_4"}),
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/maria_rodriguez/phone_setup.md",
                                                          "content_text": "iphone setup checklist",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_4"}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_phone_setup_maria", "message_id": "msg_12",
                           "filename": "phone_setup.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/maria_rodriguez/phone_setup.md"}),
            Action(name="bulk_update_checklist_items",
                   kwargs={"item_ids": ["item_8", "item_9", "item_10"], "fields": {"status": "Completed"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "finalize_phone_request",
                                                        "params_json": {"message_id": "msg_12"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="010",
        instruction=(
            "You complete the peripherals-allocation protocol for cand_5 (alex thompson). "
            "Final state must include: assets MON-DELL-001 and DS-DELL-001 assigned to cand_5; "
            "a terminal log entry with message 'assigned monitor MON-DELL-001 and dock DS-DELL-001 to alex thompson'; "
            "a sent email record message_id msg_peripherals_alex addressed to ['it-assets@company.com'] with subject 'Peripheral Allocation - Alex Thompson' and body 'monitor and dock assigned', labeled with label_id label_1; "
            "checklist items item_11, item_12, item_13, item_14 updated to status 'Completed'; "
            "an mcp audit for gmail with tool_name notify_peripherals referencing msg_peripherals_alex."
        ),
        actions=[
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "MON-DELL-001", "candidate_id": "cand_5"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "DS-DELL-001", "candidate_id": "cand_5"}),
            Action(name="insert_terminal_log",
                   kwargs={"message_text": "assigned monitor MON-DELL-001 and dock DS-DELL-001 to alex thompson"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_peripherals_alex", "subject": "Peripheral Allocation - Alex Thompson",
                           "body": "monitor and dock assigned", "to_emails": ["it-assets@company.com"],
                           "candidate_id": "cand_5", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_peripherals_alex", "label_ids": ["label_1"]}),
            Action(name="bulk_update_checklist_items", kwargs={"item_ids": ["item_11", "item_12", "item_13", "item_14"],
                                                               "fields": {"status": "Completed"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "notify_peripherals",
                                                        "params_json": {"message_id": "msg_peripherals_alex"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="011",
        instruction=(
            "You send a concise checklist reminder for cand_1 (john doe). You write /onboarding/john_doe/pending_tasks.md as text/markdown with '- it setup\n- benefits enrollment\n'. You send msg_reminder_john2 to john.doe@example.com with subject 'pending onboarding tasks - john doe' and body 'please complete items', labeled with label_2, and you update items item_3 and item_4 to 'Reminder Sent' with reminder_email_message_id_nullable msg_reminder_john2."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/john_doe/pending_tasks.md",
                                                          "content_text": "- it setup\n- benefits enrollment\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_1"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_reminder_john2", "subject": "pending onboarding tasks - john doe",
                           "body": "please complete items", "to_emails": ["john.doe@example.com"],
                           "candidate_id": "cand_1", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_reminder_john2", "label_ids": ["label_2"]}),
            Action(name="bulk_update_checklist_items", kwargs={"item_ids": ["item_3", "item_4"],
                                                               "fields": {"status": "Reminder Sent",
                                                                          "reminder_email_message_id_nullable": "msg_reminder_john2"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="012",
        instruction=(
            "You finalize the assets-provisioning closeout for cand_7 (robert singh). "
            "Provide parameters: asset_request='asset_req_5' final_status='Completed'; "
            "close_email={message_id:msg_assets_robert_close, to:['it-assets@company.com'], subject:'Asset Provisioning Completed - Robert Singh', body:'completed', label_id:label_1, thread_id:thread_assets_robert_close}; "
            "candidate_link={'asset_request_record_id_nullable':'asset_req_5'}; "
            "audit_text='closed asset_req_5 as Completed for robert singh'."
        ),
        actions=[
            Action(name="update_asset_request",
                   kwargs={"request_id": "asset_req_5", "fields": {"status": "Completed"}}),
            Action(name="insert_terminal_log",
                   kwargs={"message_text": "closed asset_req_5 as Completed for robert singh"}),
            Action(name="insert_email", kwargs={"message_id": "msg_assets_robert_close",
                                                "subject": "Asset Provisioning Completed - Robert Singh",
                                                "body": "completed", "to_emails": ["it-assets@company.com"],
                                                "candidate_id": "cand_7", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_assets_robert_close", "label_ids": ["label_1"]}),
            Action(name="set_candidate_fields",
                   kwargs={"candidate_id": "cand_7", "fields": {"asset_request_record_id_nullable": "asset_req_5"}}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_assets_robert_close", "fields": {
                "thread_id_nullable": "thread_assets_robert_close"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "asset_provision_close",
                                                        "params_json": {"message_id": "msg_assets_robert_close"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="015",
        instruction=(
            "You execute the phone-allocation protocol for cand_3 (peter jones). "
            "Provide parameters: asset_tag='PH-IPHONE-001'; "
            "audit_text='assigned phone PH-IPHONE-001 to peter jones'; "
            "notify_email={message_id:msg_phone_peter, to:['it-assets@company.com'], subject:'Phone Allocation - Peter Jones', body:'iphone assigned', label_id:label_1, thread_id:thread_phone_peter}."
        ),
        actions=[
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "PH-IPHONE-001", "candidate_id": "cand_3"}),
            Action(name="insert_terminal_log", kwargs={"message_text": "assigned phone PH-IPHONE-001 to peter jones"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_phone_peter", "subject": "Phone Allocation - Peter Jones",
                           "body": "iphone assigned", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_3",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_phone_peter", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_phone_peter", "fields": {"thread_id_nullable": "thread_phone_peter"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "notify_phone_allocation",
                                                        "params_json": {"message_id": "msg_phone_peter"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="016",
        instruction=(
            "You execute the policy-acknowledgment protocol for cand_6 (emily chen). "
            "Provide parameters: ack_path=/onboarding/emily_chen/policy_ack.md, ack_mime=text/markdown, ack_content='i acknowledge company policies'; "
            "ack_email={message_id:msg_policy_ack_emily, to:['emily.chen@example.com'], subject:'Policy Acknowledgment - Emily Chen', body:'ack attached', label_id:label_6, thread_id:thread_policy_ack_emily, attach_filename:policy_ack.md}; "
            "candidate_fields={'policy_acknowledged':'true'}."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/emily_chen/policy_ack.md",
                                                          "content_text": "i acknowledge company policies",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_6"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_policy_ack_emily", "subject": "Policy Acknowledgment - Emily Chen",
                           "body": "ack attached", "to_emails": ["emily.chen@example.com"], "candidate_id": "cand_6",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_policy_ack_emily", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_policy_ack_emily", "message_id": "msg_policy_ack_emily",
                           "filename": "policy_ack.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/emily_chen/policy_ack.md"}),
            Action(name="set_candidate_fields",
                   kwargs={"candidate_id": "cand_6", "fields": {"policy_acknowledged": "true"}}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_policy_ack_emily",
                                                         "fields": {"thread_id_nullable": "thread_policy_ack_emily"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "send_policy_ack_emily",
                                                        "params_json": {"message_id": "msg_policy_ack_emily"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="017",
        instruction=(
            "You execute the checklist-reminder protocol for cand_5 (alex thompson). "
            "Provide parameters: note_path=/onboarding/alex_thompson/pending_tasks.md, note_mime=text/markdown, note_content='- security training\n- benefits enrollment\n'; "
            "reminder_email={message_id:msg_reminder_alex, to:['alex.thompson@example.com'], subject:'Pending Onboarding Tasks - Alex Thompson', body:'please complete pending items', label_id:label_2}; "
            "update_items=[item_11,item_12] to status 'Reminder Sent' with reminder_sent_flag true and reminder_email_message_id_nullable 'msg_reminder_alex'; "
            "audit={'server_name':'gmail','tool_name':'send_reminder_alex','params_json':{'message_id':'msg_reminder_alex'}}."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/alex_thompson/pending_tasks.md",
                                                          "content_text": "- security training\n- benefits enrollment\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_5"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_reminder_alex", "subject": "Pending Onboarding Tasks - Alex Thompson",
                           "body": "please complete pending items", "to_emails": ["alex.thompson@example.com"],
                           "candidate_id": "cand_5", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_reminder_alex", "label_ids": ["label_2"]}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_11", "fields": {"status": "Reminder Sent",
                                                                                          "reminder_sent_flag": True,
                                                                                          "reminder_email_message_id_nullable": "msg_reminder_alex"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_12", "fields": {"status": "Reminder Sent",
                                                                                          "reminder_sent_flag": True,
                                                                                          "reminder_email_message_id_nullable": "msg_reminder_alex"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "send_reminder_alex",
                                                        "params_json": {"message_id": "msg_reminder_alex"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="018",
        instruction=(
            "You execute the laptop-replacement protocol for cand_4 (maria rodriguez). "
            "Provide parameters: release_asset='LT-DELL-002', assign_asset='LT-MBP-001'; "
            "audit_text='replaced maria rodriguez laptop from LT-DELL-002 to LT-MBP-001'; "
            "notify_email={message_id:msg_asset_replace_maria, to:['it-assets@company.com'], subject:'Asset Replacement - Maria Rodriguez', body:'dell to mbp', label_id:label_1, thread_id:thread_asset_replace_maria}; "
        ),
        actions=[
            Action(name="release_inventory_asset", kwargs={"asset_tag": "LT-DELL-002"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "LT-MBP-001", "candidate_id": "cand_4"}),
            Action(name="insert_terminal_log",
                   kwargs={"message_text": "replaced maria rodriguez laptop from LT-DELL-002 to LT-MBP-001"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_asset_replace_maria", "subject": "Asset Replacement - Maria Rodriguez",
                           "body": "dell to mbp", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_4",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_asset_replace_maria", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_asset_replace_maria", "fields": {
                "thread_id_nullable": "thread_asset_replace_maria"}})
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="021",
        instruction=(
            "You initiate the welcome packet resend protocol for cand_3 (peter jones). "
            "Provide parameters: "
            "file_path=/onboarding/peter_jones/welcome_peter_jones_v2.md, "
            "file_mime=text/markdown, "
            "file_content='# welcome again peter\\nplease review the attached docs.\\n', "
            "message_id=msg_welcome_peter_v2, "
            "subject='welcome packet (resend) - peter jones', "
            "body='peter, welcome again. docs attached.', "
            "to_emails=['peter.jones@example.com'], "
            "label_name='Welcome-Packet', label_id='label_6', "
            "attach_id=attach_welcome_peter_v2, attach_filename=welcome_peter_jones_v2.md, attach_mime=text/markdown, "
            "thread_id=thread_welcome_peter_v2."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/peter_jones/welcome_peter_jones_v2.md",
                           "content_text": "# welcome again peter\nplease review the attached docs.\n",
                           "mime_type": "text/markdown", "candidate_id": "cand_3"}),
            Action(name="create_or_get_email_label", kwargs={"name": "Welcome-Packet"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_welcome_peter_v2", "subject": "welcome packet (resend) - peter jones",
                           "body": "peter, welcome again. docs attached.", "to_emails": ["peter.jones@example.com"],
                           "candidate_id": "cand_3", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_welcome_peter_v2", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_welcome_peter_v2", "message_id": "msg_welcome_peter_v2",
                           "filename": "welcome_peter_jones_v2.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/peter_jones/welcome_peter_jones_v2.md"}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_welcome_peter_v2",
                                                         "fields": {"thread_id_nullable": "thread_welcome_peter_v2"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "send_welcome_resend",
                                                        "params_json": {"message_id": "msg_welcome_peter_v2"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="022",
        instruction=(
            "You run the phone allocation protocol for cand_1 (john doe). "
            "Provide parameters: asset_tag=PH-IPHONE-001, "
            "message_id=msg_phone_alloc_john, "
            "subject='phone allocation - john doe', "
            "body='iphone assigned.', "
            "to_emails=['it-assets@company.com'], "
            "label_id=label_1, "
            "thread_id=thread_phone_alloc_john, "
            "audit={'server_name':'gmail','tool_name':'notify_phone_alloc','params_json':{'message_id':'msg_phone_alloc_john'}}."
        ),
        actions=[
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "PH-IPHONE-001", "candidate_id": "cand_1"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_phone_alloc_john", "subject": "phone allocation - john doe",
                           "body": "iphone assigned.", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_1",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_phone_alloc_john", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_phone_alloc_john",
                                                         "fields": {"thread_id_nullable": "thread_phone_alloc_john"}}),
            Action(name="insert_terminal_log", kwargs={"message_text": "allocated PH-IPHONE-001 to cand_1"}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "notify_phone_alloc",
                                                        "params_json": {"message_id": "msg_phone_alloc_john"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="023",
        instruction=(
            "You execute the orientation invite protocol for cand_5 (alex thompson). "
            "Provide parameters: "
            "agenda_path=/onboarding/alex_thompson/orientation_agenda.md, agenda_mime=text/markdown, agenda_content='# orientation agenda\\nteam intros and setup\\n', "
            "message_id=msg_orientation_alex, subject='day-1 orientation - alex thompson', body='agenda attached', "
            "to_emails=['alex.thompson@example.com'], "
            "label_name='Orientation-Invite', label_id='label_4', "
            "attach_id=attach_orientation_agenda_alex, attach_filename=orientation_agenda.md, attach_mime=text/markdown, "
            "orientation_ts=2024-08-20T09:00:00Z, "
            "thread_id=thread_orientation_alex."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/alex_thompson/orientation_agenda.md",
                           "content_text": "# orientation agenda\nteam intros and setup\n",
                           "mime_type": "text/markdown", "candidate_id": "cand_5"}),
            Action(name="create_or_get_email_label", kwargs={"name": "Orientation-Invite"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_orientation_alex", "subject": "day-1 orientation - alex thompson",
                           "body": "agenda attached", "to_emails": ["alex.thompson@example.com"],
                           "candidate_id": "cand_5", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_orientation_alex", "label_ids": ["label_4"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_orientation_agenda_alex", "message_id": "msg_orientation_alex",
                           "filename": "orientation_agenda.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/alex_thompson/orientation_agenda.md"}),
            Action(name="set_candidate_fields", kwargs={"candidate_id": "cand_5", "fields": {
                "orientation_invite_ts_nullable": "2024-08-20T09:00:00Z"}}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_orientation_alex",
                                                         "fields": {"thread_id_nullable": "thread_orientation_alex"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="025",
        instruction=(
            "You execute the checklist-closeout protocol for cand_5 (alex thompson). "
            "Provide parameters: item_ids=['item_13','item_14'], "
            "message_id=msg_checklist_close_alex, subject='checklist closeout - alex thompson', body='remaining items completed', "
            "to_emails=['alex.thompson@example.com'], "
            "label_id=label_2, "
            "thread_id=thread_checklist_close_alex, "
            "log_text='closed remaining checklist items [item_13,item_14]', "
            "audit={'server_name':'gmail','tool_name':'send_closeout','params_json':{'message_id':'msg_checklist_close_alex'}}."
        ),
        actions=[
            Action(name="bulk_update_checklist_items",
                   kwargs={"item_ids": ["item_13", "item_14"], "fields": {"status": "Completed"}}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_checklist_close_alex", "subject": "checklist closeout - alex thompson",
                           "body": "remaining items completed", "to_emails": ["alex.thompson@example.com"],
                           "candidate_id": "cand_5", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_checklist_close_alex", "label_ids": ["label_2"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_checklist_close_alex", "fields": {
                "thread_id_nullable": "thread_checklist_close_alex"}}),
            Action(name="insert_terminal_log",
                   kwargs={"message_text": "closed remaining checklist items [item_13,item_14]"}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "send_closeout",
                                                        "params_json": {"message_id": "msg_checklist_close_alex"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="026",
        instruction=(
            "You finalize the phone request closure protocol for cand_4 (maria rodriguez). "
            "Provide parameters: request_id=asset_req_6, new_status=Completed, "
            "message_id=msg_phone_close_maria, subject='phone request closed - maria rodriguez', body='phone request completed', "
            "to_emails=['it-assets@company.com'], "
            "label_name='Asset-Request', label_id='label_1', "
            "thread_id=thread_phone_close_maria."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "asset_req_6", "fields": {"status": "Completed",
                                                                                                "email_message_id_nullable": "msg_phone_close_maria"}}),
            Action(name="create_or_get_email_label", kwargs={"name": "Asset-Request"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_phone_close_maria", "subject": "phone request closed - maria rodriguez",
                           "body": "phone request completed", "to_emails": ["it-assets@company.com"],
                           "candidate_id": "cand_4", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_phone_close_maria", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_phone_close_maria",
                                                         "fields": {"thread_id_nullable": "thread_phone_close_maria"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "notify_phone_close",
                                                        "params_json": {"message_id": "msg_phone_close_maria"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="028",
        instruction=(
            "You run the system-clearance notification protocol for cand_6 (emily chen). "
            "Provide parameters: checks=[('Email','Success',None),('Marketing Platform','Success',None)], "
            "message_id=msg_clearance_emily, subject='system clearance - emily chen', body='all core systems clear', "
            "to_emails=['it-support@company.com'], label_name='System-Alerts', label_id='label_7'."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_6", "system_name": "Email", "status": "Success"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_6", "system_name": "Marketing Platform", "status": "Success"}),
            Action(name="create_or_get_email_label", kwargs={"name": "System-Alerts"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_clearance_emily", "subject": "system clearance - emily chen",
                           "body": "all core systems clear", "to_emails": ["it-support@company.com"],
                           "candidate_id": "cand_6", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_clearance_emily", "label_ids": ["label_7"]}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "notify_clearance",
                                                        "params_json": {"message_id": "msg_clearance_emily"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="029",
        instruction=(
            "You apply the thread-link and notes protocol for cand_5 (alex thompson) on provisioning email msg_11. "
            "Provide parameters: notes_path=/onboarding/alex_thompson/provisioning_notes.md, notes_mime=text/markdown, notes_content='notes:\\n- slack provisioned as planned\\n', "
            "attach_id=attach_provisioning_notes_alex, attach_filename=provisioning_notes.md, attach_mime=text/markdown, "
            "label_id=label_1, thread_id=thread_slack_provisioning_link, audit_text='linked provisioning notes to msg_11 for cand_5'."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/alex_thompson/provisioning_notes.md",
                           "content_text": "notes:\n- slack provisioned as planned\n", "mime_type": "text/markdown",
                           "candidate_id": "cand_5"}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_provisioning_notes_alex", "message_id": "msg_11",
                           "filename": "provisioning_notes.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/alex_thompson/provisioning_notes.md"}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_11", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_11", "fields": {"thread_id_nullable": "thread_slack_provisioning_link"}}),
            Action(name="insert_terminal_log",
                   kwargs={"message_text": "linked provisioning notes to msg_11 for cand_5"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="033",
        instruction=(
            "You run the access-gap alert protocol for cand_3 (peter jones) focused on slack. "
            "Provide parameters: access_entry={system:'Slack', status:'Pending', note:'awaiting sso group'}, "
            "summary_path=/onboarding/peter_jones/slack_gap.md, summary_mime=text/markdown, summary_lines=['Slack: Pending - awaiting sso group'], "
            "email={message_id:msg_slack_gap_peter, to:['it-support@company.com'], subject:'access gap - peter jones (slack)', body:'see summary', label_id:label_7}, "
            "attach_id=attach_slack_gap_peter, attach_filename=slack_gap.md."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_3", "system_name": "Slack", "status": "Pending",
                           "note_nullable": "awaiting sso group"}),
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/peter_jones/slack_gap.md",
                                                          "content_text": "Slack: Pending - awaiting sso group\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_3"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_slack_gap_peter", "subject": "access gap - peter jones (slack)",
                           "body": "see summary", "to_emails": ["it-support@company.com"], "candidate_id": "cand_3",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_slack_gap_peter", "label_ids": ["label_7"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_slack_gap_peter", "message_id": "msg_slack_gap_peter",
                           "filename": "slack_gap.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/peter_jones/slack_gap.md"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="034",
        instruction=(
            "You initiate the orientation-invite protocol for cand_1 (john doe). "
            "Provide parameters: agenda_path=/onboarding/john_doe/orientation_agenda.md, agenda_mime=text/markdown, agenda_content='# orientation agenda\\nwelcome and setup\\n', "
            "email={message_id:msg_orientation_john_v2, to:['john.doe@example.com'], subject:'day-1 orientation - john doe', body:'agenda attached', label_id:label_4, thread_id:thread_orientation_john_v2}, "
            "candidate_update={orientation_invite_ts_nullable:'2024-07-31T10:00:00Z'}, "
            "attach_id=attach_orientation_agenda_john_v2, attach_filename=orientation_agenda.md."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/john_doe/orientation_agenda.md",
                                                          "content_text": "# orientation agenda\nwelcome and setup\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_1"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_orientation_john_v2", "subject": "day-1 orientation - john doe",
                           "body": "agenda attached", "to_emails": ["john.doe@example.com"], "candidate_id": "cand_1",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_orientation_john_v2", "label_ids": ["label_4"]}),
            Action(name="insert_attachment_record", kwargs={"attachment_id": "attach_orientation_agenda_john_v2",
                                                            "message_id": "msg_orientation_john_v2",
                                                            "filename": "orientation_agenda.md",
                                                            "mime_type": "text/markdown",
                                                            "file_path": "/onboarding/john_doe/orientation_agenda.md"}),
            Action(name="set_candidate_fields", kwargs={"candidate_id": "cand_1", "fields": {
                "orientation_invite_ts_nullable": "2024-07-31T10:00:00Z"}}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_orientation_john_v2", "fields": {
                "thread_id_nullable": "thread_orientation_john_v2"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="035",
        instruction=(
            "You run the checklist-reminder protocol for cand_7 (robert singh). "
            "Provide parameters: note_path=/onboarding/robert_singh/pending_tasks.md, note_mime=text/markdown, note_content='- hr forms\\n- security training\\n', "
            "reminder_email={message_id:msg_reminder_robert, to:['robert.singh@example.com'], subject:'pending tasks - robert singh', body:'please complete', label_id:label_2}, "
            "update_items=['item_15','item_16'] to status 'Reminder Sent' with reminder_sent_flag true and reminder_email_message_id_nullable 'msg_reminder_robert', "
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/robert_singh/pending_tasks.md",
                                                          "content_text": "- hr forms\n- security training\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_7"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_reminder_robert", "subject": "pending tasks - robert singh",
                           "body": "please complete", "to_emails": ["robert.singh@example.com"],
                           "candidate_id": "cand_7", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_reminder_robert", "label_ids": ["label_2"]}),
            Action(name="bulk_update_checklist_items", kwargs={"item_ids": ["item_15", "item_16"],
                                                               "fields": {"status": "Reminder Sent",
                                                                          "reminder_sent_flag": True,
                                                                          "reminder_email_message_id_nullable": "msg_reminder_robert"}})
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="036",
        instruction=(
            "You execute the peripherals-allocation protocol for cand_3 (peter jones). "
            "Provide parameters: assign_assets=['MON-DELL-001','KB-LOGI-001'], "
            "notify_email={message_id:msg_peripherals_peter, to:['it-assets@company.com'], subject:'peripherals allocation - peter jones', body:'monitor and keyboard assigned', label_id:label_1, thread_id:thread_peripherals_peter}, "
            "audit_text='assigned MON-DELL-001 and KB-LOGI-001 to cand_3'."
        ),
        actions=[
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "MON-DELL-001", "candidate_id": "cand_3"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "KB-LOGI-001", "candidate_id": "cand_3"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_peripherals_peter", "subject": "peripherals allocation - peter jones",
                           "body": "monitor and keyboard assigned", "to_emails": ["it-assets@company.com"],
                           "candidate_id": "cand_3", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_peripherals_peter", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_peripherals_peter",
                                                         "fields": {"thread_id_nullable": "thread_peripherals_peter"}}),
            Action(name="insert_terminal_log",
                   kwargs={"message_text": "assigned MON-DELL-001 and KB-LOGI-001 to cand_3"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="037",
        instruction=(
            "You run the phone-allocation protocol for cand_1 (john doe). "
            "You assign PH-IPHONE-001 to cand_1, notify it-assets with msg_phone_john_v2 using subject 'phone allocation - john doe' and body 'iphone assigned', labeled label_1 and linked under thread_phone_john_v2, and you add a short log."
        ),
        actions=[
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "PH-IPHONE-001", "candidate_id": "cand_1"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_phone_john_v2", "subject": "phone allocation - john doe",
                           "body": "iphone assigned", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_1",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_phone_john_v2", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_phone_john_v2",
                                                         "fields": {"thread_id_nullable": "thread_phone_john_v2"}}),
            Action(name="insert_terminal_log", kwargs={"message_text": "assigned PH-IPHONE-001 to cand_1"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="038",
        instruction=(
            "You initiate the benefits-reminder protocol for cand_2 (jane smith). "
            "Provide parameters: note_path=/onboarding/jane_smith/pending_tasks.md, note_mime=text/markdown, note_content='- benefits enrollment\\n- direct deposit\\n', "
            "reminder_email={message_id:msg_benefits_reminder_jane, to:['jane.smith@example.com'], subject:'benefits reminder - jane smith', body:'please complete benefits setup', label_id:label_2}, "
            "update_items=['item_5','item_6'] to status 'Reminder Sent' with reminder_sent_flag true and reminder_email_message_id_nullable 'msg_benefits_reminder_jane', "
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/jane_smith/pending_tasks.md",
                                                          "content_text": "- benefits enrollment\n- direct deposit\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_2"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_benefits_reminder_jane", "subject": "benefits reminder - jane smith",
                           "body": "please complete benefits setup", "to_emails": ["jane.smith@example.com"],
                           "candidate_id": "cand_2", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_benefits_reminder_jane", "label_ids": ["label_2"]}),
            Action(name="bulk_update_checklist_items", kwargs={"item_ids": ["item_5", "item_6"],
                                                               "fields": {"status": "Reminder Sent",
                                                                          "reminder_sent_flag": True,
                                                                          "reminder_email_message_id_nullable": "msg_benefits_reminder_jane"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="039",
        instruction=(
            "You confirm access status for cand_6 (emily chen) by recording SSO success and marketing platform pending with note 'vendor activation pending', "
            "and you send a labeled email msg_access_status_emily to ['it-support@company.com'] using subject 'access status - emily chen' and body 'latest status enclosed' with label_id label_7."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_6", "system_name": "SSO", "status": "Success"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_6", "system_name": "Marketing Platform", "status": "Pending",
                           "note_nullable": "vendor activation pending"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_access_status_emily", "subject": "access status - emily chen",
                           "body": "latest status enclosed", "to_emails": ["it-support@company.com"],
                           "candidate_id": "cand_6", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_access_status_emily", "label_ids": ["label_7"]}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="040",
        instruction=(
            "You run the manager-intro protocol for cand_1 (john doe). "
            "Provide parameters: intro_note_path=/onboarding/john_doe/manager_intro.md, intro_note_mime=text/markdown, intro_note_content='# manager intro\\nwelcome call\\n', "
            "email={message_id:msg_intro_john_v2, to:['john.doe@example.com'], subject:'manager intro - john doe', body:'calendar hold sent', label_id:label_5, thread_id:thread_intro_john_v2}, "
            "candidate_update={manager_intro_invite_ts_nullable:'2024-07-31T10:30:00Z'}."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/john_doe/manager_intro.md",
                                                          "content_text": "# manager intro\nwelcome call\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_1"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_intro_john_v2", "subject": "manager intro - john doe",
                           "body": "calendar hold sent", "to_emails": ["john.doe@example.com"],
                           "candidate_id": "cand_1", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_intro_john_v2", "label_ids": ["label_5"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_intro_john_v2",
                                                         "fields": {"thread_id_nullable": "thread_intro_john_v2"}}),
            Action(name="set_candidate_fields", kwargs={"candidate_id": "cand_1", "fields": {
                "manager_intro_invite_ts_nullable": "2024-07-31T10:30:00Z"}}),
        ],
        outputs=["ok"],
    ),

    Task(
        annotator="v2",
        user_id="044",
        instruction=(
            "You run the checklist-reminder protocol for cand_2 (jane smith). "
            "Provide parameters: note_path=/onboarding/jane_smith/pending_tasks_2.md, note_mime=text/markdown, note_content='- benefits enrollment\\n- security training\\n', "
            "message_id=msg_reminder_jane_2, subject='pending onboarding tasks - jane smith', body='please complete pending items', to_emails=['jane.smith@example.com'], "
            "label_id=label_2, update_items=[item_5,item_6]."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/jane_smith/pending_tasks_2.md",
                                                          "content_text": "- benefits enrollment\n- security training\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_2"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_reminder_jane_2", "subject": "pending onboarding tasks - jane smith",
                           "body": "please complete pending items", "to_emails": ["jane.smith@example.com"],
                           "candidate_id": "cand_2", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_reminder_jane_2", "label_ids": ["label_2"]}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_5", "fields": {"status": "Reminder Sent",
                                                                                         "reminder_sent_flag": True,
                                                                                         "reminder_email_message_id_nullable": "msg_reminder_jane_2"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_6", "fields": {"status": "Reminder Sent",
                                                                                         "reminder_sent_flag": True,
                                                                                         "reminder_email_message_id_nullable": "msg_reminder_jane_2"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="045",
        instruction=(
            "You run the laptop-swap notice protocol for cand_3 (peter jones). "
            "Provide parameters: old_tag=LT-DELL-002, new_tag=LT-MBP-001, "
            "message_id=msg_asset_swap_peter_2, subject='asset swap - peter jones', body='dell to mbp', to_emails=['it-assets@company.com'], "
            "label_id=label_1, thread_id=thread_swap_peter_2, audit_text='swapped peter jones from LT-DELL-002 to LT-MBP-001'."
        ),
        actions=[
            Action(name="release_inventory_asset", kwargs={"asset_tag": "LT-DELL-002"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "LT-MBP-001", "candidate_id": "cand_3"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_asset_swap_peter_2", "subject": "asset swap - peter jones",
                           "body": "dell to mbp", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_3",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_asset_swap_peter_2", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_asset_swap_peter_2",
                                                         "fields": {"thread_id_nullable": "thread_swap_peter_2"}}),
            Action(name="insert_terminal_log",
                   kwargs={"message_text": "swapped peter jones from LT-DELL-002 to LT-MBP-001"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="046",
        instruction=(
            "You run the peripherals-allocation notice for cand_6 (emily chen). "
            "Provide parameters: tags=['MON-DELL-001','DS-DELL-001'], "
            "message_id=msg_peripherals_emily_2, subject='peripheral allocation - emily chen', body='monitor and dock assigned', to_emails=['it-assets@company.com'], "
            "label_id=label_1, thread_id=thread_peripherals_emily_2, "
        ),
        actions=[
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "MON-DELL-001", "candidate_id": "cand_6"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "DS-DELL-001", "candidate_id": "cand_6"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_peripherals_emily_2", "subject": "peripheral allocation - emily chen",
                           "body": "monitor and dock assigned", "to_emails": ["it-assets@company.com"],
                           "candidate_id": "cand_6", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_peripherals_emily_2", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_peripherals_emily_2", "fields": {
                "thread_id_nullable": "thread_peripherals_emily_2"}})
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="049",
        instruction=(
            "You run the phone-request closeout for cand_4 (maria rodriguez). "
            "Provide parameters: request_id=asset_req_6, status='Completed', message_id=msg_phone_close_maria, subject='phone request closeout - maria rodriguez', body='completed', "
            "to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_phone_close_maria, audit_text='closed asset_req_6 for cand_4'."
        ),
        actions=[
            Action(name="update_asset_request", kwargs={"request_id": "asset_req_6", "fields": {"status": "Completed",
                                                                                                "email_message_id_nullable": "msg_phone_close_maria"}}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_phone_close_maria", "subject": "phone request closeout - maria rodriguez",
                           "body": "completed", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_4",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_phone_close_maria", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_phone_close_maria",
                                                         "fields": {"thread_id_nullable": "thread_phone_close_maria"}}),
            Action(name="insert_terminal_log", kwargs={"message_text": "closed asset_req_6 for cand_4"}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "notify_phone_closeout",
                                                        "params_json": {"message_id": "msg_phone_close_maria"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="050",
        instruction=(
            "You link a policy acknowledgment for cand_2 (jane smith). You save /onboarding/jane_smith/policy_ack.md as text/markdown with 'policy ack', "
            "and you send msg_policy_ack_jane to jane.smith@example.com using subject 'policy ack - jane smith' and body 'ack received', labeled with label_6 and attaching that file."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/jane_smith/policy_ack.md", "content_text": "policy ack\n",
                           "mime_type": "text/markdown", "candidate_id": "cand_2"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_policy_ack_jane", "subject": "policy ack - jane smith",
                           "body": "ack received", "to_emails": ["jane.smith@example.com"], "candidate_id": "cand_2",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_policy_ack_jane", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_policy_ack_jane", "message_id": "msg_policy_ack_jane",
                           "filename": "policy_ack.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/jane_smith/policy_ack.md"}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "link_policy_ack",
                                                        "params_json": {"message_id": "msg_policy_ack_jane"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="051",
        instruction=(
            "You refresh the welcome attachment for cand_3 (peter jones). You save /onboarding/peter_jones/welcome_addendum.md as text/markdown with 'addendum v2', "
            "and you send msg_welcome_addendum_peter to peter.jones@example.com using subject 'welcome addendum - peter jones' and body 'see addendum', labeled with label_6 and attaching the addendum."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/peter_jones/welcome_addendum.md", "content_text": "addendum v2\n",
                           "mime_type": "text/markdown", "candidate_id": "cand_3"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_welcome_addendum_peter", "subject": "welcome addendum - peter jones",
                           "body": "see addendum", "to_emails": ["peter.jones@example.com"], "candidate_id": "cand_3",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_welcome_addendum_peter", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_welcome_addendum_peter", "message_id": "msg_welcome_addendum_peter",
                           "filename": "welcome_addendum.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/peter_jones/welcome_addendum.md"}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "send_welcome_addendum",
                                                        "params_json": {"message_id": "msg_welcome_addendum_peter"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="052",
        instruction=(
            "You resend the orientation invite for cand_6 (emily chen). You store /onboarding/emily_chen/orientation_agenda_resend.md as text/markdown with '# orientation agenda\\nresend copy\\n', "
            "and you send msg_orientation_emily_resend to emily.chen@example.com using subject 'day-1 orientation (resend) - emily chen' and body 'agenda attached', labeled with label_4 and attaching the resend agenda."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/emily_chen/orientation_agenda_resend.md",
                           "content_text": "# orientation agenda\nresend copy\n", "mime_type": "text/markdown",
                           "candidate_id": "cand_6"}),
            Action(name="insert_email", kwargs={"message_id": "msg_orientation_emily_resend",
                                                "subject": "day-1 orientation (resend) - emily chen",
                                                "body": "agenda attached", "to_emails": ["emily.chen@example.com"],
                                                "candidate_id": "cand_6", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_orientation_emily_resend", "label_ids": ["label_4"]}),
            Action(name="insert_attachment_record", kwargs={"attachment_id": "attach_orientation_agenda_emily_resend",
                                                            "message_id": "msg_orientation_emily_resend",
                                                            "filename": "orientation_agenda_resend.md",
                                                            "mime_type": "text/markdown",
                                                            "file_path": "/onboarding/emily_chen/orientation_agenda_resend.md"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="053",
        instruction=(
            "You run the asset-reassignment protocol for cand_2 (jane smith) to move to LT-MBP-002. "
            "Provide parameters: release_tag=LT-DELL-003, assign_tag=LT-MBP-002, "
            "message_id=msg_asset_reassign_jane, subject='asset reassignment - jane smith', body='moved to mbp', to_emails=['it-assets@company.com'], "
            "label_id=label_1, thread_id=thread_asset_reassign_jane, audit_text='reassigned jane smith from LT-DELL-003 to LT-MBP-002'."
        ),
        actions=[
            Action(name="release_inventory_asset", kwargs={"asset_tag": "LT-DELL-003"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "LT-MBP-002", "candidate_id": "cand_2"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_asset_reassign_jane", "subject": "asset reassignment - jane smith",
                           "body": "moved to mbp", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_2",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_asset_reassign_jane", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_asset_reassign_jane", "fields": {
                "thread_id_nullable": "thread_asset_reassign_jane"}}),
            Action(name="insert_terminal_log",
                   kwargs={"message_text": "reassigned jane smith from LT-DELL-003 to LT-MBP-002"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="054",
        instruction=(
            "You record an access pass for cand_3 (peter jones) and notify support. You record Email pass and SSO pass with notes 'ok', "
            "and you send msg_access_pass_peter to ['it-support@company.com'] using subject 'access pass - peter jones' and body 'all good', labeled with label_7."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_3", "system_name": "Email", "status": "Pass", "note_nullable": "ok"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_3", "system_name": "SSO", "status": "Pass", "note_nullable": "ok"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_access_pass_peter", "subject": "access pass - peter jones",
                           "body": "all good", "to_emails": ["it-support@company.com"], "candidate_id": "cand_3",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_access_pass_peter", "label_ids": ["label_7"]}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="055",
        instruction=(
            "You run the benefits-reminder protocol for cand_6 (emily chen). "
            "Provide parameters: note_path=/onboarding/emily_chen/benefits_pending.md, note_mime=text/markdown, note_content='- benefits enrollment\\n', "
            "message_id=msg_benefits_reminder_emily, subject='benefits reminder - emily chen', body='please complete benefits', to_emails=['emily.chen@example.com'], "
            "label_id=label_2, update_items=[item_9], thread_id=thread_benefits_reminder_emily."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/emily_chen/benefits_pending.md",
                                                          "content_text": "- benefits enrollment\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_6"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_benefits_reminder_emily", "subject": "benefits reminder - emily chen",
                           "body": "please complete benefits", "to_emails": ["emily.chen@example.com"],
                           "candidate_id": "cand_6", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_benefits_reminder_emily", "label_ids": ["label_2"]}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_9", "fields": {"status": "Reminder Sent",
                                                                                         "reminder_sent_flag": True,
                                                                                         "reminder_email_message_id_nullable": "msg_benefits_reminder_emily"}}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_benefits_reminder_emily", "fields": {
                "thread_id_nullable": "thread_benefits_reminder_emily"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "send_benefits_reminder",
                                                        "params_json": {"message_id": "msg_benefits_reminder_emily"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="057",
        instruction=(
            "You run the laptop-ready notice for cand_7 (robert singh). "
            "Provide parameters: message_id=msg_laptop_ready_robert, subject='laptop ready - robert singh', body='pick up scheduled', to_emails=['robert.singh@example.com'], "
            "label_id=label_1, thread_id=thread_laptop_ready_robert, and update asset_req_5 to status 'Sent' with email_message_id_nullable msg_laptop_ready_robert."
        ),
        actions=[
            Action(name="insert_email",
                   kwargs={"message_id": "msg_laptop_ready_robert", "subject": "laptop ready - robert singh",
                           "body": "pick up scheduled", "to_emails": ["robert.singh@example.com"],
                           "candidate_id": "cand_7", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_laptop_ready_robert", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_laptop_ready_robert", "fields": {
                "thread_id_nullable": "thread_laptop_ready_robert"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "notify_laptop_ready",
                                                        "params_json": {"message_id": "msg_laptop_ready_robert"}}),
            Action(name="update_asset_request", kwargs={"request_id": "asset_req_5", "fields": {"status": "Sent",
                                                                                                "email_message_id_nullable": "msg_laptop_ready_robert"}}),
            Action(name="insert_terminal_log", kwargs={"message_text": "laptop ready notice sent for cand_7"}),
        ],
        outputs=["ok"],
    ),

    Task(
        annotator="v2",
        user_id="058",
        instruction=(
            "You run the access-summary record for cand_2 (jane smith). "
            "Provide parameters: checks=[('Slack','Pass','ok'),('GitHub','Pending','awaiting sso')], "
            "message_id=msg_access_summary_jane, subject='access summary - jane smith', body='status included', to_emails=['it-support@company.com'], "
            "label_id=label_7, thread_id=thread_access_summary_jane, and audit gmail notify_access_summary for {'message_id':'msg_access_summary_jane'}."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_2", "system_name": "Slack", "status": "Pass", "note_nullable": "ok"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_2", "system_name": "GitHub", "status": "Pending",
                           "note_nullable": "awaiting sso"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_access_summary_jane", "subject": "access summary - jane smith",
                           "body": "status included", "to_emails": ["it-support@company.com"], "candidate_id": "cand_2",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_access_summary_jane", "label_ids": ["label_7"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_access_summary_jane", "fields": {
                "thread_id_nullable": "thread_access_summary_jane"}}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "notify_access_summary",
                                                        "params_json": {"message_id": "msg_access_summary_jane"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="059",
        instruction=(
            "You run the supplies-request notice for cand_4 (maria rodriguez). "
            "Provide parameters: message_id=msg_supplies_maria, subject='supplies request - maria rodriguez', body='starter kit requested', to_emails=['it-assets@company.com'], "
            "label_id=label_1, thread_id=thread_supplies_maria, audit_text='starter kit requested for cand_4'."
        ),
        actions=[
            Action(name="insert_email",
                   kwargs={"message_id": "msg_supplies_maria", "subject": "supplies request - maria rodriguez",
                           "body": "starter kit requested", "to_emails": ["it-assets@company.com"],
                           "candidate_id": "cand_4", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_supplies_maria", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_supplies_maria",
                                                         "fields": {"thread_id_nullable": "thread_supplies_maria"}}),
            Action(name="insert_terminal_log", kwargs={"message_text": "starter kit requested for cand_4"}),
            Action(name="record_mcp_tool_call", kwargs={"server_name": "gmail", "tool_name": "notify_supplies_request",
                                                        "params_json": {"message_id": "msg_supplies_maria"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="061",
        instruction=(
            "You confirm the welcome for cand_2 (jane smith) with a brief note and a labeled email to jane. "
            "Save /onboarding/jane_smith/welcome_confirm.md as text/markdown with '# welcome confirmed\\nsee details inside\\n'. "
            "Send msg_welcome_confirm_jane to john.doe@example.com? no—to jane.smith@example.com with subject 'welcome confirmation - jane smith' and body 'welcome confirmed'. "
            "Label it label_6, attach welcome_confirm.md plus Company-Policies.pdf and Benefits-Guide.pdf, link thread to thread_welcome_confirm_jane, and set candidate welcome_email_message_id_nullable to msg_welcome_confirm_jane."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/jane_smith/welcome_confirm.md",
                                                          "content_text": "# welcome confirmed\nsee details inside\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_2"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_welcome_confirm_jane", "subject": "welcome confirmation - jane smith",
                           "body": "welcome confirmed", "to_emails": ["jane.smith@example.com"],
                           "candidate_id": "cand_2", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_welcome_confirm_jane", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_welcome_confirm_jane", "message_id": "msg_welcome_confirm_jane",
                           "filename": "welcome_confirm.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/jane_smith/welcome_confirm.md"}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_jane_policies_pdf", "message_id": "msg_welcome_confirm_jane",
                           "filename": "Company-Policies.pdf", "mime_type": "application/pdf",
                           "file_path": "/onboarding/jane_smith/Company-Policies.pdf"}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_jane_benefits_pdf", "message_id": "msg_welcome_confirm_jane",
                           "filename": "Benefits-Guide.pdf", "mime_type": "application/pdf",
                           "file_path": "/onboarding/jane_smith/Benefits-Guide.pdf"}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_welcome_confirm_jane", "fields": {
                "thread_id_nullable": "thread_welcome_confirm_jane"}}),
            Action(name="set_candidate_fields", kwargs={"candidate_id": "cand_2", "fields": {
                "welcome_email_message_id_nullable": "msg_welcome_confirm_jane"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="062",
        instruction=(
            "You complete a laptop replacement for cand_3 (peter jones), moving from LT-DELL-002 to LT-MBP-001, and notify it. "
            "Include a short swap note at /onboarding/peter_jones/swap_note.md (text/markdown, 'swap: LT-DELL-002 -> LT-MBP-001'). "
            "Send msg_swap_peter to it-assets@company.com with subject 'asset swap - peter jones' and body 'dell to mbp', label label_1, attach the note, and link to thread_swap_peter."
        ),
        actions=[
            Action(name="release_inventory_asset", kwargs={"asset_tag": "LT-DELL-002"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "LT-MBP-001", "candidate_id": "cand_3"}),
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/peter_jones/swap_note.md",
                                                          "content_text": "swap: LT-DELL-002 -> LT-MBP-001",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_3"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_swap_peter", "subject": "asset swap - peter jones", "body": "dell to mbp",
                           "to_emails": ["it-assets@company.com"], "candidate_id": "cand_3", "draft_flag": False,
                           "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_swap_peter", "label_ids": ["label_1"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_swap_note_peter", "message_id": "msg_swap_peter",
                           "filename": "swap_note.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/peter_jones/swap_note.md"}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_swap_peter", "fields": {"thread_id_nullable": "thread_swap_peter"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="063",
        instruction=(
            "You escalate access issues for cand_4 (maria rodriguez) with a concise summary and a labeled alert. "
            "Record Email Failed 'exchange server issue' and SSO Failed 'idp sync pending'. "
            "Write /onboarding/maria_rodriguez/access_summary.md (text/markdown) with 'email: failed - exchange server issue\\nsso: failed - idp sync pending\\n'. "
            "Send msg_access_alert_maria to it-support@company.com with subject 'access issues - maria rodriguez' and body 'see summary', label label_3, attach the summary, and link thread_access_alert_maria."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_4", "system_name": "Email", "status": "Failed",
                           "note_nullable": "exchange server issue"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_4", "system_name": "SSO", "status": "Failed",
                           "note_nullable": "idp sync pending"}),
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/maria_rodriguez/access_summary.md",
                                                          "content_text": "email: failed - exchange server issue\nsso: failed - idp sync pending\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_4"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_access_alert_maria", "subject": "access issues - maria rodriguez",
                           "body": "see summary", "to_emails": ["it-support@company.com"], "candidate_id": "cand_4",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_access_alert_maria", "label_ids": ["label_3"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_access_summary_maria", "message_id": "msg_access_alert_maria",
                           "filename": "access_summary.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/maria_rodriguez/access_summary.md"}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_access_alert_maria", "fields": {
                "thread_id_nullable": "thread_access_alert_maria"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="064",
        instruction=(
            "You send a focused checklist reminder for cand_5 (alex thompson) and update the items. You save /onboarding/alex_thompson/pending_tasks.md as text/markdown with '- kubernetes access\\n- security training\\n', "
            "and you send msg_reminder_alex2 to alex.thompson@example.com using subject 'pending tasks - alex thompson' and body 'please complete', labeled with label_2, while updating item_13 and item_14 to 'Reminder Sent' with reminder_email_message_id_nullable msg_reminder_alex2."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/alex_thompson/pending_tasks.md",
                                                          "content_text": "- kubernetes access\n- security training\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_5"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_reminder_alex2", "subject": "pending tasks - alex thompson",
                           "body": "please complete", "to_emails": ["alex.thompson@example.com"],
                           "candidate_id": "cand_5", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_reminder_alex2", "label_ids": ["label_2"]}),
            Action(name="bulk_update_checklist_items", kwargs={"item_ids": ["item_13", "item_14"],
                                                               "fields": {"status": "Reminder Sent",
                                                                          "reminder_sent_flag": True,
                                                                          "reminder_email_message_id_nullable": "msg_reminder_alex2"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="065",
        instruction=(
            "You finalize a phone allocation for cand_1 (john doe) and notify it. "
            "Assign PH-IPHONE-001 to cand_1. "
            "Include a short setup note at /onboarding/john_doe/phone_setup.md (text/markdown) with 'iphone issued to john doe'. "
            "Send msg_phone_alloc_john2 to it-assets@company.com with subject 'phone allocation - john doe' and body 'iphone assigned', label label_1, attach the setup note, and link thread_phone_alloc_john2."
        ),
        actions=[
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "PH-IPHONE-001", "candidate_id": "cand_1"}),
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/john_doe/phone_setup.md",
                                                          "content_text": "iphone issued to john doe",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_1"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_phone_alloc_john2", "subject": "phone allocation - john doe",
                           "body": "iphone assigned", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_1",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_phone_alloc_john2", "label_ids": ["label_1"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_phone_setup_john", "message_id": "msg_phone_alloc_john2",
                           "filename": "phone_setup.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/john_doe/phone_setup.md"}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_phone_alloc_john2",
                                                         "fields": {"thread_id_nullable": "thread_phone_alloc_john2"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="066",
        instruction=(
            "You complete the asset request send-off for cand_7 (robert singh) with the request JSON and a labeled handoff email. "
            "Update asset_req_5 to Sent with email id msg_assets_robert2. "
            "Write /onboarding/robert_singh/asset_request.json with {'candidate':'cand_7','asset_type':'Laptop','requested_ts':'2024-08-06T14:20:00Z'}. "
            "Send msg_assets_robert2 to it-assets@company.com with subject 'asset provisioning request - robert singh' and body 'see attached', label label_1, link thread_assets_robert2, and ensure the candidate is linked to asset_req_5."
        ),
        actions=[
            Action(name="upsert_json_artifact", kwargs={"file_path": "/onboarding/robert_singh/asset_request.json",
                                                        "content_obj": {"candidate": "cand_7", "asset_type": "Laptop",
                                                                        "requested_ts": "2024-08-06T14:20:00Z"},
                                                        "candidate_id": "cand_7"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_assets_robert2", "subject": "asset provisioning request - robert singh",
                           "body": "see attached", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_7",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_assets_robert2", "label_ids": ["label_1"]}),
            Action(name="update_asset_request", kwargs={"request_id": "asset_req_5", "fields": {"status": "Sent",
                                                                                                "email_message_id_nullable": "msg_assets_robert2"}}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_assets_robert2",
                                                         "fields": {"thread_id_nullable": "thread_assets_robert2"}}),
            Action(name="link_asset_request_to_candidate",
                   kwargs={"candidate_id": "cand_7", "request_id": "asset_req_5"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="067",
        instruction=(
            "You finalize orientation for cand_6 (emily chen) with an agenda and an invite. You create /onboarding/emily_chen/orientation_agenda.md as text/markdown with '# orientation agenda\\nwelcome and access\\n', "
            "and you send msg_orientation_emily2 to emily.chen@example.com using subject 'day-1 orientation - emily chen' and body 'agenda attached', attaching the agenda, and you set orientation_invite_ts_nullable to 2024-08-23T09:30:00Z."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/emily_chen/orientation_agenda.md",
                                                          "content_text": "# orientation agenda\nwelcome and access\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_6"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_orientation_emily2", "subject": "day-1 orientation - emily chen",
                           "body": "agenda attached", "to_emails": ["emily.chen@example.com"], "candidate_id": "cand_6",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_orientation_agenda_emily2", "message_id": "msg_orientation_emily2",
                           "filename": "orientation_agenda.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/emily_chen/orientation_agenda.md"}),
            Action(name="set_candidate_fields", kwargs={"candidate_id": "cand_6", "fields": {
                "orientation_invite_ts_nullable": "2024-08-23T09:30:00Z"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="068",
        instruction=(
            "You close out two checklist items for cand_2 (jane smith) and confirm by email. "
            "Update item_5 and item_6 to Completed. "
            "Send msg_closeout_jane to jane.smith@example.com with subject 'checklist closeout - jane smith' and body 'items completed', label label_2, and link thread_closeout_jane."
        ),
        actions=[
            Action(name="update_checklist_item", kwargs={"item_id": "item_5", "fields": {"status": "Completed"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_6", "fields": {"status": "Completed"}}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_closeout_jane", "subject": "checklist closeout - jane smith",
                           "body": "items completed", "to_emails": ["jane.smith@example.com"], "candidate_id": "cand_2",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_closeout_jane", "label_ids": ["label_2"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_closeout_jane",
                                                         "fields": {"thread_id_nullable": "thread_closeout_jane"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="069",
        instruction=(
            "You allocate peripherals for cand_3 (peter jones) and notify it. "
            "Assign MON-DELL-002 and HS-SONY-001 to cand_3. "
            "Send msg_peripherals_peter2 to it-assets@company.com with subject 'peripherals allocation - peter jones' and body 'monitor and headset assigned', label label_1, and link thread_peripherals_peter2."
        ),
        actions=[
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "MON-DELL-002", "candidate_id": "cand_3"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "HS-SONY-001", "candidate_id": "cand_3"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_peripherals_peter2", "subject": "peripherals allocation - peter jones",
                           "body": "monitor and headset assigned", "to_emails": ["it-assets@company.com"],
                           "candidate_id": "cand_3", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_peripherals_peter2", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_peripherals_peter2", "fields": {
                "thread_id_nullable": "thread_peripherals_peter2"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="070",
        instruction=(
            "You add provisioning notes for cand_5 (alex thompson) to the existing request thread. "
            "You write /onboarding/alex_thompson/provisioning_notes.md as text/markdown with 'notes:\n- slack provisioned as planned\n'. "
            "You attach it to msg_10 using the next sequential attachment id and label the email label_1. "
            "You log 'linked provisioning notes to msg_10'."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/alex_thompson/provisioning_notes.md",
                           "content_text": "notes:\n- slack provisioned as planned\n", "mime_type": "text/markdown",
                           "candidate_id": "cand_5"}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_0017", "message_id": "msg_10", "filename": "provisioning_notes.md",
                           "mime_type": "text/markdown",
                           "file_path": "/onboarding/alex_thompson/provisioning_notes.md"}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_10", "label_ids": ["label_1"]}),
            Action(name="insert_terminal_log", kwargs={"message_text": "linked provisioning notes to msg_10"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="072",
        instruction=(
            "You nudge cand_2 (jane smith) with a brief status check. The final state includes a sent email record with id msg_nudge_jane to ['jane.smith@example.com'] using subject 'status check - jane smith' and body 'just checking in', labeled Onboarding-Reminder (label_2), and linked under thread 'thread_nudge_jane'."
        ),
        actions=[
            Action(name="insert_email", kwargs={
                "message_id": "msg_nudge_jane",
                "subject": "status check - jane smith",
                "body": "just checking in",
                "to_emails": ["jane.smith@example.com"],
                "candidate_id": "cand_2",
                "draft_flag": False,
                "sent_flag": True
            }),
            Action(name="add_labels_to_email", kwargs={
                "message_id": "msg_nudge_jane",
                "label_ids": ["label_2"]
            }),
            Action(name="update_email_metadata", kwargs={
                "message_id": "msg_nudge_jane",
                "fields": {"thread_id_nullable": "thread_nudge_jane"}
            }),
        ],
        outputs=["ok"],
    ),
    # FIXED Task 073 (remove non-executable thread update, make parameters deterministic)
    Task(
        annotator="v2",
        user_id="073",
        instruction=(
            "You send a concise checklist reminder for cand_7 (robert singh). "
            "Use /onboarding/robert_singh/pending_tasks.md as text/markdown with '- account setup\\n- code repository access\\n'. "
            "Send msg_reminder_robert2 to ['robert.singh@example.com'] with subject 'pending tasks - robert singh' and body 'please complete', labeled label_2. "
            "Update item_15 and item_16 to 'Reminder Sent' with reminder_email_message_id_nullable 'msg_reminder_robert2'."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/robert_singh/pending_tasks.md",
                                                          "content_text": "- account setup\n- code repository access\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_7"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_reminder_robert2", "subject": "pending tasks - robert singh",
                           "body": "please complete", "to_emails": ["robert.singh@example.com"],
                           "candidate_id": "cand_7", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_reminder_robert2", "label_ids": ["label_2"]}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_15", "fields": {"status": "Reminder Sent",
                                                                                          "reminder_email_message_id_nullable": "msg_reminder_robert2"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_16", "fields": {"status": "Reminder Sent",
                                                                                          "reminder_email_message_id_nullable": "msg_reminder_robert2"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="074",
        instruction=(
            "You nudge cand_4 (maria rodriguez) on design access by reminder and item updates. "
            "Send msg_design_reminder_maria to maria.rodriguez@example.com with subject 'pending design access - maria rodriguez' and body 'please complete', label label_2, update item_9 and item_10 to 'Reminder Sent', and link thread_design_reminder_maria."
        ),
        actions=[
            Action(name="insert_email", kwargs={"message_id": "msg_design_reminder_maria",
                                                "subject": "pending design access - maria rodriguez",
                                                "body": "please complete", "to_emails": ["maria.rodriguez@example.com"],
                                                "candidate_id": "cand_4", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_design_reminder_maria", "label_ids": ["label_2"]}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_9", "fields": {"status": "Reminder Sent",
                                                                                         "reminder_sent_flag": True,
                                                                                         "reminder_email_message_id_nullable": "msg_design_reminder_maria"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_10", "fields": {"status": "Reminder Sent",
                                                                                          "reminder_sent_flag": True,
                                                                                          "reminder_email_message_id_nullable": "msg_design_reminder_maria"}}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_design_reminder_maria", "fields": {
                "thread_id_nullable": "thread_design_reminder_maria"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="075",
        instruction=(
            "You replace the assigned monitor for cand_3 (peter jones) and inform it. "
            "You release MON-LG-001 and assign MON-DELL-001 to cand_3, then send msg_monitor_swap_peter to it-assets@company.com with subject 'monitor swap - peter jones' and body 'lg to dell', labeled label_1 and linked under thread_monitor_swap_peter. "
            "You also log 'swapped monitor for cand_3 from MON-LG-001 to MON-DELL-001'."
        ),
        actions=[
            Action(name="release_inventory_asset", kwargs={"asset_tag": "MON-LG-001"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "MON-DELL-001", "candidate_id": "cand_3"}),
            Action(name="insert_email", kwargs={
                "message_id": "msg_monitor_swap_peter",
                "subject": "monitor swap - peter jones",
                "body": "lg to dell",
                "to_emails": ["it-assets@company.com"],
                "candidate_id": "cand_3",
                "draft_flag": False,
                "sent_flag": True
            }),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_monitor_swap_peter", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={
                "message_id": "msg_monitor_swap_peter",
                "fields": {"thread_id_nullable": "thread_monitor_swap_peter"}
            }),
            Action(name="insert_terminal_log", kwargs={
                "message_text": "swapped monitor for cand_3 from MON-LG-001 to MON-DELL-001"
            }),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="076",
        instruction=(
            "You send an updated welcome note for cand_1 (john doe). You save /onboarding/john_doe/welcome_update.md as text/markdown with '# welcome update\\nupdated docs\\n', "
            "and you send msg_welcome_update_john to john.doe@example.com using subject 'welcome update - john doe' and body 'updated docs', labeled with label_6 and attaching that file."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/john_doe/welcome_update.md",
                                                          "content_text": "# welcome update\nupdated docs\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_1"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_welcome_update_john", "subject": "welcome update - john doe",
                           "body": "updated docs", "to_emails": ["john.doe@example.com"], "candidate_id": "cand_1",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_welcome_update_john", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_welcome_update_john", "message_id": "msg_welcome_update_john",
                           "filename": "welcome_update.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/john_doe/welcome_update.md"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="077",
        instruction=(
            "You confirm orientation readiness for cand_6 (emily chen) with a simple invite. "
            "Send msg_orientation_ready_emily to emily.chen@example.com with subject 'orientation ready - emily chen' and body 'access ok', label label_4, and link thread_orientation_ready_emily."
        ),
        actions=[
            Action(name="insert_email",
                   kwargs={"message_id": "msg_orientation_ready_emily", "subject": "orientation ready - emily chen",
                           "body": "access ok", "to_emails": ["emily.chen@example.com"], "candidate_id": "cand_6",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_orientation_ready_emily", "label_ids": ["label_4"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_orientation_ready_emily", "fields": {
                "thread_id_nullable": "thread_orientation_ready_emily"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="078",
        instruction=(
            "You allocate a docking station for cand_5 (alex thompson) and notify it. "
            "Assign DS-DELL-001 to cand_5. "
            "Send msg_dock_alex to it-assets@company.com with subject 'dock allocation - alex thompson' and body 'dock assigned', label label_1, and link thread_dock_alex."
        ),
        actions=[
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "DS-DELL-001", "candidate_id": "cand_5"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_dock_alex", "subject": "dock allocation - alex thompson",
                           "body": "dock assigned", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_5",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_dock_alex", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_dock_alex", "fields": {"thread_id_nullable": "thread_dock_alex"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="079",
        instruction=(
            "You attach phone setup notes for cand_4 (maria rodriguez) to the existing phone request thread. "
            "Save /onboarding/maria_rodriguez/phone_setup.md as text/markdown with 'phone setup for maria'. "
            "Attach it to msg_12 using the next sequential attachment id, keep label_1 on the email, and link thread_phone_setup_maria."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/maria_rodriguez/phone_setup.md",
                                                          "content_text": "phone setup for maria",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_4"}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_0019", "message_id": "msg_12", "filename": "phone_setup.md",
                           "mime_type": "text/markdown", "file_path": "/onboarding/maria_rodriguez/phone_setup.md"}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_12", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_12", "fields": {"thread_id_nullable": "thread_phone_setup_maria"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="080",
        instruction=(
            "You allocate a headset for cand_2 (jane smith) and confirm by email. "
            "Assign HS-BOSE-001 to cand_2. "
            "Send msg_headset_jane to it-assets@company.com with subject 'headset allocation - jane smith' and body 'headset assigned', label label_1, and link thread_headset_jane."
        ),
        actions=[
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "HS-BOSE-001", "candidate_id": "cand_2"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_headset_jane", "subject": "headset allocation - jane smith",
                           "body": "headset assigned", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_2",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_headset_jane", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_headset_jane", "fields": {"thread_id_nullable": "thread_headset_jane"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="081",
        instruction=(
            "You complete welcome confirmation for cand_1 (john doe). "
            "Use message_id=msg_welcome_confirm_81 with subject 'welcome confirmation - john doe' and body 'welcome confirmed', "
            "to_emails=['john.doe@example.com'], label_id=label_6, "
            "file_path=/onboarding/john_doe/welcome_confirm.md (text/markdown, '# welcome confirmed\\nsee details inside\\n'), "
            "attach_id=attach_welcome_confirm_81."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/john_doe/welcome_confirm.md",
                                                          "content_text": "# welcome confirmed\nsee details inside\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_1"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_welcome_confirm_81", "subject": "welcome confirmation - john doe",
                           "body": "welcome confirmed", "to_emails": ["john.doe@example.com"], "candidate_id": "cand_1",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_welcome_confirm_81", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_welcome_confirm_81", "message_id": "msg_welcome_confirm_81",
                           "filename": "welcome_confirm.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/john_doe/welcome_confirm.md"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="082",
        instruction=(
            "You send the orientation invite for cand_2 (jane smith). You save /onboarding/jane_smith/orientation_agenda.md as text/markdown with '# orientation agenda\\nwelcome and setup\\n', "
            "and you send msg_orientation_82 to ['jane.smith@example.com'] using subject 'orientation invite - jane smith' and body 'agenda attached', labeled with label_4 and attaching the agenda."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/jane_smith/orientation_agenda.md",
                                                          "content_text": "# orientation agenda\nwelcome and setup\n",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_2"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_orientation_82", "subject": "orientation invite - jane smith",
                           "body": "agenda attached", "to_emails": ["jane.smith@example.com"], "candidate_id": "cand_2",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_orientation_82", "label_ids": ["label_4"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_orientation_agenda_82", "message_id": "msg_orientation_82",
                           "filename": "orientation_agenda.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/jane_smith/orientation_agenda.md"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="083",
        instruction=(
            "You send a manager introduction for cand_3 (peter jones). "
            "Use message_id=msg_intro_83 with subject 'manager introduction - peter jones' and body 'welcome and intro', "
            "to_emails=['peter.jones@example.com','mike.nguyen@example.com'], label_id=label_5, thread_id=thread_intro_83. "
            "Also stamp the candidate with manager_intro_invite_ts 2025-01-01T10:30:00Z."
        ),
        actions=[
            Action(name="insert_email",
                   kwargs={"message_id": "msg_intro_83", "subject": "manager introduction - peter jones",
                           "body": "welcome and intro",
                           "to_emails": ["peter.jones@example.com", "mike.nguyen@example.com"],
                           "candidate_id": "cand_3", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_intro_83", "label_ids": ["label_5"]}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_intro_83", "fields": {"thread_id_nullable": "thread_intro_83"}}),
            Action(name="set_candidate_fields", kwargs={"candidate_id": "cand_3", "fields": {
                "manager_intro_invite_ts_nullable": "2025-01-01T10:30:00Z"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="084",
        instruction=(
            "You send a concise checklist reminder for cand_1 (john doe). "
            "Use message_id=msg_reminder_84 with subject 'pending items - john doe' and body 'please complete items', "
            "to_emails=['john.doe@example.com'], label_id=label_2, thread_id=thread_reminder_84. "
            "Mark item_3 and item_4 as 'Reminder Sent' with reminder_sent_flag true and reminder_email_message_id_nullable msg_reminder_84."
        ),
        actions=[
            Action(name="insert_email", kwargs={"message_id": "msg_reminder_84", "subject": "pending items - john doe",
                                                "body": "please complete items", "to_emails": ["john.doe@example.com"],
                                                "candidate_id": "cand_1", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_reminder_84", "label_ids": ["label_2"]}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_3", "fields": {"status": "Reminder Sent",
                                                                                         "reminder_sent_flag": True,
                                                                                         "reminder_email_message_id_nullable": "msg_reminder_84"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_4", "fields": {"status": "Reminder Sent",
                                                                                         "reminder_sent_flag": True,
                                                                                         "reminder_email_message_id_nullable": "msg_reminder_84"}}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_reminder_84", "fields": {"thread_id_nullable": "thread_reminder_84"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="085",
        instruction=(
            "You confirm the asset handoff for cand_7 (robert singh). The final state includes the request asset_req_5 marked Sent with email_message_id msg_assets_handoff_85, a JSON artifact at /onboarding/robert_singh/asset_request.json containing {'candidate':'cand_7','asset_type':'Laptop','requested_ts':'2024-08-06T14:20:00Z'}, and a sent email record msg_assets_handoff_85 to ['it-assets@company.com'] using subject 'asset handoff - robert singh' and body 'handoff confirmed', labeled Asset-Request (label_1)."
        ),
        actions=[
            Action(name="upsert_json_artifact", kwargs={
                "file_path": "/onboarding/robert_singh/asset_request.json",
                "content_obj": {"candidate": "cand_7", "asset_type": "Laptop", "requested_ts": "2024-08-06T14:20:00Z"},
                "candidate_id": "cand_7"
            }),
            Action(name="insert_email", kwargs={
                "message_id": "msg_assets_handoff_85",
                "subject": "asset handoff - robert singh",
                "body": "handoff confirmed",
                "to_emails": ["it-assets@company.com"],
                "candidate_id": "cand_7",
                "draft_flag": False,
                "sent_flag": True
            }),
            Action(name="add_labels_to_email", kwargs={
                "message_id": "msg_assets_handoff_85",
                "label_ids": ["label_1"]
            }),
            Action(name="update_asset_request", kwargs={
                "request_id": "asset_req_5",
                "fields": {"status": "Sent", "email_message_id_nullable": "msg_assets_handoff_85"}
            }),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="086",
        instruction=(
            "You confirm phone allocation for cand_4 (maria rodriguez). "
            "Use asset_tag=PH-IPHONE-002 to assign to cand_4, "
            "message_id=msg_phone_alloc_86 with subject 'phone allocation - maria rodriguez' and body 'iphone assigned', "
            "to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_phone_alloc_86."
        ),
        actions=[
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "PH-IPHONE-002", "candidate_id": "cand_4"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_phone_alloc_86", "subject": "phone allocation - maria rodriguez",
                           "body": "iphone assigned", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_4",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_phone_alloc_86", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_phone_alloc_86",
                                                         "fields": {"thread_id_nullable": "thread_phone_alloc_86"}}),
            Action(name="insert_terminal_log", kwargs={"message_text": "phone PH-IPHONE-002 assigned to cand_4"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="087",
        instruction=(
            "You record an access summary for cand_2 (jane smith) and notify support. "
            "Checks: ('Slack','Pass','ok'), ('GitHub','Pending','awaiting sso'). "
            "Use message_id=msg_access_summary_87 with subject 'access summary - jane smith' and body 'status included', "
            "to_emails=['it-support@company.com'], label_id=label_7."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_2", "system_name": "Slack", "status": "Pass", "note_nullable": "ok"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_2", "system_name": "GitHub", "status": "Pending",
                           "note_nullable": "awaiting sso"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_access_summary_87", "subject": "access summary - jane smith",
                           "body": "status included", "to_emails": ["it-support@company.com"], "candidate_id": "cand_2",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email",
                   kwargs={"message_id": "msg_access_summary_87", "label_ids": ["label_7"]}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="088",
        instruction=(
            "You send a week-one reminder for cand_5 (alex thompson). "
            "Use message_id=msg_week1_88 with subject 'pending items - alex thompson' and body 'please review', "
            "to_emails=['alex.thompson@example.com'], label_id=label_2, thread_id=thread_week1_88. "
            "Update item_13 and item_14 to 'Reminder Sent' with reminder_sent_flag true and reminder_email_message_id_nullable msg_week1_88."
        ),
        actions=[
            Action(name="insert_email",
                   kwargs={"message_id": "msg_week1_88", "subject": "pending items - alex thompson",
                           "body": "please review", "to_emails": ["alex.thompson@example.com"],
                           "candidate_id": "cand_5", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_week1_88", "label_ids": ["label_2"]}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_13", "fields": {"status": "Reminder Sent",
                                                                                          "reminder_sent_flag": True,
                                                                                          "reminder_email_message_id_nullable": "msg_week1_88"}}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_14", "fields": {"status": "Reminder Sent",
                                                                                          "reminder_sent_flag": True,
                                                                                          "reminder_email_message_id_nullable": "msg_week1_88"}}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_week1_88", "fields": {"thread_id_nullable": "thread_week1_88"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="089",
        instruction=(
            "You confirm a laptop swap for cand_3 (peter jones) from LT-DELL-002 to LT-MBP-002 and notify it assets. "
            "Use message_id=msg_swap_89 with subject 'asset swap - peter jones' and body 'dell to mbp', "
            "to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_swap_89."
        ),
        actions=[
            Action(name="release_inventory_asset", kwargs={"asset_tag": "LT-DELL-002"}),
            Action(name="assign_inventory_asset", kwargs={"asset_tag": "LT-MBP-002", "candidate_id": "cand_3"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_swap_89", "subject": "asset swap - peter jones", "body": "dell to mbp",
                           "to_emails": ["it-assets@company.com"], "candidate_id": "cand_3", "draft_flag": False,
                           "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_swap_89", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_swap_89", "fields": {"thread_id_nullable": "thread_swap_89"}}),
        ],
        outputs=["ok"],
    ),
    # FIXED Task 090 (use deterministic sequential attachment_id)
    Task(
        annotator="v2",
        user_id="090",
        instruction=(
            "You confirm policy delivery for cand_2 (jane smith). "
            "Use /onboarding/jane_smith/company_policies_note.md as text/markdown with 'please review the policies'. "
            "Send msg_policy_90 to ['jane.smith@example.com'] with subject 'policies - jane smith' and body 'please review', labeled label_6, "
            "and attach that note with attachment_id attach_0021."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/jane_smith/company_policies_note.md",
                           "content_text": "please review the policies", "mime_type": "text/markdown",
                           "candidate_id": "cand_2"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_policy_90", "subject": "policies - jane smith", "body": "please review",
                           "to_emails": ["jane.smith@example.com"], "candidate_id": "cand_2", "draft_flag": False,
                           "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_policy_90", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_0021", "message_id": "msg_policy_90",
                           "filename": "company_policies_note.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/jane_smith/company_policies_note.md"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="091",
        instruction=(
            "You send a benefits reminder for cand_6 (emily chen). "
            "Use message_id=msg_benefits_91 with subject 'benefits enrollment - emily chen' and body 'enroll by friday', "
            "to_emails=['emily.chen@example.com'], label_id=label_2, thread_id=thread_benefits_91."
        ),
        actions=[
            Action(name="insert_email",
                   kwargs={"message_id": "msg_benefits_91", "subject": "benefits enrollment - emily chen",
                           "body": "enroll by friday", "to_emails": ["emily.chen@example.com"],
                           "candidate_id": "cand_6", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_benefits_91", "label_ids": ["label_2"]}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_benefits_91", "fields": {"thread_id_nullable": "thread_benefits_91"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="092",
        instruction=(
            "You confirm desk peripherals for cand_5 (alex thompson) and notify it assets. "
            "Use message_id=msg_peripherals_92 with subject 'desk peripherals - alex thompson' and body 'monitor and dock set', "
            "to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_peripherals_92. "
            "Add a short log 'peripherals confirmed for cand_5'."
        ),
        actions=[
            Action(name="insert_email",
                   kwargs={"message_id": "msg_peripherals_92", "subject": "desk peripherals - alex thompson",
                           "body": "monitor and dock set", "to_emails": ["it-assets@company.com"],
                           "candidate_id": "cand_5", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_peripherals_92", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_peripherals_92",
                                                         "fields": {"thread_id_nullable": "thread_peripherals_92"}}),
            Action(name="insert_terminal_log", kwargs={"message_text": "peripherals confirmed for cand_5"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="093",
        instruction=(
            "You send a brief welcome check-in for cand_4 (maria rodriguez) and note the outreach in a short file. "
            "Use message_id=msg_checkin_93 with subject 'welcome check-in - maria rodriguez' and body 'how is the first week going', "
            "to_emails=['maria.rodriguez@example.com'], label_id=label_6, thread_id=thread_checkin_93, "
            "and store /onboarding/maria_rodriguez/checkin_93.md as text/markdown with 'check-in sent for week-1'."
        ),
        actions=[
            Action(name="upsert_onboarding_file",
                   kwargs={"file_path": "/onboarding/maria_rodriguez/checkin_93.md",
                           "content_text": "check-in sent for week-1",
                           "mime_type": "text/markdown",
                           "candidate_id": "cand_4"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_checkin_93",
                           "subject": "welcome check-in - maria rodriguez",
                           "body": "how is the first week going",
                           "to_emails": ["maria.rodriguez@example.com"],
                           "candidate_id": "cand_4",
                           "draft_flag": False,
                           "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_checkin_93", "label_ids": ["label_6"]}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_checkin_93", "fields": {"thread_id_nullable": "thread_checkin_93"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="094",
        instruction=(
            "You notify support of final access for cand_3 (peter jones). "
            "Checks: ('Email','Pass','ok'), ('SSO','Pass','ok'). "
            "Use message_id=msg_access_final_94 with subject 'access final - peter jones' and body 'all set', "
            "to_emails=['it-support@company.com'], label_id=label_7."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_3", "system_name": "Email", "status": "Pass", "note_nullable": "ok"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_3", "system_name": "SSO", "status": "Pass", "note_nullable": "ok"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_access_final_94", "subject": "access final - peter jones",
                           "body": "all set", "to_emails": ["it-support@company.com"], "candidate_id": "cand_3",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_access_final_94", "label_ids": ["label_7"]}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="095",
        instruction=(
            "You send a benefits follow-up for cand_1 (john doe). "
            "Use message_id=msg_benefits_95 with subject 'benefits follow-up - john doe' and body 'please finish enrollment', "
            "to_emails=['john.doe@example.com'], label_id=label_2, thread_id=thread_benefits_95."
        ),
        actions=[
            Action(name="insert_email",
                   kwargs={"message_id": "msg_benefits_95", "subject": "benefits follow-up - john doe",
                           "body": "please finish enrollment", "to_emails": ["john.doe@example.com"],
                           "candidate_id": "cand_1", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_benefits_95", "label_ids": ["label_2"]}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_benefits_95", "fields": {"thread_id_nullable": "thread_benefits_95"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="096",
        instruction=(
            "You confirm asset return for cand_2 (jane smith) of LT-DELL-003 and notify it assets. "
            "Use message_id=msg_asset_return_96 with subject 'asset return - jane smith' and body 'device received', "
            "to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_asset_return_96."
        ),
        actions=[
            Action(name="release_inventory_asset", kwargs={"asset_tag": "LT-DELL-003"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_asset_return_96", "subject": "asset return - jane smith",
                           "body": "device received", "to_emails": ["it-assets@company.com"], "candidate_id": "cand_2",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_asset_return_96", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata", kwargs={"message_id": "msg_asset_return_96",
                                                         "fields": {"thread_id_nullable": "thread_asset_return_96"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="097",
        instruction=(
            "You send a brief onboarding reminder for cand_6 (emily chen). "
            "Use message_id=msg_reminder_97 with subject 'onboarding reminder - emily chen' and body 'please finish tasks', "
            "to_emails=['emily.chen@example.com'], label_id=label_2, thread_id=thread_reminder_97. "
            "Update item_15 to 'Reminder Sent' with reminder_sent_flag true and reminder_email_message_id_nullable msg_reminder_97."
        ),
        actions=[
            Action(name="insert_email",
                   kwargs={"message_id": "msg_reminder_97", "subject": "onboarding reminder - emily chen",
                           "body": "please finish tasks", "to_emails": ["emily.chen@example.com"],
                           "candidate_id": "cand_6", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_reminder_97", "label_ids": ["label_2"]}),
            Action(name="update_checklist_item", kwargs={"item_id": "item_15", "fields": {"status": "Reminder Sent",
                                                                                          "reminder_sent_flag": True,
                                                                                          "reminder_email_message_id_nullable": "msg_reminder_97"}}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_reminder_97", "fields": {"thread_id_nullable": "thread_reminder_97"}}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="098",
        instruction=(
            "You confirm final welcome for cand_5 (alex thompson). You create /onboarding/alex_thompson/welcome_resources.md as text/markdown with 'resources and links', "
            "and you send msg_welcome_final_98 to alex.thompson@example.com using subject 'welcome final - alex thompson' and body 'see resources', labeled with label_6 and attaching that file."
        ),
        actions=[
            Action(name="upsert_onboarding_file", kwargs={"file_path": "/onboarding/alex_thompson/welcome_resources.md",
                                                          "content_text": "resources and links",
                                                          "mime_type": "text/markdown", "candidate_id": "cand_5"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_welcome_final_98", "subject": "welcome final - alex thompson",
                           "body": "see resources", "to_emails": ["alex.thompson@example.com"],
                           "candidate_id": "cand_5", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_welcome_final_98", "label_ids": ["label_6"]}),
            Action(name="insert_attachment_record",
                   kwargs={"attachment_id": "attach_welcome_resources_98", "message_id": "msg_welcome_final_98",
                           "filename": "welcome_resources.md", "mime_type": "text/markdown",
                           "file_path": "/onboarding/alex_thompson/welcome_resources.md"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="099",
        instruction=(
            "You send a brief systems check for cand_7 (robert singh). "
            "Checks: ('Email','Pass','ok'), ('Slack','Pass','ok'). "
            "Use message_id=msg_systems_check_99 with subject 'systems check - robert singh' and body 'ready to go', "
            "to_emails=['it-support@company.com'], label_id=label_7."
        ),
        actions=[
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_7", "system_name": "Email", "status": "Pass", "note_nullable": "ok"}),
            Action(name="insert_access_check",
                   kwargs={"candidate_id": "cand_7", "system_name": "Slack", "status": "Pass", "note_nullable": "ok"}),
            Action(name="insert_email",
                   kwargs={"message_id": "msg_systems_check_99", "subject": "systems check - robert singh",
                           "body": "ready to go", "to_emails": ["it-support@company.com"], "candidate_id": "cand_7",
                           "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_systems_check_99", "label_ids": ["label_7"]}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="v2",
        user_id="100",
        instruction=(
            "You confirm laptop pickup for cand_6 (emily chen) and notify it assets. "
            "Use message_id=msg_pickup_100 with subject 'laptop pickup - emily chen' and body 'scheduled 10am', "
            "to_emails=['it-assets@company.com'], label_id=label_1, thread_id=thread_pickup_100."
        ),
        actions=[
            Action(name="insert_email", kwargs={"message_id": "msg_pickup_100", "subject": "laptop pickup - emily chen",
                                                "body": "scheduled 10am", "to_emails": ["it-assets@company.com"],
                                                "candidate_id": "cand_6", "draft_flag": False, "sent_flag": True}),
            Action(name="add_labels_to_email", kwargs={"message_id": "msg_pickup_100", "label_ids": ["label_1"]}),
            Action(name="update_email_metadata",
                   kwargs={"message_id": "msg_pickup_100", "fields": {"thread_id_nullable": "thread_pickup_100"}}),
        ],
        outputs=["ok"],
    ),
]
