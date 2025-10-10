from domains.dto import Task, Action
TASKS = [

    Task(
        annotator="0",
        user_id="V4_Task_001",
        instruction=(
            "You close completed checklist items for emily.chen@example.com (start 2024-08-26), then send and label a one-week checklist reminder with cutoff 2024-09-02."),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "emily.chen@example.com", "start_date": "2024-08-26"}),
            Action(name="close_completed_checklist_items", kwargs={"candidate_id": "cand_6", "due_date_lte": "2024-09-02"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-02"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_6", "file_path": "/onboarding/Emily_Chen/pending_tasks.md"}),
            Action(name="generate_and_send_email",kwargs={"task": "checklist_reminder", "to_emails": ["emily.chen@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_6","attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"]}),
            Action(name="modify_email_labels",kwargs={"candidate_id": "cand_6", "subject": "Pending Onboarding Tasks","add_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded",kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-02", "subject": "Pending Onboarding Tasks","item_ids": []}),
            Action(name="update_candidate_status_fields",kwargs={"candidate_id": "cand_6", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_002",
        instruction=(
            "You finalize the allocation for robert.singh@example.com (start 2024-09-02) per policy: allocate the first available inventory, "
            "record the allocation on the request, generate an allocation receipt, and email the employee ‘Asset Allocation – Robert Singh’ with the receipt attached."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_5"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_7","file_path": "/onboarding/Robert_Singh/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_5", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["robert.singh@example.com"],"subject": "Asset Allocation – Robert Singh","candidate_id": "cand_7","attachment_file_paths": ["/onboarding/Robert_Singh/allocation_receipt.json"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_5","status": "Completed","email_message_id": "msg_15"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_7"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_003",
        instruction=(
            "You finalize equipment provisioning for jane.smith@example.com (start 2024-08-05) in line with the Equipment Provisioning policy: "
            "prepare the request artifact, email IT using 'Asset Provisioning – Jane Smith' and ensure the required 'Asset-Request' label; record "
            "the email id and mark the request Sent; allocate the first available inventory and record the allocation; generate an allocation receipt "
            "and send the employee a confirmation with the receipt."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/asset_request.json","payload": {"request_id": "asset_req_1"}}),
            Action(name="generate_and_send_email",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Jane Smith", "candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_1", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_1"}),
            Action(name="write_onboarding_file",kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/allocation_receipt.json", "mime_type": "application/json","payload": {"request_id": "asset_req_1", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="generate_and_send_email",kwargs={"to_emails": ["jane.smith@example.com"], "subject": "Asset Allocation – Jane Smith", "candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/allocation_receipt.json"]}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_004",
        instruction=(
            "You record day-1 access checks for emily.chen@example.com (start 2024-08-26) on Email=pass, SSO=fail, Slack=pass, GitHub=pass; "
            "you send a day-1 orientation invite, then notify IT of access gaps."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "emily.chen@example.com", "start_date": "2024-08-26"}),
            Action(name="record_access_checks", kwargs={"candidate_id": "cand_6", "checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "fail"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["emily.chen@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_6"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_6","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Access Gaps","candidate_id": "cand_6"}),
        ],
        outputs=['"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_005",
        instruction=(
            "You operate on the existing asset request for jane.smith@example.com (start 2024-08-05). "
            "You send the 'Asset Provisioning – Jane Smith' email and store its message id on the request, apply the 'Asset-Request' label, "
            "allocate an available asset, write /onboarding/Jane_Smith/allocation_receipt.json, and send 'Asset Allocation – Jane Smith' with the receipt attached."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/asset_request.json","payload": {"request_id": "asset_req_1"}}),
            Action(name="generate_and_send_email",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Jane Smith", "candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_1", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_1"}),
            Action(name="write_onboarding_file",kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/allocation_receipt.json", "mime_type": "application/json","payload": {"request_id": "asset_req_1", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="generate_and_send_email",kwargs={"to_emails": ["jane.smith@example.com"], "subject": "Asset Allocation – Jane Smith", "candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/allocation_receipt.json"]}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_006",
        instruction=(
            "You personalize and send the onboarding packet for peter.jones@example.com (start 2024-07-29) with policy/benefits attached, "
            "then send and label a checklist reminder (cutoff 2024-08-05)."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="read_onboarding_file", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="write_onboarding_file",kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/welcome_Peter_Jones.md", "mime_type": "text/markdown"}),
            Action(name="generate_and_send_email",kwargs={"task": "onboarding", "to_emails": ["peter.jones@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_3","attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf","/onboarding/Peter_Jones/welcome_Peter_Jones.md"]}),
            Action(name="update_candidate_status_fields",kwargs={"candidate_id": "cand_3", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_3", "status": "Pending", "due_date_lte": "2024-08-05"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/pending_tasks.md"}),
            Action(name="generate_and_send_email",kwargs={"task": "checklist_reminder", "to_emails": ["peter.jones@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_3","attachment_file_paths": ["/onboarding/Peter_Jones/pending_tasks.md"]}),
            Action(name="modify_email_labels",kwargs={"candidate_id": "cand_3", "subject": "Pending Onboarding Tasks","add_names": ["Onboarding-Reminder"]}),
            Action(name="update_candidate_status_fields",kwargs={"candidate_id": "cand_3", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_007",
        instruction=(
            "You send day-1 orientation and manager-intro invites for maria.rodriguez@example.com (start 2024-08-12) and record both invite timestamps."),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="generate_and_send_email",kwargs={"task": "orientation_invite", "to_emails": ["maria.rodriguez@example.com"], "subject": "Day-1 Orientation","candidate_id": "cand_4"}),
            Action(name="generate_and_send_email",kwargs={"task": "manager_intro", "to_emails": ["maria.rodriguez@example.com", "david.kim@example.com"], "subject": "Manager Intro","candidate_id": "cand_4"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_4", "orientation_invite_ts": "2025-09-01T00:00:00Z","manager_intro_invite_ts": "2025-09-01T00:00:00Z"})
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
    annotator="0",
    user_id="V4_Task_008",
    instruction=(
        "You verify day-1 access for maria.rodriguez@example.com (start 2024-08-12), then send the 'Welcome to the Team' packet "
        "(attach Company-Policies.pdf, Benefits-Guide.pdf, and the personalized markdown) and record the welcome email id."
    ),
    actions=[
        Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
        Action(name="record_access_checks", kwargs={"candidate_id": "cand_4", "checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "pass"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
        Action(name="read_onboarding_file", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
        Action(name="render_onboarding_welcome", kwargs={"candidate_id": "cand_4", "candidate_name": "Maria Rodriguez", "role_title": "UX Designer", "start_date": "2024-08-12"}),
        Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md","mime_type": "text/markdown"}),
        Action(name="generate_and_send_email", kwargs={"to_emails": ["maria.rodriguez@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_4","attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf","/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md"]}),
        Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_4", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
    ],
    outputs=['"success_flag": true', '"candidate_id":"cand_4"', '"message_id":"msg_15"', '"status":"Packet Sent"'],
),
 Task(
        annotator="0",
        user_id="V4_Task_009",
        instruction=(
            "You verify day‑1 access for alex.thompson@example.com (start 2024‑08‑19); you send 'Day‑1 Orientation' and 'Welcome to the Team' (policy PDFs + personalized markdown); then you run the one‑week checklist follow‑up (cutoff 2024‑08‑26): send 'Pending Onboarding Tasks' labeled 'Onboarding‑Reminder' with pending_tasks.md, record the welcome message id, set the follow‑up timestamp, and mark the reminded items."
            "You send the 'Day-1 Orientation' invite, you send the 'Welcome to the Team' packet (Company-Policies.pdf, Benefits-Guide.pdf, and the personalized markdown), and you complete the one‑week checklist follow‑up: email 'Pending Onboarding Tasks' (cutoff 2024-08-26) labeled 'Onboarding-Reminder' with pending_tasks.md; record the welcome email message id and onboarding status, set the checklist follow-up timestamp, and mark the reminded items with the email's message id."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="record_access_checks", kwargs={"candidate_id": "cand_5", "checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "pass"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["alex.thompson@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_5"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md","mime_type": "text/markdown"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["alex.thompson@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_5","attachment_file_paths": ["/library/Company-Policies.pdf","/library/Benefits-Guide.pdf","/onboarding/Alex_Thompson/welcome_Alex_Thompson.md"]}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_5","status": "Pending","due_date_lte": "2024-08-26"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/pending_tasks.md"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["alex.thompson@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_5","fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_16", "checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
            Action(name="mark_checklist_items_reminded", kwargs={"item_ids": ["item_13", "item_14"],"reminder_email_message_id": "msg_17","updated_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_010",
        instruction=(
            "You verify day-1 access for robert.singh@example.com (start 2024-09-02), send an orientation invite, then complete provisioning by "
            "sending and labeling the request, allocating inventory, and replying to the provisioning thread to acknowledge."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
            Action(name="record_access_checks", kwargs={"candidate_id": "cand_7","checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "pass"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
            Action(name="generate_and_send_email", kwargs={"task": "orientation_invite", "to_emails": ["robert.singh@example.com"], "subject": "Day-1 Orientation", "candidate_id": "cand_7"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_7", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_5"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/asset_request.json","payload": {"request_id": "asset_req_5", "candidate_id": "cand_7", "status": "Requested"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Robert Singh", "candidate_id": "cand_7","attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_5", "status": "Sent","candidate_id": "cand_7", "subject": "Asset Provisioning – Robert Singh",}),
            Action(name="modify_email_labels", kwargs={"candidate_id": "cand_7", "subject": "Asset Provisioning – Robert Singh","add_names": ["Asset-Request"]}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_5", }),
            Action(name="reply_to_email_thread", kwargs={"candidate_id": "cand_7", "subject": "Asset Provisioning – Robert Singh",  "task": "acknowledge"})
        ],
        outputs=['"candidate_id":"cand_7"'],
    ),
 Task(
    annotator="0",
    user_id="V4_Task_011",
    instruction=(
        "You complete provisioning for alex.thompson@example.com (start 2024-08-19): email IT with subject 'Asset Provisioning – Alex Thompson' labeled 'Asset-Request' attaching /onboarding/Alex_Thompson/asset_request.json; mark asset_req_4 Sent using that email's message id; allocate the first available asset; write the receipt to /onboarding/Alex_Thompson/allocation_receipt.json; and send the employee a confirmation with subject 'Asset Allocation – Alex Thompson' attaching the receipt."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_4"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/asset_request.json","payload": {"request_id": "asset_req_4", "asset_type": "Laptop"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Alex Thompson","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_4","status": "Sent","email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_4"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_4", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["alex.thompson@example.com"],"subject": "Asset Allocation – Alex Thompson","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/allocation_receipt.json"]}),
            ],
            outputs=['"success_flag": true', '"candidate_id":"cand_5"'],
            ),

    Task(
        annotator="0",
        user_id="V4_Task_012",
        instruction=(
            "You write an access summary for alex.thompson@example.com (start 2024-08-19), then send and label a one-week checklist reminder with cutoff 2024-08-26, "
            "mark pending items as reminded with the reminder email id, and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="summarize_access_checks", kwargs={"candidate_id": "cand_5"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/pending_tasks.md"}),
            Action(name="generate_and_send_email",kwargs={"task": "checklist_reminder", "to_emails": ["alex.thompson@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_5", "label_names": ["Onboarding-Reminder"],"attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"]}),
            Action(name="mark_checklist_items_reminded",kwargs={"item_ids": ["item_13", "item_14"], "reminder_email_message_id": "msg_15",}),
            Action(name="update_candidate_status_fields",kwargs={"candidate_id": "cand_5", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_013",
        instruction=(
            "You complete provisioning for maria.rodriguez@example.com (start 2024-08-12) by sending and labeling the request, "
            "allocating inventory and writing a receipt to /onboarding/Maria_Rodriguez/allocation_receipt.json, then sending an allocation confirmation that includes the receipt."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_3"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_4","file_path": "/onboarding/Maria_Rodriguez/asset_request.json","payload": {"request_id": "asset_req_3"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Maria Rodriguez","candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_3","status": "Sent","email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_3"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_4","file_path": "/onboarding/Maria_Rodriguez/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_3", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["maria.rodriguez@example.com"],"subject": "Asset Allocation – Maria Rodriguez","candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/allocation_receipt.json"]}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_014",
        instruction=(
            "You finalize equipment provisioning for alex.thompson@example.com (start 2024-08-19) in line with the Equipment"
            " Provisioning policy: prepare the request artifact and email IT using ‘Asset Provisioning – Alex Thompson’ with the required "
            "‘Asset-Request’ label; record the email id and mark the request Sent; allocate the first available inventory and record the allocation receipt."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="write_asset_request_file", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                "payload": {"request_id": "asset_req_4", "asset_type": "Laptop", "status": "Requested"}
            }),
            Action(name="generate_and_send_email", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Alex Thompson",
                "candidate_id": "cand_5",
                "attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"],
                "label_names": ["Asset-Request"]
            }),
            Action(name="update_asset_request_status", kwargs={
                "request_id": "asset_req_4",
                "status": "Sent",
                "email_message_id": "msg_15"
            }),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_4"}),
            Action(name="write_onboarding_file", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_4", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}
            }),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_015",
        instruction=(
            "You send and label a one-week checklist reminder for jane.smith@example.com (start 2024-08-05, cutoff 2024-08-12) and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_2", "status": "Pending", "due_date_lte": "2024-08-12"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/pending_tasks.md"}),
            Action(name="generate_and_send_email", kwargs={"task": "checklist_reminder","to_emails": ["jane.smith@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded", kwargs={"item_ids": ["item_4", "item_5", "item_6", "item_7"],"reminder_email_message_id": "msg_15","updated_ts": "2025-09-01T00:00:00Z"}),
            Action(name="update_candidate_status_fields",kwargs={"candidate_id": "cand_2", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),

    

    Task(
        annotator="0",
        user_id="V4_Task_016",
        instruction=(
            "You send a one-week onboarding checklist reminder for the employee at john.doe@example.com (cutoff 2024-08-08). You attach "
            "the pending tasks summary, label the email, and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "john.doe@example.com", "start_date": "2024-08-01"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_1", "status": "Pending", "due_date_lte": "2024-08-08"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "checklist_reminder", "to_emails": ["john.doe@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_1",
                           "attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"]}),
            Action(name="modify_email_labels", kwargs={"message_id": "msg_15", "add_names": ["Onboarding-Reminder"]}),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_1", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_1"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_017",
        instruction=(
            "You send a one-week onboarding checklist reminder for the employee at peter.jones@example.com (cutoff 2024-08-05). "
            "You attach the pending tasks summary, apply label, and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_3", "status": "Pending", "due_date_lte": "2024-08-05"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"to_emails": ["peter.jones@example.com"], "subject": "Pending Onboarding Tasks", "candidate_id": "cand_3",
                           "attachment_file_paths": ["/onboarding/Peter_Jones/pending_tasks.md"]}),
            Action(name="modify_email_labels", kwargs={"message_id": "msg_15", "add_names": ["Onboarding-Reminder"]}),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_3", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}
                           })
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_3"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_018",
        instruction=(
            "You send a one-week onboarding checklist reminder for the employee at maria.rodriguez@example.com (cutoff 2024-08-19). "
            "You attach the pending tasks summary, label the email, record the follow-up timestamp, and mark pending items as reminded."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_4", "status": "Pending", "due_date_lte": "2024-08-19"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "checklist_reminder", "to_emails": ["maria.rodriguez@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_4",
                           "attachment_file_paths": ["/onboarding/Maria_Rodriguez/pending_tasks.md"]}),
            Action(name="get_or_create_email_label", kwargs={"name": "Onboarding-Reminder"}),
            Action(name="modify_email_labels", kwargs={"message_id": "msg_15", "add_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded",
                   kwargs={"item_ids": ["item_9", "item_10"], "reminder_email_message_id": "msg_15", }),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_4", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_019",
        instruction=(
            "You send a one-week onboarding checklist reminder for the employee at emily.chen@example.com (cutoff 2024-09-02). "
            "You attach the pending tasks summary, label the email, and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "emily.chen@example.com", "start_date": "2024-08-26"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-02"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_6", "file_path": "/onboarding/Emily_Chen/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"to_emails": ["emily.chen@example.com"], "subject": "Pending Onboarding Tasks", "candidate_id": "cand_6",
                           "attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"]}),
            Action(name="get_or_create_email_label", kwargs={"name": "Onboarding-Reminder"}),
            Action(name="modify_email_labels", kwargs={"message_id": "msg_15", "add_names": ["Onboarding-Reminder"]}),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_6", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}
                           })
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_020",
        instruction=(
            "You send day-1 orientation and manager-intro invites for robert.singh@example.com (start 2024-09-02) and record both invite timestamps."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["robert.singh@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_7"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_7","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["robert.singh@example.com", "sarah.wilson@example.com"],"subject": "Manager Intro","candidate_id": "cand_7"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_7","manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"candidate_id":"cand_7"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_021",
        instruction=(
            "You send the 'Asset Provisioning – Alex Thompson' email for alex.thompson@example.com (start 2024-08-19), store its id on the request, "
            "apply the 'Asset-Request' label, and write /onboarding/Alex_Thompson/allocation_receipt.json."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/asset_request.json","payload": {"request_id": "asset_req_4"}}),
            Action(name="generate_and_send_email",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Alex Thompson", "candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"], "label_names": ["Asset-Request"], "add_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_4", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json","mime_type": "application/json", "payload": {"request_id": "asset_req_4"}}),
        ],
    outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_022",
        instruction=(
            "You ensure the 'Asset-Request' label is present on the 'Asset Provisioning – Jane Smith' email for jane.smith@example.com (start 2024-08-05) "
            "and then reply to the provisioning thread to acknowledge."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_1"}),
            Action(name="get_or_create_email_label", kwargs={"name": "Asset-Request"}),
            Action(name="modify_email_labels", kwargs={"message_id": "msg_3", "add_names": ["Asset-Request"]}),
            Action(name="reply_to_email_thread",kwargs={"candidate_id": "cand_2", "thread_id": "msg_3", "subject": "Asset Provisioning – Jane Smith"}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_023",
        instruction=(
            "You close completed checklist items for maria.rodriguez@example.com (start 2024-08-12), then send and label a checklist reminder "
            "(cutoff 2024-08-19) and record the follow-up timestamp."),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="close_completed_checklist_items", kwargs={"candidate_id": "cand_4", "due_date_lte": "2024-08-19"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_4", "status": "Pending", "due_date_lte": "2024-08-19"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/pending_tasks.md"}),
            Action(name="generate_and_send_email",kwargs={"task": "checklist_reminder", "to_emails": ["maria.rodriguez@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_4", "attachment_file_paths": ["/onboarding/Maria_Rodriguez/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded", kwargs={"item_ids": ["item_9", "item_10"], "reminder_email_message_id": "msg_15"}),
            Action(name="update_candidate_status_fields",kwargs={"candidate_id": "cand_4", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_024",
        instruction=(
            "You send and label a one-week checklist reminder for alex.thompson@example.com (start 2024-08-19, cutoff 2024-08-26) and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/pending_tasks.md"}),
            Action(name="generate_and_send_email", kwargs={"task": "checklist_reminder","to_emails": ["alex.thompson@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded", kwargs={"item_ids": ["item_13", "item_14"],"reminder_email_message_id": "msg_15"}),
            Action(name="update_candidate_status_fields",kwargs={"candidate_id": "cand_5", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_025",
        instruction=(
            "You send and label a one-week checklist reminder for john.doe@example.com (start 2024-08-01, cutoff 2024-08-08) and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "john.doe@example.com", "start_date": "2024-08-01"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_1", "status": "Pending", "due_date_lte": "2024-08-08"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/pending_tasks.md"}),
            Action(name="generate_and_send_email",kwargs={"task": "checklist_reminder", "to_emails": ["john.doe@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_1", "label_names": ["Onboarding-Reminder"],"attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"]}),
            Action(name="update_candidate_status_fields",kwargs={"candidate_id": "cand_1", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_1"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_026",
        instruction=(
            "You send a day-1 orientation invite for john.doe@example.com (start 2024-08-01), then send and label a one-week checklist "
            "reminder (cutoff 2024-08-08) and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "john.doe@example.com", "start_date": "2024-08-01"}),
            Action(name="generate_and_send_email", kwargs={"task": "orientation_invite", "to_emails": ["john.doe@example.com"], "subject": "Day-1 Orientation","candidate_id": "cand_1"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_1", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_1", "status": "Pending", "due_date_lte": "2024-08-08"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/pending_tasks.md"}),
            Action(name="generate_and_send_email",kwargs={"task": "checklist_reminder", "to_emails": ["john.doe@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_1","attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"]}),
            Action(name="modify_email_labels",kwargs={"candidate_id": "cand_1", "subject": "Pending Onboarding Tasks","add_names": ["Onboarding-Reminder"]}),
            Action(name="update_candidate_status_fields",kwargs={"candidate_id": "cand_1", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_1"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_027",
        instruction=(
            "You personalize and send the onboarding packet for emily.chen@example.com (start 2024-08-26) with policy/benefits attached, "
            "then send and label a one-week checklist reminder (cutoff 2024-09-02) and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "emily.chen@example.com", "start_date": "2024-08-26"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_6","file_path": "/onboarding/Emily_Chen/welcome_Emily_Chen.md","mime_type": "text/markdown","content_text": " Welcome, Emily Chen!\n\nRole: Marketing Specialist\nStart date: 2024-08-26\n\nWe’re excited to have you onboard. Please review the attached policy and benefits guides to prepare for Day 1."}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["emily.chen@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_6","attachment_file_paths": ["/library/Company-Policies.pdf","/library/Benefits-Guide.pdf","/onboarding/Emily_Chen/welcome_Emily_Chen.md"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_6","fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_6","file_path": "/onboarding/Emily_Chen/pending_tasks.md","due_date_lte": "2024-09-02"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["emily.chen@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_6","attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_6","fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_028",
        instruction=(
            "You operate on the existing asset request for maria.rodriguez@example.com (start 2024-08-12): send the 'Asset Provisioning – "
            "Maria Rodriguez' email, store its id on the request, apply the 'Asset-Request' label, allocate an available asset, and write "
            "/onboarding/Maria_Rodriguez/allocation_receipt.json."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_3"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/asset_request.json","payload": {"request_id": "asset_req_3"}}),
            Action(name="generate_and_send_email",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Maria Rodriguez", "candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_3", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_3"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_3", "status": "allocated", "asset_tag": "LT-DELL-001","asset_type": "Laptop"}}),
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_029",
        instruction=(
            "You personalize and send the onboarding packet for jane.smith@example.com (start 2024-08-05) with the standard policy "
            "and benefits attachments and record the welcome email id while marking the candidate 'Packet Sent'. Then you send a day-1 orientation invite."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="read_onboarding_file", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/welcome_Jane_Smith.md","mime_type": "text/markdown","content_text": " Welcome, Jane Smith!\n\nRole: Product Manager\nStart date: 2024-08-05\n\nWe’re excited to have you join us. Please review the attached policy and benefits guides to prepare for Day 1."}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["jane.smith@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_2","attachment_file_paths": ["/library/Company-Policies.pdf","/library/Benefits-Guide.pdf","/onboarding/Jane_Smith/welcome_Jane_Smith.md"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_2","fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"} }),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["jane.smith@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_2"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_2","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_030",
        instruction=(
            "You record day-1 access checks for peter.jones@example.com (start 2024-07-29): Email=pass, SSO=pass, Slack=fail, GitHub=pass. "
            "Then you send a day-1 orientation invite, record the invite timestamp as 2025-09-01T00:00:00Z, and notify IT of the access gaps."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="record_access_checks", kwargs={"candidate_id": "cand_3", "checks": [{"system_name": "Email",  "status": "pass"},{"system_name": "SSO",    "status": "pass"},{"system_name": "Slack",  "status": "fail"},{"system_name": "GitHub", "status": "pass"},]}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["peter.jones@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_3"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_3","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Access Gaps","candidate_id": "cand_3"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_3"'],
    ),
    Task(
    annotator="0",
    user_id="V4_Task_031",
    instruction=(
        "You verify day-1 access for maria.rodriguez@example.com (start 2024-08-12), then send the 'Welcome to the Team' packet "
        "(attach Company-Policies.pdf, Benefits-Guide.pdf, and the personalized markdown) and record the welcome email id."
    ),
    actions=[
        Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
        Action(name="record_access_checks", kwargs={"candidate_id": "cand_4", "checks": [
            {"system_name": "Email", "status": "pass"},
            {"system_name": "SSO", "status": "pass"},
            {"system_name": "Slack", "status": "pass"},
            {"system_name": "GitHub", "status": "pass"}
        ]}),
        Action(name="read_onboarding_file", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
        Action(name="render_onboarding_welcome", kwargs={"candidate_id": "cand_4", "candidate_name": "Maria Rodriguez", "role_title": "UX Designer", "start_date": "2024-08-12"}),
        Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md","mime_type": "text/markdown"}),
        Action(name="generate_and_send_email", kwargs={
            "to_emails": ["maria.rodriguez@example.com"],
            "subject": "Welcome to the Team",
            "candidate_id": "cand_4",
            "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf","/onboarding/Maria_Rodriguez/welcome_Maria_Rodriguez.md"]
        }),
        Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_4", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
    ],
    outputs=['"success_flag": true', '"candidate_id":"cand_4"', '"message_id":"msg_15"', '"status":"Packet Sent"'],
),
Task(
    annotator="0",
    user_id="V4_Task_032",
    instruction=(
        "You verify day-1 access for emily.chen@example.com (start 2024-08-26) and send a 'Day-1 Orientation' invite, recording the orientation_invite_ts."
    ),
    actions=[
        Action(name="find_candidate_by_email", kwargs={"candidate_email": "emily.chen@example.com", "start_date": "2024-08-26"}),
        Action(name="record_access_checks", kwargs={"candidate_id": "cand_6","checks": [
            {"system_name": "Email", "status": "pass"},
            {"system_name": "SSO", "status": "pass"},
            {"system_name": "Slack", "status": "pass"},
            {"system_name": "GitHub", "status": "pass"}
        ]}),
        Action(name="generate_and_send_email", kwargs={"to_emails": ["emily.chen@example.com"], "subject": "Day-1 Orientation", "candidate_id": "cand_6"}),
        Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_6", "orientation_invite_ts": "2025-09-01T00:00:00Z"})
    ],
    outputs=['"success_flag": true', '"candidate_id":"cand_6"'],
),
Task(
    annotator="0",
    user_id="V4_Task_033",
    instruction=(
        "You verify day-1 access for robert.singh@example.com (start 2024-09-02), personalize and send the 'Welcome to the Team' packet "
        "(attach Company-Policies.pdf, Benefits-Guide.pdf, and the personalized markdown), and store the welcome email id."
    ),
    actions=[
        Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
        Action(name="record_access_checks", kwargs={"candidate_id": "cand_7", "checks": [
            {"system_name": "Email", "status": "pass"},
            {"system_name": "SSO", "status": "pass"},
            {"system_name": "Slack", "status": "pass"},
            {"system_name": "GitHub", "status": "pass"}
        ]}),
        Action(name="read_onboarding_file", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
        Action(name="render_onboarding_welcome", kwargs={"candidate_id": "cand_7", "candidate_name": "Robert Singh", "role_title": "Senior Software Engineer","start_date": "2024-09-02"}),
        Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/welcome_Robert_Singh.md","mime_type": "text/markdown"}),
        Action(name="generate_and_send_email", kwargs={
            "to_emails": ["robert.singh@example.com"],
            "subject": "Welcome to the Team",
            "candidate_id": "cand_7",
            "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf","/onboarding/Robert_Singh/welcome_Robert_Singh.md"]
        }),
        Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_7", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
    ],
    outputs=['"success_flag": true', '"candidate_id":"cand_7"', '"message_id":"msg_15"', '"status":"Packet Sent"'],
),
    Task(
        annotator="0",
        user_id="V4_Task_034",
        instruction=(
            "You operate on the existing asset request for peter.jones@example.com (start 2024-07-29). "
            "You send the 'Asset Provisioning – Peter Jones' email, store its message id on the request, apply the 'Asset-Request' label, "
            "allocate an available asset, write /onboarding/Peter_Jones/allocation_receipt.json, and send 'Asset Allocation – Peter Jones' with the receipt attached."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/asset_request.json",
                                                            "payload": {"request_id": "asset_req_2"}}),
            Action(name="generate_and_send_email",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Peter Jones", "candidate_id": "cand_3",
                           "attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_2"}),
            Action(name="write_onboarding_file",
                   kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/allocation_receipt.json", "mime_type": "application/json",
                           "payload": {"request_id": "asset_req_2", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="generate_and_send_email",
                   kwargs={"to_emails": ["peter.jones@example.com"], "subject": "Asset Allocation – Peter Jones", "candidate_id": "cand_3",
                           "attachment_file_paths": ["/onboarding/Peter_Jones/allocation_receipt.json"]}),
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_035",
        instruction=(
            "You send day-1 orientation and manager-intro invites for maria.rodriguez@example.com (start 2024-08-12), then send and label her provisioning email "
            "as Asset-Request and write an attachments audit."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="generate_and_send_email", kwargs={"task": "orientation_invite","to_emails": ["maria.rodriguez@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_4"}),
            Action(name="generate_and_send_email", kwargs={"task": "manager_intro","to_emails": ["maria.rodriguez@example.com", "david.kim@example.com"],"subject": "Manager Intro","candidate_id": "cand_4"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_4","orientation_invite_ts": "2025-09-01T00:00:00Z","manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_3"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_4","file_path": "/onboarding/Maria_Rodriguez/asset_request.json","payload": {"request_id": "asset_req_3"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Maria Rodriguez","candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_3","status": "Sent","email_message_id": "msg_17"}),
            Action(name="audit_attachments_for_email", kwargs={"candidate_id": "cand_4","subject": "Asset Provisioning – Maria Rodriguez"}),
        ],
        outputs=['"candidate_id":"cand_4"', "/onboarding/Maria_Rodriguez/attachments_audit.json"],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_036",
        instruction=(
            "You send and label a one-week onboarding checklist reminder for maria.rodriguez@example.com (cutoff 2024-08-19), "
            "mark pending items as reminded with the reminder email id, and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_4", "status": "Pending", "due_date_lte": "2024-08-19"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "checklist_reminder", "to_emails": ["maria.rodriguez@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_4",
                           "attachment_file_paths": ["/onboarding/Maria_Rodriguez/pending_tasks.md"]}),
            Action(name="get_or_create_email_label", kwargs={"name": "Onboarding-Reminder"}),
            Action(name="modify_email_labels",
                   kwargs={"candidate_id": "cand_4", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded", kwargs={"item_ids": ["item_9", "item_10"], "reminder_email_message_id": "msg_15"}),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_4", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_037",
        instruction=(
            "You personalize and send the onboarding packet for john.doe@example.com (start 2024-08-01) with policy/benefits attached, "
            "then send and label a one-week checklist reminder (cutoff 2024-08-08)."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "john.doe@example.com", "start_date": "2024-08-01"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_1","file_path": "/onboarding/John_Doe/welcome_John_Doe.md","mime_type": "text/markdown","content_text": " Welcome, John Doe!\n\nRole: Software Engineer\nStart date: 2024-08-01\n\nWe’re excited to have you on board. Please review the attached policy and benefits guides."}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["john.doe@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_1","attachment_file_paths": ["/library/Company-Policies.pdf","/library/Benefits-Guide.pdf","/onboarding/John_Doe/welcome_John_Doe.md"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_1","fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_1","file_path": "/onboarding/John_Doe/pending_tasks.md","due_date_lte": "2024-08-08"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["john.doe@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_1","attachment_file_paths": ["/onboarding/John_Doe/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_1","fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_1"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_038",
        instruction=(
            "You send a day-1 orientation invite for emily.chen@example.com (start 2024-08-26), then send and label a checklist reminder (cutoff 2024-09-01)."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "emily.chen@example.com", "start_date": "2024-08-26"}),
            Action(name="generate_and_send_email", kwargs={"task": "orientation_invite", "to_emails": ["emily.chen@example.com"], "subject": "Day-1 Orientation","candidate_id": "cand_6"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_6", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-01"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_6", "file_path": "/onboarding/Emily_Chen/pending_tasks.md"}),
            Action(name="generate_and_send_email", kwargs={"task": "checklist_reminder", "to_emails": ["emily.chen@example.com"], "subject": "Pending Onboarding Tasks","candidate_id": "cand_6","attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"]}),
            Action(name="modify_email_labels", kwargs={"candidate_id": "cand_6", "subject": "Pending Onboarding Tasks","add_names": ["Onboarding-Reminder"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_6", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_039",
        instruction=(
            "You verify day-1 access for the employee at maria.rodriguez@example.com (start 2024-08-12). You send orientation and "
            "manager-intro invites; you notify IT for any failures."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="record_access_checks", kwargs={"candidate_id": "cand_4", "checks": [{"system_name": "Email", "status": "pass"},
                                                                                             {"system_name": "SSO", "status": "pass"},
                                                                                             {"system_name": "Slack", "status": "pass"},
                                                                                             {"system_name": "VPN", "status": "fail"}]}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "orientation_invite", "to_emails": ["maria.rodriguez@example.com"], "subject": "Day-1 Orientation",
                           "candidate_id": "cand_4"}),
            Action(name="generate_and_send_email", kwargs={"task": "manager_intro", "to_emails": ["maria.rodriguez@example.com", "david.kim@example.com"],
                                               "subject": "Manager Intro", "candidate_id": "cand_4"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_4", "orientation_invite_ts": "2025-09-01T00:00:00Z",
                                                                      "manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "access_gaps", "to_emails": ["it-assets@example.com", "david.kim@example.com"], "subject": "Access Gaps",
                           "candidate_id": "cand_4"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_040",
        instruction=(
            "You verify day-1 access for the employee at john.doe@example.com (start 2024-08-01). "
            "You send orientation and manager-intro invites; you notify IT for any failures."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "john.doe@example.com", "start_date": "2024-08-01"}),
            Action(name="record_access_checks", kwargs={"candidate_id": "cand_1", "checks": [
                {"system_name": "Email", "status": "pass"},
                {"system_name": "SSO", "status": "pass"},
                {"system_name": "Slack", "status": "fail"},
                {"system_name": "GitHub", "status": "pass"}]}),
            Action(name="generate_and_send_email", kwargs={
                "task": "orientation_invite", "to_emails": ["john.doe@example.com"], "subject": "Day-1 Orientation", "candidate_id": "cand_1"}),
            Action(name="generate_and_send_email", kwargs={
                "task": "manager_intro", "to_emails": ["john.doe@example.com", "sarah.wilson@example.com"], "subject": "Manager Intro",
                "candidate_id": "cand_1"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_1", "orientation_invite_ts": "2025-09-01T00:00:00Z",
                                                                      "manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="generate_and_send_email", kwargs={
                "task": "access_gaps", "to_emails": ["it-assets@example.com"], "subject": "Access Gaps", "candidate_id": "cand_1"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_1"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_041",
        instruction=(
            "You send and label a one-week checklist reminder for maria.rodriguez@example.com (start 2024-08-12, cutoff 2024-08-19), "
            "mark the pending items as reminded with the reminder email id, and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_4", "status": "Pending", "due_date_lte": "2024-08-19"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "checklist_reminder", "to_emails": ["maria.rodriguez@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_4", "attachment_file_paths": ["/onboarding/Maria_Rodriguez/pending_tasks.md"]}),
            Action(name="modify_email_labels",
                   kwargs={"candidate_id": "cand_4", "subject": "Pending Onboarding Tasks", "add_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded",
                   kwargs={"item_ids": ["item_9", "item_10"], "reminder_email_message_id": "msg_15", "updated_ts": "2025-09-01T00:00:00Z"}),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_4", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_042",
        instruction=(
            "You record day-1 access checks for peter.jones@example.com (start 2024-07-29): Email=pass, SSO=pass, Slack=pass, GitHub=pass. "
            "Then you send a day-1 orientation invite and record the invite timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="record_access_checks", kwargs={"candidate_id": "cand_3", "checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "pass"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
            Action(name="generate_and_send_email", kwargs={"task": "orientation_invite","to_emails": ["peter.jones@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_3"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_3","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_043",
        instruction=(
            "You operate on the existing asset request for maria.rodriguez@example.com (start 2024-08-12): ensure the 'Asset-Request' label is "
            "present on the existing provisioning email (msg_9), update the request with that email_message_id and mark it Sent, allocate the first"
            " available asset, and audit the provisioning email’s attachments."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_3"}),
            Action(name="get_or_create_email_label", kwargs={"name": "Asset-Request"}),
            Action(name="modify_email_labels", kwargs={"message_id": "msg_9", "add_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={ "request_id": "asset_req_3", "status": "Sent", "email_message_id": "msg_9"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_3"}),
            Action(name="audit_attachments_for_email", kwargs={ "candidate_id": "cand_4", "subject": "Asset Provisioning – Maria Rodriguez"}),
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_044",
        instruction=(
            "You personalize and send the onboarding packet for alex.thompson@example.com (start 2024-08-19) with policy/benefits attached and "
            "then send a day-1 orientation invite, recording the required updates."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="read_onboarding_file", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md","mime_type": "text/markdown","content_text":" Welcome, Alex Thompson!\n\n""Role: DevOps Engineer\n""Start date: 2024-08-19\n\n"" Getting Started\n""- Review the attached Company Policies and Benefits Guide.\n""- Bring a valid photo ID for security badging.\n""- Your laptop pickup will be coordinated by IT on Day 1.\n\n"" Day 1 Agenda\n""- Orientation session\n""- Account setup (SSO, email, Slack)\n""- Team introductions\n\n""If you have any questions before your start date, reply to this email and HR will assist."}),
            Action(name="generate_and_send_email", kwargs={"task": "onboarding","to_emails": ["alex.thompson@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_5","attachment_file_paths": ["/library/Company-Policies.pdf","/library/Benefits-Guide.pdf","/onboarding/Alex_Thompson/welcome_Alex_Thompson.md"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_5","fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="generate_and_send_email", kwargs={"task": "orientation_invite","to_emails": ["alex.thompson@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_5"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_5","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_045",
        instruction=(
            "You send and label a one-week checklist reminder for robert.singh@example.com (start 2024-09-02, cutoff 2024-09-09), "
            "mark the pending items as reminded with the reminder email id, and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email":"robert.singh@example.com","start_date":"2024-09-02"}),
            Action(name="search_checklist_items", kwargs={"candidate_id":"cand_7","status":"Pending","due_date_lte":"2024-09-09"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id":"cand_7","file_path":"/onboarding/Robert_Singh/pending_tasks.md"}),
            Action(name="generate_and_send_email", kwargs={"task":"checklist_reminder","to_emails":["robert.singh@example.com"],"subject":"Pending Onboarding Tasks","candidate_id":"cand_7","attachment_file_paths":["/onboarding/Robert_Singh/pending_tasks.md"]}),
            Action(name="modify_email_labels", kwargs={"candidate_id":"cand_7","subject":"Pending Onboarding Tasks","add_names":["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded", kwargs={"item_ids":["item_15","item_16"],"reminder_email_message_id":"msg_15","updated_ts":"2025-09-01T00:00:00Z"}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id":"cand_7","fields":{"checklist_follow_up_ts_nullable":"2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_7"'],
    ),
    Task(
annotator="0",
user_id="V4_Task_046",
instruction=(
"You verify day-1 access for the employee at jane.smith@example.com (start 2024-08-05). You send an orientation invite and notify IT if any checks fail."
),
actions=[
Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
Action(name="record_access_checks", kwargs={"candidate_id": "cand_2", "checks": [
{"system_name": "Email", "status": "pass"},
{"system_name": "SSO", "status": "pass"},
{"system_name": "Slack", "status": "pass"},
{"system_name": "GitHub", "status": "pass"}
]}),
Action(name="generate_and_send_email", kwargs={
"to_emails": ["jane.smith@example.com"], "subject": "Day-1 Orientation", "candidate_id": "cand_2"
}),
Action(name="update_candidate_invite_timestamps", kwargs={
"candidate_id": "cand_2", "orientation_invite_ts": "2025-09-01T00:00:00Z", "message_id": "msg_15"
})
],
outputs=['"success_flag": true', '"candidate_id":"cand_2"'],
),
    Task(
        annotator="0",
        user_id="V4_Task_047",
        instruction=(
            "You record day-1 access checks for emily.chen@example.com (start 2024-08-26) on Email=pass, SSO=fail, Slack=pass, GitHub=pass; "
            "you send a day-1 orientation invite, then notify IT of access gaps."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "emily.chen@example.com", "start_date": "2024-08-26"}),
            Action(name="record_access_checks", kwargs={"candidate_id": "cand_6", "checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "fail"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["emily.chen@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_6"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_6","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Access Gaps","candidate_id": "cand_6"}),
        ],
        outputs=['"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_048",
        instruction=(
            "You record day-1 access checks for jane.smith@example.com (start 2024-08-05): Email=pass, SSO=fail, Slack=pass, GitHub=pass. "
            "You then send a day-1 orientation invite and record the invite timestamp, and notify IT of the access gaps."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="record_access_checks", kwargs={"candidate_id": "cand_2", "checks": [{"system_name": "Email", "status": "pass"},{"system_name": "SSO", "status": "fail"},{"system_name": "Slack", "status": "pass"},{"system_name": "GitHub", "status": "pass"}]}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["jane.smith@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_2"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_2","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Access Gaps","candidate_id": "cand_2"}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_049",
        instruction=(
            "You ensure the 'Asset-Request' label is present on 'Asset Provisioning – Peter Jones' for peter.jones@example.com (start 2024-07-29), "
            "update the existing request with the provisioning email id and write an attachments audit."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_2"}),
            Action(name="get_or_create_email_label", kwargs={"name": "Asset-Request"}),
            Action(name="modify_email_labels", kwargs={"message_id": "msg_4", "add_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_4"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/asset_request.json","payload": {"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_4"}}),Action(name="audit_attachments_for_email", kwargs={"candidate_id": "cand_3", "subject": "Asset Provisioning – Peter Jones"}),
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_050",
        instruction=(
            "You send day-1 orientation and manager-intro invites for maria.rodriguez@example.com (start 2024-08-12) and record both invite timestamps."),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="generate_and_send_email",kwargs={"task": "orientation_invite", "to_emails": ["maria.rodriguez@example.com"], "subject": "Day-1 Orientation","candidate_id": "cand_4"}),
            Action(name="generate_and_send_email",kwargs={"task": "manager_intro", "to_emails": ["maria.rodriguez@example.com", "david.kim@example.com"], "subject": "Manager Intro","candidate_id": "cand_4"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_4", "orientation_invite_ts": "2025-09-01T00:00:00Z","manager_intro_invite_ts": "2025-09-01T00:00:00Z"})
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_051",
        instruction=(
            "You ensure the asset request is reviewed and emailed for 'Asset Provisioning – Alex Thompson' for alex.thompson@example.com (start 2024-08-19), "
            "and allocate an available asset."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_4"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/asset_request.json","payload": {"request_id": "asset_req_4", "asset_type": "Laptop", "status": "Completed"}}),
            Action(name="generate_and_send_email",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Alex Thompson", "candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_4", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_4"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_4", "status": "allocated", "asset_tag": "LT-DELL-001","asset_type": "Laptop"}}),
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    
    

    Task(
        annotator="0",
        user_id="V4_Task_052",
        instruction=(
            "You complete Jane Smith’s provisioning by sending and labeling the request, allocating inventory and writing a receipt, "
            "and replying to the provisioning thread to acknowledge."),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_1"}),
            Action(name="write_asset_request_file", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/asset_request.json",
                "payload": {"request_id": "asset_req_1"}}),
            Action(name="generate_and_send_email", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Jane Smith",
                "candidate_id": "cand_2",
                "attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={
                "request_id": "asset_req_1",
                "status": "Sent",
                "email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_1"}),
            Action(name="write_asset_request_file", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/asset_request.json",
                "payload": {
                    "request_id": "asset_req_1",
                    "status": "Sent",
                    "email_message_id": "msg_15",
                    "inventory_checked_flag": True,
                    "asset_tag": "LT-DELL-001"}}),
            Action(name="write_onboarding_file", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_1", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="reply_to_email_thread", kwargs={
                "candidate_id": "cand_2",
                "thread_id": "msg_15",
                "subject": "Asset Provisioning – Jane Smith",
                "task": "acknowledge"
            }),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_053",
        instruction=(
            "You create and send an equipment provisioning request for the employee at john.doe@example.com "
            "with start date 2024-08-01. Use asset type Standard-Laptop, email it-assets@example.com, "
            "then mark the request as Sent and label the email Asset-Request."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "john.doe@example.com", "start_date": "2024-08-01"}),
            Action(name="create_asset_request", kwargs={"candidate_id": "cand_1", "asset_type": "Standard-Laptop", "status": "Requested"
                                                        }),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/asset_request.json",
                                                            "payload": {"candidate_name": "John Doe", "asset_type": "Standard-Laptop"}
                                                            }),
            Action(name="generate_and_send_email",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – John Doe", "candidate_id": "cand_1",
                           "attachment_file_paths": ["/onboarding/John_Doe/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status",
                   kwargs={"candidate_id": "cand_1", "asset_type": "Standard-Laptop", "status": "Sent", "email_message_id": "msg_15"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_1"', '"message_id":"msg_15"', '"request_status":"Sent"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_054",
        instruction=(
            "You create and send an equipment provisioning request for the employee at maria.rodriguez@example.com with start date 2024-08-12. "
            "You operate on the existing request, email it-assets@example.com, then mark the request as Sent and label the email Asset-Request."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_3"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                                                            "payload": {"request_id": "asset_req_3"}}),
            Action(name="generate_and_send_email",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Maria Rodriguez", "candidate_id": "cand_4",
                          "attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_3", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="modify_email_labels",
                   kwargs={"candidate_id": "cand_4", "subject": "Asset Provisioning – Maria Rodriguez",
                           "add_names": ["Asset-Request"]})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"', '"request_id":"asset_req_3"', '"request_status":"Sent"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_055",
        instruction=(
            "You create and send an equipment provisioning request for the employee at peter.jones@example.com with start date 2024-07-29. "
            "You operate on the existing request, email it-assets@example.com, then mark the request as Sent and label the email Asset-Request."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_2"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/asset_request.json",
                                                            "payload": {"request_id": "asset_req_2"}}),
            Action(name="generate_and_send_email",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Peter Jones", "candidate_id": "cand_3",
                          "attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"]}),
            Action(name="update_asset_request_status",
                   kwargs={"request_id": "asset_req_2", "status": "Sent", "candidate_id": "cand_3", "subject": "Asset Provisioning – Peter Jones",
                           }),
            Action(name="get_or_create_email_label", kwargs={"name": "Asset-Request"}),
            Action(name="modify_email_labels",
                   kwargs={"candidate_id": "cand_3", "subject": "Asset Provisioning – Peter Jones",
                           "add_names": ["Asset-Request"]})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_3"', '"request_id":"asset_req_2"', '"request_status":"Sent"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_056",
        instruction=(
            "You send a one-week onboarding checklist reminder for jane.smith@example.com (cutoff 2024-08-12), label it, "
            "mark pending items as reminded with the reminder email id, and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_2", "status": "Pending", "due_date_lte": "2024-08-12"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "checklist_reminder", "to_emails": ["jane.smith@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_2",
                           "attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"]}),
            Action(name="modify_email_labels",
                   kwargs={"candidate_id": "cand_2", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded",
                   kwargs={"item_ids": ["item_4", "item_5", "item_6", "item_7"], "reminder_email_message_id": "msg_15",
                           }),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_2", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_057",
        instruction=(
            "You send and label a one-week checklist reminder for robert.singh@example.com (start 2024-09-02, cutoff 2024-09-09), "
            "mark pending items as reminded with the reminder email id, record the follow-up timestamp, and close any completed items without timestamps."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_7", "status": "Pending", "due_date_lte": "2024-09-09"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "checklist_reminder", "to_emails": ["robert.singh@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_7",
                           "attachment_file_paths": ["/onboarding/Robert_Singh/pending_tasks.md"]}),
            Action(name="modify_email_labels",
                   kwargs={"candidate_id": "cand_7", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded",
                   kwargs={"item_ids": ["item_15", "item_16"], "reminder_email_message_id": "msg_15", }),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_7", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
            Action(name="close_completed_checklist_items", kwargs={"candidate_id": "cand_7", "due_date_lte": "2024-09-09"})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_7"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_058",
        instruction=(
            "You send and label a one-week checklist reminder for robert.singh@example.com (start 2024-09-02, cutoff 2024-09-09), "
            "mark pending items as reminded with the reminder email id, record the follow-up timestamp, and close any completed items without timestamps."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_7", "status": "Pending", "due_date_lte": "2024-09-09"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "checklist_reminder", "to_emails": ["robert.singh@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_7",
                           "attachment_file_paths": ["/onboarding/Robert_Singh/pending_tasks.md"], "label_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded",
                   kwargs={"item_ids": ["item_15", "item_16"], "reminder_email_message_id": "msg_15", }),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_7", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
            Action(name="close_completed_checklist_items", kwargs={"candidate_id": "cand_7", "due_date_lte": "2024-09-09"})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_7"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_059",
        instruction=(
            "You ensure the Asset-Request label is present on the previously sent provisioning email (message_id 'msg_4') for peter.jones@example.com (start 2024-07-29), "
            "and you update the existing asset request with that email id."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="update_asset_request_status",
                   kwargs={"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_4", }),
            Action(name="get_or_create_email_label", kwargs={"name": "Asset-Request"}),
            Action(name="modify_email_labels", kwargs={"message_id": "msg_4", "add_names": ["Asset-Request"]})
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_060",
        instruction=(
            "You send and label a one-week checklist reminder for peter.jones@example.com (start 2024-07-29, cutoff 2024-08-05) and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_3", "status": "Pending", "due_date_lte": "2024-08-05"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/pending_tasks.md"}),
            Action(name="generate_and_send_email", kwargs={"task": "checklist_reminder", "to_emails": ["peter.jones@example.com"],"subject": "Pending Onboarding Tasks", "candidate_id": "cand_3",  "attachment_file_paths": ["/onboarding/Peter_Jones/pending_tasks.md"]}),
            Action(name="modify_email_labels", kwargs={"candidate_id": "cand_3", "subject": "Pending Onboarding Tasks",  "add_names": ["Onboarding-Reminder"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_3", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_061",
        instruction=(
            "You finalize equipment provisioning for maria.rodriguez@example.com (start 2024-08-12) per policy: prepare the request artifact "
            "and email IT using 'Asset Provisioning – Maria Rodriguez' with the required 'Asset-Request' label; record the email id and mark the "
            "request Sent; allocate the first available inventory and record the allocation receipt."

        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_3"}),
            Action(name="write_asset_request_file", kwargs={
                "candidate_id": "cand_4",
                "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                "payload": {"request_id": "asset_req_3", "asset_type": "Laptop", "status": "Pending"}}),
            Action(name="generate_and_send_email", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Maria Rodriguez",
                "candidate_id": "cand_4",
                "attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={
                "request_id": "asset_req_3",
                "status": "Sent",
                "email_message_id": "msg_15" }),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_3"}),
            Action(name="write_onboarding_file", kwargs={
                "candidate_id": "cand_4",
                "file_path": "/onboarding/Maria_Rodriguez/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_3", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="write_asset_request_file", kwargs={
                "candidate_id": "cand_4",
                "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                "payload": {
                    "request_id": "asset_req_3",
                    "status": "Sent",
                    "email_message_id": "msg_15",
                    "inventory_checked_flag": True,
                    "asset_tag": "LT-DELL-001"}}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"', '"request_id":"asset_req_3"', '"allocation_status":"allocated"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_062",
        instruction=(
            "You create and send an equipment provisioning request for the employee at john.doe@example.com "
            "with start date 2024-08-01. Use asset type Standard-Laptop, email it-assets@example.com, "
            "then mark the request as Sent and label the email Asset-Request."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "john.doe@example.com", "start_date": "2024-08-01"}),
            Action(name="create_asset_request", kwargs={"candidate_id": "cand_1", "asset_type": "Standard-Laptop", "status": "Requested"
                                                        }),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/asset_request.json",
                                                            "payload": {"candidate_name": "John Doe", "asset_type": "Standard-Laptop"}
                                                            }),
            Action(name="generate_and_send_email",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – John Doe", "candidate_id": "cand_1",
                           "attachment_file_paths": ["/onboarding/John_Doe/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status",
                   kwargs={"candidate_id": "cand_1", "asset_type": "Standard-Laptop", "status": "Sent", "email_message_id": "msg_15"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_1"', '"message_id":"msg_15"', '"request_status":"Sent"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_063",
        instruction=(
            "You complete the equipment provisioning for the employee at robert.singh@example.com (start 2024-09-02) by operating on the existing "
            "request and allocating inventory. You send the provisioning email, store its message id on the request, label the email Asset-Request, "
            "allocate the first available tag for the requested type, and write an allocation receipt to the database."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
            Action(name="write_asset_request_file", kwargs={
                "candidate_id": "cand_7",
                "file_path": "/onboarding/Robert_Singh/asset_request.json",
                "payload": {"request_id": "asset_req_5"}}),
            Action(name="generate_and_send_email", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Robert Singh",
                "candidate_id": "cand_7",
                "attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={
                "request_id": "asset_req_5",
                "status": "Sent",
                "email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_5"}),
            Action(name="write_onboarding_file", kwargs={
                "candidate_id": "cand_7",
                "file_path": "/onboarding/Robert_Singh/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_5", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="write_asset_request_file", kwargs={
                "candidate_id": "cand_7",
                "file_path": "/onboarding/Robert_Singh/asset_request.json",
                "payload": {
                    "request_id": "asset_req_5",
                    "status": "Sent",
                    "email_message_id": "msg_15",
                    "inventory_checked_flag": True,
                    "asset_tag": "LT-DELL-001"}}),
            Action(name="update_asset_request_status", kwargs={
                "request_id": "asset_req_5",
                "status": "Completed",
                "email_message_id": "msg_15"}),
        ],
        outputs=['"candidate_id":"cand_7"', '"request_id":"asset_req_5"', '"status":"Completed"'],

    ),

    Task(
        annotator="0",
        user_id="V4_Task_064",
        instruction=(
            "You finalize equipment provisioning for peter.jones@example.com (start 2024-07-29) in accordance with the Equipment Provisioning policy: "
            "prepare the request artifact, email IT using the fixed subject 'Asset Provisioning – Peter Jones' with the required 'Asset-Request' label, "
            "record the provisioning email id and mark the request Sent, allocate the first available inventory, and record an allocation receipt."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="write_asset_request_file", kwargs={
                "candidate_id": "cand_3",
                "file_path": "/onboarding/Peter_Jones/asset_request.json",
                "payload": {"request_id": "asset_req_2"}}),
            Action(name="generate_and_send_email", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Peter Jones",
                "candidate_id": "cand_3",
                "attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={
                "request_id": "asset_req_2",
                "status": "Sent",
                "email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_2"}),
            Action(name="write_onboarding_file", kwargs={
                "candidate_id": "cand_3",
                "file_path": "/onboarding/Peter_Jones/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_2", "asset_tag": "LT-DELL-001"}}),
        ],
        outputs=['"candidate_id":"cand_3"', '"request_id":"asset_req_2"', '"status":"Sent"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_065",
        instruction=(
            "You close completed checklist items for alex.thompson@example.com (start 2024-08-19), then send and label a checklist reminder "
            "(cutoff 2024-08-26) and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="close_completed_checklist_items", kwargs={"candidate_id": "cand_5", "due_date_lte": "2024-08-26"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/pending_tasks.md", "due_date_lte": "2024-08-26"}),
            Action(name="generate_and_send_email", kwargs={"task": "checklist_reminder","to_emails": ["alex.thompson@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded", kwargs={"item_ids": ["item_13", "item_14"], "reminder_email_message_id": "msg_15"}),
            Action(name="update_candidate_status_fields",kwargs={"candidate_id": "cand_5", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_066",
        instruction=(
            "You send the 'Asset Provisioning – Maria Rodriguez' email for maria.rodriguez@example.com (start 2024-08-12), "
            "store its message id on the request, and apply the 'Asset-Request' label."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_3"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/asset_request.json","payload": {"request_id": "asset_req_3"}}),
            Action(name="generate_and_send_email",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Maria Rodriguez", "candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_3", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/asset_request.json","payload": {"request_id": "asset_req_3", "status": "Sent","email_message_id": "msg_15"}}),
        ],
        outputs=['"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_067",
        instruction=(
            "You operate on the existing asset request for maria.rodriguez@example.com (start 2024-08-12). You prepare the request and email IT "
            "using 'Asset Provisioning – Maria Rodriguez' with the required 'Asset-Request' label; record the email id and mark the request Sent; "
            "allocate the first available inventory and write /onboarding/Maria_Rodriguez/allocation_receipt.json; then send an allocation confirmation "
            "email to maria.rodriguez@example.com with subject 'Asset Allocation – Maria Rodriguez' attaching the receipt."

        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/asset_request.json",
                                                            "payload": {"request_id": "asset_req_3"}}),
            Action(name="generate_and_send_email",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Maria Rodriguez", "candidate_id": "cand_4",
                           "attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_3", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_3"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/allocation_receipt.json",
                                                         "mime_type": "application/json",
                                                         "payload": {"request_id": "asset_req_3", "status": "allocated", "asset_tag": "LT-DELL-001",
                                                                     "asset_type": "Laptop"}}),
            Action(name="generate_and_send_email",
                   kwargs={"to_emails": ["maria.rodriguez@example.com"], "subject": "Asset Allocation – Maria Rodriguez", "candidate_id": "cand_4",
                           "attachment_file_paths": ["/onboarding/Maria_Rodriguez/allocation_receipt.json"]}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),
 Task(
        annotator="0",
        user_id="V4_Task_068",
        instruction=(
            "You finalize equipment provisioning for peter.jones@example.com (start 2024-07-29) per the Equipment Provisioning policy: "
            "prepare the request artifact, email IT using 'Asset Provisioning – Peter Jones' with the JSON attached and the required 'Asset-Request' label; "
            "record the email id and mark the request Sent; allocate the first available inventory and record the allocation; write an allocation receipt and "
            "send the employee a confirmation with the receipt (subject 'Equipment Allocation Receipt')."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_3","file_path": "/onboarding/Peter_Jones/asset_request.json","payload": {"request_id": "asset_req_2", "asset_type": "Laptop", "status": "Requested"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Peter Jones","candidate_id": "cand_3","attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_2","status": "Sent","email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_2"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_3","file_path": "/onboarding/Peter_Jones/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_2", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["peter.jones@example.com"],"subject": "Equipment Allocation Receipt","candidate_id": "cand_3","attachment_file_paths": ["/onboarding/Peter_Jones/allocation_receipt.json"]}),
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_069",
        instruction=(
            "You send and label a one-week checklist reminder for alex.thompson@example.com (start 2024-08-19, cutoff 2024-08-26), "
            "mark the pending items as reminded with the reminder email id, and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email":"alex.thompson@example.com","start_date":"2024-08-19"}),
            Action(name="search_checklist_items", kwargs={"candidate_id":"cand_5","status":"Pending","due_date_lte":"2024-08-26"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id":"cand_5","file_path":"/onboarding/Alex_Thompson/pending_tasks.md"}),
            Action(name="generate_and_send_email", kwargs={"task":"checklist_reminder","to_emails":["alex.thompson@example.com"],"subject":"Pending Onboarding Tasks","candidate_id":"cand_5","attachment_file_paths":["/onboarding/Alex_Thompson/pending_tasks.md"]}),
            Action(name="modify_email_labels", kwargs={"candidate_id":"cand_5","subject":"Pending Onboarding Tasks","add_names":["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded", kwargs={"item_ids":["item_13","item_14"],"reminder_email_message_id":"msg_15","updated_ts":"2025-09-01T00:00:00Z"}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id":"cand_5","fields":{"checklist_follow_up_ts_nullable":"2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_070",
        instruction=(
            "You send and label a one-week checklist reminder for jane.smith@example.com (start 2024-08-05, cutoff 2024-08-12), "
            "mark the pending items as reminded with the reminder email id, and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_2", "status": "Pending", "due_date_lte": "2024-08-12"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "checklist_reminder", "to_emails": ["jane.smith@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_2", "attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"]}),
            Action(name="modify_email_labels",
                   kwargs={"candidate_id": "cand_2", "subject": "Pending Onboarding Tasks", "add_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded",
                   kwargs={"item_ids": ["item_4", "item_5", "item_6", "item_7"], "reminder_email_message_id": "msg_15",
                           "updated_ts": "2025-09-01T00:00:00Z"}),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_2", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_071",
        instruction=(
            "You create and send an equipment provisioning request for the employee at robert.singh@example.com with start date 2024-09-02. "
            "You operate on the existing request, email it-assets@example.com, then mark the request as Sent and label the email Asset-Request."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_5"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/asset_request.json",
                                                            "payload": {"request_id": "asset_req_5"}}),
            Action(name="generate_and_send_email",
                   kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Robert Singh", "candidate_id": "cand_7",
                           "attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"]}),
            Action(name="update_asset_request_status",
                   kwargs={"request_id": "asset_req_5", "status": "Sent", "candidate_id": "cand_7", "subject": "Asset Provisioning – Robert Singh",
                           }),
            Action(name="modify_email_labels", kwargs={"message_id": "msg_15", "add_names": ["Asset-Request"]})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_7"', '"request_id":"asset_req_5"', '"request_status":"Sent"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_072",
        instruction=(
            "You create and send a basic onboarding packet for the employee at john.doe@example.com with start date 2024-08-01. "
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "john.doe@example.com", "start_date": "2024-08-01"}),
            Action(name="read_onboarding_file", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="render_onboarding_welcome",
                   kwargs={"candidate_id": "cand_1", "candidate_name": "John Doe", "role_title": "Software Engineer", "start_date": "2024-08-01"}),
            Action(name="write_onboarding_file",
                   kwargs={"candidate_id": "cand_1", "file_path": "/onboarding/John_Doe/welcome_John_Doe.md", "mime_type": "text/markdown"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["john.doe@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_1",
                                               "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf",
                                                                         "/onboarding/John_Doe/welcome_John_Doe.md"]}),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_1", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_1"', '"message_id":"msg_15"', '"status":"Packet Sent"'],
    ),
    Task(
    annotator="0",
    user_id="V4_Task_073",
    instruction=(
        "You verify day-1 access for robert.singh@example.com (start 2024-09-02), personalize and send the 'Welcome to the Team' packet "
        "(attach Company-Policies.pdf, Benefits-Guide.pdf, and the personalized markdown), and store the welcome email id."
    ),
    actions=[
        Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
        Action(name="record_access_checks", kwargs={"candidate_id": "cand_7", "checks": [
            {"system_name": "Email", "status": "pass"},
            {"system_name": "SSO", "status": "pass"},
            {"system_name": "Slack", "status": "pass"},
            {"system_name": "GitHub", "status": "pass"}
        ]}),
        Action(name="read_onboarding_file", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
        Action(name="render_onboarding_welcome", kwargs={"candidate_id": "cand_7", "candidate_name": "Robert Singh", "role_title": "Senior Software Engineer","start_date": "2024-09-02"}),
        Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/welcome_Robert_Singh.md","mime_type": "text/markdown"}),
        Action(name="generate_and_send_email", kwargs={
            "to_emails": ["robert.singh@example.com"],
            "subject": "Welcome to the Team",
            "candidate_id": "cand_7",
            "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf","/onboarding/Robert_Singh/welcome_Robert_Singh.md"]
        }),
        Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_7", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}})
    ],
    outputs=['"success_flag": true', '"candidate_id":"cand_7"', '"message_id":"msg_15"', '"status":"Packet Sent"'],
),
 Task(
        annotator="0",
        user_id="V4_Task_074",
        instruction=(
            "You send the 'Asset Provisioning – Jane Smith' email for jane.smith@example.com (start 2024-08-05), store its message id on the request, "
            "and apply the 'Asset-Request' label."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_1"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/asset_request.json","payload": {"request_id": "asset_req_1"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Jane Smith","candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_1","status": "Sent","email_message_id": "msg_15"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/asset_request.json","payload": {"request_id": "asset_req_1", "status": "Sent", "email_message_id": "msg_15"}}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_075",
        instruction=(
            "You ensure the 'Asset-Request' is completed on 'Asset Provisioning – Peter Jones' for peter.jones@example.com (start 2024-07-29) "
            "and reply to the provisioning thread to acknowledge."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_3","file_path": "/onboarding/Peter_Jones/asset_request.json","payload": {"request_id": "asset_req_2"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Peter Jones","candidate_id": "cand_3","attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_2","status": "Sent","email_message_id": "msg_15"}),
            Action(name="reply_to_email_thread", kwargs={"candidate_id": "cand_3","thread_id": "msg_15","subject": "Asset Provisioning – Peter Jones","task": "acknowledge"}),
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    

    Task(
        annotator="0",
        user_id="V4_Task_076",
        instruction=(
            "You operate on the existing asset request for alex.thompson@example.com (start 2024-08-19). "
            "You send the 'Asset Provisioning – Alex Thompson' email with the request JSON attached, store its message id on the request, "
            "apply the 'Asset-Request' label, allocate an available asset, and write /onboarding/Alex_Thompson/allocation_receipt.json."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/asset_request.json","payload": {"request_id": "asset_req_4"}}),
            Action(name="generate_and_send_email",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Alex Thompson", "candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_4", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_4"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_4", "status": "allocated", "asset_tag": "LT-DELL-001","asset_type": "Laptop"}}),
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_077",
        instruction=(
            "You operate on the existing asset request for jane.smith@example.com (start 2024-08-05). "
            "You send the 'Asset Provisioning – Jane Smith' email, store its message id on the request, apply the 'Asset-Request' label, "
            "allocate an available asset, and write /onboarding/Jane_Smith/allocation_receipt.json."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_1"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/asset_request.json","payload": {"request_id": "asset_req_1"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Jane Smith","candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_1","status": "Sent","email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_1"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_1", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_078",
        instruction=(
            "You operate on the existing asset request for peter.jones@example.com (start 2024-07-29). "
            "You send the 'Asset Provisioning – Peter Jones' email, store its message id on the request, apply the 'Asset-Request' label, "
            "and write /onboarding/Peter_Jones/allocation_receipt.json."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/asset_request.json","payload": {"request_id": "asset_req_2"}}),
            Action(name="generate_and_send_email",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Peter Jones", "candidate_id": "cand_3","attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"], "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="write_onboarding_file",kwargs={"candidate_id": "cand_3", "file_path": "/onboarding/Peter_Jones/allocation_receipt.json", "mime_type": "application/json","payload": {"request_id": "asset_req_2"}}),
        ],
        outputs=['"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_079",
        instruction=(
            "You operate on the existing asset request for robert.singh@example.com (start 2024-09-02). "
            "You send the 'Asset Provisioning – Robert Singh' email, store its message id on the request, apply the 'Asset-Request' label, "
            "allocate an available asset, write /onboarding/Robert_Singh/allocation_receipt.json, and send the 'Asset Allocation – Robert Singh' confirmation with the receipt attached."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/asset_request.json","payload": {"request_id": "asset_req_5"}}),
            Action(name="generate_and_send_email",kwargs={"to_emails": ["it-assets@example.com"], "subject": "Asset Provisioning – Robert Singh", "candidate_id": "cand_7","attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"], "label_names": ["Asset-Request"],"date_ts": "2025-09-01T00:00:00Z"}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_5", "status": "Sent", "email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_5"}),
            Action(name="write_onboarding_file",kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/allocation_receipt.json", "mime_type": "application/json","payload": {"request_id": "asset_req_5", "status": "allocated", "asset_tag": "LT-DELL-001", "asset_type": "Laptop"}}),
            Action(name="generate_and_send_email",kwargs={"to_emails": ["robert.singh@example.com"], "subject": "Asset Allocation – Robert Singh", "candidate_id": "cand_7","attachment_file_paths": ["/onboarding/Robert_Singh/allocation_receipt.json"]}),
        ],
        outputs=['"candidate_id":"cand_7"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_080",
        instruction=(
            "You verify day-1 access for the employee at alex.thompson@example.com (start 2024-08-19). You send an orientation invite and notify IT if any checks fail."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="record_access_checks", kwargs={"candidate_id": "cand_5", "checks": [{"system_name": "Email", "status": "pass"},
                                                                                             {"system_name": "SSO", "status": "fail"},
                                                                                             {"system_name": "Slack", "status": "pass"},
                                                                                             {"system_name": "GitHub", "status": "pass"}]}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "orientation_invite", "to_emails": ["alex.thompson@example.com"], "subject": "Day-1 Orientation",
                           "candidate_id": "cand_5"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_5", "orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "access_gaps", "to_emails": ["it-assets@example.com"], "subject": "Access Gaps", "candidate_id": "cand_5"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_5"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_081",
        instruction=(
            "You send a one-week onboarding checklist reminder for the employee at jane.smith@example.com (cutoff 2024-08-12). "
            "You attach the pending tasks summary, label the email, record the follow-up timestamp, and mark pending items as reminded."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_2", "status": "Pending", "due_date_lte": "2024-08-12"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "checklist_reminder", "to_emails": ["jane.smith@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_2",
                           "attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"]}),
            Action(name="modify_email_labels",
                   kwargs={"candidate_id": "cand_2", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded",
                   kwargs={"item_ids": ["item_4", "item_5","item_6", "item_7"], "reminder_email_message_id": "msg_15", }),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_2", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"candidate_id":"cand_2"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_082",
        instruction=(
            "You send a one-week onboarding checklist reminder for the employee at alex.thompson@example.com (cutoff 2024-08-26). "
            "You attach the pending tasks summary, label the email, record the follow-up timestamp, and mark pending items as reminded."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_5", "file_path": "/onboarding/Alex_Thompson/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "checklist_reminder", "to_emails": ["alex.thompson@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_5", "attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"]}),
            Action(name="get_or_create_email_label", kwargs={"name": "Onboarding-Reminder"}),
            Action(name="modify_email_labels",
                   kwargs={"candidate_id": "cand_5", "subject": "Pending Onboarding Tasks",
                           "add_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded",
                   kwargs={"item_ids": ["item_13", "item_14"], "reminder_email_message_id": "msg_15", }),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_5", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_5"'],
    ),
Task(
        annotator="0",
        user_id="V4_Task_083",
        instruction=(
            "You manage checklist follow‑up for jane.smith@example.com (start 2024-08-05) using the existing asset request as context. "
            "Apply the one‑week cutoff (2024-08-12) to determine pending items and deliver a 'Pending Onboarding Tasks' email to the candidate labeled 'Onboarding-Reminder' with the generated pending_tasks.md. "
            "Update records to reflect the reminder: set checklist_follow_up_ts to 2025-09-01T00:00:00Z and mark the affected items as reminded, storing message_id msg_15."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_1"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_2", "status": "Pending", "due_date_lte": "2024-08-12"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/pending_tasks.md"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["jane.smith@example.com"], "subject": "Pending Onboarding Tasks", "candidate_id": "cand_2", "attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"], "label_names": ["Onboarding-Reminder"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_2", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
            Action(name="mark_checklist_items_reminded", kwargs={"item_ids": ["item_4", "item_5", "item_6", "item_7"], "reminder_email_message_id": "msg_15", "updated_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"', '"request_id":"asset_req_1"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_084",
        instruction=(
            "You complete the equipment provisioning for the employee at peter.jones@example.com (start 2024-07-29) by operating on the existing request. "
            "You send the provisioning email, store its message id on the request, label the email Asset-Request, and write an allocation receipt to the database."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_2"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_3",
                "file_path": "/onboarding/Peter_Jones/asset_request.json",
                "payload": {"request_id": "asset_req_2"}}),
            Action(name="generate_and_send_email", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Peter Jones",
                "candidate_id": "cand_3",
                "attachment_file_paths": ["/onboarding/Peter_Jones/asset_request.json"],
                "label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={
                "request_id": "asset_req_2",
                "status": "Sent",
                "email_message_id": "msg_15"}),
            Action(name="write_asset_request_file", kwargs={
                "candidate_id": "cand_3",
                "file_path": "/onboarding/Peter_Jones/asset_request.json",
                "payload": {"request_id": "asset_req_2", "status": "Sent", "email_message_id": "msg_15"}}),
            Action(name="write_onboarding_file", kwargs={
                "candidate_id": "cand_3",
                "file_path": "/onboarding/Peter_Jones/allocation_receipt.json",
                "mime_type": "application/json",
                "payload": {"request_id": "asset_req_2"}}),
        ]
        ,
        outputs=['"candidate_id":"cand_3"', '"request_id":"asset_req_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_085",
        instruction=(
            "You send a one-week onboarding checklist reminder for the employee at robert.singh@example.com start date 2024-09-02. "
            "You attach the pending tasks summary, label the email, record the follow-up timestamp, and mark pending items as reminded."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_7", "status": "Pending", "due_date_lte": "2024-09-09"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_7", "file_path": "/onboarding/Robert_Singh/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "checklist_reminder", "to_emails": ["robert.singh@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_7",
                           "attachment_file_paths": ["/onboarding/Robert_Singh/pending_tasks.md"]}),
            Action(name="modify_email_labels", kwargs={"message_id": "msg_15", "add_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded",
                   kwargs={"item_ids": ["item_15", "item_16"], "reminder_email_message_id": "msg_15", }),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_7", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_7"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_086",
        instruction=(
            "You create and send a basic onboarding packet for the employee at jane.smith@example.com with start date 2024-08-05. "
            "You personalize the onboarding template, attach standard docs, send the email, then set status to 'Packet Sent' and store the welcome email id."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="read_onboarding_file", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="render_onboarding_welcome",
                   kwargs={"candidate_id": "cand_2", "candidate_name": "Jane Smith", "role_title": "Product Manager", "start_date": "2024-08-05"}),

            Action(name="write_onboarding_file",
                   kwargs={"candidate_id": "cand_2", "file_path": "/onboarding/Jane_Smith/welcome_Jane_Smith.md", "mime_type": "text/markdown"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "onboarding", "to_emails": ["jane.smith@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_2",
                           "attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf",
                                                     "/onboarding/Jane_Smith/welcome_Jane_Smith.md"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_2", "fields": {"onboarding_status": "Packet Sent",
                                                                                                       "welcome_email_message_id_nullable": "msg_15"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"', '"status":"Packet Sent"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_087",
        instruction=(
            "You record day-1 access checks for peter.jones@example.com (start 2024-07-29): Email=pass, SSO=pass, Slack=fail, GitHub=pass. "
            "Then you send a day-1 orientation invite, record the invite timestamp as 2025-09-01T00:00:00Z, and notify IT of the access gaps."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "peter.jones@example.com", "start_date": "2024-07-29"}),
            Action(name="record_access_checks", kwargs={"candidate_id": "cand_3", "checks": [{"system_name": "Email",  "status": "pass"},{"system_name": "SSO",    "status": "pass"},{"system_name": "Slack",  "status": "fail"},{"system_name": "GitHub", "status": "pass"},]}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["peter.jones@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_3"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_3","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Access Gaps","candidate_id": "cand_3"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_3"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_088",
        instruction=(
            "You create and send an equipment provisioning request for the employee at jane.smith@example.com with start date 2024-08-05. "
            "You operate on the existing request, email it-assets@example.com, then mark the request as Sent and label the email Asset-Request."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_1"}),
            Action(name="write_asset_request_file", kwargs={
                "candidate_id": "cand_2",
                "file_path": "/onboarding/Jane_Smith/asset_request.json",
                "payload": {"request_id": "asset_req_1", "candidate_id": "cand_2", "status": "Completed"}}),
            Action(name="generate_and_send_email", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Jane Smith",
                "candidate_id": "cand_2",
                "attachment_file_paths": ["/onboarding/Jane_Smith/asset_request.json"]}),
            Action(name="update_asset_request_status", kwargs={
                "request_id": "asset_req_1", "status": "Sent", "email_message_id": "msg_15", }),
            Action(name="modify_email_labels", kwargs={
                "candidate_id": "cand_2", "subject": "Asset Provisioning – Jane Smith",
                "add_names": ["Asset-Request"]})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"', '"request_id":"asset_req_1"', '"request_status":"Sent"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_089",
        instruction=(
            "You create and send an equipment provisioning request for the employee at alex.thompson@example.com with start date 2024-08-19. "
            "You operate on the existing request, email it-assets@example.com, then mark the request as Sent and label the email Asset-Request."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_4"}),
            Action(name="write_asset_request_file", kwargs={
                "candidate_id": "cand_5",
                "file_path": "/onboarding/Alex_Thompson/asset_request.json",
                "payload": {"request_id": "asset_req_4", "candidate_id": "cand_5", "status": "Completed"}}),
            Action(name="generate_and_send_email", kwargs={
                "to_emails": ["it-assets@example.com"],
                "subject": "Asset Provisioning – Alex Thompson",
                "candidate_id": "cand_5",
                "attachment_file_paths": ["/onboarding/Alex_Thompson/asset_request.json"]}),
            Action(name="update_asset_request_status", kwargs={
                "request_id": "asset_req_4", "status": "Sent", "email_message_id": "msg_15", }),
            Action(name="modify_email_labels", kwargs={
                "candidate_id": "cand_5", "subject": "Asset Provisioning – Alex Thompson","add_names": ["Asset-Request"]})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_5"', '"request_id":"asset_req_4"', '"request_status":"Sent"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_090",
        instruction=(
            "You personalize and send the onboarding packet for emily.chen@example.com (start 2024-08-26) with policy/benefits attached, "
            "then send a day-1 orientation invite and record the invite timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "emily.chen@example.com", "start_date": "2024-08-26"}),
            Action(name="read_onboarding_file", kwargs={"file_path": "/onboarding/templates/Welcome-Email-Template.md"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_6","file_path": "/onboarding/Emily_Chen/welcome_Emily_Chen.md","mime_type": "text/markdown"}),
            Action(name="generate_and_send_email",kwargs={"task": "onboarding", "to_emails": ["emily.chen@example.com"], "subject": "Welcome to the Team", "candidate_id": "cand_6","attachment_file_paths": ["/library/Company-Policies.pdf", "/library/Benefits-Guide.pdf","/onboarding/Emily_Chen/welcome_Emily_Chen.md"]}),
            Action(name="update_candidate_status_fields",kwargs={"candidate_id": "cand_6", "fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="generate_and_send_email", kwargs={"task": "orientation_invite", "to_emails": ["emily.chen@example.com"], "subject": "Day-1 Orientation","candidate_id": "cand_6"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_6", "orientation_invite_ts": "2025-09-01T00:00:00Z"})
        ],
        outputs=['"candidate_id":"cand_6"'],
    ),
Task(
        annotator="0",
        user_id="V4_Task_091",
        instruction=(
            "You verify day-1 access for john.doe@example.com (start 2024-08-01): record checks (all pass), send a day-1 orientation invite, and record the invite timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "john.doe@example.com", "start_date": "2024-08-01"}),
            Action(name="record_access_checks", kwargs={"candidate_id": "cand_1", "checks": [{"system_name": "Email",  "status": "pass"},{"system_name": "SSO",    "status": "pass"},{"system_name": "Slack",  "status": "pass"},{"system_name": "GitHub", "status": "pass"},]}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["john.doe@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_1"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_1","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_1"'],
    ),

    Task(
        annotator="0",
        user_id="V4_Task_092",
        instruction=(
            "You complete provisioning for maria.rodriguez@example.com (start 2024-08-12) by sending and labeling the request, "
            "allocating inventory and writing a receipt to /onboarding/Maria_Rodriguez/allocation_receipt.json, and sending an "
            "allocation confirmation email with subject 'Asset Allocation – Maria Rodriguez'."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_3"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_4","file_path": "/onboarding/Maria_Rodriguez/asset_request.json","payload": {"request_id": "asset_req_3"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Maria Rodriguez","candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_3","status": "Sent","email_message_id": "msg_15"}),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_3"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_4","file_path": "/onboarding/Maria_Rodriguez/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_3", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["maria.rodriguez@example.com"],"subject": "Asset Allocation – Maria Rodriguez","candidate_id": "cand_4","attachment_file_paths": ["/onboarding/Maria_Rodriguez/allocation_receipt.json"]}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_093",
        instruction=(
            "You perform a one-week checklist follow-up for alex.thompson@example.com (start 2024-08-19) in line with the checklist policy: "
            "prepare the pending-tasks artifact for items due by 2024-08-26, send a labeled reminder to the employee, mark those items as reminded using the reminder email’s id, "
            "and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_5", "status": "Pending", "due_date_lte": "2024-08-26"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/pending_tasks.md","due_date_lte": "2024-08-26"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["alex.thompson@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded", kwargs={"item_ids": ["item_13", "item_14"],"reminder_email_message_id": "msg_15"}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_5","fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_5"', '"reminder_message_id":"msg_15"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_094",
        instruction=(
            "You operate on the existing asset request for robert.singh@example.com (start 2024-09-02): send the 'Asset Provisioning – Robert Singh' email, "
            "store its message id on the request, and apply the 'Asset-Request' label."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_5"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_7","file_path": "/onboarding/Robert_Singh/asset_request.json","payload": {"request_id": "asset_req_5"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Robert Singh","candidate_id": "cand_7","attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_5","status": "Sent","email_message_id": "msg_15"}),
        ],
        outputs=['"candidate_id":"cand_7"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_095",
        instruction=(
            "You close completed checklist items for emily.chen@example.com (start 2024-08-26), then send and label a checklist reminder"
            " with cutoff 2024-09-02 and record the follow-up timestamp."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "emily.chen@example.com", "start_date": "2024-08-26"}),
            Action(name="close_completed_checklist_items", kwargs={"candidate_id": "cand_6", "due_date_lte": "2024-09-02"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_6", "status": "Pending", "due_date_lte": "2024-09-02"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_6","file_path": "/onboarding/Emily_Chen/pending_tasks.md","due_date_lte": "2024-09-02"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["emily.chen@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_6","attachment_file_paths": ["/onboarding/Emily_Chen/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_6","fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_6"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_096",
        instruction=(
            "You write an access summary for jane.smith@example.com (start 2024-08-05), send an orientation invite, then send and label a "
            "one-week checklist reminder with cutoff 2024-08-12 and ensure the label is present."),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "jane.smith@example.com", "start_date": "2024-08-05"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/access_summary.md","mime_type": "text/markdown","content_text": " Access Summary (Day 1)\n\nCandidate: Jane Smith\nStart date: 2024-08-05\n"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["jane.smith@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_2"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_2","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_2","file_path": "/onboarding/Jane_Smith/pending_tasks.md","due_date_lte": "2024-08-12"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["jane.smith@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_2","attachment_file_paths": ["/onboarding/Jane_Smith/pending_tasks.md"],"label_names": ["Onboarding-Reminder"]}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_2","status": "Pending","due_date_lte": "2024-08-12"}),
            Action(name="mark_checklist_items_reminded", kwargs={"item_ids": ["item_4", "item_5", "item_6", "item_7"],"reminder_email_message_id": "msg_16"}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_2","fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_2"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_097",
        instruction=(
            "You send day-1 orientation and manager-intro invites for robert.singh@example.com (start 2024-09-02). "
            "You then send the provisioning email and ensure the Asset-Request label is applied."),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["robert.singh@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_7"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["robert.singh@example.com", "sarah.wilson@example.com"],"subject": "Manager Intro","candidate_id": "cand_7"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_7","orientation_invite_ts": "2025-09-01T00:00:00Z","manager_intro_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_7","file_path": "/onboarding/Robert_Singh/asset_request.json","payload": {"request_id": "asset_req_5"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Robert Singh","candidate_id": "cand_7","attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"],"label_names": ["Asset-Request"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_5","status": "Sent","email_message_id": "msg_17"}),
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_7"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_098",
        instruction=(
            "You send a one-week onboarding checklist reminder for the employee at maria.rodriguez@example.com (cutoff 2024-08-19). "
            "You attach the pending tasks summary, label the email, record the follow-up timestamp, and mark pending items as reminded."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "maria.rodriguez@example.com", "start_date": "2024-08-12"}),
            Action(name="search_checklist_items", kwargs={"candidate_id": "cand_4", "status": "Pending", "due_date_lte": "2024-08-19"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_4", "file_path": "/onboarding/Maria_Rodriguez/pending_tasks.md"}),
            Action(name="generate_and_send_email",
                   kwargs={"task": "checklist_reminder", "to_emails": ["maria.rodriguez@example.com"], "subject": "Pending Onboarding Tasks",
                           "candidate_id": "cand_4",
                           "attachment_file_paths": ["/onboarding/Maria_Rodriguez/pending_tasks.md"]}),
            Action(name="get_or_create_email_label", kwargs={"name": "Onboarding-Reminder"}),
            Action(name="modify_email_labels", kwargs={"message_id": "msg_15", "add_names": ["Onboarding-Reminder"]}),
            Action(name="mark_checklist_items_reminded",
                   kwargs={"item_ids": ["item_9", "item_10"], "reminder_email_message_id": "msg_15", }),
            Action(name="update_candidate_status_fields",
                   kwargs={"candidate_id": "cand_4", "fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}})
        ],
        outputs=['"success_flag": true', '"candidate_id":"cand_4"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_099",
        instruction=(
            "You send the onboarding packet for alex.thompson@example.com (start 2024-08-19), send an orientation invite, "
            "then send and label a one-week checklist reminder (cutoff 2024-08-26)."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "alex.thompson@example.com", "start_date": "2024-08-19"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/welcome_Alex_Thompson.md","mime_type": "text/markdown","content_text": " Welcome, Alex Thompson!\n\nRole: DevOps Engineer\nStart date: 2024-08-19\n\nPlease review the attached policy and benefits guides."}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["alex.thompson@example.com"],"subject": "Welcome to the Team","candidate_id": "cand_5","attachment_file_paths": ["/library/Company-Policies.pdf","/library/Benefits-Guide.pdf","/onboarding/Alex_Thompson/welcome_Alex_Thompson.md"]}),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_5","fields": {"onboarding_status": "Packet Sent", "welcome_email_message_id_nullable": "msg_15"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["alex.thompson@example.com"],"subject": "Day-1 Orientation","candidate_id": "cand_5"}),
            Action(name="update_candidate_invite_timestamps", kwargs={"candidate_id": "cand_5","orientation_invite_ts": "2025-09-01T00:00:00Z"}),
            Action(name="write_pending_tasks_file", kwargs={"candidate_id": "cand_5","file_path": "/onboarding/Alex_Thompson/pending_tasks.md","due_date_lte": "2024-08-26"}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["alex.thompson@example.com"],"subject": "Pending Onboarding Tasks","candidate_id": "cand_5","attachment_file_paths": ["/onboarding/Alex_Thompson/pending_tasks.md"],"label_names": ["Onboarding-Reminder"] }),
            Action(name="update_candidate_status_fields", kwargs={"candidate_id": "cand_5","fields": {"checklist_follow_up_ts_nullable": "2025-09-01T00:00:00Z"}}),
        ],
        outputs=['"candidate_id":"cand_5"'],
    ),
    Task(
        annotator="0",
        user_id="V4_Task_100",
        instruction=(
            "You finish provisioning for robert.singh@example.com (start 2024-09-02) by sending the 'Asset Provisioning – Robert Singh' email with the request JSON attached, "
            "storing its message id on the request, applying the 'Asset-Request' label, allocating inventory, and writing /onboarding/Robert_Singh/allocation_receipt.json."
        ),
        actions=[
            Action(name="find_candidate_by_email", kwargs={"candidate_email": "robert.singh@example.com", "start_date": "2024-09-02"}),
            Action(name="read_asset_request", kwargs={"request_id": "asset_req_5"}),
            Action(name="write_asset_request_file", kwargs={"candidate_id": "cand_7","file_path": "/onboarding/Robert_Singh/asset_request.json","payload": {"request_id": "asset_req_5", "candidate_id": "cand_7"}}),
            Action(name="generate_and_send_email", kwargs={"to_emails": ["it-assets@example.com"],"subject": "Asset Provisioning – Robert Singh","candidate_id": "cand_7","label_names": ["Asset-Request"],"attachment_file_paths": ["/onboarding/Robert_Singh/asset_request.json"]}),
            Action(name="update_asset_request_status", kwargs={"request_id": "asset_req_5","status": "Sent","email_message_id": "msg_15" }),
            Action(name="allocate_first_available_asset", kwargs={"request_id": "asset_req_5"}),
            Action(name="write_onboarding_file", kwargs={"candidate_id": "cand_7","file_path": "/onboarding/Robert_Singh/allocation_receipt.json","mime_type": "application/json","payload": {"request_id": "asset_req_5", "status": "allocated", "asset_tag": "LT-DELL-001"}}),
        ],
        outputs=['"candidate_id":"cand_7"'],
    ),
]